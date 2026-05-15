# Case-001 Mitapivat Response Capture

Date: 2026-05-15
Status: public-safe response-capture aid, not treatment advice
Privacy: no private records, screenshots, identifiers, exact dates, hospital
names, clinician names, doctor messages, owner messages, or patient-specific
treatment instructions

## Purpose

Use this note after a first-contact owner replies. The goal is to capture only
public-safe labels and keep raw replies in private workspace material.

Current label: `mitapivat_response_capture_ready`

## Required Fields

Every captured response needs:

- response label;
- owner category;
- public source or registry ID, if any;
- private-workspace action;
- public-repo action;
- next state.

## Safe Summary For Repo Updates

> An owner response was received and reduced to a public-safe label. Raw reply
> text, private contacts, identifiers, and patient-specific content remain
> outside the public repo. The next state is [insert public-safe label].

## Safe Response Labels

- `no_response_yet`;
- `wrong_owner_redirect`;
- `public_source_confirmed`;
- `missing_records_named`;
- `clinician_mediated_documents_requested`;
- `raw_records_requested_public_channel`;
- `local_access_pathway_named`;
- `not_relevant_or_not_available_now`;
- `trial_contact_process_confirmed`;
- `safety_or_adverse_event_route_named`;
- `patient_specific_treatment_advice_received`.

## Source-Backed Gates

- [Case-001 mitapivat response-capture gate](../findings/2026-05-15-case001-mitapivat-response-capture-gate.md)
- [Case-001 mitapivat first-contact packet](case-001-mitapivat-first-contact-packet.md)
- [Mitapivat response-capture template](../../../templates/mitapivat-response-capture-template.md)
