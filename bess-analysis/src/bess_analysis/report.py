"""Assemble outputs/report.md from the results of every stage."""

from __future__ import annotations

from bess_analysis.validate import DISCLAIMER


def fmt(x, spec: str = ",.1f") -> str:
    try:
        return format(x, spec)
    except (TypeError, ValueError):
        return str(x)


def series_to_md_table(s, value_fmt: str = ",.2f") -> str:
    lines = ["| metric | value |", "|---|---|"]
    for k, v in s.items():
        lines.append(f"| {k} | {fmt(v, value_fmt)} |")
    return "\n".join(lines)


def df_to_md_table(df, float_fmt: str = ",.2f", col_fmt: dict | None = None) -> str:
    """col_fmt overrides float_fmt for specific columns (by name)."""
    col_fmt = col_fmt or {}
    cols = list(df.columns)
    header = "| " + " | ".join(str(c) for c in cols) + " |"
    sep = "|" + "|".join(["---"] * len(cols)) + "|"
    rows = []
    for _, row in df.iterrows():
        cells = []
        for c in cols:
            v = row[c]
            spec = col_fmt.get(c, float_fmt)
            cells.append(fmt(v, spec) if isinstance(v, (int, float)) else str(v))
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join([header, sep] + rows)


def build_report(ctx: dict) -> str:
    """ctx carries every stage's results, keyed by the names run_pipeline.py assembles."""
    sections = [
        "# BESS Arbitrage Feasibility — Noga MCP Prices\n",
        DISCLAIMER,
        f"\n**Data window:** {ctx['date_range'][0]} to {ctx['date_range'][1]} "
        f"({ctx['n_rows']} rows, {ctx['n_days']} calendar days)\n",
        "\n## Stage 2 — Data Quality\n",
        f"- Expected hours: {ctx['completeness']['expected_hours']}, present: {ctx['completeness']['present_hours']}, "
        f"missing: {ctx['completeness']['missing_hours']}\n"
        f"- Spring-forward (23h) days: {ctx['completeness']['spring_forward_days']}\n"
        f"- Fall-back (25h) days: {ctx['completeness']['fall_back_days']}\n"
        f"- Exact duplicate rows: {ctx['n_duplicates']}\n"
        f"- Unit sanity: median DA={fmt(ctx['unit_check']['median_da_nis_mwh'])} NIS/MWh, "
        f"median RT={fmt(ctx['unit_check']['median_rt_nis_mwh'])} NIS/MWh "
        f"(suspected unit mismatch: {ctx['unit_check']['suspected_unit_mismatch']})\n"
        f"- Outlier counts (DA): negative={ctx['outlier_counts_da']['negative']}, "
        f"zero={ctx['outlier_counts_da']['zero']}, extreme={ctx['outlier_counts_da']['extreme']}\n",
        "\n## Stage 3 — Descriptive Analysis\n",
    ]

    for label, key in [("Day-Ahead", "da"), ("Real-Time", "rt")]:
        s3 = ctx["descriptive"][key]
        sections.append(f"\n### {label}\n")
        sections.append(
            "**Typical min/max hour by season**\n\n"
            + df_to_md_table(s3["typical_min_max"], col_fmt={"min_hour": ",.0f", "max_hour": ",.0f"})
        )
        sections.append("\n\n**Price percentiles (NIS/MWh)**\n\n" + series_to_md_table(s3["percentiles"]))
        sections.append(f"\n\n**Midday (10:00-15:00) median price:** {fmt(s3['midday_median'])} NIS/MWh\n")
        sections.append("\n**Hours/year above threshold**\n\n" + series_to_md_table(s3["hours_above"], ",.0f"))
        sections.append("\n\n**Daily spread_4h distribution**\n\n" + series_to_md_table(s3["spread_dist"]))
        sections.append("\n\n**Days/year crossing spread_4h thresholds**\n\n" + series_to_md_table(s3["days_above_spread"], ",.0f"))
        sections.append(f"\n\n**spread_4h trend:** {fmt(s3['spread_trend']['slope_nis_mwh_per_year'])} NIS/MWh per year "
                         f"(n={s3['spread_trend']['n_days']} days)\n")
        conc = s3["concentration"]
        sections.append(
            f"\n**Concentration:** top 10 days = {fmt(conc['top10_pct'])}%, "
            f"top 20 days = {fmt(conc['top20_pct'])}%, top 50 days = {fmt(conc['top50_pct'])}% of annual value.\n"
        )
        if conc["top20_pct"] > 40:
            sections.append(
                "\n> **⚠ This is a merchant-risk finding, not a nuance:** more than 40% of annual arbitrage "
                "value comes from just 20 days. This is not a bankable, smooth revenue stream — a handful "
                "of missed or mis-forecast days materially changes the year's return.\n"
            )

    sections.append("\n### Day-Ahead vs Real-Time\n")
    sections.append(series_to_md_table(ctx["da_vs_rt"]))

    sections.append("\n## Stage 4 — Dispatch Model\n")
    sections.append(
        df_to_md_table(
            ctx["dispatch_variants"],
            col_fmt={"cycles_per_day": ",.0f", "duration_hours": ",.0f", "cycles_run": ",.0f", "days_observed": ",.0f", "cycle_rate": ",.1%"},
        )
    )

    sections.append("\n## Stage 5 — Financial Feasibility (base case)\n")
    fin = ctx["financial_base"]
    sections.append(
        f"- Capex/MW: {fmt(fin['capex_per_mw'])} NIS\n"
        f"- Annual revenue/MW (base dispatch): {fmt(fin['annual_revenue_per_mw'])} NIS\n"
        f"- NPV: {fmt(fin['npv'])} NIS/MW\n"
        f"- IRR (unlevered): {fmt(fin['irr']*100 if fin['irr']==fin['irr'] else float('nan'))}%\n"
        f"- Payback: {fmt(fin['payback'])} years\n"
        f"- Annuity factor ({ctx['config']['discount_rate_unlevered']*100:.0f}%, "
        f"{ctx['config']['project_life_years']}y): {fmt(fin['breakeven']['annuity_factor'])}\n"
        f"- Required gross revenue/MW-year to hit target return: {fmt(fin['breakeven']['required_gross_revenue_nis_per_mw'])} NIS\n"
        f"- Implied required spread_4h: {fmt(fin['breakeven']['implied_spread_4h_nis_mwh'])} NIS/MWh\n"
        f"- **Actual spread_4h covers {fmt(ctx['coverage_pct'])}% of what's required for an unlevered "
        f"{ctx['config']['discount_rate_unlevered']*100:.0f}% return.**\n"
    )

    sections.append("\n## Stage 6 — Sensitivities & Scenarios\n")
    sections.append("\n### 6a. IRR heatmap (capex x spread multiplier)\n")
    irr_grid_reset = ctx["irr_heatmap"].reset_index()
    irr_col_fmt = {c: ",.1%" for c in irr_grid_reset.columns if c != "capex_per_kwh_nis"}
    irr_col_fmt["capex_per_kwh_nis"] = ",.0f"
    sections.append(df_to_md_table(irr_grid_reset, ",.1%", col_fmt=irr_col_fmt))
    sections.append("\n### 6b. Price-cap scenario\n")
    sections.append(df_to_md_table(ctx["price_cap_scenario"], col_fmt={"irr": ",.1%", "irr_erosion_pp": ",.2f"}))
    sections.append("\n### 6c. Spread compression scenario\n")
    sections.append(df_to_md_table(ctx["spread_compression"], col_fmt={"irr": ",.1%"}))
    sections.append("\n### 6d. Revenue gap to target return\n")
    gap = ctx["revenue_gap"]
    sections.append(
        f"- Gap: {fmt(gap['gap_nis_per_mw_year'])} NIS/MW-year "
        f"({fmt(gap['gap_pct_of_required_gross_revenue'])}% of required gross revenue)\n"
    )

    return "\n".join(sections)
