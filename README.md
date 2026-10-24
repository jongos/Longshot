![Longshot](docs/longshot-readme.svg)

# Longshot

**Make the Interface Prove It.**

Give Longshot an interface. It selects important tasks, follows the journeys and reports what works, what gets in the way and how to verify a fix. Want to direct the review? Supply your user roles and workflows.

## Put It to Work

- **Before shipping:** test whether someone can find and complete a core task.
- **After an interruption:** check whether drafts, choices and context survive leaving and returning.
- **When “done” is unclear:** distinguish a success message from a result that can actually be found and used.
- **Beyond the default path:** examine relevant keyboard, zoom and narrow-screen conditions.

Each finding includes the starting state, actions, observed result and an acceptance test.

On follow-up reviews, Longshot retests the original problem and tracks resolved, recurring and untested findings. [See how comparisons work](skills/longshot-human-centered-ui/references/report-continuity.md).

## Give It a Goal

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

Longshot also checks successful journeys for hidden workarounds and whether important decisions explain their consequences. Recommendations connect the observed obstacle to a specific change and a way to check whether it helped.

Use a compatible agent with authorized browser or application access. [Read the skill](skills/longshot-human-centered-ui/SKILL.md) for the review method and [setup details](REFERENCE.md#install-and-invoke) for alternatives.

[Visit the website](https://jongos.github.io/Longshot/) · [See an example report](REFERENCE.md#a-finding-you-can-act-on)

## In the Hex Men Family

| Project | How It Complements This Work |
|---|---|
| [Dazzler](https://github.com/jongos/Dazzler) | Create and refine interfaces, documents and slides. |
| [Style Science](https://github.com/jongos/style-science) | Connect design requirements to measurable checks and evidence. |
| [Spiral](https://github.com/jongos/Spiral) | Find gaps in workflow handoffs, ownership and recovery. |
| [Shatterstar](https://github.com/jongos/Shatterstar) | Simplify products while preserving important tasks. |
| [Mojo](https://github.com/jongos/Mojo) | Make AI outputs clear and direct. |

[Explore Hex Men](https://github.com/jongos/Hex-Men) for tools that complement your task.

## Further Reading

[Detailed project reference](REFERENCE.md) · [License and font notices](REFERENCE.md#license)

Created by Jon Gosier. Independent project; no Marvel affiliation or endorsement.
