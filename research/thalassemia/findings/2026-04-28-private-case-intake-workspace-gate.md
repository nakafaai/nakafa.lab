# Finding: Private Case Intake Workspace Gate

Date checked: 2026-04-28
Evidence label: privacy, clinical-record operations, and research-routing
guardrail; not medical advice

## Working Conclusion

The next case-001 blocker is not a new candidate. It is a private, ignored
workspace that can turn family-supplied PDFs and logs into de-identified
record indexes, timelines, and clinician questions without exposing raw medical
records in the public repository.

Use this path:

`raw_local_record -> private_intake_index -> deidentified_timeline_candidate -> privacy_scan -> public_summary_candidate`

The repo may track templates, checkers, and de-identified summaries. It must
not track raw PDFs, scans, local paths, identifiers, or patient-specific
treatment decisions.

## Why This Gate Comes Before More Candidate Claims

TIF 2025 TDT guidance makes transfusion practice, iron overload, and morbidity
monitoring record-heavy. Case-001 still needs diagnosis/genotype, transfusion
volume, pre/post hemoglobin, antibody/DAT, ferritin trend, LIC, cardiac `T2*`,
chelation identity, toxicity monitoring, organ, spleen, infection, and access
records before specialist screening can be interpreted.

HHS de-identification guidance is not used here as a legal-compliance claim.
It is used as a conservative public-repo benchmark: direct identifiers,
person-linked dates, local context, and identifiers in unstructured text can
still identify a person and need explicit removal or blocking.

## Private Workspace Rule

Use ignored paths only:

- `private/case-001/source-index.md`
- `private/case-001/timeline.csv`
- `private/case-001/transfusion-log.csv`
- `private/case-001/extraction-worksheets/`

Tracked files may reference only public-safe labels such as `private source 1`
or `historical screening record`. They must not include local file paths,
doctor names, hospital names, report layouts, signatures, stamps, barcodes,
or exact person-linked dates.

## Implementation Update

The case timeline summarizer now scans each de-identified row with the public
case-context privacy scanner before producing a summary. It fails on obvious
identifier patterns such as local user paths, emails, phone/fax labels, record
number labels, exact birth-date labels, and patient-name labels.

This does not make the scanner a full de-identification expert. It makes the
default workflow harder to misuse and keeps the public case notes aligned with
the existing release checklist.

## Decision Labels

| Label | Meaning |
| --- | --- |
| `private_intake_not_started` | Raw records exist or may exist, but there is no private index. |
| `private_intake_indexed` | Private source index exists under `private/`, but no de-identified timeline is ready. |
| `deidentified_timeline_candidate` | A timeline exists but still needs checker and human review. |
| `public_summary_candidate` | A minimum public summary is ready for release checklist review. |
| `public_summary_ready` | The summary passed privacy, source, and clinical-claim checks. |

Current case-001 label: `private_intake_index_needed`.

## Islamic Motivation Boundary

Quran 55:7-9 supports measurement discipline and avoiding distortion in
claims. Quran 16:43 supports asking qualified experts when knowledge is
missing. These anchors motivate careful record handling and clinician review;
they are not biomedical evidence and not privacy law.

## Sources

- [HHS de-identification guidance](https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 monitoring recommendations](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
- [Private-to-public case extraction gate](2026-04-28-private-to-public-case-extraction-gate.md)
- [Public case data release gate](2026-04-28-public-case-data-release-gate.md)
- [Private case intake index template](../../../templates/private-case-intake-index-template.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
