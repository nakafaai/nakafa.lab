"""Check that candidate public-repo files do not include local or private data."""

from __future__ import annotations

import pathlib
import re
import subprocess

BLOCKED_PATH_PATTERNS = {
    "local environment": re.compile(r"(^|/)\.venv(/|$)"),
    "ruff cache": re.compile(r"(^|/)\.ruff_cache(/|$)"),
    "python cache": re.compile(r"(^|/)__pycache__(/|$)|\.pyc$"),
    "notebook checkpoint": re.compile(r"(^|/)\.ipynb_checkpoints(/|$)"),
    "latex build output": re.compile(r"^paper/build/"),
    "local scratch output": re.compile(r"(^|/)tmp(/|$)"),
    "private workspace": re.compile(r"(^|/)(private|secrets|credentials)(/|$)"),
    "env file": re.compile(r"(^|/)\.env($|[.])"),
    "private key file": re.compile(r"\.(pem|key|p12|pfx)$"),
    "raw case media": re.compile(
        r"(?i)^research/thalassemia/case-context/.+\."
        r"(pdf|png|jpg|jpeg|heic|tif|tiff)$"
    ),
    "raw clinical data media": re.compile(
        r"(?i)^data/(clinical|case|medical-records)/.+\."
        r"(pdf|png|jpg|jpeg|heic|tif|tiff)$"
    ),
}

SECRET_PATTERNS = {
    "aws access key id": re.compile("AK" + "IA" + r"[0-9A-Z]{16}"),
    "github token": re.compile(
        "(" + "gh" + "p_" + "|" + "github" + "_pat_" + r")[A-Za-z0-9_]{20,}"
    ),
    "openai api key": re.compile("s" + "k-" + r"[A-Za-z0-9_-]{20,}"),
    "private key block": re.compile(r"-----BEGIN [A-Z0-9 ]+PRIVATE KEY-----"),
}

PRIVATE_REFERENCE_PATTERNS = {
    "local user path": re.compile("/" + "Users/" + r"[^\s)]+"),
    "mac temporary path": re.compile(
        "/"
        + "var/"
        + "folders/"
        + r"[^\s)]+"
        + "|"
        + "/"
        + "private/"
        + "var/"
        + "folders/"
        + r"[^\s)]+"
    ),
    "local downloads path": re.compile("/" + "Downloads/" + r"[^\s)]*"),
}

CASE_CONTEXT_PREFIXES = ("research/thalassemia/case-context/",)

CASE_CONTEXT_IDENTIFIER_PATTERNS = {
    "case email address": re.compile(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    ),
    "case phone or fax": re.compile(
        r"(?i)\b(phone|fax|mobile|whatsapp)\s*[:#]\s*\+?\d[\d .()-]{6,}\d"
    ),
    "case record identifier": re.compile(
        r"(?i)\b("
        r"mrn|medical record number|hospital id|hospital number|"
        r"accession number|national id|insurance id|record number"
        r")\s*[:#]\s*[A-Za-z0-9][A-Za-z0-9./-]{2,}"
    ),
    "case exact birth date": re.compile(
        r"(?i)\b(date of birth|birth date|dob)\s*[:#]\s*"
        r"(\d{4}-\d{2}-\d{2}|\d{1,2}[/-]\d{1,2}[/-]\d{2,4})"
    ),
    "case patient name field": re.compile(
        r"(?i)\b(patient name|name)\s*[:#]\s*[A-Z][a-z]+(\s+[A-Z][a-z]+)+"
    ),
}


def git_paths(args: list[str]) -> list[str]:
    """Return Git paths for a given `git ls-files` argument list."""
    result = subprocess.run(
        ["git", "ls-files", *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return [path for path in result.stdout.splitlines() if path]


def public_candidate_paths() -> list[str]:
    """Return tracked, staged, and untracked non-ignored paths."""
    paths = set(git_paths(["--cached"]))
    paths.update(git_paths(["--others", "--exclude-standard"]))
    return sorted(paths)


def blocked_path_reason(path: str) -> str | None:
    """Return the block reason when a tracked path should stay out of Git."""
    for reason, pattern in BLOCKED_PATH_PATTERNS.items():
        if pattern.search(path):
            return reason

    return None


def is_case_context_path(path: str) -> bool:
    """Return whether a path contains public case-context prose."""
    return path.startswith(CASE_CONTEXT_PREFIXES)


def content_matches_for_text(path: str, content: str) -> list[str]:
    """Return private-content pattern names found in a text payload."""
    matches: list[str] = []
    matches.extend(
        f"possible secret pattern ({name})"
        for name, pattern in SECRET_PATTERNS.items()
        if pattern.search(content)
    )
    matches.extend(
        f"private local reference ({name})"
        for name, pattern in PRIVATE_REFERENCE_PATTERNS.items()
        if pattern.search(content)
    )

    if not is_case_context_path(path):
        return matches

    matches.extend(
        f"case-context identifier pattern ({name})"
        for name, pattern in CASE_CONTEXT_IDENTIFIER_PATTERNS.items()
        if pattern.search(content)
    )
    return matches


def content_matches(path: str) -> list[str]:
    """Return private-content pattern names found in one tracked file."""
    try:
        content = pathlib.Path(path).read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return [f"could not read {path}"]

    return content_matches_for_text(path, content)


def collect_errors(paths: list[str]) -> list[str]:
    """Collect path and content errors for tracked public files."""
    errors: list[str] = []

    for path in paths:
        reason = blocked_path_reason(path)
        if reason:
            errors.append(f"{path}: blocked tracked path ({reason})")

        for match in content_matches(path):
            errors.append(f"{path}: {match}")

    return errors


def main() -> int:
    """Run the public repository hygiene check."""
    errors = collect_errors(public_candidate_paths())

    if not errors:
        print("public repo checks passed.")
        return 0

    print("Public repo check failed:")
    for error in errors:
        print(f"- {error}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
