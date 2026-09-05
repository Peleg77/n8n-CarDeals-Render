# Demo run — SIMULATED data, not real Noga prices

This folder proves the pipeline (`loader -> validate -> descriptive ->
dispatch -> financial -> sensitivity -> report`) runs correctly end to
end. It has nothing to do with real market prices.

- `generate_synthetic_prices.py` — builds an invented 2025-05-28 to
  2026-09-05 hourly price series with a plausible duck-curve shape
  (documented assumptions in the script's docstring), including both
  real DST transition days in that window.
- `data_raw/` — the synthetic CSVs, in the exact Noga export schema.
- `outputs/report.md`, `outputs/charts/`, `outputs/model.xlsx` — the
  pipeline's output when run against `data_raw/`, generated with
  `--label "SIMULATED DATA"` so the banner at the top of the report can't
  be missed.

Regenerate with:

```bash
PYTHONPATH=src .venv/bin/python demo/generate_synthetic_prices.py
PYTHONPATH=src .venv/bin/python run_pipeline.py \
    --raw-dir demo/data_raw --clean-dir demo/data_clean \
    --outputs-dir demo/outputs --charts-dir demo/outputs/charts \
    --label "SIMULATED DATA"
```

The real deliverable is `../data/raw/` + `../outputs/` — untouched by
this, and still waiting for real Noga exports.
