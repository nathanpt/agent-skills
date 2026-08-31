---
name: handoff
description: Transfer active work to a fresh agent with verified context.
version: 0.1.0
author: Nathan (nathanpt), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [handoff, continuity, session-transfer, agent-coordination]
    related_skills: []
---

# Handoff Skill

Create or resume a portable handoff for work moving to another session, harness, directory, agent, colleague, or parallel workstream.

A handoff is not a generic summary and is not ordinary context compaction. Its purpose is to move active work without making the receiving agent reconstruct the important state from scratch.

## When to use

Use when:

- a fresh agent or different harness must continue the work;
- work is moving to another directory, repository, or machine;
- another agent is taking a side investigation while the current session continues;
- the current context is stale or overloaded and the work must travel;
- the user asks to save state, create a handoff, or resume from one.

Do not create a handoff for every normal phase boundary. If the work remains in the same harness and directory, use the harness’s continuation or compaction mechanism unless portability is needed.

## Modes

Determine the mode before acting:

- **CREATE:** capture the current work for a receiving session or agent.
- **RESUME:** load an existing handoff, verify its claims, and continue from its first safe action.
- **TRANSFER:** the current session is ending or moving elsewhere.
- **FORK:** another agent receives the handoff while the current session continues.

If the user gives a purpose, preserve that purpose in the document. If no purpose is given, ask what the receiving agent is expected to do rather than writing a directionless summary.

## Non-negotiable rules

1. Capture state from tools and artifacts, not memory alone.
2. Separate verified facts, unverified claims, assumptions, decisions, and open questions.
3. Preserve rejected alternatives, subtle exceptions, numerical defaults, and implementation ordering when they affect future work.
4. Reference existing specs, plans, ADRs, issues, diffs, logs, and URLs instead of copying them.
5. If the conversation is the only source of a decision, preserve that decision directly.
6. State the receiving agent’s exact job and one immediate safe next action.
7. Never include credentials, tokens, cookies, private keys, or sensitive personal data.
8. Do not grant side-effect approval implicitly. State whether edits, commits, pushes, production actions, credential use, or destructive operations are allowed.
9. Treat a handoff as a potentially stale snapshot. A receiving agent must verify it before acting.
10. Do not claim completion from an unverified inherited claim.

## CREATE workflow

### 1. Define the destination

Write down:

- destination purpose and exact job;
- transfer or fork mode;
- destination project, directory, branch, or worktree;
- whether the current session continues;
- allowed and prohibited side effects.

### 2. Capture current state

Inspect the available repository and runtime state. For Git projects, capture:

```text
state as of: timestamp
project path
handoff id and predecessor path/hash, if any
branch
HEAD SHA
git status
git worktree list
changed-file inventory
relevant PRs or issues
```

A new hop must create a fresh anchor after its own work. Preserve the predecessor’s identity, but do not inherit its path, branch, SHA, file count, or completion claims as current. The receiver compares the recorded anchor with the live workspace before acting.

Record commands as compact receipts (`command → exit/result`) and point to saved artifacts for long output. Do not paste full logs when a short verified claim and a re-checkable path are sufficient. If a fact was not checked, mark it `unverified` or `assumption`.

### 3. Enumerate the work

Preserve:

- current in-flight work;
- decisions and rationale;
- rejected alternatives and why they lost;
- load-bearing constraints and exceptions;
- open decisions and who must decide them;
- non-goals and scope boundaries;
- source-of-truth artifacts;
- remaining work in priority order;
- risks and remaining uncertainty.

Do not flatten a design discussion into conclusions only. Re-scan for exceptions signaled by words such as “unless,” “except,” “only if,” and “but.”

### 4. Gate operational claims

Any claim that directs the receiver to use a command, model, provider, route, service, port, permission, or integration is an operational claim. Tag each load-bearing claim:

```text
[verified: command/source + result + date]
[unverified: what still needs checking]
[assumption: why it is believed]
```

Before making an unverified operational claim the receiver’s immediate path, verify it against the live system or authoritative source. If it cannot be verified safely, label it and make the next action a verification step—not a confident instruction. Do not turn a recommendation into evidence.

### 5. Write the handoff

Write one Markdown file to the OS temporary directory by default. Use a timestamp plus a purpose slug. Use a project-local or user-selected path only when durability or shared access is explicitly needed.

Use this structure:

```markdown
# Handoff: <destination purpose>

## Fresh-agent warning
## Destination and exact job
## Mode and side-effect gates
## Current state
## Verified facts and evidence
## In-flight work
## Decisions and rationale
## Rejected alternatives
## Load-bearing constraints and exceptions
## Source-of-truth artifacts
## Files and paths
## Blockers and approvals
## Open decisions
## Non-goals
## Immediate next action
## Remaining work
## Verification status
## Risks and uncertainty
## Handoff metadata
```

Keep it compact. Point to existing artifacts rather than duplicating their contents. Do not refer to an inaccessible conversation as the source of required information.

### 6. Self-audit and report

Before finalizing, ask:

```text
If a fresh agent had only this document, what would it ask before acting?
Which load-bearing claims did I not verify?
Which decision, exception, rejected option, or approval gate could be lost?
```

Resolve those omissions or mark them explicitly. Re-scan the file for secrets and unresolved placeholders. Report the exact file path, mode, destination job, verification anchor, and first action for the receiving agent.

## RESUME workflow

### 1. Read before acting

Read the entire handoff and identify its destination job, mode, side-effect gates, immediate next action, and source-of-truth artifacts.

### 2. Verify drift

Check:

- project path, branch, worktree, and current HEAD;
- current working-tree changes and conflicts;
- recorded state timestamp, handoff id, predecessor link/hash, and changed-file inventory;
- referenced files, plans, ADRs, issues, and URLs;
- environment and runtime assumptions;
- every `unverified` or `assumption` claim that affects the next action;
- every operational claim needed for the immediate path;
- whether blockers or approvals have changed.

For a chain, treat every predecessor as historical input. Reconcile it against the newest handoff and live workspace, then create a fresh state anchor before making new claims.

If the handoff is stale or conflicts with the repository, stop and report the conflict before modifying files.

### 3. Start safely

Read the primary source-of-truth artifact first, then begin with Immediate Next Action #1. Do not redo completed work merely because the handoff is unclear; verify the claim and continue from the current state.

If the handoff is part of a chain, read the newest handoff first and consult predecessors only for context the newest one references.

### 4. Continue the handoff chain when needed

During a long continuation, update the existing handoff or create a new timestamped handoff that links to its predecessor. Mark superseded handoffs clearly. Do not leave multiple active handoffs with contradictory next actions.

## Output format

For CREATE, report:

```text
Handoff created: <exact path>
Mode: <transfer | fork>
Destination job: <one sentence>
Verification anchor: <branch/SHA/status or not applicable>
Side-effect gates: <summary>
Receiving agent’s first action: <one action>
Unverified items: <list or none>
```

For RESUME, report:

```text
Handoff loaded: <path>
Freshness: <current | drift detected | stale>
Verified before action: <items>
Conflicts or blockers: <list or none>
Starting action: <one action>
```

## References

- `references/usage.md` — user-facing CREATE, RESUME, transfer, fork, storage, and safety guide.
- `references/source-index.md` — research sources and adopted principles.
