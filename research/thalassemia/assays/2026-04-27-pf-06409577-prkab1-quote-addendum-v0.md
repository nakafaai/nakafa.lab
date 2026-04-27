# Assay Addendum: PF-06409577 PRKAB1 Quote V0

Date checked: 2026-04-27
Status: qualified-lab quote addendum, not a patient treatment plan

## Purpose

Use this addendum only if a qualified lab can extend the first quote panel
without weakening the core HbF, alpha-globin/autophagy, maturation, viability,
and hemolysis gates.

The addendum asks whether exact PF-06409577 material can be used as a
`PRKAB1` / AMPK beta1 research probe. It must not be framed as self-use,
supplement use, off-label prescribing, or patient treatment.

## Send Boundary

Send only public research context and de-identified project context. Do not send
names, exact birth dates, hospital identifiers, raw clinical records,
prescriptions, screenshots, lab reports, or family notes.

Ask for feasibility, pricing, methods, and raw-data export. Do not ask the lab
to validate a therapy claim.

## Material Identity

| Field | Required value |
| --- | --- |
| Candidate | PF-06409577 |
| Target lane | `PRKAB1` / AMPK beta1 / `NRF2` / `ULK1` |
| PubChem CID | `71748255` |
| ChEMBL ID | `CHEMBL3891221` |
| Formula | `C19H16ClNO3` |
| InChIKey | `FHQXLWCFSUSXBF-UHFFFAOYSA-N` |
| Role | Exact-material AMPK beta1-biased assay probe |

If the lab proposes a substitute, require an explicit written mapping to
`PRKAB1` / AMPK beta1 biology, source identity, certificate of analysis,
purity, lot, storage, solvent, vehicle, and dose range before it enters the
assay plan.

## Feasibility Questions

Ask the lab:

- Can you source exact PF-06409577 with certificate of analysis, purity, lot,
  storage, solvent, vehicle, and dose range?
- Can you run a beta-thalassemia/HbE, beta-thalassemia, or CD34+ erythroid
  model rather than K562-only or reporter-only screening?
- Can you measure `HBG1` / `HBG2`, HbF protein, and F-cell percentage?
- Can you measure alpha/non-alpha globin balance and free or insoluble
  alpha-globin?
- Can you measure `PRKAB1` or AMPK beta1 context if available, while clearly
  separating that from generic AMPK-alpha phosphorylation?
- Can you measure `NRF2` target context, `ULK1` or phospho-`ULK1`, p62 /
  `SQSTM1`, and a flux-aware autophagy context if possible?
- Can you measure erythroid maturation markers such as `CD71`, `CD235a`,
  Band3, CD49d, or enucleation?
- Can you measure viability, apoptosis, and mature red-cell hemolysis or
  membrane damage?
- Can you return raw data plus per-readout and per-candidate pricing?

## Required Output Table

```text
candidate: PF-06409577
target_lane: PRKAB1 / AMPK beta1 / NRF2 / ULK1
source_identity:
supplier:
catalog_or_custom_synthesis:
certificate_of_analysis:
purity:
lot:
storage:
solvent:
vehicle:
model:
dose_range:
replicates:
HBG1:
HBG2:
HbF_protein:
F_cell_percentage:
PRKAB1_or_AMPK_beta1_context_optional:
NRF2_target_context:
ULK1_or_phospho_ULK1:
p62_SQSTM1:
autophagy_flux_context:
alpha_non_alpha_balance:
free_or_insoluble_alpha_globin:
erythroid_maturation:
viability:
apoptosis:
mature_rbc_hemolysis:
assay_interference:
decision:
reason:
raw_data_location:
```

## Pass, Hold, Reject

Pass to deeper testing only if:

- exact material identity is documented;
- HbF or F-cell signal improves reproducibly;
- alpha/non-alpha balance improves or does not worsen;
- free or insoluble alpha-globin decreases, or a validated equivalent improves;
- `NRF2`, `ULK1`, p62 / `SQSTM1`, or flux context supports useful biology;
- erythroid maturation is preserved;
- viability and apoptosis do not suggest nonspecific stress;
- mature red-cell hemolysis does not increase.

Hold if:

- the lab can run only K562, reporter-only, or generic AMPK assays;
- certificate of analysis, lot, purity, storage, solvent, vehicle, or dose
  range is missing;
- HbF is measured without alpha-globin/autophagy context;
- autophagy is measured by one static marker without flux or time-course
  context;
- mature red-cell hemolysis is missing.

Reject if:

- material identity cannot be documented;
- the result is driven by toxicity, stress, or maturation collapse;
- mature red-cell hemolysis increases;
- free or insoluble alpha-globin increases;
- the lane is framed as patient treatment, supplement substitution, or off-label
  prescribing.

## Ethics Guardrail

Quran 16:43 is used here only as an expert-consultation guardrail: ask people
of knowledge when we do not know. In this repo, that means qualified
hematology, laboratory, ethics, and biosafety review. It is not biomedical
evidence that PF-06409577 treats thalassemia.

## Sources

- [PF-06409577 probe material gate](../findings/2026-04-27-pf-06409577-probe-material-gate.md)
- [PRKAB1 target nomenclature gate](../findings/2026-04-27-prkab1-target-nomenclature-gate.md)
- [Dual HbF and alpha-globin autophagy assay spec V0](2026-04-27-dual-hbf-alpha-autophagy-assay-spec-v0.md)
- [First lab quote brief V0](2026-04-27-first-lab-quote-brief-v0.md)
- [PF-06409577 PubChem properties snapshot](../../../data/chemistry/pubchem/ampk-probes/2026-04-27-pf-06409577-properties.json)
- [PF-06409577 ChEMBL activities snapshot](../../../data/chemistry/chembl/ampk-probes/2026-04-27-pf-06409577-chembl-activities.json)
- [PF-06409577 AMPK beta1 PubMed snapshot](../../../data/literature/pubmed/2026-04-27-pf-06409577-ampk-beta1-search.json)
- [NCBI Gene: PRKAB1, Gene ID 5564](https://www.ncbi.nlm.nih.gov/gene/5564)
- [Selective AMPKB1 HbF article, PMID 41259521](https://pubmed.ncbi.nlm.nih.gov/41259521/)
- [PF-06409577 UGT1A1 article, PMID 30194276](https://pubmed.ncbi.nlm.nih.gov/30194276/)
- [Quran 16:43 expert-consultation guardrail](../../islamic/quran/016-an-nahl/043.md)
