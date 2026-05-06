# Case-001 Owner Follow-Up Ladder

Date: 2026-05-06
Status: de-identified owner-follow-up ladder, not treatment advice
Privacy: no raw replies, screenshots, identifiers, exact dates, clinician names,
hospital names, phone numbers, local paths, or patient-specific treatment
instructions

## Purpose

Use this after owner outreach is sent. The goal is to decide the next
non-clinical action without repeating broad messages or publishing private
communication.

This ladder answers: "What do we do if the owner does not answer, redirects, or
asks for records?"

## Current Follow-Up Label

`owner_follow_up_ladder_ready`

## Allowed Public States

- `follow_up_not_due`;
- `follow_up_ready`;
- `follow_up_sent`;
- `records_pending`;
- `owner_redirected`;
- `alternate_owner_needed`;
- `response_captured_private`;
- `route_closed_label_only`;
- `release_blocked`.

## Ladder

| Situation | Private action | Public-safe label |
| --- | --- | --- |
| Outreach has not been sent | Send only the owner-specific row. | `follow_up_not_due` |
| Outreach was sent and no reply is recorded | Send one short follow-up asking if this is the right owner. | `follow_up_sent` |
| Owner requests records | Use the private source index and record request matrix. | `records_pending` |
| Owner redirects | Route to the new owner role. | `owner_redirected` |
| Owner cannot review | Choose an alternate owner route or keep unresolved. | `alternate_owner_needed` |
| Owner replies with domain content | Use the response-capture guide. | `response_captured_private` |
| Owner closes a label and release checks pass | Update only the label. | `route_closed_label_only` |
| Reply contains identifiers or treatment instructions | Keep private and block release. | `release_blocked` |

## Follow-Up Message Shape

Keep follow-up messages short and domain-specific:

1. name the owner route;
2. ask whether this owner can answer the specific domain;
3. ask which record is missing if they cannot answer yet;
4. ask which owner role should review it if this is the wrong route.

Do not attach the whole research paper unless the owner asks for background.

## Private Handling Rules

- Track raw replies and follow-up details only in ignored private storage.
- Public repo may record only the allowed state and the owner role.
- Patient-specific treatment instructions remain private and clinician-owned.
- A record request returns to the record request matrix.
- A redirect returns to specialist-owner routing.
- A reply with content returns to owner response capture.

## Source-Backed Gates

- [Case-001 owner outreach packet](case-001-owner-outreach-packet.md)
- [Case-001 owner response capture](case-001-owner-response-capture.md)
- [Case-001 owner follow-up ladder gate](../findings/2026-05-06-case001-owner-follow-up-ladder-gate.md)
- [Case-001 specialist owner routing](case-001-specialist-owner-routing.md)
- [Case-001 record request matrix](case-001-record-request-matrix.md)
- [Public case data release checklist](../../../templates/public-case-data-release-checklist.md)
