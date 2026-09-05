# Grill-Me Source Index

## Agent Skills format

- [Agent Skills README](https://github.com/agentskills/agentskills/blob/main/README.md) — establishes the folder-based skill format and progressive disclosure model. Adopted: keep `SKILL.md` as the executable control loop and put research/evaluations in separate files.
- [Agent Skills specification](https://agentskills.io/specification) — defines required frontmatter and recommended size/structure. Adopted: valid `name`/`description` metadata and optional supporting files.

## Primary skill examples

- [Matt Pocock `grill-me` wrapper](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md) — minimal user-facing entry point. Adopted conceptually: explicit invocation and separation between entry point and interview mechanism; rejected as the sole implementation because it is not standalone.
- [Matt Pocock `grilling` primitive](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grilling/SKILL.md) — defines the design tree, dependency-aware frontier, round format, fact/decision split, and confirmation gate. Adopted: frontier ordering, recommendations, environment fact-finding, and no action before confirmation. Adapted: one question by default with a small independent batch for speed.
- [Matt Pocock `grill-me` guide](https://raw.githubusercontent.com/mattpocock/skills/main/docs/productivity/grill-me.md) — describes stateless use, scope control, prototype boundaries, and the danger of passive agreement or very long sessions. Adopted: stateless default, risk-based stopping, and prototype escape hatch.
- [Incubyte `grill-me`](https://raw.githubusercontent.com/incubyte/ai-plugins/main/bee/skills/grill-me/SKILL.md) — emphasizes depth-first follow-up, inspecting code instead of asking for known facts, and explicit handling of vague answers. Adopted selectively: branch depth and fact/decision separation; rejected tool-specific and repository-log instructions.
- [Satya Janghu `grill-me`](https://raw.githubusercontent.com/satya-janghu/agent-skills/main/skills/grill-me/SKILL.md) — emphasizes recommendations, hidden assumptions, alternatives, and logging. Adopted: recommendation/strawman questions and explicit assumption/alternative coverage; rejected automatic log writes for portability.

## Boundary and critique

- [Josh Wheelock `grill-me` submission tests](https://raw.githubusercontent.com/joshuawheelock/grill-me/main/docs/submission-tests.md) — repository-quiz behavior and read-only tests. Used as a boundary: implementation-grounded quizzing is a distinct skill, not the cross-domain `/grill-me` contract.
- [AIHero: The `/grill-me` Skill](https://www.aihero.dev/skills-grill-me) — practical discussion of scope, ungrillable questions, context-window drift, and session continuation. Adopted: split oversized work, stop for prototypes, and avoid endless sessions.
- [Dominic Wild: Grill Me, the Skill That Cooks Your Brain](https://blog.dominicwild.com/blogs/grill-me-brain-cooking) — critique of outsourcing critical thinking to agent-supplied questions. Adopted countermeasure: keep decisions with the user, show recommendations as strawmen rather than authority, and require explicit confirmation.
