# Student portal — During & after mobility

Once the student is placed, the student portal becomes their control centre for
the mobility itself: tracking the exchange, the learning agreement (OLA), the
transcript of records, attestations, resources, services, and direct
communication with the international relations office. The goal stays the same:
student autonomy and peace of mind for the international office.

## My exchange

**What it's for.** Once placed, this is the student's operational page for the
mobility: it shows the host university, the mobility dates, the partner contact
and the published reviews, and lets them submit their arrival and departure
attestations. The student can also download an official assignment certificate.

**Who it's for.** <span class="al-audience">student</span>

**How it works.** The page loads the student's approved affectation and presents
the forms for submitting the arrival and departure attestations; saving is
blocked once the document is validated by the coordinator. The mobility duration
relies on the real attestation dates when they are entered, otherwise on
provisional dates derived from the academic year. A button generates the
assignment certificate as a PDF, from the nomination-letter template configured
by the institution when one exists.

**Use case.**
> On arrival abroad, a student submits their signed arrival attestation and
> downloads their official assignment certificate for the host institution's
> registration desk.

??? note "Internal details (AroundLink team)"
    The arrival (COA) and departure (COD) attestations are handled by their
    dedicated managers; once validated, they are locked on the student side. The
    assignment certificate checks that the document belongs to the logged-in
    student before generation, and falls back to a built-in layout if no
    nomination-letter template is configured. The main partner contact and up to
    6 published reviews (accepted and public) complete the page.

## Learning agreement (OLA)

**What it's for.** The student builds their Learning Agreement (online learning
agreement, OLA) by choosing their courses at the host university, grouped by
field. They see the total ECTS, save drafts, then submit — which counts as their
signature. The validated agreement is downloadable as a PDF.

**Who it's for.** <span class="al-audience">student</span>

**How it works.** The portal loads the approved affectation and the latest OLA
(creating a draft if needed). The courses offered by the partner are presented by
field; the student can also add a new course. Saving as a draft keeps the draft
status; submitting records the student's signature and moves the status to
"Selected by student". Editing the courses resets any institution signatures
already applied, to avoid validation on an outdated version. Download is only
possible once the OLA is fully validated.

**Use case.**
> A student chooses 6 courses (30 ECTS) across two fields, submits their OLA, then
> later downloads the PDF signed by all three parties.

??? note "Internal details (AroundLink team)"
    A shared resolution mechanism ensures that the page render and all
    asynchronous writes target the latest OLA (protection against multiple
    affectations). The download relies on the institution's Learning Agreement
    document template and is only served once the OLA is fully validated. A
    history feed traces the actions.

## Transcript of Records

**What it's for.** After mobility, the student records the grades obtained for
each OLA course, chooses the grading system, optionally uploads the official
transcript and submits it for validation by their institution. This is what
closes the academic loop of the exchange.

**Who it's for.** <span class="al-audience">student</span>

**How it works.** The page requires an approved affectation and an existing OLA.
It shows the OLA courses, transcript statistics, the grading systems, an upload
form and the history. On submission, the portal checks that each course has a
valid grade for the chosen system, records the grades, uploads the official
transcript where applicable, then records the transcript with the status
"Pending institution validation".

**Use case.**
> A returning student enters the ECTS grades for their 6 courses, uploads the
> host institution's official transcript, and submits for validation.

??? note "Internal details (AroundLink team)"
    Grade validation depends on the chosen grading system; the statistics are
    computed by the transcript manager. The file is saved with the "Transcript of
    Records" type. The PDF download of the validated transcript is served from
    the learning-agreement module.

## Resources

**What it's for.** A library where the student finds the documents and guides
their institution has published for outgoing students (handbooks, checklists,
pre-departure information).

**Who it's for.** <span class="al-audience">student</span>

**How it works.** The page lists the institution's files intended for the
"outgoing" audience. It stays empty if no home institution is available for the
student.

**Use case.**
> A student downloads their institution's Erasmus pre-departure guide.

??? note "Internal details (AroundLink team)"
    The audience filter targets the files visible to the outgoing audience.

## Services

**What it's for.** A marketplace of third-party services (housing, insurance,
banking…) offered to students, shown only when the institution has enabled the
marketplace.

**Who it's for.** <span class="al-audience">student</span>

**How it works.** Access is conditional on the institution enabling the
marketplace. Offers are shown for information, with affiliate links (and, where
applicable, promo codes) to the provider. No payment happens in AroundLink: to
subscribe, the student is redirected to the partner's website.

**Use case.**
> A student spots an insurance offer with a promo code, clicks, and completes the
> subscription directly on the provider's site.

??? note "Internal details (AroundLink team)"
    Display + affiliation (links and promo codes to the provider); no payment goes
    through the platform. Option enabled per institution; only active offers are
    shown.

## Messaging with the international relations office

**What it's for.** Built-in messaging lets the student have one-to-one exchanges
with their international relations office / coordinator, with an inbox, message
threads, replies and an unread-messages badge.

**Who it's for.** <span class="al-audience">student / coordinator</span>

**How it works.** The inbox lists the conversations; opening a thread marks it as
read; replying sends a message. A "New message" screen presents the reachable
recipients, and starting a conversation checks that the student may indeed
contact that recipient before creating the thread. A counter feeds the
unread-messages badge.

**Use case.**
> A student writes to their coordinator about a missing document, and sees the
> reply with an unread badge on their next login.

??? note "Internal details (AroundLink team)"
    Behaves the same as the office side. The student role is required at the
    module level. Thread participation is checked on each open and each reply. A
    counting endpoint feeds the badge.

## Notifications

**What it's for.** A built-in notification feed keeps the student informed of the
events in their journey (offers, validations, messages), with read-on-open, a
"mark all as read" action and a live unread counter.

**Who it's for.** <span class="al-audience">student</span>

**How it works.** The page lists the most recent notifications; opening one marks
it as read; "mark all as read" processes the whole set and returns to the
previous page. A counter feeds the badge.

**Use case.**
> A student receives a notification that their OLA has been validated and clicks
> through to see the details.

??? note "Internal details (AroundLink team)"
    Behaves the same as the mobility side. The student role is required at the
    module level. An ownership check protects the opening of a notification.
