# Recipient Source Privacy Gate

Date checked: 2026-06-19
Status: public-card privacy refinement, not contact permission and not treatment advice

## Direct Answer

The June 18 recipient evidence card had a tension: it required public source
evidence, but raw candidate URLs can identify the real lab or CRO. The June 19
gate resolves this by separating private source auditability from public
release.

Current operational label:

`case001_recipient_source_private_index_required`

## Public vs Private Split

| Layer | Allowed content |
| --- | --- |
| Private source index outside Git | Real candidate name, raw source URLs, contacts, private notes, and source-to-capability mapping. |
| Public recipient card | Alias, `source_bundle_ref`, source-kind labels, source-count label, capability labels, constraints, and decision label. |
| Generic public sources | Assay literature, guideline pages, or method resources that do not identify a specific future recipient candidate. |

## Decision Labels

| Label | Meaning |
| --- | --- |
| `recipient_source_privacy_public_card_ready` | Public card has a private source-bundle ref and capability labels without identifying a real candidate. |
| `recipient_source_privacy_hold_missing_private_index` | A candidate cannot be audited because the private source bundle is missing or incomplete. |
| `recipient_source_privacy_hold_source_free` | A capability claim has no source trail. |
| `recipient_source_privacy_release_blocked_identifying_source` | Public content includes raw candidate URLs, real names, contacts, private replies, patient material, samples, treatment, trial, purchase, import, or procurement scope. |

## Current Source Read

The June 19 source check keeps assay evidence and privacy handling separate.
Current thalassemia and gamma-globin records support endpoint specificity, while
HUDEP2/HbF, CD34+ erythroid, hemolysis, and heme-assay records support
capability labels. HHS de-identification guidance supports not publishing
information that can identify a protected subject. The RIKEN HUDEP-2 page shows
that capability pages can be useful evidence, but a specific provider/resource
page can also disclose ownership and terms. For real candidate recipients, that
source trail should therefore be private.

## Islamic Motivation Boundary

Quran 49:6 supports verifying reports before acting. Quran 4:58 supports
routing trusts to the right owner. These are process ethics only, not
biomedical evidence.

## Boundary

This gate does not select a lab, contact anyone, request samples, interpret
private replies, screen for a trial, buy or import a compound, or recommend a
treatment.

## Sources

- [Workflow JSON](../../../data/workflows/case-001/2026-06-19-recipient-source-privacy-gate.json)
- [June 19 source refresh](../../../data/literature/pubmed/2026-06-19-recipient-source-privacy-refresh.json)
- [Recipient evidence card template](../../../templates/lab-recipient-evidence-card-template.md)
- [Recipient evidence card gate](2026-06-18-recipient-evidence-card-gate.md)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 4:58 owner-responsibility anchor](../../islamic/quran/004-an-nisa/058.md)
- [HHS de-identification guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html)
- [RIKEN HUDEP-2 source page](https://cellbank.brc.riken.jp/cell_bank/CellInfo/?cellNo=RCB4557)
- [PubMed PMID `31424735`](https://pubmed.ncbi.nlm.nih.gov/31424735/)
- [PubMed PMID `41411145`](https://pubmed.ncbi.nlm.nih.gov/41411145/)
- [PubMed PMID `39108322`](https://pubmed.ncbi.nlm.nih.gov/39108322/)
- [PubMed PMID `23861885`](https://pubmed.ncbi.nlm.nih.gov/23861885/)
- [PubMed PMID `36769243`](https://pubmed.ncbi.nlm.nih.gov/36769243/)
- [PubMed PMID `42020947`](https://pubmed.ncbi.nlm.nih.gov/42020947/)
