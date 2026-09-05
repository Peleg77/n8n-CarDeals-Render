"""Stage 6: sensitivities and scenarios, built on the real Stage 4 dispatch
model re-run under perturbed prices (not a shortcut approximation), except
where noted.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from bess_analysis.dispatch import annualize_dispatch, run_dispatch_over_period
from bess_analysis.financial import annuity_factor, capex_per_mw_nis, irr_unlevered, npv, project_cashflows


def scale_prices_around_daily_mean(df: pd.DataFrame, price_col: str, multiplier: float) -> pd.DataFrame:
    """Widen/narrow each day's price spread by `multiplier` while holding the
    daily mean price fixed: new_price = daily_mean + multiplier * (price - daily_mean).

    This lets scenario sensitivities re-run the *real* day-by-day dispatch
    heuristic under a genuinely wider/narrower spread, rather than just
    scaling the resulting revenue number.
    """
    out = df.copy()
    daily_mean = out.groupby("date")[price_col].transform("mean")
    out[price_col] = daily_mean + multiplier * (out[price_col] - daily_mean)
    return out


def irr_heatmap(
    df: pd.DataFrame,
    price_col: str,
    capex_list: list[float],
    spread_multipliers: list[float],
    duration_hours: float,
    rte: float,
    opex_per_mw_year_nis: float,
    discount_rate: float,
    degradation_annual: float,
    availability: float,
    project_life_years: int,
) -> pd.DataFrame:
    """2D grid: rows=capex (NIS/kWh), cols=spread multiplier, values=unlevered IRR."""
    rows = []
    for mult in spread_multipliers:
        scaled = scale_prices_around_daily_mean(df, price_col, mult)
        daily = run_dispatch_over_period(scaled, price_col=price_col, duration_hours=duration_hours, rte=rte, cycles_per_day=1)
        summary = annualize_dispatch(daily)
        annual_revenue = summary["annual_revenue_per_mw_nis"]
        for capex_kwh in capex_list:
            capex = capex_per_mw_nis(duration_hours, capex_kwh)
            cf = project_cashflows(annual_revenue, opex_per_mw_year_nis, degradation_annual, availability, project_life_years)
            irr = irr_unlevered(capex, cf)
            rows.append({"capex_per_kwh_nis": capex_kwh, "spread_multiplier": mult, "irr": irr, "annual_revenue_per_mw_nis": annual_revenue})
    long_df = pd.DataFrame(rows)
    return long_df.pivot(index="capex_per_kwh_nis", columns="spread_multiplier", values="irr")


def price_cap_scenario(
    df: pd.DataFrame,
    price_col: str,
    percentiles: list[float],
    duration_hours: float,
    rte: float,
    capex_per_kwh_nis_value: float,
    opex_per_mw_year_nis: float,
    discount_rate: float,
    degradation_annual: float,
    availability: float,
    project_life_years: int,
) -> pd.DataFrame:
    """Re-run dispatch with prices clipped at each percentile of the observed
    distribution — measures how much IRR depends on the right tail the
    regulator is considering capping."""
    capex = capex_per_mw_nis(duration_hours, capex_per_kwh_nis_value)
    base_daily = run_dispatch_over_period(df, price_col=price_col, duration_hours=duration_hours, rte=rte, cycles_per_day=1)
    base_summary = annualize_dispatch(base_daily)
    base_cf = project_cashflows(base_summary["annual_revenue_per_mw_nis"], opex_per_mw_year_nis, degradation_annual, availability, project_life_years)
    base_irr = irr_unlevered(capex, base_cf)

    rows = [{"percentile_cap": "none (actual)", "cap_value_nis_mwh": np.nan, "annual_revenue_per_mw_nis": base_summary["annual_revenue_per_mw_nis"], "irr": base_irr}]
    for p in percentiles:
        cap_value = df[price_col].quantile(p / 100)
        capped = df.copy()
        capped[price_col] = capped[price_col].clip(upper=cap_value)
        daily = run_dispatch_over_period(capped, price_col=price_col, duration_hours=duration_hours, rte=rte, cycles_per_day=1)
        summary = annualize_dispatch(daily)
        cf = project_cashflows(summary["annual_revenue_per_mw_nis"], opex_per_mw_year_nis, degradation_annual, availability, project_life_years)
        irr = irr_unlevered(capex, cf)
        rows.append({"percentile_cap": f"p{p}", "cap_value_nis_mwh": cap_value, "annual_revenue_per_mw_nis": summary["annual_revenue_per_mw_nis"], "irr": irr})

    out = pd.DataFrame(rows)
    out["irr_erosion_pp"] = (out["irr"] - base_irr) * 100
    return out


def spread_compression_scenario(
    base_annual_revenue_per_mw_nis: float,
    opex_per_mw_year_nis: float,
    capex_per_mw: float,
    discount_rate: float,
    degradation_annual: float,
    availability: float,
    project_life_years: int,
    compression_rates: list[float],
) -> pd.DataFrame:
    """IRR if the spread (and therefore revenue) erodes by X%/year as more
    storage enters the market, compounding on top of degradation/availability."""
    rows = []
    for rate in [0.0] + compression_rates:
        years = np.arange(1, project_life_years + 1)
        degradation_factor = (1 - degradation_annual) ** (years - 1)
        compression_factor = (1 - rate) ** (years - 1)
        revenue = base_annual_revenue_per_mw_nis * degradation_factor * compression_factor * availability
        cf = revenue - opex_per_mw_year_nis
        irr = irr_unlevered(capex_per_mw, cf)
        rows.append({"compression_pct_per_year": rate * 100, "irr": irr})
    return pd.DataFrame(rows)
