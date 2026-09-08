# Agent Workflow Quality State

This public repository stores bounded coordination state for
[Agent Workflow Quality](https://github.com/martin-beck/agent-workflow-quality).
It vendors the independently released
[Agent Workflow Coordinator](https://github.com/martin-beck/agent-workflow-coordinator)
for offline, version-pinned operation.

Read `docs/DEVELOPMENT.md`, then use `tools/handoffctl` for claims, mutations,
verification records, recovery, and publication. Never edit generated views directly.

Tracked state contains concise tasks, plans, revisions, checkpoints, and public evidence.
It must never contain credentials, prompts, transcripts, raw command output, private paths,
hostnames, machine configuration, or unrelated personal information.

Verify the vendored coordinator and project state with:

```sh
python3 tools/handoffctl_vendor.py verify --target .
tools/handoffctl doctor
tools/handoffctl snapshot
```

Licensed under the MIT License.
