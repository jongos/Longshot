![Longshot](docs/longshot-readme.svg)

# Longshot

**UI/UX Testing for Agents**

Give Longshot an interface. It selects important tasks, follows the journeys and reports what works, what gets in the way and how to verify a fix. Want to direct the review? Supply your user roles and workflows.

## The Problem

An app can pass its technical tests and still be hard to use. A save button may save one thing while another save button saves something else. A choice may be buried under a big text box. A draft may be gone when you leave and come back.

Someone has to try the task the way a person would.

## What This Does About It

Longshot is a skill: a folder of instructions you add to an AI agent. Give it an app or a website. It picks the important tasks and works through them step by step. Then it reports what works, what gets in the way and how to check a fix.

Each problem comes with the starting point, the steps taken, what happened and a test that shows when it is fixed. You can tell it which kinds of users and tasks matter most.

It is an AI agent doing the checking. It is not a study with real people.

**Example.** In one reported case, an agent found that “Photos” opened a picture generator instead of a gallery, and that two save buttons did different things. The maintainer says normal tests had missed these. This is the maintainer’s account, not measured results.

## Put It to Work

- **Before shipping:** test whether someone can find and complete a core task.
- **After an interruption:** check whether drafts, choices and context survive leaving and returning.
- **When “done” is unclear:** distinguish a success message from a result that can actually be found and used.
- **Beyond the default path:** examine relevant keyboard, zoom and narrow-screen conditions.

Each finding includes the starting state, actions, observed result and an acceptance test.

Longshot looks for hidden choices, unclear action scope, lost context and terminology that makes the task harder. These checks follow the workflow you need tested.

> Longshot was particularly useful because it shifted the question from “Does the app work?” to “Does the experience make sense to someone trying to create a scene?”

— Agent feedback supplied by the maintainer. [Read the reported scene-creation case study and review example](examples/scene-creation-case-study.md).

On follow-up reviews, Longshot retests the original problem and tracks resolved, recurring and untested findings. [See how comparisons work](skills/longshot-human-centered-ui/references/report-continuity.md).

## Give It a Goal

[Guide a review](GUIDANCE.md): examples for roles, workflows, priorities and success criteria, from a single sentence to a complete brief.

**Automatic by default:** Longshot chooses relevant journeys from the interface and context. **Guided when you want:** define roles, workflows, priorities or success criteria. Provide as much or as little direction as you need.

```sh
npx skills add jongos/Longshot --skill longshot-human-centered-ui
```

```text
Use $longshot-human-centered-ui to test this app using the supplied
test account. Choose the important workflows and report obstacles.
Do not modify the app.
```

For a guided review: “Test the editor role creating and resuming drafts, and the reviewer role approving or returning them. Prioritize preserving work. Use the supplied test accounts; skip administration.”

Longshot also checks successful journeys for hidden workarounds and whether important decisions explain their consequences. Recommendations connect the observed obstacle to a specific change, a check that it helped, and a check that useful behavior still works. A displayed shortcut is not reported as tested until it has been exercised.

Use a compatible agent with authorized browser or application access. [Read the skill](skills/longshot-human-centered-ui/SKILL.md) for the review method and [setup details](REFERENCE.md#install-and-invoke) for alternatives.

[Visit the website](https://jongos.github.io/Longshot/) · [See an example report](REFERENCE.md#a-finding-you-can-act-on)

## Part of the Hex Men Collection

[Hex Men](https://github.com/jongos/Hex-Men) is a directory of independent projects by Jon Gosier. Each project stands on its own; these are its members.

| Project | What It Does |
|---|---|
| [Hex Men](https://github.com/jongos/Hex-Men) | Directory of independent projects |
| [Dazzler](https://github.com/jongos/Dazzler) | Create and refine expressive visual interfaces |
| **Longshot** (this repository) | Independently test rendered UI tasks and provide replayable evidence |
| [Style Science](https://github.com/jongos/style-science) | Provide inspectable design reasoning, constraints and evidence |
| [Spiral](https://github.com/jongos/Spiral) | Rehearse role-limited asynchronous workflows before building |
| [Shatterstar](https://github.com/jongos/Shatterstar) | Propose reversible evidence-backed simplification while preserving important tasks |
| [Mojo](https://github.com/jongos/Mojo) | Remove repetition, needless nuance and overly cautious language from AI outputs |
| [Colossus](https://github.com/jongos/Colossus) | Inventory selected developer workspaces read-only and surface evidence-backed questions |

## Further Reading

[Detailed project reference](REFERENCE.md) · [License and font notices](REFERENCE.md#license)

Created by Jon Gosier. Independent project; no Marvel affiliation or endorsement.

## License

Created by Jon Gosier. Original work is Apache-2.0; bundled Archivo font files retain their own license and notices. See [LICENSE](LICENSE).
