# Debug Skill Brainstorm

## Purpose

Create a reusable debugging mode that interrupts the agent's default tendency to choose the first plausible explanation, edit code immediately, and repeat the same theory after weak evidence.

The skill should turn ambiguous debugging into an evidence-collection loop:

```text
observe → map system → form bounded hypotheses → instrument or select diagnostics
→ reproduce → collect runtime evidence → update hypotheses
→ create/confirm regression reproduction → fix → verify → clean up
```

The skill is not primarily a better fix generator. It is an investigation protocol that makes unsupported certainty harder.

## Relationship to existing Hermes skills

`systematic-debugging` is an existing Hermes skill that provides the general root-cause discipline and four phases. This skill should be a specialized evidence-first mode for bugs that are ambiguous, runtime-dependent, intermittent, cross-component, or resistant to ordinary debugging.

- Use `systematic-debugging` for the broad no-fix-before-root-cause process.
- Use `debug` when the missing ingredient is runtime evidence, instrumentation, or a structured investigation record.
- Combine with `test-driven-development` when a failing regression test can be created before the fix.
- Use `python-debugpy` or other domain-specific Hermes skills when the runtime requires them.

Avoid duplicating every general debugging rule in the final skill. The new skill should add the evidence-collection machinery and explicit stopping behavior.

## Candidate invocation

```text
/debug <symptom, error, or reproduction description>
```

Natural-language debugging should also activate it when the issue is uncertain or prior fixes have failed.

## Initial response contract

Before editing production code, the agent should:

1. Restate expected versus actual behavior.
2. Identify what is known, unknown, and merely assumed.
3. Inspect the repository, relevant instructions, recent changes, logs, tests, configuration, and runtime entry points.
4. Inventory available debugging tools instead of pretending one tool fits all failures.
5. Determine whether the issue is reproducible, intermittent, environmental, or currently unverified.
6. Produce two or three independent, falsifiable hypotheses when the cause is not already established.
7. Give each hypothesis the evidence that would confirm or falsify it.

If there is insufficient evidence to justify a reproduction path, remain in diagnosis mode. Do not write a speculative fix.

## Evidence collection

For each relevant boundary, collect the smallest useful evidence:

- input entering the boundary;
- output leaving it;
- state transitions;
- configuration and environment propagation;
- timing, ordering, retries, and concurrency;
- external responses and error handling;
- resource lifecycle where relevant.

Use the least invasive available mechanism:

- existing logs and traces;
- test runner diagnostics;
- browser/devtools/network inspection;
- debugger breakpoints and watches;
- profilers and resource monitors;
- temporary targeted instrumentation;
- a minimal reproduction script or test.

Instrumentation must be:

- hypothesis-tagged;
- targeted rather than verbose logging everywhere;
- safe with respect to secrets and personal data;
- clearly marked for cleanup;
- isolated from permanent behavior where possible.

Prefer an ignored local artifact such as `.debug/` or the project’s established debug-log path. Do not commit captured secrets, tokens, credentials, personal data, or large runtime dumps.

## Investigation record

Use ephemeral investigation state by default. Keep observations, hypotheses, experiment results, and evidence in the active session unless there is a reason to preserve them.

For a non-trivial or multi-session investigation, create or update a project-approved persistent record such as `DEBUG.md`. Keep it concise:

```text
Symptom
Expected behavior
Actual behavior
Reproduction
Known facts
Unknowns
Hypotheses and status
Evidence collected
Current conclusion
Next experiment
Verification result
Cleanup status
```

Hypothesis states should be explicit: `unverified`, `supported`, `refuted`, or `confirmed`. Do not promote a hypothesis because it sounds plausible.

## Hypothesis loop

For each experiment:

```text
Hypothesis: what specific cause is being tested?
Prediction: what should be observed if it is true?
Experiment: what is the smallest diagnostic action?
Result: what actually happened?
Conclusion: supported, refuted, or inconclusive?
Next: what evidence is now required?
```

Never stack unrelated fixes while investigating. If an experiment changes production behavior, record the change and revert it before testing another hypothesis unless it is the intended fix.

## Reproduction and fix boundary

Do not fix until one of these is true:

- a failing test or reliable reproduction demonstrates the defect;
- runtime evidence isolates the failing component and the causal path is understood;
- the issue is an operational/configuration failure outside application code, and the evidence supports that conclusion.

When the root cause is established:

1. Create the narrowest regression test or durable check possible.
2. Make the smallest targeted fix.
3. Re-run the reproduction.
4. Run the proportional broader verification required by the changed boundary.
5. Ask for human confirmation when the final judgment depends on user experience, production behavior, or an intermittent condition the agent cannot observe.
6. Remove temporary instrumentation and verify the diff is clean of debug residue.

## Stopping rules

Stop and report instead of thrashing when:

- the bug cannot be reproduced and available evidence is exhausted;
- all current hypotheses are refuted;
- evidence points outside the repository or available permissions;
- the next diagnostic step is destructive, unsafe, credential-sensitive, or production-affecting;
- three targeted experiments fail to narrow the problem;
- repeated fixes alter symptoms without improving the causal explanation.

At a stopping point, report the evidence collected, hypotheses ruled out, remaining uncertainty, and the single best next evidence request. Do not manufacture certainty or continue making random edits.

## Output shape

```text
## Observations
## System path and boundaries
## Hypotheses
## Evidence plan
## Reproduction / instrumentation status
## Root-cause assessment
## Fix and verification
## Cleanup and remaining uncertainty
```

When the issue is still ambiguous, stop after Observations, System path, Hypotheses, and Evidence plan. A good debug session may end with a request for better evidence; that is progress, not failure.

## Design decisions settled

- **Name:** `debug`.
- **Investigation state:** ephemeral by default; use a persistent `DEBUG.md` or project-approved equivalent only for non-trivial or multi-session investigations.
- **Relationship:** specialize the existing Hermes `systematic-debugging` skill rather than duplicate it.

## Design decisions still open

- Should the skill ship helper scripts for log capture, or rely on existing tools first?
- How should debug artifacts be ignored without modifying `.gitignore` unexpectedly?
- What tool inventory should be standard across Linux, macOS, and Windows?
- Should human confirmation be required before cleanup, as Cursor’s Debug Mode does?
- How should this skill invoke or reference `systematic-debugging` without creating competing phase orders?
