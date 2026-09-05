# BESS Arbitrage Feasibility — Noga MCP Prices

Pipeline: Noga ISO hourly MCP price exports -> cleaning/validation ->
descriptive analysis -> real day-by-day battery dispatch model ->
financial feasibility (NPV/IRR/payback) -> sensitivities.

Standalone Python project — unrelated to the n8n codebase this repo
otherwise contains; it lives in this top-level folder rather than under
`packages/`.

## Why there's no live scraper

`https://www.noga-iso.co.il` is blocked by this environment's network
egress policy (confirmed via `robots.txt` fetch and WebFetch, both
returned `EGRESS_BLOCKED`), so the Playwright-based live fetch described
in the original spec cannot run from here. Instead:

1. Go to https://www.noga-iso.co.il/trade/mcp/, pick a date range
   (a month at a time is plenty), click "הצג נתונים", then "ייצוא נתונים
   לאקסל".
2. Drop each exported file into `data/raw/` (any filename, `.csv` or
   `.xlsx`, as long as it has the four Noga columns: תאריך, שעה, מחיר יום
   מראש, מחיר זמן אמת עתידי).
3. Target range: 28/05/2025 (first publication date) through today.
4. Run the pipeline (below).

If live network access to the domain is enabled later, add a fetch
script that writes into `data/raw/` using the same schema — everything
downstream is unaffected.

## Setup

```bash
python3 -m venv .venv
.venv/bin/pip install -e .
```

## Run

```bash
PYTHONPATH=src .venv/bin/python run_pipeline.py
```

Outputs land in `outputs/report.md`, `outputs/charts/`, `outputs/model.xlsx`,
and `data/clean/mcp_hourly.parquet`.

## Tests

```bash
PYTHONPATH=src .venv/bin/python -m pytest tests/ -v
```

## Config

All financial/dispatch assumptions live in `config.yaml` — edit and
re-run rather than changing code. `outputs/model.xlsx` also has every
assumption on its own sheet as a named Excel cell, so you can sanity-check
or override values there too (NPV/IRR/payback recalculate live).

See `outputs/assumptions.md` for every judgment call made beyond what the
original spec pinned down.
