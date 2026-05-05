# Case-001 Doctor Response Triage

Date: 2026-05-02
Status: de-identified clinician-response intake guide, not treatment advice
Privacy: no screenshots, names, phone numbers, hospital identifiers, raw chat
text, exact dates, or treatment instructions

## Purpose

Use this after a doctor replies to the handoff brief. The goal is to turn the
reply into labels, missing records, and next clinical owners without converting
private clinical advice into public repo claims.

## First Pass

Classify each doctor answer into one of five outcomes:

| Outcome | Meaning |
| --- | --- |
| `confirmed` | The current public-safe label is acceptable. |
| `corrected` | The doctor gave a better label. |
| `not_confirmable_missing_records` | The doctor named records needed before answering. |
| `not_applicable` | The domain does not apply to this case, with clinician rationale. |
| `under_specialist_review` | The domain belongs to another specialist or referral center. |

## Domain Map

| Domain | Current label | What to extract from the reply |
| --- | --- | --- |
| Diagnosis | `phenotype_only` | Corrected subtype/category and missing molecular records. |
| Clinical dependence | `transfusion_dependent_reported` | Whether the clinician uses TDT, NTDT with regular transfusion, HbE/beta-thalassemia, or another category. |
| Transfusion burden | `transfusion_dependent_burden_unquantified` | Whether the doctor asks for dates, weight, volume, red-cell fraction, pre-Hb, post-Hb, reactions, or interval. |
| Immune and blood-bank | `immune_transfusion_packet_missing` | Antibody screen, DAT/direct Coombs, matching policy, red-cell phenotype/genotype, reaction history, spleen, or hemolysis workup. |
| Iron, chelation, and organ risk | `iron_packet_missing` | Ferritin trend, LIC MRI, cardiac `T2*`, chelator identity, toxicity monitoring, and organ-risk screening. |
| Referral readiness | `advanced_therapy_referral_packet_missing` | Whether screening is ready, partial, data-missing, medically unsuitable, access-blocked, or under review. |

## Public Release Rule

Before writing any public case update:

1. remove clinician names, hospital names, phone numbers, screenshots, and exact
   dates;
2. summarize only the label, missing record, or next owner;
3. keep patient-specific treatment instructions private;
4. run the public case-data release checklist;
5. keep candidate relevance blocked unless the clinician explicitly closes the
   required domain gates.

## Owner Routing

If a response is `under_specialist_review`, `owner_unknown`, or names another
clinical service, use the
[case-001 specialist owner routing](case-001-specialist-owner-routing.md). Do
not interpret that domain until the correct owner is known or the owner marks it
not applicable.

For owner-specific replies after routing, use the
[case-001 owner response capture](case-001-owner-response-capture.md) guide
before writing public case labels.

## What Not To Do

- Do not publish a raw chat transcript.
- Do not publish screenshots.
- Do not interpret a medication, transfusion, chelation, immune, referral, or
  supplement comment as an instruction from the repo.
- Do not treat one answered domain as if all domains were answered.

## Source-Backed Gates

- [Case-001 doctor handoff brief](case-001-doctor-handoff-brief.md)
- [Case-001 doctor response triage gate](../findings/2026-05-02-case001-doctor-response-triage-gate.md)
- [Case-001 specialist owner routing](case-001-specialist-owner-routing.md)
- [Case-001 owner response capture](case-001-owner-response-capture.md)
- [Public case data release checklist](../../../templates/public-case-data-release-checklist.md)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 monitoring recommendations](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
