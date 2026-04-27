# Finding: AMPKB1 Autophagy HbF Bridge

Date checked: 2026-04-27
Evidence label: target-discovery bridge, not treatment advice

## Working Conclusion

`AMPKB1` / `ULK1` / `NRF2` / autophagy is now a high-value target-discovery
lane for Nakafa Lab because it connects two cure-oriented mechanisms:

- fetal hemoglobin induction;
- excess alpha-globin cleanup through autophagy.

This does not prove a beta-thalassemia cure. The strongest `AMPKB1` paper is
still sickle-cell-disease-centered, and the beta-thalassemia autophagy evidence
is strongest around `ULK1`, sirolimus, and alpha-globin reduction. The bridge is
useful because it gives us a coherent assay hypothesis rather than a generic
antioxidant claim.

## Evidence Table

| Source | What it adds | Boundary |
| --- | --- | --- |
| Hara 2025, PMID `41259521` | Selective `AMPKB1` activation increased HbF in human erythroid cells from SCD donors and in Townes SCD mice through a noncanonical `NRF2` pathway involving `ULK1` and `SQSTM1` / p62. | SCD model, not beta-thalassemia patient evidence; Sanofi/patent conflict disclosures require caution. |
| Gambari and Finotti 2024, PMID `38891049` | Review frames beta-thalassemia around excess free alpha-globin and lists HbF induction plus autophagy induction as ways to reduce that burden. | Review-level synthesis; not a clinical trial. |
| Zurlo 2023, PMID `37894732` | Low-dose sirolimus in beta-thalassemia erythroid precursors was associated with reduced p62, increased `ULK1`, and reduced excess alpha-globin; clinical-trial patient ErPCs also showed `ULK1` increase and alpha-globin decrease. | Small mechanistic follow-up; sirolimus needs clinical monitoring and is not a self-treatment candidate. |
| Focused PubMed gap checks | `autophinib` / `VPS34`, `triciribine`, and `R547` focused searches did not find independent fetal-hemoglobin or erythroid validation beyond the Yang 2024 HUDEP2 screen. | These remain pathway probes, not lead therapies. |

## Interpretation

The important shift is that autophagy is not just a side pathway. In
beta-thalassemia, free alpha-globin toxicity is part of the core disease
biology. A useful candidate could therefore work by raising HbF, improving
alpha/non-alpha globin balance, increasing alpha-globin clearance, or combining
more than one of those effects.

This also changes how we interpret HUDEP2 hits:

- `autophinib` should stay on hold even though it appeared in the HUDEP2 hit
  map, because beta-thalassemia autophagy literature points toward inducing
  useful `ULK1`-linked clearance, not blindly inhibiting autophagy;
- `triciribine` remains high-caution because its reporter signal was entangled
  with viability loss and current focused searches did not find independent
  erythroid HbF validation;
- `R574` / probable `R547` remains a CDK-pathway benchmark, not a lead, because
  focused HbF validation searches returned no direct support.

## Assay Gates

Any candidate in this bridge must be tested against both HbF and alpha-globin
cleanup readouts:

- `HBG1` / `HBG2` messenger RNA;
- HbF protein and F-cell percentage;
- alpha/non-alpha globin balance;
- free alpha-globin or insoluble alpha-globin aggregates;
- `ULK1` expression or activation;
- p62 / `SQSTM1` reduction or flux-aware autophagy readout;
- `NRF2` target activation without nonspecific stress toxicity;
- erythroid maturation markers;
- viability and apoptosis;
- mature red-cell hemolysis.

## Research Decision

Promote the bridge as a target-discovery lane.

Do not promote any `AMPKB1`, `NRF2`, autophagy, sirolimus, autophinib,
triciribine, or `R547` claim as a patient treatment from this evidence alone.

The next useful wet-lab design is a dual-readout erythroid assay: HbF induction
plus alpha-globin cleanup. A candidate that only raises a reporter but worsens
viability or blocks useful autophagy should be rejected.

## Sources

- [AMPKB1 HbF NRF2 PubMed XML](../../../data/literature/pubmed/2026-04-27-ampkb1-hbf-nrf2-abstract.xml)
- [Autophagy beta-thalassemia review PubMed XML](../../../data/literature/pubmed/2026-04-27-autophagy-beta-thalassemia-review-abstract.xml)
- [Sirolimus ULK1 alpha-globin PubMed XML](../../../data/literature/pubmed/2026-04-27-sirolimus-ulk1-alpha-globin-abstract.xml)
- [Autophagy fetal-hemoglobin PubMed snapshot](../../../data/literature/pubmed/2026-04-27-autophagy-fetal-hemoglobin-erythroid-search.json)
- [AMPKB1 focused gap snapshot](../../../data/literature/pubmed/2026-04-27-ampkb1-hbf-nrf2-search.json)
- [Autophinib/VPS34 focused gap snapshot](../../../data/literature/pubmed/2026-04-27-vps34-autophinib-fetal-hemoglobin-search.json)
- [Triciribine focused snapshot](../../../data/literature/pubmed/2026-04-27-triciribine-fetal-hemoglobin-search.json)
- [CDK/R547 focused gap snapshot](../../../data/literature/pubmed/2026-04-27-cdk-inhibitor-fetal-hemoglobin-search.json)
- [HUDEP2 primary validation boundary](2026-04-27-hudep2-primary-validation-boundary.md)
