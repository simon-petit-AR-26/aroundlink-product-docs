# Onboarding incoming students

Onboarding is the **path a student you host follows**, from their first access to the end of
their stay: completing their profile, uploading their documents, choosing their campus,
reading and accepting a charter, receiving their acceptance letter.

You define that path once — it is a **sequence** — and every student concerned follows it,
step after step.

## Seeing where everyone stands

**What it's for.** Knowing at a glance who is waiting for what: your students who have not
acted yet, and those waiting on a decision from you.

**Who it's for.** <span class="al-audience">IRO manager / coordinator</span>

**How it works.** Two views of the same path.

The **Kanban view** shows one column per step and one card per student. Each card carries
their home institution and says who must act: *waiting on student*, or a blue **"Waiting on
you"** button when the ball is in your court.

![Onboarding in Kanban view](../assets/screenshots/onboarding-kanban.png)

*One column per step, one card per student. The counter at the head of each column says how many sit there, and the blue button flags what is waiting on you.*

The **table view** gives the same thing in rows, with progress as a figure — 2/8, 6/8 —
their current step, who must act, and the state of their access: not sent yet, sent on such a
date, or already connected. You remind with one button, and close the stay when it ends.

![Onboarding in table view](../assets/screenshots/onboarding-tableau.png)

*The same cohort as a table: progress over eight steps, the current step, who is awaited, and each person's access state.*

## Building a sequence

**What it's for.** Describing your welcome path once and for all, in the order you want it to
unfold.

**Who it's for.** <span class="al-audience">IRO manager / coordinator</span>

**How it works.** A sequence carries a name, and two notes that must not be confused:

- the **internal note** is seen by your team only;
- the **external note** is shown to the student on their onboarding page, **and to the
  partner institution** following its students with you.

Two checkboxes decide how it is used: **Active**, and **offer this one by default when
opening accesses** — handy when you only have one.

Steps are then declared in order, and reordered with the arrows.

![The sequence editor](../assets/screenshots/onboarding-sequence.png)

*The name, the two notes, the switches, then the steps in their order — each with its type, its instruction to the student and its settings.*

## What a step can ask for

**How it works.** The catalogue is **closed**, deliberately: every step type wires in a
feature that already exists in the tool — a document type, a template, the course catalogue.
A step is therefore never an inert free-text field: the path **orders existing features** and
makes them mandatory at the right moment.

![The catalogue of step types](../assets/screenshots/onboarding-types-etape.png)

*The nine types available. Under each step, the grey sentence recalls what carries it forward.*

| Step type | What it asks for | What carries it forward |
|---|---|---|
| **Complete profile** | The information you designate | The student has filled it all in |
| **Deposit documents** | The document types you choose | Everything is uploaded — then your validation |
| **Request a language test** | A test among those you accept | The certificate **and** the scores are provided — then your validation |
| **Generate a document** | Nothing from the student | The platform produces it; the student confirms having read and downloaded it |
| **Generate, then collect signed** | The signed document in return | The signed document is uploaded |
| **Choose campus** | A campus among yours | The choice is made |
| **Read and accept** | Reading a text and its attachments | The student ticks that they have read and accepted |
| **Choose courses** | A selection from your catalogue | The selection is made |
| **Give feedback** | An account of their experience | The feedback is submitted |

!!! note "A language test is not a document like any other"
    You list the tests you accept — IELTS, TOEFL iBT, Duolingo — and **any one of them is
    enough**. What is expected is not merely a scanned PDF, but the structured result: test
    type, overall score, the four skills, the European level. That is what lets you decide.

!!! tip "The target date blocks nothing"
    Each step can carry an indicative date. It guides the student, nothing more: handing in
    later does not block the step and does not mark it late. Leave it empty if you do not
    want one.

!!! warning "Validation: who opens the next step"
    On a document deposit or a language test, you can require the file to go through the
    **validation queue** before the next step opens. Without that box ticked, the student's
    action alone carries the path forward.

    On a charter to read or a document produced for them, there is nothing to validate: the
    student's acceptance opens the rest on its own. And the text they accepted is kept **as
    it was on that day**, even if you change it afterwards.

**Use case.**
> The school hosts twenty-six incoming students. It builds an eight-step sequence: proof of
> funds, language test, charter to accept, acceptance letter to download, campus choice, then
> courses. Each student moves at their own pace; the Kanban view shows the coordinator the
> three files awaiting her validation, and the rest happens without her.
