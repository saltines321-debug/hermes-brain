#!/usr/bin/env python3
"""Minimal Hermes Brain public template.

This file is intentionally neutral: it provides a working structure, guardrails,
and a simple decision loop without embedding private history or learned bias.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
POLICY_DIR = ROOT / "policies"
INBOX_DIR = ROOT / "inbox"
OUTBOX_DIR = ROOT / "outbox"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_runtime_policies() -> dict[str, Any]:
    return load_json(POLICY_DIR / "runtime_rules.json")


def load_privacy_policies() -> dict[str, Any]:
    return load_json(POLICY_DIR / "privacy.json")


def run_cycle() -> list[dict[str, Any]]:
    runtime_policies = load_runtime_policies()
    privacy_policies = load_privacy_policies()
    results: list[dict[str, Any]] = []

    for item_path in sorted(INBOX_DIR.glob("*.json")):
        payload = load_json(item_path)
        from capabilities.example_scan import scan

        capability_result = scan(payload)
        decision = {
            "item": item_path.name,
            "risk_score": runtime_policies.get("risk_score", 0.0),
            "local_first": privacy_policies.get("local_first", True),
            "capability": capability_result,
        }
        results.append(decision)

    OUTBOX_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTBOX_DIR / "decisions.json"
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(results, handle, indent=2)
        handle.write("\n")

    return results


def main() -> None:
    decisions = run_cycle()
    print(json.dumps(decisions, indent=2))


if __name__ == "__main__":
    main()
