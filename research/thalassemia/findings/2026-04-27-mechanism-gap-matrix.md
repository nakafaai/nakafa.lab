# Finding: Mechanism Gap Matrix

Date checked: 2026-04-27
Evidence label: computational literature-mapping experiment, not treatment advice

## Working Conclusion

The literature is not absent. The gap is integration.

Broad component queries retrieve PubMed records for HbF induction, HPFH/HBG
promoter biology, alpha-globin/autophagy biology, and small-molecule HbF work.
The exact Nakafa Lab framing remains sparse or zero-result:

- affordable or practical small molecule;
- `HPFH-like` rescue signature;
- alpha-globin cleanup or autophagy;
- erythroid maturation;
- mature red-cell hemolysis safety;
- beta-thalassemia context.

This supports the current research direction: design a dual-readout assay, not
another unsorted candidate list.

## Matrix Result

| Lane | Role | Count | Label |
| --- | --- | ---: | --- |
| `broad_hbf_induction` | `positive_component` | 10 | `component_evidence` |
| `hpfh_hbg_promoter` | `positive_component` | 6 | `component_evidence` |
| `alpha_globin_autophagy` | `positive_component` | 10 | `component_evidence` |
| `small_molecule_hbf` | `positive_component` | 10 | `component_evidence` |
| `integrated_assay_gates` | `narrow_bridge` | 1 | `narrow_bridge` |
| `hpfh_like_small_molecule` | `gap_boundary` | 0 | `gap_boundary` |
| `hbf_alpha_autophagy_small_molecule` | `gap_boundary` | 0 | `gap_boundary` |
| `affordable_cure_small_molecule` | `gap_boundary` | 0 | `gap_boundary` |

Notebook decision: `integration_gap_confirmed`.

## Important New Signal

The alpha-globin/autophagy query returned direct beta-thalassemia mechanism
sources, including:

- PMID `39693613`: `AMBRA1` mutations aggravating beta-thalassemia by impairing
  autophagy-mediated clearance of free alpha-globin;
- PMID `37339583`: loss of `miR-144/451` stimulating `ULK1`-mediated autophagy
  of free alpha-globin;
- PMID `31434755`: `ULK1` mediating clearance of free alpha-globin in
  beta-thalassemia.

This strengthens the `ULK1` / autophagy / alpha-globin cleanup lane. It does
not make `AMBRA1`, `miR-144/451`, sirolimus, or any autophagy-active compound a
patient treatment. It means our lab readouts should include alpha-globin burden
and autophagy state, not just HbF.

## Research Decision

Keep the next experimental design focused on a combined signal:

1. HbF/F-cell rescue.
2. Alpha-globin burden or alpha/non-alpha globin balance.
3. `ULK1`, p62/`SQSTM1`, or flux-aware autophagy readout.
4. Erythroid maturation.
5. Viability, apoptosis, and mature red-cell hemolysis.

A candidate that raises HbF but worsens alpha-globin precipitates, maturation,
or hemolysis should be rejected.

## Sources

- [Mechanism gap matrix notebook](../notebooks/2026-04-27-mechanism-gap-matrix.ipynb)
- [Broad HbF induction PubMed snapshot](../../../data/literature/pubmed/2026-04-27-gap-matrix-positive-hbf-induction.json)
- [HPFH/HBG promoter PubMed snapshot](../../../data/literature/pubmed/2026-04-27-gap-matrix-positive-hpfh-hbg-promoter.json)
- [Alpha-globin/autophagy PubMed snapshot](../../../data/literature/pubmed/2026-04-27-gap-matrix-positive-alpha-autophagy.json)
- [Small-molecule HbF PubMed snapshot](../../../data/literature/pubmed/2026-04-27-gap-matrix-broad-small-molecule-hbf.json)
- [Integrated assay-gates PubMed snapshot](../../../data/literature/pubmed/2026-04-27-gap-matrix-integrated-assay-gates.json)
- [Novelty boundary for the Nakafa question](2026-04-27-novelty-boundary-for-nakafa-question.md)
- [AMBRA1 Blood article, PMID 39693613](https://pubmed.ncbi.nlm.nih.gov/39693613/)
- [miR-144/451 Blood article, PMID 37339583](https://pubmed.ncbi.nlm.nih.gov/37339583/)
- [ULK1 Science Translational Medicine article, PMID 31434755](https://pubmed.ncbi.nlm.nih.gov/31434755/)
