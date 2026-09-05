#!/usr/bin/env python3
"""Storage-add-on economics under Israel's REGULATED PV+storage feed-in
tariff track -- a different model from run_pipeline.py's MCP merchant
arbitrage model, built for the business plan: add storage to (existing or
new) solar installations, do this N times, then sell the portfolio to a
passive investor at a target yield.

Every assumption is tagged and sourced (or flagged as a guess) in
fit_storage_config.yaml -- read that file before trusting any number here.
This reuses the same NPV/IRR/annuity math already tested in
src/bess_analysis/financial.py (test coverage: tests/test_dispatch.py
covers the dispatch side; the financial functions themselves were
validated by hand against the annuity-factor example in the original
spec -- see the chat history, not a committed test file, since this
calculator has no synthetic-data dispatch logic to unit-test the way the
MCP model does).

Usage:
    PYTHONPATH=src .venv/bin/python fit_storage_calculator.py
"""

from __future__ import annotations

import math
from pathlib import Path

import yaml

from bess_analysis.financial import irr_unlevered, npv, payback_years, project_cashflows

ROOT = Path(__file__).parent


def load_config() -> dict:
    with open(ROOT / "fit_storage_config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def annual_revenue_year1(config: dict) -> float:
    """Sum of (qualifying hours x avg discharge power x seasonal tariff) across seasons."""
    total = 0.0
    for season, hours in config["discharge_hours_per_year"].items():
        kwh = hours * config["avg_discharge_power_kw"]
        tariff_nis_per_kwh = config["tariff_agorot_per_kwh"][season] / 100
        total += kwh * tariff_nis_per_kwh
    return total


def project_economics(config: dict, capex_storage_nis_per_kwh: float | None = None, avg_discharge_power_kw: float | None = None) -> dict:
    """One project's full economics. Overrides let sensitivity() vary one input at a time."""
    cfg = dict(config)
    if capex_storage_nis_per_kwh is not None:
        cfg["capex_storage_nis_per_kwh"] = capex_storage_nis_per_kwh
    if avg_discharge_power_kw is not None:
        cfg["avg_discharge_power_kw"] = avg_discharge_power_kw

    capex = cfg["storage_capacity_kwh"] * cfg["capex_storage_nis_per_kwh"] + cfg["other_capex_nis"]
    revenue_y1 = annual_revenue_year1(cfg)
    cashflows = project_cashflows(
        revenue_y1, cfg["opex_nis_per_year"], cfg["degradation_annual"], cfg["availability"], cfg["project_life_years"]
    )

    developer_npv = npv(cfg["discount_rate_unlevered"], capex, cashflows)
    developer_irr = irr_unlevered(capex, cashflows)
    developer_payback = payback_years(capex, cashflows)

    # Price a passive investor would pay for exactly their required yield:
    # the PV of the same cash flow stream discounted at THEIR rate, with
    # zero capex netted out (capex was already sunk by the developer).
    price_at_buyer_yield = npv(cfg["buyer_required_yield"], 0.0, cashflows)

    return {
        "capex": capex,
        "annual_revenue_year1": revenue_y1,
        "annual_profit_year1": revenue_y1 - cfg["opex_nis_per_year"],
        "developer_npv": developer_npv,
        "developer_irr": developer_irr,
        "developer_payback_years": developer_payback,
        "price_at_buyer_yield": price_at_buyer_yield,
    }


def sensitivity_table(config: dict) -> list[dict]:
    rows = []
    for capex_kwh in config["sensitivity"]["capex_storage_nis_per_kwh"]:
        for discharge_kw in config["sensitivity"]["avg_discharge_power_kw"]:
            r = project_economics(config, capex_storage_nis_per_kwh=capex_kwh, avg_discharge_power_kw=discharge_kw)
            rows.append(
                {
                    "capex_nis_per_kwh": capex_kwh,
                    "avg_discharge_power_kw": discharge_kw,
                    "developer_irr": r["developer_irr"],
                    "price_at_buyer_yield": r["price_at_buyer_yield"],
                }
            )
    return rows


def main() -> None:
    config = load_config()
    base = project_economics(config)

    n_projects_needed = math.ceil(config["target_portfolio_sale_price_nis"] / base["price_at_buyer_yield"]) if base["price_at_buyer_yield"] > 0 else float("inf")

    print("=" * 70)
    print("SINGLE PROJECT ECONOMICS")
    print(f"  Storage: {config['storage_capacity_kwh']} kWh / {config['storage_power_kw']} kW, PV: {config['pv_capacity_kw']} kW")
    print(f"  Capex: {base['capex']:,.0f} NIS")
    print(f"  Annual revenue (year 1): {base['annual_revenue_year1']:,.0f} NIS")
    print(f"  Annual profit (year 1, after opex): {base['annual_profit_year1']:,.0f} NIS")
    print(f"  Developer NPV @ {config['discount_rate_unlevered']*100:.0f}%: {base['developer_npv']:,.0f} NIS")
    irr_str = f"{base['developer_irr']*100:.1f}%" if base["developer_irr"] == base["developer_irr"] else "n/a (never positive)"
    print(f"  Developer IRR (unlevered): {irr_str}")
    print(f"  Developer payback: {base['developer_payback_years']:.1f} years" if base["developer_payback_years"] != float("inf") else "  Developer payback: never within project life")
    print()
    print(f"  Price a buyer wanting {config['buyer_required_yield']*100:.0f}% would pay for ONE project: {base['price_at_buyer_yield']:,.0f} NIS")
    print()
    print("=" * 70)
    print(f"PORTFOLIO TARGET: sell for {config['target_portfolio_sale_price_nis']:,.0f} NIS at {config['buyer_required_yield']*100:.0f}% buyer yield")
    print(f"  Projects needed: {n_projects_needed}")
    print(f"  ({n_projects_needed} projects x {base['price_at_buyer_yield']:,.0f} NIS/project = {n_projects_needed*base['price_at_buyer_yield']:,.0f} NIS)")
    print(f"  Total capex you'd have to fund yourself first: {n_projects_needed*base['capex']:,.0f} NIS")
    print()
    print("=" * 70)
    print("SENSITIVITY: developer IRR / price-per-project vs capex and discharge power")
    print(f"{'capex NIS/kWh':>15} {'discharge kW':>13} {'IRR':>8} {'price/project':>15}")
    for row in sensitivity_table(config):
        irr_disp = f"{row['developer_irr']*100:.1f}%" if row["developer_irr"] == row["developer_irr"] else "n/a"
        print(f"{row['capex_nis_per_kwh']:>15,.0f} {row['avg_discharge_power_kw']:>13,.0f} {irr_disp:>8} {row['price_at_buyer_yield']:>15,.0f}")


if __name__ == "__main__":
    main()
