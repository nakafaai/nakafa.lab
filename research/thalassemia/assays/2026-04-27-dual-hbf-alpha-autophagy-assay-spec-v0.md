# Assay Spec: Dual HbF And Alpha-Globin Autophagy Readouts V0

Date checked: 2026-04-27
Status: qualified-lab readout specification, not a patient treatment plan

## Purpose

This spec converts the mechanism gap matrix into a practical assay gate.

The project should not promote a candidate because HbF alone rises. A
cure-oriented beta-thalassemia signal should ask whether the same candidate also
improves the alpha-globin burden or autophagy side of the disease biology while
preserving erythroid maturation and mature red-cell safety.

## Minimum Readout Set

| Readout | Preferred method | Why it matters |
| --- | --- | --- |
| `HBG1/HBG2` messenger RNA | qPCR, ddPCR, or RNA-seq | confirms gamma-globin transcription |
| HbF protein | HPLC, intracellular flow, immunoassay, or endogenous reporter | confirms transcript-to-protein translation |
| F-cell percentage | intracellular HbF flow cytometry | checks whether HbF is broadly distributed across erythroid cells |
| alpha/non-alpha globin balance | HPLC, globin-chain assay, mass spectrometry, or lab-equivalent method | beta-thalassemia damage includes chain imbalance |
| free or insoluble alpha-globin | membrane globin assay, fractionation, immunoblot, or validated equivalent | directly tests alpha-globin burden |
| `ULK1` state | qPCR, immunoblot, phospho-readout, or lab-equivalent method | links to autophagy-mediated free alpha-globin clearance |
| p62 / `SQSTM1` state | immunoblot, flow, or lab-equivalent method | helps avoid false autophagy interpretation |
| autophagy flux control | lab-approved flux marker, inhibitor control, or time-course | separates true clearance biology from static marker noise |
| erythroid maturation | `CD71`, `CD235a`, Band3, CD49d, enucleation, or lab-equivalent flow panel | rejects candidates that trap cells in an immature state |
| viability and apoptosis | viability dye and apoptosis assay | rejects stress-driven HbF artifacts |
| mature red-cell hemolysis | hemolysis or membrane-damage assay | rejects candidates that worsen red-cell fragility |

## Expanded Readouts

These are useful if a qualified lab can add them without weakening the minimum
panel:

| Readout | Preferred method | Why it matters |
| --- | --- | --- |
| `AHSP` mRNA or protein | qPCR, ddPCR, RNA-seq, immunoblot, flow-compatible antibody, or lab-equivalent method | tests whether a candidate changes alpha-globin buffering, not just alpha-globin clearance |

## Evidence Anchors

| Source signal | Assay lesson |
| --- | --- |
| PMID `31434755` | `ULK1` can mediate free alpha-globin clearance in beta-thalassemia models. |
| PMID `37339583` | `miR-144/451` loss can stimulate `ULK1`-mediated autophagy of free alpha-globin. |
| PMID `39693613` | `AMBRA1` mutations can aggravate beta-thalassemia through impaired autophagy-mediated free alpha-globin clearance. |
| PMID `37894732` | Sirolimus-treated beta-thalassemia erythroid precursors showed `ULK1` increase, p62 reduction, and lower alpha-globin. |
| PMID `38891049` | Review-level synthesis frames HbF induction and autophagy induction as alpha-globin-burden reduction strategies. |
| PMID `35092867` | `NRF2` can expand the `AHSP` pool in beta-thalassemia model context. |
| PMID `38731008` | Sirolimus-treated beta-thalassemia erythroid precursors can show increased `AHSP` mRNA. |
| PMID `20815047` | `AHSP` overexpression alone did not produce major hematologic rescue in a murine beta-thalassemia model. |

## Pass, Hold, Reject

Pass to deeper testing only if:

- HbF or F-cell signal increases reproducibly;
- alpha/non-alpha globin balance improves or does not worsen;
- free or insoluble alpha-globin decreases, or a validated equivalent improves;
- `ULK1`, p62/`SQSTM1`, or flux-aware readouts support useful clearance
  biology;
- erythroid maturation is preserved;
- viability and apoptosis do not indicate nonspecific stress;
- mature red-cell hemolysis does not increase.

Hold if:

- HbF rises but alpha-globin burden is not measured;
- alpha-globin changes but HbF/F-cell readouts are missing;
- autophagy is measured only by one static marker without flux context;
- the model is K562-only, reporter-only, or missing maturation markers;
- compound identity, extract standardization, or batch traceability is
  incomplete.

Reject if:

- HbF rises only with viability loss;
- free or insoluble alpha-globin increases;
- erythroid maturation collapses;
- mature red-cell hemolysis increases;
- the candidate is immune-active or hazard-first and lacks a qualified
  monitoring or safety plan.

## Candidate Interpretation

| Candidate class | Dual-readout expectation |
| --- | --- |
| hydroxyurea | positive HbF comparator; not expected to solve every alpha-globin/autophagy endpoint |
| sirolimus | monitored autophagy/HbF/`AHSP` comparator; requires strict immune and drug-monitoring boundary |
| `AMPKB1` / `NRF2` lane | target-discovery bridge; `AHSP` is an optional buffer readout, not proof of rescue |
| metformin | translational warning comparator; not promoted because retrieved NTDT evidence did not show extra benefit over stable hydroxyurea |
| curcuminoid or resveratrol seeds | must show HbF plus safety before autophagy language is used |
| ginger/6-shogaol support lane | red-cell support comparator unless HbF and alpha-globin endpoints are proven |
| bee venom or melittin | hazard control only; hemolysis boundary comes before efficacy |

## Lab Output Table

Every dual-readout run should return this compact table:

```text
candidate:
identity_or_batch:
model:
concentration_range:
vehicle:
HBG1:
HBG2:
HbF_protein:
F_cell_percentage:
alpha_non_alpha_balance:
free_or_insoluble_alpha_globin:
ULK1_state:
p62_SQSTM1_state:
autophagy_flux_context:
AHSP_mRNA_or_protein_optional:
erythroid_maturation:
viability:
apoptosis:
mature_rbc_hemolysis:
assay_interference:
dual_readout_decision:
reason:
raw_data_location:
```

## Research Decision

Use this spec when a candidate claims any of the following:

- HPFH-like HbF rescue;
- alpha-globin cleanup;
- `ULK1`, `AMBRA1`, p62/`SQSTM1`, `AMPKB1`, `NRF2`, or autophagy biology;
- reduced globin-chain imbalance;
- red-cell survival support with a cure-like framing.

Do not use this spec to justify patient treatment. It is a qualified-lab
research gate.

## Sources

- [Mechanism gap matrix](../findings/2026-04-27-mechanism-gap-matrix.md)
- [AMPKB1 autophagy HbF bridge](../findings/2026-04-27-ampkb1-autophagy-hbf-bridge.md)
- [AMPK/NRF2 expansion gate](../findings/2026-04-27-ampk-nrf2-expansion-gate.md)
- [AHSP alpha-globin buffer gate](../findings/2026-04-27-ahsp-alpha-globin-buffer-gate.md)
- [HPFH-like assay readout spec V0](2026-04-27-hpfh-like-assay-readout-spec-v0.md)
- [Red-cell metabolism readout spec V0](2026-04-27-red-cell-metabolism-readout-spec-v0.md)
- [Alpha-globin/autophagy PubMed snapshot](../../../data/literature/pubmed/2026-04-27-gap-matrix-positive-alpha-autophagy.json)
- [Novelty boundary HbF-alpha-autophagy snapshot](../../../data/literature/pubmed/2026-04-27-novelty-boundary-hbf-alpha-autophagy.json)
- [AMBRA1 Blood article, PMID 39693613](https://pubmed.ncbi.nlm.nih.gov/39693613/)
- [miR-144/451 Blood article, PMID 37339583](https://pubmed.ncbi.nlm.nih.gov/37339583/)
- [ULK1 Science Translational Medicine article, PMID 31434755](https://pubmed.ncbi.nlm.nih.gov/31434755/)
- [Sirolimus ULK1 alpha-globin article, PMID 37894732](https://pubmed.ncbi.nlm.nih.gov/37894732/)
- [NRF2 AHSP article, PMID 35092867](https://pubmed.ncbi.nlm.nih.gov/35092867/)
- [Sirolimus AHSP article, PMID 38731008](https://pubmed.ncbi.nlm.nih.gov/38731008/)
