# Finding: Case-001 Transfusion Burden Quantification Gate

Date checked: 2026-04-28
Evidence label: de-identified case-context gate, guideline-backed calculation,
not diagnosis and not treatment advice

## Working Conclusion

Case-001 should carry an additional record label:

`transfusion_burden_unknown`

The family-reported weekly transfusion schedule is not enough to judge disease
severity, iron input, response to transfusion, or relevance of any candidate
therapy. The repo must treat the current interval as a prompt for measurement,
not as a conclusion.

The research-safe question is:

> What is the baseline transfusion requirement in total volume, pure red-cell
> volume, pre- and post-transfusion hemoglobin response, and estimated
> transfusional iron input?

## Why This Matters

TIF 2025 blood-transfusion guidance frames transfusion burden as calculable from
the administered unit volume or weight, the unit hematocrit, and the patient's
weight. It also explains that annual pure red-cell volume per kg can be
multiplied by `1.08` to estimate transfusional iron received per kg per year.

This converts "weekly transfusion" into a measurable packet:

```text
annual total volume = total transfused volume per year / body weight
annual pure red-cell volume = annual total volume x red-cell fraction
daily iron loading = annual pure red-cell volume x 1.08 / 365
```

Without these fields, the repo cannot distinguish high annual red-cell
requirement from small-volume weekly visits, shortened donor-cell survival,
immune hemolysis, hypersplenism, or a deliberate scheduling choice.

## Minimum Record Set

Ask a hematologist or transfusion unit for de-identified values covering the
last `6-12` months where available:

| Field | Why it matters |
| --- | --- |
| transfusion dates | Computes interval and observation window. |
| body weight at visits | Converts volume into `ml/kg` and `ml/kg/year`. |
| transfused volume or unit count | Separates visit frequency from total exposure. |
| unit hematocrit, Hb content, or red-cell fraction | Converts total volume into pure red-cell volume. |
| pre-transfusion Hb | Shows whether the regimen holds the target range. |
| post-transfusion Hb or increment | Detects under-response or shortened survival. |
| product type and matching policy | Explains volume, compatibility, and safety context. |
| reactions or delayed symptoms | Connects burden to immune/transfusion safety gates. |
| ferritin, LIC, cardiac `T2*`, and chelator context | Connects iron input to organ-risk interpretation. |

## Tooling Update

Nakafa Lab now treats the transfusion-burden calculator as a first-class gate:

- `scripts/calc_transfusion_burden.py` calculates interval, annualized
  `ml/kg/year`, annualized pure red-cell `ml/kg/year`, daily iron loading, and
  mean Hb values from a de-identified CSV.
- `scripts/selftest_transfusion_burden.py` verifies the synthetic weekly-log
  math and CSV validation rules without private data.
- `docs/transfusion-burden-calculator.md` documents private-log handling and
  clinician-review boundaries.

## Research Consequence

Candidate relevance remains blocked for case-001 until this packet is reviewed.
An HbF inducer, alpha-globin rebalancing idea, immune/transfusion intervention,
or iron-axis idea cannot be called relevant to this case from interval alone.

Use the durable label:

`transfusion_burden_unknown`

Then upgrade only when a clinician-reviewed packet gives enough data to assign
one or more narrower labels, such as `annual_volume_known`,
`pure_red_cell_volume_known`, `iron_input_known`, `hb_increment_known`, or
`transfusion_survival_under_review`.

## Islamic Motivation Boundary

Quran 55:7-9 is used here only as a `mizan` research-method anchor: measure
carefully and do not overstate claims. Quran 16:43 supports expert review by
qualified clinicians. Neither verse is used as biomedical evidence for a
treatment, dose, transfusion schedule, or chelation decision.

## Boundary

This finding does not decide whether the current transfusion schedule is right
or wrong. It does not recommend changing transfusion, chelation, immune
medicine, diet, supplements, or trial participation. It only defines the
minimum measurement gate before case-specific research claims can become
stronger.

## Sources

- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [Weekly transfusion differential map](2026-04-27-weekly-transfusion-differential-map.md)
- [Case-001 immune transfusion record gate](2026-04-28-case001-immune-transfusion-record-gate.md)
- [Case-001 iron chelation organ-risk record gate](2026-04-28-case001-iron-chelation-organ-risk-record-gate.md)
- [Transfusion burden calculator](../../../docs/transfusion-burden-calculator.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
