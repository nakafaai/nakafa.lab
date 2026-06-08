# Lab Recipient Qualification Gate

Date checked: 2026-06-08
Status: recipient qualification gate, not contact permission and not treatment
advice

## Purpose

This gate defines how to qualify a possible lab recipient before any approved
quote packet is sent. It does not name a lab, contact a lab, or authorize
outreach.

Current operational label:

`case001_lab_recipient_qualification_gate_hold`

## Current Read

| Layer | Result | Meaning |
| --- | --- | --- |
| Literature activity | A 2024-2026 PubMed query for thalassemia plus `HUDEP2`, `CD34`, erythroid, HbF, or `HBG` returned 246 records. | The assay-model space is active enough that recipient capability must be specific. |
| Assay anchors | PubMed resolved model and readout anchors for AMPK beta1/HbF, endogenous HbF reporter, small-molecule HbF screen, hemolysis assay, beta-thalassemia/HbE erythroid progenitors, and flow cytometric HbF. | A qualified lab should name model, readouts, controls, and raw-data export. |
| Registry boundary | ClinicalTrials.gov CD34/HbF queries returned gene-cell therapy benchmark records. | Do not treat trial or therapy centers as preclinical assay vendors. |
| Approval | No founder approval is recorded. | Do not contact a lab. |

## Recipient Classes

| Class | Useful for | Qualification requirement |
| --- | --- | --- |
| Quote admin or CRO feasibility | Cost, timeline, sample requirements, and capability routing. | Must accept public-safe preclinical context only. |
| Erythroid HbF screening lab | `HBG1` / `HBG2`, HbF protein or F-cell, maturation, viability. | Must separate HbF signal from toxicity or blocked maturation. |
| Primary erythroid or disease-model lab | CD34+ erythroid differentiation or beta-thalassemia/HbE context. | Must state ethics, sample, and disease-model constraints clearly. |
| Mature red-cell safety lab | Hemolysis or membrane-damage rejection threshold. | Must document red-cell source, controls, and raw-data format. |
| Clinical trial or therapy center | Benchmark context only. | Do not approach as a preclinical quote lab. |

## Pass / Hold / Reject

- Pass: the recipient can answer model, readout, controls, raw-data, cost,
  timeline, ethics, biosafety, and material constraints without requesting
  private case records.
- Hold: the recipient has partial capability but cannot yet state sample,
  ethics, material-transfer, or raw-data constraints.
- Reject for this lane: the recipient asks for raw records, patient samples, or
  treatment-selection context before an approved clinical pathway exists.

## Decision

Keep recipient selection on hold until explicit founder approval exists and at
least one recipient class passes this qualification gate.

## Islamic Motivation Boundary

Quran 13:17 supports discarding weak or misleading signals. Quran 55:7-9
supports measured claims. These anchors are not biomedical evidence and do not
authorize lab contact.

## Sources

- [June 8 workflow map](../../../data/workflows/case-001/2026-06-08-lab-recipient-qualification-gate.json)
- [June 7 lab outreach approval gate](2026-06-07-lab-outreach-approval-gate.md)
- [June 2 first quote request table](2026-06-02-first-quote-request-table.md)
- [PubMed PMID 41259521](https://pubmed.ncbi.nlm.nih.gov/41259521/)
- [PubMed PMID 39108322](https://pubmed.ncbi.nlm.nih.gov/39108322/)
- [PubMed PMID 39504332](https://pubmed.ncbi.nlm.nih.gov/39504332/)
- [PubMed PMID 36769243](https://pubmed.ncbi.nlm.nih.gov/36769243/)
- [PubMed PMID 33879818](https://pubmed.ncbi.nlm.nih.gov/33879818/)
- [PubMed PMID 15163316](https://pubmed.ncbi.nlm.nih.gov/15163316/)
- [ClinicalTrials.gov](https://clinicaltrials.gov/)
- [Quran 13:17 benefit-versus-foam anchor](../../islamic/quran/013-ar-rad/017.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
