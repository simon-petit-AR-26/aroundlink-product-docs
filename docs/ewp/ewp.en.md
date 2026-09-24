# EWP network (Erasmus Without Paper)

EWP (Erasmus Without Paper) is the European interoperability standard that lets
international relations offices exchange their mobility data fully digitally, with no
paper and no manual emails. AroundLink connects your institution to this network:
your inter-institutional agreements, learning agreements, transcripts of records and
nominations flow directly software-to-software with your partner universities.
Concretely, an agreement signed on your side appears at the partner's, a grade
entered here travels to the student's home university, and every change notifies the
other side automatically.

!!! info "Are you on the IT / integration team?"
    This page describes the **value** of each building block. For the list of
    endpoints, methods, API versions and links to the official EWP specifications,
    see the [EWP API reference](reference-api.md).

## Discovery / Manifest

**What it's for.** The manifest is your institution's digital business card on the
EWP network. It tells every partner university which services you offer and how to
reach you reliably. Without it, no partner can discover you or exchange anything with
you.

**Who it's for.** <span class="al-audience">partner institution / admin</span>

**How it works.** AroundLink publishes and maintains this manifest for your
institution. A partner (or the network's central directory) reads it to learn that
you can exchange agreements, learning agreements, transcripts and nominations, then
establishes a trust relationship. Everything is automatic — you have nothing to
publish by hand.

**Use case.**
> A Spanish university adds you as a partner; its software reads your manifest and
> immediately discovers it can send you a digital agreement.


## Echo

**What it's for.** Echo is a connectivity test: it confirms that your institution and
a partner can reach and mutually authenticate each other. It's the diagnostic tool
used when connecting a new partner, before any real data flows.

**Who it's for.** <span class="al-audience">partner institution / admin</span>

**How it works.** A test call returns exactly the information sent, together with the
verified identity of the caller. A correct response proves that the link and the
trust between the two institutions are working.

**Use case.**
> During partner onboarding, the team sends an Echo call; a successful response
> confirms the trust handshake is operational.


## Institutions

**What it's for.** This building block publishes your institution's basic identity
(its official name) from its identifier. It lets partners display a readable name
instead of a technical code in their screens.

**Who it's for.** <span class="al-audience">partner institution</span>

**How it works.** A partner supplies one or more institution identifiers and gets
back the matching names. Its interfaces can then present your agreements and
mobilities with a human-readable label.

**Use case.**
> A partner shows "Institut Polytechnique des Sciences Avancées" next to an incoming
> agreement, rather than the institution's technical identifier.


## Factsheet (institution info sheet)

The factsheet is your institution's practical info sheet: nomination and application
deadlines, housing / visa / insurance contacts, accessibility, decision and
transcript turnaround limits. AroundLink covers three complementary uses.

### Publish your factsheet

**What it's for.** You broadcast your practical information to the whole network, so
partners can advise their outgoing students without having to email you.

**Who it's for.** <span class="al-audience">partner institution</span>

**How it works.** As soon as a partner requests your sheet, AroundLink generates it
from the information entered by your office and returns it in a network-compliant
format.

**Use case.**
> A partner reads your factsheet and sees your application deadlines without having
> to email the international relations office.

### Edit your factsheet

**What it's for.** From a simple form, you maintain the content of the sheet that
will be broadcast to all your partners.

**Who it's for.** <span class="al-audience">IRO manager</span>

**How it works.** From the dedicated screen in your workspace, you fill in and update
the sheet's sections. Incorrectly filled fields (for example a phone number without a
country prefix) are flagged before saving.

**Use case.**
> The IRO manager updates the spring-semester nomination dates; the new sheet is
> immediately available to partners.

### Fetch a partner's factsheet

**What it's for.** You import a partner's practical sheet on demand, to find its dates
and contacts directly in AroundLink instead of looking them up elsewhere.

**Who it's for.** <span class="al-audience">IRO manager</span>

**How it works.** From a partner institution's page, a sync action fetches its
factsheet from the network and stores it on your side. Fields you have locked
manually are never overwritten; if the partner exposes no sheet, your hand-entered
data is kept.

**Use case.**
> Before a campaign, the manager syncs a partner's factsheet to display its decision
> turnaround directly in the agreement file.


## IIA — inter-institutional agreements

Exchanging inter-institutional agreements (IIA) is the flagship function: negotiate,
compare and sign bilateral Erasmus+ agreements without paper, with a shared copy
between both institutions. This maps to **agreements** in AroundLink.

**What it's for.** You manage an agreement's entire lifecycle — content, mobility
conditions, contacts, signing dates — digitally and shared with the partner. No more
divergent PDF versions traded by email: both sides work from a single reference.

**Who it's for.** <span class="al-audience">IRO manager / partner institution</span>

**How it works.** The partner can list and view the agreements it shares with you.
Each institution approves the exact version it has in front of it; when both have
approved, the agreement is in effect. Any change on one side automatically notifies
the other, which fetches the fresh version.

**Use case.**
> You adjust the number of places on an agreement; the partner is notified, fetches
> the new version, approves it, and the agreement flips to "in effect" on both sides.

### Change notification (CNR) and review

**What it's for.** When a partner modifies an agreement, you are notified and you
decide field by field what you accept, rather than suffering an automatic overwrite.
It's the safeguard that protects the integrity of your data.

**Who it's for.** <span class="al-audience">IRO manager</span>

**How it works.** A change notification triggers fetching the partner's version.
AroundLink prepares a side-by-side comparison and stages the proposal for review
(never applied automatically); the coordinator is notified by email. They accept the
desired fields — the agreement then returns to draft for a fresh approval — or reject
without touching their data.

**Use case.**
> A partner changes a language of instruction; the coordinator sees the difference,
> accepts that single change and leaves the rest unchanged.


## OLA — learning agreements

Digital exchange and co-signing of the learning agreements (OLA) for the students you
send on mobility. See also the [Learning Agreement](../etablissement/documents.md) page.

**What it's for.** You publish your outgoing students' learning agreements — courses
studied, courses recognised on return, signatures — so the host university reviews
and signs them online. The validation round-trip happens without paper.

**Who it's for.** <span class="al-audience">IRO manager / coordinator / partner institution</span>

**How it works.** The host university can list and fetch your students' agreements,
then approve them or request changes. On approval, its signature is recorded; when
both sides have signed, the agreement is validated. If the partner reports a change
on its side, AroundLink automatically fetches the up-to-date version.

**Use case.**
> The host university approves a student's learning agreement online; the status turns
> to "validated" in AroundLink and recognition is set in motion.


## Transcript (ToR — transcript of records)

Digital sending of transcripts for the students you **host**, back to their home
university. See also [Transcript of Records](../etablissement/documents.md).

**What it's for.** You transmit the official transcript (courses, grades, ECTS
credits, pass / fail) of your incoming students, so their home institution imports
the results and grants recognition without a paper transcript.

**Who it's for.** <span class="al-audience">coordinator / partner institution</span>

**How it works.** The home institution can list and fetch the transcripts of its
students who studied with you. The transcript is transmitted in a standardised
European format, ready to be imported and recognised automatically.

**Use case.**
> After exams, the partner's software fetches its student's transcript and
> automatically recognises the credits earned.


## Nominations (outgoing mobilities)

Digital nomination of the students you send to a partner, and receipt of its
decision. See also [affectation](../etablissement/campagnes.md).

**What it's for.** You transmit each outgoing student nomination (identity, field of
study, level, linked agreement) so the host university accepts or rejects it
digitally, with a tracked history of the decision.

**Who it's for.** <span class="al-audience">IRO manager / partner institution</span>

**How it works.** The host university can list and view the nominations you send it,
then approve or reject them. The decision comes back into AroundLink and updates the
student's status, with a record of the signer or the rejection reason.

**Use case.**
> You nominate a student to Milan; the Milan office approves via the network and the
> student's status turns to "approved" in AroundLink, with the signer recorded.


## Technical foundations

**What it's for.** Beneath every exchange sit the mechanisms that guarantee data
reaches the right partner, intact and from a certified source. They are invisible to
the user but essential to the network's trust.

**Who it's for.** <span class="al-audience">admin</span>

**How it works.** Every message exchanged is signed and verified, so each institution
knows with certainty who is talking to it. A central network directory makes it
possible to find each partner's address and identity before transmitting anything.

**Use case.**
> Before sending an agreement, AroundLink queries the directory to locate the partner
> and signs the message so it is accepted as authentic.

