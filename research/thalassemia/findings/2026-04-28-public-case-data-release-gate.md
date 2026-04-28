# Public Case Data Release Gate

Date: 2026-04-28
Status: repository privacy gate
Evidence label: security and research-operations guardrail, not medical advice

## Bottom Line

Case records can help the thalassemia research loop only after they pass a
public-release gate. Raw medical PDFs, lab scans, photos, exact identifiers, and
local file paths must stay outside this public repository.

The public repo may hold de-identified summaries, record checklists, lab values,
research labels, and clinician questions when they are necessary for source-
backed reasoning and when they do not identify the person.

## Release Classes

| Class | Public repo decision | Meaning |
| --- | --- | --- |
| `private_raw_record` | Block | Raw PDF, image, scan, clinical form, medical-record export, or source file path. |
| `public_blocked_identifier` | Block | Name, exact address, hospital ID, accession number, phone, email, exact birth date, face photo, signature, stamp, barcode, or QR code. |
| `public_blocked_treatment_claim` | Block | Patient-specific dosing, transfusion, chelation, immune-medicine, supplement, or therapy action without clinician review. |
| `deidentified_extract_candidate` | Manual review | Extracted facts with identifiers removed, still needing a privacy and clinical-claim check. |
| `source_link_only` | Allow with caution | Public URL, DOI, PMID, registry ID, or official guideline link without copied raw private material. |
| `public_summary_ready` | Allow | De-identified summary or checklist that keeps uncertainty labels and clinician-review boundaries. |

## Required Checks Before Public Commit

1. Keep raw clinical files outside Git.
2. Remove direct identifiers and local source paths.
3. Replace exact dates tied to a person with broad timing unless the exact date
   is clinically necessary and explicitly reviewed.
4. Keep clinician-facing text as questions and record requests, not treatment
   instructions.
5. Store source-backed literature and registry evidence under `data/`, but do
   not copy private records into `data/`.
6. Run `scripts/check_public_repo.py` before committing case-context or public
   data changes.

## Tooling Change

The public-repo checker now blocks:

- candidate raw media under `research/thalassemia/case-context/`;
- candidate raw media under clinical case-data folders in `data/`;
- local absolute user, downloads, and temporary file references inside candidate
  files;
- existing blocked caches, local environments, secrets, credentials, and common
  secret patterns.

The checker also has case-context-specific content rules for direct
identifier-shaped label-value fields, including patient-name, email, phone,
fax, medical-record, hospital, accession, national, insurance, record-number,
and exact birth-date patterns.

This is not a complete legal de-identification engine. It is a repo guardrail
that catches the most likely public-repo mistakes before they are pushed.

## Case-001 Application

The existing case-001 medical extraction remains public because it excludes raw
files and direct identifiers, uses broad timing, separates extracted facts from
interpretation, and blocks treatment advice.

Future case-001 updates should use the release checklist before entering:

- new transfusion logs;
- blood-bank records;
- ferritin, LIC, cardiac `T2*`, chelation, and organ-risk records;
- genetic reports;
- clinician letters or referral decisions.

## Islamic Research Boundary

Quran 16:43 supports asking qualified experts when knowledge is missing. Quran
55:7-9 supports careful measure and avoiding distorted claims. In this gate,
those anchors support disciplined privacy review and clinician review. They do
not prove any biomedical treatment.

## Sources

- [Public case data release checklist](../../../templates/public-case-data-release-checklist.md)
- [Private-to-public case extraction template](../../../templates/private-to-public-case-extraction-template.md)
- [Private-to-public case extraction gate](2026-04-28-private-to-public-case-extraction-gate.md)
- [Public case data release notebook](../notebooks/2026-04-28-public-case-data-release-gate.ipynb)
- [Public repo checker](../../../scripts/check_public_repo.py)
- [Case-001 medical record extraction](../case-context/case-001-medical-record-extraction-2026-04-28.md)
- [Case-001 minimum hematologist packet](../case-context/case-001-minimum-hematologist-packet.md)
- [HHS de-identification guidance](https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
