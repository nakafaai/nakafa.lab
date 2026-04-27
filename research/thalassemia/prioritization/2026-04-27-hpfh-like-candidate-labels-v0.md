# HPFH-Like Candidate Labels V0

Date: 2026-04-27
Scope: research triage labels, not treatment advice

## Purpose

This file applies [HPFH-like signature V0](2026-04-27-hpfh-like-signature-v0.md)
to the current candidate map. It is meant to make the repo easier to read:
each lane gets one current label and one reason.

## Label Map

| Candidate or lane | HPFH-like label | Current use |
| --- | --- | --- |
| Exa-cel / BCL11A enhancer editing | `hpfh_like` | clinical cure-like HbF benchmark, not affordable route yet |
| HPFH-like `HBG` promoter editing | `hpfh_like` | natural and genome-editing positive-control biology |
| Hydroxyurea | `partial_hbf` | best low-cost clinical HbF comparator; response is heterogeneous |
| Sirolimus | `partial_hbf` | repurposing signal; immune and monitoring boundaries remain |
| `AMPKB1` / `ULK1` / `NRF2` / autophagy bridge | `partial_hbf` | target-discovery lane linking HbF induction and alpha-globin cleanup; needs beta-thalassemia primary-cell validation |
| Alpha-globin rebalancing / `HBA` reduction | `not_hbf_lane` | root-cause-adjacent chain-balance benchmark; advanced RNA/vector/HSC/editing delivery, not a first affordable lead |
| Thalidomide / CRBN class | `blocked` | strong HbF/transfusion signal but safety boundary is too hard for promotion |
| Decitabine / DNMT1 depletion | `blocked` | strong HbF biology but cytotoxic and marrow-safety boundary is high |
| `MBD2-NuRD`, `LSD1`, HDAC target discovery | `partial_hbf` | assay-design lane, not direct treatment lead |
| `T-BDMC` trienone analog | `partial_hbf` | best natural-product-adjacent HbF seed, still needs hemolysis and batch gates |
| Resveratrol | `partial_hbf` | beta-thalassemia erythroid precursor HbF signal, needs repeat safety ladder |
| `HHBDMC` reduced curcuminoid analog | `partial_hbf` | primary erythroid HbF signal, but identity is unresolved |
| `Isocoronarin D` / `Curcuma comosa` | `reporter_only` | K562 reporter signal until endogenous or primary validation exists |
| Quercetin analogs | `reporter_only` | DOI-confirmed HbF title, but current extracted signal is reporter-stage |
| Angelicin / bergapten / TMA / citropten | `blocked` | HbF-adjacent furanocoumarin signal with phototoxicity or DNA-damage concern |
| Hepcidin-ferroportin-`TMPRSS6` axis | `not_hbf_lane` | disease-biology iron comparator, not HbF reactivation |
| EGCG / green-tea extract | `not_hbf_lane` | clinical adjunct comparator, not HbF or cure lane |
| Ginger / 6-shogaol-rich extract | `not_hbf_lane` | red-cell support and hemolysis lane, not HbF lane |
| Propolis | `not_hbf_lane` | oxidative-stress support hypothesis only |
| Royal jelly | `not_hbf_lane` | oxidative/inflammation support hypothesis only |
| Quercetin supplement lane | `not_hbf_lane` | adjunct iron/liver/inflammation biology, not HbF reactivation |
| Nigella sativa / manuka adjunct lane | `not_hbf_lane` | iron-overload adjunct hypothesis, not HbF reactivation |
| Melittin / bee venom | `blocked` | hemolysis and allergy hazard boundary |

## Current Read

The only true `hpfh_like` lanes are gene-editing or natural-genetic
benchmarks. That is expected. The affordable search has not yet found a
validated small molecule that reaches this label.

The best practical discovery candidates are therefore `partial_hbf` lanes that
can be tested against the HPFH-like signature:

- hydroxyurea as the low-cost clinical comparator;
- sirolimus as a monitored repurposing comparator;
- `AMPKB1` / `ULK1` / `NRF2` / autophagy as a dual HbF and alpha-globin
  cleanup target-discovery bridge;
- epigenetic target lanes as assay controls;
- `T-BDMC`, resveratrol, and `HHBDMC` as natural-product-adjacent HbF seeds.

Everything labeled `not_hbf_lane` can still matter, but it should not be sold
as a cure-mimic HbF route. It belongs in red-cell support, iron axis, platelet,
oxidative-stress, chain-balance, or adjunct biology until stronger evidence
appears.

Alpha-globin rebalancing is the exception that is not HbF but still directly
disease-relevant. It belongs beside the dual-readout assay as a chain-balance
benchmark because HBA copy-number and reduction evidence supports the biology,
while delivery and over-suppression risk block a first affordable lead.

## Immediate Decision Rule

Before adding a new candidate to the top ranking, assign one of these labels.

If the label is:

- `hpfh_like`: compare to gene-editing benchmark and ask why access or safety
  still blocks it;
- `partial_hbf`: design the missing HbF, F-cell, maturation, and hemolysis
  tests;
- `stress_hbf`: reject unless toxicity can be separated from HbF induction;
- `reporter_only`: require HUDEP2, primary erythroid, or disease-cell
  validation;
- `not_hbf_lane`: keep it out of cure-mimic ranking;
- `blocked`: do not promote without a new safety or identity resolution.

## Linked Evidence

- [HPFH-like signature V0](2026-04-27-hpfh-like-signature-v0.md)
- [Candidate scoring V0](2026-04-27-candidate-scoring-v0.md)
- [Candidate ranking](2026-04-26-candidate-ranking.md)
- [Natural-product HbF expansion map](../findings/2026-04-27-natural-product-hbf-expansion-map.md)
- [BCL11A HbF switch mimic boundary](../findings/2026-04-27-bcl11a-hbf-switch-mimic-boundary.md)
- [HPFH natural HbF blueprint](../findings/2026-04-27-hpfh-natural-hbf-blueprint.md)
- [AMPKB1 autophagy HbF bridge](../findings/2026-04-27-ampkb1-autophagy-hbf-bridge.md)
- [Alpha-globin rebalancing gate](../findings/2026-04-27-alpha-globin-rebalancing-gate.md)
