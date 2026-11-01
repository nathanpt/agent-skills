# ADR Red Team Source Index

Retrieved 2026-09-25 (local date). This skill adapts principles; no third-party article text is vendored or shipped. Local verification extracts exist only on the author's host for traceability and are not shipped with the skill; the original URLs remain canonical.

## SEI — Architecture Tradeoff Analysis Method (ATAM) collection

- URL: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection
- Adopted principle: business-driver primacy; quality scenarios as stimulus/context/response; sensitivity and trade-off points; explicit reporting of risks and non-risks.
- Application: `review-lenses.md` § ATAM (light). The full workshop, utility trees, and stakeholder brainstorming are deliberately not adopted.
- Local verification extract (author host only, not shipped): `~/.hermes/cache/web/www.sei.cmu.edu-eb07bf9a53.md`

## AWS Well-Architected Framework — overview

- URL: https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html
- Adopted principle: treat the pillars as a vocabulary of quality concerns to weigh, not a compliance checklist.
- Application: `review-lenses.md` § AWS Well-Architected (selective).
- Local verification extract (author host only, not shipped): `~/.hermes/cache/web/docs.aws.amazon.com-db54bd4996.md`

## AWS Well-Architected — evaluate operational priorities, tradeoffs, benefits, and risks

- URL: https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_eval_tradeoffs.html
- Adopted principle: weigh benefits against risks using explicit priorities; make trade-offs deliberate and recorded.
- Application: priority, probability/impact, and reversibility weighting rules in `review-lenses.md`.
- Local verification extract (author host only, not shipped): `~/.hermes/cache/web/docs.aws.amazon.com-2e472e5d28.md`

## AWS Reliability Pillar — design interactions in a distributed system to mitigate or withstand failures

- URL: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-interactions-in-a-distributed-system-to-mitigate-or-withstand-failures.html
- Adopted principle: probe failure interactions — dependency degradation, retry/amplification, partial failure, blast radius.
- Application: failure-interaction checks in `review-lenses.md`; feeds the PRR dependency and blast-radius questions.
- Local verification extract (author host only, not shipped): `~/.hermes/cache/web/docs.aws.amazon.com-d209df5bc1.md`

## Google SRE — Evolving SRE Engagement Model (Production Readiness Review)

- URL: https://sre.google/sre-book/evolving-sre-engagement-model/
- Adopted principle: PRR as a short, tailored question set over dependencies, failure behavior, observability, capacity, emergency/rollback controls, and change management.
- Application: `review-lenses.md` § Google SRE PRR. The full engagement/L documentation gate is not adopted.
- Local verification extract (author host only, not shipped): `~/.hermes/cache/web/sre.google-fc6c08f991.md`
