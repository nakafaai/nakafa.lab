# Finding: CS-101 Base-Editing Benchmark

Date checked: 2026-04-28
Evidence label: editing benchmark, not treatment advice

## Direct Answer

CS-101 is now a major Asia-based benchmark for the Nakafa Lab cure-oriented
map. It does not solve the Nakafa affordability question, but it raises the
evidence bar for any claim that HBG promoter editing and HbF rescue are an open
or unsolved therapeutic concept.

The strongest source found in this pass is the 2026 Nature phase 1 report
linked from the ClinicalTrials.gov record `NCT06024876`. The trial enrolled 5
participants with beta-thalassemia and used autologous CD34+ cells modified ex
vivo by transformer base editing. The target is the BCL11A binding motif in the
`HBG1/HBG2` promoters, with the goal of reactivating HbF.

## What Was Found

| Item | Evidence | Meaning |
| --- | --- | --- |
| Trial record | `NCT06024876`, completed, early phase 1, China, actual enrollment 5 | Registry-level confirmation of a small autologous base-editing trial. |
| Intervention | `CS-101`, autologous CD34+ hematopoietic stem-cell suspension modified by ex vivo base editing | This is a cell-therapy/editing benchmark, not a small-molecule or supplement lane. |
| Mechanism | BCL11A binding-site modification in the `HBG` promoter to restore gamma-globin and HbF | Directly overlaps the HPFH-like rescue biology Nakafa tracks. |
| Primary outcomes | Safety, engraftment, transplant-related mortality, all-cause mortality, transfusion independence for at least 6 months, time to last RBC transfusion | Strong endpoint benchmark for future assay and clinical translation claims. |
| Secondary outcomes | Total hemoglobin, HbF, intended genetic modification in blood and marrow | Useful benchmark for HbF and editing persistence readouts. |
| Publication | Nature 2026, PMID `41951736`, DOI `10.1038/s41586-026-10342-9` | Peer-reviewed clinical benchmark. |

## Nature Report Snapshot

The Nature abstract reports 5 treated patients, median follow-up of 23 months,
engraftment after infusion, all patients stopping red-cell transfusions, mean
total hemoglobin around 12.4 g/dL and HbF around 11.5 g/dL at month 3, and no
reported deaths or cancer occurrences in the abstract.

This is a powerful signal, but it has boundaries:

- only 5 patients in phase 1;
- autologous HSC collection, ex vivo editing, busulfan myeloablation, and
  transplant-style monitoring are required;
- it does not answer Indonesia affordability or infrastructure access;
- it does not validate natural products, oral small molecules, or no-lab
  interventions;
- longer follow-up and broader eligibility remain important.

## What This Changes

Before this finding, `VGB-Ex01` was the closest editing registry benchmark. Now
CS-101 is a stronger clinical-outcome benchmark because it has a peer-reviewed
Nature report connected to the registry.

The Nakafa Lab novelty statement should be:

> HBG promoter editing and HbF-mediated transfusion independence are no longer
> hypothetical. Nakafa Lab's open question is whether a cheaper, safer,
> non-editing or low-infrastructure candidate can pass a comparable
> multi-endpoint validation gate.

## Proximity Gate Update

For future candidate triage, the closest editing benchmark should be recorded
as:

```text
closest_editing_benchmark: CS-101 / NCT06024876, with VGB-Ex01 / NCT06041620 as a registry comparator
```

Any candidate that only says "increase HbF" is not novel. It must state what it
adds beyond:

- CS-101: clinical base-editing HbF benchmark;
- VGB-Ex01: registry-described HBG promoter-editing benchmark with alpha-chain
  burden and hemolysis logic;
- NCT07338344: non-editing luspatercept plus low-dose thalidomide benchmark.

## Practical Consequence

CS-101 pushes Nakafa Lab away from vague "find an HbF inducer" language. The
practical discovery gap is now:

1. affordability and access;
2. non-editing or lower-infrastructure validation;
3. dual HbF plus alpha-globin/autophagy readouts;
4. mature red-cell hemolysis exclusion;
5. clinician-reviewed patient relevance.

## Sources

- [ClinicalTrials.gov `NCT06024876`](https://clinicaltrials.gov/study/NCT06024876)
- [Nature 2026 CS-101 article](https://www.nature.com/articles/s41586-026-10342-9)
- [PubMed PMID `41951736`](https://pubmed.ncbi.nlm.nih.gov/41951736/)
- [`NCT06024876` compact detail snapshot](../../../data/registries/clinicaltrials/2026-04-28-nct06024876-cs101-detail.json)
- [CS-101 PubMed snapshot](../../../data/literature/pubmed/2026-04-28-cs101-base-editing-beta-thalassemia.json)
