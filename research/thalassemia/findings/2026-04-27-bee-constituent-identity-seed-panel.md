# Finding: Bee Constituent Identity Seed Panel

Date checked: 2026-04-27
Evidence label: constituent identity and evidence-gap triage, not treatment advice

## Working Conclusion

The bee-derived lane should move from broad labels to auditable constituents.
The first seed panel is melittin, apamin, 10-HDA, caffeic acid phenethyl ester,
chrysin, pinocembrin, and quercetin.

This panel does not show a bee-derived thalassemia cure. It gives Nakafa Lab a
cleaner way to decide what is testable, what is hazard-first, and what should
stay outside patient-facing claims.

## Seed Panel

| Constituent | Source lane | PubChem CID | ChEMBL signal | First-pass thalassemia/HbF status | Decision |
| --- | --- | --- | --- | --- | --- |
| Melittin | bee venom peptide | `16133648` | `CHEMBL412927` | no Title/Abstract hit for thalassemia, HbF, or gamma-globin | hazard-first only |
| Apamin | bee venom peptide | `16133797` | `CHEMBL525408` | no Title/Abstract hit for thalassemia, HbF, or gamma-globin | hazard-first only |
| 10-HDA | royal jelly fatty acid | `5312738` | noisy/low-information search hit | no Title/Abstract hit for thalassemia, HbF, or gamma-globin | identity seed only |
| Caffeic acid phenethyl ester | propolis constituent | `5281787` | `CHEMBL319244` | no strict Title/Abstract hit for thalassemia, HbF, or gamma-globin | identity seed only |
| Chrysin | propolis/flavonoid lane | `5281607` | `CHEMBL117` | first-pass hits are indirect, not a thalassemia cure signal | low-priority mechanistic seed |
| Pinocembrin | propolis/flavonoid lane | `68071` | `CHEMBL399910` | no Title/Abstract hit for thalassemia, HbF, or gamma-globin | identity seed only |
| Quercetin | propolis/flavonoid/polyphenol lane | `5280343` | `CHEMBL50` | thalassemia major oxidative-stress and iron-overload literature exists | adjunct biology seed, not HbF cure |

## Interpretation

- Venom peptides stay behind hemolysis and allergy gates before any HbF
  question.
- 10-HDA and CAPE are now identifiable candidates, but first-pass direct HbF
  or thalassemia evidence is missing.
- Quercetin is the strongest bee-adjacent/polyphenol lead in this panel for
  thalassemia context, but the signal is oxidative stress, iron burden, and
  liver/inflammation support, not a curative fetal-hemoglobin mechanism.
- Chrysin and pinocembrin should not be promoted unless future evidence links
  them to erythroid maturation, HbF, globin balance, or red-cell safety.

## Assay Implication

The first experimental question for this panel is not patient dosing. It is:

- does the constituent damage mature red cells?
- does it affect `HBG1/HBG2`, HbF protein, or F-cell percentage in erythroid
  systems?
- does it preserve erythroid maturation and viability?
- is the dose remotely plausible after considering solubility, bioavailability,
  allergy, and monitoring burden?

Anything that fails identity, hemolysis, or viability should stop before
translation discussion.

## Sources

- [PubChem bee-constituent snapshots](../../../data/chemistry/pubchem/bee-constituents/)
- [ChEMBL bee-constituent snapshots](../../../data/chemistry/chembl/bee-constituents/)
- [Melittin thalassemia/HbF PubMed gap snapshot](../../../data/literature/pubmed/2026-04-27-melittin-thalassemia-hbf-gap.json)
- [Apamin thalassemia/HbF PubMed gap snapshot](../../../data/literature/pubmed/2026-04-27-apamin-thalassemia-hbf-gap.json)
- [10-HDA thalassemia/HbF PubMed gap snapshot](../../../data/literature/pubmed/2026-04-27-10-hda-thalassemia-hbf-gap.json)
- [CAPE thalassemia/HbF PubMed gap snapshot](../../../data/literature/pubmed/2026-04-27-cape-thalassemia-hbf-gap.json)
- [Chrysin thalassemia/HbF PubMed snapshot](../../../data/literature/pubmed/2026-04-27-chrysin-thalassemia-hbf-gap.json)
- [Pinocembrin thalassemia/HbF PubMed gap snapshot](../../../data/literature/pubmed/2026-04-27-pinocembrin-thalassemia-hbf-gap.json)
- [Quercetin thalassemia/HbF PubMed snapshot](../../../data/literature/pubmed/2026-04-27-quercetin-thalassemia-hbf-gap.json)
- [Bee-derived materials beyond honey](2026-04-26-bee-derived-materials-beyond-honey.md)
- [Chemistry identity benchmark map](2026-04-27-chemistry-identity-benchmark-map.md)
