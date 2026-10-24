![Longshot](docs/longshot-readme.svg)

# Longshot

**Make the Interface Prove It.**

Longshot is an independent interface-testing skill. Give it a realistic task and an interface to use. It attempts the journey, checks the result and returns obstacles you can reproduce, supported strengths and recommendations you can verify.

## Put It to Work

- **Before shipping:** test whether someone can find and complete a core task.
- **After an interruption:** check whether drafts, choices and context survive leaving and returning.
- **When “done” is unclear:** distinguish a success message from a result that can actually be found and used.
- **Beyond the default path:** examine relevant keyboard, zoom and narrow-screen conditions.

The deliverable connects each finding to its starting state, actions, observed result and a concrete acceptance test. Longshot can report no findings when the evidence supports that conclusion.

## Give It a Goal

```sh
npx skills add jongos/Longshot --skill longshot-human-centered-ui
```

```text
Use $longshot-human-centered-ui to test this demo. Prepare a draft,
open its required reference, then return and finish. Use the supplied
test account. Report reproducible obstacles without modifying the app.
```

Use a compatible agent with authorized browser or application access. [Read the skill](skills/longshot-human-centered-ui/SKILL.md) for the review method and [setup details](REFERENCE.md#install-and-invoke) for alternatives.

Longshot tests the rendered experience; it does not redesign the application merely because a review was requested. Agent observations do not replace human research or certify accessibility. Broad reliability remains unproven; see the [validation record](validation/RESULTS.md).

[Visit the website](https://jongos.github.io/Longshot/) · [See an example report](REFERENCE.md#a-finding-you-can-act-on)

## In the Hex Men Family

| Project | How It Complements This Work |
|---|---|
| [Dazzler](https://github.com/jongos/Dazzler) | Create and refine expressive interfaces, documents and visual stories. |
| [Style Science](https://github.com/jongos/style-science) | Make design requirements, constraints and evidence inspectable. |
| [Spiral](https://github.com/jongos/Spiral) | Trace multi-person workflows, handoffs and waiting states before building. |
| [Shatterstar](https://github.com/jongos/Shatterstar) | Evaluate what to remove, combine, hide or defer while preserving important tasks. |

[Hex Men](https://github.com/jongos/Hex-Men) brings the collection together. Choose the project your question needs; there is no required sequence. Spiral and Shatterstar are research-informed drafts and their repositories require access.

## Further Reading

[Detailed project reference](REFERENCE.md) · [License and font notices](REFERENCE.md#license)

Created by Jon Gosier. Independent project; no Marvel affiliation or endorsement.
