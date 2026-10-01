# Mobility campaigns

The Campaigns module structures application rounds: eligible students rank a set number
of wishes among the catalogue's offers, and the IRO drives the whole thing — from opening
to final placement — without rebuilding the list by hand.

## Mobility campaigns

**What it's for.** Lets an international relations office run a framed application round,
where students rank a fixed number of exchange wishes within a given window. The campaign
automatically determines which students and which partner offers belong to it, avoiding
hand-picking each participant.

**Who it's for.** <span class="al-audience">IRO manager / coordinator</span>

**How it works.** The coordinator creates a campaign by choosing the academic year, the
number of allowed wishes, the target academic levels, the mobility periods, the eligible
agreement types and an optional partner-tag filter. On save, the system builds the pool of
participating students and the pool of eligible offers from those criteria. The campaign
moves from Draft to Ready (opening it to students), then Opened and Finished; only a draft
campaign remains editable.

**The end date closes the campaign on its own.** The morning after its last day, the
campaign moves to Finished with nobody clicking: wishes still in draft become wishes, your
students are notified and you receive the summary — exactly what the "Finish" button does.

If that closing feels premature, the "Reopen" button gives your students back the right to
change their wishes. Remember to push the end date back: without that, the campaign closes
again the next morning.

![Campaign list, showing how many campaigns are draft, open and finished](../assets/screenshots/campagnes-liste.png)

*Your campaigns, whatever their status. The four counters at the top give you the state of play at a glance. Click the image to enlarge it.*

**Use case.**
> The IRO opens a "2026/2027 – Semester 1 – Master" campaign, 5 wishes allowed, restricted
> to Erasmus+ partners tagged "Engineering"; every Master student with a Semester 1 period
> is enrolled automatically.


## Setting up a campaign, setting by setting

**What it's for.** Understanding what each setting changes before you turn it on — several
of them cannot be undone once your students have started answering.

**Who it's for.** <span class="al-audience">IRO manager / coordinator</span>

### Identity

**Name**, **school year**, **start** and **end date**. The end cannot precede the start, and
it is not decorative: the morning after the last day, the campaign closes by itself.

### The student pool

Who takes part. Combine as many criteria as you need:

- **Academic level** and **track** — the track is the label you gave your cohorts
  ("Aero 4", "MSc 26-27");
- **Campus** — or all of them;
- **General tags** and **student filters**;
- **manual additions**, student by student, for the odd case.

### The destination pool

Where they can go:

- **Agreement types** — exchange, double degree, paying mobility, traineeship;
- **Mobility type** — including staff mobility, teaching and training;
- **Periods**;
- **Partners** — all of them, or narrowed by your institution tags and filters.

Here too you can add or remove an agreement by hand.

### Wishes

**Minimum** and **maximum**, both optional. The minimum blocks just as the maximum does: a
student who has not reached the required number cannot submit their list.

### The student's file

You choose the **required documents**, then what happens when one is missing:

- **Show it and assign anyway** *(recommended)* — the gap is flagged, the decision stays
  yours;
- **Block the assignment** until everything is in hand.

### Can a student say they are not going?

- **No** — an empty wish list simply means "no answer yet";
- **Yes** — they can declare they do not wish to go. They answer once, **no reason is
  asked**, and they immediately stop appearing in your reminders and in the matching. Their
  answer stays reversible while the campaign is open.

!!! warning "This setting cannot be caught up mid-course"
    A campaign that never asked the question does not start asking on its own. And once
    answers have come in, there is no going back — otherwise decisions your students already
    made would become unreadable.

### Who confirms the destination

- **The student accepts or declines** the proposal;
- **The coordinator assigns directly** — the acceptance step disappears, your decision
  creates the placement.

### The note to students

Free text, optional, shown to everyone taking part.

### The preview before saving

Before you confirm your changes, a summary tells you what the save will **add, keep and
remove** — destinations as well as students. Removing a partner takes all of its agreements
out of the campaign, along with the wishes already placed on them: the preview says so
beforehand, not after.

## What matching requires

**What it's for.** Knowing what must be ready for a matching round to run — and why it
sometimes refuses to start.

**Who it's for.** <span class="al-audience">IRO manager / coordinator</span>

**How it works.** The engine seats each student on the cell of **their own track** — "Aero
4" is not "Aero 5" — and it never guesses. Three conditions are therefore required of every
participant:

| Condition | Why |
|---|---|
| **A profile** | With no file, there is nothing to place. |
| **A track** | It is what designates the cell. With no track, no cell matches them. |
| **An imported ranking** | The round is an **order**: it serves the first-ranked, and what is left goes to the next. With no rank, a student has no position in that order. |

A participant missing any of the three is **set aside and named** in the report, with the
reason. The round does not run in silence.

!!! warning "A track is required even if you do not use them"
    If your institution does not distinguish cohorts, give yourself one track per level you
    use — "Bachelor", "Master". A single mechanism then carries every case, and nothing is
    ever inferred on your behalf.

!!! info "Rankings are imported beforehand, never during"
    The round does not produce a ranking. Import it first; otherwise unranked students would
    be served last, which would be a decision nobody took.

**None of this constrains you by hand.** You remain free to place whoever you want, wherever
you want, ranked or not: that is your call, and the engine does not stand in the way. These
three conditions apply to the automatic round only.

A round can be re-run as often as needed — it is not a one-shot.

## Wishes, proposals and placements

**What it's for.** Turns each student's ranked wish list into a confirmed placement,
respecting real place availability and student rank. Automates the "who goes where"
allocation offices otherwise run on spreadsheets, while letting the coordinator adjust and
the student accept or refuse.

**Who it's for.** <span class="al-audience">coordinator / student</span>

**How it works.** Students submit an ordered wish list. The coordinator launches automatic
allocation, which processes students by rank (GPA) and offers each the first wish that
still has a place for their period; those who can't be placed are flagged. The coordinator
can then pre-assign (override), refuse or cancel a proposal — each action recalculates the
rest — then send proposals to students, who accept (creating a nomination to the partner)
or refuse (which cancels their other wishes and frees the place). When a proposal is sent
or a student is placed, they can be notified — by email and/or in the app; these
notifications are configurable and can be turned off by the institution.

![Placement screen: students and their wishes on the left, destinations and their places on the right](../assets/screenshots/campagne-suivi-affectation.png)

*A campaign's tracking: at the top, what it holds, what is placed and how wishes were met; below, your students in ranking order, with their wishes as they ranked them.*

**Use case.**
> Two students rank Berlin as wish #1: the higher-ranked one (GPA) gets the proposal, the
> other automatically rolls to their wish #2. The coordinator then pre-assigns a special
> case, and the system redistributes the freed place.


## What the matching round did

**What it's for.** Knowing exactly what a matching round placed, what it could not place,
and **who** it left aside.

**Who it's for.** <span class="al-audience">IRO manager / coordinator</span>

**How it works.** At the end of the round, a report tells you how many students were served
and which ones were left out. Skipped students are **named**, with the reason — a bare total
would send you through the whole cohort to find them.

Four reasons can leave a student aside:

- they have **no profile**;
- their level has **no track** attached;
- they have **no ranking**;
- their **file is incomplete**.

A round that places nobody now says so plainly, instead of reporting itself as completed.

**Use case.**
> The coordinator runs the round and reads the report: forty-two students placed, three left
> out for want of a ranking. It names them; they import the ranks and run the round again.

## Tracking, results and exports

**What it's for.** Gives the coordinator an operational dashboard of the running campaign
(who submitted, who's placed, dossier completeness), results and accepted views, plus CSV
exports for downstream processing. A campaign becomes a traceable, usable process.

**Who it's for.** <span class="al-audience">IRO manager / coordinator</span>

**How it works.** The tracking page aggregates participants, their wishes by rank, proposals
and placements, with charts and a completed-dossier counter. Wishes are also grouped by
**geographic zone** — Europe, North America, Latin America, Asia-Oceania, Africa, Middle
East — so you can read at a glance where demand is going. Dedicated pages present results
and accepted students, and two exports produce the all-wishes list and the final-assignments
list.

**Counter accuracy.** Destination and institution counts only include what is genuinely open
to students: hidden or archived partners are excluded, as are destinations with no place
available. The figures shown match what the student will see.

**Use case.**
> Mid-round, the coordinator sees 60% of students have submitted their wishes and 12 are
> placed; after closing, they export the final assignments for the mobility team.



## Nominating to your partners

**What it's for.** Officially telling the host institution you are sending them a student,
then recording their answer.

**Who it's for.** <span class="al-audience">IRO manager / coordinator</span>

**How it works.** Each row is a student assigned to a destination. You nominate them, and
the partner is informed. When they reply, you record their decision, stating how it reached
you: the platform, the EWP network, an email or a phone call. A refusal comes with its
reason.

The tab appears as soon as a place is held in the campaign. You can nominate a whole
selection in one go: the batch is processed in slices, its progress stays visible, and an
interrupted batch resumes where it stopped instead of starting over.

While the partner has not replied, two actions save you leaving the tool:

- **Remind** — a reminder goes to the partner without going through your mailbox. One
  reminder per twenty-four hours: the button greys out afterwards.
- **Withdraw** — you cancel the nomination and say why. The partner is told no decision is
  expected any more, and the student becomes available for another destination.

![Campaign nominations screen, showing each nomination's state and confirmation channel](../assets/screenshots/campagne-nominations.png)

*Each nomination's state and, for confirmed ones, how the answer came in.*

**Use case.**
> The coordinator nominates twelve students; eight confirmations come back through the
> platform or EWP, two by phone which they record by hand, and one destination refuses for
> lack of a place in the requested specialisation.

!!! note "Document reminders"
    Automatic reminders to students with an incomplete dossier are covered by
    [document reminders](communications.md).

## A campaign's statistics

**What it's for.** Knowing where a campaign stands, why some students are not placed, and
producing a report you can take to a committee.

**Who it's for.** <span class="al-audience">IRO manager / coordinator</span>

**How it works.** Statistics have their **own address**: a tab in their own right, at the
same level as wish management and nominations. You can send the link to a colleague, and
they will land on the same figures.

Everything shown comes from **the same source as the placement screen**. Tables and charts
cannot contradict each other.

**The headline figures.** The placement rate, the average wish obtained, and the breakdown of
those still waiting: awaiting a decision, all wishes refused, mobility declined, cancelled.
Each line is a different thing to do — reminding a student who is waiting is not the same
gesture as handling one whose every wish was refused.

**The breakdowns.** By agreement type, by country, by zone, by period.

**Demand and tension per destination**: where the crowd is, and where room is left.

!!! note "Two rules that stop the figures from flattering"
    The **average wish obtained** is computed on **placed students only**. Saying "80% got
    their first choice" while counting everyone would flatter a campaign that placed nobody.

    A **breakdown of fewer than five students is not shown**. On a small cohort, a percentage
    is one person: it reads as a trend when it is an anecdote.

![A campaign's statistics](../assets/screenshots/campagne-statistiques.png)

*The four headline figures, the wish obtained by rank, "why they are not placed", then the breakdowns by country, zone, agreement type and period — and tension destination by destination.*

**The report prints.** The header recalls the campaign's settings — school year, opening
dates, mobility type, number of wishes allowed, who confirms the destination, whether an
incomplete file blocks — and repeats at the top of every page, with your logo and the date.
Charts survive printing, and a block that does not fit moves to the next page instead of
being cut.

![The printed statistics report](../assets/screenshots/campagne-statistiques-rapport.png)

*Both pages of the report as it comes out: the campaign's settings at the top, the four figures, the rank of wish obtained and the reasons for not being placed; then tension destination by destination.*

[:material-file-pdf-box: **Download a sample report**](../assets/exemples/aroundlink-statistiques-campagne.pdf){ .md-button } — PDF, 2 pages, demonstration data.

**The data export.** Alongside the report, a three-sheet workbook:

| Sheet | What it holds |
|---|---|
| **Students** | One row per student: class rank, identity, level, track, year, language scores, then **each wish** with its code, university, city, country, place type and period |
| **By university** | The same campaign seen by destination |
| **Final assignments** | The placements retained |

[:material-microsoft-excel: **Download a sample workbook**](../assets/exemples/aroundlink-statistiques-campagne.xlsx){ .md-button } — Excel, 3 sheets, identities replaced with sample values.

The report is for showing, the workbook for working on: one goes to the committee, the other
into a spreadsheet.

**Use case.**
> Before the committee meets, the coordinator opens the statistics, prints the report to PDF
> and attaches it to the invitation. Members arrive having seen the same figures she has, and
> the discussion is about the twelve unplaced students rather than about reading tables.
