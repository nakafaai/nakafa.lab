# Finding: Experiment Status Boundary

Date checked: 2026-04-27
Evidence label: project-status boundary, not treatment advice

## Direct Answer

Nakafa Lab has not performed its own biological experiment yet.

So far, the repo has performed source-backed research, reproducible data
retrieval, computational prioritization, regulatory-access screening, and assay
design. That is more than passive reading, but it is not wet-lab evidence.

## What Counts As Done

| Layer | Done in repo? | Examples |
| --- | --- | --- |
| Literature/source retrieval | yes | PubMed, ClinicalTrials.gov, Quran/hadith, guideline, full-text, and regulatory snapshots |
| Computational prioritization | yes | candidate scoring, benchmark extraction, score sensitivity notebook |
| Regulatory/access screen | yes | BPOM product-search snapshots for advanced therapies, hydroxyurea, and sirolimus |
| Case-routing experiment design | yes | genotype-first intake gate, weekly-transfusion differential map, clinician question sheet |
| Assay design | yes | HbF, HPFH-like, red-cell metabolism, and hemolysis work orders |
| Wet-lab assay | no | no HbF reporter assay, no hemolysis assay, no cell culture run |
| Patient-sample experiment | no | no blood sample experiment |
| Animal experiment | no | no animal work |
| Clinical experiment | no | no clinical trial and no patient treatment recommendation |

## Interpretation

The current project is in a pre-experimental discovery phase. The strongest
output is a ranked, source-backed assay plan: test affordable or scalable
candidate lanes against HbF, F-cell distribution, globin-chain balance,
erythroid maturation, viability, and mature red-cell hemolysis.

Calling the current work an "experiment" is only accurate for computational and
reproducibility work. It is not accurate for biological validation.

## Next Evidence Upgrade

The next real evidence upgrade is a qualified-lab pilot panel that runs the
current candidates against:

- `HBG1` / `HBG2` messenger RNA;
- HbF protein;
- F-cell percentage;
- alpha/non-alpha globin balance;
- `ULK1`, p62 / `SQSTM1`, and autophagy readouts where relevant;
- erythroid maturation;
- viability and apoptosis;
- mature red-cell hemolysis.

Until that exists, every candidate remains a hypothesis, comparator, or
benchmark.

## Sources

- [First HbF and red-cell safety assay work order V0](../assays/2026-04-27-first-assay-work-order-v0.md)
- [Candidate scoring V0](../prioritization/2026-04-27-candidate-scoring-v0.md)
- [Research journal 2026-04-27](../../../docs/status/2026-04-27.md)
