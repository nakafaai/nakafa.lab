# Finding: AHSP Alpha-Globin Buffer Gate

Date checked: 2026-04-27
Status: expanded assay readout, not a therapy claim

## Working Conclusion

Alpha-hemoglobin-stabilizing protein (`AHSP`) should be added to the Nakafa Lab
dual-readout assay map as an optional expanded readout for alpha-globin
buffering. It should not be promoted as a standalone cure or patient-facing
therapy lane.

The reason is specific: `AHSP` is close to the disease mechanism because it
buffers free alpha-globin, but the intervention evidence does not show that
raising `AHSP` alone is enough to rescue beta-thalassemia.

## Evidence Table

| Source | What it supports | Boundary |
| --- | --- | --- |
| PMID `21490703` | `AHSP` is an erythroid molecular chaperone for free alpha-globin and is relevant to beta-thalassemic erythroid precursors. | Review-level mechanism, not intervention evidence. |
| PMID `31894534` | `AHSP` is discussed as a modulatory factor in beta-thalassemia severity. | Modulation is not a cure claim. |
| PMID `35092867` | `NRF2` can expand the `AHSP` pool in beta-thalassemia model context, and `AHSP` knockdown worsened alpha-globin precipitation and ROS in thalassemic erythroid cells. | Cellular and mouse-model context; not a validated patient therapy. |
| PMID `38731008` | Sirolimus-treated beta-thalassemia erythroid precursor cells showed increased `AHSP` mRNA, and the authors proposed `AHSP` as a clinical-trial endpoint. | Exploratory endpoint evidence; sirolimus remains immune-active and monitor-only. |
| PMID `20815047` | Supraphysiologic `AHSP` overexpression did not produce major hematologic rescue in a murine beta-thalassemia intermedia model. | This blocks simplistic "more AHSP equals cure" framing. |

## Assay Consequence

If a qualified lab can measure `AHSP` without making the first quote too large,
add one of these readouts:

- `AHSP` mRNA by qPCR, ddPCR, or RNA-seq;
- `AHSP` protein by immunoblot, flow-compatible antibody, or lab-equivalent
  method.

Interpret `AHSP` only beside the core dual-readout panel:

- HbF protein or F-cell percentage;
- alpha/non-alpha globin balance;
- free or insoluble alpha-globin;
- `ULK1`, p62 / `SQSTM1`, or flux-aware autophagy context;
- erythroid maturation;
- viability, apoptosis, and mature red-cell hemolysis.

## Decision

Add `AHSP` as `expanded_readout_optional`.

Do not add an `AHSP inducer` therapy lane unless future evidence shows a
defined, safe intervention that improves HbF or F-cells, alpha-globin burden,
erythroid maturation, viability, and hemolysis in beta-thalassemia-relevant
cells.

## Sources

- [AHSP buffer gate notebook](../notebooks/2026-04-27-ahsp-buffer-gate.ipynb)
- [AHSP selected abstracts](../../../data/literature/pubmed/2026-04-27-ahsp-selected-abstracts.xml)
- [Broad AHSP PubMed snapshot](../../../data/literature/pubmed/2026-04-27-ahsp-beta-thalassemia-alpha-globin-search.json)
- [NRF2 AHSP PubMed snapshot](../../../data/literature/pubmed/2026-04-27-nrf2-ahsp-beta-thalassemia-search.json)
- [Sirolimus AHSP PubMed snapshot](../../../data/literature/pubmed/2026-04-27-sirolimus-ahsp-beta-thalassemia-search.json)
- [AHSP overexpression PubMed snapshot](../../../data/literature/pubmed/2026-04-27-ahsp-overexpression-beta-thalassemia-search.json)
- [NRF2 AHSP article, PMID 35092867](https://pubmed.ncbi.nlm.nih.gov/35092867/)
- [Sirolimus AHSP article, PMID 38731008](https://pubmed.ncbi.nlm.nih.gov/38731008/)
- [AHSP overexpression article, PMID 20815047](https://pubmed.ncbi.nlm.nih.gov/20815047/)
