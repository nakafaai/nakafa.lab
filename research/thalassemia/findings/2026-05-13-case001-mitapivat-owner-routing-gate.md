# Case-001 Mitapivat Owner Routing Gate

Date checked: 2026-05-13
Evidence label: owner-routing gate, not medical advice

## Direct Answer

After the jurisdiction access gate, the next blocker is owner routing. A
mitapivat question is unsafe when it is sent to the wrong owner because the
answer can look confident while skipping the person who actually controls the
decision.

Case-001 should use this label:

`mitapivat_owner_routing_ready`

## Owner Routes

| Question type | First owner | Safe state |
| --- | --- | --- |
| Is mitapivat clinically relevant to discuss? | Treating hematologist | `clinical_owner_review_needed` |
| Is local dispensing or pharmacy certification feasible? | Hospital or specialty pharmacy | `pharmacy_owner_review_needed` |
| Is the product registered or legally importable? | Regulator or regulatory-affairs contact | `regulatory_owner_review_needed` |
| What is the official product or regional medical-information route? | Manufacturer medical information | `manufacturer_medinfo_review_needed` |
| Is a study open, screening, or contactable? | Trial site or registry contact | `trial_owner_review_needed` |
| Is coverage, reimbursement, or financial support possible? | Payer or financial-access owner | `financial_owner_review_needed` |

## Why This Matters

The FDA label and AQVESME REMS create prescriber, patient, and pharmacy
requirements in the United States. ClinicalTrials.gov records create registry
questions, not access. The Agios medical page provides manufacturer medical
information and medical-science-liaison routing, but manufacturer information
does not replace a treating clinician.

Therefore, a useful next message is not a broad explanation. It is a routed
question with one owner, one public source, one jurisdiction, and one blocked
claim.

## Safe Questions

1. To hematology: is mitapivat even clinically worth reviewing for this case,
   given diagnosis, age and weight band, transfusion burden, iron and organ
   status, liver tests, medication list, and local access constraints?
2. To pharmacy: can the product be dispensed, imported, or handled through a
   certified or special-access pathway in the relevant jurisdiction?
3. To regulatory affairs: is there a registration, named-patient,
   compassionate-use, or special-access route?
4. To manufacturer medical information: what official regional route should a
   clinician use for medical information, product-status routing, adverse-event
   reporting, or medical-science-liaison contact?
5. To a trial owner: for a public registry ID, is any site open or screening,
   and what is the official contact process?

## Blocked Claims

- No claim that any owner can approve treatment alone.
- No claim that manufacturer medical information is medical care.
- No claim that a registry country list means access or eligibility.
- No claim that a pharmacy, payer, or regulator answer replaces hematology.
- No public raw records, identifiers, doctor messages, or exact private dates.
- No dosing, start, stop, transfusion, chelation, supplement, travel, or import
  instruction.

## Operational Rule

Every outreach row must include exactly one first owner, one question, one
source, one jurisdiction, and one safe state. If a question has multiple
owners, split it before sending.

## Biomedical Boundary

This gate does not diagnose thalassemia subtype, recommend mitapivat, change
standard care, decide trial eligibility, or decide legal access. It only routes
questions to the qualified owner before interpretation.

## Islamic Motivation Boundary

Quran 4:58 is used as an owner-responsibility and trust-routing anchor. Quran
49:6 supports verifying consequential reports before acting. Quran 16:43
supports expert consultation. These are method anchors, not biomedical
evidence.

## Sources

- [Mitapivat owner route map](../../../data/regulatory/mitapivat/2026-05-13-mitapivat-owner-route-map.json)
- [Aqvesme FDA label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/216196s003lbl.pdf)
- [AQVESME official site](https://www.aqvesme.com/)
- [Agios medical information page](https://www.agios.com/medical/)
- [ClinicalTrials.gov](https://clinicaltrials.gov/)
- [TIF 2025 TDT guideline](https://www.ncbi.nlm.nih.gov/books/NBK614251/)
- [BPOM drug-registration portal](https://registrasiobat.pom.go.id/en)
- [Quran 4:58 owner-responsibility anchor](../../islamic/quran/004-an-nisa/058.md)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
