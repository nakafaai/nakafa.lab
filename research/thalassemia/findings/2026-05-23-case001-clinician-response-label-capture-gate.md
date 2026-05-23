# Case-001 Clinician Response Label Capture Gate

Date checked: 2026-05-23
Evidence label: clinician-response label capture, not medical advice

## Direct Answer

The next blocker after the May 22 packet index is response capture.

When a doctor replies, the repo should not paste the answer. It should convert
the reply into domain labels, missing-record categories, owner categories, and a
next gate.

Current operational label:

`case001_clinician_response_label_capture_ready`

## Source Refresh

The May 23 source refresh changes context but not the safety boundary.

- FDA sources support adult mitapivat regulatory context for anemia in adults
  with alpha- or beta-thalassemia, plus REMS and liver-safety context.
- Agios announced European Commission adult thalassemia approval for Pyrukynd on
  2026-05-22. This is access context, not a local availability or individual-fit
  conclusion.
- `NCT07506863` pediatric TDT and `NCT07517133` pediatric NTDT remain
  not-yet-recruiting records with no posted results in the May 23 API check.
- `NCT04770779` adult TDT remains active-not-recruiting with posted results and
  an actual enrollment of 258, so it stays adult benchmark context until a
  clinician reviews case fit.

## Capture Contract

| Step | Private action | Public output |
| --- | --- | --- |
| `store_raw_reply_private_only` | Save the raw reply outside Git. | `raw_reply_received_private_only` |
| `extract_domain_answered` | Mark the answered domain. | `domain_label_only` |
| `classify_response_type` | Map to confirmed, corrected, not confirmable, not applicable, or specialist review. | `response_type_label_only` |
| `map_missing_records_and_owner` | Capture missing record and owner categories. | `missing_record_owner_labels_only` |
| `map_mitapivat_context_if_mentioned` | Separate adult-label, adult-trial, pediatric-watchlist, access-owner, safety-owner, or not-relevant labels. | `mitapivat_context_label_only` |
| `release_public_label_only` | Run release review before Git updates. | `public_label_release_ready` |

## Stop Conditions

Stop before public release if the reply contains:

- raw records, screenshots, or exact private dates;
- clinician names, hospital names, phone numbers, contact details, or owner
  replies;
- patient-specific treatment instructions;
- dose, access, import, travel, or trial-screening instructions;
- a free-text answer that cannot be reduced to an allowed label.

## Biomedical Boundary

This gate does not diagnose subtype, recommend mitapivat, change transfusion or
chelation, decide local access, decide affordability, or screen a trial. Adult
approval and adult trial context only make the clinician question more precise:
is this lane worth qualified review after the case labels and missing records
are validated?

## Islamic Motivation Boundary

Quran 49:6 supports verification before acting on consequential reports. Quran
16:43 supports qualified expert consultation. Quran 55:7-9 supports measured
claims and anti-exaggeration. These are research-method anchors, not biomedical
evidence.

## Sources

- [Clinician response label-capture map](../../../data/workflows/case-001/2026-05-23-clinician-response-label-capture.json)
- [Case-001 clinician confirmation packet index](../case-context/case-001-clinician-confirmation-packet-index.md)
- [Case-001 doctor response triage](../case-context/case-001-doctor-response-triage.md)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [FDA AQVESME approval page](https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-first-oral-treatment-anemia-thalassemia-inherited-blood-disorder)
- [FDA AQVESME approval letter](https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2025/216196Orig1s002,s003ltr.pdf)
- [Agios European Commission approval announcement](https://investor.agios.com/news-releases/news-release-details/european-commission-approves-agios-pyrukyndr-mitapivat-first)
- [ClinicalTrials.gov NCT07506863](https://clinicaltrials.gov/study/NCT07506863)
- [ClinicalTrials.gov NCT07517133](https://clinicaltrials.gov/study/NCT07517133)
- [ClinicalTrials.gov NCT04770779](https://clinicaltrials.gov/study/NCT04770779)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
