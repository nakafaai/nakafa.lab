# Transfusion Burden Calculator

Status: de-identified engineering helper, not medical advice

## Purpose

Use this helper to turn a private, de-identified transfusion log into rough
transfusion-burden numbers:

- observed mean transfusion interval;
- total volume in `ml/kg`;
- annualized transfusion volume in `ml/kg/year`;
- annualized pure red-cell volume in `ml/kg/year`;
- estimated daily iron loading in `mg/kg/day`;
- mean pre- and post-transfusion hemoglobin if recorded.

This helps separate "weekly transfusion" from the real measurement question:
how much red-cell volume is being given per kg per year, and how fast Hb falls.

The calculation follows the TIF framing that annual transfusion requirements
can be expressed as total volume or pure red-cell volume per kg, and that pure
red-cell volume can be multiplied by `1.08` to estimate transfusional iron input
per kg before dividing by days.

## Input

Use the CSV header in
[transfusion-log-template.csv](../templates/transfusion-log-template.csv).

For case-context work, keep the public-safe label
`transfusion_dependent_burden_unquantified` until the private log has enough
fields for calculation and clinician review.

Required columns:

- `date`
- `body_weight_kg`
- `transfused_volume_ml`
- `red_cell_fraction`

Optional columns:

- `pre_hb_g_dl`
- `post_hb_g_dl`

Do not put names, hospital IDs, addresses, phone numbers, or photos in this
file. Keep patient logs under `private/`, which is ignored by git.

`red_cell_fraction` means the red-cell fraction of the transfused product. Use
the unit hematocrit as a decimal when the blood bank provides it, for example
`0.60` for 60%. If the value is not known, do not guess it in the public repo;
ask the hematologist or transfusion unit which value should be used.

## Command

```bash
UV_CACHE_DIR=/tmp/nakafa-uv-cache uv run python scripts/calc_transfusion_burden.py private/transfusion-log.csv
```

For machine-readable output:

```bash
UV_CACHE_DIR=/tmp/nakafa-uv-cache uv run python scripts/calc_transfusion_burden.py private/transfusion-log.csv --json
```

The JSON output includes:

- `row_count`
- `start_date`
- `end_date`
- `period_days`
- `mean_interval_days`
- `total_transfused_volume_ml`
- `total_volume_ml_per_kg`
- `annual_volume_ml_per_kg`
- `annual_pure_red_cell_ml_per_kg`
- `daily_iron_loading_mg_per_kg`
- `mean_pre_hb_g_dl`
- `mean_post_hb_g_dl`
- `warnings`

Warnings are expected when the log has only one row or covers fewer than 28
days. Short windows can be useful for debugging the data format, but they are
too noisy for case interpretation.

Use the
[case-001 transfusion burden readiness gate](../research/thalassemia/findings/2026-05-01-case001-transfusion-burden-readiness-gate.md)
before treating any aggregate as ready for clinician discussion.

## Verification

The synthetic self-test uses no private case data:

```bash
UV_CACHE_DIR=/tmp/nakafa-uv-cache uv run python scripts/selftest_transfusion_burden.py
```

## Public Repo Rule

Only commit the template, documentation, and de-identified aggregate findings.
Do not commit completed patient logs, raw records, screenshots, local source
paths, or clinician notes. Run the
[public case data release checklist](../templates/public-case-data-release-checklist.md)
before adding any new case-context facts to the public repo.

## Boundary

The calculation is only a preparation aid for clinician review. It does not
decide whether a transfusion schedule, chelation plan, splenectomy question, or
advanced therapy is appropriate.

Source anchor:
[TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/).
