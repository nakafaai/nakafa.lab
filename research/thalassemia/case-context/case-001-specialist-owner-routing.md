# Case-001 Specialist Owner Routing

Date: 2026-05-03
Status: de-identified clinical-owner routing guide, not treatment advice
Privacy: no raw records, screenshots, identifiers, exact dates, clinician names,
hospital names, or patient-specific treatment instructions

## Purpose

Use this after the doctor handoff or doctor-response triage. The goal is to
decide which clinical owner should answer each unresolved domain.

This is not a referral instruction. It is a structured way to ask, "Who is the
right qualified reviewer for this missing piece?"

## Routing Table

| Domain | Ask this owner first | What they should return |
| --- | --- | --- |
| Diagnosis and molecular subtype | hematologist, then molecular genetics or genetic counseling if needed | corrected subtype and missing molecular records |
| Clinical dependence category | hematologist or thalassemia clinic | TDT, NTDT with regular transfusion, HbE/beta-thalassemia, mixed disease, or unconfirmed |
| Transfusion burden and Hb response | hematologist plus transfusion service | transfusion volume, interval, weight, unit hematocrit/red-cell fraction, pre/post Hb, and reaction context |
| Immune and blood-bank risk | transfusion medicine or blood bank | antibody screen, named antibodies, DAT/direct Coombs, matching policy, phenotype/genotype, reaction and hemolysis context |
| Iron, chelation, and organ risk | hematologist plus MRI/cardiology/endocrine owners as needed | ferritin trend, LIC, cardiac `T2*`, chelator monitoring, and organ-risk status |
| Advanced therapy or trial screening | thalassemia specialist, transplant center, gene-cell therapy center, or trial team | ready, partial, data-missing, medically unsuitable, access-blocked, or under specialist review |

## Public-Safe Owner States

Use only these public labels:

- `owner_confirmed`;
- `owner_requested_records`;
- `owner_redirected`;
- `owner_marked_not_applicable`;
- `owner_marked_under_review`;
- `owner_unknown`.

Do not publish raw clinician messages, names, hospital names, phone numbers,
screenshots, or treatment instructions.

## Next Action Rule

If the owner is unknown, the next action is outreach routing, not biomedical
interpretation. If an owner asks for records, return to the private source index
and record request matrix. If an owner gives patient-specific treatment
instructions, keep them private and do not convert them into public repo claims.

Once a likely owner is known, use the
[Case-001 owner outreach packet](case-001-owner-outreach-packet.md) instead of
sending the full research paper as the first-contact artifact.

## Source-Backed Gates

- [Case-001 doctor response triage](case-001-doctor-response-triage.md)
- [Case-001 specialist owner routing gate](../findings/2026-05-03-case001-specialist-owner-routing-gate.md)
- [Case-001 owner outreach packet](case-001-owner-outreach-packet.md)
- [Case-001 owner outreach packet gate](../findings/2026-05-04-case001-owner-outreach-packet-gate.md)
- [Case-001 record request matrix](case-001-record-request-matrix.md)
- [Public case data release checklist](../../../templates/public-case-data-release-checklist.md)
