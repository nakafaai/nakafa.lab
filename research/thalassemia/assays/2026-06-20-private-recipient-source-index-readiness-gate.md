# Private Recipient Source Index Readiness Gate

Date checked: 2026-06-20
Status: private-index template readiness, not contact permission and not treatment advice

## Direct Answer

The next unresolved blocker after the June 19 source-privacy gate is the absence
of a private source index. The repo can safely add the template and readiness
logic now, but it must not contain any real candidate identity or raw candidate
URL.

Current operational label:

`case001_private_source_index_template_ready_no_real_sources`

## Private Index Fields

| Field | Purpose |
| --- | --- |
| `recipient_alias` | Stable alias such as `recipient-candidate-001`. |
| `source_bundle_ref` | Private bundle key reused by the public card. |
| `raw_source_url` | Real candidate URL; private only. |
| `candidate_identity_private` | Real organization or owner identity; private only. |
| `source_kind_label` | Publication, method page, capability page, registry, or unclear. |
| `capability_mapping` | Model, endpoint, raw-data, cost, timeline, ethics, biosafety, or material label. |
| `privacy_review_label` | Whether the public summary has been checked for identity leakage. |

## Decision Labels

| Label | Meaning |
| --- | --- |
| `private_recipient_source_index_ready` | Private row has source evidence and maps to a public-safe bundle ref. |
| `private_recipient_source_index_hold_missing_source` | Raw source URL, candidate identity, or bundle reference is missing privately. |
| `private_recipient_source_index_hold_mapping_incomplete` | Source exists but capability mapping or privacy review is incomplete. |
| `private_recipient_source_index_release_blocked_public_leak` | Public output leaks raw URL, real identity, contact, private reply, patient material, sample, treatment, trial, purchase, import, or procurement scope. |

## Current Source Read

The June 20 source refresh did not change the biomedical action boundary.
Current thalassemia, gamma-globin, HUDEP2/HbF, CD34 erythroid, hemolysis,
heme-assay, and therapy/trial-review records support source-to-capability
mapping only. HHS privacy guidance supports keeping identifying material out of
public outputs. The RIKEN HUDEP-2 page remains a generic capability source, not
a recipient-selection source.

## Islamic Motivation Boundary

Quran 49:6 supports verifying reports before acting. Quran 4:58 supports
routing trusts to the right owner. These are process ethics only, not
biomedical evidence.

## Boundary

This gate does not select a lab, contact anyone, request samples, interpret
private replies, screen for a trial, buy or import a compound, or recommend a
treatment.

## Sources

- [Workflow JSON](../../../data/workflows/case-001/2026-06-20-private-recipient-source-index-readiness-gate.json)
- [June 20 source refresh](../../../data/literature/pubmed/2026-06-20-private-recipient-source-index-refresh.json)
- [Private source index note](../../../docs/private-recipient-source-index.md)
- [Private source index CSV template](../../../templates/private-recipient-source-index-template.csv)
- [Recipient source privacy gate](2026-06-19-recipient-source-privacy-gate.md)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 4:58 owner-responsibility anchor](../../islamic/quran/004-an-nisa/058.md)
- [HHS de-identification guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html)
- [HHS Privacy Rule summary](https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html)
- [RIKEN HUDEP-2 source page](https://cellbank.brc.riken.jp/cell_bank/CellInfo/?cellNo=RCB4557)
- [PubMed PMID `31424735`](https://pubmed.ncbi.nlm.nih.gov/31424735/)
- [PubMed PMID `41411145`](https://pubmed.ncbi.nlm.nih.gov/41411145/)
- [PubMed PMID `39108322`](https://pubmed.ncbi.nlm.nih.gov/39108322/)
- [PubMed PMID `23861885`](https://pubmed.ncbi.nlm.nih.gov/23861885/)
- [PubMed PMID `36769243`](https://pubmed.ncbi.nlm.nih.gov/36769243/)
- [PubMed PMID `41348010`](https://pubmed.ncbi.nlm.nih.gov/41348010/)
- [PubMed PMID `39794549`](https://pubmed.ncbi.nlm.nih.gov/39794549/)
- [PubMed PMID `42020947`](https://pubmed.ncbi.nlm.nih.gov/42020947/)
