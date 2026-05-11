# Case-001 Mitapivat Boundary And Access Inquiry

Date: 2026-05-11
Status: public-safe clinician inquiry aid, not treatment advice
Privacy: no private records, screenshots, identifiers, exact dates, hospital
names, clinician names, doctor messages, or patient-specific treatment
instructions

## Purpose

Use this note when asking a hematologist or qualified trial/contact owner about
mitapivat. The goal is to keep adult label evidence, adult TDT trial evidence,
pediatric TDT registry context, and pediatric NTDT registry context separate.

Current label: `mitapivat_boundary_access_inquiry_ready`

## What To Ask

1. Which context should be reviewed for this case, if any:
   `approved_adult_label_context`, `adult_tdt_trial_context`,
   `pediatric_tdt_trial_context`, `pediatric_ntdt_trial_context`, or
   `not_relevant_now`?
2. What minimum records are required before discussing relevance: diagnosis,
   genotype, age and weight band, transfusion burden, hemoglobin trend, iron
   and organ status, liver tests, medication list, and local access constraints?
3. Does the FDA label's liver-risk, REMS, and interaction language create a
   specialist-review blocker?
4. Is there any local availability, referral pathway, or trial-site contact to
   verify, or should this remain access-mapping context only?

## Safe Summary For A Doctor

> Nakafa Lab found that mitapivat now has adult FDA label context for
> alpha- or beta-thalassemia anemia, and separate registry contexts for adult
> TDT, pediatric TDT, and pediatric NTDT studies. We are not asking whether to
> start treatment. We are asking which context, if any, is worth reviewing and
> what records are required before relevance can be assessed.

## Safe States

- `approved_adult_label_context`;
- `adult_tdt_trial_context`;
- `pediatric_tdt_trial_context`;
- `pediatric_ntdt_trial_context`;
- `access_mapping_only`;
- `owner_review_needed`;
- `not_case_eligibility`;
- `not_relevant_now`;
- `release_blocked`.

## Source-Backed Gates

- [Case-001 mitapivat boundary and access inquiry gate](../findings/2026-05-11-case001-mitapivat-boundary-access-inquiry-gate.md)
- [Case-001 registry link disambiguation](case-001-registry-link-disambiguation.md)
- [Mitapivat access inquiry template](../../../templates/mitapivat-access-inquiry-template.md)
