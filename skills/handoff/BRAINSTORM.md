# Handoff Skill Brainstorm

## Purpose

Create a portable, trustworthy handoff that lets a fresh agent or different harness continue active work without access to the original conversation.

A handoff is not a generic summary and is not ordinary context compaction. It is useful when work must travel to another session, directory, repository, harness, agent, colleague, or parallel branch.

## Candidate invocation

```text
/handoff [what the next session or agent is for]
```

The argument matters. A handoff written for “verify the existing implementation and finish the remaining work” must preserve different context from one written for “continue implementing the API.”

## Core contract

A handoff must:

- state the next agent’s exact job;
- preserve the current work state and intended direction;
- distinguish verified facts from assumptions and inherited claims;
- point to existing files, plans, ADRs, issues, diffs, and URLs instead of duplicating them;
- preserve decisions, rejected alternatives, subtle exceptions, numerical defaults, and implementation order when they are load-bearing;
- name blockers, approvals, open decisions, and non-goals;
- end with one safe, concrete first action;
- remain useful when read cold by an agent with no conversation access.

## Create versus resume

The skill should support two explicit modes.

### CREATE

1. Read the user’s destination/purpose for the handoff.
2. Inspect repository state and gather facts from tools rather than memory.
3. Identify the source of truth for each major claim.
4. Write a compact handoff to an appropriate path.
5. Self-audit for omitted constraints, rejected options, and unverified claims.
6. Report the exact path and how to pass it to the next agent.

### RESUME

1. Read the handoff completely before acting.
2. Verify project path, branch, commit, worktree, and working-tree state.
3. Re-check stale or unverified claims against the repository and runtime.
4. Read referenced source-of-truth artifacts before relying on the handoff.
5. Resolve blockers and approvals before taking side effects.
6. Start with Immediate Next Action #1.

A handoff is a snapshot, not authority. The resume agent must not treat a claim as verified merely because it appears in the document.

## Verified versus unverified state

Every load-bearing claim should be tagged or clearly classified:

```text
[verified: command and result, or file/source evidence]
[unverified: claim not checked in this session]
[assumption: working belief requiring confirmation]
[decision: chosen path and rationale]
```

Capture a repository anchor where available:

```text
project path
branch
HEAD SHA
working-tree status
worktree list
relevant PR/issue/URL
capture timestamp
```

Do not launder inherited claims from an older handoff, issue, plan, or conversation. Re-check them or preserve their uncertainty.

## Handoff document structure

Use a compact structure such as:

```text
# Handoff: <purpose>

## Fresh-agent warning
## Destination and exact job
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

Do not copy entire specs, diffs, logs, or transcripts into the handoff when a stable path or URL exists. If the conversation itself contains the only specification, enumerate the decisions rather than hiding them behind “see conversation.”

## Transfer and fork

The handoff should support two destinations:

- **Transfer:** the current session is ending or moving to another harness/directory.
- **Fork:** another agent receives the handoff while the current session continues.

The document should state which mode applies, what workspace the recipient should use, and whether the current agent must remain untouched.

## Safety and side effects

A handoff must state side-effect gates explicitly:

- whether the next agent may edit files;
- whether it may commit, push, open issues, or open PRs;
- whether production, credentials, external services, or destructive operations require user approval;
- which unrelated dirty files must be preserved.

Never include secrets. Redact credentials, tokens, cookies, private keys, and sensitive personal data. Reference their secure location without copying values.

## Proactive use

The skill is user-invoked by default. It may recommend a handoff when:

- the user is ending a substantial session;
- work is moving to another harness or directory;
- a parallel agent needs the current state;
- context is stale or overloaded;
- a major milestone leaves meaningful work in flight.

Do not turn every normal phase boundary into a handoff. If work remains in the same harness and directory, ordinary compaction or a project progress file may be more appropriate.

## Design decisions settled

- **Name:** `handoff`.
- **Default mode:** user-invoked; do not create handoffs for every ordinary phase boundary.
- **Modes:** support both `CREATE` and `RESUME`, including transfer and fork use cases.
- **Default storage:** OS temporary directory because the default handoff is a transit document.
- **Naming:** timestamp plus purpose slug.
- **Durability:** use a project-local or user-selected path only when explicitly requested or needed for a long-lived handoff.
- **Verification:** capture repository state with tools and distinguish verified facts from assumptions.
- **Suggested skills:** include a section naming useful skills for the receiving agent.
- **User guide:** keep bundled guidance at `references/usage.md`; a root `README.md` can be added later if the skill package needs standalone browsing documentation.

## Design decisions still open

- What exact tool commands should establish the repository anchor across Git and non-Git projects?
- How much automatic staleness checking is worth implementing before a real use case proves it necessary?
- What minimum self-audit should be required before finalizing a handoff?
