# From Functional Checks to a Clearer Scene-Creation Journey

## Reported Experience

> Longshot was particularly useful because it shifted the question from “Does the app work?” to “Does the experience make sense to someone trying to create a scene?”

— Feedback from another agent, supplied by the project maintainer on October 24, 2026.

The agent reported friction in a scene-creation application that functional tests had missed:

| Reported friction | Example from the feedback | Review lens |
| --- | --- | --- |
| Hidden choices | Selecting a saved prompt was buried beneath a large writing area. | Choice visibility |
| Unclear decisions | Save buttons had different scopes; “Photos” opened generation rather than a gallery. | Action scope |
| Lost context | Comparing prompts required applying choices and backtracking; Repair and Continuity assumed an existing timeline. | Context continuity |
| Unnecessary translation | Frame counts, provider terminology and shifting “scene” / “casting” labels required interpretation. | Translation burden |

The feedback says the review used rendered screens, synthetic journeys and counterchecks, and preserved paid consent, replacement warnings and truthful provider status. It reports **21 traceable recommendations**, followed by a phased plan and mockups centered on **character → prompt → scene → result**, with editing optional.

This is an attributed account supplied by the maintainer. The original findings, screenshots, counterchecks and implementation/retest records are not included in this case study. The recommendation count is the reported output, not a measure of accuracy or improved user outcomes. No participant quotations or measured outcomes are claimed.

## Example of Applying the Lesson

The following is a proposed review task and acceptance test derived from the feedback, not a reconstructed observation or one of the original 21 findings.

**Task:** Choose between an existing prompt and a new prompt for a scene, compare the alternatives, and return to the initial choice.

**Inspect:** Can the tester discover both routes from the starting screen? Does previewing a candidate change the active prompt? Is the scope of each Save action apparent from its label and context? Can the prior choice be restored without losing entered work?

**Potential recommendation, if supported:** Make the existing-prompt route discoverable at the decision point; distinguish preview from applying a selection; label save actions by the object they save. Preserve replacement warnings and paid-action consent.

**Acceptance test:** Starting with a selected prompt and unsaved scene text, preview another candidate, cancel, and verify the original selection and text remain. Apply a candidate through the explicit action and verify only the intended scope changes. Check the saved-prompt route and new-prompt route remain available to the authorized role. Payment or generation is outside this example unless separately authorized.

## Track the Follow-Through

To extend this case study with verified results, link original finding IDs and evidence, then record acceptance/rejection reasons, implemented changes and comparable retest results. Evaluate the obstacle and the proposed remedy separately. Do not infer that all 21 recommendations were implemented or effective.

[Read the walkthrough](../skills/longshot-human-centered-ui/references/walkthrough-protocol.md) · [Back to Longshot](../README.md)
