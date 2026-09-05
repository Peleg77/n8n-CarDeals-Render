#!/usr/bin/env python3
"""Generate SIMULATED Noga-format MCP price exports for pipeline testing.

These are NOT real prices. They are a hand-built approximation of what
Israeli MCP prices plausibly look like, based on public knowledge of the
Israeli grid rather than any real Noga data (which this environment
cannot fetch — see README.md). Used only to prove the pipeline (loader ->
validate -> descriptive -> dispatch -> financial -> sensitivity -> report)
runs correctly end-to-end. Every real report generated from this data
must (and does, via --label) carry a "SIMULATED DATA" banner.

Modeled dynamics (documented so it's clear these are guesses, not data):
  - Duck-curve shape: solar suppresses midday prices, demand peaks in
    the evening after sunset.
  - Midday suppression is deepest in spring/autumn (high solar, moderate
    demand) and shallower in winter (weak solar) — and strengthens over
    the simulated period to reflect Israel's fast-growing PV fleet,
    occasionally pushing midday prices to zero/negative.
  - Summer evening peaks are the highest of the year (AC load persisting
    after sunset) and occur later in the evening than winter's peak.
  - Friday/Saturday (the Israeli weekend) demand — and price — is lower.
  - A small number of "scarcity" days (heat waves, cold snaps) get a
    multiplicative price spike concentrated in evening hours, to produce
    the kind of tail risk / revenue concentration real merchant BESS
    projects are exposed to.
  - Real-Time = Day-Ahead + heteroscedastic noise (larger during spikes),
    approximating forecast/execution risk.
  - The two real DST transition days in the simulated window (2025-10-26
    fall-back, 2026-03-27 spring-forward) are generated with 25 and 23
    hourly rows respectively, per the hour-label convention documented in
    validate.py, specifically to exercise that code path.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

OUT_DIR = Path(__file__).parent / "data_raw"
START = pd.Timestamp("2025-05-28")
END = pd.Timestamp("2026-09-05")
FALL_BACK_2025 = pd.Timestamp("2025-10-26")
SPRING_FORWARD_2026 = pd.Timestamp("2026-03-27")

SEED = 20250528


def season_params(month: int) -> dict:
    if month in (12, 1, 2):
        return dict(night=45.0, midday=48.0, evening_level=140.0, evening_hour=18.0, evening_width=2.0, morning_bump=15.0)
    if month in (6, 7, 8, 9):
        return dict(night=55.0, midday=22.0, evening_level=230.0, evening_hour=20.0, evening_width=2.6, morning_bump=0.0)
    return dict(night=35.0, midday=6.0, evening_level=115.0, evening_hour=19.0, evening_width=2.2, morning_bump=5.0)


def hour_labels_for_date(date: pd.Timestamp) -> list[int]:
    if date == SPRING_FORWARD_2026:
        return [1, 2] + list(range(4, 25))  # skip label 3 (02:00-03:00 doesn't exist)
    if date == FALL_BACK_2025:
        return [1, 2, 2] + list(range(3, 25))  # label 2 (01:00-02:00) occurs twice
    return list(range(1, 25))


def da_price_for_hour(date: pd.Timestamp, clock_hour: int, rng: np.random.Generator, solar_growth: float) -> float:
    p = season_params(date.month)
    midday_level = p["midday"] / solar_growth
    is_weekend = date.dayofweek in (4, 5)  # Friday, Saturday

    price = p["night"]
    price += (p["evening_level"] - p["night"]) * np.exp(-((clock_hour - p["evening_hour"]) ** 2) / (2 * p["evening_width"] ** 2))
    price -= (p["night"] - midday_level) * np.exp(-((clock_hour - 13) ** 2) / (2 * 3.5**2))
    price += p["morning_bump"] * np.exp(-((clock_hour - 7) ** 2) / (2 * 1.5**2))

    if is_weekend:
        price = price * 0.82 if price > 0 else price * 1.1

    price += rng.normal(0, 3.5 + 0.04 * abs(price))
    return price


def apply_scarcity_spikes(daily_df: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    """A handful of days per year get a multiplicative evening-hour spike,
    concentrating annual value in a small number of days (a real merchant-
    risk feature this simulation deliberately reproduces)."""
    out = daily_df.copy()
    is_summer = out["month"].isin([6, 7, 8])
    is_winter = out["month"].isin([12, 1, 2])
    spike_prob = np.where(is_summer, 0.035, np.where(is_winter, 0.015, 0.005))
    is_spike_day = rng.random(len(out)) < spike_prob
    out["is_spike_day"] = is_spike_day
    evening_mask = out["clock_hour"].between(17, 22)
    spike_mult = rng.uniform(2.5, 5.5, len(out))
    out.loc[is_spike_day & evening_mask, "price_da_nis_mwh"] *= spike_mult[is_spike_day & evening_mask]
    return out


def apply_negative_price_events(daily_df: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    """Occasional midday oversupply events (high solar + low weekend
    demand in shoulder months) push a few hours negative."""
    out = daily_df.copy()
    is_shoulder = out["month"].isin([3, 4, 5, 10, 11])
    is_weekend = out["dayofweek"].isin([4, 5])
    midday = out["clock_hour"].between(11, 14)
    candidate = is_shoulder & is_weekend & midday
    event_prob = 0.12
    is_event = candidate & (rng.random(len(out)) < event_prob)
    out.loc[is_event, "price_da_nis_mwh"] = -rng.uniform(2, 25, is_event.sum())
    return out


def build() -> pd.DataFrame:
    rng = np.random.default_rng(SEED)
    total_days = (END - START).days
    rows = []
    for day_idx, date in enumerate(pd.date_range(START, END, freq="D")):
        solar_growth = 1.0 + 0.6 * (day_idx / total_days)  # PV fleet grows ~60% notional over the window
        for hour_label in hour_labels_for_date(date):
            clock_hour = hour_label - 1
            da = da_price_for_hour(date, clock_hour, rng, solar_growth)
            rows.append(
                {
                    "date": date,
                    "month": date.month,
                    "dayofweek": date.dayofweek,
                    "hour_label": hour_label,
                    "clock_hour": clock_hour,
                    "price_da_nis_mwh": da,
                }
            )
    df = pd.DataFrame(rows)
    df = apply_scarcity_spikes(df, rng)
    df = apply_negative_price_events(df, rng)

    rt_noise_scale = 5.0 + 0.06 * df["price_da_nis_mwh"].abs() + np.where(df["is_spike_day"], 15.0, 0.0)
    df["price_rt_nis_mwh"] = df["price_da_nis_mwh"] + rng.normal(0, rt_noise_scale)

    df["price_da_nis_mwh"] = df["price_da_nis_mwh"].round(2)
    df["price_rt_nis_mwh"] = df["price_rt_nis_mwh"].round(2)
    return df


def write_monthly_csvs(df: pd.DataFrame) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for f in OUT_DIR.glob("*.csv"):
        f.unlink()
    for period, g in df.groupby(df["date"].dt.to_period("M")):
        out = pd.DataFrame(
            {
                "תאריך": g["date"].dt.strftime("%d/%m/%Y"),
                "שעה": g["hour_label"],
                "מחיר יום מראש (₪/MWh)": g["price_da_nis_mwh"],
                "מחיר זמן אמת עתידי (₪/MWh)": g["price_rt_nis_mwh"],
            }
        )
        out.to_csv(OUT_DIR / f"mcp_{period}.csv", index=False, encoding="utf-8-sig")
    print(f"Wrote {df['date'].dt.to_period('M').nunique()} monthly files, {len(df)} rows, to {OUT_DIR}")


if __name__ == "__main__":
    write_monthly_csvs(build())
