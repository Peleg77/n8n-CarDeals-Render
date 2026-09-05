> **הבהרה:** ראה דיסקליימר מלא בראש `outputs/report.md`. המחירים שעליהם
> מבוסס ניתוח זה סימולטיביים ואינם מהווים ייעוץ השקעות.

# Assumptions beyond the spec

Everything below is a judgment call this pipeline made that the spec did
not fully pin down. Listed so it's clear what's the spec's and what's ours.

## Data access (Stage 1)

- **No live scraping.** This sandbox's egress proxy blocks
  `www.noga-iso.co.il` outright (confirmed via `robots.txt` fetch attempt
  and WebFetch — both returned `EGRESS_BLOCKED`), so Playwright network
  interception per the spec's priority-1 approach is not possible from
  here. The loader instead parses files the user exports manually from
  the site (or any CSV/XLSX with equivalent columns) dropped into
  `data/raw/`. If network access to the domain is later enabled, the
  Playwright/API-discovery step described in the spec should be added as
  a separate fetch script that writes into the same `data/raw/` folder —
  everything downstream (Stages 2-6) is unchanged either way.
- Because of the above, **Stage 1 has not yet run against real data.**
  The full pipeline was validated end-to-end on synthetic hourly prices
  (a duck-curve shape) to prove Stages 2-6 are correct; `outputs/report.md`
  will regenerate against real numbers as soon as real exports are placed
  in `data/raw/` and `run_pipeline.py` is re-run.

## Hour-label / DST convention (Stage 2)

- Assumed convention: hour label N = interval `[N-1:00, N:00)` local time
  (label 1 = 00:00-01:00 ... label 24 = 23:00-24:00).
- Spring-forward day (23h): assumed Noga simply omits the row for the
  nonexistent local hour (e.g. skips label "3"), rather than renumbering
  23 rows consecutively as 1-23. **Unverified against a real export.**
- Fall-back day (25h): assumed one hour label appears twice consecutively
  (e.g. label "2" twice), with the first occurrence = summer time (DST,
  UTC+3) and the second = standard time (UTC+2), matching Israel's actual
  2:00→1:00 transition.
- If real data uses a different convention, `completeness_report()`'s
  `nonexistent_local_time_count` and the missing/duplicate-hour counts
  will surface it immediately — this was designed to fail loudly rather
  than silently misalign timestamps.

## Dispatch model (Stage 4)

- Dispatch is run using the **Day-Ahead** price series for the base
  case (Financial model, Stage 5) since DA is the tradable/schedulable
  price a real operator would optimize against; Real-Time dispatch is
  computed separately in the Stage 4 variant table for comparison, and
  DA-vs-RT divergence is analyzed separately in Stage 3E as an execution-
  risk metric (not folded into the Stage 4 dispatch itself).
- **2-cycles-per-day heuristic**: the spec asks to "try" 2 cycles/day
  without specifying an algorithm. This pipeline splits each day into two
  contiguous halves by array position and applies the single-cycle
  heuristic independently to each half, summing profits. This is one
  reasonable heuristic among several possible ones — a different split
  (e.g., a rolling/lookahead optimizer) could do better or worse.
- The ordering constraint ("all discharge hours after all charge hours")
  is enforced exactly as specified, including for the 2h/8h duration
  variants, even though the spec's constraint was framed around the 4h
  base case.

## Financial model (Stage 5)

- `opex_per_mwh_year_nis` in `config.yaml` is applied as a **flat NIS-per-
  MW-per-year** cost (not multiplied by MWh throughput), despite the "mwh"
  in its name — this matches both its description ("תחזוקה, ביטוח, קרקע,
  augmentation": fixed O&M items) and its magnitude (20,000 NIS is a
  per-MW-year O&M benchmark, not a per-MWh figure).
- Opex is held constant in nominal terms across the project life (no
  escalation/inflation assumption).
- Payback is **simple (undiscounted)** payback, linearly interpolated
  within the crossing year. A discounted-payback variant was not computed
  since the spec did not specify which convention.
- The breakeven "implied spread_4h" (Stage 5's headline coverage-ratio
  number) is back-solved using the simplified relation
  `required_gross_revenue ≈ cycles_per_year × duration_hours × rte ×
  spread_4h`, consistent with the spec's own illustrative annuity-factor
  back-of-envelope approach for this one step. It does **not** net out the
  charging-cost baseline price level the way the full Stage 4 day-by-day
  dispatch model does — it's a comparison yardstick, not a substitute for
  the Stage 4 result.

## Sensitivities (Stage 6)

- The capex × spread-multiplier IRR heatmap (6a) **re-runs the real
  Stage 4 dispatch model** on prices rescaled around each day's own mean
  (`new_price = daily_mean + multiplier × (price − daily_mean)`), rather
  than just scaling the resulting revenue number — so the ordering
  constraint and the no-cycle-if-unprofitable rule are still enforced
  under each scenario.
- The price-cap scenario (6b) clips prices at the given percentile of the
  **observed** distribution, then re-runs the real dispatch model — it is
  not a synthetic percentile assumption.
- The spread-compression scenario (6c) applies the compression rate as a
  compounding annual multiplier on top of degradation and availability,
  starting from the base case's actual annual revenue.
