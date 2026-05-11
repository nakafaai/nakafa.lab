# Case-001 Registry Link Disambiguation

Date: 2026-05-10
Status: public-safe registry-link triage, not treatment advice
Privacy: no private records, screenshots, identifiers, exact dates, hospital
names, clinician names, doctor messages, or patient-specific treatment
instructions

## Purpose

Use this when someone sends a trial, center, registry, or advanced-therapy link.
The goal is to classify the link before it becomes a clinical-owner question.

Current label: `registry_link_disambiguation_ready`

## Triage Flow

1. Extract the public registry ID, usually an `NCT` ID.
2. Classify the record as direct TDT, query-adjacent NTDT, iron-axis,
   transplant, gene-cell therapy, follow-up, or unclear.
3. Record status, country, intervention, and primary endpoint as access context.
4. Route to the right owner only after classification.
5. Keep the state `not_case_eligibility` until a qualified owner reviews it.

## Safe Reply Text

If someone sends a link:

> Thank you. Please share the official registry ID or URL. We will classify it
> first as TDT, NTDT, iron-axis, transplant, gene-cell therapy, follow-up, or
> unclear. Registry presence is access context only, not case eligibility or
> treatment advice.

## Source-Backed Gates

- [Case-001 registry link disambiguation gate](../findings/2026-05-10-case001-registry-link-disambiguation-gate.md)
- [Case-001 mitapivat boundary and access inquiry](case-001-mitapivat-boundary-access-inquiry.md)
- [Case-001 public responder qualification](case-001-public-responder-qualification.md)
- [Registry link disambiguation template](../../../templates/registry-link-disambiguation-template.md)
