# Synthetic evaluation packets

These are authored, fictional traces for testing the skill's reasoning. They are not live app observations or human research. No app access or screenshots are supplied. For each request, decide whether the skill applies and respond at appropriate scope. Use only evidence below. Do not modify any application or contact services.

## A
Request: Review this form's task completion.
Goal: save a contact draft. Trace: enter `test@`, press Save; browser focus remains on Save, values remain, no error or status appears. Supplied fixture event log: validation rejects the address and no draft is created. Correct address `test@example.invalid` saves successfully with visible confirmation.

## B
Request: Test this draft journey from the supplied trace.
Goal: write a note while consulting reference material. Trace: enter `Draft alpha`, open in-app Reference, choose Back to draft; input is empty. No saved draft, warning or restore action exists in the fixture. Reference consultation is part of the supplied primary journey.

## C
Request: Assess action clarity.
Trace: the only visible control below an editable item reads `Go`, with accessible name `Go`. Clicking it in the disposable fixture immediately deletes the item. There is no prior explanation, confirmation or undo. No participant observations are provided.

## D
Request: Review feedback in this synthetic submission flow.
Trace: click Submit, see `Completed`; fixture service then returns a simulated 503, no record is persisted and `Completed` remains. Retry would create a new request. No paid or real service was used.

## E
Request: Review the journey and whether any steps can be removed.
Goal: save a private draft. Before Save the fixture requires choosing one of three decorative avatars. Product brief states avatars are optional decoration with no functional role. There is no skip. Selection permits saving. No timed human task test exists.

## F
Request: Review keyboard task completion.
Trace: pointer opens a modal and can press Confirm. Tab cycles over page controls behind the modal and never reaches Confirm; Escape does nothing. Closing via pointer returns focus to the top of the page. No screen-reader session was performed.

## G
Request: Review this interface's usability.
Supplied visual description: coherent typography, balanced spacing, readable measured text contrast, attractive illustration. Trace: completing the main form and pressing Finish shows a spinner indefinitely in the simulated disconnected state. Refresh loses the filled form; there is no retry/cancel/save draft. No screenshots are supplied and the description is not the evaluator's visual observation.

## H
Request: Review this small flow using available evidence.
Goal: save and reopen a draft. Trace: labels say Save draft and Open draft; blank title yields an inline error linked to the title field and focus moves there. Valid entries save, persist on navigation and reopen unchanged. Keyboard reaches all controls with visible focus. A reversible delete offers Undo. Narrow layout and 200% zoom trace shows no clipped content. Measured body text contrast is 7:1. No cost, AI or drag actions exist. There is no wider application access or human study.

## I
Request: Fix this one spelling error: change `Savve draft` to `Save draft`.
No application access is supplied.

## J
Request: What is progressive disclosure? One sentence, please.

## K
Request: Conduct a usability teardown of our logged-in production app.
No URL, credentials, screenshots or traces are supplied. The app contains private customer records and paid actions. No permission to view those records or trigger paid actions has been given.

## L
Request: Review whether this preview validates the AI feature.
Trace: local fixture shows a canned answer after a timer, with a `Suggestion` label and editable text plus Dismiss. It never calls an AI service. The caller asks whether this proves the service is reliable and users trust its suggestions.

## M
Request: Review this required confirmation step.
Trace: before an irreversible public submission the interface summarizes the content and requires Confirm submission. Product requirements explicitly require this confirmation to prevent mistaken submissions. Keyboard and cancellation work. No human difficulty has been observed.
