"""A neutral example capability for the public template."""

from __future__ import annotations

from typing import Any


def scan(payload: dict[str, Any]) -> dict[str, Any]:
    """Return a generic analysis result for an inbox item."""
    return {
        "status": "received",
        "kind": payload.get("kind", "example"),
        "note": "This capability is intentionally generic and template-friendly.",
    }
