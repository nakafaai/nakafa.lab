# Cure Program Automation Runbook

Date updated: 2026-07-13
Status: active

## Active Automations

| Time | Automation id | Role | Model |
| --- | --- | --- | --- |
| Daily 09:00 WIB | `continue-nakafa-lab-research-loop` | Advance one cure-oriented milestone. | `gpt-5.6-sol`, `xhigh` |
| Daily 23:00 WIB | `nakafa-lab-daily-research-summary` | Integrate evidence into one program decision. | `gpt-5.6-sol`, `xhigh` |

The Codex app stores the automation definitions outside this repository. This
file records their shared operating contract so research artifacts remain
auditable even when automation state is unavailable.

## Start Current

Every run must:

1. read `AGENTS.md`;
2. inspect the worktree and fetch `origin`;
3. fast-forward with `git pull --ff-only` only when the worktree is clean and
   the branch can fast-forward;
4. preserve all user work and never reset or force-push;
5. read the newest status entry, source registry, current prioritization, and
   only the domain files needed for the selected question;
6. re-check time-sensitive claims against primary or official sources current
   on the run date.

## Morning: Advance

The morning run selects one explicit question and advances one outcome from
[`docs/next-steps.md`](../next-steps.md):

- make the clinical/genotype branch reviewable;
- verify a real curative access route; or
- move one affordable candidate toward real multi-endpoint validation.

It may instead run a reproducible analysis when that analysis changes candidate
ranking or an experimental decision.

The result must end with `promote`, `hold`, `deprioritize`, `falsify`, or
`unresolved`, plus the next decisive action.

## Night: Integrate

The nightly run reconciles material evidence produced that day. It should:

- resolve a contradiction or stale claim;
- update a candidate or route decision;
- connect each changed claim to its source and each added source to the claim it
  supports; and
- update `docs/status/YYYY-MM-DD.md` only when evidence, analysis, or a decision
  materially changed.

If nothing changed, it should leave the repository unchanged and report the
queries and sources checked. A status-only commit is not progress.

## Evidence Contract

Every material claim change records:

- `Fact`, `Hypothesis`, `Interpretation`, or `Open question`;
- direct URL, DOI, PMID, registry id, regulatory id, or stable accession;
- date checked and research lane;
- study design, population or model, comparator, endpoint, and follow-up;
- limitations, conflicts, and uncertainty;
- affordability or access implication;
- falsification criterion and next owner or experiment.

Primary literature, clinical guidelines, trial registries, regulatory records,
and official databases take priority. Quran, tafsir, hadith, and Islamic ethics
remain separate from biomedical evidence.

## NGS Boundary

Use the NGS analysis router only when real BCL, FASTQ, BAM/CRAM, VCF, or count
matrix inputs and essential metadata exist. Record accession or file provenance,
checksums, reference build, tool and pipeline versions, QC, and reproducible
commands. Do not fabricate inputs, infer results without data, install software,
or upload human data without explicit approval.

## Anti-Slop Contract

- Search before creating a file and prefer the existing canonical artifact.
- Do not add a gate, tracker, packet, notebook, or duplicate finding merely to
  show activity.
- One question should normally produce one evidence change.
- Do not claim cure, causality, novelty, availability, affordability, clinical
  relevance, or patient eligibility beyond the evidence.
- Keep private health data out of the public repository.

## Verification And Delivery

Run the checks required by `AGENTS.md` for every touched file. The baseline is:

```text
uv run python scripts/check_repo.py
uv run python scripts/check_repo_language.py
uv run python scripts/check_public_repo.py
```

For Python changes, also run Ruff lint and format checks, Pyright, and a focused
behavior test. Build the paper when LaTeX changes and the toolchain is available.

Commit and push only a small, substantive, verified batch when the worktree is
safe. Never force-push.

## Medical Boundary

The automations do not provide patient-specific diagnosis, treatment, dosing,
supplement, transfusion, chelation, referral, travel, import, purchase, or
sample-routing advice. Clinical decisions belong to qualified clinicians.
