# EWP network (Erasmus Without Paper)

EWP (Erasmus Without Paper) is the European interoperability standard that lets
international relations offices exchange their mobility data fully digitally, with no
paper and no manual emails. AroundLink connects your institution to this network:
your inter-institutional agreements, learning agreements, transcripts of records and
nominations flow directly software-to-software with your partner universities.
Concretely, an agreement signed on your side appears at the partner's, a grade
entered here travels to the student's home university, and every change notifies the
other side automatically.

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

??? note "Internal details (AroundLink team)"
    Discovery API v6. The manifest is served at `/ewp/{ewpHeiId}/manifest.xml`,
    identified by the client university's HEI ID. It declares 15 API entries:
    discovery, echo, institutions, omobilities, omobility-cnr, omobility-las,
    omobility-la-cnr, iias, iia-cnr, iias-approval, iia-approval-cnr, imobility-tors,
    imobility-tor-stats, imobility-tor-cnr and factsheet, each with its version and
    URL. The manifest is self-validated before publication (503 if invalid) and
    cached for 1 h. Only AroundLink client universities expose a manifest;
    partner-only institutions return 404. Institution provisioning (keys included)
    is done through a dedicated console command.

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

??? note "Internal details (AroundLink team)"
    Echo API v2, exposed at `/ewp/{ewpHeiId}/echo`. The response returns the caller's
    actually-authenticated identity (HEI ID), never a client-supplied value. EWP
    responses are never compressed (integrity digests are computed on the
    uncompressed body). Serves as a connectivity probe and as validation of the
    authentication chain.

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

??? note "Internal details (AroundLink team)"
    Institutions API v2 (declared 2.2.0), up to 10 HEI IDs per request
    (`max-hei-ids=10`). The current response is minimal (hei-id + English name); the
    rich information (addresses, contacts, calendars) is carried by the Factsheet API
    rather than here.

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

??? note "Internal details (AroundLink team)"
    Factsheet API v1.2, `max-hei-ids=1`, anonymous client authentication allowed
    (public data). Publishing (incoming) at `/ewp/{ewpHeiId}/factsheet`; empty
    optional blocks fall back to the institution contact and then to fallback values
    to stay schema-valid. Internal editing via `/mobility/ewp-factsheet`
    (ROLE_MOBILITY + MODULE_WRITE:institution), one factsheet per university.
    Fetching (outgoing) through a sync service that first queries the registry to
    verify the partner exposes the API, then maps the response onto the `EwpFactsheet`
    entity — locked fields and 6 EWP-out-of-schema local fields are never touched
    (ticket AROUNDLINK-324). Triggerable from the agreement screen or via console
    command.

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

??? note "Internal details (AroundLink team)"
    IIAs API v7.0.1, `max-iia-ids=100`. Entities: `Exchange`. Incoming endpoints:
    `iias/index` (partner, receiving academic year, modified_since filters),
    `iias/get` (full content), `iias/approval` (iia-hash fingerprint), `iias/stats`
    (counts by approval state). The v7 iia-hash covers only "strategic" fields
    (mobilities, languages, ISCED, EQF) and excludes contacts, PDF, in-effect,
    iia-code. Multi-tenant scoping: each endpoint returns only agreements where the
    authenticated caller is the partner, so no volume or content is exposed toward a
    third party.

    Change notifications: iia-cnr v3, iia-approval-cnr v2. Incoming — an `iia-cnr`
    notification triggers an agreement re-fetch, a diff, then an
    `ExchangeIiaPendingUpdate` in PENDING_REVIEW status + coordinator email;
    idempotence is based on the full payload fingerprint (not the iia-hash). If the
    agreement is unknown, a minimal Exchange shell is created. Outgoing — editing an
    agreement on our side emits an `iia-cnr` to the partner; an incoming
    `iia-approval-cnr` re-fetches the partner's approval. Internal review via
    `/mobility/iia-reviews`: granular field-level diff (including add/remove of
    mobility-specs), selective apply that recomputes the iia-hash and resets approval
    to DRAFT.

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

??? note "Internal details (AroundLink team)"
    omobility-las API v1.2. Entity: `LearningAgreement` (AroundLink is the sending
    institution). Incoming endpoints: `omobility-las/index`, `omobility-las/get` (full
    content, Tables A/B, A2/B2 amendments, signatures, changes-proposal),
    `omobility-las/update` (partner approve/comment), `omobility-las/stats`. Scoping:
    only the authenticated host HEI can fetch an agreement, to protect the student's
    personal data. Concurrent-edit guard: a stale proposal returns a conflict (409).
    Change notification: omobility-la-cnr v1 — incoming, `fetchOla` retrieves the
    fresh version and merges signatures + validation state (AROUNDLINK-519); outgoing,
    `sendOlaCnr` notifies the host HEI when our agreement changes. Table B auto-filled
    on validation.

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

??? note "Internal details (AroundLink team)"
    imobility-tors v1, imobility-tor-stats v1, imobility-tor-cnr v1. Entities:
    `TranscriptOfRecord` + `ExchangeAffectation` (AroundLink is the host institution).
    Incoming endpoints: `imobility-tors/index`, `imobility-tors/get` (transcript in
    ELMO / EMREX format, learner identity via ESI, graded courses),
    `imobility-tors/stats`. Data access requires authentication; scoping relies on the
    calling HEI. Change notification imobility-tor-cnr on the incoming side (with
    optional `fetchTor` re-fetch on the outgoing side). Only graded courses are
    emitted; country codes are normalised to ISO.

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

??? note "Internal details (AroundLink team)"
    omobilities API v3, omobility-cnr v1. Entity: `ExchangeAffectation`. Incoming
    endpoints: `omobilities/index`, `omobilities/get` (`student-mobility` content:
    student, agreement + nominee ISCED-F, EQF level, sending/receiving HEI, IIA link,
    activity type, status), `omobilities/update` (partner approve/reject, writes a
    history row with signer or comment). Status follows `ExchangeAffectationStatus`
    (values aligned 1:1 with the network; an undecided nomination = pending). Scoping:
    `get` discloses only to authenticated host HEIs. Change notification omobility-cnr
    on the incoming side.

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

??? note "Internal details (AroundLink team)"
    EWP HTTP signature (server and client authentication): every request and response
    is signed, and the caller's identity is resolved to a HEI ID — the basis of the
    multi-tenant scoping across all endpoints. EWP registry: a local mirror of the
    network catalogue (institutions, APIs, versions, public keys) used to resolve a
    partner endpoint's URL before an outgoing call and to identify the caller.
    Outgoing hub `EwpClientService`: centralises signed calls (fetching agreements,
    approvals, mobilities, learning agreements, transcripts, factsheets; sending
    change notifications). ECHE: mirror of the public Erasmus Charter list (Erasmus
    Charter for Higher Education) used as an institution-lookup source. Current model
    of one keypair per institution (planned evolution: separate client and server
    keys, ticket AROUNDLINK-537).
