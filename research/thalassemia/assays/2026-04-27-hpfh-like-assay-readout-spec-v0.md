# Assay Spec: HPFH-Like Readouts V0

Date checked: 2026-04-27
Status: qualified-lab readout specification, not a patient treatment plan

## Purpose

This spec turns the HPFH-like signature into measurable lab outputs.

The key rule is simple: do not accept "HbF went up" as enough. A useful
candidate should show HbF in the right cells, preserve erythroid maturation,
improve or at least not worsen globin-chain imbalance, and avoid mature red-cell
damage.

## Minimum Readout Set

| Readout | Preferred method | Why it matters |
| --- | --- | --- |
| `HBG1/HBG2` messenger RNA | qPCR or RNA-seq in erythroid cells | earliest gamma-globin activation signal |
| HbF protein | HPLC, intracellular flow, immunoassay, or endogenous reporter | confirms transcript-to-protein translation |
| F-cell percentage | intracellular HbF flow cytometry | separates broad HPFH-like distribution from sparse-cell signal |
| HbF per F-cell | quantitative flow where feasible | distinguishes more F-cells from more HbF inside the same cells |
| erythroid maturation | flow markers such as `CD71`, `CD235a`, Band3, CD49d, and enucleation where available | blocks false positives caused by differentiation arrest |
| alpha/non-alpha globin balance | globin-chain electrophoresis, HPLC, mass spectrometry, or lab-equivalent validated method | beta-thalassemia damage is driven by globin-chain imbalance |
| viability and apoptosis | viability dye and apoptosis assay | blocks stress-driven HbF signals |
| mature red-cell hemolysis | hemolysis or membrane-damage assay | blocks candidates that damage RBCs |

## Evidence Anchors

| Source signal | Assay lesson |
| --- | --- |
| PMID `15163316` | Flow cytometry can measure HbF-containing RBCs, reticulocytes, and normoblasts in beta-thalassemia; increased HbF can reflect more F-cells rather than more HbF per cell. |
| PMID `12779269` | Hydroxyurea culture assays can measure HbF response in beta-thalassemia erythroid precursors, but cell number and maturation effects must be watched. |
| PMID `25183077` | Hydroxyurea-associated benefit may involve improved alpha/non-alpha and gamma-globin chain ratios, not HbF percentage alone. |
| PMID `8562958` | Beta-thalassemia/HbE hydroxyurea studies measured HbF, reticulocytes, globin biosynthesis ratios, and ineffective erythropoiesis signals together. |
| PMID `39108322` | Endogenous fetal-hemoglobin reporter systems are useful for compound screening when they measure the native `HBG` locus. |
| PMID `39504332` | HUDEP2 endogenous `HBG1` reporter screening should be followed by primary erythroid validation before therapeutic interpretation. |
| PMID `23861885` | A synthetic CD34+ beta-thalassemia erythropoiesis model can connect globin imbalance, HPLC hemoglobin fractions, and terminal erythroid differentiation. |
| PMID `31698466` | HBG1/HBG2 promoter editing studies measure HbF induction alongside erythroid progenitor output and safety readouts. |
| PMID `27525524` | Recapitulating benign HPFH-like promoter biology is a valid positive-control concept for beta-hemoglobinopathy research. |

## Pass, Hold, Reject

Pass to deeper testing only if:

- `HBG1/HBG2` or HbF protein increases reproducibly;
- F-cell percentage or distribution supports broad erythroid rescue;
- erythroid maturation is preserved;
- alpha/non-alpha balance improves or does not worsen;
- viability and apoptosis do not indicate toxic stress;
- mature red-cell hemolysis does not increase.

Hold if:

- only `HBG1/HBG2` messenger RNA is available;
- HbF protein rises but F-cell distribution is missing;
- the model is K562-only or artificial reporter-only;
- maturation markers are missing;
- globin-chain balance is not measured.

Reject if:

- HbF rises only while viability falls;
- erythroid maturation stalls;
- hemolysis increases;
- the candidate is a mixture without identity or batch control;
- the mechanism is generic antioxidant or anti-inflammatory language without
  any HbF, globin-balance, or erythroid endpoint.

## Lab Output Table

Every candidate should return this compact table:

```text
candidate:
identity_or_batch:
model:
concentration_range:
vehicle:
HBG1:
HBG2:
HbF_protein:
F_cell_percentage:
HbF_per_F_cell:
alpha_non_alpha_balance:
erythroid_maturation:
viability:
apoptosis:
mature_rbc_hemolysis:
assay_interference:
hpfh_like_label:
proximity_novelty_label:
closest_editing_benchmark:
closest_non_editing_benchmark:
claimed_gap:
decision:
reason:
raw_data_location:
```

Use the [assay run template](../../../templates/assay-run-template.md) when a
partner returns candidate data, so each run records identity, controls, missing
readouts, and a `promote`, `hold`, or `reject` decision against the same gates.

## Query Boundaries

Several first-pass searches for combined `HBG1/HBG2`, `CD71`, `CD235a`, and
HPFH-like terms returned zero PubMed records. Those zero snapshots are retained
as query-boundary records. The positive evidence came from more focused
F-cell-flow, globin-chain-ratio, endogenous-reporter, and HBG editing sources.

## Sources

- [F-cell flow readout PubMed snapshot](../../../data/literature/pubmed/2026-04-27-hpfh-like-fcell-flow-readouts.json)
- [Globin-chain balance PubMed snapshot](../../../data/literature/pubmed/2026-04-27-hpfh-like-globin-chain-balance.json)
- [Erythroid differentiation marker PubMed snapshot](../../../data/literature/pubmed/2026-04-27-hpfh-like-erythroid-differentiation-markers.json)
- [HBG1/HBG2 editing title PubMed snapshot](../../../data/literature/pubmed/2026-04-27-hpfh-like-hbg1-hbg2-editing-title.json)
- [Endogenous reporter and assay selected abstracts](../../../data/literature/pubmed/2026-04-27-hpfh-like-assay-readouts-selected-abstracts.xml)
- [Over-constrained maturation readout snapshot](../../../data/literature/pubmed/2026-04-27-hpfh-like-erythroid-maturation-readouts.json)
- [Over-constrained HBG editing assay snapshot](../../../data/literature/pubmed/2026-04-27-hpfh-like-hbg-editing-assay-readouts.json)
- [Over-constrained HBG broad maturation snapshot](../../../data/literature/pubmed/2026-04-27-hpfh-like-erythroid-maturation-hbg-broad.json)
- [Over-constrained HUDEP2 reporter readout snapshot](../../../data/literature/pubmed/2026-04-27-hpfh-like-hudep2-hbf-reporter-readouts.json)
- [HPFH-like signature V0](../prioritization/2026-04-27-hpfh-like-signature-v0.md)
- [Proximity novelty gate V0](../prioritization/2026-04-28-proximity-novelty-gate-v0.md)
- [Assay run template](../../../templates/assay-run-template.md)
