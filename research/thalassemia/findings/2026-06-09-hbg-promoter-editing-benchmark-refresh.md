# Finding: HBG Promoter Editing Benchmark Refresh

Date checked: 2026-06-09
Evidence label: benchmark refresh and novelty gate, not treatment advice

## Direct Answer

The June 9 evidence refresh tightens the same conclusion started by `CS-101`:
HBG promoter editing and HbF-mediated transfusion independence are already
clinical benchmark territory. Nakafa Lab should not claim that HbF rescue,
HBG1/HBG2 promoter editing, or HPFH-like restoration is new by itself.

The useful open lane remains narrower:

> Can a cheaper, lower-infrastructure, non-editing candidate pass HbF or `HBG`,
> alpha-globin/autophagy, maturation, viability, and hemolysis gates before any
> clinical claim is made?

## What Changed

| Benchmark | Source | Why it matters |
| --- | --- | --- |
| EDIT-301 / reni-cel Cas12a HBG promoter editing | NEJM 2026, PMID `41931048`, DOI `10.1056/NEJMoa2501277` | Adds a global clinical HBG1/HBG2 promoter-editing benchmark alongside `CS-101`. |
| `CS-101` base-edited autologous CD34+ cells | Nature 2026, PMID `41951736`; `NCT06024876`; `NCT06065189`; `NCT07489196` | Keeps China and Asia base editing as the closest active HbF-restoration benchmark. |
| `VGB-Ex01` Cas12b HBG promoter editing | `NCT06041620` | Remains a registry comparator for HBG promoter editing, HbF induction, and red-cell survival logic. |

## Decision Rule

Reject or downgrade a candidate claim if it only says "raises HbF",
"reactivates gamma-globin", "copies HPFH", "targets HBG", or "could reduce
transfusions" without a validation path.

Keep a candidate researchable only if it adds affordability or lower
infrastructure, non-editing validation, HbF or `HBG` readout, alpha-globin or
autophagy readout, maturation and viability checks, hemolysis stop rules, and
clinician-reviewed relevance before patient-specific claims.

## Notebook Result

The notebook
[`2026-06-09-hbg-promoter-editing-benchmark-refresh.ipynb`](../notebooks/2026-06-09-hbg-promoter-editing-benchmark-refresh.ipynb)
returns:

```text
decision_label: hbg_promoter_editing_benchmark_refresh_active
HbF-only candidate claim: novelty_blocked_by_hbg_editing_benchmark
non-editing affordable dual-readout assay candidate: assay_gap_candidate
```

This does not change the June 7 and June 8 outreach gates. Lab contact remains
blocked until founder approval and recipient qualification are recorded.

## Islamic Motivation Boundary

Quran 13:17 remains useful as a research-method guardrail: let weak, noisy, or
unsafe claims disappear and keep only what benefits people after measurement.
This is motivation for disciplined evidence filtering, not biomedical evidence
for any intervention.

## Boundary

This finding does not provide diagnosis, dosing, supplement changes,
transfusion changes, chelation changes, referral decisions, trial screening,
travel guidance, import guidance, purchase guidance, or treatment advice.

## Sources

- [PubMed PMID `41931048`](https://pubmed.ncbi.nlm.nih.gov/41931048/)
- [PubMed PMID `41951736`](https://pubmed.ncbi.nlm.nih.gov/41951736/)
- [PubMed PMID `42024260`](https://pubmed.ncbi.nlm.nih.gov/42024260/)
- [ClinicalTrials.gov `NCT06024876`](https://clinicaltrials.gov/study/NCT06024876)
- [ClinicalTrials.gov `NCT06065189`](https://clinicaltrials.gov/study/NCT06065189)
- [ClinicalTrials.gov `NCT07489196`](https://clinicaltrials.gov/study/NCT07489196)
- [ClinicalTrials.gov `NCT06041620`](https://clinicaltrials.gov/study/NCT06041620)
- [PubMed compact snapshot](../../../data/literature/pubmed/2026-06-09-hbg-promoter-editing-benchmark-refresh.json)
- [ClinicalTrials.gov compact snapshot](../../../data/registries/clinicaltrials/2026-06-09-hbg-promoter-editing-benchmark-refresh.json)
- [Workflow JSON](../../../data/workflows/case-001/2026-06-09-hbg-promoter-editing-benchmark-refresh.json)
- [Quran 13:17 research-method note](../../islamic/quran/013-ar-rad/017.md)
