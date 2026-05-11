# Case-001 Mitapivat Boundary And Access Inquiry Gate

Date checked: 2026-05-11
Evidence label: regulatory and registry boundary, not medical advice

## Direct Answer

The next blocker after registry-link disambiguation is mitapivat context
separation. Nakafa Lab can now discuss four different public contexts without
mixing them:

- `approved_adult_label_context`: FDA approval and label context for adults
  with alpha- or beta-thalassemia anemia in the United States.
- `adult_tdt_trial_context`: `NCT04770779` / ENERGIZE-T, an adult
  transfusion-dependent alpha- or beta-thalassemia phase 3 record.
- `pediatric_tdt_trial_context`: `NCT07506863`, a not-yet-recruiting pediatric
  transfusion-dependent alpha- or beta-thalassemia phase 3 record.
- `pediatric_ntdt_trial_context`: `NCT07517133`, a not-yet-recruiting pediatric
  non-transfusion-dependent alpha- or beta-thalassemia phase 3 record.

Case-001 should use this label:

`mitapivat_boundary_access_inquiry_ready`

## Why This Matters

Mitapivat is no longer only a watchlist molecule in the United States: FDA
approved Aqvesme for anemia in adults with alpha- or beta-thalassemia. That
does not make it a cure, does not decide relevance for case-001, and does not
replace clinician review.

The pediatric registry records are separate from the adult approval context.
The TDT and NTDT pediatric records also have different endpoints:
`NCT07506863` uses transfusion reduction response, while `NCT07517133` uses
hemoglobin response. Mixing these records would make the doctor question
unclear.

## Clinician Inquiry Questions

Use these as narrow questions for a hematologist or qualified trial/contact
owner:

1. Which context is clinically relevant to review, if any: adult approved label,
   adult TDT trial evidence, pediatric TDT trial context, pediatric NTDT trial
   context, or none?
2. What records are required before discussing relevance: molecular diagnosis,
   age and weight band, transfusion burden, pre/post hemoglobin trend, iron and
   organ status, liver tests, medication list, and local access constraints?
3. Does the FDA label's liver-risk, REMS, and drug-interaction language create
   any special review requirement before this can even be discussed for
   case-001?
4. Is there a local availability, compassionate-use, trial-site, or referral
   pathway to verify, or is the record only global access-mapping context?

## Blocked Claims

- No dosing, start, stop, substitution, transfusion, chelation, supplement, or
  travel advice.
- No claim that case-001 is eligible or ineligible for mitapivat or a trial.
- No claim that adult FDA approval applies to a pediatric case.
- No claim that a registry record means access in Indonesia.
- No raw records, screenshots, identifiers, doctor messages, or exact private
  dates in the public repo.

## Biomedical Boundary

This gate is about context separation and inquiry quality. It does not diagnose
thalassemia subtype, decide trial eligibility, recommend mitapivat, or change
standard care.

## Islamic Motivation Boundary

Quran 49:6 supports verifying consequential reports before acting. Quran 16:43
supports qualified expert consultation. Quran 55:7-9 supports measured claims
and anti-exaggeration. These are method anchors, not biomedical evidence.

## Sources

- [FDA Aqvesme approval page](https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-first-oral-treatment-anemia-thalassemia-inherited-blood-disorder)
- [Aqvesme FDA label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/216196s003lbl.pdf)
- [ClinicalTrials.gov NCT04770779](https://clinicaltrials.gov/study/NCT04770779)
- [ClinicalTrials.gov NCT07506863](https://clinicaltrials.gov/study/NCT07506863)
- [ClinicalTrials.gov NCT07517133](https://clinicaltrials.gov/study/NCT07517133)
- [NCT04770779 current registry snapshot](../../../data/registries/clinicaltrials/2026-05-11-nct04770779-energize-t-detail.json)
- [NCT07506863 current registry snapshot](../../../data/registries/clinicaltrials/2026-05-11-nct07506863-mitapivat-pediatric-tdt-detail.json)
- [NCT07517133 current registry snapshot](../../../data/registries/clinicaltrials/2026-05-11-nct07517133-mitapivat-pediatric-ntdt-detail.json)
- [Mitapivat ENERGIZE trial, PubMed PMID 40544857](https://pubmed.ncbi.nlm.nih.gov/40544857/)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
