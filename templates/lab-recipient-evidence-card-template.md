# Lab Recipient Evidence Card Template

Status: public-safe recipient qualification worksheet, not contact permission

Use this template to classify a future lab or CRO candidate before any contact.
Do not put real organization names, people, emails, phone numbers, addresses,
raw replies, patient records, patient samples, pricing files, or private dates
in the public repository.

## Public-Safe Fields

| Field | Allowed value |
| --- | --- |
| Recipient alias | `recipient-candidate-001` or similar |
| Recipient class | `quote_admin_or_cro_feasibility`, `erythroid_hbf_screening_lab`, `primary_erythroid_or_disease_model_lab`, or `mature_red_cell_safety_lab` |
| Public source URLs | URLs only, no private messages |
| Model capability | `HUDEP2_like`, `CD34_erythroid`, `disease_model`, `mature_red_cell_only`, or `unclear` |
| HbF or HBG capability | `present`, `missing`, or `unclear` |
| Maturation and viability | `present`, `missing`, or `unclear` |
| Hemolysis or heme safety | `present`, `missing`, or `unclear` |
| Raw-data export | `present`, `missing`, or `unclear` |
| Cost and timeline | `present`, `missing`, or `unclear` |
| Ethics and biosafety constraints | `present`, `missing`, or `unclear` |

## Release Blockers

- real recipient identity or contact details;
- raw private replies or attachments;
- patient records or sample identifiers;
- treatment, dosing, trial-screening, purchase, import, or procurement language;
- source-free capability claims.

Public output:

`recipient_evidence_label: <one allowed decision label>`
