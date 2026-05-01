# Case-001 Transfusion Burden Readiness Gate

Date checked: 2026-05-01
Evidence label: de-identified data-readiness gate, not medical advice

## Direct Answer

Case-001 should keep the public-safe label:

`transfusion_dependent_burden_unquantified`

Regular transfusion dependence is already acknowledged in the public workflow.
The remaining blocker is whether the private log has enough high-quality fields
to calculate burden without guessing.

## Minimum Readiness Rule

Do not interpret burden until the private log has, at minimum:

- `date`;
- `body_weight_kg`;
- `transfused_volume_ml` or a clinician-approved unit-to-volume conversion;
- `red_cell_fraction` or unit hematocrit from the blood bank;
- `pre_hb_g_dl`;
- at least two transfusion rows;
- a window of at least 28 days.

`post_hb_g_dl`, product type, reactions, and matching context are not required
for the first calculation, but they are required for explaining why the interval
is short.

## Why This Matters

TIF 2025 explains that transfusion records can include administered unit volume
or weight, unit hematocrit, and patient weight. These fields allow annual blood
requirements to be calculated as total volume or pure red-cell volume per kg.
Pure red-cell volume multiplied by `1.08` estimates transfusional iron received
per kg per year.

Without those fields, "weekly transfusion" cannot distinguish high annual
requirement from small-volume visits, shortened red-cell survival, immune
hemolysis, spleen context, blood-bank complexity, or scheduling.

## Data Quality Outcomes

| Outcome | Meaning | Next action |
| --- | --- | --- |
| `ready_for_private_calculation` | Minimum fields are present with a sufficient window. | Run `scripts/calc_transfusion_burden.py` privately and bring the aggregate result to the clinician. |
| `format_debug_only` | The log runs but the window is too short or has too few rows. | Keep collecting rows; do not interpret annualized values. |
| `not_ready_missing_core_fields` | A core field is missing. | Ask the hospital, transfusion unit, or blood bank for the missing values. |
| `needs_clinician_conversion` | Unit count exists but volume or red-cell fraction is unknown. | Ask the clinician or blood bank for a conversion rule before calculating. |

## Repository Consequence

The calculator remains a private preparation aid. Public repo artifacts should
contain only templates, source aliases, data-readiness labels, and clinician-
reviewed aggregate summaries that pass the release checklist.

## Biomedical Boundary

This gate does not judge whether the transfusion schedule is correct, whether
chelation should change, or whether an advanced therapy is appropriate. It only
defines when the private transfusion log is ready for calculation and clinician
review.

## Islamic Motivation Boundary

Quran 55:7-9 is used as a measurement-discipline anchor: do not distort the
scale. Quran 16:43 is used as an expert-consultation anchor. These are not
biomedical evidence.

## Sources

- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [Transfusion burden calculator](../../../docs/transfusion-burden-calculator.md)
- [Case-001 doctor handoff brief](../case-context/case-001-doctor-handoff-brief.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
