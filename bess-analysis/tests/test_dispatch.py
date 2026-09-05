"""Unit tests for the dispatch heuristic on synthetic data with known answers."""

from __future__ import annotations

import pandas as pd
import pytest

from bess_analysis.dispatch import annualize_dispatch, dispatch_day, run_dispatch_over_period


def _flat_day(cheap_hours, cheap_price, expensive_hours, expensive_price, mid_price, n_hours=24, start_hour=1):
    hours = list(range(start_hour, start_hour + n_hours))
    prices = {}
    for h in hours:
        if h in cheap_hours:
            prices[h] = cheap_price
        elif h in expensive_hours:
            prices[h] = expensive_price
        else:
            prices[h] = mid_price
    return pd.Series(prices)


def test_base_case_profitable_ordered_day():
    # Cheapest 4 hours early (1-4) at 10, priciest 4 hours late (21-24) at 100, rest 50.
    prices = _flat_day(cheap_hours=[1, 2, 3, 4], cheap_price=10, expensive_hours=[21, 22, 23, 24], expensive_price=100, mid_price=50)
    result = dispatch_day(prices, power_mw=1.0, duration_hours=4, rte=0.85, cycles_per_day=1)

    expected_cost = 4 * 10  # 1 MW * 4h * 10 NIS/MWh
    expected_revenue = 0.85 * 4 * 100
    expected_profit = expected_revenue - expected_cost

    assert result.cycled is True
    assert result.profit_nis == pytest.approx(expected_profit)
    assert result.charge_hours == [1, 2, 3, 4]
    assert result.discharge_hours == [21, 22, 23, 24]


def test_ordering_violation_blocks_cycle():
    # Priciest hours EARLY, cheapest hours LATE -> discharge would have to precede charge.
    prices = _flat_day(cheap_hours=[21, 22, 23, 24], cheap_price=10, expensive_hours=[1, 2, 3, 4], expensive_price=100, mid_price=50)
    result = dispatch_day(prices, power_mw=1.0, duration_hours=4, rte=0.85, cycles_per_day=1)

    assert result.cycled is False
    assert result.profit_nis == 0.0


def test_negative_profit_day_does_not_cycle():
    # rte=0.5 makes the round trip lossy enough that a thin spread is unprofitable,
    # but hours are still correctly ordered (cheap early, expensive late).
    prices = _flat_day(cheap_hours=[1, 2, 3, 4], cheap_price=9, expensive_hours=[21, 22, 23, 24], expensive_price=10, mid_price=9.5)
    result = dispatch_day(prices, power_mw=1.0, duration_hours=4, rte=0.5, cycles_per_day=1)

    # cost = 4*9=36, revenue = 0.5*4*10=20 -> profit -16 -> should not cycle
    assert result.cycled is False
    assert result.profit_nis == 0.0


def test_two_cycles_per_day_sums_two_independent_half_day_cycles():
    # First half (hours 1-12): cheap at 1-2, expensive at 11-12.
    # Second half (hours 13-24): cheap at 13-14, expensive at 23-24.
    prices = pd.Series(
        {
            1: 10, 2: 10, 3: 50, 4: 50, 5: 50, 6: 50, 7: 50, 8: 50, 9: 50, 10: 50, 11: 100, 12: 100,
            13: 10, 14: 10, 15: 50, 16: 50, 17: 50, 18: 50, 19: 50, 20: 50, 21: 50, 22: 50, 23: 100, 24: 100,
        }
    )
    result = dispatch_day(prices, power_mw=1.0, duration_hours=2, rte=0.85, cycles_per_day=2)

    half_profit = 0.85 * 2 * 100 - 2 * 10
    assert result.cycled is True
    assert result.profit_nis == pytest.approx(2 * half_profit)


def test_run_dispatch_over_period_and_annualize():
    day1 = pd.DataFrame(
        {
            "date": [pd.Timestamp("2025-06-01")] * 24,
            "hour_offset": list(range(1, 25)),
            "price": [10, 10, 10, 10] + [50] * 16 + [100, 100, 100, 100],
        }
    )
    day2 = day1.copy()
    day2["date"] = pd.Timestamp("2025-06-02")

    df = pd.concat([day1, day2], ignore_index=True)
    daily = run_dispatch_over_period(df, price_col="price", power_mw=1.0, duration_hours=4, rte=0.85, cycles_per_day=1)

    assert len(daily) == 2
    assert daily["cycled"].all()
    summary = annualize_dispatch(daily)
    assert summary["cycles_run"] == 2
    assert summary["days_observed"] == 2
    assert summary["cycle_rate"] == 1.0
    assert summary["annual_revenue_per_mw_nis"] > 0
