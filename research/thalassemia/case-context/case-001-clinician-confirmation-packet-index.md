# Case-001 Clinician Confirmation Packet Index

Date: 2026-05-22
Status: public-safe clinician packet index, not treatment advice
Privacy: no raw records, exact dates, screenshots, doctor messages, clinician
names, hospital names, owner replies, contact details, or patient-specific
instructions

## Purpose

Use this when a clinician asks what needs to be confirmed. The goal is to make
the packet easy to read in order.

Current label: `case001_clinician_confirmation_packet_index_ready`

## Packet Order

1. Send the one-page doctor handoff first.
2. Attach original medical records privately, outside Git.
3. Ask the clinician to validate the public-safe working labels.
4. Ask which missing records should be requested first and from which owner.
5. Ask whether specialist screening is ready, data-missing, unsuitable,
   access-blocked, or already under review.
6. Use the mitapivat conversation sequence only after prerequisites pass.
7. Offer the main research paper only as an appendix.

## Stop Rule

If diagnosis category, transfusion category, missing-record owner, release
status, or specialist-readiness state is unclear, stop and return to records.
Public output should be labels only.

## Source-Backed Gates

- [Case-001 clinician confirmation packet index gate](../findings/2026-05-22-case001-clinician-confirmation-packet-index-gate.md)
- [Case-001 clinician response label capture](case-001-clinician-response-label-capture.md)
- [Case-001 doctor handoff brief](case-001-doctor-handoff-brief.md)
- [Case-001 minimum hematologist packet](case-001-minimum-hematologist-packet.md)
- [Case-001 mitapivat clinician conversation sequence](case-001-mitapivat-clinician-conversation-sequence.md)
