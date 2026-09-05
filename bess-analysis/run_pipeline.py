#!/usr/bin/env python3
"""End-to-end pipeline: raw Noga exports in data/raw/ -> outputs/.

Usage:
    PYTHONPATH=src python run_pipeline.py

Requires manually-exported Noga MCP files in data/raw/ (see README.md —
live scraping is not available from this environment). Runs Stages 2-6
against whatever date range those files cover.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import yaml

from bess_analysis import charts, descriptive, dispatch, excel_model, financial, loader, report, sensitivity, validate

ROOT = Path(__file__).parent
DATA_RAW = ROOT / "data" / "raw"
DATA_CLEAN = ROOT / "data" / "clean"
OUTPUTS = ROOT / "outputs"
CHARTS = OUTPUTS / "charts"


def load_config() -> dict:
    with open(ROOT / "config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def run_descriptive_for_series(df: pd.DataFrame, price_col: str) -> dict:
    daily = descriptive.daily_spread(df, price_col)
    return {
        "typical_min_max": descriptive.typical_min_max_hour(df, price_col),
        "percentiles": descriptive.percentile_table(df, price_col),
        "midday_median": descriptive.midday_median(df, price_col),
        "hours_above": descriptive.hours_above_thresholds_per_year(df, price_col),
        "daily_spread": daily,
        "spread_dist": descriptive.spread_distribution(daily),
        "days_above_spread": descriptive.days_above_spread_thresholds(daily),
        "spread_trend": descriptive.spread_trend(daily),
        "concentration": descriptive.concentration_analysis(daily),
        "heatmap_matrix": descriptive.heatmap_matrix(df, price_col),
    }


def main() -> None:
    config = load_config()
    CHARTS.mkdir(parents=True, exist_ok=True)
    DATA_CLEAN.mkdir(parents=True, exist_ok=True)

    print("Stage 1: loading raw exports...")
    raw = loader.load_all_raw(DATA_RAW)
    print(f"  {len(raw)} raw rows loaded from data/raw/")

    print("Stage 2: building timestamps + validating...")
    df = validate.build_timestamps(raw)
    completeness = validate.completeness_report(df)
    duplicates = validate.duplicate_report(df)
    df = validate.flag_outliers(df)
    unit_check = validate.unit_sanity_check(df)
    print(f"  completeness: {completeness['present_hours']}/{completeness['expected_hours']} hours present")
    print(f"  duplicates: {len(duplicates)}")

    df.to_parquet(DATA_CLEAN / "mcp_hourly.parquet", index=False)

    print("Stage 3: descriptive analysis...")
    desc_da = run_descriptive_for_series(df, "price_da_nis_mwh")
    desc_rt = run_descriptive_for_series(df, "price_rt_nis_mwh")
    da_vs_rt = descriptive.da_vs_rt_diff(df)

    print("Stage 4: dispatch model (base case: Day-Ahead prices)...")
    variant_rows = []
    dispatch_daily_cache = {}
    for cycles in config["cycles_per_day_variants"]:
        for duration in config["duration_variants_hours"]:
            daily = dispatch.run_dispatch_over_period(
                df, price_col="price_da_nis_mwh", duration_hours=duration, rte=config["rte"], cycles_per_day=cycles
            )
            summary = dispatch.annualize_dispatch(daily)
            variant_rows.append({"cycles_per_day": cycles, "duration_hours": duration, **summary})
            dispatch_daily_cache[(cycles, duration)] = daily
    dispatch_variants = pd.DataFrame(variant_rows)

    base_cycles, base_duration = 1, config["duration_hours"]
    base_daily = dispatch_daily_cache[(base_cycles, base_duration)]
    base_summary = dispatch.annualize_dispatch(base_daily)

    print("Stage 5: financial feasibility (base case)...")
    capex = financial.capex_per_mw_nis(base_duration, config["capex_per_kwh_nis"])
    opex = config["opex_per_mwh_year_nis"]
    cf = financial.project_cashflows(
        base_summary["annual_revenue_per_mw_nis"], opex, config["degradation_annual"], config["availability"], config["project_life_years"]
    )
    npv_val = financial.npv(config["discount_rate_unlevered"], capex, cf)
    irr_val = financial.irr_unlevered(capex, cf)
    payback_val = financial.payback_years(capex, cf)
    cycles_per_year = base_summary["cycles_run"] / (base_summary["days_observed"] / 365.25)
    breakeven = financial.breakeven_spread_4h(
        capex, opex, config["discount_rate_unlevered"], config["project_life_years"], config["rte"], base_duration, cycles_per_year
    )
    coverage_pct = financial.coverage_ratio_pct(desc_da["spread_dist"]["mean"], breakeven["implied_spread_4h_nis_mwh"])

    print("Stage 6: sensitivities...")
    irr_grid = sensitivity.irr_heatmap(
        df,
        "price_da_nis_mwh",
        config["sensitivity"]["capex_per_kwh_nis"],
        config["sensitivity"]["spread_multiplier"],
        base_duration,
        config["rte"],
        opex,
        config["discount_rate_unlevered"],
        config["degradation_annual"],
        config["availability"],
        config["project_life_years"],
    )
    price_cap = sensitivity.price_cap_scenario(
        df,
        "price_da_nis_mwh",
        config["sensitivity"]["price_cap_percentiles"],
        base_duration,
        config["rte"],
        config["capex_per_kwh_nis"],
        opex,
        config["discount_rate_unlevered"],
        config["degradation_annual"],
        config["availability"],
        config["project_life_years"],
    )
    compression = sensitivity.spread_compression_scenario(
        base_summary["annual_revenue_per_mw_nis"],
        opex,
        capex,
        config["discount_rate_unlevered"],
        config["degradation_annual"],
        config["availability"],
        config["project_life_years"],
        config["sensitivity"]["spread_compression_annual_pct"],
    )
    revenue_gap = financial.revenue_gap_per_mw_year(
        breakeven["required_annual_cashflow_nis_per_mw"], base_summary["annual_revenue_per_mw_nis"], opex
    )

    print("Generating charts...")
    charts.plot_hour_month_heatmap(desc_da["heatmap_matrix"], "Day-Ahead price (NIS/MWh)", CHARTS / "heatmap_da.png")
    charts.plot_hour_month_heatmap(desc_rt["heatmap_matrix"], "Real-Time price (NIS/MWh)", CHARTS / "heatmap_rt.png")
    charts.plot_spread_distribution(desc_da["daily_spread"], CHARTS / "spread_distribution_da.png")
    charts.plot_concentration_curve(desc_da["daily_spread"], CHARTS / "concentration_da.png")
    charts.plot_irr_sensitivity_heatmap(irr_grid, CHARTS / "irr_sensitivity.png")

    print("Building outputs/model.xlsx...")
    excel_model.build_model_workbook(config, base_daily, OUTPUTS / "model.xlsx")

    print("Writing outputs/report.md...")
    ctx = {
        "date_range": (df["timestamp"].min(), df["timestamp"].max()),
        "n_rows": len(df),
        "n_days": df["date"].nunique(),
        "completeness": completeness,
        "n_duplicates": len(duplicates),
        "unit_check": unit_check,
        "outlier_counts_da": {
            "negative": int(df["price_da_nis_mwh_is_negative"].sum()),
            "zero": int(df["price_da_nis_mwh_is_zero"].sum()),
            "extreme": int(df["price_da_nis_mwh_is_extreme"].sum()),
        },
        "descriptive": {"da": desc_da, "rt": desc_rt},
        "da_vs_rt": da_vs_rt,
        "dispatch_variants": dispatch_variants,
        "financial_base": {
            "capex_per_mw": capex,
            "annual_revenue_per_mw": base_summary["annual_revenue_per_mw_nis"],
            "npv": npv_val,
            "irr": irr_val,
            "payback": payback_val,
            "breakeven": breakeven,
        },
        "coverage_pct": coverage_pct,
        "irr_heatmap": irr_grid,
        "price_cap_scenario": price_cap,
        "spread_compression": compression,
        "revenue_gap": revenue_gap,
        "config": config,
    }
    report_md = report.build_report(ctx)
    (OUTPUTS / "report.md").write_text(report_md, encoding="utf-8")
    print("Done. See outputs/report.md, outputs/charts/, outputs/model.xlsx, data/clean/mcp_hourly.parquet")


if __name__ == "__main__":
    main()
