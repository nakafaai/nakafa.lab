"""Check that repository-authored prose stays in English."""

from __future__ import annotations

import pathlib
import re
import subprocess

AUTHOR_PREFIXES = (
    ".zed/",
    "docs/",
    "paper/",
    "research/",
    "scripts/",
    "templates/",
)

ROOT_AUTHOR_FILES = {
    "AGENTS.md",
    "README.md",
    "data/README.md",
}

SKIP_PATHS = {
    "scripts/check_repo_language.py",
}

TEXT_SUFFIXES = {
    ".bib",
    ".csv",
    ".ipynb",
    ".json",
    ".md",
    ".py",
    ".tex",
    ".txt",
}

URL_RE = re.compile(r"https?://\S+")

INDONESIAN_MARKERS = {
    "akses",
    "adalah",
    "agar",
    "apakah",
    "atau",
    "bahan",
    "belum",
    "berjalan",
    "bila",
    "bisa",
    "bukan",
    "buat",
    "butuh",
    "dan",
    "dari",
    "dengan",
    "dokter",
    "gunakan",
    "harian",
    "harus",
    "hasil",
    "ini",
    "jalankan",
    "jangan",
    "karena",
    "kasus",
    "klaim",
    "kita",
    "konteks",
    "masih",
    "menjadi",
    "menulis",
    "mungkin",
    "obat",
    "pada",
    "pakai",
    "pasien",
    "penelitian",
    "perubahan",
    "riset",
    "ringkasan",
    "sebagai",
    "setiap",
    "sudah",
    "supaya",
    "sumber",
    "tanpa",
    "terapi",
    "tetap",
    "tidak",
    "untuk",
}


def tracked_paths() -> list[str]:
    """Return tracked paths in deterministic order."""
    result = subprocess.run(
        ["git", "ls-files"],
        check=True,
        capture_output=True,
        text=True,
    )
    return sorted(path for path in result.stdout.splitlines() if path)


def should_scan(path: str) -> bool:
    """Return whether a tracked path is repo-authored text."""
    if path in SKIP_PATHS:
        return False

    if path in ROOT_AUTHOR_FILES:
        return True

    if not path.startswith(AUTHOR_PREFIXES):
        return False

    return pathlib.Path(path).suffix in TEXT_SUFFIXES


def normalized_line(line: str) -> str:
    """Remove content that should not drive prose-language checks."""
    without_urls = URL_RE.sub("", line)
    return without_urls.replace("produk-obat", "")


def marker_pattern() -> re.Pattern[str]:
    """Return the marker regex used for English-policy checks."""
    escaped = sorted(re.escape(marker) for marker in INDONESIAN_MARKERS)
    return re.compile(r"\b(" + "|".join(escaped) + r")\b")


def find_language_markers(paths: list[str]) -> list[str]:
    """Return language-policy findings for authored text files."""
    pattern = marker_pattern()
    findings: list[str] = []

    for path in paths:
        if not should_scan(path):
            continue

        try:
            lines = pathlib.Path(path).read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue

        for line_number, line in enumerate(lines, start=1):
            match = pattern.search(normalized_line(line))
            if match:
                findings.append(f"{path}:{line_number}: Indonesian marker `{match[0]}`")

    return findings


def main() -> int:
    """Run the repository language-policy check."""
    findings = find_language_markers(tracked_paths())

    if not findings:
        print("repo language checks passed.")
        return 0

    print("Repository language check failed:")
    for finding in findings:
        print(f"- {finding}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
