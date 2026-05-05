# Case-001 Owner Response Capture Gate

Date checked: 2026-05-05
Evidence label: operational response-capture gate, not medical advice

## Direct Answer

After owner-specific outreach, the next blocker is owner-response capture.

Case-001 should use this public-safe operational label:

`owner_response_capture_gate_ready`

The goal is to turn an owner reply into a structured private row and a
public-safe label. A clinician reply is not a general approval of Nakafa Lab
research, and it must not be copied into the public repository as raw text.

## Capture Rule

For each owner response, capture only the minimum private fields needed to
preserve traceability:

- source alias, not raw screenshot or message text;
- owner route and owner role, not clinician name;
- generalized response timing, not exact public date;
- domain answered;
- answer type: confirm, correct, request records, redirect, under review,
  decline, unclear, or private treatment instruction;
- missing-record category if records are requested;
- next owner if redirected;
- public-safe output label;
- release decision.

## Public-Safe Output Labels

Use only these labels in public artifacts:

- `capture_pending`;
- `captured_label_only`;
- `records_requested`;
- `owner_redirected`;
- `owner_under_review`;
- `owner_declined`;
- `follow_up_needed`;
- `private_treatment_instruction_omitted`;
- `release_blocked`.

## Response-To-Label Map

| Private response type | Public-safe output | Next action |
| --- | --- | --- |
| Confirms a public-safe label | `captured_label_only` | Update only the de-identified label after release check. |
| Corrects a public-safe label | `captured_label_only` | Record corrected wording without raw quote or identifiers. |
| Requests records | `records_requested` | Return to the private source index and record request matrix. |
| Redirects to another owner | `owner_redirected` | Use specialist-owner routing before interpretation. |
| Says the domain is under review | `owner_under_review` | Wait for private owner response or formal record. |
| Declines or cannot review | `owner_declined` | Find a new owner or mark route unresolved. |
| Gives patient-specific treatment instructions | `private_treatment_instruction_omitted` | Keep instructions private and clinician-owned. |
| Is unclear | `follow_up_needed` | Ask a narrow clarification question privately. |

## Why This Matters

TIF 2025 separates TDT care into transfusion, blood-bank safety, iron overload,
monitoring, multidisciplinary care, HCT, and gene manipulation domains.
GeneReviews separates phenotype-level labels from molecular confirmation and
genetic counseling. Current active registry examples, including CTX001/exa-cel
follow-up studies, reinforce that advanced therapy remains a formal specialist
screening domain.

Therefore, one owner reply can close one narrow domain while leaving other
domains blocked. The response-capture gate prevents the repo from turning a
private clinical message into a public treatment claim.

## Stop Conditions

This gate is complete for one response when:

1. the raw response stays private;
2. the private capture row has source alias, owner route, answer type, and next
   action;
3. any public update is reduced to one allowed label;
4. patient-specific treatment instructions are omitted from public artifacts;
5. the public case-data release checklist passes before commit.

## Biomedical Boundary

This gate does not diagnose, dose, change transfusion, change chelation, change
immune medicine, recommend supplements, choose a referral, or decide trial
eligibility. It only defines how to capture owner responses safely.

## Islamic Motivation Boundary

Quran 16:43 is used as an expert-consultation anchor. Quran 55:7-9 is used as a
measurement and anti-exaggeration anchor. These are method boundaries, not
biomedical evidence.

## Sources

- [Case-001 owner outreach packet](../case-context/case-001-owner-outreach-packet.md)
- [Case-001 doctor response triage](../case-context/case-001-doctor-response-triage.md)
- [Case-001 specialist owner routing](../case-context/case-001-specialist-owner-routing.md)
- [Case-001 record request matrix](../case-context/case-001-record-request-matrix.md)
- [Public case data release checklist](../../../templates/public-case-data-release-checklist.md)
- [Private case intake threat model](../../../docs/private-case-intake-threat-model.md)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 monitoring recommendations](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
- [TIF 2025 HCT chapter](https://www.ncbi.nlm.nih.gov/books/NBK614242/)
- [TIF 2025 gene manipulation chapter](https://www.ncbi.nlm.nih.gov/books/NBK614241/)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [ClinicalTrials.gov NCT05477563 CTX001 TDT registry record](https://clinicaltrials.gov/study/NCT05477563)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
