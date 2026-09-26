# Review Lenses

Compact, actionable synthesis of three frameworks. Select lenses by relevance to the stated drivers, constraints, and failure surface; never apply all of them exhaustively. Depth scales with stakes, impact, and reversibility.

## Selection rules

1. Read the decision record, plan, and constraints first; list the material claims and the quality attributes the drivers prioritize.
2. Pick only the probes that can change the verdict or reveal a material risk. Skip lenses, pillars, and questions with no connection to this decision.
3. A generic best practice is not a finding. Report only what exposes a concrete failure scenario tied to the drivers, constraints, or evidence.
4. Report non-risks (checked, holds) alongside risks; this is what keeps the review proportionate.

## ATAM (light)

Adopted: business-driver primacy, quality scenarios, sensitivity/trade-off points, explicit risks and non-risks. Not adopted: full workshop, utility trees, stakeholder scenario brainstorming.

- Derive the important business drivers and the prioritized quality scenarios as stimulus/context/response triplets (e.g., "peak write load / under current replica topology / p99 latency stays within SLO").
- Probe sensitivity points (choices that strongly affect one quality attribute) and trade-off points (choices that move multiple attributes in opposite directions).
- Report material risks AND non-risks, each tied to a scenario.

## AWS Well-Architected (selective)

Adopted: benefits-versus-risks trade-off framing, priority weighting, failure-interaction thinking. Not adopted: exhaustive six-pillar checklist.

- Use pillars as targeted probes only where the decision touches them (operational excellence, reliability, security, cost optimization, performance efficiency, sustainability as relevant).
- Weigh each benefit against its risk using the priorities explicitly stated for the decision, plus probability/impact and reversibility. If no priority ranking is stated, surface the trade-offs and mark priority as unknown; never substitute a default ranking.
- For distributed-system decisions, check failure interactions: retry and amplification behavior, backpressure, cascading failure, partial-failure behavior, and what callers experience when a dependency degrades.
- Do not impose full-pillar depth on low-impact, reversible decisions.

## Google SRE PRR (when operationally relevant)

Adopted: tailored production-readiness questioning. Not adopted: the full engagement and documentation gate process.

Ask only when the decision has operational surface:

- Dependencies: what happens when each dependency is slow, degraded, or down?
- Failure and blast radius: what fails together, and what limits the blast radius?
- Observability: which metrics, dashboards, and alerts distinguish this decision's failure modes?
- Capacity: headroom and scaling behavior under the prioritized scenarios.
- Emergency controls: fallback, kill switches, rollback; who can trigger them and how fast?
- Change management: rollout order, canary/validation, and what would invalidate the decision.
- Incident evidence: what past incidents or postmortems bear on the claims?

## Finding calibration

- Severity: blocker (decision-invalidating), major (must mitigate before or during rollout), minor (non-blocking improvement).
- Confidence: high (repository evidence), medium (strong inference), low (assumption).
- Every finding carries: exact path/line, failure scenario, consequence, and a mitigation or question.
- Label each load-bearing item as verified fact, assumption, or missing evidence; never silently promote one into another.
