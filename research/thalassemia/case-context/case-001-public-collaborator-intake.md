# Case-001 Public Collaborator Intake

Date updated: 2026-07-04
Status: de-identified public-collaborator intake guide, not treatment advice
Privacy: no raw records, screenshots, identifiers, exact dates, clinician names,
hospital names, phone numbers, local paths, or patient-specific treatment
instructions

## Purpose

Use this when Nakafa Lab is shared publicly and people offer help. The goal is
to route each offer to a bounded task without exposing private case data or
creating public medical advice.

Use the public share kit and branch-routing gate before posting a public call:
[Case-001 public share kit](case-001-public-share-kit.md).

## Current Intake Label

`case001_public_outreach_branch_routing_ready_general_only`

## Public-Safe Intake States

- `public_call_ready`;
- `inquiry_received`;
- `role_unverified`;
- `qualified_role_claimed`;
- `scope_matched`;
- `scope_mismatch`;
- `private_intro_needed`;
- `do_not_share_private_records`;
- `declined_or_spam`;
- `blocked_medical_advice`.

## Public Call Shape

A safe public call should ask for help with roles, not treatment decisions:

- hematology or thalassemia label review;
- transfusion medicine or blood-bank record needs;
- molecular genetics record needs;
- iron, MRI, cardiology, endocrine, or organ-monitoring packet review;
- transplant, gene-cell therapy, or trial pathway explanation without
  eligibility screening;
- wet-lab assay feasibility review;
- data, software, reproducibility, and privacy tooling;
- funding, logistics, and access mapping;
- Islamic ethics and tafsir boundary review.

## Intake Workflow

1. Record the inquiry privately by alias.
2. Classify the role and whether the scope matches a current gate.
3. Ask for public sources, PMIDs, guideline URLs, or registry IDs when a reply
   mentions a pathway.
4. Do not request or accept raw private records in public channels.
5. Route qualified clinical roles to the owner outreach packet.
6. Route non-clinical roles to scoped repo tasks, assay review, privacy review,
   access mapping, or Islamic ethics review.
7. Block public medical advice and keep patient-specific treatment comments
   private.

## Do Not Ask The Public To Decide

- Diagnosis.
- Transfusion frequency, volume, or targets.
- Chelation, immune medicines, supplements, diet, or any other treatment.
- Transplant, gene therapy, CRISPR therapy, luspatercept, mitapivat,
  hydroxyurea, or trial suitability for case-001.

Those are qualified clinical-owner questions. Public collaboration can help
organize evidence, locate qualified reviewers, improve tooling, and map access
barriers.

## Source-Backed Gates

- [Case-001 public outreach branch routing gate](case-001-public-outreach-branch-routing-gate.md)
- [Case-001 public share kit](case-001-public-share-kit.md)
- [Case-001 public collaborator intake gate](../findings/2026-05-07-case001-public-collaborator-intake-gate.md)
- [Case-001 owner outreach packet](case-001-owner-outreach-packet.md)
- [Case-001 owner follow-up ladder](case-001-owner-follow-up-ladder.md)
- [Case-001 owner response capture](case-001-owner-response-capture.md)
- [Public case data release checklist](../../../templates/public-case-data-release-checklist.md)
