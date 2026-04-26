# Finding: K562 To HUDEP2 Validation Guardrail

Date checked: 2026-04-27
Evidence label: assay interpretation guardrail, not treatment advice

## Working Conclusion

K562 reporter activity is useful for seed discovery, but it is not enough to
rank a compound as a credible thalassemia therapy hypothesis.

For Nakafa Lab, every K562-only HbF seed must pass through a stricter validation
ladder:

1. chemistry identity and batch purity;
2. K562 reporter repeat only as a cheap first screen;
3. endogenous `HBG1/HBG2` or HbF protein readout in a more relevant erythroid
   system;
4. HUDEP2 or primary erythroid maturation validation;
5. beta-thalassemia/HbE primary-cell validation when accessible;
6. mature red-cell hemolysis and toxicity gates.

This guardrail prevents false confidence from comparing fold-change values
across different reporter constructs, doses, and cell models.

## Why This Matters

The current natural-product HbF seeds are not on equal evidence footing:

| Seed | Current strongest evidence | Interpretation |
| --- | --- | --- |
| `T-BDMC` | K562 plus beta-thalassemia/HbE primary erythroid evidence | strongest natural-product-adjacent seed so far |
| `isocoronarin D` | K562 gamma-globin reporter `FC 1.6` at `20 uM` | chemistry-resolved, but K562-only at current retrieval level |
| `3,4'-Di-O-methylquercetin` | Springer abstract reports K562 reporter `2.6-fold` at `8 uM` | chemistry-resolved, but K562-only at current retrieval level |

`3,4'-Di-O-methylquercetin` should not outrank `T-BDMC` merely because its
abstract-level K562 fold-change is numerically higher. Model relevance matters
more than raw fold-change.

## Assay Sources

Verheul 2024 describes an endogenously tagged fetal-hemoglobin reporter based
on adult erythroid progenitor HUDEP2 cells. The key methodological shift is
that the reporter is integrated at the endogenous `HBG1` gene, and the authors
report high sensitivity and specificity for fetal hemoglobin induction.

Yang 2024 uses a HUDEP2 `HBG1` HiBiT reporter to screen about 5000 annotated
clinical-stage or FDA-approved compounds. The strongest workflow point is not
the screen size alone; it is that top hits were orthogonally confirmed in
parental HUDEP2 cells and human primary `CD34+` hematopoietic stem/progenitor
cells.

## Research Decision

Update the assay gate:

- K562-only hits stay in the seed queue.
- Endogenous HUDEP2/HBG1 reporter confirmation is the preferred next screen.
- Human primary `CD34+` or beta-thalassemia/HbE primary erythroid validation is
  the promotion gate.
- Mature red-cell hemolysis stays mandatory before patient-facing discussion.

## Sources

- [Verheul 2024 PubMed snapshot](../../../data/literature/fulltext/pubmed/2026-04-27-verheul-2024-endogenous-hbf-reporter.dom.txt)
- [Yang 2024 PubMed snapshot](../../../data/literature/fulltext/pubmed/2026-04-27-small-molecule-hbf-agonists.dom.txt)
- [Verheul 2024 PubMed PMID 39108322](https://pubmed.ncbi.nlm.nih.gov/39108322/)
- [Yang 2024 PubMed PMID 39504332](https://pubmed.ncbi.nlm.nih.gov/39504332/)
- [Epigenetic HbF screen V0](../assays/2026-04-27-epigenetic-hbf-screen-v0.md)
- [Natural-product HbF expansion map](2026-04-27-natural-product-hbf-expansion-map.md)
