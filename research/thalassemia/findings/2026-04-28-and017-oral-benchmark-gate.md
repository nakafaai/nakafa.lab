# Finding: AND017 Oral Benchmark Gate

Date checked: 2026-04-28
Evidence label: clinical-registry benchmark, not treatment advice

## Direct Answer

`NCT06302491` / AND017 is a meaningful China non-editing benchmark, but it does
not replace `NCT07338344` as the closest non-editing pharmacologic proximity
benchmark for Nakafa Lab's HbF-rich claim.

The useful role is narrower:

> AND017 should be tracked as an oral non-editing anemia, transfusion-load, red
> cell-index, and iron-marker benchmark.

It should not be described from this source snapshot as an HbF rescue,
alpha-globin cleanup, autophagy, cure, or patient-suitability candidate.

## What Was Found

| Item | Evidence | Meaning |
| --- | --- | --- |
| Registry record | `NCT06302491`, China, recruiting, phase 2 | Active oral non-editing thalassemia trial signal. |
| Design | randomized, parallel, quadruple-masked, placebo-controlled | Stronger than an open-label exploratory record. |
| Enrollment | estimated 64 participants | Larger than many early gene-editing benchmarks, but no results are posted. |
| Population | TDT and NTDT beta-thalassemia cohorts | Directly relevant to transfusion-burden and hemoglobin endpoints. |
| Intervention | AND017 capsules versus placebo | Oral comparator lane, not cell therapy or biologic backbone. |
| Primary endpoint | safety and tolerability at different oral doses | Primary role is safety gate, not cure or HbF proof. |
| Secondary endpoint groups | hemoglobin, red-cell and reticulocyte counts, red-cell indices, transferrin, TSAT, ferritin, serum iron, TIBC, transfusion load, transfusion count, and at least 33% transfusion-load reduction | Useful benchmark endpoints for anemia, transfusion, and iron-marker tracking. |

## Proximity Decision

`NCT06302491` is not a blank-field discovery lane. It means China also has an
active oral non-editing pharmacologic benchmark in beta-thalassemia.

However, this compact official-source pass did not show:

- HbF or gamma-globin endpoints;
- hemolysis endpoints;
- alpha-globin burden endpoints;
- autophagy endpoints;
- posted efficacy or safety results.

So the current benchmark map should stay:

| Benchmark role | Record |
| --- | --- |
| Closest editing benchmark | `CS-101` / `NCT06024876` plus `NCT07489196`; `VGB-Ex01` as integrated HBG/HbF/alpha-chain/hemolysis registry comparator |
| Closest non-editing HbF/hemolysis-rich pharmacologic benchmark | `NCT07338344`, luspatercept plus low-dose thalidomide |
| Oral non-editing anemia/transfusion/iron-marker watchlist benchmark | `NCT06302491`, AND017 |

## Operational Consequence

Future candidates should now answer two non-editing questions:

1. What does the candidate add beyond luspatercept plus low-dose thalidomide as
   the HbF/gamma-globin and hemolysis-rich non-editing comparator?
2. What does the candidate add beyond AND017 as an oral Hb, transfusion-load,
   red-cell-index, and iron-marker comparator?

If the answer is only "it is oral" or "it may improve hemoglobin," it is not a
novel Nakafa lead.

## Boundary

This finding does not recommend AND017 or any oral anemia drug for any patient.
It only updates the benchmark map used for research triage and manuscript
wording.

## Sources

- [ClinicalTrials.gov `NCT06302491`](https://clinicaltrials.gov/study/NCT06302491)
- [`NCT06302491` redacted compact snapshot](../../../data/registries/clinicaltrials/2026-04-28-nct06302491-and017-detail.json)
- [AND017 oral benchmark notebook](../notebooks/2026-04-28-and017-oral-benchmark-gate.ipynb)
