# Assay Plan: Epigenetic HbF Screen V0

Date checked: 2026-04-27
Status: experiment design note, not an unsupervised wet-lab protocol

## Goal

Build a testable path for candidates that may reactivate fetal hemoglobin
through `MBD2-NuRD`, `LSD1/KDM1A`, `DNMT1`, `NRF2/BACH1`, or related
chromatin/stress-response biology.

This plan is for qualified lab partners. It is not a patient treatment plan.

## Candidate Intake

Each candidate must be identified before testing:

- exact compound, fraction, or extract name;
- `CID`, `ChEMBL ID`, or equivalent identity record when available;
- source, supplier, and batch;
- purity or standardization marker;
- solvent and storage condition;
- expected mechanism lane;
- safety reason to exclude early.

Unstandardized mixtures should not be compared against purified drugs.

## Screen Gates

| Gate | Pass question | Minimum endpoint |
| --- | --- | --- |
| 1. Identity | Do we know what is being tested? | batch record, concentration, storage |
| 2. Reporter | Does the candidate raise fetal globin signal? | `HBG1/HBG2` reporter or gamma-globin mRNA |
| 3. Erythroid validation | Does the signal survive in erythroid maturation? | HbF protein, F-cells, `CD71`/`CD235a` profile |
| 4. Disease relevance | Does it matter in beta-thalassemia-like biology? | globin balance or beta-thalassemia/HbE cells |
| 5. Red-cell safety | Does it damage mature red cells? | hemolysis below rejection threshold |
| 6. General safety | Does it broadly hurt cells? | viability, apoptosis, stress markers |
| 7. Translation review | Could it ever be affordable and monitorable? | dose, route, monitoring, access note |

## Benchmark Controls

Use controls to prevent self-deception:

- positive HbF comparator: hydroxyurea or another lab-accepted HbF inducer;
- high-caution epigenetic comparator: decitabine or an approved reference only
  under qualified supervision;
- repurposing comparator: sirolimus only when the assay question includes
  mTOR/autophagy or gamma-globin pilot-trial context;
- natural-product-adjacent comparator: curcumin or a defined curcuminoid
  analog only when chemistry identity and dose-response are traceable;
- negative control: vehicle;
- safety reject comparator: known hemolytic or cytotoxic condition.

## Rejection Rules

Reject or hold a candidate if any of these occur:

- HbF signal appears only at toxic concentrations;
- erythroid maturation is blocked;
- mature red-cell hemolysis increases;
- signal cannot be repeated across batches;
- material identity is vague;
- plausible patient route would be unaffordable or unsafe;
- immune or allergy risk is uncontrolled.

## Candidate Classes To Enter First

| Lane | Entry condition |
| --- | --- |
| `MBD2-NuRD` | only if there is a plausible interaction-disruption or chromatin-target rationale |
| `LSD1/KDM1A` | prioritize reversible or non-covalent approaches over irreversible inhibitors |
| `DNMT1` | treat as proof-of-biology and safety boundary, not a casual candidate |
| `NRF2/BACH1` | require HbF endpoint plus viability, not just antioxidant activity |
| curcuminoid/trienone analogs | require defined chemistry and beta-thalassemia/HbE endpoint replication |
| bee-derived materials | require batch identity, allergy screen plan, and hemolysis-first triage |

## Output Per Run

Every completed run should produce:

- a filled assay-run note using `templates/assay-run-template.md`;
- raw data location;
- endpoint summary;
- pass/hold/reject decision;
- source and batch trace;
- next experiment or stop reason.

## Sources

- [Epigenetic HbF target drilldown](../findings/2026-04-27-epigenetic-hbf-target-drilldown.md)
- [Chemistry identity benchmark map](../findings/2026-04-27-chemistry-identity-benchmark-map.md)
- [Assay-ready HbF screen](../findings/2026-04-26-assay-ready-hbf-screen.md)
- [Assay funnel for cure discovery](../findings/2026-04-26-assay-funnel-for-cure-discovery.md)
- [Endogenous HbF reporter system, PubMed PMID 39108322](https://pubmed.ncbi.nlm.nih.gov/39108322/)
- [Small molecule HbF screen, PubMed PMID 39504332](https://pubmed.ncbi.nlm.nih.gov/39504332/)
- [Hemolysis assay optimization, PubMed PMID 36769243](https://pubmed.ncbi.nlm.nih.gov/36769243/)
