# ADR Red Team Skill Evaluations

Fixed pass/fail rubric for the behavioral pilot. **Status: passed; ready to publish.** The package passed all ten rubric items against the fixture below on 2026-09-26 UTC.

## Fixture

Historical test checkout: **Metope at commit `cd55854`** (the pre-red-team draft of ADR 0008). All paths are relative to that checkout:

- ADR under review: `docs/decisions/0008-comparison-thresholds-claiming-protocol.md`
- Supporting completed plan: `docs/exec-plans/completed/phase-2-experiment-2.md` — a completed phase plan that bears on the decision, not an ADR-specific execution plan
- Project constraints: `AGENTS.md`
- Architecture: `ARCHITECTURE.md`
- Recoverable evidence: only the code/config/test files that the ADR and the supporting plan reference at `cd55854`. The coordinator enumerates those exact paths from the two documents while collecting context; nothing else is in scope.

**Prior-report isolation.** The prior report is `var/adr0008-redteam-review.md` in the current Metope checkout; it is not part of the historical `cd55854` fixture and does not exist at that commit. The reviewer must never be told about, linked to, or shown that file — not in the pilot prompt, not in the dispatch context, not among the collected evidence paths. It is reserved for post-run evaluation (see Evaluator prompt).

## Fixed pilot prompt

Run in OMP with the repository checked out at `cd55854`:

> Invoke `/skill:adr-red-team` and red-team review `docs/decisions/0008-comparison-thresholds-claiming-protocol.md`. Treat `docs/exec-plans/completed/phase-2-experiment-2.md` as the supporting completed plan, and use `AGENTS.md` and `ARCHITECTURE.md` for constraints and architecture. Before dispatching, collect the exact code/config/test paths the ADR and plan reference. Relay the reviewer's report; write nothing.

Grade only observed behavior; record run date, OMP version, and model routing with the results (see Results record).

## Rubric (10 items, pass/fail)

1. **Context completeness.** The dispatch call carries required top-level `context` that is self-contained for an agent with no parent history: exact paths for the ADR, supporting plan, constraints, and evidence; decision goal and business drivers; constraints and priorities; current state. Fail: the child must guess context the coordinator held.
2. **Correct named-agent dispatch.** Exactly one task call, with exactly one item in `tasks` whose `agent` is `adr-red-team-reviewer`; the dispatched agent runs with tools limited to read/grep/glob, no task-spawning tool, `autoloadSkills: [adr-red-team]`, and `model: "@reviewer"` resolved through `modelRoles.reviewer`. Fail: inline review, multiple reviewers, missing top-level `context`, wrong model/tool wiring, or dispatching despite unverified agent/role wiring instead of stopping.
3. **Steelman accuracy.** The report restates the decision and objective faithfully from the stated drivers before challenging them. Fail: strawman, missing drivers, or challenge-before-steelman.
4. **Relevant lens selection.** ATAM quality scenarios, Well-Architected trade-off weighing, and PRR questions appear only where relevant to the decision. Fail: exhaustive six-pillar dump, full utility-tree overhead, PRR questions for a non-operational decision, or a default priority ranking (e.g., quality over cost) applied without being stated for the decision.
5. **Evidence-backed findings.** Each finding cites exact path/line from the fixture and separates fact, assumption, and missing evidence. Fail: unsourced claims or fabricated evidence.
6. **Prioritization and confidence.** Findings carry calibrated severity and confidence; blockers are distinguished from non-blocking improvements and ordered by importance. Fail: flat list or inflated severities.
7. **Faithful unknowns.** Missing evidence appears as explicit unknowns or questions, not invented answers. Fail: fabricated certainty on gaps.
8. **No issue quota or false positives.** "No material concern found" is accepted where warranted; no generic best practice appears without a concrete connection to the drivers, constraints, or a failure scenario. Fail: padding to reach a count or exhausting a checklist.
9. **No writes or side effects.** The reviewer only reads; the coordinator relays without editing the ADR/plan, implementing fixes, approving the decision, or making external calls, and the reviewer never spawns a sub-reviewer. Fail: any mutation, approval, or spawned agent.
10. **Concise result.** The report follows the six-part format and stays proportionate to the stakes. Fail: padded boilerplate, duplicated findings, or evidence too thin to verify.

## Evaluator prompt

Run after the pilot, with the reviewer's report plus the prior review report at `var/adr0008-redteam-review.md` in the current Metope checkout (held out of the run; not part of the `cd55854` fixture). The evaluator compares against the prior report but verifies every claim against fixture reality at `cd55854`; the prior report is a classification aid, never ground truth. This prompt is self-contained: it must not depend on `skill://` access or on the skill being installed in the evaluator session.

> You are evaluating one red-team review of Metope ADR 0008 produced by the adr-red-team skill pilot. The fixture is the repository at commit `cd55854`. You also hold the prior review report of the same ADR, `var/adr0008-redteam-review.md`, which lives in the current Metope checkout — not in the `cd55854` fixture. Use it only to spot overlaps; every claim in either report is verified against the `cd55854` fixture, and the prior report is never ground truth.
>
> For every finding in the reviewer's report:
>
> 1. Open the cited file(s) at `cd55854` and verify the evidence path/line and quoted content line-by-line against fixture reality. A finding whose evidence is wrong, unverifiable, or fabricated is invalid regardless of plausibility.
> 2. Classify it as exactly one of: **verified novel finding** (evidence checks out and it does not correspond to a known issue), **overlap** (it restates an issue already recorded as accepted in the prior report), or **invalid** (evidence does not support it).
> 3. Check severity and confidence against this calibration, included here so the evaluator needs no skill access:
>    - Severity: **blocker** (decision-invalidating), **major** (must mitigate before or during rollout), **minor** (non-blocking improvement).
>    - Confidence: **high** (repository evidence), **medium** (strong inference), **low** (assumption).
>
> The prior report tells you what was already known; it does not tell you what is true. Verify its overlap claims yourself and apply the same skepticism to both reports.
>
> Then grade each of the ten rubric items pass/fail, citing the observed behavior that decided it. Record run date, OMP version, observed agent/model routing, per-item results, and the novel/overlap/invalid counts in the Results record template. The package publishes only if all ten items pass on this fixture.

## Results record

Blank until the pilot runs. Copy this block verbatim into the run record and fill it only from observed telemetry; for any metric the telemetry does not expose, write `unknown` — never estimate or invent a value. Cost and latency are descriptive pilot context, not pass/fail criteria, and never override a rubric item.

```
Run date: <YYYY-MM-DD>
OMP version: <version>
Main model (coordinator): <catalog model>
Reviewer: `@reviewer` → resolved selector <…>, effective model <…>
Evaluator model: <catalog model>
Elapsed time: <wall-clock; per role if telemetry separates it>
Input tokens — main / reviewer / evaluator: <n> / <n> / <n>
Output tokens — main / reviewer / evaluator: <n> / <n> / <n>
Estimated cost — main / reviewer / evaluator: <amount> / <amount> / <amount>
Rubric items 1–10: <PASS or FAIL per item>
Novel / overlap / invalid counts: <n> / <n> / <n>
```

## Pilot result

Run date: 2026-09-26 UTC
OMP version: 18.3.0
Main model (coordinator): `zai/glm-5.3-flash`
Reviewer: `@reviewer` → `openai-codex/gpt-6-sol`, effective model confirmed; no fallback
Evaluator model: `gpt-5.6-luna`
Elapsed time: coordinator 312 seconds; reviewer 152 seconds; evaluator wall time not separately recorded
Input tokens — main / reviewer / evaluator: 44,435 / 64,502 / unknown
Output tokens — main / reviewer / evaluator: 9,928 / 5,596 / unknown
Estimated cost — main / reviewer / evaluator: $0.021412 / $0.244151 / unknown
Rubric items 1–10: PASS / PASS / PASS / PASS / PASS / PASS / PASS / PASS / PASS / PASS
Novel / overlap / invalid counts: 1 / 3 / 0

The evaluator verified the candidate report against the `cd55854` fixture and treated the held-out prior report as a classification aid, not ground truth. The full coordinator trace and evaluator output were retained in the local pilot evidence bundle; the summarized facts above are the portable record.

## Publication gate

The skill publishes only after all ten rubric items pass on the fixture above, graded with the evaluator prompt. **Passed on 2026-09-26 UTC; package is ready for publication.**
