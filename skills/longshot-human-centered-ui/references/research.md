# Retained research guidance

Verified 2026-10-23 against the linked primary publishers. These are concise interpretations for agentic interface testing, not copied articles or proof about any particular application's users. Reuse without a fresh literature search; verify again for changed standards, precise conformance claims or questions beyond this synthesis.

## Recognition, conventions and recovery

[Nielsen Norman Group: ten usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) supports visible system state, familiar terminology, consistency, recognition instead of remembered instructions, control, error prevention and understandable recovery. Keep relevant context and choices available where decisions occur. Check whether errors explain what happened and how to proceed without destroying valid work. Accommodate experienced users as well as newcomers.

Limit: heuristics guide inspection; they are not evidence that a particular person was confused, nor universal rules prescribing one interface.

## Disclosure and meaning

[NN/G: progressive disclosure](https://www.nngroup.com/articles/progressive-disclosure/) supports deferring advanced or infrequent options while keeping primary work accessible. Determine frequency and importance from context; do not hide a frequent action merely to simplify the screen. Preserve expert paths.

[NN/G: icon usability](https://www.nngroup.com/articles/icon-usability/) explains why icon interpretation depends on experience and convention. Prefer understandable action labels when symbols are ambiguous. A tooltip or accessible name can support a control but does not alone establish visible discoverability.

Limit: the right disclosure boundary and familiarity of a symbol depend on users and tasks. An extra step can be justified by risk, required choices or meaningful control.

## Appearance and performance

[NN/G: aesthetic-usability effect](https://www.nngroup.com/articles/aesthetic-usability-effect/) describes how appealing presentation can influence perceived usability and mask problems. Record visual coherence separately from completion and recovery evidence. Do not claim a beautiful interface is usable because the tester likes it, or a plain interface is unusable because it lacks decoration.

Limit: this effect does not quantify a specific product's usability or replace observed task performance and human research.

## AI expectations and control

[Microsoft Research: Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/) and its [author explanation of the 18 guidelines](https://www.microsoft.com/en-us/research/articles/guidelines-for-human-ai-interaction-eighteen-best-practices-for-human-centered-ai-design/) support clear capabilities and limitations, contextual behavior, efficient invocation/dismissal/correction, appropriate behavior under uncertainty, understandable consequences and controls over adaptation.

Check whether users can distinguish a suggestion from an executed action, correct an output and recover from failure. Report a mocked AI response as simulated; it does not validate model quality or live-service reliability.

Limit: these guidelines involve contextual tradeoffs and predate many current generative-AI interfaces. They are not a complete safety or reliability assessment. The supplied [CHI 2019 paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf) was discoverable in search, but direct full-text retrieval timed out twice; the synthesis above was verified against Microsoft's accessible project page and author explanation, not a full reading of that PDF.

## Accessibility evidence

[W3C: WCAG overview](https://www.w3.org/WAI/standards-guidelines/wcag/) identifies WCAG 2.2 as a Recommendation and distinguishes normative criteria from supporting guidance. Use the linked [WCAG quick reference](https://www.w3.org/WAI/WCAG22/quickref/) for precise criteria and exceptions when making a conformance claim.

Check keyboard access, focus, names, labels, contrast, resizing/zoom, reflow, error identification and alternatives to dragging as relevant. Record which methods and states were actually checked. Do not guess numeric contrast from a screenshot or claim a criterion failure without its applicable conditions. State the standard/version/level if evaluated; do not silently assume a compliance target.

Limit: an automated scanner, agent walkthrough or small checklist cannot establish complete accessibility. Native interfaces require platform-appropriate methods; web criteria are not automatically a complete native-app assessment. Disabled participants and assistive-technology testing supply evidence these inspections cannot.

## Human task testing

[GOV.UK: moderated usability testing](https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing) supports observing actual or likely users attempting realistic tasks, using neutral prompts and follow-up questions. Choose tasks with believable context, without naming the control or revealing the solution. Record completion, difficulty and interpretation separately from opinions about appearance.

Limit: agent execution is not participant research. Do not invent a sample, quotation, success rate or user sentiment. Propose human tests to resolve consequential uncertainties; do not prescribe arbitrary participant counts or generalize beyond the research design.
