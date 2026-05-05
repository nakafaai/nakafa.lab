# Case-001 Owner Response Capture

Date: 2026-05-05
Status: de-identified owner-response capture guide, not treatment advice
Privacy: no raw replies, screenshots, identifiers, exact dates, clinician names,
hospital names, phone numbers, local paths, or patient-specific treatment
instructions

## Purpose

Use this after an owner replies to the owner outreach packet. The goal is to
record what changed without copying private clinical communication into the
public repository.

This guide answers the practical question: "How do we record the reply safely?"

## Current Capture Label

`owner_response_capture_gate_ready`

## Private Capture Fields

Completed capture rows belong in ignored private storage unless they are reduced
to de-identified labels and pass the public release checklist.

| Field | Public-safe rule |
| --- | --- |
| Source alias | Use an alias such as `owner-response-001`; do not publish raw message IDs or screenshots. |
| Owner route | Use role labels such as hematology, blood bank, genetics, iron/organ monitoring, or trial team. |
| Response timing | Generalize before public release. |
| Domain answered | Use the existing domain names from the record request matrix. |
| Answer type | Use confirm, correct, request records, redirect, under review, decline, unclear, or private treatment instruction. |
| Missing records | Name the record category only. |
| Next owner | Use owner role only, not a person or facility name. |
| Treatment instruction present | Record privately as yes/no; never publish the instruction. |
| Public output label | Use one allowed label from this guide. |
| Release decision | Use release blocked, private only, or label-only public update. |

## Allowed Public Output Labels

- `capture_pending`;
- `captured_label_only`;
- `records_requested`;
- `owner_redirected`;
- `owner_under_review`;
- `owner_declined`;
- `follow_up_needed`;
- `private_treatment_instruction_omitted`;
- `release_blocked`.

## Capture Workflow

1. Save or index the raw reply only in ignored private storage.
2. Create one private capture row using the response-capture template.
3. Convert the reply into one answer type.
4. If records are requested, update the private source index and record request
   matrix.
5. If another owner is named, return to specialist-owner routing.
6. If treatment instructions appear, keep them private and clinician-owned.
7. Commit only de-identified labels after public release checks pass.

## Do Not Ask This Guide To Decide

- Whether a diagnosis is correct.
- Whether transfusion frequency, volume, or target should change.
- Whether chelation, immune medicines, supplements, diet, or any other treatment
  should change.
- Whether transplant, gene therapy, CRISPR therapy, luspatercept, mitapivat,
  hydroxyurea, or any trial is suitable for case-001.

Those are qualified clinical-owner questions. This guide only protects response
capture and public release.

## Source-Backed Gates

- [Case-001 owner outreach packet](case-001-owner-outreach-packet.md)
- [Case-001 owner response capture gate](../findings/2026-05-05-case001-owner-response-capture-gate.md)
- [Case-001 doctor response triage](case-001-doctor-response-triage.md)
- [Case-001 specialist owner routing](case-001-specialist-owner-routing.md)
- [Public case data release checklist](../../../templates/public-case-data-release-checklist.md)
