#!/usr/bin/env python3
# Invariant: decisions are pure; effects only occur through the mode gate.
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
MEMORY_DIR = ROOT / "memory"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_runtime_policies() -> dict[str, Any]:
    return load_json(POLICY_DIR / "runtime_rules.json")


def load_privacy_policies() -> dict[str, Any]:
    return load_json(POLICY_DIR / "privacy.json")


def append_outcome(entry: dict[str, Any]) -> None:
    memory_path = MEMORY_DIR / "outcomes.jsonl"
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    with memory_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry))
        handle.write("\n")


def read_recent_outcomes(limit: int = 50) -> list[dict[str, Any]]:
    memory_path = MEMORY_DIR / "outcomes.jsonl"
    if not memory_path.exists():
        return []

    entries: list[dict[str, Any]] = []
    with memory_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            entry = json.loads(line)
            if entry.get("_note"):
                continue
            entries.append(entry)

    return entries[-limit:]


def failure_streak(outcomes: list[dict[str, Any]]) -> int:
    streak = 0
    for outcome in reversed(outcomes):
        if outcome.get("status") != "ok":
            streak += 1
        else:
            break
    return streak


def perform_action(decision: dict[str, Any]) -> dict[str, Any]:
    return {
        "status": "executed",
        "detail": f"performed {decision.get('intent', 'action')}",
    }


def run_cycle() -> list[dict[str, Any]]:
    runtime_policies = load_runtime_policies()
    privacy_policies = load_privacy_policies()
    results: list[dict[str, Any]] = []
    recent_outcomes = read_recent_outcomes(limit=50)

    for item_path in sorted(INBOX_DIR.glob("*.json")):
        payload = load_json(item_path)
        from capabilities.example_scan import scan

        capability_result = scan(payload)
        decision = {
            "item": item_path.name,
            "risk_score": runtime_policies.get("risk_score", 0.0),
            "local_first": privacy_policies.get("local_first", True),
            "capability": capability_result,
            "schema_version": "1.0",
            "intent": "process_inbox_item",
            "status": "ok",
            "failure_streak": failure_streak(recent_outcomes),
            "mode": runtime_policies.get("default_mode", "execute"),
        }
        if decision.get("mode") == "execute":
            action_result = perform_action(decision)
        else:
            action_result = {"status": "skipped", "detail": "dry_run"}
        decision["action"] = action_result
        results.append(decision)
        if runtime_policies.get("memory_enabled", True):
            append_outcome(decision)

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
