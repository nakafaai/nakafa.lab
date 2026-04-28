# Private Case Intake Index Template

Status: private workspace template, not a medical record and not medical advice

Use this template only under an ignored `private/` path when family-supplied
records need to be indexed before de-identified extraction. Do not commit a
completed copy.

## Workspace Boundary

| Field | Value |
| --- | --- |
| Case code | `case-001` or another non-identifying case code |
| Storage path | `private/<case-code>/` |
| Source owner | family / clinician / public source |
| Intake date | broad date only |
| Reviewer | role only |
| Public-release status | `private_intake_not_started` / `private_intake_indexed` / `deidentified_timeline_candidate` / `public_summary_candidate` / `public_summary_ready` |

## Source Index

Use source aliases, not local file paths.

| Source alias | Source class | Broad date | Record type | Key fields present | Missing fields | Next action |
| --- | --- | --- | --- | --- | --- | --- |
| private source 1 | private raw record | broad timing | example | example | example | extract or omit |

Allowed source classes:

- `private_raw_record`
- `clinician_summary`
- `family_reported`
- `public_source`
- `unknown_source`

## Extraction Targets

Mark only the domains needed for clinician questions or research routing.

- [ ] Diagnosis, subtype, HPLC, electrophoresis, or genetic testing.
- [ ] Transfusion dates, volume, body weight, product type, pre/post Hb, and
      reaction history.
- [ ] Blood-bank, antibody screen, named antibodies, DAT/direct Coombs, and
      matching policy.
- [ ] Ferritin trend, LIC, cardiac `T2*`, chelator identity, toxicity
      monitoring, and organ-risk records.
- [ ] Autoimmune, spleen, infection, vaccination, fertility, or access context.
- [ ] Prior HSCT, gene-cell therapy, disease-modifying drug, or trial review.

## Identifier And Context Blocks

Do not move these into public files:

- names, initials, direct contact details, local file paths, addresses, record
  numbers, national IDs, insurance IDs, exact birth dates, and exact
  person-linked dates;
- hospital names, doctor names, signatures, stamps, barcodes, QR codes, report
  images, faces, or rare family/event context;
- raw instructions that could be mistaken for diagnosis, dosing, transfusion,
  chelation, immune medicine, supplement, diet, or therapy advice.

## Public Extraction Queue

| Candidate fact | Public-safe form | Evidence label | Target public file | Release blocker |
| --- | --- | --- | --- | --- |
| example | broad, non-identifying value | extracted fact | review required | privacy review |

## Checker Steps Before Public Commit

Run these after writing any public candidate:

```bash
uv run python scripts/summarize_case_timeline.py <deidentified-timeline.csv>
uv run python scripts/check_public_repo.py
uv run python scripts/check_repo_language.py
```

The default timeline summary suppresses exact date windows and rejects
day-level dates unless `--private-input` is used. If a private reviewer needs
exact dates, use `--private-input --include-dates` only for ignored private
outputs. Keep raw records and completed private indexes under `private/`.
