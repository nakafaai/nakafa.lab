# HPFH-Like Signature V0

Date: 2026-04-27
Scope: candidate triage signature, not a clinical prediction tool

## Purpose

This file converts the HPFH blueprint into a practical scoring signature.

The goal is to stop weak HbF claims early. A candidate should not move upward
just because it raises one fetal-hemoglobin marker. It should move upward only
when the total pattern looks closer to useful HPFH-like erythropoiesis than to
toxic stress, stalled differentiation, or reporter-only noise.

## Core Signature

| Marker or feature | Desired direction | Why it matters |
| --- | --- | --- |
| `HBG1` messenger RNA | up | direct gamma-globin response |
| `HBG2` messenger RNA | up | direct gamma-globin response |
| HbF protein | up | confirms transcript signal reaches protein |
| F-cell percentage or distribution | up or broader | HPFH is useful partly because HbF is present across more red cells |
| alpha/non-alpha globin balance | improved | beta-thalassemia damage comes from globin-chain imbalance |
| erythroid maturation markers | preserved | excludes false positives from blocked differentiation |
| mature red-cell hemolysis | not increased | excludes candidates that damage red cells |
| viability or apoptosis | preserved | excludes broad cytotoxic stress |

## Mechanism Context

These markers do not all need to move for every candidate, but they define the
interpretation frame:

| Mechanism node | Useful pattern | Caution pattern |
| --- | --- | --- |
| `BCL11A` | lower erythroid repression or bypassed repression with preserved maturation | broad systemic suppression claim |
| `ZBTB7A` / `LRF` | evidence of fetal-globin repressor relief | broad transcription-factor disruption |
| `KLF1` | activator-pattern support without erythroid collapse | impaired erythroid identity |
| `GATA1` | preserved erythroid program and promoter activation context | cytopenia-like or differentiation-failure signal |
| `NF-Y` | promoter activation context in HPFH-like variants | nonspecific stress response |

## Scoring Labels

Use these labels for every HbF candidate:

| Label | Meaning |
| --- | --- |
| `hpfh_like` | raises `HBG1/HBG2` and HbF while preserving maturation, viability, and red-cell safety |
| `partial_hbf` | raises one HbF marker but lacks protein, F-cell, disease-cell, or safety confirmation |
| `stress_hbf` | HbF rises with toxicity, apoptosis, differentiation block, or hemolysis |
| `reporter_only` | signal exists only in K562 or artificial reporter context |
| `not_hbf_lane` | candidate may support red cells or iron biology but does not belong in HbF promotion |
| `blocked` | identity, safety, immune, hemolysis, or clinical-risk issue blocks promotion |

## Minimum Candidate Record

```text
candidate:
batch_or_identity:
model:
HBG1:
HBG2:
HbF_protein:
F_cell_distribution:
BCL11A:
ZBTB7A_LRF:
KLF1:
GATA1:
NF_Y:
erythroid_maturation:
viability:
apoptosis:
mature_rbc_hemolysis:
alpha_non_alpha_balance:
label:
reason:
source:
```

## Promotion Rules

Promote to the next assay stage only when:

- `HBG1/HBG2` or HbF protein increases;
- maturation and viability are preserved;
- mature red-cell hemolysis is not increased;
- identity and batch are clear;
- the model is endogenous erythroid, disease-cell, or primary-cell relevant.

Hold when:

- HbF is transcript-only;
- F-cell distribution is missing;
- the model is K562-only;
- the candidate is a mixture without standardization;
- the mechanism cannot be separated from generic oxidative or inflammatory
  claims.

Reject or block when:

- hemolysis increases;
- erythroid maturation collapses;
- apoptosis or cytotoxicity explains the signal;
- a high-risk drug class is being promoted without clinician review;
- the source does not measure any thalassemia-relevant endpoint.

## Why This Helps The Cure Search

This signature makes the target falsifiable.

It does not say the future cure must edit `HBG` promoters. It says any
affordable candidate should be judged by whether it imitates the useful
consequence of HPFH: enough safe fetal hemoglobin in the right erythroid
context to reduce beta-globin imbalance.

## Linked Evidence

- [HPFH natural HbF blueprint](../findings/2026-04-27-hpfh-natural-hbf-blueprint.md)
- [BCL11A HbF switch mimic boundary](../findings/2026-04-27-bcl11a-hbf-switch-mimic-boundary.md)
- [HbF responder signature V0](2026-04-27-hbf-responder-signature-v0.md)
- [Epigenetic HbF screen V0](../assays/2026-04-27-epigenetic-hbf-screen-v0.md)
- [First HbF and red-cell safety assay work order V0](../assays/2026-04-27-first-assay-work-order-v0.md)
