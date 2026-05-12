# Case-001 Mitapivat Jurisdiction Access Verification

Date: 2026-05-12
Status: public-safe access verification aid, not treatment advice
Privacy: no private records, screenshots, identifiers, exact dates, hospital
names, clinician names, doctor messages, or patient-specific treatment
instructions

## Purpose

Use this note after the mitapivat boundary inquiry. The goal is to verify
jurisdiction and access before anyone assumes that a foreign approval, registry
record, or trial country list creates a local pathway.

Current label: `mitapivat_jurisdiction_access_verification_ready`

## What To Ask

1. Is mitapivat registered, importable, reimbursed, or formulary-accessible in
   the relevant care jurisdiction?
2. If not registered locally, is there a legal named-patient,
   compassionate-use, special-access, or clinical-trial pathway that a
   clinician can verify?
3. Which safety and monitoring requirements would the local system require
   before this can be discussed?
4. Which owner can answer: hematologist, hospital pharmacy, regulatory affairs,
   insurer, trial site, or manufacturer medical information?

## Safe Summary For A Doctor Or Pharmacist

> Nakafa Lab found public evidence that mitapivat has adult thalassemia
> approval or registration in some jurisdictions, and separate trial records in
> other countries. We are not asking for treatment. We are asking whether there
> is any legally verifiable local access pathway, and what records or safety
> checks would be required before relevance could be reviewed.

## Safe States

- `foreign_adult_label_context`;
- `foreign_adult_registration_context`;
- `trial_country_context`;
- `local_registration_unverified`;
- `local_access_unverified`;
- `owner_review_needed`;
- `not_case_eligibility`;
- `not_relevant_now`;
- `release_blocked`.

## Source-Backed Gates

- [Case-001 mitapivat jurisdiction access verification gate](../findings/2026-05-12-case001-mitapivat-jurisdiction-access-verification-gate.md)
- [Case-001 mitapivat boundary and access inquiry](case-001-mitapivat-boundary-access-inquiry.md)
- [Mitapivat access inquiry template](../../../templates/mitapivat-access-inquiry-template.md)
