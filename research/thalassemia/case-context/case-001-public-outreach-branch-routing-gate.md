# Case-001 Public Outreach Branch Routing Gate

Date checked: 2026-07-04
Status: public outreach routing gate, not treatment advice

## Direct Answer

Public sharing can help Nakafa Lab only if it asks for qualified roles,
bounded domains, and public sources. It should not ask the internet to decide
diagnosis, eligibility, treatment, referral, trial screening, travel, import,
purchase, transfusion, chelation, lab contact, private-message routing, or
sample routing for Case-001.

Current operational label:

`case001_public_outreach_branch_routing_ready_general_only`

Current branch-review state:

`branch_review_handoff_packet_incomplete`

## Public Call Objective

Find people who can help with one safe task:

- identify the correct clinical owner for one packet domain;
- explain a public HCT, gene-cell, or trial pathway without screening the case;
- point to a public registry ID, guideline, paper, or institutional source;
- review wet-lab assay feasibility without receiving patient samples;
- help with privacy-safe tooling, access mapping, funding, or Islamic ethics.

## Allowed Public Reply Fields

Allowed public fields are public alias or organization, claimed role, narrow
domain, public source or registry ID, and general pathway explanation. These
fields support routing without private data transfer.

## Blocked Public Reply Fields

Raw records, screenshots, files, doctor messages, names, hospitals, exact
dates, private contact details, local paths, accession numbers, private
timeline details, diagnosis, prognosis, eligibility, treatment selection,
dosing, transfusion targets, chelation changes, immune medicine changes,
supplement or diet advice, referral instructions, trial-screening instructions,
travel/import/purchase plans, lab contact permission, private-message routing,
and sample-routing requests.

## Reply Routing

| Incoming reply type | Public-safe next state |
| --- | --- |
| Clinical role with bounded packet domain | `role_scope_check_needed` |
| HCT, gene-cell, or trial pathway source | `registry_or_pathway_disambiguation_needed` |
| Wet-lab or assay offer | `assay_feasibility_scope_needed` |
| Software, data, privacy, or source-mapping offer | `repo_task_scope_needed` |
| Funding, logistics, or access offer | `access_mapping_scope_needed` |
| Islamic ethics or tafsir review offer | `ethics_scope_needed` |
| General support without domain | `share_to_qualified_roles` |
| Request for raw records | `blocked_raw_record_request` |
| Public treatment advice | `blocked_treatment_advice` |

## Current Evidence Interpretation

Current guideline, PubMed, and ClinicalTrials.gov sources support public source
routing because thalassemia has multiple active branches. They do not support
public eligibility or treatment selection. Case-specific branch review remains
blocked until qualified review of the private packet.

## Islamic Motivation Boundary

Quran 49:6, 4:58, and 16:43 are process-ethics anchors only. They support
verification, owner-routing, and expert consultation. They are not biomedical
evidence and do not authorize medical decisions.

## Sources

- [July 4 source JSON](../../../data/literature/pubmed/2026-07-04-public-outreach-branch-routing-refresh.json)
- [July 4 workflow JSON](../../../data/workflows/case-001/2026-07-04-public-outreach-branch-routing-gate.json)
- [Updated public share kit](case-001-public-share-kit.md)
- [Public responder qualification](case-001-public-responder-qualification.md)
- [Public collaborator intake](case-001-public-collaborator-intake.md)
- [Case-001 branch review clinician brief gate](case-001-branch-review-clinician-brief-gate.md)
- [TIF 2025 HCT chapter](https://www.ncbi.nlm.nih.gov/books/NBK614242/)
- [TIF 2025 gene manipulation chapter](https://www.ncbi.nlm.nih.gov/books/NBK614241/)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
