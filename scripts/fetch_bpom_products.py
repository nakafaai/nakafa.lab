"""Fetch compact BPOM registered-drug search snapshots."""

from __future__ import annotations

import argparse
import http.cookiejar
import json
import re
import urllib.parse
import urllib.request
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

BASE_URL = "https://cekbpom.pom.go.id"
PRODUCT_PAGE_URL = f"{BASE_URL}/produk-obat"
PRODUCT_ENDPOINT_URL = f"{BASE_URL}/produk-dt/01"
TOKEN_PATTERN = re.compile(r'<meta name="csrf-token" content="([^"]+)"')


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for BPOM product search snapshots."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("terms", nargs="+", help="Product or ingredient terms.")
    parser.add_argument("--output", default="", help="Optional JSON output path.")
    parser.add_argument("--limit", type=int, default=10, help="Rows per term.")
    return parser.parse_args()


def build_opener() -> urllib.request.OpenerDirector:
    """Build a urllib opener with cookie handling."""
    cookie_jar = http.cookiejar.CookieJar()
    return urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))


def fetch_csrf_token(opener: urllib.request.OpenerDirector) -> str:
    """Fetch the BPOM product page and extract its CSRF token."""
    request = urllib.request.Request(
        PRODUCT_PAGE_URL,
        headers={"User-Agent": "nakafa.lab/0.1"},
    )
    with opener.open(request, timeout=30) as response:
        html = response.read().decode("utf-8", errors="replace")

    match = TOKEN_PATTERN.search(html)
    if not match:
        raise ValueError("Could not find BPOM CSRF token.")

    return match.group(1)


SEARCH_FIELDS = ("product_name", "ingredients")


def build_payload(term: str, search_field: str, limit: int) -> bytes:
    """Build a DataTables-compatible BPOM product search payload."""
    fields = {
        "draw": "1",
        "start": "0",
        "length": str(limit),
        "product_name": term,
        "product_register": "",
        "product_brand": "",
        "product_package": "",
        "product_form": "",
        "ingredients": "",
        "submit_date_start": "",
        "submit_date_end": "",
        "product_date_start": "",
        "product_date_end": "",
        "expire_date_start": "",
        "expire_date_end": "",
        "manufacturer_name": "",
        "status": "",
    }
    fields[search_field] = term
    return urllib.parse.urlencode(fields).encode("utf-8")


def fetch_term(
    opener: urllib.request.OpenerDirector,
    token: str,
    term: str,
    search_field: str,
    limit: int,
) -> dict[str, Any]:
    """Fetch one compact BPOM product search result."""
    request = urllib.request.Request(
        PRODUCT_ENDPOINT_URL,
        data=build_payload(term, search_field, limit),
        headers={
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "nakafa.lab/0.1",
            "X-CSRF-TOKEN": token,
            "X-Requested-With": "XMLHttpRequest",
        },
        method="POST",
    )
    with opener.open(request, timeout=30) as response:
        payload = json.load(response)

    if not isinstance(payload, dict):
        raise ValueError("BPOM response was not a JSON object.")

    return compact_response(term, search_field, payload)


def compact_response(
    term: str,
    search_field: str,
    payload: dict[str, Any],
) -> dict[str, Any]:
    """Return only the BPOM fields needed for access research."""
    records = payload.get("data", [])
    if not isinstance(records, list):
        records = []

    return {
        "term": term,
        "search_field": search_field,
        "records_filtered": payload.get("recordsFiltered"),
        "records_total": payload.get("recordsTotal"),
        "records": [
            compact_record(record) for record in records if isinstance(record, dict)
        ],
    }


def compact_record(record: dict[str, Any]) -> dict[str, Any]:
    """Return a compact BPOM product record."""
    return {
        "product_register": record.get("PRODUCT_REGISTER"),
        "product_name": record.get("PRODUCT_NAME"),
        "product_brand": record.get("PRODUCT_BRANDS"),
        "product_package": record.get("PRODUCT_PACKAGE"),
        "product_date": record.get("PRODUCT_DATE"),
        "product_expired": record.get("PRODUCT_EXPIRED"),
        "manufacturer_name": record.get("MANUFACTURER_NAME"),
        "manufacturer_country": record.get("MANUFACTURER_COUNTRY_DETAIL"),
        "status": record.get("STATUS"),
    }


def fetch_snapshot(terms: list[str], limit: int) -> dict[str, Any]:
    """Fetch a BPOM product search snapshot for multiple terms."""
    opener = build_opener()
    token = fetch_csrf_token(opener)
    return {
        "checked_at": datetime.now(UTC).date().isoformat(),
        "source_page": PRODUCT_PAGE_URL,
        "source_endpoint": PRODUCT_ENDPOINT_URL,
        "queries": [
            fetch_term(opener, token, term, search_field, limit)
            for term in terms
            for search_field in SEARCH_FIELDS
        ],
    }


def main() -> int:
    """Fetch BPOM product searches and print or write JSON."""
    args = parse_args()
    snapshot = fetch_snapshot(args.terms, args.limit)
    content = json.dumps(snapshot, indent=2, sort_keys=True)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(f"{content}\n", encoding="utf-8")
        return 0

    print(content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
