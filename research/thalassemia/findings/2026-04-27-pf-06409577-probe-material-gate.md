# Finding: PF-06409577 Probe Material Gate

Date checked: 2026-04-27
Evidence label: chemistry and literature material gate, not wet-lab evidence and
not treatment advice

## Working Conclusion

PF-06409577 is now the named material anchor for the `AMPKB1` / `NRF2` /
`ULK1` expansion lane.

It passes only as a qualified-lab research probe. It does not pass as a patient
candidate, supplement candidate, or treatment recommendation.

## Why This Matters

The previous `AMPKB1` expansion gate was intentionally phrased as
PF-06409577-style because the repo had not yet pinned a material identity
packet. This update pins the candidate to source-backed chemistry records and
turns the lane into a stricter quote addendum.

The useful question is no longer "should we activate AMPK generically?" The
useful question is:

Can a qualified lab source exact PF-06409577 material and test whether
`AMPKB1`-biased activation creates a dual signal: HbF induction plus
alpha-globin/autophagy improvement without maturation, viability, or hemolysis
failure?

## Material Identity

| Field | Source-backed value |
| --- | --- |
| PubChem CID | `71748255` |
| PubChem title | `PF-06409577` |
| ChEMBL ID | `CHEMBL3891221` |
| Formula | `C19H16ClNO3` |
| Molecular weight | `341.8` in PubChem, `341.79` in ChEMBL |
| InChIKey | `FHQXLWCFSUSXBF-UHFFFAOYSA-N` |

This is enough to ask a lab for exact material sourcing with certificate of
analysis, purity, lot, solvent, and concentration-range documentation. It is
not enough to infer clinical safety or patient efficacy.

## Target-Selectivity Evidence

The ChEMBL activity snapshot supports a beta1-biased AMPK probe interpretation:

- `AMPK alpha1/beta1/gamma1` values include `EC50` or `Kd` values of `3.3`,
  `7.0`, `8.2`, `9.0`, and `28.2 nM`;
- beta2-containing AMPK complexes in the same snapshot have weak `EC50`
  boundaries reported as `>40000 nM`;
- this supports a material-gate claim for assay design, not a therapy claim.

## HbF Bridge Evidence

The PubMed refresh recovers PMID `41259521`, which connects selective
`AMPKB1` activation with fetal hemoglobin induction, noncanonical `NRF2`
biology, `ULK1`, and p62 / `SQSTM1` context.

This bridge is valuable but still incomplete for beta-thalassemia cure work:

- the source is an HbF and sickle-cell-disease-oriented bridge, not a
  beta-thalassemia patient trial;
- it does not replace direct beta-thalassemia primary-cell testing;
- it does not prove that alpha-globin burden improves in beta-thalassemia.

## Metabolism And Safety Caution

The PF-06409577 PubMed snapshot also recovers PMID `30194276`, a UGT1A1
glucuronidation source. That does not block lab assay use, but it keeps the
patient-treatment boundary strict.

Do not frame PF-06409577 as a self-use candidate, supplement, or off-label
shortcut.

## Quote Addendum

If a qualified lab can add this lane, ask for:

- exact PF-06409577 or explicitly agreed `AMPKB1`-selective analog identity;
- certificate of analysis, purity, lot, storage, solvent, vehicle, and dose
  range;
- vehicle control and known HbF comparator;
- `HBG1` / `HBG2` messenger RNA;
- HbF protein and F-cell percentage;
- `NRF2` target context;
- `ULK1` or phospho-`ULK1`;
- p62 / `SQSTM1`;
- alpha/non-alpha globin balance;
- free or insoluble alpha-globin;
- erythroid maturation;
- viability and apoptosis;
- mature red-cell hemolysis.

## Reject Or Hold Conditions

Reject or hold the lane if:

- the lab can offer only metformin, generic AMPK activation, or generic
  antioxidant / `NRF2` framing;
- the material lacks identity, certificate of analysis, purity, lot, or storage
  documentation;
- the model is K562-only or reporter-only;
- alpha-globin burden, autophagy context, maturation, viability, or hemolysis
  is missing;
- the work is framed as patient treatment instead of preclinical assay biology.

## Research Decision

Add PF-06409577 as a quote addendum for the `AMPKB1` / `NRF2` / `ULK1`
expansion lane, behind the fixed first panel.

Decision label: `quote_addendum_ready_as_research_probe`.

Boundary label: `not_patient_candidate_not_treatment_advice`.

## Sources

- [PF-06409577 probe material gate notebook](../notebooks/2026-04-27-pf-06409577-probe-material-gate.ipynb)
- [PF-06409577 PubChem properties snapshot](../../../data/chemistry/pubchem/ampk-probes/2026-04-27-pf-06409577-properties.json)
- [PF-06409577 PubChem description snapshot](../../../data/chemistry/pubchem/ampk-probes/2026-04-27-pf-06409577-description.json)
- [PF-06409577 ChEMBL search snapshot](../../../data/chemistry/chembl/ampk-probes/2026-04-27-pf-06409577-search.json)
- [PF-06409577 ChEMBL activities snapshot](../../../data/chemistry/chembl/ampk-probes/2026-04-27-pf-06409577-chembl-activities.json)
- [PF-06409577 AMPK beta1 PubMed snapshot](../../../data/literature/pubmed/2026-04-27-pf-06409577-ampk-beta1-search.json)
- [AMPKB1 NRF2 ULK1 HbF refresh snapshot](../../../data/literature/pubmed/2026-04-27-expansion-ampkb1-nrf2-ulk1-hbf.json)
- [Selective AMPKB1 HbF article, PMID 41259521](https://pubmed.ncbi.nlm.nih.gov/41259521/)
- [PF-06409577 UGT1A1 article, PMID 30194276](https://pubmed.ncbi.nlm.nih.gov/30194276/)
