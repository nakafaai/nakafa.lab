# Private-To-Public Case Extraction Template

Status: extraction worksheet, not a medical record and not medical advice

Use this template when a private family-supplied record contains a fact that may
need to enter the public repo as de-identified research context.

Do not complete this file with raw identifiers and commit it. Keep any working
copy with private source details under `private/`.

## Source Boundary

| Field | Value |
| --- | --- |
| Source class | `private_raw_record` / `clinician_summary` / `family_reported` / `public_source` |
| Source storage | local private workspace only |
| Public release class | `private_raw_record` / `public_blocked_identifier` / `public_blocked_treatment_claim` / `deidentified_extract_candidate` / `source_link_only` / `public_summary_ready` |
| Extraction date | broad date only |
| Reviewer | role only, no personal contact detail |

## Identifier Check

- [ ] No name.
- [ ] No address or location smaller than needed for research routing.
- [ ] No hospital, accession, national, insurance, or record identifier.
- [ ] No phone, email, messaging handle, barcode, QR code, signature, stamp, or
  face image.
- [ ] No exact birth date or exact person-linked sample date unless explicitly
  reviewed and required.
- [ ] No facility, school, employer, family, or event detail that could
  re-identify the person in context.

## Extracted Fact Candidate

| Public field | De-identified value | Evidence label | Why it matters | Release decision |
| --- | --- | --- | --- | --- |
| example field | broad, non-identifying value | extracted fact | case routing only | review required |

## Omitted Material

List what was intentionally omitted and why:

- direct identifiers;
- raw record layout, images, signatures, stamps, barcodes, and local paths;
- free-text narrative that is not needed for the public research question;
- patient-specific treatment instructions.

## Clinical Claim Boundary

The public output must be framed as one of:

- extracted historical context;
- missing-record label;
- clinician question;
- research routing label;
- source-backed hypothesis boundary.

It must not diagnose, dose, change transfusion, change chelation, change immune
medicine, recommend supplements, or decide therapy eligibility.

## Final Public Text

Write only the public-ready summary here after the checks above pass.
