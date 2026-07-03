# Case-001 Branch Review Clinician Brief Gate

Date checked: 2026-07-02
Status: clinician-brief sequence gate, not treatment advice

## Direct Answer

The doctor-facing artifact should not be the full main paper. It should be a
short branch-review brief that asks the clinician to do three things in order:

1. say whether the six private packet domains are complete enough to review;
2. if complete, answer one branch-scope question;
3. return only labels and missing-record requests that can later be summarized
   publicly.

Current operational label:

`case001_branch_review_clinician_brief_ready_general_only`

## The One Branch-Scope Question

After private packet review, ask:

> Are any domains still missing before you can answer whether Case-001 belongs
> in allogeneic HCT discussion, autologous gene-cell therapy discussion,
> non-curative disease modification, standard-care stabilization first, or
> benchmark-only tracking?

If the packet is incomplete, the useful answer is not a therapy branch. The
useful answer is which packet domains are missing and who owns them.

## Required Private Packet Domains

| Domain | Why the clinician needs it |
| --- | --- |
| Diagnosis, genotype, phenotype | Branch relevance depends on confirmed disease type and molecular context. |
| Transfusion burden and response | Severity, annual burden, and response pattern frame any advanced-therapy discussion. |
| Blood-bank and immune history | Alloantibodies, DAT, reactions, matching, and spleen context can change risk and priority. |
| Iron, organ-risk, chelation status | Liver iron, cardiac `T2*`, ferritin, organ risk, and chelator safety shape timing and risk. |
| HCT/gene-cell access context | Donor, HLA, center, payer, geography, fertility, and travel constraints decide whether branches are discussable. |
| Consent, ethics, owner review | Consequential routing requires private-record owner handling and qualified clinical review. |

## Output Requested From Clinician

Ask for one of these response shapes:

- packet complete enough for branch discussion;
- packet incomplete, with missing domains named;
- stabilization or safety issues should be reviewed first;
- one or more branches are in scope for private specialist review;
- branch discussion should stay benchmark-only for now;
- cannot answer from current packet.

These are workflow and review labels. They are not treatment instructions.

## Boundary

Quran 49:6, 4:58, and 16:43 are process-ethics anchors only. They support
verification, trust routing, and expert consultation. They are not biomedical
evidence.

This gate does not provide diagnosis, treatment selection, eligibility,
trial-screening instruction, referral, travel guidance, import guidance,
purchase guidance, dosing, transfusion change, chelation change, lab contact,
private-message routing, or sample-routing permission.

## Sources

- [July 2 source JSON](../../../data/literature/pubmed/2026-07-02-branch-review-clinician-brief-refresh.json)
- [July 2 workflow JSON](../../../data/workflows/case-001/2026-07-02-branch-review-clinician-brief-gate.json)
- [Updated doctor handoff brief](case-001-doctor-handoff-brief.md)
- [Updated doctor handoff PDF source](../../../paper/case-001-doctor-handoff.tex)
- [TIF 2025 HCT chapter](https://www.ncbi.nlm.nih.gov/books/NBK614242/)
- [TIF 2025 gene manipulation chapter](https://www.ncbi.nlm.nih.gov/books/NBK614241/)
- PubMed records: [PMID 42274009](https://pubmed.ncbi.nlm.nih.gov/42274009/),
  [PMID 42252696](https://pubmed.ncbi.nlm.nih.gov/42252696/),
  [PMID 41955126](https://pubmed.ncbi.nlm.nih.gov/41955126/),
  [PMID 41919270](https://pubmed.ncbi.nlm.nih.gov/41919270/),
  [PMID 42091200](https://pubmed.ncbi.nlm.nih.gov/42091200/),
  [PMID 41947014](https://pubmed.ncbi.nlm.nih.gov/41947014/),
  [PMID 42362985](https://pubmed.ncbi.nlm.nih.gov/42362985/),
  [PMID 40058646](https://pubmed.ncbi.nlm.nih.gov/40058646/)
