# Proximity Novelty Gate V0

Date: 2026-04-28
Scope: candidate triage and lab-pitch guardrail, not treatment advice

## Purpose

This gate prevents Nakafa Lab from overstating novelty after two close
editing and non-editing benchmarks were identified:

- `CS-101` / `NCT06024876`: China phase 1 autologous CD34+ base editing at the
  BCL11A binding motif in the `HBG1/HBG2` promoters, with a 2026 Nature report
  describing transfusion independence in 5 treated patients.
- `NCT07489196`: China phase 2 CS-101 registry escalation, not yet recruiting,
  with safety, survival, engraftment, 12-month transfusion-independence,
  targeted-editing, HbF, and total-hemoglobin endpoints.
- `VGB-Ex01` / `NCT06041620`: ex vivo `HBG1/2` promoter editing with HbF,
  alpha-chain burden, red-cell survival, hemolysis, and transfusion-need logic
  in the registry description.
- `NCT07338344`: luspatercept plus low-dose thalidomide, a non-editing
  pharmacologic trial with transfusion burden, HbF/gamma-globin, hemolysis,
  iron, and safety endpoints.

## Required Question

Before a candidate is promoted, answer:

> What does this candidate add beyond the closest editing benchmark and the
> closest non-editing pharmacologic benchmark?

If that answer is vague, the candidate stays `hold` or `reject`.

## Gate Labels

| Label | Meaning | Action |
| --- | --- | --- |
| `benchmark_only` | The lane mainly reproduces a known benchmark or clinical comparator. | Use as endpoint standard, not discovery claim. |
| `incremental_variant` | The lane changes material, dose, geography, or combination but not the core mechanism or endpoints. | Keep as literature context until a clear affordability or safety advantage is shown. |
| `affordability_gap` | The lane could reduce cost, access burden, or infrastructure compared with known benchmarks. | Keep only if identity and safety gates are strong. |
| `safety_gap` | The lane could avoid myeloablation, expensive biologics, thalidomide-class toxicity, or mature red-cell damage. | Promote to assay only if safety readouts are explicit. |
| `integrated_assay_gap` | The lane has a realistic plan to measure HbF/F-cells, alpha-globin/autophagy, maturation, hemolysis, iron-risk, and access. | Promote to lab-quote candidate if identity and controls are ready. |
| `novelty_blocked` | The lane does not differ meaningfully from `CS-101`, `VGB-Ex01`, luspatercept plus thalidomide, or known HbF inducer classes. | Do not pitch as novel. |

## Promotion Rule

A candidate can move above `hold` only if it has at least one defensible gap:

- lower-cost or more accessible than luspatercept, gene therapy, or editing;
- safer or more monitorable than thalidomide-class or cytotoxic HbF biology;
- measurable in a qualified lab with dual HbF plus alpha-globin/autophagy
  readouts;
- useful as a comparator or rejection control without being framed as a cure.

## Required Assay Metadata

Every assay run should record:

```text
closest_editing_benchmark:
phase2_escalation:
closest_non_editing_benchmark:
proximity_novelty_label:
claimed_gap:
why_not_benchmark_only:
```

## Current Decision

The current Nakafa Lab gap is:

`affordability_gap` + `safety_gap` + `integrated_assay_gap`.

That is narrower than "new cure" and stronger than "random supplement screen."
It asks whether any practical candidate can pass the same kind of multi-endpoint
scrutiny as the closest editing and non-editing benchmarks.

## Sources

- [CS-101 base-editing benchmark](../findings/2026-04-28-cs101-base-editing-benchmark.md)
- [CS-101 phase 2 escalation gate](../findings/2026-04-28-cs101-phase2-escalation-gate.md)
- [China HbF editing proximity gate](../findings/2026-04-27-china-hbf-editing-proximity-gate.md)
- [Non-editing pharmacologic proximity gate](../findings/2026-04-28-non-editing-pharmacologic-proximity-gate.md)
- [`NCT06024876` compact detail snapshot](../../../data/registries/clinicaltrials/2026-04-28-nct06024876-cs101-detail.json)
- [`NCT07489196` compact detail snapshot](../../../data/registries/clinicaltrials/2026-04-28-nct07489196-cs101-phase2-detail.json)
- [`NCT06041620` compact detail snapshot](../../../data/registries/clinicaltrials/2026-04-27-nct06041620-vgb-ex01-detail.json)
- [`NCT07338344` compact detail snapshot](../../../data/registries/clinicaltrials/2026-04-27-nct07338344-luspatercept-thalidomide-detail.json)
- [ClinicalTrials.gov `NCT06024876`](https://clinicaltrials.gov/study/NCT06024876)
- [ClinicalTrials.gov `NCT07489196`](https://clinicaltrials.gov/study/NCT07489196)
- [ClinicalTrials.gov `NCT06041620`](https://clinicaltrials.gov/study/NCT06041620)
- [ClinicalTrials.gov `NCT07338344`](https://clinicaltrials.gov/study/NCT07338344)
