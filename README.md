# Nakafa Lab

AI-assisted research lab by Nakafa.

The first program is thalassemia: finding a real, evidence-backed, and more
affordable path toward better treatment. The work starts from humility: current
medicine already has standards of care, but access, price, and curative options
are still hard problems, especially for families in Indonesia.

## Problem Statement

Can we discover, validate, and communicate a scientifically credible path toward
thalassemia treatment that is more accessible than today's high-cost curative
options?

This repo exists to make the research traceable enough that doctors,
scientists, donors, and builders can inspect the evidence and help move it
forward.

## Research Lanes

- Clinical baseline: current care, guidelines, approved therapies, trials.
- Mechanism: globin biology, fetal hemoglobin, erythropoiesis, iron overload.
- Therapeutics: drugs, biologics, gene and cell therapy, adjuvant hypotheses.
- Indonesia context: burden, access, screening, blood supply, affordability.
- Islamic research: Quran, tafsir, sirah, hadith, and how they may guide
  ethical reflection and testable hypotheses.

## Repo Map

- `docs/research-protocol.md` - how evidence becomes a hypothesis.
- `docs/next-steps.md` - current operating roadmap.
- `docs/parallel-research-tracks.md` - work that can continue without case data.
- `docs/status/` - dated research status journal entries, not final summaries.
- `docs/security/` - public-repo security assumptions and future threat-model
  gates.
- `docs/repo-traceability-2026-04-27.md` - tracked-file audit and data-snapshot
  justification.
- `research/thalassemia/README.md` - first disease program.
- `research/thalassemia/findings/` - small source-backed research notes.
- `research/thalassemia/hypotheses/` - structured hypothesis candidates.
- `research/thalassemia/prioritization/` - ranked research decisions.
- `research/thalassemia/notebooks/` - small reproducible scoring or analysis
  notebooks.
- `research/thalassemia/case-context/` - de-identified patient context.
- `research/thalassemia/references/source-registry.md` - seed source list.
- `research/islamic/README.md` - Islamic research lane.
- `research/islamic/quran/` - structured Quran anchor notes.
- `research/islamic/findings/` - Quran, hadith, tafsir, and ethics notes.
- `paper/main.tex` - working LaTeX paper skeleton.
- `paper/notes/` - focused LaTeX notes that may later feed the main paper.
- `paper/references.bib` - initial bibliography.
- `templates/` - reusable research and clinical-context templates.
- `scripts/helpers/` - small reusable helpers for Python research utilities.
- `scripts/manifests/` - line-oriented repo manifests kept outside Python code.
- `docs/zed-latex.md` - how to build and preview the paper in Zed.
- `docs/repo-hygiene.md` - public repo hygiene, privacy, and security checks.

## Python Tooling

Python research utilities should use `uv` for environment management, `ruff`
for linting/formatting, and Pyright for editor-compatible type checks. This
repo keeps the Python setup minimal until real analysis code exists.

Common commands:

- `uv run python scripts/check_repo.py`
- `uv run python scripts/check_public_repo.py`
- `uv run python scripts/fetch_clinical_trials.py --condition Thalassemia`
- `uv run python scripts/fetch_pubmed.py "fetal hemoglobin beta thalassemia"`
- `uv run python scripts/fetch_bpom_products.py REBLOZYL luspatercept`
- `uv run python scripts/summarize_case_timeline.py <deidentified-timeline.csv>`
- `uv run ruff check .`
- `uv run ruff format .`
- `uv run pyright scripts`

This repo does not use Node dependencies right now. Do not add `package.json`
or `pnpm` just to wrap Python or LaTeX commands.

## Safety Boundary

Nothing here is medical advice. The repository can generate questions,
hypotheses, evidence maps, and draft papers. Diagnosis, treatment, dosing, and
patient decisions require licensed clinicians.

## Current Status

Kickoff scaffold created on 2026-04-26. Current research focus:

- cure-oriented endpoint: durable transfusion independence;
- biological strategy: HbF reactivation and globin-balance mimicry;
- first affordable comparator: hydroxyurea;
- discovery workflow: HbF assay funnel plus hemolysis and toxicity screening;
- no-lab action: complete the de-identified clinical packet until a doctor can
  judge trial/referral screenability;
- Islamic lane: Quran-wide `shifa` map and theology of means;
- bee-derived lane: broad material scope, but direct HbF evidence remains a gap.
