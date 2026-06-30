"""Summarize branch-review gates into one public-safe handoff label."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Final, NotRequired, TypedDict

PACKET_NOT_READY_LABEL: Final = "branch_review_packet_not_ready_public_only"
PACKET_READY_LABEL: Final = "branch_review_packet_ready_for_private_clinician_review"

RESPONSE_CAPTURED_LABEL: Final = "branch_review_response_captured_public_labels_only"
RESPONSE_FOLLOWUP_LABEL: Final = "branch_review_response_needs_private_followup"
RESPONSE_BLOCKED_LABEL: Final = (
    "branch_review_response_release_blocked_private_material"
)

HANDOFF_PACKET_INCOMPLETE_LABEL: Final = "branch_review_handoff_packet_incomplete"
HANDOFF_READY_FOR_QUESTION_LABEL: Final = (
    "branch_review_handoff_ready_for_private_clinician_question"
)
HANDOFF_NEEDS_FOLLOWUP_LABEL: Final = "branch_review_handoff_needs_private_followup"
HANDOFF_RELEASE_BLOCKED_LABEL: Final = (
    "branch_review_handoff_release_blocked_private_material"
)
HANDOFF_RESPONSE_CAPTURED_LABEL: Final = (
    "branch_review_handoff_response_captured_public_only"
)

PACKET_LABELS: Final = {
    PACKET_NOT_READY_LABEL,
    PACKET_READY_LABEL,
}

RESPONSE_LABELS: Final = {
    RESPONSE_CAPTURED_LABEL,
    RESPONSE_FOLLOWUP_LABEL,
    RESPONSE_BLOCKED_LABEL,
}

PRIVATE_ONLY_KEYS: Final = {
    "private_record_ref",
    "notes_private",
    "private_response_ref",
    "raw_clinician_message",
    "doctor_identity",
    "hospital_identity",
}

BLOCKED_OUTPUTS: Final = [
    "raw private record",
    "raw clinician message",
    "private response reference",
    "doctor or hospital identity",
    "patient-specific eligibility claim",
    "therapy selection",
    "trial-screening instruction",
    "referral instruction",
    "travel or import plan",
    "purchase or procurement route",
    "dose or treatment recommendation",
    "transfusion or chelation change",
    "lab contact permission",
    "sample routing",
]

NEXT_STEP_BY_HANDOFF_LABEL: Final = {
    HANDOFF_PACKET_INCOMPLETE_LABEL: "publish_missing_packet_labels_only",
    HANDOFF_READY_FOR_QUESTION_LABEL: "ask_private_clinician_branch_question",
    HANDOFF_NEEDS_FOLLOWUP_LABEL: "publish_followup_labels_only",
    HANDOFF_RELEASE_BLOCKED_LABEL: "public_release_blocked",
    HANDOFF_RESPONSE_CAPTURED_LABEL: "publish_captured_response_labels_only",
}


class PacketSummary(TypedDict):
    """Public output emitted by the branch-review packet checker."""

    current_label: str
    ready_domains: list[str]
    missing_domains: list[str]
    public_labels: list[str]
    blocked_outputs: list[str]


class ResponseSummary(TypedDict):
    """Public output emitted by the branch-review response-capture gate."""

    current_label: str
    captured_labels: list[str]
    missing_domains: list[str]
    branch_scope_labels: list[str]
    blocked_outputs: list[str]


class HandoffSummary(TypedDict):
    """Public-safe handoff status across packet and response gates."""

    current_label: str
    packet_label: str
    response_label: NotRequired[str | None]
    missing_domains: list[str]
    branch_scope_labels: list[str]
    next_public_step_label: str
    blocked_outputs: list[str]


def load_json(path: str) -> dict[str, object]:
    """Read one gate output JSON object from disk."""
    with Path(path).open(encoding="utf-8") as source_file:
        parsed = json.load(source_file)

    if isinstance(parsed, dict):
        return parsed

    raise ValueError(f"{path} must contain a JSON object.")


def require_string_list(payload: dict[str, object], key: str) -> list[str]:
    """Return a required list of strings from one JSON payload."""
    value = payload.get(key)
    if not isinstance(value, list):
        raise ValueError(f"`{key}` must be a list.")

    values: list[str] = []
    for item in value:
        if not isinstance(item, str):
            raise ValueError(f"`{key}` must contain only strings.")
        values.append(item)

    return values


def reject_private_keys(payload: dict[str, object], path_label: str) -> None:
    """Fail closed if private-only keys appear in an input or output object."""
    leaked = PRIVATE_ONLY_KEYS.intersection(payload)
    if not leaked:
        return

    joined = ", ".join(sorted(leaked))
    raise ValueError(f"{path_label} contains private-only keys: {joined}.")


def parse_packet(payload: dict[str, object]) -> PacketSummary:
    """Validate public packet-checker output before handoff summarization."""
    reject_private_keys(payload, "packet JSON")
    current_label = payload.get("current_label")
    if not isinstance(current_label, str):
        raise ValueError("Packet JSON needs string `current_label`.")
    if current_label not in PACKET_LABELS:
        raise ValueError(f"Unknown packet label `{current_label}`.")

    summary: PacketSummary = {
        "current_label": current_label,
        "ready_domains": require_string_list(payload, "ready_domains"),
        "missing_domains": require_string_list(payload, "missing_domains"),
        "public_labels": require_string_list(payload, "public_labels"),
        "blocked_outputs": require_string_list(payload, "blocked_outputs"),
    }
    return summary


def parse_response(payload: dict[str, object]) -> ResponseSummary:
    """Validate public response-capture output before handoff summarization."""
    reject_private_keys(payload, "response JSON")
    current_label = payload.get("current_label")
    if not isinstance(current_label, str):
        raise ValueError("Response JSON needs string `current_label`.")
    if current_label not in RESPONSE_LABELS:
        raise ValueError(f"Unknown response label `{current_label}`.")

    summary: ResponseSummary = {
        "current_label": current_label,
        "captured_labels": require_string_list(payload, "captured_labels"),
        "missing_domains": require_string_list(payload, "missing_domains"),
        "branch_scope_labels": require_string_list(payload, "branch_scope_labels"),
        "blocked_outputs": require_string_list(payload, "blocked_outputs"),
    }
    return summary


def unique_sorted(values: list[str]) -> list[str]:
    """Return stable unique labels without empty placeholders."""
    return sorted({value for value in values if value})


def choose_handoff_label(
    packet: PacketSummary, response: ResponseSummary | None
) -> str:
    """Collapse packet and optional response labels into one handoff state."""
    if packet["current_label"] == PACKET_NOT_READY_LABEL:
        return HANDOFF_PACKET_INCOMPLETE_LABEL

    if response is None:
        return HANDOFF_READY_FOR_QUESTION_LABEL

    if response["current_label"] == RESPONSE_BLOCKED_LABEL:
        return HANDOFF_RELEASE_BLOCKED_LABEL

    if response["current_label"] == RESPONSE_FOLLOWUP_LABEL:
        return HANDOFF_NEEDS_FOLLOWUP_LABEL

    return HANDOFF_RESPONSE_CAPTURED_LABEL


def summarize_handoff(
    packet: PacketSummary, response: ResponseSummary | None = None
) -> HandoffSummary:
    """Build a label-only public summary from packet and response outputs."""
    current_label = choose_handoff_label(packet, response)
    missing_domains = list(packet["missing_domains"])
    branch_scope_labels: list[str] = []

    if response is not None:
        missing_domains.extend(response["missing_domains"])
        branch_scope_labels.extend(response["branch_scope_labels"])

    summary: HandoffSummary = {
        "current_label": current_label,
        "packet_label": packet["current_label"],
        "response_label": response["current_label"] if response else None,
        "missing_domains": unique_sorted(missing_domains),
        "branch_scope_labels": unique_sorted(branch_scope_labels),
        "next_public_step_label": NEXT_STEP_BY_HANDOFF_LABEL[current_label],
        "blocked_outputs": list(BLOCKED_OUTPUTS),
    }
    reject_private_keys(dict(summary), "handoff summary")
    return summary


def main() -> int:
    """Run the branch-review handoff summarizer CLI."""
    parser = argparse.ArgumentParser(
        description="Summarize public branch-review packet and response labels."
    )
    parser.add_argument("packet_json")
    parser.add_argument("--response-json")
    args = parser.parse_args()

    packet = parse_packet(load_json(args.packet_json))
    response = None
    if args.response_json:
        response = parse_response(load_json(args.response_json))

    summary = summarize_handoff(packet, response)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
