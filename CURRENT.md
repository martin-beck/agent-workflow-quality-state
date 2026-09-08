# Agent Workflow Quality current coordination state

This file is generated. Read `README.md`, then use `tools/handoffctl snapshot`.
Never edit this file directly.

## In Progress

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-0001](tasks/AR-0001.md): Bootstrap Agent Workflow Quality |  Published AWQ v0.1.0 and integrated its pinned shadow policy across all four target repositories.  |  Wait for exact ASB attestation head post-main quality, Rust and emulated-aarch64 runs; then finish consumer and root coordination audits.  | codex-awq-bootstrap-20260908 |

## Planned

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P1 | [AR-0002](tasks/AR-0002.md): Standards traceability and control catalogue | Make every AWQ requirement traceable to versioned external controls without overstating certification. | Decompose control-source ingestion, mapping review, generated matrices and drift detection. | - |
| P1 | [AR-0003](tasks/AR-0003.md): Policy governance and exception lifecycle | Harden weakening detection, exception approval, repository rules and ownership boundaries. | Decompose semantic policy diff, exception expiry, CODEOWNERS and GitHub ruleset enforcement. | - |
| P1 | [AR-0004](tasks/AR-0004.md): Python shell documentation and schema adapters | Turn baseline format checks into composable first-class adapters with pinned tool contracts. | Decompose one child AR per adapter family and define portable evidence normalization. | - |
| P1 | [AR-0005](tasks/AR-0005.md): Rust and Android JVM assurance profiles | Add deep ecosystem gates for the two compiled stacks used by the initial consumers. | Decompose Rust and Android JVM implementations after adapter contracts from AR-0004 stabilize. | - |
| P1 | [AR-0007](tasks/AR-0007.md): Reproducible releases SBOM and provenance | Harden AWQ distribution with reproducibility, SBOM, attestations and verified update metadata. | Design the release manifest and decompose reproducibility, SBOM, provenance and update verification. | - |
| P1 | [AR-0008](tasks/AR-0008.md): Consumer equivalence and enforcement promotion | Measure shadow results across all four consumers and safely promote proven shared gates. | Define an equivalence corpus, mismatch taxonomy, observation period and per-consumer promotion decisions. | - |
| P2 | [AR-0006](tasks/AR-0006.md): Formal evidence and refactoring assurance | Model stateful quality semantics and add behavior-preserving refactoring evidence contracts. | Identify safety invariants, bounded models, counterexample fixtures and refactoring equivalence strategies. | - |

## Future

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P2 | [AR-0009](tasks/AR-0009.md): Property fuzz mutation and adversarial testing | Expand hostile testing beyond curated fixtures to generated and mutation-based assurance. | Select bounded generators and mutation operators for paths, policies, schemas, workflows and redaction. | - |
| P2 | [AR-0010](tasks/AR-0010.md): Performance flake and evidence-retention budgets | Define scalable runtime, determinism, flake and privacy-preserving retention budgets. | Establish representative repository-size fixtures and decompose performance, flake and retention controls. | - |
| P2 | [AR-0011](tasks/AR-0011.md): Agent onboarding distribution and compatibility | Make AWQ easy for new agents to adopt, update and diagnose across supported environments. | Design compatibility metadata, agent-readable recipes, migration fixtures and package distribution channels. | - |
