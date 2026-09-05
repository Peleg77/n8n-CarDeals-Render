"""Stage 1: load Noga MCP price exports into a standard schema.

Noga (www.noga-iso.co.il/trade/mcp/) is a JS-driven query form with no
network access from this environment (egress to the domain is blocked),
so this pipeline does NOT scrape live. Instead it parses files the user
exports manually from the site's "ייצוא נתונים לאקסל" (export to Excel)
button, or any CSV/XLSX with the same four columns, dropped into
``data/raw/``.

Expected raw columns (Hebrew, order not assumed):
    תאריך                          -> date
    שעה                            -> hour_label (1-24, or 1-23 / 1-25 on DST transition days)
    מחיר יום מראש (₪/MWh)          -> price_da_nis_mwh   (Day-Ahead)
    מחיר זמן אמת עתידי (₪/MWh)     -> price_rt_nis_mwh   (Real-Time)

Column names are matched by keyword, not exact string, since exports from
different date ranges / site versions may vary slightly.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

RAW_SCHEMA_COLUMNS = ["date_raw", "hour_label", "price_da_nis_mwh", "price_rt_nis_mwh", "source_file"]

_DATE_KEYWORDS = ["תאריך", "date"]
_HOUR_KEYWORDS = ["שעה", "hour"]
_DA_KEYWORDS = ["יום מראש", "day-ahead", "day ahead", "da"]
_RT_KEYWORDS = ["זמן אמת", "real-time", "real time", "rt"]


def _match_column(columns: list[str], keywords: list[str]) -> str | None:
    """Return the first column whose lowercased name contains any keyword."""
    for col in columns:
        low = str(col).strip().lower()
        for kw in keywords:
            if kw.lower() in low:
                return col
    return None


def _canonicalize_columns(df: pd.DataFrame, source_file: str) -> pd.DataFrame:
    cols = list(df.columns)
    date_col = _match_column(cols, _DATE_KEYWORDS)
    hour_col = _match_column(cols, _HOUR_KEYWORDS)
    da_col = _match_column(cols, _DA_KEYWORDS)
    rt_col = _match_column(cols, _RT_KEYWORDS)

    missing = [
        name
        for name, col in [("date", date_col), ("hour", hour_col), ("day-ahead price", da_col), ("real-time price", rt_col)]
        if col is None
    ]
    if missing:
        raise ValueError(
            f"{source_file}: could not find columns for {missing}. "
            f"Found columns: {cols}. Update the keyword lists in loader.py "
            "if Noga's export uses different headers."
        )

    out = pd.DataFrame(
        {
            "date_raw": df[date_col],
            "hour_label": df[hour_col],
            "price_da_nis_mwh": pd.to_numeric(df[da_col], errors="coerce"),
            "price_rt_nis_mwh": pd.to_numeric(df[rt_col], errors="coerce"),
        }
    )
    out["source_file"] = source_file
    return out


def load_raw_file(path: Path) -> pd.DataFrame:
    """Read one Noga export (csv/xlsx) and return it in the canonical raw schema.

    Does not parse timestamps or touch timezone/DST logic — that is
    validate.build_timestamps's job, since it needs to see the full
    monthly window to detect duplicate/missing hours from DST transitions.
    """
    path = Path(path)
    if path.suffix.lower() in {".xlsx", ".xls"}:
        df = pd.read_excel(path, dtype=str)
    elif path.suffix.lower() == ".csv":
        df = pd.read_csv(path, dtype=str, encoding="utf-8-sig")
    else:
        raise ValueError(f"Unsupported file type: {path}")
    return _canonicalize_columns(df, path.name)


def load_all_raw(raw_dir: Path) -> pd.DataFrame:
    """Load and concatenate every export file in raw_dir, sorted by filename.

    Sorting by filename (not by parsed date) is deliberate: files are named
    by fetch window (e.g. mcp_2025-05.csv, mcp_2025-06.csv) so filename
    order is chronological without needing to parse dates first.
    """
    raw_dir = Path(raw_dir)
    files = sorted(
        [p for p in raw_dir.iterdir() if p.suffix.lower() in {".xlsx", ".xls", ".csv"} and not p.name.startswith(".")]
    )
    if not files:
        raise FileNotFoundError(
            f"No export files found in {raw_dir}. Export monthly windows from "
            "https://www.noga-iso.co.il/trade/mcp/ (or place equivalent CSV/XLSX "
            "files with the same 4 columns) and drop them here before running Stage 1."
        )
    frames = [load_raw_file(p) for p in files]
    combined = pd.concat(frames, ignore_index=True)
    return combined[RAW_SCHEMA_COLUMNS]
