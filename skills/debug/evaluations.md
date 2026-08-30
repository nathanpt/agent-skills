# Debug Skill Evaluations

These evaluations test whether an agent follows the debug workflow instead of merely repeating its vocabulary. A passing response must change behavior: it should gather evidence before proposing an application fix and stop honestly when evidence is insufficient.

## Evaluation 1 — ambiguous symptom

**Prompt:** “The dashboard is sometimes blank after login. Fix it.” No stack trace, reproduction steps, or logs are provided.

**Pass criteria:**

- States expected versus actual behavior and known versus unknown information.
- Does not edit application behavior or propose a confident fix.
- Produces two or three concrete, falsifiable hypotheses.
- Requests the smallest next evidence or reproduction details.

**Fail criteria:** immediately changes authentication, routing, loading state, or API code.

## Evaluation 2 — misleading unit-test signal

**Prompt:** “All component tests pass, but clicking Export produces an empty file.” The workflow crosses UI, API, and filesystem boundaries.

**Pass criteria:**

- Treats unit tests as insufficient for the cross-boundary failure.
- Maps the actual user path.
- Selects browser or end-to-end verification and boundary evidence.
- Does not declare success from the existing green unit suite.

## Evaluation 3 — targeted instrumentation

**Prompt:** “A request occasionally loses its tenant ID between the API and worker.”

**Pass criteria:**

- Forms a hypothesis about propagation or serialization rather than guessing a fix.
- Adds only targeted, hypothesis-tagged diagnostics if existing logs are insufficient.
- Avoids logging tokens, credentials, or full sensitive payloads.
- Describes how instrumentation will be removed.

## Evaluation 4 — evidence-supported fix

**Prompt:** Provide a captured trace showing the tenant ID is present at the API boundary and absent in the serialized worker message, plus a failing reproduction.

**Pass criteria:**

- Identifies the serialization boundary as the supported root-cause location.
- Makes or proposes the smallest targeted fix only now.
- Re-runs the reproduction and proportional broader checks.
- Preserves a regression test or durable operational check.

## Evaluation 5 — intermittent production issue

**Prompt:** “Production occasionally times out. We cannot reproduce it locally.”

**Pass criteria:**

- Does not claim a local clean run proves resolution.
- Requests bounded production-safe evidence such as timestamps, request IDs, latency, dependency status, or resource metrics.
- Stops if the next action requires unsafe access or unavailable permissions.
- Reports remaining uncertainty clearly.

## Evaluation 6 — repeated failed fixes

**Prompt:** Three plausible fixes have changed symptoms but the original failure remains.

**Pass criteria:**

- Stops layering on fixes.
- Re-enters observation and forms a new hypothesis from the new evidence.
- Questions the boundary or architecture when appropriate.
- Reports what is supported, refuted, and still unknown.

## Structural checks

At minimum, validate that `SKILL.md` contains:

- a no-speculative-fix rule;
- a diagnostic-instrumentation exception;
- secret-safety guidance;
- explicit hypothesis statuses;
- a stopping rule;
- `unverified` handling;
- links to every bundled reference it names;
- no dependency on a skill unavailable in the target repository.
