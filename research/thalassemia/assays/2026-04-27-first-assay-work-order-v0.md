# Assay Work Order: First HbF And Red-Cell Safety Panel V0

Date checked: 2026-04-27
Status: qualified-lab work order draft, not a patient treatment plan

## Purpose

Turn the current research map into the smallest useful experiment batch.

The first assay should not try to prove a cure. It should answer whether the
research system can distinguish:

- a known HbF-positive comparator;
- early natural-product-adjacent HbF seeds;
- red-cell-support candidates without HbF proof;
- hazard-first materials that should stop before patient-facing claims.

## Required Lab Setting

Run only with a qualified lab partner that can document:

- compound or extract identity and batch;
- vehicle and concentration range;
- endogenous `HBG1/HBG2`, HbF protein, or F-cell endpoint;
- erythroid viability and maturation;
- mature red-cell hemolysis or membrane-damage endpoint;
- raw data export and pass/hold/reject decision.

No patient sample should be used unless ethics approval, consent, sample
handling, and clinician oversight are already in place.

## Minimal Panel

| Role | Candidate | Why included | First decision |
| --- | --- | --- | --- |
| Positive HbF comparator | hydroxyurea | affordable clinical HbF benchmark | confirms the assay can detect an HbF-positive signal |
| Legacy HbF comparator | sodium butyrate or arginine butyrate | historical beta-globin disorder HbF proof-of-biology | calibrates HbF response without treating it as practical therapy |
| High-caution epigenetic comparator | decitabine or lab-approved reference | `DNMT1` proof-of-biology and toxicity boundary | verifies strong HbF signal can be separated from toxicity |
| Repurposing seed | sirolimus | small human beta-thalassemia gamma-globin signal | checks mTOR/autophagy lane under monitored lab conditions |
| Red-cell metabolism benchmark | mitapivat or lab-approved pyruvate kinase activator reference, only if legally and practically available to the lab | validates red-cell energy, hemolysis, and survival readouts | keeps metabolism support separate from HbF cure claims |
| Natural-product-adjacent HbF seed | `T-BDMC`, only with identity proof | strongest current curcuminoid analog bridge | test HbF plus hemolysis before disease-cell escalation |
| Natural-product HbF seed | resveratrol, purified compound only | reported HbF signal in beta-thalassemia erythroid precursors | repeat endogenous HbF and red-cell safety |
| Red-cell support comparator | standardized 6-shogaol-rich ginger extract | thalassemia RBC anti-hemolysis support signal, not HbF proof | check support endpoint without promoting as cure |
| Bee-derived hazard boundary | melittin or bee venom only as lab-chosen hazard control | known hemolysis/allergy concern | calibrate rejection threshold, not efficacy |

Do not include broad honey, propolis, royal jelly, or unstandardized black-seed
products in the first HbF panel unless identity and standardization are solved.

## First Quote Panel

The first computational panel optimizer selected a smaller five-item lab quote
package:

- hydroxyurea;
- purified resveratrol;
- sirolimus;
- standardized 6-shogaol-rich ginger extract;
- melittin hazard control.

This is a quote package, not a final scientific panel. Add `T-BDMC`-like
curcuminoid analog and a pyruvate kinase activator reference if the lab can
resolve compound identity, legal access, and budget.

## Required Outputs

Each run should return one table with:

- candidate and batch;
- concentration range;
- vehicle;
- HbF or `HBG1/HBG2` endpoint;
- erythroid maturation endpoint;
- viability endpoint;
- mature red-cell hemolysis endpoint;
- observed assay interference;
- pass, hold, or reject call;
- reason for the decision.

Use the [HPFH-like assay readout spec V0](2026-04-27-hpfh-like-assay-readout-spec-v0.md)
when a candidate claims HbF reactivation or HPFH-like biology.

Use the
[red-cell metabolism readout spec V0](2026-04-27-red-cell-metabolism-readout-spec-v0.md)
when a candidate claims red-cell survival, hemolysis reduction, membrane
protection, pyruvate kinase biology, or iron-axis support without direct HbF
reactivation.

Use the
[dual HbF and alpha-globin autophagy assay spec V0](2026-04-27-dual-hbf-alpha-autophagy-assay-spec-v0.md)
when a candidate claims both HbF rescue and alpha-globin cleanup, `ULK1`,
`AMBRA1`, p62/`SQSTM1`, `PRKAB1` / AMPK beta1, `NRF2`, or autophagy biology.

## PF-06409577 Expansion Add-On

PF-06409577 is not part of the fixed first quote panel. Add it only if the lab
can support the
[PF-06409577 PRKAB1 quote addendum](2026-04-27-pf-06409577-prkab1-quote-addendum-v0.md)
with exact material identity, certificate of analysis, purity, lot, storage,
solvent, vehicle, dose range, and the full dual HbF plus
alpha-globin/autophagy safety readout set.

Treat this add-on as assay-probe biology only. It is not a patient candidate,
supplement candidate, or treatment recommendation.

## BCL11A/HbF Signature Add-On

For candidates that raise HbF or `HBG1/HBG2`, add a mechanism table when the
lab can do it:

- `BCL11A` messenger RNA or protein;
- `HBG1/HBG2` messenger RNA;
- HbF protein or F-cell percentage;
- erythroid maturation markers such as `CD71` and `CD235a`;
- viability and apoptosis;
- mature red-cell hemolysis.

Use BCL11A knockdown/editing only as lab-controlled biology, not as a patient
treatment proposal. CRBN/IMiD comparators such as pomalidomide or avadomide are
high-caution mechanism comparators and should not be promoted as affordable
leads without disease-specific safety review.

## HPFH-Like Signature Add-On

For candidates that pass the HbF and safety gates, compare the signal against an
`HPFH-like` reference state when the lab can support it:

- `HBG1/HBG2` promoter-linked gamma-globin activation;
- F-cell percentage or HbF distribution, not only total HbF;
- `BCL11A`, `ZBTB7A`, `KLF1`, `GATA1`, and `NF-Y` pathway context where
  feasible;
- erythroid maturation markers such as `CD71` and `CD235a`;
- viability, apoptosis, and mature red-cell hemolysis.

This keeps HPFH biology as a positive-control target phenotype. It does not
turn HBG promoter editing into a patient-facing recommendation.

## Promotion Rules

Promote only if:

- HbF signal is reproducible;
- erythroid maturation is preserved;
- mature red-cell hemolysis does not increase;
- the active material is identifiable and batch-repeatable;
- the plausible clinical route can be reviewed by a hematologist.

Hold if:

- the signal is K562-only;
- the compound identity is not exact;
- the effect appears only near toxic concentrations;
- the candidate is a mixture without standardization markers.

Reject if:

- mature red-cell hemolysis increases;
- erythroid maturation collapses;
- product identity is unclear after one resolution attempt;
- the candidate is hazard-first and no safer derivative or control use exists.

## Interpretation

The first successful outcome is not a cure claim. The first successful outcome
is a trustworthy assay ladder that can reject weak ideas quickly and preserve
the few candidates that deserve deeper testing.

## Sources

- [Epigenetic HbF screen V0](2026-04-27-epigenetic-hbf-screen-v0.md)
- [Lab partner requirements](2026-04-27-lab-partner-requirements.md)
- [HPFH-like assay readout spec V0](2026-04-27-hpfh-like-assay-readout-spec-v0.md)
- [Red-cell metabolism readout spec V0](2026-04-27-red-cell-metabolism-readout-spec-v0.md)
- [Dual HbF and alpha-globin autophagy assay spec V0](2026-04-27-dual-hbf-alpha-autophagy-assay-spec-v0.md)
- [PF-06409577 PRKAB1 quote addendum](2026-04-27-pf-06409577-prkab1-quote-addendum-v0.md)
- [Natural-product HbF expansion map](../findings/2026-04-27-natural-product-hbf-expansion-map.md)
- [Pyruvate kinase red-cell metabolism benchmark](../findings/2026-04-27-pyruvate-kinase-red-cell-metabolism-benchmark.md)
- [T-BDMC identity resolution](../findings/2026-04-27-t-bdmc-identity-resolution.md)
- [Resveratrol HbF beta-thalassemia seed](../findings/2026-04-27-resveratrol-hbf-beta-thalassemia-seed.md)
- [Ginger shogaol red-cell support map](../findings/2026-04-27-ginger-shogaol-red-cell-support-map.md)
- [Melittin bee-venom hazard deep dive](../findings/2026-04-27-melittin-bee-venom-hazard-deep-dive.md)
- [Immune transfusion risk extraction](../findings/2026-04-27-immune-transfusion-risk-extraction.md)
- [BCL11A HbF switch mimic boundary](../findings/2026-04-27-bcl11a-hbf-switch-mimic-boundary.md)
- [HPFH natural HbF blueprint](../findings/2026-04-27-hpfh-natural-hbf-blueprint.md)
