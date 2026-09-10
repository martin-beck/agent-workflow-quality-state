# Agent Workflow Quality current coordination state

This file is generated. Read `README.md`, then use `tools/handoffctl snapshot`.
Never edit this file directly.

## In Progress

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P1 | [AR-0030](tasks/AR-0030.md): Terminology registry and enforcement | Add reusable canonical-vocabulary declarations and deterministic terminology enforcement. | Coordinator independently reviews exact-head PR 27 at 6b6147a505b81d642df47dc84bca4a5156c5150b; merge only after accepting the Markdown fence correction and all durable evidence. | codex-awq-ar0030-terminology |
| P1 | [AR-0031](tasks/AR-0031.md): Formal-model adapter profile | Add a bounded formal-model execution adapter with truthful evidence output. | No further AR-0031 action; v0.25.0 is publicly released and independently authenticated. Continue dependency-ready AR-0030 and AR-0032 work. | codex-awq-ar0031-formal-adapter |

## Planned

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P1 | [AR-0032](tasks/AR-0032.md): Native-gate and requirement mapping contracts | Bind AWQ requirements to existing native gates without duplicating or weakening them. | Design native-gate mapping schema and implement validation, evidence normalization, and equivalence fixtures. | - |
| P2 | [AR-0033](tasks/AR-0033.md): Agent-ready quality integration workflow | Publish a complete agent-ready workflow for adopting AWQ while retaining native gates. | Generate and test the end-to-end agent integration recipe after terminology and mapping contracts stabilize. | - |

## Done

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-0001](tasks/AR-0001.md): Bootstrap Agent Workflow Quality |  Published AWQ v0.1.0 and integrated its pinned shadow policy across all four target repositories.  | No further bootstrap action; select and promote a dependency-ready planned AR through the coordinator. | - |
| P0 | [AR-0017](tasks/AR-0017.md): State coordinator v0.3.1 and source-header compliance | Sync immutable coordinator v0.3.2 and enforce Huawei/MIT headers on state-owned source files. | Sync and verify coordinator v0.3.2, then implement state-owned header policy and run focused and full gates. | - |
| P1 | [AR-0002](tasks/AR-0002.md): Standards traceability and control catalogue | Make every AWQ requirement traceable to versioned external controls without overstating certification. | Commit the verified v0.2.0 candidate, publish its pull request, merge after green checks, release, and fresh-clone verify. | - |
| P1 | [AR-0003](tasks/AR-0003.md): Policy governance and exception lifecycle | Harden weakening detection, exception approval, repository rules and ownership boundaries. | Decompose semantic policy diff, exception expiry, CODEOWNERS and GitHub ruleset enforcement. | - |
| P1 | [AR-0004](tasks/AR-0004.md): Python shell documentation and schema adapters | Turn baseline format checks into composable first-class adapters with pinned tool contracts. | Run final gate, build and wheel smoke; audit, sign and publish the v0.4.0 candidate. | - |
| P1 | [AR-0005](tasks/AR-0005.md): Rust and Android JVM assurance profiles | Add deep ecosystem gates for the two compiled stacks used by the initial consumers. | Umbrella acceptance verified; close AR-0005 and select the next dependency-ready P1 AR. | - |
| P1 | [AR-0007](tasks/AR-0007.md): Reproducible releases SBOM and provenance | Harden AWQ distribution with reproducibility, SBOM, attestations and verified update metadata. | Complete and release the deterministic-artifact, SPDX SBOM and signed-provenance/update children, then verify umbrella acceptance. | - |
| P1 | [AR-0008](tasks/AR-0008.md): Consumer equivalence and enforcement promotion | Measure shadow results across all four consumers and safely promote proven shared gates. | Define an equivalence corpus, mismatch taxonomy, observation period and per-consumer promotion decisions. | - |
| P1 | [AR-0012](tasks/AR-0012.md): Pinned Python quality adapters | Published AWQ v0.5.0 with reviewed opt-in Python quality adapters and normalized remediation evidence. | No further AR-0012 action; select the next dependency-ready adapter family. | - |
| P1 | [AR-0013](tasks/AR-0013.md): Pinned shell quality adapters | Published AWQ v0.6.0 with reviewed opt-in ShellCheck, shfmt and Bats adapters plus atomic checksum-pinned acquisition. | No further AR-0013 action; select the next dependency-ready adapter family. | - |
| P1 | [AR-0014](tasks/AR-0014.md): Pinned documentation quality adapters | Published AWQ v0.7.0 with reviewed offline rumdl and Vale documentation adapters, bounded tracked-format selection, and checksum-pinned acquisition. | No further AR-0014 action; select the next dependency-ready adapter family. | - |
| P1 | [AR-0015](tasks/AR-0015.md): Pinned schema quality adapters | Implement JSON, YAML and JSON Schema adapters on the shared contract. | Add strict parser and schema-validation adapters with duplicate-key and draft/version fixtures. | - |
| P1 | [AR-0016](tasks/AR-0016.md): Huawei and MIT source-header compliance | Enforce exact Huawei 2026 and SPDX MIT headers across first-party AWQ source files. | Register the established SSH signing key with GitHub, review and merge product PR 4, then sync state-vendored coordinator source only from a released upstream version. | - |
| P1 | [AR-0018](tasks/AR-0018.md): Pinned Rust assurance profile and adapters | Add reviewed Rust formatting, lint, dependency, compatibility and advanced test evidence contracts. | Complete and release the three Rust child ARs, then verify the combined profile acceptance. | - |
| P1 | [AR-0019](tasks/AR-0019.md): Pinned Android and JVM assurance profile and adapters | Add reviewed Gradle, Kotlin, Android lint, dependency, ABI and UI-boundary evidence contracts. | Release verification complete; close AR-0019 and verify the AR-0005 umbrella acceptance. | - |
| P1 | [AR-0020](tasks/AR-0020.md): Pinned Rust stable PR gates | Add exact stable-toolchain formatting, Clippy, build, documentation and test contracts. | Create the signed DCO commit, publish its PR, and verify exact-head CI. | - |
| P1 | [AR-0021](tasks/AR-0021.md): Pinned Rust supply and API compatibility gates | Add dependency policy, advisory and public API compatibility contracts for Rust projects. | Implement after stable Rust PR contracts define the toolchain and fixture boundary. | - |
| P1 | [AR-0023](tasks/AR-0023.md): Deterministic release artifacts and manifest | Make wheel and source builds reproducible and bind them to a canonical offline-verifiable release manifest. | Promote and implement the deterministic build recipe, manifest schema, generator, verifier and hostile fixtures. | - |
| P1 | [AR-0024](tasks/AR-0024.md): Canonical SPDX SBOM and license inventory | Generate deterministic release SBOMs that identify AWQ, build inputs, licenses and artifact relationships. | Implement after AR-0023 fixes the release-manifest and artifact identity contracts. | - |
| P1 | [AR-0025](tasks/AR-0025.md): Signed provenance trust roots and verified updates | Bind release provenance to trusted identities and require verified local bundles before consumer lock updates. | Implement after AR-0023 and AR-0024 stabilize artifact and SBOM identities. | - |
| P1 | [AR-0029](tasks/AR-0029.md): Formal syntax and evidence contracts | Make formal-language checks precise and formal-evidence claims structured and truthful. | Coordinator independently reviews exact-head PR 26 at 89bc34e529c9dc77523a0316501eb255c3c43c8e; merge and release only after that review. | - |
| P2 | [AR-0006](tasks/AR-0006.md): Formal evidence and refactoring assurance | Model stateful quality semantics and add behavior-preserving refactoring evidence contracts. | Identify safety invariants, bounded models, counterexample fixtures and refactoring equivalence strategies. | - |
| P2 | [AR-0009](tasks/AR-0009.md): Property fuzz mutation and adversarial testing | Expand hostile testing beyond curated fixtures to generated and mutation-based assurance. | Select bounded generators and mutation operators for paths, policies, schemas, workflows and redaction. | - |
| P2 | [AR-0010](tasks/AR-0010.md): Performance flake and evidence-retention budgets | Define scalable runtime, determinism, flake and privacy-preserving retention budgets. | Establish representative repository-size fixtures and decompose performance, flake and retention controls. | - |
| P2 | [AR-0011](tasks/AR-0011.md): Agent onboarding distribution and compatibility | Make AWQ easy for new agents to adopt, update and diagnose across supported environments. | Design compatibility metadata, agent-readable recipes, migration fixtures and package distribution channels. | - |
| P2 | [AR-0022](tasks/AR-0022.md): Bounded Rust coverage fuzz and mutation evidence | Add bounded coverage, fuzzing and mutation contracts with explicit corpus, time and platform limits. | Push signed commit e32c5a3, open the PR, and verify hosted exact-head CI. | - |
| P2 | [AR-0026](tasks/AR-0026.md): Formal policy lifecycle and concurrency models | Extend bounded formal assurance to policy updates, exception renewal, tier transitions, freshness, rollback and concurrent crash recovery. | Define the finite lifecycle state, interleavings, recovery assumptions and counterexample corpus. | - |
| P2 | [AR-0027](tasks/AR-0027.md): Formal implementation refinement contracts | Bind bounded AWQ models to reviewed implementation refinement maps without overstating formal proof. | Define refinement-map schema, correspondence obligations, executable trace checks and hostile mismatch fixtures. | - |
| P2 | [AR-0028](tasks/AR-0028.md): Language-specific refactoring evidence adapters | Add reviewed collectors/adapters for language-specific characterization, differential, property and mutation evidence. | Select first supported language, define pinned tool and native-equivalence contracts, then add hostile fixtures. | - |
