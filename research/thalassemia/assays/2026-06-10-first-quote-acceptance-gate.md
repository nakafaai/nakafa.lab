# First Quote Acceptance Gate

Date checked: 2026-06-10
Status: lab quote acceptance gate, not treatment advice and not contact
permission

## Direct Answer

After the June 9 HBG promoter editing refresh, a lab quote is not acceptable if
it only offers HbF or `HBG` measurement. The quote must either support the
multi-endpoint package or clearly price what is missing.

Current operational label:

`case001_first_quote_acceptance_gate_ready`

## Pass, Hold, Reject

| Decision | Meaning |
| --- | --- |
| `quote_acceptance_ready` | Recipient class passes; model, controls, HbF or `HBG`, maturation, viability, alpha-globin/autophagy, hemolysis or membrane safety, raw data, cost, timeline, ethics, biosafety, and material constraints are stated. |
| `quote_acceptance_partial_endpoint_hold` | The lab can answer part of the package, but alpha-globin/autophagy, hemolysis, model relevance, controls, raw data, or cost/timeline are incomplete. |
| `quote_acceptance_rejected` | The offer is HbF-only, requests private records or patient samples, becomes treatment/trial/import/purchase/procurement advice, or cannot state safety and data boundaries. |

## Current Source Read

The June 10 PubMed refresh found active 2026 non-editing and assay-adjacent
signals: a DNMT1 inhibitor paper, decitabine plus RN-1 in beta-thalassemia/HbE
erythroid progenitors, a circRNA erythropoiesis/gamma-globin mechanism paper,
a Southeast Asia alpha-thalassemia erythroid model, a plasma heme assay, and
extracellular-vesicle phenotype-marker context.

These sources strengthen assay discipline. They do not make any first-quote
item a treatment candidate and do not weaken the June 9 rule that HbF-only
claims are insufficient.

## Acceptance Questions

Ask a qualified lab to answer these before any quote is considered usable:

- What erythroid or red-cell model is available, and why is it relevant?
- Which controls are included: positive HbF, vehicle, toxicity, and hemolysis
  or hazard control where applicable?
- Can the lab measure HbF or `HBG`, maturation, viability, and apoptosis?
- Can it measure alpha-globin burden, alpha/non-alpha balance, or autophagy?
- Can it run mature red-cell hemolysis or membrane-safety checks?
- What raw data, method metadata, cost, timeline, ethics, biosafety, and
  material constraints will be reported?

## Boundary

This gate does not authorize contact. Use it only after the June 7 approval
gate and June 8 recipient gate. Do not send raw records, patient samples,
doctor messages, treatment-selection requests, trial-screening requests,
purchase requests, import requests, or procurement requests.

If a lab reply arrives, use the
[first quote response-capture gate](2026-06-13-first-quote-response-capture-gate.md)
before applying this acceptance gate to public repo updates.

## Islamic Motivation Boundary

Quran 13:17 supports discarding weak signals. Here that means rejecting HbF-only
or unsafe quote offers. It is not biomedical evidence for any intervention.

## Sources

- [Workflow JSON](../../../data/workflows/case-001/2026-06-10-first-quote-acceptance-gate.json)
- [June 10 PubMed compact snapshot](../../../data/literature/pubmed/2026-06-10-first-quote-acceptance-gate-refresh.json)
- [June 9 HBG promoter editing benchmark refresh](../findings/2026-06-09-hbg-promoter-editing-benchmark-refresh.md)
- [First quote request table](2026-06-02-first-quote-request-table.md)
- [Minimum assay readiness gate](2026-05-31-minimum-assay-readiness-gate.md)
- [Dual HbF and alpha-globin autophagy assay spec](2026-04-27-dual-hbf-alpha-autophagy-assay-spec-v0.md)
- [PubMed PMID `41347631`](https://pubmed.ncbi.nlm.nih.gov/41347631/)
- [PubMed PMID `41555220`](https://pubmed.ncbi.nlm.nih.gov/41555220/)
- [PubMed PMID `41790270`](https://pubmed.ncbi.nlm.nih.gov/41790270/)
- [PubMed PMID `42162272`](https://pubmed.ncbi.nlm.nih.gov/42162272/)
- [PubMed PMID `42020947`](https://pubmed.ncbi.nlm.nih.gov/42020947/)
- [PubMed PMID `42174368`](https://pubmed.ncbi.nlm.nih.gov/42174368/)
- [Quran 13:17 research-method note](../../islamic/quran/013-ar-rad/017.md)
