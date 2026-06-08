# Lab Outreach Approval Gate

Date checked: 2026-06-07
Status: approval gate, not contact permission and not treatment advice

## Purpose

This gate defines what can and cannot leave the repository if founder approval
is later given for lab quote outreach. It does not send, authorize, or imply
permission to contact any lab.

Current operational label:

`case001_lab_outreach_approval_gate_hold`

## Current Read

| Layer | Result | Send meaning |
| --- | --- | --- |
| Source freshness | PubMed IDs `41259521`, `36769243`, `40938906`, `33879818`, and `24857542` resolved on 2026-06-07 | The evidence trail still resolves. |
| Compound identity | PubChem resolved hydroxyurea, resveratrol, sirolimus, melittin, PF-06409577, `T-BDMC`, and 6-shogaol CIDs | Material names can stay in the quote table. |
| Registry sanity check | ClinicalTrials.gov searches for thalassemia resveratrol and PF-06409577 thalassemia returned no studies | Do not frame these as clinical access or trial lanes. |
| Held-item cleanup | Ginger and `T-BDMC` now have separate held gates | Keep them out of the first quote lines. |
| Approval | No founder approval is recorded in the repo | Do not contact a lab. |

## If Founder Approval Is Later Given

The outgoing packet may include only:

- public-safe preclinical lab quote context;
- the June 2 first quote request table;
- lab capability questions for erythroid model, HbF/`HBG`, maturation,
  viability, hemolysis, autophagy, cost, timeline, and raw-data format;
- public source links.

Use the [lab recipient qualification gate](2026-06-08-lab-recipient-qualification-gate.md)
before selecting any recipient.

First quote items remain:

- hydroxyurea positive HbF comparator;
- purified resveratrol preclinical seed;
- sirolimus mTOR/autophagy comparator;
- melittin hemolysis hazard control only if the lab accepts it;
- PF-06409577 `PRKAB1` expansion probe.

Held addenda, not quote lines:

- standardized 6-shogaol-rich ginger extract;
- `T-BDMC` or `HY-N11902` catalog lead.

## Blocked Material

Do not send raw records, patient samples, doctor messages, owner replies,
names, direct identifiers, screenshots, prescriptions, lab reports, private
family notes, treatment-selection requests, dosing requests, trial-screening
requests, travel requests, import requests, purchase requests, or procurement
requests.

## Decision

Keep outreach blocked until explicit founder approval is recorded. If approval
is given, send only the public-safe preclinical quote packet and keep held
items as addenda.

## Islamic Motivation Boundary

Quran 13:17 supports discarding weak signals. Quran 55:7-9 supports measured
claims. These are research-method anchors, not biomedical evidence for any
quote item or outreach decision.

## Sources

- [June 7 workflow map](../../../data/workflows/case-001/2026-06-07-lab-outreach-approval-gate.json)
- [June 2 first quote request table](2026-06-02-first-quote-request-table.md)
- [June 5 ginger extract standardization gate](2026-06-05-ginger-extract-standardization-gate.md)
- [June 6 T-BDMC catalog feasibility gate](2026-06-06-t-bdmc-catalog-feasibility-gate.md)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/)
- [PubChem](https://pubchem.ncbi.nlm.nih.gov/)
- [ClinicalTrials.gov](https://clinicaltrials.gov/)
- [Quran 13:17 benefit-versus-foam anchor](../../islamic/quran/013-ar-rad/017.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
