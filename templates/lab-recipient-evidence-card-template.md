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
| Source bundle ref | `private-source-bundle-001`; raw candidate URLs stay outside Git |
| Source-kind labels | publication, method page, capability page, registry, or unclear |
| Source-count label | count or range, without naming the candidate |
| Model capability | `HUDEP2_like`, `CD34_erythroid`, `disease_model`, `mature_red_cell_only`, or `unclear` |
| HbF or HBG capability | `present`, `missing`, or `unclear` |
| Maturation and viability | `present`, `missing`, or `unclear` |
| Hemolysis or heme safety | `present`, `missing`, or `unclear` |
| Raw-data export | `present`, `missing`, or `unclear` |
| Cost and timeline | `present`, `missing`, or `unclear` |
| Ethics and biosafety constraints | `present`, `missing`, or `unclear` |

## Release Blockers

- real recipient identity or contact details;
- raw candidate source URLs that identify a real lab or CRO;
- raw private replies or attachments;
- patient records or sample identifiers;
- treatment, dosing, trial-screening, purchase, import, or procurement language;
- source-free capability claims.

## Source Handling

Real candidate names, domains, pages, people, emails, phone numbers, addresses,
private replies, quotes, and business terms belong in a private source index
outside Git. The public card should only include a `source_bundle_ref`,
source-kind labels, source-count label, capability labels, and the final
decision label.

Use `templates/private-recipient-source-index-template.csv` as the private
index schema. Completed copies must stay under ignored private storage.

Generic assay literature, guidelines, or method pages that do not identify a
future recipient candidate may still be cited publicly.

Public output:

`recipient_evidence_label: <one allowed decision label>`
