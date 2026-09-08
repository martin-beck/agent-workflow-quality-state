# Agent Workflow Quality current coordination state

This file is generated. Read `README.md`, then use `tools/handoffctl snapshot`.
Never edit this file directly.

## In Progress

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P1 | [AR-0020](tasks/AR-0020.md): Pinned Rust stable PR gates | Add exact stable-toolchain formatting, Clippy, build, documentation and test contracts. | Pin Rust 1.93.0 acquisition and implement offline native-equivalent PR contracts. | codex-awq-ar0020 |

## Blocked

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-0017](tasks/AR-0017.md): State coordinator v0.3.1 and source-header compliance | Sync immutable coordinator v0.3.2 and enforce Huawei/MIT headers on state-owned source files. | Sync and verify coordinator v0.3.2, then implement state-owned header policy and run focused and full gates. | - |
| P1 | [AR-0016](tasks/AR-0016.md): Huawei and MIT source-header compliance | Enforce exact Huawei 2026 and SPDX MIT headers across first-party AWQ source files. | Register the established SSH signing key with GitHub, review and merge product PR 4, then sync state-vendored coordinator source only from a released upstream version. | - |

## Planned

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P1 | [AR-0005](tasks/AR-0005.md): Rust and Android JVM assurance profiles | Add deep ecosystem gates for the two compiled stacks used by the initial consumers. | Complete and release the Rust and Android/JVM child ARs, then verify umbrella acceptance. | - |
| P1 | [AR-0007](tasks/AR-0007.md): Reproducible releases SBOM and provenance | Harden AWQ distribution with reproducibility, SBOM, attestations and verified update metadata. | Design the release manifest and decompose reproducibility, SBOM, provenance and update verification. | - |
| P1 | [AR-0008](tasks/AR-0008.md): Consumer equivalence and enforcement promotion | Measure shadow results across all four consumers and safely promote proven shared gates. | Define an equivalence corpus, mismatch taxonomy, observation period and per-consumer promotion decisions. | - |
| P1 | [AR-0018](tasks/AR-0018.md): Pinned Rust assurance profile and adapters | Add reviewed Rust formatting, lint, dependency, compatibility and advanced test evidence contracts. | Promote and implement the Rust profile after AR-0005 decomposition is recorded. | - |
| P1 | [AR-0019](tasks/AR-0019.md): Pinned Android and JVM assurance profile and adapters | Add reviewed Gradle, Kotlin, Android lint, dependency, ABI and UI-boundary evidence contracts. | Promote after the Rust child or when independently scheduled, then implement the Android/JVM profile. | - |
| P1 | [AR-0021](tasks/AR-0021.md): Pinned Rust supply and API compatibility gates | Add dependency policy, advisory and public API compatibility contracts for Rust projects. | Implement after stable Rust PR contracts define the toolchain and fixture boundary. | - |
| P2 | [AR-0006](tasks/AR-0006.md): Formal evidence and refactoring assurance | Model stateful quality semantics and add behavior-preserving refactoring evidence contracts. | Identify safety invariants, bounded models, counterexample fixtures and refactoring equivalence strategies. | - |
| P2 | [AR-0022](tasks/AR-0022.md): Bounded Rust coverage fuzz and mutation evidence | Add bounded coverage, fuzzing and mutation contracts with explicit corpus, time and platform limits. | Implement after the stable Rust toolchain contract is released. | - |

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
| P1 | [AR-0004](tasks/AR-0004.md): Python shell documentation and schema adapters | Turn baseline format checks into composable first-class adapters with pinned tool contracts. | Run final gate, build and wheel smoke; audit, sign and publish the v0.4.0 candidate. | - |
| P1 | [AR-0012](tasks/AR-0012.md): Pinned Python quality adapters | Published AWQ v0.5.0 with reviewed opt-in Python quality adapters and normalized remediation evidence. | No further AR-0012 action; select the next dependency-ready adapter family. | - |
| P1 | [AR-0013](tasks/AR-0013.md): Pinned shell quality adapters | Published AWQ v0.6.0 with reviewed opt-in ShellCheck, shfmt and Bats adapters plus atomic checksum-pinned acquisition. | No further AR-0013 action; select the next dependency-ready adapter family. | - |
| P1 | [AR-0014](tasks/AR-0014.md): Pinned documentation quality adapters | Published AWQ v0.7.0 with reviewed offline rumdl and Vale documentation adapters, bounded tracked-format selection, and checksum-pinned acquisition. | No further AR-0014 action; select the next dependency-ready adapter family. | - |
| P1 | [AR-0015](tasks/AR-0015.md): Pinned schema quality adapters | Implement JSON, YAML and JSON Schema adapters on the shared contract. | Add strict parser and schema-validation adapters with duplicate-key and draft/version fixtures. | - |
