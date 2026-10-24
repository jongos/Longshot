# Guide Longshot Your Way

Longshot chooses important tasks automatically. To focus the review, tell it who uses the product, what they need to do, what matters most and what a successful result looks like. Supply any combination in ordinary language. No special syntax or complete brief is required.

## Start Automatically

```text
Use $longshot-human-centered-ui to test this app using the supplied
test account. Choose the important workflows and report obstacles
with evidence and recommendations. Do not modify the app.
```

Longshot infers the product's purpose, selects relevant journeys and states its assumptions. It asks only for missing information that changes access or the meaning of success.

## Add the Direction You Need

| Input | What to provide | Example |
| --- | --- | --- |
| Roles | Responsibilities, relevant experience and what each role can see or do | “Editors create drafts. Reviewers approve or return them but cannot edit the text.” |
| Workflows | Starting situation, goal, important branches and handoffs | “An editor submits a draft; a reviewer returns it with notes; the editor revises and resubmits.” |
| Priorities | What matters most, what comes next and what to exclude | “Prioritize lost work and unclear ownership. Then check keyboard access. Skip billing.” |
| Success criteria | An observable result that would demonstrate the task worked | “After returning from the reference, the title and body still match what was entered.” |

### Roles: Describe Responsibilities

Useful role details explain permissions and knowledge: a new editor, a returning reviewer or an administrator handling access. Provide the corresponding authorized test accounts separately. Naming a role does not grant access. Avoid sharing passwords in a reusable prompt.

For handoffs, identify who acts next and what they should see: “The reviewer sees the submitted version and can return it with notes. The editor can find those notes and resume the same draft.” Longshot can check each side when the necessary access is available.

### Workflows: Give a Goal, or Specify a Route

For discovery, describe the job without revealing the clicks: “Find a suitable plan and determine its total cost.” For a known route, provide exact steps: “Open Settings, select Billing, then compare plans.” Longshot can test either; exact steps guide the route rather than test whether it can be discovered.

Include interruptions or alternatives that matter: leave and return, cancel, correct an error, or hand work to another role. You do not need to list every possible branch.

### Priorities: Make the Tradeoff Clear

“Focus on usability” is broad. “Check draft preservation before visual polish; focus on the editor and skip administration” tells Longshot where to spend attention. You can request one journey, a short review or broader coverage. Supplied exclusions remain in force.

### Success Criteria: Describe What Can Be Checked

Replace “make it intuitive” with “the reviewer can locate the pending draft, identify its latest version and return it with a reason.” Replace “saving should work” with “save, reopen the record and verify both fields retain their entered values.” If you do not know the criteria, ask Longshot to propose them from the goal.

## Copy a Complete Brief

```text
Use $longshot-human-centered-ui to review our staging app.

Roles: Editors create and revise drafts. Reviewers approve or return
drafts with notes; they cannot edit the draft text.
Workflows: Create a draft, consult the reference, return and submit.
Then return it for edits as a reviewer and resume it as the editor.
Priorities: Preserve work first, make the next owner clear second,
and check keyboard access third. Skip billing and administration.
Success: Entered text survives the reference trip. The reviewer sees
the submitted version. The editor can find the return notes and resume
the same draft without losing its text.
Access: Use only the supplied staging accounts and synthetic records.
Report evidence, working behavior, obstacles and acceptance tests.
Do not modify the application.
```

## A Single Sentence Is Enough

- Role only: “Test as a first-time editor; choose the important workflows.”
- Workflow only: “Test creating and resuming a draft; infer the relevant role.”
- Priority only: “Choose the tasks, but prioritize recovery from interruptions.”
- Criteria help: “Test plan comparison and propose observable success criteria.”

Longshot fills in the missing pieces and labels its assumptions. To change focus during a review, say “Keep the editor role, focus only on resuming drafts, and skip submission.” To return to automatic selection, say “Choose the remaining workflows yourself, keeping the same access limits.”

The report identifies supplied versus inferred scope, what completed, what needed help and what remains untested. A workflow can complete and still reveal an unnecessary workaround or missing decision information.

[Back to Longshot](README.md) · [Use the landing-page guide](https://jongos.github.io/Longshot/#guidance)
