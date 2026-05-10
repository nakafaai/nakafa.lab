# Case-001 Registry Link Disambiguation Gate

Date checked: 2026-05-10
Evidence label: registry triage gate, not medical advice

## Direct Answer

After responder qualification, the next blocker is registry-link
disambiguation. If someone sends a trial or center link, Nakafa Lab must first
classify the record before it becomes a clinician question.

Case-001 should use this label:

`registry_link_disambiguation_ready`

## Why This Matters

The 2026-05-09 ClinicalTrials.gov query returned `total_count=37`, but the first
page mixed direct TDT records with query-adjacent records. A 2026-05-10 lookup
also found `NCT07506863`, a not-yet-recruiting pediatric mitapivat TDT record,
while the first-page sibling `NCT07517133` is pediatric mitapivat NTDT.

That distinction matters: a registry hit is an access-mapping clue, not
eligibility, treatment advice, or a case-specific recommendation.

## Allowed Registry States

- `registry_link_received`;
- `nct_id_parsed`;
- `direct_tdt_context`;
- `query_adjacent_context`;
- `access_mapping_only`;
- `owner_review_needed`;
- `not_case_eligibility`;
- `release_blocked`.

## Disambiguation Rules

| Question | Safe rule |
| --- | --- |
| Is there an `NCT` ID? | If not, ask for the registry ID or official URL before discussing. |
| Is the record TDT, NTDT, iron-axis, transplant, or follow-up? | Classify the domain before linking it to a case question. |
| Is it recruiting or not-yet-recruiting? | Treat status as access context only. |
| Is there a country or center? | Record geography as access mapping, not availability for case-001. |
| Is it a drug, gene-cell therapy, transplant, or monitoring study? | Route to the matching clinical owner. |

## Biomedical Boundary

This gate does not diagnose, dose, change transfusion, change chelation,
recommend mitapivat, select gene therapy, select transplant, or decide trial
eligibility.

## Islamic Motivation Boundary

Quran 49:6 is used as a report-verification anchor. Quran 16:43 is used as an
expert-consultation anchor. Quran 55:7-9 is used as a measurement and
anti-exaggeration anchor. These are method boundaries, not biomedical evidence.

## Sources

- [ClinicalTrials.gov 2026-05-09 TDT query refresh](../../../data/registries/clinicaltrials/2026-05-09-active-tdt-registry-refresh.json)
- [NCT07506863 pediatric mitapivat TDT detail](../../../data/registries/clinicaltrials/2026-05-10-nct07506863-mitapivat-pediatric-tdt-detail.json)
- [ClinicalTrials.gov NCT07506863](https://clinicaltrials.gov/study/NCT07506863)
- [ClinicalTrials.gov NCT07517133](https://clinicaltrials.gov/study/NCT07517133)
- [TIF 2025 TDT guideline](https://www.ncbi.nlm.nih.gov/books/NBK614251/)
- [TIF 2025 gene manipulation chapter](https://www.ncbi.nlm.nih.gov/books/NBK614241/)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [HHS de-identification guidance](https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification/index.html)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
