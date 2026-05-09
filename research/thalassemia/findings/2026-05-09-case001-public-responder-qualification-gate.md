# Case-001 Public Responder Qualification Gate

Date checked: 2026-05-09
Evidence label: operational qualification gate, registry context, not medical advice

## Direct Answer

After the public share kit, the next blocker is responder qualification. Public
replies must become role, scope, evidence link, and safe next state before any
private introduction or clinical interpretation.

Case-001 should use this label:

`public_responder_qualification_ready`

## Allowed States

- `role_claim_received`;
- `scope_matched`;
- `credential_or_source_needed`;
- `private_intro_ready`;
- `repo_task_ready`;
- `release_blocked`;
- `blocked_raw_record_request`;
- `blocked_treatment_advice`.

## Qualification Questions

| Reply type | First safe question |
| --- | --- |
| Clinical or genetics role | Which domain can you review, and can you keep this to missing-record or label confirmation? |
| Advanced-therapy or trial-access role | Which trial, center, registry ID, or access pathway are you referencing? |
| Wet-lab or assay role | Which assay, readout, biosafety constraint, sample requirement, and quote boundary can you review? |
| Software, privacy, funding, logistics, or ethics role | Which scoped task can you do without private records or treatment advice? |

## Registry Refresh

A ClinicalTrials.gov API refresh on 2026-05-09 for the query
`transfusion dependent beta thalassemia` returned `total_count=37`. The saved
first page includes TDT gene-modified autologous cell records and query-adjacent
NTDT, iron-axis, BCL11A enhancer editing, transplant, EDIT-301, and long-term
follow-up records.

This is referral and access context only. It is not case eligibility and not a
recommendation.

## Blockers

- Do not treat a public role claim as proof of qualification.
- Do not share raw records in public.
- Do not accept public patient-specific treatment advice.
- Do not infer eligibility from a registry listing.
- Do not move to private introduction until the role and bounded task are clear.

## Biomedical Boundary

This gate does not diagnose, dose, change transfusion, change chelation,
recommend supplements, select curative therapy, or decide trial eligibility.

## Islamic Motivation Boundary

Quran 16:43 supports asking qualified people when knowledge is missing, and
Quran 55:7-9 supports careful measurement and avoiding distorted claims. These
are method anchors, not biomedical evidence.

## Sources

- [Case-001 public share kit](../case-context/case-001-public-share-kit.md)
- [Public responder qualification template](../../../templates/public-responder-qualification-template.md)
- [ClinicalTrials.gov TDT query refresh](../../../data/registries/clinicaltrials/2026-05-09-active-tdt-registry-refresh.json)
- [ClinicalTrials.gov query URL](https://clinicaltrials.gov/api/v2/studies?query.cond=transfusion+dependent+beta+thalassemia&filter.overallStatus=RECRUITING%2CNOT_YET_RECRUITING%2CACTIVE_NOT_RECRUITING&pageSize=10&countTotal=true)
- [TIF 2025 TDT guideline](https://www.ncbi.nlm.nih.gov/books/NBK614251/)
- [TIF 2025 gene manipulation chapter](https://www.ncbi.nlm.nih.gov/books/NBK614241/)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [HHS de-identification guidance](https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification/index.html)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
