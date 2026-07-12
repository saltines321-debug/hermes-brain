# Hermes Brain

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Security Policy](https://img.shields.io/badge/security-policy-blue.svg)](SECURITY.md)

Hermes Brain is a public, zero-knowledge template for a modular agent skeleton.
The goal is to share the architecture and guardrails without publishing private history, memory, or tuned behavior.

## What this template contains

- A minimal core loop in `brain.py`
- Neutral runtime and privacy defaults in `policies/`
- Example capability scaffolding in `capabilities/`
- Sample inbox input and an empty outbox
- A placeholder memory directory for private deployments

## Public vs. private

This repository intentionally separates two layers:

- Public template: clean structure, guardrails, and reusable capability hooks
- Private runtime: local memory, environment-specific tuning, and learned behavior

The public version should be useful on its own, but it should not carry the accumulated knowledge of a private deployment.

## Quick start

```bash
python3 brain.py
```

This processes any JSON files in `inbox/` and writes a decision report to `outbox/decisions.json`.

## Repository layout

```text
brain.py
capabilities/
policies/
inbox/
outbox/
memory/
README.md
VERSION
```

## Suggested next steps

- Adjust `policies/runtime_rules.json` for your environment.
- Add new capabilities under `capabilities/`.
- Keep `memory/` empty in the public repo and populate it only in private deployments.
