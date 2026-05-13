# Case-001 Mitapivat Owner Routing

Date: 2026-05-13
Status: public-safe owner-routing aid, not treatment advice
Privacy: no private records, screenshots, identifiers, exact dates, hospital
names, clinician names, doctor messages, or patient-specific treatment
instructions

## Purpose

Use this note before sending any mitapivat-related outreach. The goal is to
route each question to the first owner who can answer it without mixing
clinical, pharmacy, regulatory, manufacturer, trial, and financial questions.

Current label: `mitapivat_owner_routing_ready`

## Routing Rules

- Clinical relevance starts with the treating hematologist.
- Dispensing, formulary, certification, and import operations start with
  hospital or specialty pharmacy.
- Registration, named-patient, compassionate-use, and special-access questions
  start with a regulator or regulatory-affairs contact.
- Product medical information, regional routing, adverse-event reporting, and
  medical-science-liaison questions start with manufacturer medical
  information.
- Study opening, screening, and contact-process questions start with the
  official trial site or registry contact.
- Coverage and financial support questions start with payer or financial-access
  owners.

## Safe Summary For Outreach

> Nakafa Lab is separating clinical relevance, local access, pharmacy handling,
> regulatory status, trial status, and financial access into different owner
> questions. We are not asking for treatment advice in this message. We are
> asking who owns this specific question and what public-safe source or record
> is needed before the next step.

## Safe States

- `clinical_owner_review_needed`;
- `pharmacy_owner_review_needed`;
- `regulatory_owner_review_needed`;
- `manufacturer_medinfo_review_needed`;
- `trial_owner_review_needed`;
- `financial_owner_review_needed`;
- `not_case_eligibility`;
- `release_blocked`.

## Source-Backed Gates

- [Case-001 mitapivat owner routing gate](../findings/2026-05-13-case001-mitapivat-owner-routing-gate.md)
- [Case-001 mitapivat jurisdiction access verification](case-001-mitapivat-jurisdiction-access-verification.md)
- [Mitapivat owner routing template](../../../templates/mitapivat-owner-routing-template.md)
