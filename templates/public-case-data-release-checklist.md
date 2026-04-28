# Public Case Data Release Checklist

Use this checklist before committing any case-context update, extracted medical
record fact, doctor packet, or case-linked data artifact to the public repo.

## 1. Source Type

- [ ] The source is a de-identified extraction, summary, table, or checklist.
- [ ] No raw PDF, scan, photo, export, or clinical form is being committed.
- [ ] No local file path is being committed.
- [ ] A private working copy, if needed, stays under `private/` and is not
  tracked.
- [ ] The extraction follows the
  [private-to-public case extraction template](private-to-public-case-extraction-template.md)
  when a private record is the source.
- [ ] Public literature, registry, guideline, or database sources are cited by
  URL, DOI, PMID, registry ID, or local source snapshot.

## 2. Identifier Removal

- [ ] No patient name.
- [ ] No exact address or location smaller than needed for research routing.
- [ ] No hospital ID, accession number, national ID, insurance ID, or record
  number.
- [ ] No phone number, email, messaging handle, or contact detail.
- [ ] No exact birth date.
- [ ] No face photo, signature, stamp, QR code, barcode, or report image.
- [ ] No family, employer, school, clinic, doctor, or event detail that makes
  the person reasonably identifiable in context.

## 3. Date And Context Handling

- [ ] Person-linked dates are generalized to broad timing unless exact timing is
  essential and has been reviewed.
- [ ] Rare combinations of facts are reduced or generalized when they could
  identify the person.
- [ ] The record explains what was extracted, what was omitted, and why.
- [ ] The public text contains only the minimum fact needed for research routing
  or clinician questions.

## 4. Clinical Claim Boundary

- [ ] The public text does not diagnose the person.
- [ ] The public text does not recommend dosing, transfusion changes, chelation
  changes, immune-medicine changes, supplements, diet, or therapy changes.
- [ ] Candidate relevance is blocked until clinician review closes the relevant
  case gates.
- [ ] Doctor-facing text is written as questions, record requests, and evidence
  boundaries.

## 5. Decision

Choose one release class:

- [ ] `private_raw_record`
- [ ] `public_blocked_identifier`
- [ ] `public_blocked_treatment_claim`
- [ ] `deidentified_extract_candidate`
- [ ] `source_link_only`
- [ ] `public_summary_ready`

Reviewer:

Date:

Notes:
