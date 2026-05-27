# Case-001 Advanced-Therapy Screening Owner Packet

Date checked: 2026-05-26
Status: public-safe doctor-facing owner map, not treatment advice

## Purpose

Use this note when a doctor asks what needs confirmation before any
advanced-therapy conversation. It is narrower than the main paper and more
ordered than the registry watchlist.

The question is:

> Which owner can label each missing domain before a hematologist or referral
> center decides whether advanced-therapy screening is reasonable?

## Current State

Current public label:

`advanced_therapy_referral_packet_missing`

Do not ask for trial selection, travel, import, product access, dosing, or a
treatment decision from this note.

## Owner Sequence

1. Diagnosis and genotype: hematologist or genetics owner.
2. Transfusion burden: hematologist or transfusion service.
3. Immune and blood-bank context: blood bank or transfusion medicine.
4. Iron, organ risk, and chelation: hematology plus organ specialists if
   needed.
5. Infection, fertility, and transplant readiness: transplant or
   advanced-therapy referral team.
6. Donor or HLA context: hematologist or transplant center, private only.
7. Access, center, and payer context: referral coordinator, center, or payer
   owner.

## Doctor-Facing Script

> We are not asking to choose HSCT, gene therapy, CRISPR therapy, or any trial
> today. We need to know which record domains are still missing, which owner
> should confirm them, and whether the packet is still missing, partial, or
> ready for specialist screening.

## Safe Public Outputs

- `advanced_therapy_referral_packet_missing`
- `advanced_therapy_referral_packet_partial`
- `advanced_therapy_referral_packet_ready_for_specialist_screening`
- `under_specialist_review`
- `medically_unsuitable`
- `access_blocked`
- `release_blocked_private_material`

## Privacy Boundary

Raw records, screenshots, doctor messages, names, hospitals, contact details,
exact private dates, owner replies, HLA details, and patient-specific
instructions stay outside Git.

Use the
[advanced-therapy clinician-answer ladder](case-001-advanced-therapy-clinician-answer-ladder.md)
after a doctor or specialist responds. It decides which public-safe label, if
any, can change state.

## Sources

- [May 26 owner-packet finding](../findings/2026-05-26-case001-advanced-therapy-screening-owner-packet-gate.md)
- [May 27 clinician-answer ladder](case-001-advanced-therapy-clinician-answer-ladder.md)
- [May 26 workflow map](../../../data/workflows/case-001/2026-05-26-advanced-therapy-screening-owner-packet.json)
- [Curative trial geography watchlist](case-001-curative-trial-geography-watchlist.md)
- [Minimum hematologist packet](case-001-minimum-hematologist-packet.md)
