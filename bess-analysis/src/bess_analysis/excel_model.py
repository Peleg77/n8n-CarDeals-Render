"""Build outputs/model.xlsx: an editable cash-flow model.

Structure:
    Assumptions   - every config.yaml parameter as a named cell.
    Daily Dispatch - one row per calendar day of the base-case dispatch
                     (DA prices, 1 cycle/day, config duration_hours), so
                     "annual_revenue_per_mw_base" is a real SUM() formula
                     over actual dispatch results, not a pasted number.
    Cashflow      - per-year revenue/opex/net cash flow as formulas
                     referencing Assumptions, plus NPV/IRR/payback cells
                     using Excel's own NPV()/IRR() functions so changing
                     any assumption cell recalculates the whole model.

All formulas reference named cells, so editing a value on the Assumptions
sheet propagates through without touching any other sheet.

Note on `opex_per_mwh_year_nis`: despite the "mwh" in the name (kept
verbatim from the spec's config.yaml key), this is applied as a flat
NIS-per-MW-per-year cost — see outputs/assumptions.md.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from openpyxl import Workbook
from openpyxl.workbook.defined_name import DefinedName

PARAM_ORDER = [
    ("capex_per_kwh_nis", "Capex (NIS/kWh)"),
    ("duration_hours", "Duration (hours)"),
    ("opex_per_mwh_year_nis", "Opex (NIS/MW-year)"),
    ("rte", "Round-trip efficiency"),
    ("project_life_years", "Project life (years)"),
    ("discount_rate_unlevered", "Discount rate (unlevered)"),
    ("degradation_annual", "Annual degradation"),
    ("availability", "Availability"),
]


def _write_assumptions_sheet(wb: Workbook, config: dict) -> None:
    ws = wb.active
    ws.title = "Assumptions"
    ws["A1"] = "Parameter"
    ws["B1"] = "Value"
    for i, (key, label) in enumerate(PARAM_ORDER, start=2):
        ws[f"A{i}"] = label
        ws[f"B{i}"] = config[key]
        wb.defined_names[key] = DefinedName(key, attr_text=f"Assumptions!$B${i}")

    capex_row = len(PARAM_ORDER) + 3
    ws[f"A{capex_row}"] = "Capex per MW (NIS)"
    ws[f"B{capex_row}"] = "=duration_hours*1000*capex_per_kwh_nis"
    wb.defined_names["capex_per_mw"] = DefinedName("capex_per_mw", attr_text=f"Assumptions!$B${capex_row}")


def _write_daily_dispatch_sheet(wb: Workbook, daily: pd.DataFrame) -> None:
    ws = wb.create_sheet("Daily Dispatch")
    ws.append(["date", "profit_nis", "cycled"])
    for _, row in daily.iterrows():
        date_val = row["date"]
        date_str = str(date_val.date()) if hasattr(date_val, "date") else str(date_val)
        ws.append([date_str, float(row["profit_nis"]), bool(row["cycled"])])
    n = len(daily) + 1
    ws["E1"] = "years_observed"
    ws["F1"] = f"=COUNTA(A2:A{n})/365.25"
    wb.defined_names["years_observed"] = DefinedName("years_observed", attr_text="'Daily Dispatch'!$F$1")
    ws["E2"] = "annual_revenue_per_mw_base"
    ws["F2"] = f"=SUM(B2:B{n})/years_observed"
    wb.defined_names["annual_revenue_per_mw_base"] = DefinedName("annual_revenue_per_mw_base", attr_text="'Daily Dispatch'!$F$2")


def _write_cashflow_sheet(wb: Workbook, project_life_years: int) -> None:
    ws = wb.create_sheet("Cashflow")
    ws.append(["Year", "Revenue (NIS/MW)", "Opex (NIS/MW)", "Net Cash Flow (NIS/MW)", "Cumulative CF"])
    for year in range(1, project_life_years + 1):
        row = year + 1
        prev_cum = f"E{row - 1}" if year > 1 else "0"
        ws.append(
            [
                year,
                f"=annual_revenue_per_mw_base*(1-degradation_annual)^({year}-1)*availability",
                "=opex_per_mwh_year_nis",
                f"=B{row}-C{row}",
                f"={prev_cum}+D{row}",
            ]
        )
    last_row = project_life_years + 1

    # Column H: [-capex, CF_1..CF_N] as one contiguous range for IRR().
    ws["H1"] = "=-capex_per_mw"
    for year in range(1, project_life_years + 1):
        ws[f"H{year + 1}"] = f"=D{year + 1}"

    ws["J1"] = "NPV (NIS/MW)"
    ws["K1"] = f"=NPV(discount_rate_unlevered,D2:D{last_row})-capex_per_mw"
    ws["J2"] = "IRR"
    ws["K2"] = f"=IRR(H1:H{last_row})"
    ws["J3"] = "Payback (years, simple)"
    ws["K3"] = f"=MATCH(TRUE,INDEX(E2:E{last_row}>=capex_per_mw,0),0)"


def build_model_workbook(
    config: dict,
    base_case_daily_dispatch: pd.DataFrame,
    out_path: Path,
) -> None:
    wb = Workbook()
    _write_assumptions_sheet(wb, config)
    _write_daily_dispatch_sheet(wb, base_case_daily_dispatch)
    _write_cashflow_sheet(wb, int(config["project_life_years"]))
    wb.save(out_path)
