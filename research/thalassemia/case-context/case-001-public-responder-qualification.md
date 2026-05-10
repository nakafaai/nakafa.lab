# Case-001 Public Responder Qualification

Date: 2026-05-09
Status: public-safe reply triage, not treatment advice
Privacy: no raw records, screenshots, identifiers, exact dates, hospital names,
clinician names, doctor messages, local paths, or patient-specific treatment
instructions

## Purpose

Use this after someone replies to a public Nakafa Lab post. The goal is to turn
interest into a role, scope, source, and next gate before private follow-up.

Current label: `public_responder_qualification_ready`

## Triage Flow

1. Record only a public alias and channel.
2. Classify the claimed role.
3. Ask for the bounded domain they can review.
4. Ask for a source, credential cue, registry ID, assay description, or scoped
   repo task depending on role.
5. Route to `private_intro_ready`, `repo_task_ready`, `release_blocked`,
   `blocked_raw_record_request`, or `blocked_treatment_advice`.

## Safe First Replies

| Incoming claim | Safe response |
| --- | --- |
| "I am a clinician" | "Which domain can you review: diagnosis/genetics, transfusion, blood bank, iron/organ monitoring, or advanced-therapy screening pathway?" |
| "I know a trial or center" | "Please share the public registry ID, center, country, and what screening pathway you can explain." |
| "I can run assays" | "Please share the assay type, readouts, sample requirement, biosafety boundary, and quote constraints." |
| "I can help with data/software/privacy/access" | "Please pick one scoped task that does not require private records." |
| "Send me the records" | "We cannot share raw records in public. This is blocked until privacy review." |
| Treatment advice | "We cannot use public treatment advice. Qualified clinical review must happen privately." |

## Source-Backed Gates

- [Case-001 public responder qualification gate](../findings/2026-05-09-case001-public-responder-qualification-gate.md)
- [Case-001 registry link disambiguation](case-001-registry-link-disambiguation.md)
- [Case-001 public share kit](case-001-public-share-kit.md)
- [Public responder qualification template](../../../templates/public-responder-qualification-template.md)
