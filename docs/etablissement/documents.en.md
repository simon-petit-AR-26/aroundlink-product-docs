# Documents & validation

The Documents module brings together, in one place, everything your international
relations office needs to produce, review and validate during a mobility: the learning
agreement (Learning Agreement / OLA), the transcript of records, students' administrative
files and official document templates. The goal: a clear flow, a single queue for
validations, and Erasmus+ rules applied automatically.

## Learning Agreement (OLA)

**What it does.** The Learning Agreement describes the programme of courses a student
will follow abroad. This view lets the office track every agreement, see at a glance
which ones are pending, validated or need corrections, and enforce the signature of both
institutions before an agreement becomes final.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** The coordinator opens the OLA list, filters by status and reviews each
agreement in a window that shows its history. They can request modifications — the
agreement then returns to draft with a comment for the student — or approve it. For a
standard agreement, each institution signs on its own side, in any order, and the
agreement is validated only once both signatures are in place; for an EWP agreement,
approval hands the agreement to the host institution following the network's sequential
flow.

**Use case.**
> The coordinator reviews Marie's pre-departure OLA (3 courses, 18 ECTS), asks her to
> swap one course, then signs on behalf of the sending institution; as soon as the
> partner signs in turn, the OLA becomes "Validated".

??? note "Internal details (AroundLink team)"
    Statuses (`LearningAgreementStatus`): Draft, Selected by student, Pending sending
    school validation, Pending receiving school validation, Validated, Refused by
    receiving school. Steps (`LearningAgreementStep`, official OLA wording): Before /
    During / After the mobility (1/3, 2/3, 3/3).

    Non-EWP agreement = parallel signing (`sendingSchoolSignedAt` /
    `receivingSchoolSignedAt`), validated once `areBothSchoolsSigned()` ; EWP agreement =
    sequential progression via the status. A refusal sends the OLA back to draft,
    re-editable by the student. Amendment tables (A2/B2) trigger a fresh signature cycle
    (`resetForAmendments()`).

    On full validation, the LA signature date is carried over to the linked grant
    (bridge to the Mobility grants module). Every mutating action checks that the student
    belongs to the coordinator's scope.

## PDF generation: OLA & transcript of records

**What it does.** Produces the official PDF of the learning agreement or the transcript
of records from the institution's document template (letterhead, layout), with the
student's course table inserted automatically. The office gets a document ready to file,
in the institution's colours.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** From the OLA list, the coordinator downloads the PDF of the learning
agreement or the transcript of records. The agreement can only be downloaded once fully
validated; the transcript once the transcript itself is validated. The system fills the
template with the courses (and the grades, for the transcript).

**Use case.**
> After both signatures, the coordinator downloads the Learning Agreement as a PDF, on
> the institution's letterhead, for the student's file.

??? note "Internal details (AroundLink team)"
    The PDF reuses the institution's active template for the requested type (see
    "Document templates"). The `{{COURSES_TABLE}}` / `{{COURSES_TABLE_WITH_GRADES}}`
    tokens are resolved with the agreement's courses. If no active template of the type
    exists, a message points to Settings → Document templates.

## Transcript of Records (ToR)

**What it does.** Manages the incoming student's transcript that the host institution
must return to the home institution. The coordinator reviews the entered grades and the
uploaded official transcript, then validates or requests corrections.

**Who it's for.** <span class="al-audience">RI manager / coordinator (validation) ; student (entry)</span>

**How it works.** The student enters each grade according to the chosen grading system
and uploads the official transcript. The coordinator opens the transcript in a window
showing the history and the uploaded document, then validates — the transcript becomes
downloadable — or sends the file back to the student for correction.

**Use case.**
> An incoming student uploads their official transcript and enters their grades; the
> coordinator checks, validates, and the transcript of records is ready to be sent to
> the home university.

??? note "Internal details (AroundLink team)"
    Statuses (`TranscriptOfRecordStatus`): Pending student filling grades, Pending
    validation by school, Validated by receiving/sending school, Refused by
    receiving/sending school. Student submission requires a valid grade (per
    `GradingSystemEnum`) for every course.

    Business validation "makes faith": approving aligns the uploaded official file to the
    validated state, which ticks the "transcript of records" item on the grant side and
    satisfies the closure condition. A modification request un-ticks the grant.

## Validation Hub

**What it does.** A single queue where the coordinator validates everything the student
submits during their mobility — administrative files, learning agreements, transcripts
and testimonials about partners — without having to browse several screens. Items that
have been waiting a long time are flagged as urgent, and every decision is archived with
its author, its outcome and the refusal reason.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** The queue gathers pending documents, OLAs awaiting the institution's
signature, transcripts and testimonials, with counters (pending / students concerned /
urgent). The coordinator opens each item and decides to validate or refuse; a comment is
required when refusing. A "History" tab lists past decisions with their reason.

**Use case.**
> Monday morning, the coordinator sees 12 pending items, 3 of them urgent: they validate
> two passports, sign one OLA on behalf of the sending institution, and refuse an
> unreadable insurance certificate with a comment — all from the same queue.

??? note "Internal details (AroundLink team)"
    Four item types (StudentFile, non-EWP LearningAgreement awaiting signature,
    TranscriptOfRecord, Feedback). Reason stored per type (`refusal_reason` for files,
    a history row for LA/ToR/Feedback, ticket AROUNDLINK-548). Urgent = waiting ≥ 7 days.

    Business guard: an arrival/departure certificate can only be validated if the student
    has declared the matching date (it conditions the grant payment). Testimonial
    moderation: validating can also publish; refusing always hides. Nominations do not go
    through this queue.

## Students' administrative files

**What it does.** A central page listing all files uploaded by students (passport,
insurance, language tests, arrival/departure certificates, etc.) with their status. The
office validates or refuses files one by one or in bulk, records arrival dates and
launches reminder campaigns to students whose documents are missing or were refused.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** The coordinator filters the file list, validates or refuses several at
once, enters a student's arrival date, estimates how many students would be reminded,
then triggers a reminder campaign in one click.

**Use case.**
> The coordinator filters on "Refused", selects 8 files, refuses them in bulk with a
> comment, then sends a reminder to the students concerned.

??? note "Internal details (AroundLink team)"
    Statuses (`StudentFileStatusEnum`): Pending / Validated / Refused (with
    `refusal_reason`). Bulk validations re-check that each file belongs to the
    coordinator's scope. The arrival date rejects future dates and drives the grant
    balance payment. Validating a file can feed the linked grant's checklist.

## Document templates

**What it does.** Lets each institution design its own reusable document templates
(nomination letter, learning agreement, acceptance letter, enrolment certificate,
transcript of records, visa certificate, housing certificate) with `{{…}}` fields that
fill automatically with a student's real data.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** The coordinator lists, creates and edits their templates, composes the
document body using the available variables, previews the layout as a PDF (tokens still
visible) to check spacing and pagination, then generates a filled PDF for a given
student. They can activate/deactivate a template or delete it. Institutional templates
made available are visible read-only.

**Use case.**
> The coordinator creates an "Acceptance Letter" template with the institution's logo,
> checks the preview, then generates it filled for an incoming student in one click.

??? note "Internal details (AroundLink team)"
    Types (`DocumentTemplateTypeEnum`, closed set, DB-enforced): nomination_letter,
    learning_agreement, acceptance_letter, enrollment_certificate, transcript,
    visa_certificate, housing_certificate. Fields: name, type, mobility type (default
    "ALL"), content, active/inactive, owner, home university.

    Each coordinator owns their own pool; institutional templates (no owner) are visible
    to coordinators of the targeted university but editable only on the admin side.
    Generation is restricted to students of the coordinator's own university. Variables
    come from `DocumentVariableEnum`.

## Enable / disable document types

**What it does.** Lets each institution enable or disable certain document types, so an
unwanted type stops appearing on the students' upload page and in dropdown lists. By
default, all types are active.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** In Settings → Documents, each document type has an ON/OFF switch saved
per institution.

**Use case.**
> An institution that never issues housing certificates disables that type: it
> disappears from every student's checklist.

??? note "Internal details (AroundLink team)"
    Deactivation by the presence of a `DisabledDocumentType` row, unique per (university,
    file type). No row = active type (default behaviour preserved). The list of disabled
    types drives the display on the student side.

## Agreement update review (IIA)

**What it does.** When a partner institution pushes changes to an inter-institutional
agreement (IIA) over the EWP network, this review shows a field-by-field comparison and
lets you selectively accept or reject the changes before they touch local data.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** The coordinator opens the pending update and sees the comparison
between their version and the partner's. They tick the fields to accept and apply — a
count of applied/skipped fields is shown — or reject the update, in which case their data
stays unchanged.

**Use case.**
> The partner changes the agreement's ECTS and languages; the coordinator accepts the
> language change but rejects the ECTS one — only the accepted field is written locally.

??? note "Internal details (AroundLink team)"
    Pending-update statuses (`ExchangeIiaPendingUpdateStatusEnum`): PENDING_REVIEW /
    REJECTED. Applying is only possible while the update is under review. Author,
    timestamp and review notes are kept. Returns to the agreements list after the
    decision.
