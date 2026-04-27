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

## K562 Guardrail

K562 reporter data are an entry signal, not a promotion signal. A candidate
should not move toward therapy hypothesis status until the HbF signal survives
in an endogenous `HBG1/HBG2` or HbF protein readout, preferably in HUDEP2 or
primary erythroid cells.

For K562-only natural-product seeds, do not rank by fold-change alone across
different papers. Prioritize validation order by identity quality, model
relevance, viability, hemolysis risk, and disease-cell replication.

## Benchmark Controls

Use controls to prevent self-deception:

- positive HbF comparator: hydroxyurea or another lab-accepted HbF inducer;
- legacy HbF comparator: sodium butyrate or arginine butyrate only as a
  literature and assay benchmark, not an unsupervised treatment route;
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
| curcuminoid/trienone analogs | require defined chemistry, HbF endpoint, and beta-thalassemia/HbE endpoint replication |
| bee-derived materials | require batch identity, allergy screen plan, and hemolysis-first triage |

For curcuminoid analog work, `T-BDMC` is the first high-priority seed. Its
structure now resolves to PubChem `CID 10447050` and ChEMBL `CHEMBL469419`, but
it still needs a supplier or synthesis batch before testing.

## Natural-Product HbF Seed Queue

| Seed | Current status | First assay decision |
| --- | --- | --- |
| `T-BDMC` | chemistry-resolved as PubChem `CID 10447050` / ChEMBL `CHEMBL469419`; strongest current biology bridge; K562 plus beta-thalassemia/HbE primary-cell evidence; low-micromolar KB/Vero cytotoxicity boundary | obtain supplier/synthesis batch, confirm purity, and run hemolysis plus erythroid viability before disease-cell escalation |
| `HHBDMC` | PubMed PMID `23079892` reports human primary erythroid precursor gamma-globin mRNA and HbF induction, but exact chemistry identity is unresolved | hold procurement until paper structure, InChIKey, supplier certificate, or synthesis record is recovered |
| resveratrol | chemistry-resolved as PubChem `CID 445154` / ChEMBL `CHEMBL165`; PubMed PMID `22378234` reports HbF induction in beta-thalassemia patient erythroid precursors | use purified compound only; repeat endogenous HbF and hemolysis before ranking above trienone analogs |
| `isocoronarin D` | chemistry-resolved as `CHEMBL1099267` / PubChem `CID 46871816`; K562 reporter `FC 1.6` at `20 uM` | hemolysis and K562 repeat before disease-cell escalation |
| `3,4'-Di-O-methylquercetin` | chemistry-resolved as PubChem `CID 5380905` / `CHEMBL309263`; Springer abstract reports K562 reporter `2.6-fold` at `8 uM` | treat as quercetin analog, not quercetin supplement; repeat reporter and add endogenous HbF |
| angelicin / bergapten / exact TMA / citropten | chemistry-resolved furanocoumarin/coumarin probes; PubMed abstracts connect them to gamma-globin or HbF-adjacent induction | hazard-first mechanism probes only; require no-UVA handling, hemolysis, viability, genotoxicity, and phototoxicity review before promotion |

These seeds should be compared inside the same assay framework rather than as
separate anecdotes. The first meaningful decision is not "is this a cure?" but
"does this reproducibly raise HbF without damaging erythroid or mature red
cells?"

## HUDEP2 Benchmark Hit Queue

| Benchmark | Current use | Caution |
| --- | --- | --- |
| `avadomide` | mechanistic comparator for `BCL11A`/`IKZF`-adjacent HbF induction | thalidomide-class neighborhood; not an access shortcut |
| `autophinib` | VPS34/autophagy pathway probe | pathway toxicity and erythroid maturation risk must be checked |
| `triciribine` | AKT/DNA-synthesis inhibitor comparator | cytotoxicity and oncology-like mechanism caution |
| `R574` / probable `R547` | CDK1/2/4 inhibitor benchmark | use `R547` for chemistry lookup, but keep the source-label discrepancy visible |

These hits help validate the assay ladder. They should not displace affordable
candidate discovery unless they show a realistic safety and access path.

In Yang 2024, the primary `CD34+` validation lane was restricted to
`pomalidomide`, `avadomide`, and `idoxuridine`. Among the four novel hit names,
only `avadomide` clearly crossed that published primary-cell validation boundary.
Treat the other novel hits as pathway probes until independent primary-cell or
beta-thalassemia/HbE validation is found.

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
- [Curcuminoid HbF bridge deep dive](../findings/2026-04-27-curcuminoid-hbf-bridge-deep-dive.md)
- [Curcuminoid analog assay map](../findings/2026-04-27-curcuminoid-analog-assay-map.md)
- [HHBDMC identity conflict](../findings/2026-04-27-hhbdmc-identity-conflict.md)
- [T-BDMC identity resolution](../findings/2026-04-27-t-bdmc-identity-resolution.md)
- [T-BDMC cytotoxicity boundary](../findings/2026-04-27-t-bdmc-cytotoxicity-boundary.md)
- [Resveratrol HbF beta-thalassemia seed](../findings/2026-04-27-resveratrol-hbf-beta-thalassemia-seed.md)
- [Furanocoumarin HbF hazard map](../findings/2026-04-27-furanocoumarin-hbf-hazard-map.md)
- [Trimethylangelicin and citropten identity map](../findings/2026-04-27-trimethylangelicin-citropten-identity-map.md)
- [Isocoronarin D identity map](../findings/2026-04-27-isocoronarin-d-identity-map.md)
- [Quercetin analog HbF extraction](../findings/2026-04-27-quercetin-analog-hbf-extraction.md)
- [K562 to HUDEP2 validation guardrail](../findings/2026-04-27-k562-to-hudep2-validation-guardrail.md)
- [HUDEP2 small-molecule hit map](../findings/2026-04-27-hudep2-small-molecule-hit-map.md)
- [Butyrate HbF-inducer legacy map](../findings/2026-04-27-butyrate-hbf-inducer-legacy-map.md)
- [Assay-ready HbF screen](../findings/2026-04-26-assay-ready-hbf-screen.md)
- [Assay funnel for cure discovery](../findings/2026-04-26-assay-funnel-for-cure-discovery.md)
- [Endogenous HbF reporter system, PubMed PMID 39108322](https://pubmed.ncbi.nlm.nih.gov/39108322/)
- [Small molecule HbF screen, PubMed PMID 39504332](https://pubmed.ncbi.nlm.nih.gov/39504332/)
- [Hemolysis assay optimization, PubMed PMID 36769243](https://pubmed.ncbi.nlm.nih.gov/36769243/)
