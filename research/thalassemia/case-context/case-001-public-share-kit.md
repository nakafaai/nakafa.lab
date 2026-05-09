# Case-001 Public Share Kit

Date: 2026-05-08
Status: public-safe collaboration text, not treatment advice
Privacy: no raw records, screenshots, identifiers, exact dates, hospital names,
clinician names, doctor messages, local paths, or patient-specific treatment
instructions

## Purpose

Use this when sharing Nakafa Lab publicly. The goal is to ask for specific help
without asking the public to make medical decisions.

Current label: `public_share_kit_ready`

## Short Public Post Draft

Nakafa Lab is organizing source-backed thalassemia research. We have not found a
cure, and we are not asking the public for treatment advice.

We need qualified help in bounded roles: thalassemia clinicians, transfusion
medicine, molecular genetics, iron/organ monitoring, advanced-therapy access,
wet-lab assay feasibility, privacy-safe software, access mapping, and Islamic
ethics review.

Please do not send raw patient records in public replies. If you can help, reply
with your role and the specific domain you can review.

## Longer Public Post Draft

Nakafa Lab is an open, source-backed research effort focused on thalassemia. The
current blocker is coordination: a transfusion-dependent thalassemia case cannot
be reviewed as one broad question.

We need role-bounded help across diagnosis/genetics, transfusion burden, immune
and blood-bank records, iron and organ monitoring, advanced-therapy screening
pathways, assay feasibility, privacy-safe tooling, access mapping, and Islamic
ethics boundaries.

This is not public treatment advice, and we have not found a cure. Please do not
post raw records, screenshots, doctor messages, names, hospitals, exact dates, or
private contact details. If you can help, reply with your role and narrow review
domain.

## Do Not Share

- Raw records, screenshots, doctor messages, or medical files.
- Names, exact dates, hospitals, clinicians, phone numbers, local paths,
  accession numbers, or private timeline details.
- Full case-specific lab values unless a release checklist approves them.
- Public treatment recommendations or cure claims.

## Inbound Routing

| Public reply type | Safe next step |
| --- | --- |
| Clinical, genetics, transfusion, iron, or organ role | Route to public collaborator intake and private introduction only if the task is bounded. |
| Advanced-therapy or trial-access role | Ask for screening-pathway explanation, not eligibility. |
| Wet-lab partner | Route to assay feasibility and quote requirements. |
| Software, data, privacy, funding, access, or Islamic ethics role | Route to a scoped task that does not need private records. |
| Treatment advice in public | Mark `blocked_treatment_advice` and do not copy into public repo. |
| Request for raw records in public | Mark `blocked_raw_record_request` and move to privacy review. |

## Source-Backed Gates

- [Case-001 public responder qualification](case-001-public-responder-qualification.md)
- [Case-001 public share kit gate](../findings/2026-05-08-case001-public-share-kit-gate.md)
- [Case-001 public collaborator intake](case-001-public-collaborator-intake.md)
- [Case-001 owner outreach packet](case-001-owner-outreach-packet.md)
- [Public collaboration call template](../../../templates/public-collaboration-call-template.md)
- [Public case data release checklist](../../../templates/public-case-data-release-checklist.md)
