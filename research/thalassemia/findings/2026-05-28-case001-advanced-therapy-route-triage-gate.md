# Case-001 Advanced-Therapy Route Triage Gate

Date checked: 2026-05-28
Evidence label: guideline, regulator, workflow, and privacy synthesis, not
medical advice

## Direct Answer

After the owner packet and answer ladder, the next blocker is route confusion:
HSCT, autologous gene-cell therapy, disease-modifying drugs, standard-care
stabilization, and registry/trial monitoring must not be mixed.

Current operational label:

`case001_advanced_therapy_route_triage_ready`

This label does not choose a therapy. It only defines which specialist branch
can be asked which question.

## Route Branches

| Branch | What it asks | What it does not do |
| --- | --- | --- |
| `allogeneic_hsct_branch_owner_question` | Whether HLA/donor-based transplant evaluation belongs in scope after packet review. | Does not publish HLA, donor, or family-identifying details. |
| `autologous_gene_cell_branch_owner_question` | Whether a gene-addition or gene-editing center considers screening reasonable. | Does not infer product access, manufacturing feasibility, or eligibility. |
| `disease_modifying_noncurative_branch_owner_question` | Whether non-curative drugs should be reviewed separately from curative-route screening. | Does not treat transfusion-reduction drugs as cures. |
| `standard_care_stabilization_first` | Whether iron, immune, infection, organ, or transfusion blockers must be stabilized first. | Does not change transfusion, chelation, immune, or infection care. |
| `trial_registry_benchmark_only` | Whether a registry record is benchmark context only. | Does not create trial-screening, travel, or import instructions. |

## Evidence Boundary

TIF 2025 HSCT guidance supports allogeneic HCT as a curative benchmark that
requires donor-route review, pre-transplant workup, iron and organ assessment,
fertility assessment, conditioning, follow-up, and expert thalassemia-transplant
centers.

TIF 2025 gene-manipulation guidance and FDA Casgevy/Zynteglo pages support
autologous gene-addition and gene-editing product categories. These sources do
not establish local access, affordability, center availability, or individual
suitability.

## Decision Rule

Route triage can name the branch question. It cannot select a therapy, infer
eligibility, infer access, or bypass clinician review.

## Islamic Motivation Boundary

Quran 16:43 supports expert consultation. Quran 49:6 supports verification
before acting. Quran 55:7-9 supports measured claims. These are process
anchors, not biomedical evidence for any therapy.

## Sources

- [May 28 route-triage workflow map](../../../data/workflows/case-001/2026-05-28-advanced-therapy-route-triage.json)
- [May 27 clinician-answer ladder](../case-context/case-001-advanced-therapy-clinician-answer-ladder.md)
- [TIF 2025 HSCT chapter](https://www.ncbi.nlm.nih.gov/books/NBK614242/)
- [TIF 2025 gene manipulation chapter](https://www.ncbi.nlm.nih.gov/books/NBK614241/)
- [FDA Casgevy product page](https://www.fda.gov/vaccines-blood-biologics/casgevy)
- [FDA Zynteglo product page](https://www.fda.gov/vaccines-blood-biologics/zynteglo)
- [Private case intake threat model](../../../docs/private-case-intake-threat-model.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
