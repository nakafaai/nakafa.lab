# Finding: Curcuminoid Analog Assay Map

Date checked: 2026-04-27
Evidence label: compound and assay map, not treatment advice

## Working Conclusion

The curcuminoid HbF lane should prioritize publication-defined trienone analogs
instead of generic turmeric or curcumin supplement claims.

The key compounds are:

- natural curcuminoids: `Cur`, `DMC`, and `BDMC`;
- trienone analogs: `T-Cur`, `T-DMC`, and especially `T-BDMC`.

`T-BDMC` is the most important seed in the current paper-level evidence map.
It produced the strongest K562 HbF signal in the Scientific Reports study and
also entered beta-thalassemia/HbE primary erythroid validation.

A follow-on natural-product HbF expansion map now tracks adjacent leads from
the same citation neighborhood without promoting them above `T-BDMC`.

## Compound Identity Status

| Compound | Identity status | Research note |
| --- | --- | --- |
| `Cur` | PubChem `CID 969516`, ChEMBL `CHEMBL140` | benchmark natural curcuminoid; supportive biology lane and comparator |
| `DMC` | PubChem `CID 5469424`; ChEMBL search is not clean enough for exact assertion | natural curcuminoid comparator |
| `BDMC` | PubChem `CID 5315472`; ChEMBL search overlaps with DMC-like results | strongest natural curcuminoid in the study's K562 screen |
| `T-Cur` | no first-pass exact PubChem hit; ChEMBL search noisy | publication-defined trienone analog |
| `T-DMC` | no first-pass exact PubChem hit; ChEMBL search noisy | publication-defined trienone analog |
| `T-BDMC` | no first-pass exact PubChem hit; ChEMBL search noisy | highest-priority trienone analog seed |

For the trienone analogs, the current clean identity trail is the publication:
chemical names, synthesis/chemical modification route, and reported purity
greater than 95% by TLC and NMR. They should not be treated as purchasable or
database-normalized compounds until a clean supplier, structure file, or
compound identifier is obtained.

## Assay Map From The Trienone Study

| Layer | Model | Endpoint | Result direction |
| --- | --- | --- | --- |
| Reporter | `K562:Delta G gamma-A gamma EGFP` | gamma-globin promoter reporter | dose-responsive signal across curcuminoids and trienone analogs |
| Endogenous HbF | native K562 | anti-HbF flow cytometry | `T-BDMC` higher than `BDMC`; reported around 2.4-fold HbF in K562 |
| Disease-relevant validation | beta-thalassemia/HbE erythroid progenitors, `n=5` | HbF flow cytometry and F-cell percentage | HbF increased, but F-cell percentage did not reach significance |
| Epigenetic readout | K562 and beta-thalassemia/HbE progenitors | G gamma promoter CpG methylation | demethylation signal strongest/clearest at selected G gamma CpG sites |
| Safety proxy | K562 viability and progenitor cell number | viability/cell number | no major cell-number reduction in the reported primary-cell condition |

## Interpretation

This is a stronger bridge than the quercetin lane because it touches HbF
directly. It is still early:

- K562 is a useful screen but not enough for a therapy claim.
- Primary beta-thalassemia/HbE validation is promising but small.
- F-cell percentage was not significantly increased in the reported primary
  cell experiment.
- The mechanism may include G gamma promoter demethylation, but the authors
  note that other mechanisms may explain primary-cell effects.
- Bioavailability and pharmacokinetics of the trienone analogs remain open.

## Research Decision

Keep `T-BDMC` as a high-priority assay seed, but with strict gates:

- obtain a clean structure file, supplier, or synthesis partner;
- repeat identity and purity checks;
- run hemolysis before any patient-facing discussion;
- test `HBG1/HBG2`, HbF protein, F-cells, globin balance, and erythroid
  maturation;
- compare against hydroxyurea, decitabine, and vehicle controls;
- keep curcumin supplementation separate from trienone analog discovery.

## Sources

- [Nuamsee 2021 Nature snapshot](../../../data/literature/fulltext/nature/2026-04-27-nuamsee-2021-curcuminoid-trienone.html)
- [Nuamsee 2021 PMC snapshot](../../../data/literature/fulltext/nature/2026-04-27-nuamsee-2021-curcuminoid-trienone-pmc.html)
- [PMC Open Access metadata](../../../data/literature/pubmed/2026-04-27-curcuminoid-trienone-pmc-oa.xml)
- [PubMed-to-PMC link snapshot](../../../data/literature/pubmed/2026-04-27-curcuminoid-trienone-pubmed-to-pmc.json)
- [Curcuminoid HbF PubMed ESummary](../../../data/literature/pubmed/2026-04-27-curcuminoid-hbf-esummary.json)
- [Curcuminoid analog PubChem snapshots](../../../data/chemistry/pubchem/curcuminoid-analogs/)
- [Curcuminoid analog ChEMBL search snapshots](../../../data/chemistry/chembl/curcuminoid-analogs/)
- [Curcuminoid HbF bridge deep dive](2026-04-27-curcuminoid-hbf-bridge-deep-dive.md)
- [Natural-product HbF expansion map](2026-04-27-natural-product-hbf-expansion-map.md)
