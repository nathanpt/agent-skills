# ADR Red Team Skill Brainstorm

Status: **validated in pilot; prepared for publication.** All ten rubric items passed on 2026-09-26 UTC. The local OMP installation and model-role wiring are retained as the tested reference configuration.

## Purpose

One high-rigor, on-demand, read-only red-team review of an ADR/decision record together with its implementation plan, hard constraints, and the repository evidence behind its claims — without the overhead of a reviewer cohort or heavyweight process.

## Agreed decisions

- **One reviewer only.** The coordinator dispatches exactly one named task agent, `adr-red-team-reviewer`. No six-agent cohort, no consensus loop, no forced second round.
- **Model role versus agent.** The custom model role `reviewer` is an alias that routes the model; it is not an agent and spawns nothing. The coordinator invokes the named task agent; the skill is role-aware (coordinator prepares and dispatches; reviewer performs the review and never spawns).
- **v18.3.0 wiring.** Dispatch is one task call with required top-level `context` and exactly one item in `tasks`, whose `agent` is `adr-red-team-reviewer` and whose `task` asks for the review. The agent is installed at `~/.omp/agent/agents/adr-red-team-reviewer.md`; its `model: "@reviewer"` resolves through `modelRoles.reviewer` (`templates/model-role-reviewer.yml`). OMP v18.3.0 defines agent-frontmatter `autoloadSkills` as names of skills from the parent session injected into the child, so the parent must invoke/load `/skill:adr-red-team` before dispatch. Before dispatch the coordinator verifies the installed agent exists with `model: "@reviewer"` and that `modelRoles.reviewer` resolves to the intended independent reviewer model; absent, malformed, or unverifiable wiring stops the run with a reported gap — never an inline review or a silent fallback to the main model.
- **Pilot objective only: review quality over reviewer cost.** For this skill's pilot evaluation, review quality and result correctness outrank reviewer cost, while reviewer cost is still tracked; analytical rigor is not capped. This is a pilot-specific objective, not a general rule of the skill: the reusable instructions tell the reviewer to weigh trade-offs by the priorities explicitly stated for the decision and to mark priority as unknown when no ranking is stated. No fixed token cap.
- **Sources adapted, not copied.** ATAM, AWS Well-Architected, and Google SRE PRR appear as compact, selective lenses. No vendored third-party text; `references/source-index.md` keeps provenance.
- **Scope beyond ADR prose.** Review covers the decision record, implementation plan, hard-constraint/architecture documents, and only the relevant source/config/tests/incident evidence needed to validate material claims.
- **Child context is explicit.** The task agent receives no parent history; the coordinator supplies exact paths, decision goal, drivers, constraints, priorities, current state, and critical facts, recovering gaps from the repository before asking the user.
- **Proportionate depth.** Investigation expands only for material uncertainty or high-stakes gaps; low-impact reversible decisions get a lighter pass.
- **Test in OMP before publishing.** Fixture: the pre-red-team draft of Metope ADR 0008 at commit `cd55854` plus its supporting completed plan (`docs/exec-plans/completed/phase-2-experiment-2.md`) and relevant code. Running the pilot requires a temporary installation of this package in OMP; that copy exists only for the bounded evaluation and must be fully removed if any rubric item fails: uninstall the installed skill directory, delete `~/.omp/agent/agents/adr-red-team-reviewer.md`, and revert the `modelRoles.reviewer` overlay. Results are recorded only after the pilot runs.

## Local model mapping (this user's OMP test only)

The portable artifacts `templates/model-role-reviewer.yml` and `templates/adr-red-team-agent.md` keep the selector a placeholder. For the local OMP pilot, the model role `reviewer` maps to selector `openai-codex/gpt-6-sol` (catalog display name `GPT-6-Sol`) in this user's OMP configuration. This mapping is environment-specific and intentionally kept out of the portable skill instructions.

## Rejected alternatives

- **Six-agent reviewer cohort:** coordination overhead without a demonstrated rigor gain; one reviewer with targeted evidence access was chosen.
- **Forced second review round or consensus loop:** ceremony; re-examine only when material new uncertainty appears.
- **Fixed token cap:** caps rigor, not waste; proportionality rules do the real work.
- **Exhaustive Well-Architected or PRR checklists:** produces noise and generic findings; selective lenses with explicit selection rules instead.
- **Vendoring source pages:** repository policy forbids third-party text; original URLs stay authoritative in the source index.
- **Baking the local model selector into portable instructions:** breaks portability; placeholder in the template plus a separate local mapping note instead.

## Open questions

- Whether the coordinator should persist the report to a file on request; default is relay-only with no writes.
