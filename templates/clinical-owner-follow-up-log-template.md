# Clinical Owner Follow-Up Log Template

Status: private worksheet template, not treatment advice
Privacy: completed copies may contain sensitive communication and must stay in
ignored private storage unless reduced to de-identified labels and
release-checked

## Follow-Up Metadata

| Field | Value |
| --- | --- |
| Case code |  |
| Owner route |  |
| Owner role |  |
| Outreach alias |  |
| Follow-up alias |  |
| Generalized timing |  |
| Current state before follow-up |  |

## Follow-Up Classification

Choose one next state:

- `follow_up_not_due`;
- `follow_up_ready`;
- `follow_up_sent`;
- `records_pending`;
- `owner_redirected`;
- `alternate_owner_needed`;
- `response_captured_private`;
- `route_closed_label_only`;
- `release_blocked`.

## Private Extraction

| Field | Value |
| --- | --- |
| Narrow follow-up question used |  |
| Missing-record category, if any |  |
| Next owner role, if redirected |  |
| Response-capture alias, if any |  |
| Patient-specific treatment instruction present, yes/no |  |
| Raw quote omitted from public repo, yes/no |  |

## Release Check

- Raw follow-up stays private.
- No clinician name, hospital name, phone number, screenshot, local path, exact
  date, accession number, or full lab value is included in public text.
- No patient-specific treatment instruction is included in public text.
- Public update is state-only or missing-record-category only.
- `scripts/check_public_repo.py` passes before commit.
