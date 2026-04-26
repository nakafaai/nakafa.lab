"""Fetch compact ClinicalTrials.gov snapshots for research notes."""

import argparse
import json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen


BASE_URL = "https://clinicaltrials.gov/api/v2/studies"


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the trial snapshot fetcher."""
    parser = argparse.ArgumentParser(
        description="Fetch a compact ClinicalTrials.gov snapshot."
    )
    parser.add_argument("--condition", default="Thalassemia")
    parser.add_argument("--location", default="")
    parser.add_argument("--page-size", type=int, default=20)
    parser.add_argument("--output", default="")
    parser.add_argument(
        "--all-statuses",
        action="store_true",
        help="Do not filter to recruiting and not-yet-recruiting studies.",
    )
    return parser.parse_args()


def build_url(args: argparse.Namespace) -> str:
    """Build the ClinicalTrials.gov API URL from parsed arguments."""
    params = {
        "query.cond": args.condition,
        "pageSize": str(args.page_size),
        "countTotal": "true",
    }

    if args.location:
        params["query.locn"] = args.location

    if not args.all_statuses:
        params["filter.overallStatus"] = "RECRUITING,NOT_YET_RECRUITING"

    return f"{BASE_URL}?{urlencode(params)}"


def summarize_study(study: dict) -> dict:
    """Return a compact summary for one ClinicalTrials.gov study payload."""
    protocol = study.get("protocolSection", {})
    identification = protocol.get("identificationModule", {})
    status = protocol.get("statusModule", {})
    design = protocol.get("designModule", {})
    interventions = protocol.get("armsInterventionsModule", {})
    locations = protocol.get("contactsLocationsModule", {})

    countries = sorted(
        {
            location.get("country")
            for location in locations.get("locations", [])
            if location.get("country")
        }
    )

    return {
        "nct_id": identification.get("nctId"),
        "title": identification.get("briefTitle"),
        "status": status.get("overallStatus"),
        "last_update": status.get("lastUpdatePostDateStruct", {}).get("date"),
        "phases": design.get("phases", []),
        "interventions": [
            item.get("name") for item in interventions.get("interventions", [])
        ],
        "countries": countries,
    }


def main() -> int:
    """Fetch a trial snapshot and print or write it as JSON."""
    args = parse_args()
    url = build_url(args)

    with urlopen(url, timeout=30) as response:
        payload = json.load(response)

    snapshot = {
        "query_url": url,
        "total_count": payload.get("totalCount"),
        "studies": [summarize_study(study) for study in payload.get("studies", [])],
    }

    content = json.dumps(snapshot, indent=2, sort_keys=True)

    if args.output:
        Path(args.output).write_text(f"{content}\n", encoding="utf-8")
        return 0

    print(content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
