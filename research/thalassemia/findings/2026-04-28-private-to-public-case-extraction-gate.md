# Finding: Private-To-Public Case Extraction Gate

Date checked: 2026-04-28
Evidence label: security, privacy, and research-operations guardrail, not
medical advice

## Working Conclusion

Nakafa Lab can use private family-supplied records only through a controlled
extraction path:

`private_raw_record -> deidentified_extract_candidate -> public_summary_ready`

The public repository must not become a medical-record store. It can hold only
the minimum de-identified facts needed for research routing, clinician
questions, and source-backed case gates.

## Source-Backed Privacy Anchor

HHS de-identification guidance describes two HIPAA Privacy Rule routes:
expert determination and safe harbor. It also emphasizes that health data can
identify a person directly or through context, and that identifiers in free
text must be handled as carefully as structured fields.

Nakafa Lab is not claiming legal HIPAA compliance. The repo uses this source as
a conservative public-repo benchmark:

- remove direct identifiers;
- reduce context that could re-identify a person;
- document what was extracted and what was omitted;
- keep raw records outside Git.

## Practical Threat Model

| Asset | Abuse path | Mitigation in this repo |
| --- | --- | --- |
| Raw PDFs, scans, photos, and report layouts | A public commit exposes direct identifiers or visual identifiers. | Block raw case media paths and keep source files outside Git. |
| Local file paths and Downloads references | A public commit leaks the family member's workstation context. | `scripts/check_public_repo.py` blocks local user, Downloads, and macOS temporary paths. |
| Direct identifiers in extracted case text | A public summary accidentally includes a name, record number, phone, email, or exact birth date. | Case-context scanner now blocks label-value identifier patterns. |
| Patient-specific action claims | A research note could be mistaken for dosing, transfusion, chelation, or therapy instruction. | Public release checklist blocks treatment claims and requires clinician-review language. |
| Rare fact combinations | Even without names, a narrow story can re-identify a person. | Extraction template requires omitted-material notes and broad timing. |

## Tooling Update

The public checker now has case-context-specific content checks for:

- email-like strings;
- phone or fax label-value patterns;
- medical record, hospital, accession, national, insurance, or record
  identifier label-value patterns;
- exact birth-date label-value patterns;
- patient-name label-value patterns.

These checks are intentionally scoped to public case-context prose so public
literature snapshots can keep legitimate author affiliations, trial locations,
and registry metadata.

## New Reusable Template

Use
[`private-to-public-case-extraction-template.md`](../../../templates/private-to-public-case-extraction-template.md)
before turning private source material into public case context.

The template forces four decisions:

1. source class;
2. release class;
3. extracted fact candidate;
4. omitted material.

## Case-001 Implication

The existing case-001 extraction remains an allowed public summary because it
omits raw files, identifiers, facility names, doctor names, exact sample date,
and local paths. Any future update from PDFs, blood-bank documents, genetic
reports, transfusion logs, or clinician letters must pass this extraction gate
before entering the repo.

## Islamic Motivation Boundary

Quran 55:7-9 supports careful measure and avoiding distortion in claims. Quran
16:43 supports asking qualified experts when knowledge is missing. Here these
anchors motivate privacy discipline and clinician review; they are not used as
biomedical evidence or legal authority.

## Sources

- [HHS de-identification guidance](https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification)
- [Public case data release gate](2026-04-28-public-case-data-release-gate.md)
- [Private-to-public case extraction template](../../../templates/private-to-public-case-extraction-template.md)
- [Public repo checker](../../../scripts/check_public_repo.py)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
