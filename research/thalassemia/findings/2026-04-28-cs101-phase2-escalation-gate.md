# Finding: CS-101 Phase 2 Escalation Gate

Date checked: 2026-04-28
Evidence label: clinical-registry benchmark, not treatment advice

## Direct Answer

`NCT07489196` makes the CS-101 benchmark stronger. The registered phase 2 China
study does not change Nakafa Lab's patient-facing boundary, but it raises the
novelty bar for the research program.

The defensible claim is no longer that HbF rescue through `HBG` promoter /
BCL11A biology is an open concept. It is that Nakafa Lab should test whether a
more affordable, safer, non-editing, lower-infrastructure candidate can pass a
comparable validation gate.

## What Was Found

| Item | Evidence | Meaning |
| --- | --- | --- |
| Trial record | `NCT07489196`, posted 2026-03-24, not yet recruiting | CS-101 has moved into a registered phase 2 development path. |
| Sponsor | CorrectSequence Therapeutics Co., Ltd | Same CS-101 development ecosystem as the phase 1 benchmark. |
| Location | China | Reinforces China as the highest-yield regional editing benchmark in this map. |
| Phase and enrollment | Phase 2, estimated 20 participants | Larger than the phase 1 Nature report but still registry evidence until results are posted or published. |
| Primary endpoints | adverse events, serious adverse events, overall survival, engraftment, transplant-related mortality, and 12-month transfusion independence with weighted mean hemoglobin threshold | The endpoint bar is clinical and transplant-style, not a simple HbF screen. |
| Secondary endpoints | 6-month transfusion independence, targeted editing efficiency in blood and marrow, HbF, and total hemoglobin | Confirms that HbF is measured beside persistence, hemoglobin, and clinical durability. |

## Impact On Novelty

`NCT07489196` upgrades the CS-101 lane from:

> small phase 1 report plus registry context

to:

> phase 1 Nature clinical signal plus phase 2 registry escalation.

That blocks weak novelty claims such as:

- "HbF rescue is unexplored";
- "`HBG` promoter / BCL11A reactivation is an empty lane";
- "a candidate is novel because it raises HbF."

The remaining Nakafa gap is:

- `affordability_gap`;
- `safety_gap`;
- `non_editing_validation_gap`;
- `integrated_assay_gap`.

## Operational Consequence

For every future candidate, record:

```text
closest_editing_benchmark: CS-101 / NCT06024876 plus NCT07489196 phase 2 registry escalation
proximity_novelty_label:
claimed_gap:
why_not_benchmark_only:
```

If the candidate cannot explain what it adds beyond the CS-101 development path,
it stays `hold`, `benchmark_only`, or `novelty_blocked`.

## Boundary

This finding does not recommend CS-101 or any therapy for any patient. It only
updates the external benchmark used for research triage and manuscript wording.

## Sources

- [ClinicalTrials.gov `NCT07489196`](https://clinicaltrials.gov/study/NCT07489196)
- [`NCT07489196` compact detail snapshot](../../../data/registries/clinicaltrials/2026-04-28-nct07489196-cs101-phase2-detail.json)
- [CS-101 phase 2 escalation notebook](../notebooks/2026-04-28-cs101-phase2-escalation-gate.ipynb)
- [CS-101 base-editing benchmark](2026-04-28-cs101-base-editing-benchmark.md)
