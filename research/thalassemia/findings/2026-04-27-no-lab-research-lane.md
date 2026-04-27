# No-Lab Research Lane

Date: 2026-04-27
Status: dry-lab and clinician-facing research plan, not treatment advice

## Bottom Line

Without a lab partner, Nakafa Lab cannot prove a new thalassemia cure.

But we can still do high-value work:

- reduce clinical uncertainty for case review;
- identify existing therapy and trial eligibility gates;
- mine public literature, compound, trial, regulatory, and omics data;
- rank hypotheses by mechanism, safety, affordability, and access;
- prepare a small, disciplined wet-lab package for later, so the first lab
  conversation is not vague.

The no-lab goal is not to replace experiments. The goal is to make the first
real experiment smaller, cheaper, and more likely to answer the right question.

## What We Can Do Now

### 1. Build A Doctor-Ready Case Packet

This is the most immediately useful no-lab action for the family.

Collect or ask for:

- exact subtype: `TDT`, `NTDT`, HbE/beta, alpha, or mixed disease;
- `HBB` and `HBA` genotype if available;
- Hb fractions: HbA, HbA2, HbF, and HbE if present;
- transfusion dates, volume, units, and pre-transfusion hemoglobin;
- antibody screen, named alloantibodies, direct antiglobulin test, crossmatch
  difficulty, and reaction history;
- spleen status and hemolysis markers;
- ferritin trend, liver iron concentration MRI, and cardiac `T2*`;
- chelator name, dose, adherence, side effects, kidney/liver monitoring;
- exact autoimmune diagnosis and immune medicines.

This can change the research direction without any lab work. Weekly transfusion
may mean severe beta-globin failure, but it may also be amplified by immune
red-cell loss, hypersplenism, under-matching, iron/organ risk, or suboptimal
chelation context.

### 2. Run Existing-Therapy Eligibility Mapping

Before chasing a new molecule, the repo can map what a hematologist should
evaluate:

- HSCT/transplant donor and risk packet;
- gene therapy or CRISPR therapy referral feasibility;
- luspatercept relevance;
- mitapivat relevance;
- hydroxyurea history and responder context;
- trial availability and exclusion criteria.

This is not self-treatment. It is a structured way to avoid missing an existing
specialist option while the research program searches for a lower-cost future
candidate.

### 3. Keep The Candidate Funnel Computational

No-lab candidate ranking can still be useful if it stays honest:

- evidence strength: human TDT, patient-cell, primary erythroid, HUDEP2/K562,
  animal, or mechanism-only;
- endpoint fit: HbF, F-cells, alpha/non-alpha globin balance, red-cell survival,
  iron burden, transfusion burden;
- safety gates: hemolysis, liver, kidney, immune, cardiac, endocrine, fertility,
  infection, teratogenicity, and drug interactions;
- access gates: local availability, price, legal status, monitoring burden;
- identity gates: exact molecule, extract standardization, batch quality, and
  supplier traceability.

This can reject bad candidates before money is spent.

### 4. Mine Public Data

Dry-lab work can use public sources:

- PubMed and PMC for mechanism and clinical evidence;
- ClinicalTrials.gov for trial design, endpoints, inclusion, and exclusion;
- FDA, NICE, BPOM, and other regulators for approved-product boundaries;
- PubChem and ChEMBL for compound identity, warnings, targets, and activities;
- public expression and omics datasets where available, such as erythroid,
  HbF, globin-switch, autophagy, and iron-homeostasis datasets.

The useful output is not "AI says this cures thalassemia." The useful output is
a ranked list of hypotheses with explicit missing evidence.

### 5. Prepare A Minimal Future Lab Request

Even if no partner is ready now, the repo can define the first assay package:

- positive controls such as hydroxyurea and known HbF/erythroid benchmarks;
- candidate list kept small;
- endpoints: `HBG1/HBG2`, HbF protein, F-cell distribution, maturation,
  viability, apoptosis, alpha-globin burden, autophagy markers, and hemolysis;
- stop rules for hemolysis, poor identity, toxicity, or no HbF signal;
- no patient sample and no clinical claim unless ethics and clinician review
  are in place.

That turns a future lab discussion from "please help us find a cure" into
"please quote this exact assay panel with these controls and stop conditions."

## What We Cannot Do Without A Lab

No-lab work cannot prove:

- a new molecule increases HbF in relevant human erythroid cells;
- a compound improves alpha/non-alpha globin balance safely;
- a natural product is safe for severe anemia;
- a candidate does not lyse mature red cells;
- a therapy reduces transfusion burden;
- patient-specific safety, dosing, or drug interaction risk.

Any claim beyond source-backed hypothesis must wait for lab, clinician, and
eventually regulated clinical evidence.

## Current Best No-Lab Priority

The next highest-value no-lab work is case-context completion, not another
random candidate search.

Decision order:

1. Confirm subtype/genotype and Hb fractions.
2. Explain weekly transfusion using volume, pre-transfusion Hb, immune testing,
   spleen status, and red-cell survival context.
3. Complete iron-overload organ-risk packet.
4. Ask whether existing specialist options are relevant.
5. Continue computational candidate ranking only after the case gates are not
   empty.

## Sources

- [TIF 2025 TDT guideline](https://www.ncbi.nlm.nih.gov/books/NBK614251/)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [FDA CASGEVY product page](https://www.fda.gov/vaccines-blood-biologics/casgevy)
- [FDA Aqvesme / mitapivat approval](https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-first-oral-treatment-anemia-thalassemia-inherited-blood-disorder)
- [Curative options eligibility gate](2026-04-27-curative-options-eligibility-gate.md)
- [Iron overload organ-risk gate](2026-04-27-iron-overload-organ-risk-gate.md)
- [Experiment status boundary](2026-04-27-experiment-status-boundary.md)
- [Mechanism gap matrix](2026-04-27-mechanism-gap-matrix.md)
- [First lab quote brief](../assays/2026-04-27-first-lab-quote-brief-v0.md)
