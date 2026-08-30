# `/handoff` Usage Guide

`handoff` writes a portable context document for a fresh agent, different harness, different directory, colleague, or parallel workstream.

It is for moving active work. It is not a replacement for ordinary conversation compaction when the work is staying in the same session, harness, and directory.

## Create a handoff

Invoke it with the purpose of the receiving session:

```text
/handoff Have a fresh agent verify the current implementation and finish the remaining work
```

The purpose controls what the skill preserves. A handoff for implementation, review, debugging, or deployment should emphasize different evidence and next actions.

The skill will:

1. Inspect the current repository and session state.
2. Capture the project path, branch, commit, working-tree state, and relevant artifacts where available.
3. Separate verified facts from assumptions and unverified claims.
4. Preserve decisions, rejected alternatives, constraints, exceptions, open decisions, and implementation order that matter to the destination task.
5. Reference existing files and URLs instead of copying their contents.
6. Write a timestamped, purpose-slugged handoff to the OS temporary directory by default.
7. Return the exact file path and a copy-pasteable instruction for the receiving agent.

## Resume from a handoff

Start the new session by pointing it at the file rather than pasting the whole document into a shell command:

```text
Read `/path/to/handoff.md` completely. Verify its repository and runtime claims against the current workspace, then begin with Immediate Next Action #1.
```

The receiving agent should verify:

- project path and branch;
- current HEAD and working-tree state;
- referenced files, plans, ADRs, issues, and URLs;
- assumptions marked `unverified` or `assumption`;
- blockers and approval gates;
- whether the destination workspace matches the handoff.

A handoff is a snapshot, not unquestionable authority.

## Transfer versus fork

### Transfer

Use when the current session is ending or work is moving to another harness, directory, or agent.

```text
/handoff Continue this implementation in a fresh OMP session
```

### Fork

Use when another agent should take a side task while the current session continues.

```text
/handoff Investigate the database timeout independently and return evidence without changing the main implementation
```

The handoff must state the destination workspace, whether the current session remains active, and which side effects are allowed.

## Storage

The default location is the operating system temporary directory because a handoff is normally a transit document. Temporary storage may be cleared, so copy the file to a durable project or user location when:

- the receiving session will not start soon;
- the handoff must survive a reboot;
- the destination cannot access the original temp directory;
- the handoff is being retained as a project artifact.

Do not place temporary handoffs in the repository by default. Use a project-local path only when the user requests durability or the work requires a shared artifact.

## What belongs in the document

Include:

- exact destination job;
- current in-flight state;
- verified facts and evidence;
- unverified claims and assumptions;
- decisions with rationale;
- rejected alternatives;
- load-bearing constraints and exceptions;
- files, paths, commits, issues, plans, ADRs, and URLs;
- blockers and required approvals;
- non-goals;
- immediate next action;
- verification status and remaining uncertainty.

Do not copy:

- credentials, tokens, cookies, private keys, or secrets;
- full logs when a path and relevant excerpt are sufficient;
- complete specs, diffs, or plans already stored elsewhere;
- irrelevant conversation history.

If the conversation is the only source of a decision, preserve the decision directly rather than saying “see the previous conversation.”

## Handoff versus other continuity tools

| Situation | Use |
|---|---|
| Same work, same harness, new context window | Compaction or the harness’s continuation feature |
| Work moves to another session, harness, directory, or agent | `/handoff` |
| Another agent investigates a side question while you continue | `/handoff` in fork mode |
| Durable project state that remains true after the task | Project docs, progress file, ADR, or feature list |

## Safety

The handoff must state whether the receiving agent may:

- edit files;
- run services or tests;
- use credentials or external systems;
- commit or push;
- open issues or pull requests;
- perform destructive operations.

Side effects not explicitly authorized remain gated. Never use the handoff as a way to smuggle approval for commits, pushes, production changes, credential use, or destructive commands.
