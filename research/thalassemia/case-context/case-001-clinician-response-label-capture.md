# Case-001 Clinician Response Label Capture

Date: 2026-05-23
Status: public-safe clinician-response capture guide, not treatment advice
Privacy: no raw records, exact private dates, screenshots, doctor messages,
clinician names, hospital names, owner replies, contact details, or
patient-specific instructions

## Purpose

Use this after the May 22 clinician packet if a doctor replies. The goal is to
turn the reply into labels and next gates before any public repo update.

Current label: `case001_clinician_response_label_capture_ready`

## Capture Steps

1. Store the raw reply in the private workspace only.
2. Mark which domain was answered.
3. Classify the response as confirmed, corrected, not confirmable, not
   applicable, under specialist review, release-blocked, or private-only.
4. Record missing record categories and owner categories without identifiers.
5. If mitapivat is mentioned, classify the context before any action:
   adult-label, adult-trial benchmark, pediatric-watchlist, access owner,
   safety owner, or not clinically relevant now.
6. Release only labels after public release review passes.

## Stop Rule

If the answer contains treatment instructions, dosing, access/import/travel
instructions, trial-screening instructions, raw records, screenshots,
identifiers, or unclear free text, do not update the public case. Keep it
private and ask for a label or owner clarification.

## Source-Backed Gates

- [Case-001 clinician response label-capture gate](../findings/2026-05-23-case001-clinician-response-label-capture-gate.md)
- [Case-001 clinician confirmation packet index](case-001-clinician-confirmation-packet-index.md)
- [Case-001 doctor response triage](case-001-doctor-response-triage.md)
- [Case-001 mitapivat clinician conversation sequence](case-001-mitapivat-clinician-conversation-sequence.md)
