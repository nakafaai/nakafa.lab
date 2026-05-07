# Case-001 Public Collaborator Intake Gate

Date checked: 2026-05-07
Evidence label: operational public-collaboration gate, not medical advice

## Direct Answer

After owner outreach, response capture, and follow-up routing, the next blocker
is public collaborator intake. If Nakafa Lab is shared publicly, incoming help
must be sorted by role and scope before any private data or clinical claim is
discussed.

Case-001 should use this public-safe operational label:

`public_collaborator_intake_ready`

The goal is to convert public interest into bounded roles: clinical review,
transfusion medicine, genetics, iron/organ monitoring, trial or access routing,
assay review, software and reproducibility, privacy/security, funding/access,
or Islamic ethics review.

## Public-Safe Intake States

Use only these labels in public artifacts:

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

## Role Map

| Incoming helper role | Safe first ask | Next gate |
| --- | --- | --- |
| Hematologist or thalassemia clinician | Can you confirm labels or missing records for one domain? | owner outreach packet |
| Transfusion medicine or blood-bank owner | Can you review transfusion burden and immune/blood-bank record needs? | owner outreach packet |
| Molecular genetics or genetic counseling | Can you review subtype-confirmation record needs? | owner outreach packet |
| Iron, MRI, cardiology, endocrine, or organ owner | Can you review iron and organ-risk packet completeness? | owner outreach packet |
| Transplant, gene-cell therapy, or trial access owner | Can you explain screening pathway and blocking data, without deciding eligibility publicly? | specialist screening readiness |
| Wet-lab or assay partner | Can you review assay feasibility, readouts, safety controls, and quote requirements? | assay work order or lab quote brief |
| Data, software, or reproducibility contributor | Can you improve scripts, checks, notebooks, or source traceability without private records? | repo issue or scoped pull request |
| Privacy, security, or legal reviewer | Can you improve public/private boundaries without giving legal certification? | public release checklist or threat model |
| Funding, logistics, or access helper | Can you help with non-clinical access barriers without requesting raw records publicly? | private intake review |
| Islamic scholar or ethics reviewer | Can you review motivation, tafsir boundaries, and ethics without making biomedical claims? | Islamic research note |

## Public Call Boundary

A public call may say Nakafa Lab needs qualified help with thalassemia research,
record organization, privacy-safe tooling, assay planning, and access mapping.
It must not say that the repo has found a cure or that a specific treatment is
suitable for case-001.

Do not share raw lab reports, screenshots, exact dates, names, hospitals,
doctor messages, phone numbers, accession numbers, or patient-specific
treatment instructions in public replies or public repository files.

## Why This Matters

TIF 2025 separates transfusion-dependent thalassemia management into clinical
domains such as diagnosis, blood transfusion, iron overload, monitoring, HCT,
and gene manipulation. GeneReviews separates phenotype-level beta-thalassemia
labels from molecular confirmation and genetic counseling. ClinicalTrials.gov
records show active TDT advanced-therapy studies, but registry presence is only
screening context, not case eligibility. HHS de-identification guidance treats
medical records and laboratory reports with identifiers as protected health
information, and warns that de-identification reduces but does not eliminate
re-identification risk.

Therefore, public collaboration is useful only when it protects privacy and
routes each offer to a qualified, bounded task.

## Stop Conditions

This gate is complete for one public inquiry when:

1. the helper's role is recorded without publishing personal contact details;
2. the scope is matched or rejected;
3. no raw private records are shared publicly;
4. medical advice offers are blocked or routed to qualified private clinician
   review;
5. any public repo update remains label-only.

## Biomedical Boundary

This gate does not diagnose, dose, change transfusion, change chelation, change
immune medicine, recommend supplements, choose a referral, or decide trial
eligibility. It only defines how public offers of help are routed safely.

## Islamic Motivation Boundary

Quran 5:2 is used as a cooperation-in-goodness anchor. Quran 16:43 is used as
an expert-consultation anchor. Quran 55:7-9 is used as a measurement and
anti-exaggeration anchor. These are method boundaries, not biomedical evidence.

## Sources

- [Case-001 owner outreach packet](../case-context/case-001-owner-outreach-packet.md)
- [Case-001 owner follow-up ladder](../case-context/case-001-owner-follow-up-ladder.md)
- [Public case data release checklist](../../../templates/public-case-data-release-checklist.md)
- [Private case intake threat model](../../../docs/private-case-intake-threat-model.md)
- [HHS de-identification guidance](https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification/index.html)
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework)
- [TIF 2025 TDT guideline](https://www.ncbi.nlm.nih.gov/books/NBK614251/)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 gene manipulation chapter](https://www.ncbi.nlm.nih.gov/books/NBK614241/)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [ClinicalTrials.gov thalassemia search](https://clinicaltrials.gov/search?cond=Thalassemia)
- [Quran 5:2 cooperation anchor](../../islamic/quran/005-al-maidah/002.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
