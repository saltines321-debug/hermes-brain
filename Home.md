# 🧠 Hermes Brain

Welcome to the **Hermes Brain** wiki! This is the central hub for documentation, guides, and resources for the Hermes Brain public template.

## 📚 Quick Navigation

- **[Getting Started](https://github.com/saltines321-debug/hermes-brain/blob/main/docs/developer-setup.md)** - Installation and initial setup
- **[Architecture](https://github.com/saltines321-debug/hermes-brain/blob/main/docs/ARCHITECTURE.md)** - System design and components
- **[Core Loop](https://github.com/saltines321-debug/hermes-brain/blob/main/brain.py)** - The minimal decision loop (`brain.py`)
- **[Configuration](https://github.com/saltines321-debug/hermes-brain/blob/main/config/README.md)** - Runtime and privacy policy setup
- **[Examples](https://github.com/saltines321-debug/hermes-brain/blob/main/docs/examples/MODULAR_REFERENCE.md)** - Extension seams and usage patterns
- **[Developer Experience](https://github.com/saltines321-debug/hermes-brain/blob/main/docs/DEVEX.md)** - Local workflow, validation, and debugging
- **[Contributing](https://github.com/saltines321-debug/hermes-brain/blob/main/CONTRIBUTING.md)** - Contribution guidelines

## 🚀 What is Hermes Brain?

Hermes Brain is a **public, zero-knowledge template** for a modular agent skeleton. It ships the architecture and guardrails of an agentic system — a minimal core decision loop, capability hooks, a policy gate, and append-only memory — without embedding private history, learned behavior, or tuned configuration.

It is a **starting point for building your own brain logic**, not a hosted platform or a distributed orchestration service. Clone it, then fill the extension seams (`core/`, `providers/`, `plugins/`) with your own behavior. The private runtime lives in your own deployment, not in this template.

## ⚡ Key Features

- **Modular skeleton** - A minimal core loop (`brain.py`) plus capability hooks you can extend (`capabilities/`).
- **Policy gate** - Runtime and privacy rules that are safe by default (`allow_external_actions: false`, `retain_private_memory: false`, `redact_sensitive_fields: true`).
- **Append-only memory** - Decisions and outcomes are logged to `memory/outcomes.jsonl`, one JSON object per line.
- **Template vs. Sync modes** - Keep `memory/` private per agent, or commit and share it intentionally across instances.
- **Public / private split** - Clean structure and guardrails ship publicly; private runtime state stays out of the template.

## 🛠️ Tech Stack

- **Language**: Python (template core) with shell helper scripts (`scripts/`)
- **License**: MIT
- **Repository**: [saltines321-debug/hermes-brain](https://github.com/saltines321-debug/hermes-brain)

## 📖 Documentation Structure

### Core Concepts

- [Architecture](https://github.com/saltines321-debug/hermes-brain/blob/main/docs/ARCHITECTURE.md) - Folder responsibilities and the template boundary
- [Extension Seams](https://github.com/saltines321-debug/hermes-brain/blob/main/docs/examples/MODULAR_REFERENCE.md) - `core -> providers -> plugins` dependency direction
- [Configuration & Policies](https://github.com/saltines321-debug/hermes-brain/blob/main/config/README.md) - Runtime rules and privacy defaults
- [State & Memory](https://github.com/saltines321-debug/hermes-brain/blob/main/memory/README.md) - Append-only outcomes and the Template/Sync mode split

### Development

- [Development Setup](https://github.com/saltines321-debug/hermes-brain/blob/main/docs/developer-setup.md) - Bootstrapping the project
- [Developer Experience](https://github.com/saltines321-debug/hermes-brain/blob/main/docs/DEVEX.md) - Validation, debugging, and coding standards
- [Repository Standards](https://github.com/saltines321-debug/hermes-brain/blob/main/docs/REPOSITORY_STANDARDS.md) - Branching, commits, releases
- [Repository Setup](https://github.com/saltines321-debug/hermes-brain/blob/main/docs/REPOSITORY_SETUP.md) - Branch protection and CI guidance

### Operations

- [CI Workflows](https://github.com/saltines321-debug/hermes-brain/tree/main/.github/workflows) - Reusable quality, CI, and release pipelines
- [Security Policy](https://github.com/saltines321-debug/hermes-brain/blob/main/SECURITY.md) - Reporting and handling guidance

## 🔗 External Resources

- [GitHub Repository](https://github.com/saltines321-debug/hermes-brain)
- [Issues & Feature Requests](https://github.com/saltines321-debug/hermes-brain/issues)
- [Discussions](https://github.com/saltines321-debug/hermes-brain/discussions)

## 💡 Getting Help

### For Issues

- Check the [Developer Experience](https://github.com/saltines321-debug/hermes-brain/blob/main/docs/DEVEX.md) debugging section
- Search existing [GitHub Issues](https://github.com/saltines321-debug/hermes-brain/issues)
- Create a new issue with detailed information

### For Questions

- Review relevant documentation pages linked above
- Check [GitHub Discussions](https://github.com/saltines321-debug/hermes-brain/discussions)
- Ask the community for guidance

## 🤝 Contributing

We welcome contributions! Please see [Contributing](https://github.com/saltines321-debug/hermes-brain/blob/main/CONTRIBUTING.md) for guidelines on:

- Reporting bugs
- Proposing features
- Submitting pull requests
- Code standards and conventions

## 📝 License

Hermes Brain is licensed under the MIT License. See the [LICENSE](https://github.com/saltines321-debug/hermes-brain/blob/main/LICENSE) file for details.

---

**Last Updated**: 2026-07-12

*This wiki is maintained by the Hermes Brain community. For the latest updates, visit the [GitHub repository](https://github.com/saltines321-debug/hermes-brain).*
