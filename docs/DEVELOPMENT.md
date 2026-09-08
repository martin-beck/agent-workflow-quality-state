# Coordinated development

Agent Workflow Quality development uses the vendored Agent Workflow Coordinator in this repository.
The sibling product checkout is `../agent-workflow-quality`; isolated task worktrees use the task's
declared key and branch.

## Start or recover

1. Verify `coordinator.vendor.json` and the permanent binding.
2. Inspect processes, worktrees, branches, commits, pull requests and CI before retrying interrupted work.
3. Run `tools/handoffctl reconcile --commit --push`, then `tools/handoffctl snapshot`.
4. Read the selected task and plan completely.
5. Claim one dependency-ready open task with a stable unique owner.

```sh
tools/handoffctl claim AR-NNNN --owner WORKER_ID --lease-minutes 120
```

## Mutation boundary

Run every product-file, Git, GitHub, review, test, build and publication mutation through:

```sh
tools/handoffctl run --owner WORKER_ID AR-NNNN -- COMMAND ARGUMENTS
```

Use exact paths and scoped staging. Preserve unrelated work. Commits must be SSH-signed and contain
a `Signed-off-by` trailer matching the author. Product changes reach `main` only through a reviewed
pull request. Never weaken or regenerate a policy, threshold, exception, baseline or evidence record
merely to make a gate pass.

## Verification

Run focused tests during development and the complete applicable gate on the exact candidate tree.
Validate deterministic generation, schemas, negative fixtures, privacy, dependency pins, evidence,
Git diff cleanliness, commit signatures, DCO, pull-request checks and the merged main revision.

The product may use public repository and CI identifiers as evidence. Never record tokens, private
paths, hostnames, prompts, transcripts, raw logs, environment contents or machine-local configuration.

## Update and completion

After every material result or failure, update the task with the exact current revision and a concise
result. Heartbeat before lease expiry. After interruption, inspect durable effects before retrying.

Release a task as done only after the pull request is merged, main is green, public documentation is
rendered, installation and CLI behavior are verified from a fresh checkout, and all acceptance criteria
in the task plan are proven.

```sh
tools/handoffctl release AR-NNNN --owner WORKER_ID --status done --note "Verified outcome"
tools/handoffctl reconcile --commit --push
tools/handoffctl doctor --live
```
