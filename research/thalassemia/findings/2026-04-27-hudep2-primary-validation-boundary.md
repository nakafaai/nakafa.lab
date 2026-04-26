# Finding: HUDEP2 Primary Validation Boundary

Date checked: 2026-04-27
Evidence label: assay-validation boundary, not treatment advice

## Working Conclusion

Yang 2024 strengthens the HbF assay ladder, but it does not validate every
novel hit equally.

The source selected three compounds for human primary erythroid `CD34+`
validation: `pomalidomide`, `avadomide`, and `idoxuridine`. Among the four novel
hit names, only `avadomide` clearly crosses from HUDEP2 reporter hit into the
primary-cell validation lane in the published text.

Therefore:

- `avadomide` is the strongest novel benchmark from this paper;
- `autophinib`, `triciribine`, and `R574` / probable `R547` should stay in
  reporter-hit or pathway-probe status until primary erythroid or
  beta-thalassemia/HbE replication is found;
- natural-product seeds must not be promoted on K562 evidence alone when even
  some HUDEP2 hits lack primary-cell validation.

## Fig 4 Dose-Response Signals

The Fig 4 supporting workbook gives a useful toxicity boundary:

| Hit | HiBiT fold-change pattern | Viability pattern | Interpretation |
| --- | --- | --- | --- |
| `avadomide` | about `26.1x`, `27.0x`, `15.9x`, `8.7x` at `10`, `3.3`, `1.1`, `0.37 uM` | about `92.8%`, `105.0%`, `86.7%`, `87.8%` | strong reporter signal with preserved viability in this assay |
| `triciribine` | about `1.3x`, `4.1x`, `4.4x`, `3.2x` | about `17.7%`, `32.0%`, `54.4%`, `109.5%` | reporter signal is entangled with high-concentration viability loss |
| `autophinib` | about `0.7x`, `1.3x`, `3.6x`, `2.9x` | about `45.6%`, `68.4%`, `78.8%`, `92.4%` | lower-dose signal is more interesting than high-dose toxicity |

`R574` / probable `R547` remains difficult to extract cleanly from the workbook
labels in the first pass, so it should not outrank the molecules with visible
dose-response rows.

## Research Decision

The HUDEP2 benchmark queue should be split:

1. primary-cell benchmark: `avadomide`;
2. source positive comparators: `pomalidomide` and `idoxuridine`;
3. pathway probes requiring independent validation: `autophinib`,
   `triciribine`, and `R574` / probable `R547`.

This is directly relevant to thalassemia discovery. A candidate is not
interesting because it raises a reporter once; it becomes interesting when it
raises endogenous HbF while preserving erythroid viability and then survives a
primary or disease-cell model.

## Sources

- [Yang 2024 PLOS snapshot](../../../data/literature/fulltext/pubmed/2026-04-27-yang-2024-hudep2-hbf-agonists-plos.dom.txt)
- [Yang 2024 Fig 4 supporting data](../../../data/literature/supplementary/plos/2026-04-27-yang-2024-fig4-lead-hit-drugs-s003.xlsx)
- [Yang 2024 Fig 5 supporting data](../../../data/literature/supplementary/plos/2026-04-27-yang-2024-fig5-cd34-s004.xlsx)
- [HUDEP2 small-molecule hit map](2026-04-27-hudep2-small-molecule-hit-map.md)
- [R574 / R547 label resolution](2026-04-27-r574-r547-label-resolution.md)
