---
name: debug
description: Investigate ambiguous bugs with runtime evidence first.
version: 0.1.0
author: Nathan (nathanpt), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [debugging, root-cause, runtime-evidence, instrumentation]
    related_skills: []
---

# Debug Skill

Use this skill as an evidence-first debugging mode for ambiguous, runtime-dependent, intermittent, cross-component, or repeatedly misdiagnosed failures.

The goal is to identify the failing boundary and causal path before changing application behavior. Do not optimize for a plausible fix; optimize for a supported explanation.

## When to use

Use for:

- vague or incomplete bug reports;
- failures not explained by the stack trace alone;
- intermittent, timing, race-condition, or concurrency failures;
- performance, memory, resource-lifecycle, or environment failures;
- cross-component failures where isolated tests pass;
- regressions with unclear cause;
- repeated fixes that change symptoms without resolving the issue.

For an obvious isolated failure, use the smallest evidence and verification process that can support the claim.

## Non-negotiable rules

1. **No speculative application fixes.** Do not change application behavior until runtime evidence or a reliable failing reproduction supports the root-cause assessment.
2. **Diagnostic instrumentation is not a fix.** Temporary instrumentation is allowed when it is the smallest useful experiment. Mark it clearly and remove it afterward.
3. **Separate facts from assumptions.** Label observations, hypotheses, predictions, results, and conclusions.
4. **Keep hypotheses bounded.** Produce two or three concrete, independent, falsifiable hypotheses when the cause is uncertain.
5. **Test one variable at a time.** Do not stack unrelated changes while investigating.
6. **Protect sensitive data.** Never log passwords, API keys, tokens, cookies, private user data, or unnecessary request bodies.
7. **Do not manufacture certainty.** Report unavailable or inconclusive evidence as `unverified`.
8. **Stop before thrashing.** Repeated unsuccessful experiments require a new direction, more evidence, or human judgment—not random edits.

## Workflow

### 1. Establish the incident

Record or extract:

- expected behavior and actual behavior;
- exact errors, stack traces, timestamps, and affected requests;
- reproduction steps and frequency;
- environment, version, configuration, and dependency details;
- recent changes;
- previous attempts and their effects.

Inspect repository instructions, entry points, tests, configuration, logs, recent history, and runtime boundaries. Do not assume the reported component is the failing component.

If the report is too vague to identify a useful path, remain in diagnosis mode and request the smallest missing evidence.

### 2. Map the system path

Trace the request, event, job, or data value:

```text
trigger → boundary → component → boundary → component → observable result
```

For each relevant boundary, state what should enter, what should leave, and what state or configuration must be preserved. Consider UI/API, API/service, service/database, configuration/runtime, process/provider, container/host, browser/backend, and worker/scheduler boundaries as applicable.

### 3. Form bounded hypotheses

For each hypothesis, record:

```text
Hypothesis: specific proposed cause
Why: evidence making it plausible
Location: likely files, components, or boundary
Prediction: what should be observed if true
Falsifier: what would rule it out
Experiment: smallest safe distinguishing action
Status: unverified | supported | refuted | confirmed
```

Do not edit application behavior merely because one hypothesis is familiar or likely.

### 4. Collect evidence

Use the least invasive available source, in roughly this order:

1. Existing logs, traces, metrics, and error reports.
2. Focused tests with verbose output.
3. Repository history, configuration, and runtime checks.
4. Browser/network tools, debuggers, profilers, or resource monitors.
5. A minimal reproduction script or failing test.
6. Temporary targeted instrumentation.

Use the project’s established commands and tools. Record the exact command or interaction and relevant result. See `references/instrumentation.md` for instrumentation rules.

### 5. Instrument only to distinguish hypotheses

If current evidence cannot distinguish the hypotheses, add the smallest diagnostic instrumentation that can. It may capture boundary inputs/outputs, state transitions, timing, ordering, resource lifecycle, or configuration propagation.

Instrumentation must be targeted, hypothesis-tagged, secret-safe, clearly marked for removal, and written to the project-approved local diagnostic path when one exists. Do not scatter logging throughout the repository or introduce a new observability stack without need.

For remote, mobile, intermittent, or inaccessible runtimes, adapt the evidence transport. Reproduction and evidence from the real failure path remain mandatory.

### 6. Reproduce and update conclusions

Run the smallest safe reproduction. For each hypothesis, record what the result supports, rules out, and leaves unknown. A clean run that did not trigger the failure is not proof of a fix.

A supported root-cause assessment identifies the failing component or boundary, causal input/state/configuration, propagation path, and explanation for the reported symptom.

### 7. Create a durable reproduction

Once the failure path is credible, create the narrowest durable check possible:

- regression test;
- integration test;
- end-to-end scenario;
- diagnostic script;
- operational/configuration check.

Make it fail before the application fix when practical. If not, document why and preserve the captured evidence.

### 8. Fix only the established cause

After evidence supports the root cause:

1. State the assessment and supporting evidence.
2. Make the smallest targeted application change.
3. Avoid unrelated refactors or cleanup.
4. Re-run the durable reproduction.
5. Run broader verification proportional to the changed boundary.
6. Obtain human confirmation for user-visible, production, or intermittent behavior the agent cannot fully observe.

If the fix fails, return to observation and form a new hypothesis. Do not layer on another speculative fix.

### 9. Verify and clean up

Before completion:

- reproduce the original failure path with the fix;
- run relevant unit, integration, or end-to-end checks;
- test important failure behavior, not only the happy path;
- remove temporary instrumentation and diagnostic residue;
- inspect the diff for secrets, debug markers, accidental behavior changes, and unrelated edits;
- preserve a `DEBUG.md` only for a substantial or multi-session investigation;
- report skipped or unavailable verification as `unverified`.

## Stopping rules

Stop modifying application behavior and report when:

- the failure cannot be reproduced and available evidence is exhausted;
- current hypotheses are refuted;
- evidence points outside the repository or available permissions;
- the next step is destructive, production-affecting, or credential-sensitive;
- three targeted experiments have failed to narrow the problem;
- fixes change symptoms without improving the causal explanation;
- required human confirmation is unavailable.

A stopping report must identify evidence collected, hypotheses supported/refuted, the current best explanation, remaining uncertainty, and the single best next evidence request. See `references/evidence-and-stopping.md` for the detailed format.

## Persistent investigation record

Keep state ephemeral by default. For substantial or multi-session investigations, create or update a project-approved `DEBUG.md` using the structure in `references/investigation-record.md`. Do not turn it into a permanent diary; retain only decisions, evidence, regression protection, and operational risk that remain useful.

## Output format

When the issue is ambiguous, stop after:

```text
## Observations
## System path and boundaries
## Hypotheses
## Evidence plan
```

After investigation:

```text
## Observations
## System path and boundaries
## Hypotheses and evidence
## Root-cause assessment
## Reproduction
## Fix
## Verification
## Cleanup and remaining uncertainty
```

Always distinguish `confirmed by evidence`, `supported but not confirmed`, `refuted`, and `unverified`.

## References

- `references/instrumentation.md` — safe temporary instrumentation and evidence transport.
- `references/investigation-record.md` — persistent `DEBUG.md` template.
- `references/evidence-and-stopping.md` — experiment table and stopping-report format.
- `references/source-index.md` — source material behind this workflow.
