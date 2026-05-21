# Case-001 Mitapivat Clinician Conversation Sequence

Date: 2026-05-21
Status: public-safe clinician conversation aid, not treatment advice
Privacy: no raw records, exact dates, screenshots, doctor messages, owner
replies, contact details, or patient-specific instructions

## Purpose

Use this when a clinician asks what should be confirmed. The goal is to keep the
conversation ordered and stop before unsafe jumps.

Current label: `mitapivat_clinician_conversation_sequence_ready`

## Sequence

1. Confirm the scope: label validation and missing-record routing only.
2. Validate the core case labels.
3. Identify missing records and owner categories.
4. Confirm whether all seven mitapivat packet domains are privately label-ready
   and release-checked.
5. Ask the mitapivat review-readiness question only if the first four steps pass.
6. Reduce any answer through the May 18 action ladder before public recording.

## Stop Rule

Stop and return to records if diagnosis category, transfusion category, any
required domain, or release status is unclear. Public output should be labels
only.

## Source-Backed Gates

- [Case-001 mitapivat clinician conversation sequence gate](../findings/2026-05-21-case001-mitapivat-clinician-conversation-sequence-gate.md)
- [Case-001 mitapivat seven-domain owner action map](case-001-mitapivat-seven-domain-owner-action-map.md)
- [Case-001 mitapivat minimum-packet readiness](case-001-mitapivat-minimum-packet-readiness.md)
- [Case-001 mitapivat clinician-review readiness](case-001-mitapivat-clinician-review-readiness.md)
