# Case-001 Mitapivat First-Contact Packet Gate

Date checked: 2026-05-14
Evidence label: first-contact outreach gate, not medical advice

## Direct Answer

After owner routing, the next blocker is first-contact packet discipline. The
first message to any owner should not carry raw records or ask for a treatment
decision. It should ask one narrow, owner-matched question and attach only
public-safe sources.

Case-001 should use this label:

`mitapivat_first_contact_packet_ready`

## First-Contact Rule

Every first-contact packet must include:

- one owner;
- one question;
- one jurisdiction or public registry ID;
- one allowed public source bundle;
- one blocked-material list;
- one escalation condition;
- one safe state.

If a packet needs raw records, case identifiers, exact dates, a treatment
request, or legal-import instructions, it is not a first-contact packet.

## Owner-Specific Packets

| Owner | First-contact goal | Safe state |
| --- | --- | --- |
| Treating hematologist | Ask whether mitapivat is clinically worth reviewing at all. | `clinical_first_contact_ready` |
| Hospital or specialty pharmacy | Ask what dispensing, formulary, certification, or special-access steps require verification. | `pharmacy_first_contact_ready` |
| Regulator or regulatory-affairs contact | Ask whether any product-registration, legal import, named-patient, compassionate-use, or special-access pathway exists. | `regulatory_first_contact_ready` |
| Manufacturer medical information | Ask what official regional route a clinician should use for medical information or product-status routing. | `manufacturer_first_contact_ready` |
| Trial site or registry contact | Ask whether a public registry ID has an open contact process. | `trial_first_contact_ready` |
| Payer or financial-access owner | Ask what coverage, reimbursement, or support verification process applies after clinician relevance and legal pathway review. | `financial_first_contact_ready` |

## Blocked Claims

- No dosing, start, stop, transfusion, chelation, supplement, travel, import,
  or legal instruction.
- No claim that case-001 is eligible or ineligible for mitapivat or a trial.
- No raw lab PDFs, screenshots, identifiers, doctor messages, exact private
  dates, or private financial documents in public or first-contact material.
- No request for manufacturer, pharmacy, payer, or trial owner to replace the
  treating hematologist.
- No assumption that a foreign approval, REMS process, support program, or trial
  country list creates local access.

## Escalation Rule

Escalate only when the contacted owner gives a public-safe next state, names the
next owner, or requests clinician-mediated documents. Keep private documents in
the private workspace and release only de-identified labels to the repo.

## Biomedical Boundary

This gate does not diagnose thalassemia subtype, recommend mitapivat, change
standard care, decide trial eligibility, or decide legal access. It only
constrains the first outreach message.

## Islamic Motivation Boundary

Quran 5:2 is used as a bounded-cooperation anchor: help should be truthful,
lawful, qualified, and privacy-preserving. Quran 4:58 supports routing
responsibilities to the proper owner. Quran 49:6 supports verification before
acting. These are method anchors, not biomedical evidence.

## Sources

- [Mitapivat first-contact packet map](../../../data/regulatory/mitapivat/2026-05-14-mitapivat-first-contact-packet-map.json)
- [Mitapivat owner route map](../../../data/regulatory/mitapivat/2026-05-13-mitapivat-owner-route-map.json)
- [Aqvesme FDA label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/216196s003lbl.pdf)
- [AQVESME official site](https://www.aqvesme.com/)
- [Agios healthcare-provider and medical-information page](https://www.agios.com/patients-partners/healthcare-providers/)
- [Agios medicines page](https://www.agios.com/our-medicines/)
- [ClinicalTrials.gov how to read a study record](https://clinicaltrials.gov/study-basics/how-to-read-study-record)
- [TIF 2025 TDT guideline](https://www.ncbi.nlm.nih.gov/books/NBK614251/)
- [BPOM drug-registration portal](https://registrasiobat.pom.go.id/en)
- [HHS de-identification guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html)
- [Quran 5:2 cooperation anchor](../../islamic/quran/005-al-maidah/002.md)
- [Quran 4:58 owner-responsibility anchor](../../islamic/quran/004-an-nisa/058.md)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
