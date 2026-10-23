# Longshot

**An agentic tester for human-facing interfaces.** Longshot attempts realistic tasks, examines feedback and recovery, and turns observed UI/UX problems into prioritized, testable recommendations. It is a companion to [Dazzler](https://github.com/jongos/Dazzler) and [Style Science](https://github.com/jongos/style-science), with no runtime dependency on either.

Longshot tests interfaces; it does not automatically redesign or modify applications. Its observations are agent-based expert inspection, never fabricated human participant research.

## Install and invoke

Copy `skills/human-centered-ui-review` into your agent's discoverable skills directory (for Codex, `~/.codex/skills/`). The skill identifier is `human-centered-ui-review`; its display name is Longshot. Automatic selection is enabled for interface tests and usability reviews, not ordinary fixes or factual questions.

```text
Use $human-centered-ui-review to test the primary journey in this isolated demo, including keyboard access and recovery. Report evidence and acceptance tests; do not modify the application.
```

## What it delivers

- Task-based evidence, with clear distinctions among observed defects, usability concerns and aesthetic preferences.
- Coverage limits, prioritized findings, recovery checks and acceptance tests.
- A plan grouped by user outcome and neutral tasks for subsequent human research.

See [the skill](skills/human-centered-ui-review/SKILL.md), [research and limitations](skills/human-centered-ui-review/references/research.md), and [finding format](skills/human-centered-ui-review/references/finding-template.md). Existing authorized browser/testing tools provide interaction; no custom testing runtime is included.

See [validation](validation/RESULTS.md) for synthetic evaluation scope and limitations. Synthetic evidence tests do not establish human usability or reliability against every application.

The name is a nod to the Marvel/X-Men character. This independent project is not affiliated with Marvel or Disney.
