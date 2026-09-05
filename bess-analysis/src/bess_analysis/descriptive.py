"""Stage 3: descriptive analysis of DA/RT price series.

Every function takes a price column name (`price_da_nis_mwh` or
`price_rt_nis_mwh`) so the same code runs on both series independently,
per the spec's requirement to analyze them separately and compare.

Clock hour (0-23) is derived as `hour_offset - 1`, per the convention
documented in validate.py (hour_offset N = interval [N-1:00, N:00)).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

SEASON_MAP = {
    12: "winter", 1: "winter", 2: "winter",
    6: "summer", 7: "summer", 8: "summer", 9: "summer",
    3: "transition", 4: "transition", 5: "transition",
    10: "transition", 11: "transition",
}

PERCENTILES = [1, 5, 25, 50, 75, 95, 99, 99.9]
HOUR_THRESHOLDS_NIS_MWH = [500, 800, 1000, 1200]
SPREAD_THRESHOLDS_NIS_MWH = [200, 300, 360, 400, 450]


def add_season_and_clock_hour(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["clock_hour"] = out["hour_offset"] - 1
    out["month"] = out["date"].dt.month
    out["season"] = out["month"].map(SEASON_MAP)
    return out


def hourly_profile(df: pd.DataFrame, price_col: str) -> pd.DataFrame:
    """Mean/median price per (season, clock_hour)."""
    d = add_season_and_clock_hour(df)
    return (
        d.groupby(["season", "clock_hour"])[price_col]
        .agg(mean="mean", median="median")
        .reset_index()
    )


def heatmap_matrix(df: pd.DataFrame, price_col: str) -> pd.DataFrame:
    """Hour (0-23, rows) x month (1-12, cols) mean price matrix for the heatmap chart."""
    d = add_season_and_clock_hour(df)
    pivot = d.pivot_table(index="clock_hour", columns="month", values=price_col, aggfunc="mean")
    return pivot.reindex(index=range(24), columns=range(1, 13))


def typical_min_max_hour(df: pd.DataFrame, price_col: str) -> pd.DataFrame:
    """Typical (mean-based) minimum and maximum hour of day, per season."""
    profile = hourly_profile(df, price_col)
    rows = []
    for season, g in profile.groupby("season"):
        min_row = g.loc[g["mean"].idxmin()]
        max_row = g.loc[g["mean"].idxmax()]
        rows.append(
            {
                "season": season,
                "min_hour": int(min_row["clock_hour"]),
                "min_level_nis_mwh": float(min_row["mean"]),
                "max_hour": int(max_row["clock_hour"]),
                "max_level_nis_mwh": float(max_row["mean"]),
            }
        )
    return pd.DataFrame(rows)


def percentile_table(df: pd.DataFrame, price_col: str) -> pd.Series:
    s = df[price_col].dropna()
    result = s.quantile([p / 100 for p in PERCENTILES])
    result.index = [f"p{p}" for p in PERCENTILES]
    result["max"] = s.max()
    return result


def midday_median(df: pd.DataFrame, price_col: str, start_hour: int = 10, end_hour: int = 15) -> float:
    """Median price over clock hours [start_hour, end_hour) — default 10:00-15:00."""
    d = add_season_and_clock_hour(df)
    mask = (d["clock_hour"] >= start_hour) & (d["clock_hour"] < end_hour)
    return float(d.loc[mask, price_col].median())


def hours_above_thresholds_per_year(df: pd.DataFrame, price_col: str, thresholds: list[float] = HOUR_THRESHOLDS_NIS_MWH) -> pd.Series:
    n_days = df["date"].nunique()
    years = n_days / 365.25 if n_days else np.nan
    counts = {f">{t}": (df[price_col] > t).sum() / years for t in thresholds}
    return pd.Series(counts)


def daily_spread(df: pd.DataFrame, price_col: str) -> pd.DataFrame:
    """Per-day spread_max (hourly max-min) and spread_4h (avg top4 - avg bottom4)."""
    rows = []
    for date, g in df.groupby("date"):
        prices = g[price_col].dropna().to_numpy()
        if len(prices) < 8:
            continue
        sorted_p = np.sort(prices)
        spread_max = sorted_p[-1] - sorted_p[0]
        spread_4h = sorted_p[-4:].mean() - sorted_p[:4].mean()
        rows.append({"date": date, "spread_max": spread_max, "spread_4h": spread_4h})
    return pd.DataFrame(rows)


def spread_distribution(daily: pd.DataFrame, col: str = "spread_4h") -> pd.Series:
    s = daily[col].dropna()
    stats = {
        "mean": s.mean(),
        "median": s.median(),
    }
    for p in PERCENTILES:
        stats[f"p{p}"] = s.quantile(p / 100)
    return pd.Series(stats)


def days_above_spread_thresholds(daily: pd.DataFrame, col: str = "spread_4h", thresholds: list[float] = SPREAD_THRESHOLDS_NIS_MWH) -> pd.Series:
    return pd.Series({f">{t}": int((daily[col] > t).sum()) for t in thresholds})


def spread_trend(daily: pd.DataFrame, col: str = "spread_4h") -> dict:
    """Simple linear trend of spread_4h over time (NIS/MWh per year)."""
    d = daily.dropna(subset=[col]).sort_values("date")
    if len(d) < 2:
        return {"slope_nis_mwh_per_year": np.nan, "n_days": len(d)}
    x = (d["date"] - d["date"].min()).dt.days.to_numpy(dtype=float)
    y = d[col].to_numpy(dtype=float)
    slope_per_day, intercept = np.polyfit(x, y, 1)
    return {"slope_nis_mwh_per_year": float(slope_per_day * 365.25), "n_days": len(d)}


def concentration_analysis(daily: pd.DataFrame, col: str = "spread_4h") -> dict:
    """Share of total (positive) daily value coming from the top-N days."""
    s = daily[col].clip(lower=0).sort_values(ascending=False)
    total = s.sum()
    if total <= 0:
        return {"total": 0.0, "top10_pct": 0.0, "top20_pct": 0.0, "top50_pct": 0.0}
    return {
        "total": float(total),
        "top10_pct": float(s.iloc[:10].sum() / total * 100),
        "top20_pct": float(s.iloc[:20].sum() / total * 100),
        "top50_pct": float(s.iloc[:50].sum() / total * 100),
    }


def da_vs_rt_diff(df: pd.DataFrame) -> pd.Series:
    """Distribution of (RT - DA) per hour — execution-risk indicator."""
    diff = (df["price_rt_nis_mwh"] - df["price_da_nis_mwh"]).dropna()
    stats = {"mean": diff.mean(), "median": diff.median(), "std": diff.std()}
    for p in PERCENTILES:
        stats[f"p{p}"] = diff.quantile(p / 100)
    return pd.Series(stats)
