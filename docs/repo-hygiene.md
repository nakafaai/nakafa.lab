# Repository Hygiene

This repository is public-facing. It should be readable for doctors,
researchers, engineers, and donors without exposing private data or generated
noise.

## Tracked Content

| Area | Purpose |
| --- | --- |
| `README.md` | public project overview and repo map |
| `docs/` | operating protocol, status journals, setup notes, and repo hygiene |
| `research/thalassemia/` | thalassemia findings, hypotheses, assay plans, prioritization, and de-identified case context |
| `research/islamic/` | Quran, hadith, tafsir, and Islamic reasoning lane kept separate from biomedical claims |
| `data/` | small reproducible source snapshots, not patient data |
| `paper/` | LaTeX paper source and bibliography |
| `scripts/` | small Python utilities for reproducible fetching and calculations |
| `templates/` | reusable research, assay, and de-identified clinical-context templates |

## Ignored Content

Generated or local-only files should not enter Git:

- `.ruff_cache/`;
- `.venv/`;
- `__pycache__/` and `*.pyc`;
- `paper/build/` and other LaTeX outputs;
- `.env*`, private keys, credentials, and `private/`.

If a generated file is needed for evidence, save the smallest source-linked
snapshot under `data/` and register it in
`research/thalassemia/references/source-registry.md`.

## Public Repo Privacy Rule

Do not commit identifiable patient data:

- no names;
- no exact addresses;
- no hospital record numbers;
- no phone numbers or emails;
- no ID numbers;
- no face photos;
- no exact birth dates.

Case material must stay de-identified and must separate family-reported context,
medical records, lab values, repo interpretation, and questions for clinicians.

## Security Checks

Before committing hygiene-sensitive changes, run:

```bash
git status --short
uv run ruff check .
uv run ruff format --check .
uv run python scripts/check_repo.py
git diff --check
```

For public-repo review, also check:

```bash
git ls-files | rg '(^|/)(\\.env|\\.venv|\\.ruff_cache|__pycache__|paper/build|private|secrets|credentials|.*\\.pem|.*\\.key)'
git ls-files | rg '(AKIA[0-9A-Z]{16}|ghp_|github_pat_|sk-[A-Za-z0-9_-]{20,}|BEGIN .*PRIVATE KEY)'
```

The first command should return nothing for tracked generated or private paths.
The second command should return nothing for common secret patterns.
