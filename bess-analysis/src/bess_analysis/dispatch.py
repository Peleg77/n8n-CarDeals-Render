"""Stage 4: day-by-day battery dispatch heuristic (no averaged-spread shortcut).

Heuristic (per spec), generalized from the 1 MW / 4 MWh base case to
arbitrary duration D (hours) and power P=1 MW:

    charge_hours    = D cheapest hours of the day
    discharge_hours = D most expensive hours of the day
    energy in       = P * D MWh, cost = P * sum(price at charge_hours)
    energy out      = rte * P * D MWh, revenue = rte * P * sum(price at discharge_hours)
    daily profit    = rte * P * sum(price at discharge_hours) - P * sum(price at charge_hours)

Constraint: every discharge hour must occur after every charge hour within
the same day (you cannot sell energy before you've bought it). If that
ordering is violated, or if profit would be negative, the unit does not
cycle that day (profit = 0, cycle not counted) — this is a same-day
buy-low-sell-high heuristic, not a lookahead/rolling optimizer.

Two-cycles-per-day variant: the day is split into two contiguous halves
by array position (first half / second half of the day's hours), and the
single-cycle heuristic above is applied independently to each half, with
profits summed. This is a simplifying choice (documented in
outputs/assumptions.md) — the spec asks to "try" 2 cycles/day without
prescribing an exact algorithm for splitting the day.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd


@dataclass
class DayDispatchResult:
    date: object
    profit_nis: float
    cycled: bool
    charge_hours: list[int] = field(default_factory=list)
    discharge_hours: list[int] = field(default_factory=list)


def _single_cycle(prices: np.ndarray, hour_index: np.ndarray, power_mw: float, duration_hours: int, rte: float) -> tuple[float, bool, list[int], list[int]]:
    """Apply the base one-cycle heuristic to a slice of a day's prices.

    `prices` and `hour_index` must be aligned (same order); hour_index
    carries the true hour-of-day so ordering can be checked correctly
    even when this is called on a sub-slice (2-cycle variant).
    """
    n = len(prices)
    d = min(duration_hours, n // 2)
    if d <= 0:
        return 0.0, False, [], []

    order = np.argsort(prices, kind="stable")
    cheap_idx = order[:d]
    expensive_idx = order[-d:]

    charge_hours = sorted(hour_index[cheap_idx].tolist())
    discharge_hours = sorted(hour_index[expensive_idx].tolist())

    if max(charge_hours) >= min(discharge_hours):
        return 0.0, False, [], []

    cost = power_mw * prices[cheap_idx].sum()
    revenue = rte * power_mw * prices[expensive_idx].sum()
    profit = revenue - cost

    if profit <= 0:
        return 0.0, False, [], []
    return float(profit), True, charge_hours, discharge_hours


def dispatch_day(
    prices: pd.Series,
    power_mw: float = 1.0,
    duration_hours: int = 4,
    rte: float = 0.85,
    cycles_per_day: int = 1,
) -> DayDispatchResult:
    """Run the dispatch heuristic on one day's hourly prices.

    Args:
        prices: hourly prices for one calendar day, index = hour-of-day
            (int), values = NIS/MWh. Length is normally 24 but may be 23
            or 25 on DST transition days.
        power_mw: nameplate power rating (MW).
        duration_hours: energy duration, i.e. MWh of capacity per MW.
        rte: round-trip efficiency applied to discharged energy.
        cycles_per_day: 1 (base case) or 2 (split-day variant).

    Returns:
        DayDispatchResult with total daily profit (NIS) and whether at
        least one cycle actually ran.
    """
    if prices.isna().any():
        prices = prices.dropna()
    values = prices.to_numpy(dtype=float)
    hours = prices.index.to_numpy()
    date = None

    if len(values) < 2:
        return DayDispatchResult(date=date, profit_nis=0.0, cycled=False)

    if cycles_per_day == 1:
        profit, cycled, ch, dh = _single_cycle(values, hours, power_mw, duration_hours, rte)
        return DayDispatchResult(date=date, profit_nis=profit, cycled=cycled, charge_hours=ch, discharge_hours=dh)

    if cycles_per_day == 2:
        mid = len(values) // 2
        p1, c1, ch1, dh1 = _single_cycle(values[:mid], hours[:mid], power_mw, duration_hours, rte)
        p2, c2, ch2, dh2 = _single_cycle(values[mid:], hours[mid:], power_mw, duration_hours, rte)
        total_profit = p1 + p2
        return DayDispatchResult(
            date=date,
            profit_nis=total_profit,
            cycled=c1 or c2,
            charge_hours=ch1 + ch2,
            discharge_hours=dh1 + dh2,
        )

    raise ValueError(f"Unsupported cycles_per_day={cycles_per_day}; only 1 or 2 are implemented.")


def run_dispatch_over_period(
    df: pd.DataFrame,
    price_col: str,
    power_mw: float = 1.0,
    duration_hours: int = 4,
    rte: float = 0.85,
    cycles_per_day: int = 1,
) -> pd.DataFrame:
    """Run dispatch_day for every calendar date in df, return one row per day.

    df must have columns: 'date' (calendar date), 'hour_offset' (1-25 int,
    used as the within-day ordering key), and `price_col`.
    """
    rows = []
    for date, group in df.groupby("date"):
        prices = pd.Series(group[price_col].to_numpy(), index=group["hour_offset"].to_numpy())
        result = dispatch_day(prices, power_mw=power_mw, duration_hours=duration_hours, rte=rte, cycles_per_day=cycles_per_day)
        rows.append({"date": date, "profit_nis": result.profit_nis, "cycled": result.cycled})
    return pd.DataFrame(rows)


def annualize_dispatch(daily: pd.DataFrame) -> dict:
    """Summarize a run_dispatch_over_period output into annual figures."""
    n_days = len(daily)
    if n_days == 0:
        return {"annual_revenue_per_mw_nis": 0.0, "cycles_run": 0, "days_observed": 0, "cycle_rate": 0.0}
    total_profit = daily["profit_nis"].sum()
    years = n_days / 365.25
    return {
        "annual_revenue_per_mw_nis": total_profit / years if years > 0 else 0.0,
        "cycles_run": int(daily["cycled"].sum()),
        "days_observed": n_days,
        "cycle_rate": float(daily["cycled"].mean()),
    }
