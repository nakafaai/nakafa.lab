# Finding: YOLT-204 Registry Disambiguation Gate

Date checked: 2026-04-28
Evidence label: clinical-registry benchmark, not treatment advice

## Direct Answer

YOLT-204 should no longer be treated as only one ambiguous record.

The current source packet separates it into two China registry signals:

| Record | Current role | Boundary |
| --- | --- | --- |
| `NCT06678165` | TDT-specific YOLT-204 pilot record with safety, laboratory, sustained transfusion-reduction, and 3-month transfusion-independence primary endpoints. | Not yet recruiting in the compact source pass; no posted results; no cure, eligibility, or affordability claim. |
| `NCT07190001` | Mixed hemoglobinopathy YOLT-204 record with TDT/SCD wording plus HbF, F-cell, intended-modification, transfusion, and SCD vaso-occlusive endpoints. | The eligibility excerpt in the saved snapshot is heavily SCD-genotype oriented, so it should not be used alone as a TDT-specific evidence claim. |

The practical conclusion is:

> YOLT-204 is a high-interest China registry watchlist lane. It resolves part of
> the earlier ambiguity because `NCT06678165` is TDT-specific, but it does not
> displace `CS-101` as the strongest reported Asia editing benchmark or
> `VGB-Ex01` as the closest integrated HbF / alpha-chain / hemolysis registry
> comparator.

## What Changed

The earlier China proximity gate only highlighted `NCT07190001`, where the
trial title and condition mention TDT and SCD but the eligibility excerpt is
SCD-oriented. That made YOLT-204 hard to classify.

The targeted 2026-04-28 registry refresh found `NCT06678165`, a separate
YOLT-204 record titled for transfusion-dependent beta-thalassemia. Its compact
snapshot lists:

- China location;
- `YOLT-204` intervention;
- early phase 1 status;
- not-yet-recruiting status;
- primary outcomes for treatment-emergent adverse events, laboratory findings,
  safety measurements, sustained transfusion reduction, and 3-month transfusion
  independence.

That is enough to change the label from:

> "YOLT-204 is ambiguous."

to:

> "YOLT-204 has a TDT-specific registry watchlist record plus a separate mixed
> hemoglobinopathy/SCD-leaning record."

## Novelty Impact

This does not create a new Nakafa cure claim. It raises the benchmark bar.

Future candidates should now answer:

1. What do they add beyond `CS-101` and `NCT07489196` as the reported and
   phase-2-escalating Asia base-editing benchmark?
2. What do they add beyond `VGB-Ex01` as the integrated HbF, alpha-chain,
   hemolysis, and transfusion-need registry comparator?
3. What do they add beyond YOLT-204 as a China registry watchlist signal for
   TDT transfusion reduction and mixed HbF/F-cell endpoint design?

If the answer is only "this raises HbF" or "this may reduce transfusion," the
candidate is not a defensible Nakafa novelty claim.

## Operational Consequence

- Track `NCT06678165` and `NCT07190001` separately.
- Do not collapse them into one evidence claim.
- Keep YOLT-204 in the editing/HbF registry-watchlist section.
- Do not present YOLT-204 as published efficacy, cure evidence, patient
  eligibility evidence, or an affordable route.
- Keep CS-101 and VGB-Ex01 as the stronger benchmark anchors until YOLT-204 has
  posted results, a publication, or more detailed protocol evidence.

## Boundary

This finding does not recommend YOLT-204, gene editing, trial enrollment, or any
therapy for any patient. It only updates the benchmark map used for research
triage and manuscript wording.

## Sources

- [ClinicalTrials.gov `NCT06678165`](https://clinicaltrials.gov/study/NCT06678165)
- [ClinicalTrials.gov `NCT07190001`](https://clinicaltrials.gov/study/NCT07190001)
- [`NCT06678165` compact detail snapshot](../../../data/registries/clinicaltrials/2026-04-28-nct06678165-yolt204-tdt-detail.json)
- [`NCT07190001` compact detail snapshot](../../../data/registries/clinicaltrials/2026-04-27-nct07190001-yolt204-detail.json)
- [YOLT-204 registry disambiguation notebook](../notebooks/2026-04-28-yolt204-registry-disambiguation-gate.ipynb)
