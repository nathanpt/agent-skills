---
name: adr-red-team
description: On-demand read-only architecture and ADR red-team review.
version: 0.1.0
author: Nathan (nathanpt)
license: MIT
platforms: [linux, macos, windows]
metadata:
  tags: [architecture, adr, review, risk-analysis, red-team]
---

# ADR Red Team

**Validated:** the bounded OMP pilot passed all ten rubric items on 2026-09-26 UTC. The installed reviewer agent and `modelRoles.reviewer` mapping are now the tested local wiring; keep them aligned with the templates when updating the package.

One high-rigor, read-only red-team review of an architecture decision record (ADR) and its supporting material. Runs on demand in the main coordinator, which dispatches exactly one named task agent, `adr-red-team-reviewer`, routed through the custom model role `reviewer`. No reviewer cohorts, consensus loops, forced second rounds, or fixed token caps.

## When to use

Use this skill for consequential architecture and system-design decisions: an ADR, its implementation plan, or a material design choice, reviewed before acceptance or commitment. It is not routine PR or style review.

## Roles

This skill is role-aware. Determine which role you are in before acting:

- **Coordinator (main OMP session):** prepare and dispatch the review. Never perform the review inline; never spawn more than one reviewer.
- **Reviewer (the `adr-red-team-reviewer` task agent, which autoloads this skill):** perform the review yourself. You are the only reviewer; never spawn another reviewer or any task.

The model role `reviewer` is an alias that routes the model; it is not an agent and spawns nothing. The coordinator dispatches the named task agent. See `templates/model-role-reviewer.yml` and `templates/adr-red-team-agent.md`.

## Coordinator workflow

### 1. Collect context

The child agent receives no parent conversation history. The dispatch's required top-level `context` must be self-contained:

- exact repository paths: the ADR/decision record, its implementation plan, project hard-constraint and architecture documents, plus the specific source/config/test files and incident evidence that bear on material claims;
- decision goal and business drivers;
- stated constraints, priorities, and non-goals;
- current state: what is deployed or implemented versus what is proposed;
- critical facts the reviewer cannot recover from files.

If essential context is missing, inspect repository sources first. Ask the user only when the gap cannot be recovered from the repository. Do not infer decisions from unstated priorities; record them as unknowns instead.

### 2. Dispatch

The `adr-red-team` skill must be loaded in this session before dispatch: `autoloadSkills: [adr-red-team]` injects skills from the parent session into the child, so invoke `/skill:adr-red-team` first if it is not already active.

Make exactly one task call — required top-level `context`, exactly one item in `tasks`, whose `agent` is `adr-red-team-reviewer` and whose `task` asks for the review. The collected context from step 1 goes in `context`; target paths and any user-stated focus or urgency go in `task`:

```
context: <self-contained review context from step 1>
tasks:
  - agent: adr-red-team-reviewer
    task: <review request: target paths, user-stated focus or urgency>
```

Custom-agent dispatch selects the named agent installed from `templates/adr-red-team-agent.md` as `~/.omp/agent/agents/adr-red-team-reviewer.md` (tools `read`, `grep`, `glob` only, no task-spawning tool, `thinking-level: high`). Its `model: "@reviewer"` resolves through `modelRoles.reviewer` from `templates/model-role-reviewer.yml`; the role routes the model only and is not an agent.

**Verify the wiring before dispatch; fail closed.** Confirm that `~/.omp/agent/agents/adr-red-team-reviewer.md` exists with `model: "@reviewer"` in its frontmatter, and that `modelRoles.reviewer` in the merged OMP configuration resolves to the intended independent reviewer model. If the agent is missing or malformed, the role is absent or unmapped, or the effective model cannot be verified, stop and report the wiring gap to the user. Never perform the review inline and never fall back silently to the main model.

### 3. Relay

Relay the reviewer's report to the user. Do not edit the ADR or plan, implement fixes, approve the decision, or make external calls. Changes and acceptance belong to the user.

## Reviewer workflow

1. **Read the scope:** the decision record first, then the implementation plan, constraint/architecture documents, and the targeted evidence named in the task context. Expand investigation with read/grep/glob only where a material claim is unverified or a high-stakes gap appears.
2. **Steelman first:** restate the decision and its objective in their strongest form, grounded in the stated drivers. Challenge only after the steelman.
3. **Apply lenses selectively** per `skill://adr-red-team/references/review-lenses.md` (read it before reviewing):
   - **ATAM, light:** derive the important business drivers and prioritized quality scenarios (stimulus/context/response); probe sensitivity and trade-off points; report material risks AND non-risks. Do not reproduce full workshop or utility-tree overhead.
   - **AWS Well-Architected, selective:** weigh benefits against risks using the priorities explicitly stated for the decision, plus probability/impact and reversibility. If no priority ranking is stated, surface the trade-offs and mark priority as unknown; never substitute a default ranking. Do not burden low-impact, reversible decisions with full six-pillar depth.
   - **Google SRE PRR, when operationally relevant:** dependency behavior, failure/blast radius, observability, capacity, emergency fallback/rollback, change management, and relevant incident/postmortem evidence. Tailor the checklist to the service.
4. **Findings bar:** every finding is specific and evidenced in repository material. State severity, confidence, exact evidence path/line, failure scenario, consequence, and a mitigation or question. Separate fact from assumption and missing evidence. Distinguish decision-invalidating blockers from non-blocking improvements. Collapse duplicates. Never convert a generic best practice into a finding without a connection to stated drivers, project constraints, or a concrete failure scenario.
5. **Proportionality:** depth scales with stakes, irreversibility, and uncertainty. No finding quota: "no material concern found" is a valid result.
6. **Stay read-only:** never edit the ADR or plan, implement fixes, approve the decision, or contact anything external. Return findings only.

## Report format

Compact by default; expand only enough to make each finding verifiable and actionable:

1. **Assessment** — one paragraph.
2. **Steelman** — the decision at its strongest, with its drivers.
3. **Prioritized findings** — severity, confidence, evidence path/line, scenario/impact, mitigation or question; blockers first.
4. **Strengths and non-risks** — what was checked and holds.
5. **Material unknowns** — missing evidence, stated as questions.
6. **Bottom line** — proceed / proceed with mitigations / revisit; the user decides.

## References

- `skill://adr-red-team/references/review-lenses.md` — compact ATAM / Well-Architected / PRR synthesis and lens-selection rules. The reviewer must read this before reviewing.
- `references/source-index.md` — source provenance; third-party text is not vendored.
- `templates/adr-red-team-agent.md` — dispatchable named-agent template; installed as `~/.omp/agent/agents/adr-red-team-reviewer.md`.
- `templates/model-role-reviewer.yml` — `modelRoles.reviewer` overlay behind the `@reviewer` alias.
- `evaluations.md` — pass/fail rubric for the OMP pilot; fixture and status inside.
- `BRAINSTORM.md` — design decisions, local model mapping, rejected alternatives.
