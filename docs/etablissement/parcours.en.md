# Mobility paths

A **path** — a *workflow* in the interface — is the list of things a student has to do
during a mobility. You build it once, then apply it to a group of students: each of them
moves at their own pace, and you see where everyone stands.

It replaces the old onboarding sequence: one workshop now serves the students you send
**and** the students you host.

!!! info "Where it happens"
    **Settings ▸ Workflows** to build a path. You **plug it in** elsewhere: on a campaign for
    outgoing students, on a welcome session for incoming ones. A path that is plugged in
    nowhere does nothing.

## One path per direction

**What it is for.** Sending and hosting do not call for the same pieces. The direction is
chosen when you create the path and never changes: it decides where the path can be used.

**Who it is for.** <span class="al-audience">IO officer / coordinator</span>

**How it works.**

| Direction | For whom | What usually goes in |
|---|---|---|
| **Outgoing** | the students you send | from the partner's yes to the return: identity document, insurance, learning agreement, arrival and departure certificates, transcript |
| **Incoming** | the students you host | from arrival to transcript: information check, documents, charter, campus and course choice, feedback |

Two mechanics only exist in one direction, and the screen says so before you find out by
having the step refused:

- **Choose campus** only exists for incoming students — the host institution is the one with
  several sites;
- **Choose courses** too — it reads the host's course catalogue and feeds the incoming
  transcript. For a student you send, the equivalent is the learning agreement, which lives
  in its own module.

!!! tip "Start from an existing path"
    The copy icon on each row duplicates a path under a new name. It beats the blank page,
    and two close paths stay comparable.

## Plugging the path in

**What it is for.** A path on its own starts nothing. It begins when you attach it to a
group.

**How it works.**

- **Outgoing** — open a campaign, **Edit**, settings tab, **Mobility workflow** field. Every
  student accepted by a partner then receives the path automatically. The field is optional:
  you can plug it in later from the campaign's **Mobility** tab.
- **Incoming** — under **Onboarding**, create a **welcome session**, name it, pick its path.
  When you accept a nomination, you choose which session the student joins.

The same path can serve several campaigns or sessions. The **Used by** column in the list
tells you how many.

!!! warning "Changing a step reaches those already on their way"
    A path in service is not frozen: a change to a step reaches every student already
    following it. Check the **Used by** column before touching a step, and the **Students**
    column to know how many files are concerned.

!!! note "Changing a campaign's path asks for confirmation"
    The replacement happens from the screen it governs, and asks for confirmation: students
    already under way switch to the new path.

## What a step can ask for

**What it is for.** Each step carries **one action type**, which decides who acts and what
moves the student on.

**How it works.** The catalogue is **closed**, by design: each type plugs into a function
that already exists in the tool — a document type, a template, the course catalogue, the
validation queue. A step is therefore never a free-text field: the path **orders existing
functions** and makes them compulsory at the right moment.

| Step type | Available for | Who acts | What moves the student on |
|---|---|---|---|
| **Complete profile** | both directions | the student | they have filled in the fields you picked, checked the rest, and confirmed their information is correct |
| **Deposit documents** | both directions | the student | every requested document is uploaded |
| **Request a language test** | both directions | the student | the test you asked for is provided, certificate **and** scores |
| **Generate a document** | both directions | nobody — automatic | the platform produces the document; the student confirms they have read and downloaded it |
| **Generate, then collect signed** | both directions | the student | they return, signed, the document the platform issued |
| **Choose campus** | incoming only | the student | they have picked one of your campuses |
| **Read and accept** | both directions | the student | they tick that they have read and accepted — the wording accepted is kept **as it was on that day** |
| **Choose courses** | incoming only | the student | they have handed in their course selection |
| **Give feedback** | both directions | the student | they write their review, you moderate it in the validation queue: accepted on every topic asked closes the step, refused sends it back for a rewrite |
| **Mirror something done elsewhere** | both directions | nobody — a mirror | see below |

!!! note "A language test is not a document like any other"
    You list the tests you accept — IELTS, TOEFL iBT, Duolingo — and **one of them is
    enough**. What is expected is not only a scanned PDF, but the structured result: test
    type, overall score, the four skills, the European level. That is what lets you decide.

!!! tip "The target date blocks nothing"
    Each step can carry an indicative date. It guides the student, nothing more: handing in
    later does not block the step. Leave it empty if you do not want one.

## Steps that tick themselves

**What it is for.** Most steps in a path are not things anyone does *inside* the path. They
**watch an object that already exists elsewhere** in AroundLink — a signed learning
agreement, a validated document, a grant payment — and tick on their own when it changes.
They untick too, if the object goes back.

**How it works.** That is why you cannot tick them by hand, and why they are not in the type
list when you add a step: **the platform sets them up**, with the object they watch. The
paths delivered with AroundLink already contain them — "learning agreement signed by all
three", "confirmation of arrival", "transcript validated".

!!! info "A mirror copies nothing"
    The step does not duplicate the data: it reads the original object. There are therefore
    never two versions of the same fact, and a withdrawn signature sends the step back to
    pending.

## Ordering, folding, archiving

**How it works.** Steps are reordered **by dragging** them from one card to another, and each
step declares the **phase** it belongs to — before, during or after the mobility. It is that
phase which feeds [mobility tracking](suivi-mobilites.md).

The path list sorts and filters. Its **State** column speaks: *With steps*, *With students*,
*Not in use*, *Inactive*. A path you no longer want goes to the archives — **Archive**, then
**View archived workflows** to find it again and restore it.

**Use case.**
> The school builds two paths: an outgoing one in nine steps, an incoming one in seven. The
> outgoing path is plugged into this year's campaign; the incoming one into the "Autumn 2026
> intake" session. The four learning-agreement and transcript steps are mirrors: nobody ticks
> them, they follow the documents. The coordinator therefore only watches the five steps that
> really ask for something.
