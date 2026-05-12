# Case-001 Mitapivat Jurisdiction Access Verification Gate

Date checked: 2026-05-12
Evidence label: jurisdiction and access verification gate, not medical advice

## Direct Answer

After separating mitapivat label and trial contexts, the next blocker is
jurisdiction access verification. Foreign approval, a registry record, and a
trial country list are not the same as local availability for case-001.

Case-001 should use this label:

`mitapivat_jurisdiction_access_verification_ready`

## What Changed

The May 12 current-registry snapshot found six active or active-not-recruiting
mitapivat query records. One is query-adjacent sickle-cell context and must not
be treated as thalassemia access evidence. The remaining records include adult
NTDT, adult TDT, and pediatric TDT/NTDT thalassemia contexts.

The jurisdiction pass also separates:

- United States: FDA adult thalassemia approval for Aqvesme.
- Saudi Arabia: SFDA adult thalassemia registration for Pyrukynd.
- European Union: EMA positive CHMP opinion source found; current European
  Commission authorisation state still needs direct verification before access
  claims.
- Indonesia: local BPOM registration remains unverified in this public pass.

## Verification Questions

Use these as narrow questions for the hematologist, hospital pharmacist,
trial/contact owner, or regulator-facing contact:

1. Is mitapivat registered, importable, reimbursed, or formulary-accessible in
   the relevant care jurisdiction?
2. If not registered locally, is there any legal named-patient, compassionate,
   special-access, or clinical-trial pathway that a clinician can verify?
3. Which safety and monitoring requirements would the local system require
   before even considering relevance?
4. Which local owner can answer this: hematologist, hospital pharmacy,
   regulatory affairs, insurer, trial site, or manufacturer medical
   information?

## Blocked Claims

- No claim that FDA or SFDA approval means Indonesia access.
- No claim that a trial country means current recruitment, availability, or
  eligibility.
- No claim that case-001 should receive mitapivat.
- No public raw records, identifiers, doctor messages, or exact private dates.
- No dosing, start, stop, substitution, transfusion, chelation, supplement, or
  travel advice.

## Operational Rule

Every mitapivat access claim must name the jurisdiction, source type,
date checked, owner to verify, and safe state. If any of those are missing, use
`local_access_unverified`.

## Biomedical Boundary

This gate does not diagnose thalassemia subtype, recommend mitapivat, change
standard care, decide trial eligibility, or decide import/legal access. It only
keeps access evidence auditable before clinician review.

## Islamic Motivation Boundary

Quran 49:6 supports verifying consequential reports before acting. Quran 16:43
supports expert consultation. Quran 55:7-9 supports measured claims and
anti-exaggeration. These are method anchors, not biomedical evidence.

## Sources

- [May 12 active mitapivat thalassemia registry snapshot](../../../data/registries/clinicaltrials/2026-05-12-active-mitapivat-thalassemia.json)
- [Mitapivat jurisdiction access map](../../../data/regulatory/mitapivat/2026-05-12-mitapivat-jurisdiction-access-map.json)
- [FDA Aqvesme approval page](https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-first-oral-treatment-anemia-thalassemia-inherited-blood-disorder)
- [Aqvesme FDA label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/216196s003lbl.pdf)
- [SFDA Pyrukynd thalassemia registration announcement](https://www.sfda.gov.sa/en/news/4197558)
- [SFDA mitapivat product page](https://www.sfda.gov.sa/en/node/5014016)
- [EMA Pyrukynd variation page](https://www.ema.europa.eu/en/medicines/human/variation/pyrukynd)
- [BPOM drug-registration portal](https://registrasiobat.pom.go.id/en)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
