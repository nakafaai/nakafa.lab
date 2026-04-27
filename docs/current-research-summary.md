# Current Research Summary

Date: 2026-04-27
Audience: Nakafa founder / engineer
Status: research synthesis, not medical advice

## One-Line State

Nakafa Lab has not found a new cure yet. What we have built is an auditable
research system and an evidence map showing which cure paths are already
validated, which affordable hypotheses are plausible, and which ideas are weak
or unsafe.

## Repo Mental Model

Think of the repo like an engineering pipeline:

- `data/` is raw-ish reproducible evidence snapshots from PubMed,
  ClinicalTrials.gov, PubChem, ChEMBL, full-text sources, and regulatory
  sources.
- `research/thalassemia/findings/` is normalized evidence notes.
- `research/thalassemia/hypotheses/` is the testable backlog.
- `research/islamic/` is Quran, hadith, and ethics framing, kept separate from
  biomedical proof.
- `paper/main.tex` is the evolving paper synthesis.
- `scripts/` is the minimum tooling for repeatable source intake.

## What We Know So Far

For severe transfusion-dependent thalassemia, the credible cure-oriented
endpoint is durable transfusion independence with safe hemoglobin, controlled
iron burden, and acceptable long-term toxicity.

The strongest existing cure logic is hematopoietic stem-cell biology:

- replace the marrow through allogeneic HSCT;
- add functional beta-globin through lentiviral gene therapy;
- reactivate fetal hemoglobin through CRISPR editing of the `BCL11A` enhancer.

These prove that thalassemia can be made transfusion-independent in selected
patients, but they are expensive, infrastructure-heavy, and not yet broadly
accessible in Indonesia.

## Main Scientific Lanes

| Lane | Current meaning | Status |
| --- | --- | --- |
| HbF reactivation | Make fetal hemoglobin compensate for defective beta-globin | strongest cure-mimic lane |
| Globin and erythroid biology | Improve globin balance, erythroid maturation, or red-cell survival | active mechanism map |
| Iron axis | Hepcidin, ferroportin, `TMPRSS6`, `ERFE`, chelation, MRI iron burden | credible disease-modifying comparator |
| Existing drugs | hydroxyurea, sirolimus, thalidomide class, luspatercept, mitapivat | evidence review, not recommendation |
| Natural products | curcuminoid analogs, resveratrol, ginger, EGCG, olive, pomegranate, date-palm, bee products | mostly hypothesis/support lanes |
| Indonesia access | BPOM, BPJS, centers, genotype testing, MRI, trials | major unsolved access problem |
| Islamic lane | Quran/hadith as ethical frame and hypothesis inspiration | useful guardrail, not proof by itself |

## Current Candidate Ranking

The current research ranking is:

1. Hydroxyurea evidence map.
2. Sirolimus evidence map.
3. Thalidomide-class evidence map, high caution.
4. Epigenetic HbF target discovery: `MBD2-NuRD`, `LSD1`, `DNMT1`,
   `NRF2/BACH1`.
5. Curcuminoid analog HbF bridge, especially defined analogs rather than
   ordinary curcumin.
6. Assay-ready HbF screen.
7. Hepcidin-ferroportin-`TMPRSS6` iron-restriction comparator.
8. EGCG / green-tea extract adjunct comparator.
9. Propolis red-cell oxidative-stress lane.
10. Royal jelly oxidative-stress lane.
11. Melittin / bee venom lane, hazard-first.

This is not a patient treatment ranking. It is a research prioritization.

## Most Important Findings

Gene therapy and CRISPR validate the biology, but not the access model. Casgevy
and Zynteglo show that stem-cell modification can create transfusion
independence, but the cost and infrastructure are the problem Nakafa Lab is
trying to work around.

HbF reactivation is the main affordable-cure hypothesis. If we can find a safer
and cheaper way to raise `HBG1/HBG2`, HbF protein, and F-cells while preserving
erythroid maturation and avoiding hemolysis, that would mimic part of the
gene-editing success.

Iron biology matters, but it is not "give iron." Quran 57:25 is now documented
as an Al-Hadid guardrail: iron has strength and benefit, but in thalassemia
iron overload can damage organs. The scientific lane is hepcidin, ferroportin,
`TMPRSS6`, `ERFE`, chelation, and MRI iron burden.

Natural-product lanes are mostly not cure lanes yet. Some have useful support
signals:

- EGCG / green-tea extract has randomized TDT adjunct evidence, but also liver
  safety and standardization risks.
- Ginger / 6-shogaol has ex vivo TDT red-cell support evidence, not HbF cure
  evidence.
- Black seed plus manuka honey has an adjunct iron-overload trial signal, not a
  thalassemia cure claim.
- Curcuminoid analogs are more interesting than ordinary curcumin because some
  defined analogs connect to HbF endpoints.
- Bee venom / melittin is hazard-first because hemolysis and allergy are major
  risks.

The Islamic lane is useful, but only with discipline. Quran and hadith can
motivate search, ethics, humility, and hypothesis generation. They cannot be
used to bypass compound identity, dose, safety, reproducibility, and clinician
review.

## Have We Done Experiments?

Not yet in the wet-lab sense.

We have done:

- literature retrieval;
- clinical-trial registry snapshots;
- chemistry identity snapshots;
- full-text extraction for selected open sources;
- assay design;
- hypothesis cards;
- source-backed ranking.

We have not done:

- patient intervention;
- blood sample experiment;
- HbF reporter assay;
- hemolysis assay;
- cell culture experiment;
- animal experiment;
- clinical trial;
- molecular docking or AI-designed molecule validation.

So the current maturity is research intelligence and experiment design, not
biological proof from our own lab.

## How Could We Actually Move Toward A Cure?

The realistic path is staged:

1. Confirm the exact disease subtype and genotype.
2. Make sure standard care is optimized: transfusion interval, antigen matching,
   chelation, ferritin, liver iron, cardiac `T2*`, endocrine and organ checks.
3. Ask a hematologist whether approved disease-modifying options are relevant:
   luspatercept, mitapivat, HSCT, gene therapy, CRISPR therapy, or clinical
   trials.
4. Build an affordable discovery program around HbF reactivation and red-cell
   survival.
5. Run assays: endogenous HbF reporter or gamma-globin mRNA, HbF protein,
   F-cells, erythroid maturation, hemolysis, viability, and disease-cell
   validation.
6. Only after reproducible assay data, talk about translational development.

## What To Bring To A Doctor

Ask for the exact medical records behind these items:

- exact thalassemia subtype: TDT, NTDT, HbE/beta-thalassemia,
  alpha-thalassemia, or mixed;
- HPLC or electrophoresis: HbA, HbA2, HbF, HbE if present;
- `HBB` and `HBA` genotype if available;
- pre-transfusion hemoglobin trend and target;
- transfusion records: interval, unit count, volume, reactions;
- blood matching policy: ABO, Rh C/c, Rh D, Rh E/e, Kell, and extended matching;
- antibody screen, named alloantibodies, direct Coombs / DAT, crossmatch
  difficulty;
- ferritin trend, liver iron concentration MRI, cardiac `T2*`;
- chelation medicine, dose, adherence, side effects, kidney/liver monitoring;
- spleen status;
- exact autoimmune diagnosis, tests, symptoms, and medicines;
- whether luspatercept, mitapivat, HSCT, gene therapy, or clinical trial
  evaluation is medically appropriate.

The most urgent doctor question from our repo is:

Why is transfusion weekly, and is it due to disease severity alone, poor red-cell
survival, antibody/autoimmune complications, hypersplenism, under-matching,
chelation/iron burden, or another factor?

## Honest Assessment

We still need deep research. But we are no longer starting from zero.

The current repo already has:

- a traceable source registry;
- a main paper draft;
- disease taxonomy and cure strategy;
- Indonesia access map;
- Quran guardrails;
- patient-context checklist;
- assay design;
- candidate ranking;
- hypothesis cards.

The next meaningful leap is not more random reading. It is targeted deepening:
extract numerical evidence, collect the patient's de-identified clinical data,
ask hematologists the right questions, and find a lab partner for HbF /
hemolysis assays.
