# Founder Approval Record Gate

Date checked: 2026-06-16
Status: approval-record gate, not contact permission and not treatment advice

## Direct Answer

The next blocker is not more biology. The next blocker is a durable, public-safe
approval record. The public repository should record approval state as labels,
never raw messages, names, contacts, exact private send details, or owner
identities.

Current operational label:

`case001_founder_approval_record_gate_ready`

## Public Approval Labels

| Label | Meaning |
| --- | --- |
| `approval_not_recorded` | No approval record exists yet. Contact remains blocked. |
| `approval_denied` | Approval was denied. Contact remains blocked. |
| `founder_review_only` | Packet may be reviewed privately, but send remains blocked. |
| `approval_scope_public_safe_quote_only` | Approval is limited to a public-safe preclinical quote workflow. |
| `approval_expired_or_superseded` | A prior approval cannot be used for the current packet. |
| `approval_release_blocked` | Private, clinical, sample, trial, purchase, import, procurement, or ambiguous scope blocks release. |

## Pass And Stop Rules

A scoped public label requires an outside-Git approval record, private founder
identity, explicit packet version, public-safe preclinical quote scope,
continued recipient qualification, continued response capture, and blocked
content acknowledgment.

Use `approval_release_blocked` if the public record includes raw messages,
private contacts, patient records, patient samples, treatment language,
trial-screening language, purchase, import, procurement, or ambiguous scope.

The label still does not send anything. A future private send workflow also
needs the June 8 recipient qualification gate, the June 15 packet gate, and the
June 13 response-capture path.

## Source Read

The June 16 source check did not change the approval boundary. Recent
pyruvate-kinase, erythroid-metabolism, gamma-globin, and HBG editing sources
remain benchmark or optional-endpoint context. A Guangxi 2026 ex vivo
SNH-119014 pyruvate-kinase activator study supports keeping metabolism readouts
visible, not treatment, procurement, or patient-specific action.

## Boundary

This gate does not diagnose, select therapy, change transfusion or chelation,
screen for a trial, request a sample, buy or import a compound, select a lab, or
authorize contact. Quran 49:6 is used only as a verification ethic; Quran 5:2 is
used only as a bounded-cooperation ethic. Neither is biomedical evidence.

## Sources

- [Workflow JSON](../../../data/workflows/case-001/2026-06-16-founder-approval-record-gate.json)
- [June 16 current literature refresh](../../../data/literature/pubmed/2026-06-16-founder-approval-record-refresh.json)
- [Approval record template](../../../templates/lab-outreach-approval-record-template.md)
- [First quote outbound packet gate](2026-06-15-first-quote-outbound-packet-gate.md)
- [Lab recipient qualification gate](2026-06-08-lab-recipient-qualification-gate.md)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 5:2 cooperation anchor](../../islamic/quran/005-al-maidah/002.md)
- [PubMed PMID `42261266`](https://pubmed.ncbi.nlm.nih.gov/42261266/)
- [PubMed PMID `41411145`](https://pubmed.ncbi.nlm.nih.gov/41411145/)
- [PubMed PMID `41184165`](https://pubmed.ncbi.nlm.nih.gov/41184165/)
- [Frontiers SNH-119014 source](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2026.1719328/full)
