# Architecture

Hermes Brain is structured as a public template with a clear separation between reusable architecture and private runtime state.

The repository intentionally keeps a minimal, neutral core that can be extended without embedding learned behavior or personal history.

## Layout

```text
brain.py
capabilities/
policies/
inbox/
outbox/
memory/
```

## Folder responsibilities

### `brain.py`

This is the public core loop. It loads policy defaults, processes inbox items, and writes decisions to the outbox.

### `capabilities/`

Contains simple capability hooks that can be extended over time. Keep them generic and easy to swap.

### `policies/`

Stores neutral defaults for runtime rules and privacy behavior. These should be safe by default and easy to tune in private deployments.

### `inbox/`

Receives sample or user-generated input payloads. The public template ships with a minimal example.

### `outbox/`

Stores generated outputs such as decisions or reports. The template keeps this directory empty except for a placeholder.

### `memory/`

Intentionally empty in the public repository. Private deployments can store runtime state here without contaminating the template.

## Template boundary

Keep the public repository focused on:

- structure
- guardrails
- capability hooks
- clear defaults

Avoid placing private or environment-specific knowledge in the public template. That includes:

- real memory data
- tuned confidences or risk scores
- logs or generated artifacts
- deployment-specific values

## Extension pattern

When adding a new capability:

1. Define the general behavior in `brain.py` or a capability module.
2. Keep the implementation generic and reusable.
3. Document policy defaults in `policies/`.
4. Add example input under `inbox/` when helpful.
5. Keep private state under `memory/` only for local deployments.
