# Case-001 Specialist Owner Routing Gate

Date checked: 2026-05-03
Evidence label: operational specialist-routing gate, not medical advice

## Direct Answer

After the doctor handoff and doctor-response triage, the next blocker is owner
routing. One clinician reply should not be expected to resolve every domain.

Case-001 should use this public-safe operational label:

`specialist_owner_routing_needed`

The goal is to route each unresolved domain to the clinical owner most likely
to answer it or name the missing record.

## Owner Map

| Domain | Current public-safe label | Likely clinical owner | Output needed |
| --- | --- | --- | --- |
| Diagnosis and molecular subtype | `phenotype_only` | hematologist plus molecular genetics or genetic counseling | corrected subtype, `HBB` status, `HBA1/HBA2` status, and modifier/HPFH/delta-beta question |
| Clinical dependence category | `transfusion_dependent_reported` | hematologist or thalassemia clinic | TDT, NTDT with regular transfusion, HbE/beta-thalassemia, mixed disease, or still unconfirmed |
| Transfusion burden and response | `transfusion_dependent_burden_unquantified` | hematologist plus transfusion service | dates, volume, weight, red-cell fraction, pre/post Hb, reactions, interval, and annualized burden readiness |
| Immune and blood-bank risk | `immune_transfusion_packet_missing` | transfusion medicine or blood bank | antibody screen, named antibodies, DAT/direct Coombs, matching policy, red-cell phenotype/genotype, reaction and hemolysis context |
| Iron, chelation, and organ risk | `iron_packet_missing` | hematologist plus iron/MRI/cardiology/endocrine owners as needed | ferritin trend, LIC MRI, cardiac `T2*`, chelator monitoring, organ-risk packet |
| Advanced therapy or trial screening | `advanced_therapy_referral_packet_missing` | thalassemia specialist, transplant center, gene-cell therapy center, or trial team | ready, partial, data-missing, medically unsuitable, access-blocked, or under specialist review |

## Why This Matters

TIF 2025 separates the practical domains. Transfusion review needs target
pre-transfusion hemoglobin, interval, volume, antibody screen, red-cell matching,
and reaction context. Iron review needs ferritin trend, LIC, cardiac `T2*`, and
validated MRI interpretation. GeneReviews separates phenotype-level diagnosis
from molecular confirmation and family-risk genetics. HCT and gene manipulation
chapters are specialist-center domains rather than general research approvals.

Therefore, the safest next workflow is not "wait for the doctor." It is:

1. ask the first doctor to correct labels and name missing records;
2. route each unresolved domain to the right clinical owner;
3. keep all patient-specific candidate relevance blocked until the relevant
   owner closes the domain gate.

## Stop Conditions

This routing gate is complete when every unresolved domain has one of these
states:

- `owner_confirmed`;
- `owner_requested_records`;
- `owner_redirected`;
- `owner_marked_not_applicable`;
- `owner_marked_under_review`;
- `owner_unknown`.

`owner_unknown` is not failure. It means the next practical task is finding the
right clinical service, not interpreting the domain.

## Biomedical Boundary

This gate does not diagnose, dose, change transfusion, change chelation, change
immune medicine, recommend supplements, select referral, or decide eligibility.
It only assigns domains to likely specialist owners for safer review.

## Islamic Motivation Boundary

Quran 16:43 is used as an expert-consultation anchor. Quran 55:7-9 is used as a
measurement and anti-exaggeration anchor. These are method boundaries, not
biomedical evidence.

## Sources

- [Case-001 doctor response triage](../case-context/case-001-doctor-response-triage.md)
- [Case-001 specialist owner routing](../case-context/case-001-specialist-owner-routing.md)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 monitoring recommendations](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
- [TIF 2025 HCT chapter](https://www.ncbi.nlm.nih.gov/books/NBK614242/)
- [TIF 2025 gene manipulation chapter](https://www.ncbi.nlm.nih.gov/books/NBK614241/)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
