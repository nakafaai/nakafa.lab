# Clinical Owner Response Capture Template

Status: private worksheet template, not treatment advice
Privacy: completed copies may contain sensitive clinical communication and must
stay in ignored private storage unless reduced to de-identified labels and
release-checked

## Response Metadata

| Field | Value |
| --- | --- |
| Source alias |  |
| Case code |  |
| Owner route |  |
| Owner role |  |
| Response timing, generalized |  |
| Domain answered |  |

## Response Classification

Choose one answer type:

- `confirm`;
- `correct`;
- `request_records`;
- `redirect`;
- `under_review`;
- `decline`;
- `unclear`;
- `private_treatment_instruction`.

## Private Extraction

| Field | Value |
| --- | --- |
| Public-safe label confirmed or corrected |  |
| Missing-record category requested |  |
| Next owner role, if redirected |  |
| Follow-up question needed |  |
| Patient-specific treatment instruction present, yes/no |  |
| Raw quote omitted from public repo, yes/no |  |

## Public Output

Choose one public output label:

- `capture_pending`;
- `captured_label_only`;
- `records_requested`;
- `owner_redirected`;
- `owner_under_review`;
- `owner_declined`;
- `follow_up_needed`;
- `private_treatment_instruction_omitted`;
- `release_blocked`.

## Release Check

- Raw reply stays private.
- No clinician name, hospital name, phone number, screenshot, local path, exact
  date, accession number, or full lab value is included in public text.
- No patient-specific treatment instruction is included in public text.
- Public update is label-only or missing-record-category only.
- `scripts/check_public_repo.py` passes before commit.
