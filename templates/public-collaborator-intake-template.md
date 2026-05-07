# Public Collaborator Intake Template

Status: public-safe intake template, not treatment advice
Privacy: completed private copies may include contact details and must stay in
ignored private storage unless reduced to role-only labels

## Inquiry Metadata

| Field | Value |
| --- | --- |
| Inquiry alias |  |
| Public channel |  |
| Generalized timing |  |
| Claimed role |  |
| Scope offered |  |
| Public-safe state |  |

## Role Classification

Choose one role:

- `hematology_or_thalassemia_clinician`;
- `transfusion_medicine_or_blood_bank`;
- `molecular_genetics_or_genetic_counseling`;
- `iron_mri_cardiology_endocrine_or_organ_owner`;
- `transplant_gene_cell_therapy_or_trial_access`;
- `wet_lab_or_assay_partner`;
- `data_software_or_reproducibility`;
- `privacy_security_or_legal_boundary`;
- `funding_logistics_or_access`;
- `islamic_scholar_or_ethics`;
- `unknown_or_unverified`.

## Public-Safe State

Choose one state:

- `public_call_ready`;
- `inquiry_received`;
- `role_unverified`;
- `qualified_role_claimed`;
- `scope_matched`;
- `scope_mismatch`;
- `private_intro_needed`;
- `do_not_share_private_records`;
- `declined_or_spam`;
- `blocked_medical_advice`.

## Release Check

- No raw patient records are requested or shared publicly.
- No clinician name, hospital name, phone number, screenshot, local path, exact
  date, accession number, or full lab value is included in public text.
- No patient-specific treatment instruction is included in public text.
- Public update is role-only, state-only, or task-scope only.
- `scripts/check_public_repo.py` passes before commit.
