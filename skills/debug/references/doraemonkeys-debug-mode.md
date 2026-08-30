[Skip to content](#start-of-content)   
 

## Navigation Menu

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fdoraemonkeys%2Fclaude-code-debug-mode)

Appearance settings

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fdoraemonkeys%2Fclaude-code-debug-mode)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=doraemonkeys%2Fclaude-code-debug-mode)

Appearance settings

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

{{ message }}

[doraemonkeys](/doraemonkeys)   /  **[claude-code-debug-mode](/doraemonkeys/claude-code-debug-mode)**  Public

* [Notifications](/login?return_to=%2Fdoraemonkeys%2Fclaude-code-debug-mode)  You must be signed in to change notification settings
* [Fork 6](/login?return_to=%2Fdoraemonkeys%2Fclaude-code-debug-mode)
* [Star  111](/login?return_to=%2Fdoraemonkeys%2Fclaude-code-debug-mode)

[Branches](/doraemonkeys/claude-code-debug-mode/branches)[Tags](/doraemonkeys/claude-code-debug-mode/tags)

Open more actions menu

## Latest commit

## History

[15 Commits](/doraemonkeys/claude-code-debug-mode/commits/master/)

15 Commits

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| [debug-mode](/doraemonkeys/claude-code-debug-mode/tree/master/debug-mode "debug-mode") | [debug-mode](/doraemonkeys/claude-code-debug-mode/tree/master/debug-mode "debug-mode") |  |  |
| [LICENSE](/doraemonkeys/claude-code-debug-mode/blob/master/LICENSE "LICENSE") | [LICENSE](/doraemonkeys/claude-code-debug-mode/blob/master/LICENSE "LICENSE") |  |  |
| [README.md](/doraemonkeys/claude-code-debug-mode/blob/master/README.md "README.md") | [README.md](/doraemonkeys/claude-code-debug-mode/blob/master/README.md "README.md") |  |  |
|  |

## Repository files navigation

# Debug Mode Skill (Claude Code + Codex + Gemini CLI)

A hypothesis-driven debugging skill for [Claude Code](https://docs.anthropic.com/en/docs/claude-code), Codex, and [Gemini CLI](https://github.com/google-gemini/gemini-cli). Instead of blindly guessing fixes, it instruments your code with runtime logs, generates multiple hypotheses, and iteratively narrows down the root cause — with you in the loop.

Inspired by [Cursor's Debug Mode](https://www.cursor.com/blog/introducing-debug-mode).

## How It Works

```
Bug Report → Hypotheses → Instrument Code → Reproduce → Analyze Logs → Fix → Verify → Clean Up 
```

1. **Understand** — Gathers context about the bug (expected vs actual behavior, repro steps)
2. **Hypothesize** — Generates 3–5 testable hypotheses about root causes
3. **Instrument** — Adds targeted debug logging wrapped in `#region DEBUG` blocks
4. **Reproduce** — You trigger the bug while logs are collected to `.claude/debug.log`
5. **Diagnose** — Maps log output to hypotheses, confirms or rules out each one
6. **Fix** — Writes a minimal, targeted fix (not a refactor)
7. **Verify** — You confirm the fix works; if not, the cycle repeats
8. **Clean up** — Removes all instrumentation, leaving a clean diff

## Install

### One-liner (Claude Code)

```
# macOS / Linux / Windows (Git Bash / MSYS2) # ~ && ~# Claude Code discovers skills only ONE directory level under ~/.claude/skills/ ## (it does not recurse), but this repo keeps SKILL.md inside debug-mode/. Lift that ## folder up one level, otherwise the skill silently won't load: # ~ ~ ~
```

> **Why the extra step (Claude only):** Codex and Gemini scan `skills/` recursively, so they find `claude-code-debug-mode/debug-mode/SKILL.md` on their own. Claude Code looks only at the immediate children of `~/.claude/skills/`, so `SKILL.md` must sit exactly one level deep — `~/.claude/skills/debug-mode/SKILL.md`. With the nested path it loads no skill and reports no error, so the gap is easy to miss.

### One-liner (Codex)

```
# macOS / Linux / Windows (Git Bash / MSYS2) # ~ && ~
```

### One-liner (Gemini CLI)

```
# macOS / Linux / Windows (Git Bash / MSYS2) # ~ && ~
```

Or use the built-in install command:

```
gemini skills install https://github.com/doraemonkeys/claude-code-debug-mode.git
```

### Manual

1. Clone or download this repository into your skills directory:

   ```
   # Claude Code # cd ~ # Codex # cd ~ # Gemini CLI # cd ~
   ```
2. That's it. Skills are automatically discovered under `~/.claude/skills/`, `~/.codex/skills/`, and `~/.gemini/skills/`.

   For **Claude Code**, apply the same lift step as the one-liner above — move the inner `debug-mode/` folder up so `SKILL.md` lands at `~/.claude/skills/debug-mode/SKILL.md`. Codex and Gemini need no extra step.

### Verify installation

```
# Claude Code # ~ # Codex # ~ # Gemini CLI # ~ # or #
```

If the file exists, you're good to go.

## Usage

In Claude Code, Codex, or Gemini CLI, simply describe a bug and the skill will activate automatically. You can also invoke it explicitly:

```
/debug-mode Something isn't working — the API returns 200 but the data is empty 
```

Or just describe the problem naturally:

```
> The login page shows a blank screen after clicking submit. No errors in the console. 
```

The agent will follow the structured debug workflow — generating hypotheses, adding instrumentation, and asking you to reproduce the bug at each step.

## Don't Be Too Rigid — It's About Evidence, Not the Recipe

The skill describes one concrete path (write logs to a local `.claude/debug.log` via an absolute path), and that default works for **most** situations. But the workflow isn't a strict ritual — the real core is always the same two things:

1. **Reproduce** the bug.
2. **Collect evidence** (logs) from that reproduction and hand it back to the agent.

*How* the evidence gets collected and delivered is flexible. As long as the agent ends up with the logs from a real reproduction, the result is identical. A couple of common adaptations:

* **The default local-file path doesn't fit your runtime.** For example, the code runs on a phone (a mobile app), in a remote device, or anywhere it can't write to your project folder. No problem — have it log to a file *on that device*, reproduce there, then copy or paste those logs back to the agent. The transport changed; the workflow didn't.
* **The bug is intermittent / hard to trigger on demand.** You don't have to reproduce while the agent waits. Let the agent add the debug instrumentation up front, then just keep it in place and go about your work. Whenever the bug finally happens, grab the logs and drop them to the agent for analysis. Prepared-and-waiting works just as well as reproduce-on-the-spot.

When the standard flow fits, follow it. When it doesn't, keep the two core steps and adapt the rest — the agent can work with evidence from any source.

## Key Design Decisions

* **Logs go to `.claude/debug.log`** (absolute path), not stdout/stderr — keeps your terminal clean and avoids context window flooding
* **`#region DEBUG` markers** wrap all instrumentation for reliable, automated cleanup
* **Hypothesis-tagged logs** (`[DEBUG H1]`, `[DEBUG H2]`) map directly back to hypotheses for clear diagnosis
* **Human-in-the-loop** — the agent never removes instrumentation or declares victory until you confirm the fix

## Supported Languages

The `#region DEBUG` markers work with:

| Syntax | Languages |
| --- | --- |
| `// #region DEBUG` | JavaScript, TypeScript, Java, C#, Go, Rust, C, C++ |
| `# #region DEBUG` | Python, Ruby, Shell, YAML |
|  | HTML, Vue, Svelte |
| `-- #region DEBUG` | Lua |

```
# Claude Code # ~ # Codex # ~ # Gemini CLI # ~ # or #
```

## About

Cursor-style Debug Mode skill for coding agents. Hypothesis-driven debugging with runtime log instrumentation and human-in-the-loop verification.

### Resources

[MIT license](#MIT-1-ov-file)

### Stars

**111** stars

### Watchers

**1** watching

### Forks

[**6** forks](/doraemonkeys/claude-code-debug-mode/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fdoraemonkeys%2Fclaude-code-debug-mode&report=doraemonkeys+%28user%29)

You can’t perform that action at this time.

 