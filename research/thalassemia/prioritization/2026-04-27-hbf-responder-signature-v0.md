# HbF Responder Signature V0

Date: 2026-04-27
Scope: research data model, not a clinical prediction tool

## Purpose

This table defines the minimum variables needed before Nakafa Lab interprets an
HbF-inducing candidate. It is inspired by hydroxyurea response heterogeneity and
the need to avoid generic "works for thalassemia" claims.

## Required Variables

| Variable | Why it matters | Status for case-001 |
| --- | --- | --- |
| Clinical class: `TDT` or `NTDT` | response evidence and endpoints differ | unknown |
| Exact subtype: beta, alpha, HbE/beta, mixed | genotype can change HbF biology and response | unknown |
| `HBB` genotype | defines beta-globin production defect | unknown |
| `HBA` genotype | rules in or out alpha-thalassemia contribution | unknown |
| Hb fractions: HbA, HbA2, HbF, HbE | baseline phenotype and HbF reserve | unknown |
| XmnI-HBG2 | hydroxyurea/HbF response modifier signal | unknown |
| `BCL11A` modifier status | HbF silencing and response context | unknown |
| `HBS1L-MYB` modifier status | HbF modifier context | unknown |
| Baseline pre-transfusion Hb | severity and endpoint baseline | unknown |
| Transfusion interval and units | burden endpoint | weekly reported |
| Spleen status | hypersplenism can increase transfusion need | unknown |
| Antibody/DAT status | immune red-cell loss can mimic non-response | unknown |
| Ferritin and MRI iron | safety and disease burden context | unknown |
| Chelation drug and dose | interaction and toxicity context | unknown |
| Autoimmune diagnosis | safety and eligibility context | reported but unspecified |

## Candidate Interpretation Rule

Do not promote an HbF candidate unless the note states which responder variables
are known, unknown, or irrelevant.

Use these labels:

- `matched`: evidence source resembles the target subtype and endpoint;
- `partial`: some biology matches, but genotype or phenotype differs;
- `unmatched`: evidence comes from a different disease, cell line, or endpoint;
- `blocked`: safety, identity, immune, or hemolysis risk blocks promotion.

## First Application

| Candidate lane | Current responder fit | Reason |
| --- | --- | --- |
| Hydroxyurea | partial | human evidence exists, but case genotype, HbF, XmnI, and spleen status are unknown |
| Sirolimus | partial | small selected beta-thalassemia cohort; immune issue in case-001 is unresolved |
| Thalidomide class | blocked | effect signal exists, but safety gate is too hard for patient-facing relevance |
| Curcuminoid analog HbF | unmatched | direct HbF biology exists, but mostly assay-stage and chemistry-gated |
| Exa-cel | matched biologically, blocked by access | validates HbF reactivation but requires cell-therapy infrastructure |
| Beti-cel | matched biologically, blocked by access | validates stem-cell gene addition but depends on genotype and access |

## Data Capture Form

Use this compact form when new records arrive:

```text
case_id:
date_checked:
clinical_class:
subtype:
HBB:
HBA:
HbA:
HbA2:
HbF:
HbE:
XmnI_HBG2:
BCL11A_modifier:
HBS1L_MYB_modifier:
pre_transfusion_Hb:
transfusion_interval:
units_or_volume:
spleen_status:
antibody_screen:
DAT:
ferritin:
liver_iron_MRI:
cardiac_T2_star:
chelation:
autoimmune_diagnosis:
current_interpretation:
```

## Linked Evidence

- [Hydroxyurea response predictor map](../findings/2026-04-27-hydroxyurea-response-predictor-map.md)
- [Indonesia genotype-first rule](../findings/2026-04-27-indonesia-genotype-first-rule.md)
- [Top clinical lanes numeric extraction](../findings/2026-04-27-top-clinical-lanes-numeric-extraction.md)
- [Hematologist question sheet](../case-context/hematologist-question-sheet-case-001.md)
