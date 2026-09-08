# Agent Workflow Quality current coordination state

This file is generated. Read `README.md`, then use `tools/handoffctl snapshot`.
Never edit this file directly.

## In Progress

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P1 | [AR-0004](tasks/AR-0004.md): Python shell documentation and schema adapters | Turn baseline format checks into composable first-class adapters with pinned tool contracts. | Decompose one child AR per adapter family and define portable evidence normalization. | codex-awq-ar0004 |

## Planned

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P1 | [AR-0005](tasks/AR-0005.md): Rust and Android JVM assurance profiles | Add deep ecosystem gates for the two compiled stacks used by the initial consumers. | Decompose Rust and Android JVM implementations after all common adapter families stabilize. | - |
| P1 | [AR-0007](tasks/AR-0007.md): Reproducible releases SBOM and provenance | Harden AWQ distribution with reproducibility, SBOM, attestations and verified update metadata. | Design the release manifest and decompose reproducibility, SBOM, provenance and update verification. | - |
| P1 | [AR-0008](tasks/AR-0008.md): Consumer equivalence and enforcement promotion | Measure shadow results across all four consumers and safely promote proven shared gates. | Define an equivalence corpus, mismatch taxonomy, observation period and per-consumer promotion decisions. | - |
| P1 | [AR-0012](tasks/AR-0012.md): Pinned Python quality adapters | Implement first-class Python format, lint, type, test and coverage adapters on the shared contract. | Add pinned Ruff, mypy and project-test adapters with project-owned configuration and equivalence fixtures. | - |
| P1 | [AR-0013](tasks/AR-0013.md): Pinned shell quality adapters | Implement first-class ShellCheck, shfmt and Bats adapters on the shared contract. | Add reviewed tool pins, portable argv and native-equivalence fixtures for shell projects. | - |
| P1 | [AR-0014](tasks/AR-0014.md): Pinned documentation quality adapters | Implement Markdown, link and prose adapters on the shared contract. | Select reviewed offline-capable tools and add deterministic Markdown, link and prose fixtures. | - |
| P1 | [AR-0015](tasks/AR-0015.md): Pinned schema quality adapters | Implement JSON, YAML and JSON Schema adapters on the shared contract. | Add strict parser and schema-validation adapters with duplicate-key and draft/version fixtures. | - |
| P1 | [AR-0016](tasks/AR-0016.md): Huawei and MIT source-header compliance | Enforce exact Huawei 2026 and SPDX MIT headers across first-party AWQ source files. | Add a strict tracked-source checker, tests and CI with explicit generated and vendor exclusions. | - |
| P2 | [AR-0006](tasks/AR-0006.md): Formal evidence and refactoring assurance | Model stateful quality semantics and add behavior-preserving refactoring evidence contracts. | Identify safety invariants, bounded models, counterexample fixtures and refactoring equivalence strategies. | - |

## Future

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P2 | [AR-0009](tasks/AR-0009.md): Property fuzz mutation and adversarial testing | Expand hostile testing beyond curated fixtures to generated and mutation-based assurance. | Select bounded generators and mutation operators for paths, policies, schemas, workflows and redaction. | - |
| P2 | [AR-0010](tasks/AR-0010.md): Performance flake and evidence-retention budgets | Define scalable runtime, determinism, flake and privacy-preserving retention budgets. | Establish representative repository-size fixtures and decompose performance, flake and retention controls. | - |
| P2 | [AR-0011](tasks/AR-0011.md): Agent onboarding distribution and compatibility | Make AWQ easy for new agents to adopt, update and diagnose across supported environments. | Design compatibility metadata, agent-readable recipes, migration fixtures and package distribution channels. | - |

## Done

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-0001](tasks/AR-0001.md): Bootstrap Agent Workflow Quality |  Published AWQ v0.1.0 and integrated its pinned shadow policy across all four target repositories.  | No further bootstrap action; select and promote a dependency-ready planned AR through the coordinator. | - |
| P1 | [AR-0002](tasks/AR-0002.md): Standards traceability and control catalogue | Make every AWQ requirement traceable to versioned external controls without overstating certification. | Commit the verified v0.2.0 candidate, publish its pull request, merge after green checks, release, and fresh-clone verify. | - |
| P1 | [AR-0003](tasks/AR-0003.md): Policy governance and exception lifecycle | Harden weakening detection, exception approval, repository rules and ownership boundaries. | Decompose semantic policy diff, exception expiry, CODEOWNERS and GitHub ruleset enforcement. | - |
