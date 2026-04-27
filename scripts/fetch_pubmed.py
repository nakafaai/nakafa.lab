"""Fetch compact PubMed search results through NCBI E-utilities."""

import argparse
import json
import time
import urllib.error
import urllib.parse
import urllib.request

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for a PubMed search snapshot."""
    parser = argparse.ArgumentParser(description="Fetch compact PubMed search results.")
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--output", default="")
    return parser.parse_args()


def build_esearch_url(query: str, limit: int) -> str:
    """Build an ESearch URL for a PubMed query."""
    params = {
        "db": "pubmed",
        "retmode": "json",
        "retmax": str(limit),
        "sort": "relevance",
        "term": query,
    }
    return f"{BASE_URL}/esearch.fcgi?{urllib.parse.urlencode(params)}"


def build_esummary_url(pubmed_ids: list[str]) -> str:
    """Build an ESummary URL for PubMed IDs."""
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "json",
    }
    return f"{BASE_URL}/esummary.fcgi?{urllib.parse.urlencode(params)}"


def fetch_json(url: str) -> dict:
    """Fetch JSON from a URL with one retry for transient throttling."""
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        if error.code != 429:
            raise

        time.sleep(1)

        with urllib.request.urlopen(url, timeout=30) as response:
            return json.load(response)


def summarize_record(record: dict) -> dict:
    """Return a compact PubMed record summary."""
    return {
        "pmid": record.get("uid"),
        "title": record.get("title"),
        "journal": record.get("source"),
        "pubdate": record.get("pubdate"),
        "article_ids": record.get("articleids", []),
    }


def search_pubmed(query: str, limit: int) -> dict:
    """Search PubMed and return compact metadata for the top results."""
    try:
        search_payload = fetch_json(build_esearch_url(query, limit))
    except urllib.error.HTTPError as error:
        return {"query": query, "count": 0, "error": f"HTTP {error.code}"}

    pubmed_ids = search_payload.get("esearchresult", {}).get("idlist", [])

    if not pubmed_ids:
        return {"query": query, "count": 0, "results": []}

    try:
        summary_payload = fetch_json(build_esummary_url(pubmed_ids))
    except urllib.error.HTTPError as error:
        return {
            "query": query,
            "count": 0,
            "error": f"HTTP {error.code}",
            "pubmed_ids": pubmed_ids,
        }

    result = summary_payload.get("result", {})
    records = [result[pubmed_id] for pubmed_id in pubmed_ids if pubmed_id in result]

    return {
        "query": query,
        "count": len(records),
        "results": [summarize_record(record) for record in records],
    }


def main() -> int:
    """Fetch a PubMed snapshot and print or write it as JSON."""
    args = parse_args()
    snapshot = search_pubmed(args.query, args.limit)
    content = json.dumps(snapshot, indent=2, sort_keys=True)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as output_file:
            output_file.write(f"{content}\n")
        return 0

    print(content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
