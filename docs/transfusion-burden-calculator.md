# Transfusion Burden Calculator

Status: de-identified engineering helper, not medical advice

## Purpose

Use this helper to turn a transfusion log into rough transfusion-burden numbers:

- observed mean transfusion interval;
- total volume in `ml/kg`;
- annualized transfusion volume in `ml/kg/year`;
- annualized pure red-cell volume in `ml/kg/year`;
- estimated daily iron loading in `mg/kg/day`;
- mean pre- and post-transfusion hemoglobin if recorded.

This helps separate "weekly transfusion" from the real measurement question:
how much red-cell volume is being given per kg per year, and how fast Hb falls.

## Input

Use the CSV header in
[transfusion-log-template.csv](../templates/transfusion-log-template.csv).

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

## Command

```bash
python3 scripts/calc_transfusion_burden.py private/transfusion-log.csv
```

For machine-readable output:

```bash
python3 scripts/calc_transfusion_burden.py private/transfusion-log.csv --json
```

## Boundary

The calculation is only a preparation aid for clinician review. It does not
decide whether a transfusion schedule, chelation plan, splenectomy question, or
advanced therapy is appropriate.
