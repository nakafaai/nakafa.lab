# Case-001 Owner Outreach Packet

Date: 2026-05-04
Status: de-identified owner-outreach packet, not treatment advice
Privacy: no raw records, screenshots, identifiers, exact dates, clinician names,
hospital names, phone numbers, local paths, or patient-specific treatment
instructions

## Purpose

Use this after the specialist-owner routing guide. Do not send every row to
every clinician. Use only the row for the owner being contacted.

This packet answers the practical question: "What do we need this owner to
confirm?"

## Current Packet Label

`owner_outreach_packet_ready`

## Universal Cover Note

This is a de-identified research-support packet for a transfusion-dependent
thalassemia case. Nakafa Lab is not asking you to approve a treatment plan from
the repository. We are asking for the right qualified owner to confirm labels,
name missing records, or redirect the question.

Please answer only the domain you own.

## Owner Rows

| Owner | One-sentence ask | Private attachments or record requests | Output needed |
| --- | --- | --- | --- |
| Hematology or thalassemia clinic | Please confirm or correct the current diagnosis label, clinical-dependence category, and missing-record list. | Current clinician diagnosis note; HPLC/electrophoresis timing; transfusion pattern summary; chelator summary; any prior referral or screening notes. | confirmed category, corrected category, missing-record list, or redirect |
| Transfusion service or blood bank | Please identify what is needed to quantify transfusion burden and immune/blood-bank risk safely. | Transfusion dates; body weight; product type; transfused volume; unit hematocrit or red-cell fraction; pre/post hemoglobin; antibody screen; DAT/direct Coombs; matching policy; reaction history. | burden-ready, immune-packet-ready, partial, or records-requested label |
| Molecular genetics or genetic counseling | Please identify whether records are enough to confirm molecular subtype or what molecular records are missing. | `HBB`; `HBA1/HBA2`; HPFH; delta-beta-thalassemia; `HBG1/HBG2`; XmnI-HBG2; `BCL11A`; `HBS1L-MYB`; family testing context if available. | molecular-confirmed, molecular-partial, molecular-records-needed, or redirect |
| Iron, MRI, cardiology, endocrine, or organ-monitoring owner | Please identify whether the iron and organ-risk packet is complete enough for specialist interpretation. | Ferritin trend; LIC MRI; cardiac `T2*`; chelator monitoring; renal, liver, endocrine, cardiac, bone, hearing, eye, and infection monitoring as applicable. | iron-packet-ready, organ-packet-partial, monitoring-records-needed, or redirect |
| Transplant, gene-cell therapy, or trial team | Please state whether the packet is ready for formal specialist screening or what data blocks screening. | Hematology label, molecular context, transfusion burden, immune/blood-bank packet, iron and organ-risk packet, infection and access context as requested privately. | ready, partial, data-missing, medically unsuitable, access-blocked, or under review |

## Public-Safe Outcome States

Use only these labels in public:

- `outreach_not_sent`;
- `outreach_sent`;
- `records_requested`;
- `owner_redirected`;
- `owner_declined`;
- `owner_under_review`;
- `response_received_private`.

## Private Handling Rules

- Keep raw PDFs, images, screenshots, lab values, dates, names, hospital names,
  clinician messages, and contact details outside the public repository.
- Store private records only in ignored private storage.
- Public updates may only say which owner route changed state.
- Patient-specific treatment instructions remain private and clinician-owned.
- If an owner asks for records, return to the private source index and the
  record request matrix before changing public labels.
- If an owner replies, use the
  [Case-001 owner response capture](case-001-owner-response-capture.md) guide
  before writing any public update.

## Do Not Ask This Packet To Decide

- Whether transfusion frequency, volume, or target should change.
- Whether chelation, immune medicines, supplements, diet, or any other treatment
  should change.
- Whether transplant, gene therapy, CRISPR therapy, luspatercept, mitapivat,
  hydroxyurea, or any trial is suitable for case-001.
- Whether the repository has discovered a cure.

Those are specialist clinical questions. This packet only makes the question
small enough for the right owner to answer.

## Source-Backed Gates

- [Case-001 specialist owner routing](case-001-specialist-owner-routing.md)
- [Case-001 owner outreach packet gate](../findings/2026-05-04-case001-owner-outreach-packet-gate.md)
- [Case-001 owner response capture](case-001-owner-response-capture.md)
- [Case-001 owner response capture gate](../findings/2026-05-05-case001-owner-response-capture-gate.md)
- [Case-001 record request matrix](case-001-record-request-matrix.md)
- [Public case data release checklist](../../../templates/public-case-data-release-checklist.md)
