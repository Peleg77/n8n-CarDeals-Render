"""Stage 5: financial feasibility model (NPV / IRR / payback / breakeven spread).

All monetary figures are nominal NIS, unlevered (no debt/tax layer — the
spec's `discount_rate_unlevered` and `project_life_years` describe a
simple unlevered project cash-flow analysis).
"""

from __future__ import annotations

import numpy as np
import numpy_financial as npf


def capex_per_mw_nis(duration_hours: float, capex_per_kwh_nis: float) -> float:
    """Capex per MW of power capacity.

    duration_hours * 1000 (kWh per MWh) * capex_per_kwh_nis (NIS/kWh)
    e.g. 4h * 1000 * 800 = 3,200,000 NIS/MW.
    """
    return duration_hours * 1000 * capex_per_kwh_nis


def annuity_factor(rate: float, years: int) -> float:
    """Present-value annuity factor: (1 - (1+r)^-n) / r."""
    if rate == 0:
        return float(years)
    return (1 - (1 + rate) ** (-years)) / rate


def project_cashflows(
    annual_revenue_per_mw_nis: float,
    opex_per_mw_year_nis: float,
    degradation_annual: float,
    availability: float,
    project_life_years: int,
) -> np.ndarray:
    """Net cash flow (NIS/MW) for years 1..N.

    Revenue in year t is degraded by (1 - degradation_annual)^(t-1) and
    scaled by `availability` (fraction of days the unit can actually
    dispatch); opex is held constant in nominal terms (no escalation
    assumption is made — documented in assumptions.md).
    """
    years = np.arange(1, project_life_years + 1)
    degradation_factor = (1 - degradation_annual) ** (years - 1)
    revenue = annual_revenue_per_mw_nis * degradation_factor * availability
    return revenue - opex_per_mw_year_nis


def npv(rate: float, capex_per_mw: float, cashflows: np.ndarray) -> float:
    discounted = cashflows / (1 + rate) ** np.arange(1, len(cashflows) + 1)
    return float(discounted.sum() - capex_per_mw)


def irr_unlevered(capex_per_mw: float, cashflows: np.ndarray) -> float:
    """IRR of [-capex, CF_1, ..., CF_N]. Returns NaN if no sign change (no real root)."""
    flows = np.concatenate([[-capex_per_mw], cashflows])
    if not (flows > 0).any():
        return float("nan")
    try:
        return float(npf.irr(flows))
    except Exception:
        return float("nan")


def payback_years(capex_per_mw: float, cashflows: np.ndarray) -> float:
    """Simple (undiscounted) payback period in years, linearly interpolated
    within the year the cumulative cash flow crosses capex. Returns inf if
    it never pays back within the given cash flow horizon."""
    cumulative = np.cumsum(cashflows)
    crossing = np.where(cumulative >= capex_per_mw)[0]
    if len(crossing) == 0:
        return float("inf")
    idx = crossing[0]
    prev_cumulative = cumulative[idx - 1] if idx > 0 else 0.0
    year_fraction = (capex_per_mw - prev_cumulative) / cashflows[idx] if cashflows[idx] != 0 else 0.0
    return float(idx + year_fraction)


def breakeven_spread_4h(
    capex_per_mw: float,
    opex_per_mw_year_nis: float,
    discount_rate: float,
    project_life_years: int,
    rte: float,
    duration_hours: float,
    cycles_per_year: float,
) -> dict:
    """Back-solve the spread_4h (NIS/MWh) needed to hit the target unlevered return.

    Approximation, consistent with the illustrative annuity-factor method:
        required_net_cashflow = capex / annuity_factor(rate, years)
        required_gross_revenue = required_net_cashflow + opex
        required_gross_revenue ≈ cycles_per_year * duration_hours * rte * spread_4h

    This ignores the charging-cost baseline level (unlike the full
    day-by-day dispatch model in Stage 4, which nets bottom-hour cost
    against discharge revenue exactly) — it is a comparison yardstick,
    not a substitute for the Stage 4 dispatch result.
    """
    af = annuity_factor(discount_rate, project_life_years)
    required_net_cashflow = capex_per_mw / af
    required_gross_revenue = required_net_cashflow + opex_per_mw_year_nis
    denom = cycles_per_year * duration_hours * rte
    implied_spread_4h = required_gross_revenue / denom if denom > 0 else float("inf")
    return {
        "annuity_factor": af,
        "required_annual_cashflow_nis_per_mw": required_net_cashflow,
        "required_gross_revenue_nis_per_mw": required_gross_revenue,
        "implied_spread_4h_nis_mwh": implied_spread_4h,
    }


def coverage_ratio_pct(actual_spread_4h_avg: float, implied_spread_4h: float) -> float:
    """What % of the required breakeven spread does the actual data provide?"""
    if implied_spread_4h == 0:
        return float("nan")
    return actual_spread_4h_avg / implied_spread_4h * 100


def revenue_gap_per_mw_year(
    required_net_cashflow_nis_per_mw: float,
    actual_annual_revenue_per_mw_nis: float,
    opex_per_mw_year_nis: float,
) -> dict:
    """NIS/MW-year shortfall to reach the target unlevered return (Stage 6d)."""
    actual_net_cashflow = actual_annual_revenue_per_mw_nis - opex_per_mw_year_nis
    gap_nis = required_net_cashflow_nis_per_mw - actual_net_cashflow
    required_gross_revenue = required_net_cashflow_nis_per_mw + opex_per_mw_year_nis
    gap_pct_of_required_revenue = gap_nis / required_gross_revenue * 100 if required_gross_revenue else float("nan")
    return {
        "gap_nis_per_mw_year": gap_nis,
        "gap_pct_of_required_gross_revenue": gap_pct_of_required_revenue,
    }
