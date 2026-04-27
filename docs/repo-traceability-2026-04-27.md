# Repo Traceability Audit: 2026-04-27

Status: public-repo cohesion audit

## Purpose

This audit records what is currently tracked in `nakafa.lab` and why the repo
is intentionally data-heavy. The goal is to keep the project inspectable for
engineers, doctors, researchers, and future collaborators without hiding noisy
or private files in the public repository.

## Current File Trace

Tracked files after this audit batch: `663`.

| Top-level area | Files | Role |
| --- | ---: | --- |
| `data/` | 477 | source snapshots and extracted evidence records |
| `research/` | 145 | findings, assays, hypotheses, case-context, Islamic lane, and research maps |
| `docs/` | 12 | operating docs, status journals, security, setup, and hygiene |
| `scripts/` | 10 | small Python utilities and manifests |
| `templates/` | 6 | reusable research, assay, and de-identified clinical templates |
| `paper/` | 4 | LaTeX paper source, bibliography, notes, and editor root |
| `.zed/` | 1 | editor task integration for local research workflow |
| root config/docs | 8 | repo config, README, agent guide, Python project files |

## File-Type Trace

| Type | Files | Meaning |
| --- | ---: | --- |
| `.json` | 420 | PubMed, ClinicalTrials.gov, PubChem, ChEMBL, BPOM, and registry snapshots |
| `.md` | 157 | docs, findings, assays, hypotheses, Quran notes, templates |
| `.xml` | 40 | PubMed or PMC abstract/full-text source snapshots |
| `.txt` | 15 | source-linked full-text extracts, not raw browser HTML |
| `.py` | 9 | small Python utilities |
| `.ipynb` | 8 | small reproducible notebooks |
| no extension | 5 | root/editor configuration files such as `.gitattributes` and `.gitignore` |
| `.xlsx` | 3 | PLOS supplementary assay tables used for reproducible extraction |
| `.tex` | 2 | LaTeX paper source |
| `.bib`, `.toml`, `.csv`, `.lock` | 1 each | bibliography, Python config, template CSV, uv lockfile |

## Data Directory Trace

| Data area | Files | Reason kept |
| --- | ---: | --- |
| `data/literature/` | 261 | literature, full-text extracts, PubMed XML/JSON, and supplementary source tables |
| `data/chemistry/` | 157 | PubChem and ChEMBL identity snapshots for candidate molecules |
| `data/registries/` | 55 | ClinicalTrials.gov snapshots |
| `data/regulatory/` | 3 | BPOM and EFSA access/safety snapshots |
| `data/README.md` | 1 | data-governance rules |

## Research Directory Trace

| Research area | Files | Reason kept |
| --- | ---: | --- |
| `research/thalassemia/findings/` | 84 | small source-backed findings and decision notes |
| `research/thalassemia/assays/` | 8 | assay specs, lab partner requirements, and quote/work-order docs |
| `research/thalassemia/hypotheses/` | 8 | structured candidate hypotheses |
| `research/thalassemia/case-context/` | 5 | de-identified case routing and clinician questions |
| `research/thalassemia/prioritization/` | 5 | candidate ranking and signature labels |
| `research/thalassemia/notebooks/` | 9 | reproducible scoring and literature-matrix experiments |
| `research/thalassemia/references/` | 1 | source registry |
| `research/thalassemia/README.md` | 1 | disease program entrypoint |
| `research/islamic/` | 24 | Quran, hadith, tafsir, ethics, and natural-material anchor notes |

## HTML And Generated-File Boundary

No `.html` files are tracked.

The only browser-derived full-text files are four `.dom.txt` files under
`data/literature/fulltext/pubmed/`. They are text extracts used as source-linked
research artifacts, not raw HTML dumps.

`data/**` and `paper/build/**` are marked `linguist-generated` in
`.gitattributes`, so source snapshots should not be treated as the codebase's
primary programming language on GitHub.

## Largest Files

The largest tracked file is under `1 MB`:

| Size | Path | Reason kept |
| ---: | --- | --- |
| 861,704 bytes | `data/literature/supplementary/plos/2026-04-27-yang-2024-fig4-lead-hit-drugs-s003.xlsx` | PLOS supplementary hit table for the HUDEP2 HbF screen |
| 394,230 bytes | `data/literature/pubmed/2026-04-27-top-clinical-lanes-abstracts.xml` | PubMed abstract bundle for clinical benchmark extraction |
| 352,447 bytes | `data/chemistry/pubchem/natural-product-hbf/2026-04-27-citropten-description.json` | PubChem identity/description snapshot |
| 349,833 bytes | `data/regulatory/efsa/2026-04-27-efsa-green-tea-catechins-safety-pmc.txt` | EFSA-linked safety source extract |
| 340,475 bytes | `data/literature/pubmed/2026-04-27-bcl11a-hbf-switch-selected-abstracts.xml` | PubMed abstract bundle for BCL11A/HbF switch evidence |

None of these are build outputs, local caches, secrets, or private patient data.

## Current Guardrails

- `.gitignore` excludes `.venv/`, `.ruff_cache/`, `.ipynb_checkpoints/`,
  `__pycache__/`, `.env*`, private keys, `private/`, `secrets/`, credentials,
  and LaTeX build outputs.
- `scripts/check_public_repo.py` fails if blocked local paths or common secret
  patterns enter tracked files.
- `scripts/check_repo.py` validates required scaffold paths.
- `data/README.md` forbids raw browser HTML and identifiable patient data.
- `research/thalassemia/references/source-registry.md` is the public evidence
  index for source-backed claims.

## Decision

The repo is intentionally snapshot-heavy because research claims need
reproducible source artifacts. The current data volume is acceptable for a
public research repo because:

- source snapshots are under `data/` and marked generated for GitHub Linguist;
- no raw `.html` files are tracked;
- no local cache, virtual environment, private workspace, or credential file is
  tracked;
- biomedical conclusions are written in `research/` and `paper/`, while raw
  evidence stays in `data/`.

Next hygiene upgrade: add an automated file-count and largest-file report if
the data directory grows beyond the current manual-audit scale.
