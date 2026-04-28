# Publication Readiness

Date checked: 2026-04-27
Status: real-world paper standard and repo-cohesion audit

## Bottom Line

`paper/main.tex` now compiles as a short publication shell with separate
`paper/sections/`, `paper/tables/`, and `paper/figures/` inputs. The manuscript
has the first real-world shape of a biomedical paper, but it is still not a
publication-ready submission.

Current paper type: exploratory, AI-assisted evidence map and research program
proposal.

It should not be framed as original clinical research, a systematic review, a
clinical guideline, or proof of a new treatment until the underlying methods and
data support that claim.

## Real-World Manuscript Standard

The practical baseline for a biomedical paper is:

- a clear article type;
- a title page with authors, affiliations, disclosures, funding, and counts;
- a structured abstract when required by the article type;
- Introduction, Methods, Results, and Discussion structure when reporting
  original research;
- transparent reporting guideline selection, usually through EQUATOR;
- reproducible Methods, including search strategy, data sources, inclusion and
  exclusion logic, extraction, scoring, and software;
- Results that separate retrieved evidence from interpretation;
- Discussion that states what is new, what is limited, and what should happen
  next;
- tables and figures that reduce text burden and are cited in order;
- ethics, AI-use, data availability, code availability, competing interests, and
  funding statements;
- references verified against PubMed, regulators, registries, or original
  sources whenever possible.

## Source-Backed Rules

| Source | Rule for Nakafa Lab |
| --- | --- |
| ICMJE manuscript preparation | Use IMRAD when reporting original research; make Methods reproducible; avoid unsupported conclusions; cite direct sources; include tables and figures only when they clarify evidence. |
| EQUATOR Network | Choose the reporting guideline by study type instead of inventing our own reporting format. |
| PLOS Medicine submission guidance | Keep writing concise and accessible; organize manuscript around Title, Abstract, Introduction, Methods, Results, Discussion, Acknowledgments, References, Supporting information, and Figures/Tables. |
| JAMA instructions | For research reports, include data sharing, acknowledgment/disclosure, AI-use disclosure, timely data, cautious causal language, and limited high-value tables/figures. |

## Current Paper Audit

| Area | Current state | Publication gap |
| --- | --- | --- |
| Article type | Exploratory evidence map and research program proposal. | Must be stated explicitly in title, abstract, and methods. |
| Abstract | Present, but unstructured. | Needs structured form or journal-specific format. |
| Introduction | Present through problem and objective sections. | Needs tighter problem, knowledge gap, and objective. |
| Methods | First explicit Methods section added. | Needs more exact search strings, date ranges, extraction fields, and scoring rules before journal submission. |
| Results | First Results section added. | Needs stronger numeric extraction and tighter links from each table to source snapshots. |
| Discussion | Dedicated Discussion and Limitations sections added. | Needs target-journal word count and reviewer-oriented tightening. |
| Figures | First pipeline and mechanism figures added. | Needs visual polish and possibly one more candidate decision funnel. |
| Tables | First benchmark, candidate, packet, and referral tables added. | Needs final source verification and journal formatting. |
| Ethics and privacy | Dedicated statements plus public case-data release boundary added. | Needs final author/funder/institution details and legal review if submitted. |
| AI disclosure | Dedicated AI-use statement added. | Needs final journal-specific wording. |
| Data/code availability | Dedicated availability statement added. | Needs DOI/archive if the repo is deposited for publication. |
| Islamic lane | Present and carefully bounded. | Must stay in ethics/hypothesis framing, not biomedical proof. |

## Required Main Manuscript Shape

The first LaTeX refactor now follows this structure:

1. Title page
2. Abstract
3. Key points or author summary, if target journal expects it
4. Introduction
5. Methods
6. Results
7. Discussion
8. Limitations
9. Ethics, privacy, AI use, data availability, code availability, funding, and
   competing interests
10. References
11. Figure legends and tables, depending on journal format

## Minimum Tables

| Table | Purpose | Source path |
| --- | --- | --- |
| Table 1: Existing therapy benchmark | Compare HSCT, gene therapy, CRISPR/HbF, luspatercept, mitapivat, hydroxyurea, and iron-axis therapies by endpoint, evidence, access, and safety gate. | `research/thalassemia/findings/` |
| Table 2: Candidate gate matrix | Separate promoted, held, rejected, and hazard-first candidates. | `research/thalassemia/prioritization/` and `research/thalassemia/findings/` |
| Table 3: No-lab clinical packet | Show what data a hematologist needs before trial/referral screening. | `research/thalassemia/case-context/` |
| Table 4: Trial/referral snapshot | Summarize Indonesia, regional, and global active registry counts. | `data/registries/clinicaltrials/` |

## Minimum Figures

| Figure | Purpose | Design rule |
| --- | --- | --- |
| Figure 1: Evidence-to-assay pipeline | Show source retrieval, evidence gating, candidate ranking, assay design, clinical/referral gate, and paper output. | Original vector diagram; no copied publisher art. |
| Figure 2: Thalassemia mechanism map | Connect beta-globin defect, globin imbalance, ineffective erythropoiesis, transfusion, iron overload, and intervention entry points. | Use simple boxes/arrows with clearly named endpoints. |
| Figure 3: Candidate decision funnel | Show reject, hold, assay-only, comparator, and clinician-review lanes. | Should prevent hype by making rejection visible. |

## Repo Cohesion Audit

Current public repo state after this audit:

- no tracked `.html` files;
- no tracked `.venv/`, `.ruff_cache/`, `__pycache__/`, `.env`, private key, or
  credential paths;
- source snapshots are intentionally under `data/`;
- `data/**` and `paper/build/**` are generated for GitHub Linguist through
  `.gitattributes`;
- `scripts/check_public_repo.py` scans tracked, staged, and untracked
  non-ignored files for cache, secret, private, raw case-media, local-path, and
  LaTeX build artifacts;
- `scripts/check_repo_language.py` scans tracked, staged, and untracked
  non-ignored repo-authored text for Indonesian markers;
- `scripts/selftest_repo_checks.py` self-tests the public and language checker
  guardrails;
- `scripts/check_repo.py` uses `scripts/manifests/required_paths.txt` so
  important docs and artifacts cannot silently disappear.

Local ignored caches may exist during tool execution, but they are not part of
the public repository and must stay ignored.

## Dead-File Rule

A file should exist only if at least one of these is true:

- it is a source-backed research artifact;
- it is referenced from `README.md`, a program README, a finding, the source
  registry, or the scaffold manifest;
- it is an executable utility used by documented commands;
- it is a reusable template used by a documented workflow;
- it is a generated evidence snapshot under `data/` with a source-linked note.

If none of those apply, remove or merge the file.

## Next Refactor Rule

Do not expand `paper/main.tex` again. It should remain a short publication
shell. New manuscript content should go into `paper/sections/`, `paper/tables/`,
or `paper/figures/`, and should replace long narrative text with tables or
figures when possible.

The next cleanup should tighten the Methods and Results sections, verify each
table row against a source snapshot, and add the candidate decision funnel only
if it clarifies the manuscript.

## Sources

- [ICMJE manuscript preparation](https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html)
- [EQUATOR reporting guidelines](https://www.equator-network.org/reporting-guidelines/)
- [PLOS Medicine submission guidelines](https://journals.plos.org/plosmedicine/s/submission-guidelines)
- [JAMA instructions for authors](https://jamanetwork.com/journals/jama/pages/instructions-for-authors)
