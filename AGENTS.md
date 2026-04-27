# Nakafa Lab Agent Guide

Build for longevity. Keep the repo readable, sourced, and easy for both
developers and researchers to navigate.

## Mission

Nakafa Lab is an AI-assisted research lab under Nakafa. The first research
program focuses on thalassemia, especially the search for treatments that are
scientifically credible and realistically affordable.

This repository is not a medical practice and must not give treatment advice.
Every clinical claim needs a source, and any patient-facing recommendation must
be reviewed by qualified clinicians.

## Working Rules

- Read the repo before changing it.
- Prefer small, direct files over abstraction layers.
- Keep writing skimmable. Avoid cleverness and avoid bloated generated text.
- Use Indonesian by default for public notes unless a paper or source requires
  English.
- Track sources as first-class research objects.
- Distinguish fact, hypothesis, interpretation, and open question.
- For Islamic research, separate Quran text, translation, tafsir, hadith,
  scholarly interpretation, and scientific hypothesis.
- For Python tooling, prefer `uv` for environments and `ruff` for lint/format.
- For Python code changes, also run Pyright-compatible type checking. Do not
  assume Ruff catches editor/Pylance errors.
- Do not overstate causality from observational or preclinical evidence.
- Commit meaningful completed changes when the user asks for repo work.

## Research Standards

- Prefer primary literature, clinical guidelines, registries, regulatory
  documents, and official databases.
- Record source URL, date checked, research lane, and why it matters.
- Keep hypotheses testable: mechanism, evidence, risks, validation plan,
  affordability path, and falsification criteria.
- No unpublished medical claims without a clear evidence label.

## Verification

- Run `uv run python scripts/check_repo.py` after scaffold or documentation
  changes.
- Run `uv run ruff check .` for Python changes.
- Run `uv run ruff format --check .` for Python changes.
- Run `uv run pyright scripts` for Python changes.
- Run a small behavior smoke test for the script or function you changed.
- Build the paper when the LaTeX toolchain is available.
