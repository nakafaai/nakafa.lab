# Threat Model Assumption Gate

Date opened: 2026-04-27
Last updated: 2026-04-28
Status: context check needed before final threat model

## Why This Exists

Nakafa Lab is public-facing and may later include de-identified medical context,
research notebooks, source snapshots, scripts, and a LaTeX paper. A final threat
model should not guess the deployment model or data sensitivity. This gate
records what is already visible in the repo and what needs founder confirmation.

## Current Repo Model From Evidence

| Component | Evidence | Current security relevance |
| --- | --- | --- |
| Public research docs | `README.md`, `docs/`, `research/` | Integrity and privacy matter because doctors, researchers, and donors may read the repo. |
| De-identified case lane | `research/thalassemia/case-context/` | Patient context must stay de-identified and separated from interpretation. |
| Source snapshots | `data/` | Snapshots should be reproducible and source-linked, not private patient data. |
| Python scripts | `scripts/` | CLI tools fetch public sources and calculate de-identified research metrics. |
| Notebooks | `research/thalassemia/notebooks/` | Notebooks must avoid hidden outputs containing private data or credentials. |
| LaTeX paper | `paper/` | Generated build outputs should stay ignored; source is public. |

## Assumptions To Confirm

- The GitHub repository is intended to remain public.
- No named patient data, hospital record numbers, exact birth dates, contact
  details, or clinical documents should be committed.
- Raw medical PDFs should stay outside Git. Only de-identified extracted
  clinical facts may be committed to the case lane.
- The current repo is not deployed as a web service; it is a research/document
  repository with local CLI tooling.
- Any future automation or website will need a separate threat model before
  accepting user uploads, accounts, or medical data.

## Questions For Final Threat Model

1. Will `nakafa.lab` stay public even after more case-context data arrives?
2. Will future contributors be allowed to submit files through pull requests, a
   website, or only direct maintainer commits?
3. Will this repo ever store raw medical records privately, or should all raw
   records stay outside Git forever?

## Current Mitigation Before Final Threat Model

- `.gitignore` excludes local environments, caches, private folders, secrets,
  and LaTeX build output.
- `docs/repo-hygiene.md` defines public privacy rules.
- `scripts/check_public_repo.py` checks tracked files for blocked paths and
  common secret patterns.
- Case-001 medical PDFs are handled as local-only inputs; the repo stores only a
  de-identified extraction without names, record numbers, exact addresses,
  facility names, doctor names, phone or fax numbers, signatures, or exact
  sample dates.
