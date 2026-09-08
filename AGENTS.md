# Worker entry point

Read `docs/DEVELOPMENT.md`, `docs/agent-workflow-coordinator.md`, the complete snapshot,
the selected task, and its plan before modifying the product. Claim exactly one ready task.
Route every product, Git, review, and publication mutation through `tools/handoffctl run`.

Do not patch vendored coordinator files. Do not store private evidence. Preserve signed,
DCO-certified, focused commits and publish product changes through reviewed pull requests.
