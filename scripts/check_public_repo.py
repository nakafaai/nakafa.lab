"""Check that tracked public-repo files do not include local or private data."""

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
}

SECRET_PATTERNS = {
    "aws access key id": re.compile("AK" + "IA" + r"[0-9A-Z]{16}"),
    "github token": re.compile(
        "(" + "gh" + "p_" + "|" + "github" + "_pat_" + r")[A-Za-z0-9_]{20,}"
    ),
    "openai api key": re.compile("s" + "k-" + r"[A-Za-z0-9_-]{20,}"),
    "private key block": re.compile(r"-----BEGIN [A-Z0-9 ]+PRIVATE KEY-----"),
}


def tracked_paths() -> list[str]:
    """Return all tracked Git paths in deterministic order."""
    result = subprocess.run(
        ["git", "ls-files"],
        check=True,
        capture_output=True,
        text=True,
    )
    return sorted(path for path in result.stdout.splitlines() if path)


def blocked_path_reason(path: str) -> str | None:
    """Return the block reason when a tracked path should stay out of Git."""
    for reason, pattern in BLOCKED_PATH_PATTERNS.items():
        if pattern.search(path):
            return reason

    return None


def secret_matches(path: str) -> list[str]:
    """Return secret-pattern names found in one tracked file."""
    try:
        content = pathlib.Path(path).read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return [f"could not read {path}"]

    return [
        name for name, pattern in SECRET_PATTERNS.items() if pattern.search(content)
    ]


def collect_errors(paths: list[str]) -> list[str]:
    """Collect path and content errors for tracked public files."""
    errors: list[str] = []

    for path in paths:
        reason = blocked_path_reason(path)
        if reason:
            errors.append(f"{path}: blocked tracked path ({reason})")

        for secret_name in secret_matches(path):
            errors.append(f"{path}: possible secret pattern ({secret_name})")

    return errors


def main() -> int:
    """Run the public repository hygiene check."""
    errors = collect_errors(tracked_paths())

    if not errors:
        print("public repo checks passed.")
        return 0

    print("Public repo check failed:")
    for error in errors:
        print(f"- {error}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
