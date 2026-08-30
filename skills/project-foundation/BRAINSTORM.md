# Project Foundation Skill — Brainstorm

**Status:** Draft only. Do not install, invoke, commit, or publish yet.

## Working name

`project-foundation` is tentative. It may be renamed after the source research and the boundary with `harness-bootstrap` are settled.

## Proposed purpose

Create the smallest useful foundation for a new or early-stage project repository so future agents can discover the project quickly without loading one oversized `AGENTS.md` file.

## Likely durable outputs

- `AGENTS.md` — short routing and operating contract
- `ARCHITECTURE.md` — system purpose, stack, entry points, boundaries, and stable relationships
- `PROGRESS.md` — current state, active work, verification status, and open items
- `CHANGELOG.md` — user-visible or project-significant changes
- Repository-specific source/test/CI scaffolding only when the project actually needs it

## Boundary with harness-bootstrap

- `project-foundation`: new project or thin/early repository; establish the initial foundation.
- `harness-bootstrap`: existing repository; inspect and reconcile what is already there, preserve stronger references, and avoid duplicate or generator-owned context.
- A foundation run should hand off to bootstrap/reconciliation once the repository has meaningful existing structure.

## Proposed durable repository layout

The first source supports a short root map plus a structured `docs/` knowledge store. The foundation skill should scaffold this layout when the project is substantial enough to benefit from progressive disclosure:

```text
AGENTS.md
ARCHITECTURE.md
docs/
├── design-docs/
│   ├── index.md
│   ├── core-beliefs.md
│   └── ...
├── exec-plans/
│   ├── active/
│   ├── completed/
│   └── tech-debt-tracker.md
├── generated/
│   └── ...
├── product-specs/
│   ├── index.md
│   └── ...
└── references/
    └── ...

DESIGN.md
FRONTEND.md
PLANS.md
PRODUCT_SENSE.md
QUALITY_SCORE.md
RELIABILITY.md
SECURITY.md
CHANGELOG.md
PROGRESS.md
```

Do not create every file as empty ceremony. The skill should:

- Create the directories and index files that match the project type.
- Create `ARCHITECTURE.md`, `PROGRESS.md`, and `CHANGELOG.md` when each has a distinct question to answer.
- Create `DESIGN.md`, `FRONTEND.md`, `PRODUCT_SENSE.md`, `QUALITY_SCORE.md`, `RELIABILITY.md`, and `SECURITY.md` only when the project actually has that surface.
- Put execution plans under `docs/exec-plans/active/` and move completed plans to `docs/exec-plans/completed/` rather than leaving stale active plans.
- Put generated schemas, API maps, or reports under `docs/generated/`, with the generating command and ownership recorded.
- Put external technical references and source notes under `docs/references/`; link to originals rather than copying third-party prose into project guidance.
- Keep `AGENTS.md` as a short table of contents and operating contract, not a duplicate of the docs store.

The output should be progressive disclosure: a new agent reads the short root map, follows the relevant link, and loads only the context needed for the task.

- What belongs in `AGENTS.md` versus `ARCHITECTURE.md`, `PROGRESS.md`, and `CHANGELOG.md`?
- How short should the top-level routing file remain?
- How should generated regions and project-specific conventions be detected?
- When should the skill create nothing beyond a minimal README and source layout?
- How should the skill handle an existing repository with partial, stale, or conflicting documents?
- What must be verified before a foundation is considered complete?
- Should the skill create a change log from day one, or only when there are meaningful user-facing changes?

## Verification layer — proportional evidence

Verification depth should match the boundary changed. The foundation skill should not demand a full end-to-end run for every typo or isolated helper, but it must prevent agents from treating unit tests or a successful process start as proof that a cross-component feature works.

| Change surface | Minimum evidence |
|---|---|
| Documentation only | Link, format, and repository checks |
| Pure utility or isolated logic | Focused unit tests |
| Module or service interaction | Integration tests |
| API/database/configuration boundary | Integration plus migration/runtime checks as applicable |
| UI or user workflow | End-to-end browser or real-client verification |
| Deployment or environment change | Start the real service and exercise the affected path |

For cross-component changes:

- Define the relevant architectural boundaries before writing the E2E check.
- Test the real user or system path, including important failure behavior.
- Treat passing unit tests as necessary but insufficient evidence.
- Make failure output state what failed, why it matters, and how to fix it.
- Promote recurring review or runtime defects into tests, lints, or other executable checks.
- Record the exact command and observed result; a green report without the command is not evidence.

E2E tests provide integrated evidence; they do not prove the absence of all defects. The skill should require the strongest practical evidence for the changed boundary and explicitly mark skipped or unavailable verification as unverified.


For projects with meaningful architectural, data, security, deployment, dependency, or user-visible tradeoffs, strongly recommend a versioned MADR decision layer:

```text
docs/
└── decisions/
    ├── README.md
    ├── 0001-first-decision.md
    └── ...
```

This layer is optional for tiny projects. Do not create ADR scaffolding merely to satisfy a template.

The decision process should be trigger-based, not calendar-based. Create or update an ADR when a choice will constrain future implementation, operations, security, data handling, dependencies, interfaces, or user-visible behavior.

Each decision record should capture:

- Context and problem statement
- Decision drivers
- Considered options
- Decision outcome
- Consequences, including rejected alternatives
- Confirmation evidence after implementation
- Status such as proposed, accepted, deprecated, or superseded

The foundation skill should add an `AGENTS.md` route such as:

> For decisions that affect architecture, interfaces, data storage, security, deployment, dependencies, or major user-visible behavior, create or update an ADR in `docs/decisions/`. Read relevant existing ADRs before changing a decision they constrain.

When a decision changes, preserve the old record and mark it superseded by a new ADR. Do not silently rewrite decision history. Keep minor implementation preferences and routine edits out of the decision log.


The entry file should remain a router, not an encyclopedia. Target roughly 50–200 lines, with the shortest useful version preferred.

It should contain only:

1. **Project overview** — one or two sentences explaining what the repository is.
2. **Quick start** — exact setup, test, check, and run commands discovered from the repository or chosen during initialization.
3. **Global hard constraints** — a small, prioritized set of non-negotiable rules. Do not dump every preference or historical lesson here.
4. **Topic-document map** — one-line links with applicability conditions, such as “read `docs/database-rules.md` when changing database operations.”
5. **Completion contract** — what must be verified and what the agent must report before considering work complete.

Every topic document should answer:

- What subject does this cover?
- When does it apply?
- What source or decision supports it?
- What commands or checks verify it?
- When can it be removed or revised?

Historical lessons should become tests, constraints, or concise references—not an ever-growing incident diary in `AGENTS.md`.


The foundation skill should distinguish the first run from later runs:

### Initializer pass

- Inspect the user’s goal and repository type.
- Create the minimum project scaffold and repository-local knowledge map.
- Create a repeatable `init.sh` or equivalent startup/check command when the project has a runnable application or service.
- Create a structured feature list when the project has multiple user-visible or testable requirements. Prefer machine-readable status fields such as `passes: false` over a prose checklist that agents can casually rewrite.
- Make the initial git commit only if the user has authorized commits; otherwise leave a clear uncommitted foundation and report that boundary.

### Subsequent coding passes

- Read `AGENTS.md`, the relevant architecture/progress sources, recent Git history, and the feature list before coding.
- Run the startup/check command and verify the existing baseline before adding another feature.
- Select one highest-priority failing feature or one explicitly assigned task.
- Implement incrementally rather than attempting the whole project in one context window.
- Verify the feature end-to-end where possible, including browser or real-client behavior for applications.
- Update progress and feature status only from observed evidence.
- Leave a clean, understandable handoff state for the next context window: no unrelated broken work, undocumented half-implementations, or ambiguous next step.

### Feature list as a harness primitive

When a project has multiple user-visible or testable requirements, create a machine-readable feature list in the repository. It should be the shared scope contract for the initializer, coding agent, verifier, scheduler, and handoff—not a memo that agents can rewrite casually.

Each feature should include:

- stable identifier
- category or area
- concise behavior description
- ordered verification steps
- explicit `passes: false` or equivalent state
- optional priority and dependency fields when the project needs them

The foundation skill should instruct later agents to:

- select one highest-priority failing feature at a time;
- avoid declaring the project complete because scaffolding or visible UI exists;
- change feature status only after the listed checks pass;
- never delete or weaken a feature to make the project appear complete;
- keep implicit requirements from conversations, TODOs, and plans synchronized with the feature list or deliberately remove them.

Use JSON or another machine-readable format when the project has enough scope to justify it. For a tiny project, a feature list may be unnecessary ceremony.
The skill should treat `PROGRESS.md`, Git history, and the feature list as complementary:

- `PROGRESS.md`: narrative current state, decisions, blockers, and next move.
- Feature list: machine-checkable requirements and pass/fail state.
- Git history: recoverable implementation history and clean rollback points.
- `init.sh`: repeatable environment startup and baseline verification.

Do not require all four for every tiny project. The initializer should create them when the project’s duration, complexity, or number of requirements justifies them.

## Initial design stance

- Inspect before creating.
- Prefer one clear source of truth per question.
- Keep `AGENTS.md` short and route agents to deeper files.
- Do not create files merely to satisfy a template.
- Do not invent architecture, test commands, progress, or project goals.
- Treat generated files and existing conventions as ownership boundaries.
- Record actual verification, not assumed verification.
- Keep the first run reversible and easy to review.

## Source links to add later

The user will provide OpenAI, Anthropic, and other reference links. Add them to a skill-local `references/source-index.md` rather than copying third-party prose into the skill.
