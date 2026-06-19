# Recipient Evidence Card Gate

Date checked: 2026-06-18
Status: recipient qualification dry-run, not contact permission and not treatment advice

## Direct Answer

The next blocker is recipient qualification. Since scoped approval is still a
human decision, the repo can still improve readiness by making a public-safe
evidence card for future lab or CRO candidates. The card classifies capability
from public sources only. It must not name, contact, endorse, or clinically
route any real organization.

Current operational label:

`case001_recipient_evidence_card_template_ready_no_recipient_selected`

## Required Public Fields

June 19 refinement: for a real future recipient candidate, raw source URLs that
identify the organization belong in a private source index. The public card
should use a `source_bundle_ref` plus capability labels.

| Field | Requirement |
| --- | --- |
| Recipient alias | De-identified candidate label only. |
| Recipient class | Preclinical quote, erythroid/HbF, disease-model, or red-cell safety class. |
| Public sources | Source-bundle refs or non-identifying generic sources; no raw candidate URLs or private messages. |
| Model capability | HUDEP2-like, CD34 erythroid, disease model, mature red-cell only, or unclear. |
| Core endpoints | HbF or HBG, maturation, viability, and hemolysis or heme safety. |
| Execution metadata | Raw data, controls, replicate plan, cost, timeline, ethics, biosafety, and material constraints. |

## Decision Labels

| Label | Meaning |
| --- | --- |
| `recipient_evidence_card_preclinical_quote_candidate` | Public evidence supports a preclinical quote capability card. |
| `recipient_evidence_card_hold_missing_capability` | A required model, endpoint, data, cost, timeline, or constraint field is missing. |
| `recipient_evidence_card_wrong_owner_hold` | The candidate is a therapy or trial owner, not a preclinical assay recipient. |
| `recipient_evidence_card_release_blocked` | Real identity, private reply, patient data, sample, treatment, trial, purchase, import, procurement, or source-free claims appear. |

## Source Read

The June 18 source pass supports the same recipient capability questions:
HUDEP2/HbF reporter systems, CD34+ beta-thalassemia erythropoiesis models, HbF
flow cytometry, hemolysis cytotoxicity, and a current PubMed heme-assay record.
These sources help define evidence-card fields; they do not identify or qualify
any real recipient.

## Islamic Motivation Boundary

Quran 49:6 supports verifying reports before acting. Quran 4:58 supports
routing trusts to the right owner. These are process ethics only, not
biomedical evidence.

## Boundary

This gate does not diagnose, select therapy, change transfusion or chelation,
screen for a trial, request a sample, buy or import a compound, choose a lab, or
contact anyone.

## Sources

- [Workflow JSON](../../../data/workflows/case-001/2026-06-18-recipient-evidence-card-gate.json)
- [June 18 PubMed refresh](../../../data/literature/pubmed/2026-06-18-recipient-evidence-card-refresh.json)
- [Recipient evidence card template](../../../templates/lab-recipient-evidence-card-template.md)
- [Lab recipient qualification gate](2026-06-08-lab-recipient-qualification-gate.md)
- [Private send readiness gate](2026-06-17-private-send-readiness-gate.md)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 4:58 owner-responsibility anchor](../../islamic/quran/004-an-nisa/058.md)
- [PubMed PMID `39108322`](https://pubmed.ncbi.nlm.nih.gov/39108322/)
- [PubMed PMID `23861885`](https://pubmed.ncbi.nlm.nih.gov/23861885/)
- [PubMed PMID `36769243`](https://pubmed.ncbi.nlm.nih.gov/36769243/)
- [PubMed PMID `42020947`](https://pubmed.ncbi.nlm.nih.gov/42020947/)
