# Case-001 Mitapivat Minimum-Packet Readiness

Date: 2026-05-19
Status: public-safe packet readiness aid, not treatment advice
Privacy: no raw records, screenshots, identifiers, exact dates, contact
details, doctor messages, owner replies, or patient-specific instructions

## Purpose

Use this before asking the May 17 mitapivat clinician-review question. The goal
is to decide whether the packet is ready enough to ask, still missing records,
or blocked from public release.

Current label: `mitapivat_minimum_packet_readiness_ready`

## Required Domains

- diagnosis and genotype context;
- age and weight band;
- transfusion burden context;
- iron and organ context;
- liver safety context;
- medication interaction context;
- local access owner context.

## Allowed Readiness States

- `packet_not_ready`
- `packet_ready_for_clinician_question`
- `packet_private_release_blocked`

## Use Rule

If any domain is missing, ask for records first. If all seven domains are
label-ready and release-checked, use the May 17 clinician-review question. Do
not ask for treatment, dosing, trial screening, import, travel, or access
instructions.

## Source-Backed Gates

- [Case-001 mitapivat seven-domain owner action map](case-001-mitapivat-seven-domain-owner-action-map.md)
- [Case-001 mitapivat minimum-packet readiness gate](../findings/2026-05-19-case001-mitapivat-minimum-packet-readiness-gate.md)
- [Case-001 mitapivat clinician-review readiness](case-001-mitapivat-clinician-review-readiness.md)
- [Case-001 mitapivat clinician-answer action ladder](case-001-mitapivat-clinician-answer-action-ladder.md)
