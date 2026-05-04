# Case-001 Owner Outreach Packet Gate

Date checked: 2026-05-04
Evidence label: operational outreach gate, not medical advice

## Direct Answer

After the specialist-owner routing gate, the next blocker is not another broad
paper. The next blocker is one owner-specific outreach packet per clinical
domain.

Case-001 should use this public-safe operational label:

`owner_outreach_packet_ready`

The goal is to ask each owner a narrow question that they can answer, redirect,
or convert into a missing-record request. Do not send the full research paper as
the first-contact artifact.

## Owner-Specific Ask Map

| Owner route | Ask | Attach or request privately | Output needed |
| --- | --- | --- | --- |
| Hematology or thalassemia clinic | Please confirm or correct the diagnosis label, clinical dependence category, and which records are still needed. | De-identified cover note plus private diagnosis, transfusion, iron, and medication summaries as approved by family. | confirmed category, corrected category, or missing-record list |
| Transfusion service or blood bank | Please identify which transfusion and blood-bank records are needed to quantify burden and immune risk safely. | Transfusion log, product type, volume, pre/post hemoglobin, antibody screen, DAT/direct Coombs, matching policy, reaction history. | burden-ready, immune-packet-ready, or records-requested label |
| Molecular genetics or genetic counseling | Please identify whether existing records are enough to confirm molecular subtype or whether additional testing records are needed. | HPLC/electrophoresis timing, `HBB`, `HBA1/HBA2`, HPFH, delta-beta-thalassemia, `HBG1/HBG2`, XmnI-HBG2, `BCL11A`, or `HBS1L-MYB` context if available. | molecular-confirmed, molecular-partial, or molecular-records-needed label |
| Iron, MRI, cardiology, endocrine, or organ-monitoring owner | Please identify whether the iron and organ-risk packet is complete enough for specialist interpretation. | Ferritin trend, LIC MRI, cardiac `T2*`, chelator monitoring, renal, liver, endocrine, cardiac, bone, hearing, eye, and infection monitoring as applicable. | iron-packet-ready, organ-packet-partial, or monitoring-records-needed label |
| Transplant, gene-cell therapy, or trial team | Please state whether the packet is ready for formal specialist screening or what data blocks screening. | Only after hematology, transfusion, molecular, immune, iron, and organ domains are packeted enough for review. | ready, partial, data-missing, medically unsuitable, access-blocked, or under review |

## Public-Safe Outcome States

Use only these labels in public artifacts:

- `outreach_not_sent`;
- `outreach_sent`;
- `records_requested`;
- `owner_redirected`;
- `owner_declined`;
- `owner_under_review`;
- `response_received_private`.

Do not publish raw messages, names, hospital names, phone numbers, exact dates,
screenshots, PDFs, local paths, accession numbers, or patient-specific treatment
instructions.

## Why This Matters

TIF 2025 separates routine TDT work into practical domains: transfusion
planning and safety, iron and organ monitoring, multidisciplinary care, HCT, and
gene manipulation. GeneReviews separates phenotype-level thalassemia labels from
molecular confirmation and family-risk genetics. A broad paper can be useful as
background, but it is not the right first object for a busy clinician who asks,
"What do you want me to confirm?"

The practical answer should be one owner-specific row, not the whole research
map.

## Stop Conditions

This gate is complete when each active owner route has one public-safe state and
one private next action:

- send the focused packet;
- request a missing record;
- follow an owner redirect;
- wait for a private response;
- close the route as not applicable after qualified review.

## Biomedical Boundary

This gate does not diagnose, dose, change transfusion, change chelation, change
immune medicine, recommend supplements, choose a referral, or decide trial
eligibility. It only converts the current research map into narrower questions
for qualified owners.

## Islamic Motivation Boundary

Quran 16:43 is used as an expert-consultation anchor. Quran 55:7-9 is used as a
measurement and anti-exaggeration anchor. These are method boundaries, not
biomedical evidence.

## Sources

- [Case-001 specialist owner routing](../case-context/case-001-specialist-owner-routing.md)
- [Case-001 specialist owner routing gate](2026-05-03-case001-specialist-owner-routing-gate.md)
- [Case-001 record request matrix](../case-context/case-001-record-request-matrix.md)
- [Public case data release checklist](../../../templates/public-case-data-release-checklist.md)
- [Private case intake threat model](../../../docs/private-case-intake-threat-model.md)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 monitoring recommendations](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
- [TIF 2025 multidisciplinary care chapter](https://www.ncbi.nlm.nih.gov/books/NBK614243/)
- [TIF 2025 HCT chapter](https://www.ncbi.nlm.nih.gov/books/NBK614242/)
- [TIF 2025 gene manipulation chapter](https://www.ncbi.nlm.nih.gov/books/NBK614241/)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
