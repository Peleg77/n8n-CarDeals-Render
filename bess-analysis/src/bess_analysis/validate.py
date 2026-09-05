"""Stage 2: timestamp construction (DST-aware) + data quality validation.

Convention assumed for the ``hour_label`` column (documented in
outputs/assumptions.md as unverified against a real Noga export, since
this pipeline currently runs on user-supplied files rather than a live
fetch): hour label N represents the interval [N-1:00, N:00) local time,
i.e. label 1 = 00:00-01:00 ... label 24 = 23:00-24:00. On the spring
DST-forward day, Israel skips the local hour 02:00-03:00, so that day is
assumed to have 23 rows with the corresponding label simply absent (not
23 consecutively-numbered labels). On the autumn DST-fallback day, the
local hour 01:00-02:00 occurs twice, so that day is assumed to have 25
rows with one label value repeated twice (first occurrence = summer
time/DST, second = standard time). If real Noga exports use a different
convention, the completeness/duplicate counts below will surface it
immediately (unexpected nonexistent-time or leftover-ambiguous rows).
"""

from __future__ import annotations

import pandas as pd

DISCLAIMER = """\
> **הבהרה חשובה (מקור: נגה — מנהל המערכת):** המחירים במאגר זה הם
> **סימולטיביים**. אין התחייבות לחישוב או לפרסום יומי סדיר, המתווה
> וכללי החישוב עשויים להשתנות בהתאם להחלטות רשות החשמל, וייתכנו סטיות
> בין הערכים המתפרסמים לבין החישוב הרשמי — "בעיקר במקרי קצה". הניתוח
> שלהלן מבוסס על נתונים אלה כפי שפורסמו, ואינו מהווה ייעוץ השקעות.
"""

TZ = "Asia/Jerusalem"


def _parse_date(date_raw: pd.Series) -> pd.Series:
    parsed = pd.to_datetime(date_raw, dayfirst=True, errors="coerce")
    if parsed.isna().any():
        bad = date_raw[parsed.isna()].unique()[:10]
        raise ValueError(f"Unparseable date values (sample): {list(bad)}")
    return parsed.dt.normalize()


def _parse_hour_offset(hour_label: pd.Series) -> pd.Series:
    """Extract an integer hour label (1-25) from raw hour column values.

    Handles plain integers ("1", "24") and range strings ("00:00-01:00")
    by taking the value / the start-of-range hour + 1.
    """
    s = hour_label.astype(str).str.strip()
    numeric = pd.to_numeric(s, errors="coerce")

    def _from_range(v: str) -> float:
        if ":" not in v:
            return float("nan")
        start = v.split("-")[0].strip()
        try:
            h = int(start.split(":")[0])
            return h + 1
        except (ValueError, IndexError):
            return float("nan")

    needs_range_parse = numeric.isna()
    if needs_range_parse.any():
        numeric = numeric.copy()
        numeric.loc[needs_range_parse] = s.loc[needs_range_parse].map(_from_range)

    if numeric.isna().any():
        bad = hour_label[numeric.isna()].unique()[:10]
        raise ValueError(f"Unparseable hour label values (sample): {list(bad)}")
    return numeric.astype(int)


def build_timestamps(raw: pd.DataFrame) -> pd.DataFrame:
    """Attach a tz-aware ``timestamp`` column (Asia/Jerusalem) to raw rows.

    Returns raw plus: date (normalized, naive), hour_offset (1-25),
    timestamp (tz-aware start-of-hour), and a `dst_flag` column
    ('normal' / 'spring_forward_day' / 'fall_back_day') per source row,
    based on how many distinct hour labels each calendar date has.
    """
    df = raw.copy()
    df["date"] = _parse_date(df["date_raw"])
    df["hour_offset"] = _parse_hour_offset(df["hour_label"])
    df["naive_local"] = df["date"] + pd.to_timedelta(df["hour_offset"] - 1, unit="h")

    counts = df.groupby("date")["hour_offset"].transform("size")
    df["dst_flag"] = "normal"
    df.loc[counts == 23, "dst_flag"] = "spring_forward_day"
    df.loc[counts == 25, "dst_flag"] = "fall_back_day"

    is_dup = df.duplicated(subset=["date", "hour_offset"], keep=False)
    ambiguous = pd.Series(False, index=df.index)
    if is_dup.any():
        first_of_pair = ~df.duplicated(subset=["date", "hour_offset"], keep="first")
        ambiguous = is_dup & first_of_pair

    timestamps = []
    nonexistent_count = 0
    for idx, row in df.iterrows():
        naive = row["naive_local"]
        try:
            if is_dup.loc[idx]:
                ts = naive.tz_localize(TZ, ambiguous=bool(ambiguous.loc[idx]))
            else:
                ts = naive.tz_localize(TZ, nonexistent="raise")
        except pytz_nonexistent_errors():
            nonexistent_count += 1
            ts = naive.tz_localize(TZ, nonexistent="shift_forward")
        except Exception:
            ts = pd.NaT
        timestamps.append(ts)
    df["timestamp"] = timestamps
    df.attrs["nonexistent_local_time_count"] = nonexistent_count
    return df


def pytz_nonexistent_errors():
    import pytz

    return (pytz.exceptions.NonExistentTimeError,)


def completeness_report(df: pd.DataFrame) -> dict:
    """Summarize missing hours, partial days, and DST-day handling."""
    full_range = pd.date_range(df["timestamp"].min(), df["timestamp"].max(), freq="h", tz=TZ)
    present = pd.DatetimeIndex(df["timestamp"].dropna().sort_values().unique())
    missing = full_range.difference(present)

    by_day = df.groupby("date").size()
    expected_by_day = df.groupby("date")["dst_flag"].first().map(
        {"normal": 24, "spring_forward_day": 23, "fall_back_day": 25}
    )
    partial_days = by_day[by_day != expected_by_day]

    return {
        "expected_hours": len(full_range),
        "present_hours": len(present),
        "missing_hours": len(missing),
        "missing_timestamps": missing,
        "partial_days": partial_days,
        "spring_forward_days": sorted(df.loc[df["dst_flag"] == "spring_forward_day", "date"].dt.date.unique().tolist()),
        "fall_back_days": sorted(df.loc[df["dst_flag"] == "fall_back_day", "date"].dt.date.unique().tolist()),
        "nonexistent_local_time_count": df.attrs.get("nonexistent_local_time_count", 0),
    }


def duplicate_report(df: pd.DataFrame) -> pd.DataFrame:
    """Fully-identical rows (same timestamp AND same prices) — true duplicates."""
    dupe_mask = df.duplicated(subset=["timestamp", "price_da_nis_mwh", "price_rt_nis_mwh"], keep="first")
    return df.loc[dupe_mask]


def flag_outliers(df: pd.DataFrame, extreme_threshold_nis_mwh: float = 1500.0) -> pd.DataFrame:
    """Add boolean flag columns; never drops rows — outliers are the signal."""
    out = df.copy()
    for col in ["price_da_nis_mwh", "price_rt_nis_mwh"]:
        out[f"{col}_is_null"] = out[col].isna()
        out[f"{col}_is_negative"] = out[col] < 0
        out[f"{col}_is_zero"] = out[col] == 0
        out[f"{col}_is_extreme"] = out[col] > extreme_threshold_nis_mwh
    return out


def unit_sanity_check(df: pd.DataFrame) -> dict:
    """Sanity check that values look like NIS/MWh (tens-hundreds), not NIS/kWh.

    1 NIS/MWh = 0.1 agorot/kWh. Typical Israeli MCP values are on the order
    of tens to low-hundreds of NIS/MWh; if the median were < 5 that would
    suggest the column is actually already in NIS/kWh (off by 1000x).
    """
    med_da = df["price_da_nis_mwh"].median()
    med_rt = df["price_rt_nis_mwh"].median()
    suspect = (med_da is not None and med_da < 5) or (med_rt is not None and med_rt < 5)
    return {
        "median_da_nis_mwh": med_da,
        "median_rt_nis_mwh": med_rt,
        "agorot_per_kwh_conversion_factor": 0.1,
        "suspected_unit_mismatch": bool(suspect),
    }
