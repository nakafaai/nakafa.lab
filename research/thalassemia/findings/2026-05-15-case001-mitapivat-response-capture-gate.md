# Case-001 Mitapivat Response-Capture Gate

Date checked: 2026-05-15
Evidence label: response-capture gate, not medical advice

## Direct Answer

After first-contact packets, the next blocker is response capture. Owner replies
can contain private contact details, raw-record requests, patient-specific
advice, adverse-event details, or legal-access language. The public repo should
capture only labels, owners, public source URLs, and next states.

Case-001 should use this label:

`mitapivat_response_capture_ready`

## Capture Rule

Every owner response must be reduced to:

- one response label;
- one owner category;
- one public source or registry ID when available;
- one private-workspace action;
- one public-repo action;
- one next state.

Do not copy raw replies into the public repo.

## Allowed Response Labels

| Response label | Public repo action |
| --- | --- |
| `no_response_yet` | Record unanswered status only. |
| `wrong_owner_redirect` | Record redirect owner category only. |
| `public_source_confirmed` | Record source URL and owner category. |
| `missing_records_named` | Record record-domain labels only. |
| `clinician_mediated_documents_requested` | Record clinician-mediated request label only. |
| `raw_records_requested_public_channel` | Record `release_blocked` only. |
| `local_access_pathway_named` | Record pathway type and public source only. |
| `not_relevant_or_not_available_now` | Record `not_relevant_now` or `local_access_unverified`. |
| `trial_contact_process_confirmed` | Record `NCT` ID and public contact-process label. |
| `safety_or_adverse_event_route_named` | Record route category and public source only. |
| `patient_specific_treatment_advice_received` | Record `treatment_advice_blocked` only. |

## Blocked Material

- raw owner replies;
- private emails, phone numbers, names, hospital contacts, or screenshots;
- raw lab files, doctor messages, or exact private dates;
- patient-specific treatment, dosing, import, travel, or eligibility advice;
- adverse-event narratives or product-quality details tied to a person;
- legal conclusions or instructions.

## Escalation Rule

Escalate only after a response label is assigned. If the response asks for raw
records, patient details, or clinician-mediated documents, move the raw material
to the private workspace and route through the treating clinician or proper
owner.

## Biomedical Boundary

This gate does not diagnose thalassemia subtype, recommend mitapivat, change
standard care, decide trial eligibility, report an adverse event, or decide
legal access. It only governs how responses are reduced before public tracking.

## Islamic Motivation Boundary

Quran 49:6 supports verifying consequential reports before acting. Quran 5:2
supports bounded cooperation that is truthful, lawful, qualified, and
privacy-preserving. Quran 4:58 supports routing responsibilities to the proper
owner. These are method anchors, not biomedical evidence.

## Sources

- [Mitapivat response-capture map](../../../data/regulatory/mitapivat/2026-05-15-mitapivat-response-capture-map.json)
- [Mitapivat first-contact packet map](../../../data/regulatory/mitapivat/2026-05-14-mitapivat-first-contact-packet-map.json)
- [FDA MedWatch adverse-event reporting information](https://www.fda.gov/safety/medwatch-fda-safety-information-and-adverse-event-reporting-program/information-about-reporting-adverse-events-fdas-medwatch-program)
- [FDA reporting serious problems page](https://www.fda.gov/reporting-serious-problems-fda)
- [Agios healthcare-provider and medical-information page](https://www.agios.com/patients-partners/healthcare-providers/)
- [ClinicalTrials.gov how to read a study record](https://clinicaltrials.gov/study-basics/how-to-read-study-record)
- [NLM ClinicalTrials.gov sponsor-contact support article](https://support.nlm.nih.gov/knowledgebase/article/KA-03645/en-us)
- [HHS de-identification guidance](https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 5:2 cooperation anchor](../../islamic/quran/005-al-maidah/002.md)
- [Quran 4:58 owner-responsibility anchor](../../islamic/quran/004-an-nisa/058.md)
