# Longshot

### Make the Interface Prove It.

**An independent agent skill for testing human-facing interfaces.** Longshot attempts realistic tasks, challenges design assumptions, and returns reproducible findings with recommendations you can verify.

[Visit the Website](https://jongos.github.io/Longshot/) · [Read the Skill](skills/longshot-human-centered-ui/SKILL.md) · [Validation](validation/rename-independent-role.md) · [Report an Issue](https://github.com/jongos/Longshot/issues)

Your design has a point of view. Give it a second pair of eyes.

A companion to **[Dazzler](https://github.com/jongos/Dazzler)** and **[Style Science](https://github.com/jongos/style-science)**: Dazzler creates and refines the interface; Style Science makes its design reasoning and constraints inspectable; Longshot independently tests the experience. Use them together or use Longshot on its own.

Longshot is deliberately skeptical of the happy path, including the one a designer or superuser prefers. It asks whether the interface supports the user's task, follows the evidence, and reports supported strengths as well as flaws. It does not manufacture criticism to look useful.

## What You Can Use It For

| Situation | What Longshot Investigates |
| --- | --- |
| Before shipping a workflow | Discoverability, terminology, choices, feedback and meaningful completion |
| A form or editor spans several screens | Draft preservation, navigation, interruptions and resuming work |
| A service says it is done | Whether the result is queued, acknowledged or actually verified |
| A task fails or gets cancelled | Actionable errors, recovery, undo and uncertain outcomes |
| The default interaction excludes someone | Relevant keyboard, focus, zoom, overflow and responsive behavior |
| The design team agrees too quickly | Counterexamples, unexplained constraints and alternatives to the prescribed route |

The intended benefit is a more actionable review: fewer unsupported assertions, clearer priorities, preserved safeguards and concrete acceptance tests. These are the skill's goals, not measured claims of improved human outcomes.

## Install and Invoke

With the [Skills CLI](https://skills.sh/docs):

```sh
npx skills add jongos/Longshot --skill longshot-human-centered-ui
```

Or copy `skills/longshot-human-centered-ui` into your agent's discoverable skills directory. For Codex, use `~/.codex/skills/longshot-human-centered-ui/`.

```text
Use $longshot-human-centered-ui to test creating a draft, consulting a
reference, and returning to finish it in this isolated demo. Challenge
the workflow. Report reproducible findings and acceptance tests.
Do not modify the application.
```

The skill's display name is **Longshot**. Its identifier is **longshot-human-centered-ui**. It replaces the earlier `human-centered-ui-review` identifier; remove an obsolete duplicate installation when upgrading. Automatic selection is enabled for interface testing and usability reviews, not ordinary fixes or factual questions.

Longshot needs a host agent with suitable browser or application tools and an authorized test environment. No separate runtime, paid model, Jev account or companion skill is required. Without interaction access, it can review supplied evidence, but must label the result as limited evidence review rather than a live walkthrough.

## How the Loops Work

Longshot specifies bounded review cycles carried out by the host agent:

1. **Attempt:** establish a user goal, authorized boundary and observable completion condition; try the rendered interface.
2. **Observe:** capture actions, states and results, distinguishing visual evidence from accessibility-tree, DOM or service evidence.
3. **Challenge:** consider an alternative route, interruption or competing explanation. Designer intent is context, not proof.
4. **Verify and report:** reproduce consequential issues where authorized, describe uncertainty, and recommend an observable acceptance test.

The cycle stops at the agreed scope, evidence limits or action boundary. An unavailable role is not a product defect. A timeout is not necessarily a failed operation. Never repeatedly submit an uncertain transaction.

A later fix-and-retest cycle requires separate implementation authorization. Longshot does not automatically redesign, run forever, schedule itself or approve its own changes. There is no hidden autonomous repair engine.

## What Comes Back

A report scaled to the request, with:

- Overall disposition, coverage limits and consequential findings first.
- Task/state, expected versus observed behavior, reproducible evidence and relevant authorized screenshots.
- Separate classifications for defects, usability concerns and aesthetic preferences; execution limits and cause attribution remain distinct.
- Severity and confidence with explanations, not a composite score that hides critical problems.
- Recommendations addressing the evidenced obstacle, useful behavior to preserve, and acceptance tests that could contradict the recommendation.
- Neutral follow-up tasks for actual human research.

**Illustrative finding:** a required reference screen clears a draft when the user returns. Recommend preserving the draft across navigation, retain the code-verification requirement, and test restoration. Do not claim that the stored record was permanently deleted unless the evidence establishes that. This example is synthetic.

See the [finding template](skills/longshot-human-centered-ui/references/finding-template.md) and [retained research](skills/longshot-human-centered-ui/references/research.md).

## Dazzler, Style Science and Longshot

| Project | Primary Responsibility |
| --- | --- |
| [Dazzler](https://github.com/jongos/Dazzler) | Designs, builds and refines interfaces and visual outputs. Dazzler styled this project's website. |
| [Style Science](https://github.com/jongos/style-science) | Makes design requirements, constraints and supporting evidence inspectable. |
| **Longshot** | Independently tests the experience, including whether declared requirements serve the user's task. |

They share an interest in evidence but do different jobs. Longshot has no runtime dependency on either companion.

## Why Longshot?

Longshot is one of creator Jon Gosier's favorite X-Men characters. Ann Nocenti and Art Adams introduced him in 1985: a luck-powered outsider rebelling against Mojo's entertainment empire. He and Dazzler become teammates and romantic partners; later stories reveal them as Shatterstar's parents.

That makes the companion name a personal comics connection as well as a useful metaphor: question the show and follow what actually happens. The software relies on evidence, not luck.

Sources: [Marvel's Longshot collection](https://www.marvel.com/comics/collection/46821/x-men_longshot_new_printing_trade_paperback), [character history and issue references](https://en.wikipedia.org/wiki/Longshot_(Marvel_Comics)). Independent project; not affiliated with or endorsed by Marvel or Disney. No Marvel artwork is included.

## Validation and Limits

Current validation includes structural checks and small synthetic text-packet exercises. The [original record](validation/RESULTS.md) and [rename/independent-role check](validation/rename-independent-role.md) state exactly what ran. They do not establish broad reliability on rendered applications.

Agent observations are not human participant evidence. Longshot cannot infer human confusion, satisfaction or success rates from its own behavior. Automated accessibility checks and agent keyboard tests do not constitute a complete accessibility assessment.

Review permission does not authorize private-content inspection, paid actions, production changes or deployment. Application changes require separate authorization.

## Contributing

Useful issues include a sanitized task, environment, reproduction steps, observed behavior and expected outcome. Mark simulated service behavior explicitly. Avoid private data, credentials and invented participant results. Include good control cases as well as failures; a new instruction should solve a demonstrated problem without expanding every review into an audit.

## License

Original skill instructions, documentation and website code: [MIT](LICENSE). Bundled Archivo font files retain their [SIL Open Font License](docs/fonts/archivo/OFL.txt) and notices. Character names and comics remain the property of their respective owners.
