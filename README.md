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
- `research/thalassemia/README.md` - first disease program.
- `research/thalassemia/findings/` - small source-backed research notes.
- `research/thalassemia/case-context/` - de-identified patient context.
- `research/thalassemia/references/source-registry.md` - seed source list.
- `research/islamic/README.md` - Islamic research lane.
- `research/islamic/findings/` - Quran, hadith, tafsir, and ethics notes.
- `paper/main.tex` - working LaTeX paper skeleton.
- `paper/notes/` - focused LaTeX notes that may later feed the main paper.
- `paper/references.bib` - initial bibliography.
- `templates/` - reusable research and clinical-context templates.
- `docs/zed-latex.md` - how to build and preview the paper in Zed.

## Python Tooling

Python research utilities should use `uv` for environment management and `ruff`
for linting/formatting. This repo keeps the Python setup minimal until real
analysis code exists.

Common commands:

- `pnpm check`
- `uv run python scripts/check_repo.py`
- `uv run ruff check .`
- `uv run ruff format .`

## Safety Boundary

Nothing here is medical advice. The repository can generate questions,
hypotheses, evidence maps, and draft papers. Diagnosis, treatment, dosing, and
patient decisions require licensed clinicians.

## Current Status

Kickoff scaffold created on 2026-04-26. The next useful milestone is a compact
landscape review of approved and investigational thalassemia therapies, with a
separate affordability map for Indonesia.
