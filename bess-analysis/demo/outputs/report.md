# ⚠ SIMULATED DATA — NOT REAL NOGA PRICES ⚠

This report was generated from invented/simulated prices for pipeline testing. Do not use any number below for a real investment decision.

---

# BESS Arbitrage Feasibility — Noga MCP Prices

> **הבהרה חשובה (מקור: נגה — מנהל המערכת):** המחירים במאגר זה הם
> **סימולטיביים**. אין התחייבות לחישוב או לפרסום יומי סדיר, המתווה
> וכללי החישוב עשויים להשתנות בהתאם להחלטות רשות החשמל, וייתכנו סטיות
> בין הערכים המתפרסמים לבין החישוב הרשמי — "בעיקר במקרי קצה". הניתוח
> שלהלן מבוסס על נתונים אלה כפי שפורסמו, ואינו מהווה ייעוץ השקעות.


**Data window:** 2025-05-28 00:00:00+03:00 to 2026-09-05 23:00:00+03:00 (11184 rows, 466 calendar days)


## Stage 2 — Data Quality

- Expected hours: 11184, present: 11184, missing: 0
- Spring-forward (23h) days: [datetime.date(2026, 3, 27)]
- Fall-back (25h) days: [datetime.date(2025, 10, 26)]
- Exact duplicate rows: 0
- Unit sanity: median DA=45.8 NIS/MWh, median RT=46.0 NIS/MWh (suspected unit mismatch: False)
- Outlier counts (DA): negative=38, zero=0, extreme=0


## Stage 3 — Descriptive Analysis


### Day-Ahead

**Typical min/max hour by season**

| season | min_hour | min_level_nis_mwh | max_hour | max_level_nis_mwh |
|---|---|---|---|---|
| summer | 12 | 20.09 | 20 | 243.80 |
| transition | 12 | 4.94 | 19 | 102.53 |
| winter | 12 | 35.80 | 18 | 140.25 |


**Price percentiles (NIS/MWh)**

| metric | value |
|---|---|
| p1 | 3.32 |
| p5 | 11.56 |
| p25 | 30.94 |
| p50 | 45.83 |
| p75 | 74.95 |
| p95 | 191.51 |
| p99 | 235.99 |
| p99.9 | 898.11 |
| max | 1,243.53 |


**Midday (10:00-15:00) median price:** 21.4 NIS/MWh


**Hours/year above threshold**

| metric | value |
|---|---|
| >500 | 39 |
| >800 | 16 |
| >1000 | 3 |
| >1200 | 1 |


**Daily spread_4h distribution**

| metric | value |
|---|---|
| mean | 146.13 |
| median | 100.22 |
| p1 | 67.23 |
| p5 | 72.62 |
| p25 | 86.16 |
| p50 | 100.22 |
| p75 | 184.83 |
| p95 | 323.51 |
| p99 | 413.39 |
| p99.9 | 512.48 |


**Days/year crossing spread_4h thresholds**

| metric | value |
|---|---|
| >200 | 52 |
| >300 | 34 |
| >360 | 15 |
| >400 | 7 |
| >450 | 1 |


**spread_4h trend:** -8.5 NIS/MWh per year (n=466 days)


**Concentration:** top 10 days = 6.3%, top 20 days = 11.5%, top 50 days = 24.1% of annual value.


### Real-Time

**Typical min/max hour by season**

| season | min_hour | min_level_nis_mwh | max_hour | max_level_nis_mwh |
|---|---|---|---|---|
| summer | 13 | 20.63 | 20 | 241.56 |
| transition | 12 | 4.95 | 19 | 102.92 |
| winter | 12 | 37.07 | 18 | 141.97 |


**Price percentiles (NIS/MWh)**

| metric | value |
|---|---|
| p1 | 0.21 |
| p5 | 10.40 |
| p25 | 29.99 |
| p50 | 46.04 |
| p75 | 75.19 |
| p95 | 192.00 |
| p99 | 245.27 |
| p99.9 | 873.78 |
| max | 1,236.90 |


**Midday (10:00-15:00) median price:** 20.8 NIS/MWh


**Hours/year above threshold**

| metric | value |
|---|---|
| >500 | 42 |
| >800 | 13 |
| >1000 | 5 |
| >1200 | 1 |


**Daily spread_4h distribution**

| metric | value |
|---|---|
| mean | 148.22 |
| median | 114.42 |
| p1 | 67.10 |
| p5 | 74.07 |
| p25 | 88.18 |
| p50 | 114.42 |
| p75 | 185.80 |
| p95 | 318.38 |
| p99 | 400.49 |
| p99.9 | 474.57 |


**Days/year crossing spread_4h thresholds**

| metric | value |
|---|---|
| >200 | 65 |
| >300 | 27 |
| >360 | 14 |
| >400 | 6 |
| >450 | 1 |


**spread_4h trend:** -10.4 NIS/MWh per year (n=466 days)


**Concentration:** top 10 days = 6.1%, top 20 days = 11.3%, top 50 days = 23.5% of annual value.


### Day-Ahead vs Real-Time

| metric | value |
|---|---|
| mean | -0.18 |
| median | 0.07 |
| std | 10.98 |
| p1 | -28.30 |
| p5 | -15.62 |
| p25 | -5.66 |
| p50 | 0.07 |
| p75 | 5.58 |
| p95 | 14.84 |
| p99 | 25.04 |
| p99.9 | 54.76 |

## Stage 4 — Dispatch Model

| cycles_per_day | duration_hours | annual_revenue_per_mw_nis | cycles_run | days_observed | cycle_rate |
|---|---|---|---|---|---|
| 1 | 2 | 108,256.10 | 466 | 466 | 100.0% |
| 1 | 4 | 175,632.78 | 458 | 466 | 98.3% |
| 1 | 8 | 203,811.42 | 335 | 466 | 71.9% |
| 2 | 2 | 105,979.62 | 457 | 466 | 98.1% |
| 2 | 4 | 149,201.60 | 376 | 466 | 80.7% |
| 2 | 8 | 112,036.20 | 198 | 466 | 42.5% |

## Stage 5 — Financial Feasibility (base case)

- Capex/MW: 3,200,000.0 NIS
- Annual revenue/MW (base dispatch): 175,632.8 NIS
- NPV: -2,064,205.8 NIS/MW
- IRR (unlevered): -6.0%
- Payback: inf years
- Annuity factor (8%, 15y): 8.6
- Required gross revenue/MW-year to hit target return: 393,854.5 NIS
- Implied required spread_4h: 322.7 NIS/MWh
- **Actual spread_4h covers 45.3% of what's required for an unlevered 8% return.**


## Stage 6 — Sensitivities & Scenarios


### 6a. IRR heatmap (capex x spread multiplier)

| capex_per_kwh_nis | 0.7 | 0.85 | 1.0 | 1.15 | 1.3 |
|---|---|---|---|---|---|
| 600 | -8.0% | -5.2% | -2.8% | -0.6% | 1.3% |
| 700 | -9.5% | -6.8% | -4.6% | -2.6% | -0.7% |
| 800 | -10.8% | -8.2% | -6.0% | -4.1% | -2.4% |
| 900 | -11.8% | -9.4% | -7.3% | -5.4% | -3.8% |
| 1,000 | -12.8% | -10.4% | -8.4% | -6.6% | -5.0% |

### 6b. Price-cap scenario

| percentile_cap | cap_value_nis_mwh | annual_revenue_per_mw_nis | irr | irr_erosion_pp |
|---|---|---|---|---|
| none (actual) | nan | 175,632.78 | -6.0% | 0.00 |
| p99 | 235.99 | 155,352.77 | -7.6% | -1.51 |
| p97.5 | 218.48 | 153,200.65 | -7.7% | -1.68 |
| p95 | 191.51 | 145,574.13 | -8.3% | -2.30 |
| p90 | 146.69 | 122,736.35 | -10.4% | -4.33 |

### 6c. Spread compression scenario

| compression_pct_per_year | irr |
|---|---|
| 0.00 | -6.0% |
| 3.00 | -9.0% |
| 5.00 | -11.2% |
| 8.00 | -14.7% |

### 6d. Revenue gap to target return

- Gap: 218,221.8 NIS/MW-year (55.4% of required gross revenue)
