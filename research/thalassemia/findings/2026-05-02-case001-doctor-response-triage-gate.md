# Case-001 Doctor Response Triage Gate

Date checked: 2026-05-02
Evidence label: operational clinician-response gate, not medical advice

## Direct Answer

The next blocker after sending the doctor handoff is response triage.

The doctor response should not be treated as a free-form approval or rejection
of Nakafa Lab research. It should be converted into a small set of labels:

- `confirmed`;
- `corrected`;
- `not_confirmable_missing_records`;
- `not_applicable`;
- `under_specialist_review`.

Anything outside those labels should stay in private notes until it is either
clarified by the clinician or reduced to a de-identified public-safe summary.

## Why This Matters

TIF 2025 makes the clinical review multi-domain: diagnosis and molecular context
matter, transfusion targets and volume matter, antibody screen and matching
matter, and iron/organ monitoring matters. A short doctor reply can therefore
answer one domain while leaving the others blocked.

The triage gate prevents a common failure mode: reading one clinician comment as
if it resolved diagnosis, transfusion burden, blood-bank risk, iron risk, and
advanced-therapy readiness at the same time.

## Response Fields To Capture Privately

Capture only these fields in the private workspace:

- clinician role, not name;
- date received, generalized before any public release;
- domain answered;
- exact label correction or missing-record request;
- whether the answer is definitive, provisional, or not confirmable;
- next clinical owner if the doctor names one;
- whether follow-up records are needed before interpretation.

Do not put screenshots, names, phone numbers, hospital identifiers, or raw chat
text in the public repo.

## Public-Safe Triage Outputs

| Domain | Current label | Allowed public-safe update |
| --- | --- | --- |
| Diagnosis | `phenotype_only` | `confirmed`, `corrected`, or `not_confirmable_missing_records` with the missing molecular record named generically. |
| Clinical dependence | `transfusion_dependent_reported` | corrected category such as TDT, NTDT with regular transfusion, HbE/beta-thalassemia, or still unconfirmed. |
| Transfusion burden | `transfusion_dependent_burden_unquantified` | burden remains unquantified until date, weight, volume, red-cell fraction, and Hb response fields are available. |
| Immune and blood-bank | `immune_transfusion_packet_missing` | antibody, DAT, matching, reaction, spleen, or hemolysis packet status only. |
| Iron, chelation, and organ risk | `iron_packet_missing` | ferritin trend, LIC, cardiac `T2*`, chelator-monitoring, or organ-screen status only. |
| Referral readiness | `advanced_therapy_referral_packet_missing` | ready, partial, data-missing, medically unsuitable, access-blocked, or under specialist review. |

## Stop Conditions

The doctor-response sprint stops only when one of these is true:

1. the clinician gives corrected labels and a missing-record list;
2. the clinician says the labels cannot be validated without named records;
3. the clinician redirects the case to another specialist owner;
4. the response contains patient-specific treatment instructions that must stay
   private and cannot be converted into public repo content.

## Biomedical Boundary

This gate does not diagnose, change transfusion, change chelation, change immune
medicine, recommend supplements, select referral, or decide trial eligibility.
It only defines how to structure a clinician response safely.

## Islamic Motivation Boundary

Quran 16:43 is used as an expert-consultation anchor. Quran 55:7-9 is used as a
measurement and anti-exaggeration anchor. These are method boundaries, not
biomedical evidence.

## Sources

- [Case-001 doctor handoff brief](../case-context/case-001-doctor-handoff-brief.md)
- [Case-001 doctor response triage](../case-context/case-001-doctor-response-triage.md)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 monitoring recommendations](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
