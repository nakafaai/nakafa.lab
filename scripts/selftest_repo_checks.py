"""Self-test the repository hygiene checkers without external dependencies."""

from __future__ import annotations

import pathlib
import tempfile

import check_public_repo
import check_repo_language


def test_public_path_blocks() -> None:
    """Check path-level blocks for local and raw clinical artifacts."""
    cases = {
        ".venv/bin/python": "local environment",
        "research/thalassemia/case-context/raw-record.pdf": "raw case media",
        "data/clinical/raw-scan.png": "raw clinical data media",
        "secrets/token.txt": "private workspace",
    }

    for path, expected in cases.items():
        assert check_public_repo.blocked_path_reason(path) == expected


def test_public_content_blocks() -> None:
    """Check content-level blocks without storing private-looking literals."""
    downloads_dir = "Down" + "loads"
    local_user_path = "/" + "Users/" + f"example/{downloads_dir}/report.pdf"
    mac_temp_path = "/" + "private/" + "var/" + "folders/example/report.pdf"
    openai_key = "s" + "k-" + ("a" * 24)

    content = "\n".join([local_user_path, mac_temp_path, openai_key])

    with tempfile.TemporaryDirectory() as tmpdir:
        path = pathlib.Path(tmpdir) / "candidate.md"
        path.write_text(content, encoding="utf-8")

        matches = check_public_repo.content_matches(str(path))

    assert "private local reference (local user path)" in matches
    assert "private local reference (mac temporary path)" in matches
    assert "private local reference (local downloads path)" in matches
    assert "possible secret pattern (openai api key)" in matches


def test_language_marker_detection() -> None:
    """Check authored-language marker detection and URL normalization."""
    marker = "ka" + "sus"
    url_only_marker = "https://example.test/" + ("un" + "tuk")

    pattern = check_repo_language.marker_pattern()

    assert pattern.search(f"one {marker} marker")
    assert pattern.search(check_repo_language.normalized_line(url_only_marker)) is None


def main() -> int:
    """Run the checker self-tests."""
    test_public_path_blocks()
    test_public_content_blocks()
    test_language_marker_detection()
    print("repo checker self-tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
