# Repository Hygiene

This repository is public-facing. It should be readable for doctors,
researchers, engineers, and donors without exposing private data or generated
noise.

## Tracked Content

| Area | Purpose |
| --- | --- |
| `README.md` | public project overview and repo map |
| `docs/` | operating protocol, status journals, setup notes, and repo hygiene |
| `research/thalassemia/` | thalassemia findings, hypotheses, assay plans, prioritization, notebooks, and de-identified case context |
| `research/islamic/` | Quran, hadith, tafsir, and Islamic reasoning lane kept separate from biomedical claims |
| `data/` | small reproducible source snapshots, not patient data |
| `paper/` | LaTeX paper source and bibliography |
| `scripts/` | small Python utilities for reproducible fetching and calculations |
| `scripts/manifests/` | line-oriented manifests used by Python checks |
| `templates/` | reusable research, assay, and de-identified clinical-context templates |

## Ignored Content

Generated or local-only files should not enter Git:

- `.ruff_cache/`;
- `.ipynb_checkpoints/`;
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
uv run pyright scripts
uv run python scripts/check_repo.py
uv run python scripts/check_public_repo.py
git diff --check
```

`scripts/check_public_repo.py` wraps these public-repo checks in one repeatable
command. It fails if blocked local paths or common secret patterns are tracked.
