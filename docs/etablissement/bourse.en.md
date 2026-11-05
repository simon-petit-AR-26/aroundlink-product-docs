# Mobility grants

Mobility grants handle the Erasmus+ financial side — and that of your other funding: your
grant programmes, awarding students, the documents each payment depends on, the payment
circuit through to the accountant, and the file the Commission's Beneficiary Module expects.

## Grant programmes

**What it's for.** Keep each source of funding apart: this year's Erasmus+ agreement, a
regional grant, a campus scheme. Each has its own budget, rates and files.

**Who it's for.** <span class="al-audience">grants office / IRO coordinator</span>

**How it works.** **Bourse** opens the list of your programmes; **New program** creates
one: name, academic year, type (**Erasmus+ KA131** or **Other (regional, campus…)**), grant
agreement number, start and end dates, and status:

| Status | What it allows |
|---|---|
| **Draft** | the programme is being set up |
| **Open** | it accepts grants |
| **Closed** | no new grants |

A student has at most one grant per programme. The year belongs to the programme: it is not
picked on the screen.

**Use case.**
> The grants office creates "Erasmus+ KA131 2026-2027" with its agreement number, leaves it
> in Draft while entering its rates, then opens it.

## A programme's screen

**What it's for.** See where the money and each file stand, on one screen.

**Who it's for.** <span class="al-audience">grants office / IRO coordinator</span>

**How it works.** At the top, four figures: **Agency allocation**, **Engaged (signed GA)**,
**Paid (advances + balances)** and **Docs pending**. If the programme is split into pockets,
the **Budget by category** table gives each one's planned, committed, paid and
**remaining** amounts.

The **Pipeline** bar counts files by status and the oldest wait; a click filters the list.
Files read as **Kanban** or **Table**:

| Column | Statuses it groups |
|---|---|
| **Before award** | To award, Zero grant, Waiting list |
| **Contract** | Contract to generate, Contract sent, Contract signed |
| **Advance** | Advance to pay, Advance paid |
| **In mobility** | In mobility |
| **Final documents** | Final documents expected, Certificate received, Balance to pay, Balance paid |
| **Closed** | Closed |

Panels point out what needs action: overpaid files, files waiting on end-of-mobility
documents (**Remind** chases the students), and documents no longer needed that can be
deleted.

**Use case.**
> In September, the head of office opens her programme: the Pipeline bar shows 12 files in
> "Advance to pay", the oldest waiting for 9 days. One click and the list shows just those.

## Awarding grants

**What it's for.** Create files from the mobilities already recorded, and set amounts
without working them out by hand.

**Who it's for.** <span class="al-audience">grants office</span>

**How it works.**

- **Add students** offers students with an active assignment to a country that has a rate
  — destination, period, suggested type —; those who already have a grant are greyed out.
  **Add N** creates the files.
- **New grant** creates a single file. Next to the amount, **Suggest** works out a proposal
  and breaks it down: stay, travel, traineeship, inclusion and green-travel top-ups, total,
  then advance and balance.
- In **Table** view, ticking files opens a decision bar: an amount (or the scale), then
  **Award**, **Zero grant** or **Hold** for the whole selection.
- **Import CSV** loads grants in bulk, with a preview flagging each row in error; an empty
  amount cell gets the suggested amount.

**Budget safeguards.** Creating a grant, importing or awarding in bulk refuses anything that
would exceed the year's allocation — "This grant would exceed the remaining allocation for
the year by X €" — or the pocket concerned. With no allocation entered, the screen says so
instead of letting it through.

**Use case.**
> The head of office adds the 48 students placed this year in one go, ticks those going to
> Germany and clicks **Award** with the scale: 14 files move to "Contract to generate".

## A grant file

**What it's for.** Everything about a student's grant, from award to balance.

**Who it's for.** <span class="al-audience">grants office</span>

**How it works.** The file holds the financial details, bank details, documents and six
dated milestones: **Grant Agreement signed**, **Learning Agreement signed**, **Arrival
confirmed**, **Certificate of attendance**, **Transcript of Records**, **EU Survey
received**.

The status follows from those milestones and the payments, in order: a file only reaches
**Closed** once the balance is paid and the final documents are in.

**Payment conditions.** Depending on your settings, each document can **block nothing**,
**block the advance** or **block the balance**. The file names what is missing for each
payment; overriding requires a reason. A recorded payment can no longer be rewritten: to
correct it, you recalculate the grant.

A file can be **deleted** as long as nothing has been paid; after that it is **cancelled**
(reason required) and can be **reopened**. Its **history** says who changed what, and when.

**Use case.**
> A student's advance stays blocked: the file shows the Learning Agreement is not signed. It
> is signed the next day, and the advance becomes payable.

## Rates and rules

**What it's for.** Set the programme's calculation and payment rules once and for all.

**Who it's for.** <span class="al-audience">grants office</span>

**How it works.** **Rates** opens the programme's settings: budget and pockets, funded
duration, stay rate, travel scale, top-ups, advance percentage, required documents, payment
blocks — with what differs from the Commission's default —, reminders (first reminder after
the end of mobility, then every N days) and closing the programme.

**Use case.**
> For its regional grant, the school sets the advance at 70% and decides the transcript
> blocks nothing.

## Paying: requests, approval, accounting

**What it's for.** Move money through three separate hands: who prepares, who approves,
who transfers.

**Who it's for.** <span class="al-audience">grants office · approver · accountant</span>

**How it works.**

1. **Prepare.** **Payments ▸ New payment request**: advance or balance, then the files to
   pay. Those that cannot be paid say why (blocked, already in a request, file cancelled).
   **Submit for approval** sends the request.
2. **Approve.** Whoever holds the **Payment approval** function sees it under **Awaiting
   your approval**, then **Approve** or **Send back** with a reason.
3. **Transfer.** The accountant opens **Payments**, a section of their own under
   **Institution**: approved batches to transfer, with beneficiary, IBAN, BIC, reference and
   amount. **Mark as paid** records the transfer, **Attach receipt** adds the proof. They
   see no student file.

| Request status | |
|---|---|
| **In preparation** | being put together |
| **Submitted** | awaiting approval |
| **Returned for correction** | sent back with a reason |
| **Approved** | to transfer |
| **Paid** | transferred |

The student is told when a payment is recorded, and confirms they received it — or reports
a discrepancy, which shows up under **Reported by students**.

**Use case.**
> The officer prepares October's advances request, the director approves it, the accountant
> transfers and marks it paid: the 14 files move to "Advance paid".

## The Commission's Beneficiary Module

**What it's for.** Produce the file the Beneficiary Module expects without rebuilding it by
hand, and check the two stay in agreement.

**Who it's for.** <span class="al-audience">grants office</span>

**How it works.** **Erasmus & mail merge** opens the export screen:

- **Erasmus file** — for the whole programme or a selection, in the Beneficiary Module's
  exact template. A check runs first: rows that would be rejected are held back, and a
  blocking issue prevents the download.
- **Mail merge file** — the mail-merge file for grant agreements; exported files move to
  "Contract sent".
- **Export history** — which file, by whom, when.

**Re-import BM file** links your files to the Beneficiary Module's activity IDs, and
**Compare with BM** shows the differences, read-only, with **Download the differences**.
**Export**, on the programme screen, only gives the list on screen.

**Use case.**
> Before the interim report, the head of office compares her programme with the Beneficiary
> Module: two amounts differ, she fixes them and exports the Erasmus file.

## On the student side

The **Bourse** tab of their profile asks whether they are applying for an Erasmus+ grant
(saying no does not take them out of Erasmus+), shows their grant and has them confirm each
payment received. See the [student portal](../etudiant/decouverte-candidature.md).
