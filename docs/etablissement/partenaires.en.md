# Partners & institution files

The **Partners** module brings together, in one place, every institution your
international relations office works with: where they are, what agreements bind
you, how many places remain open, and the state of their official data. Each
partner has a complete file that your students and your team consult throughout
the year.

## Partner directory

**What it's for.** A single, filterable table of all your partner institutions.
It gives an immediate overview — country, city, accreditations, tags, languages,
levels, remaining places, number and type of agreements — and acts as the entry
point into each partner file.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** The directory lists the partners your institution tracks (those
you have an agreement with or that you created). You filter the list straight from
the search bar, then click a row to open the file. A toggle switches the same
table to the consolidated agreements view.

**Use case.**
> A coordinator filters on "Spain + active agreements", then opens a university's
> file to check its contacts.

??? note "Internal details (AroundLink team)"
    `UniversityController::universities()`. Visibility relies on the "tracked"
    relationship (`trackedBy`) or an existing `Exchange` with the client. Grid
    relations (factsheet, contacts, exchanges) are batch-loaded to avoid N+1
    queries. Only the current institution's tags are shown. A badge flags pending
    IIA updates.

## Create a partner institution

**What it's for.** Register a new partner not yet on the platform, capturing its
identity, location, official identifiers and at least one main contact. The
partner immediately becomes visible in the directory and available for agreements.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** A form pre-fills a main contact card (mandatory). On save, the
partner is automatically attached to your institution and its contacts are linked
to any matching existing accounts. You are then redirected to the full file to
keep editing.

**Use case.**
> The office signs a new partner in Portugal; the coordinator adds it with its
> Erasmus code and the receiving coordinator as main contact.

??? note "Internal details (AroundLink team)"
    `UniversityController::newUniversity()`. The explicit attachment to the client
    is required for the institution to appear in the directory. Contact–account
    linking happens after the save. Duplicates (code, EWP identifier, contact
    email) are reported with a message.

## Institution file (Information)

**What it's for.** The editable identity card of a partner: description,
accreditations, links, private tags, internal code, logo and photo. Everything the
office wants to remember about a partner is centralised here.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** One page combines the information form, logo and photo uploads,
and the expected language-scores block. Descriptive fields are editable; the
official technical identifiers stay read-only. Saving only affects your own tags
and your internal code for that partner; other institutions' data on a shared
partner is never modified.

**Use case.**
> The coordinator tags Bologna as "Priority" and records the office's internal
> reference for that institution.

??? note "Internal details (AroundLink team)"
    `UniversityController::informationUniversity()`. `University` entity: code,
    name, country, city, address, email, school type (business / engineering /
    university), mobility plan (paid / free), accreditations (22 values: AACSB,
    EQUIS, CTI, Qualiopi…), EWP identifiers (HEI ID, SCHAC, Erasmus code, ROR).
    Logo and photo handled via `UniversityFile`. An error message is always shown
    when validation fails.

### Partner tags

**What it's for.** Define your own colour-coded labels (for example "Priority",
"Double degree", "Watch") and apply them to partners for grouping and filtering.
Tags are private to the institution that creates them.

**Who it's for.** <span class="al-audience">RI manager / admin</span>

**How it works.** A management screen (Settings ▸ Institution) lets you create,
edit and delete tags, each with a name and a colour. Tags are applied from the
partner file and appear as badges and filters in the directory.

**Use case.**
> The office creates a red "Suspended" tag and applies it to two partners whose
> agreements have expired.

??? note "Internal details (AroundLink team)"
    `PartnerTagsController`. `PartnerTag` entity (owner, name, colour, many-to-many
    to universities). Ownership is checked on edit and delete.

### Partner internal code

**What it's for.** Record your own internal identifier for each partner, distinct
from the official code, to map partners onto your existing spreadsheets or
management tools.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** It's not a separate screen: just a field on the partner file.
Left blank, it clears the code; filled in, it creates or updates a reference
private to your institution. It appears as a column in the directory.

**Use case.**
> The coordinator records the internal reference "IT-BOL-01" for Bologna.

??? note "Internal details (AroundLink team)"
    `PartnerInternalCode` entity (institution, partner, code), unique per
    institution/partner pair. Managed inline on the Information file.

### Expected language scores

**What it's for.** Record the language-test thresholds a partner expects from
incoming students (for example IELTS 6.5, TOEFL 90, B2), on the same scale
students declare — so the two can be compared directly during selection.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** A management block (add, edit, delete via a dialog) on the
partner file. Each entry reuses the student-score structure: test type, overall
score, the four sub-scores and an optional CEFR level.

**Use case.**
> The coordinator records "Lund: IELTS 6.5 / B2"; a student at IELTS 6.0 is then
> flagged below the threshold.

??? note "Internal details (AroundLink team)"
    `UniversityLanguageScoreController`. `UniversityLanguageScore` entity, same
    structure as student scores, attached to the university.

## Partner contacts

**What it's for.** A directory of the people the office deals with at each partner,
one designated as main. These contacts feed the agreement and signatory dropdowns.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** Two entry points: a global list of your contacts and a
"Relationship" tab per partner. Each contact has name, email, phone, position and
a "main" flag. On save, a contact is automatically linked to a matching existing
account.

**Use case.**
> The coordinator adds a partner's Erasmus officer and marks them as the main
> contact.

??? note "Internal details (AroundLink team)"
    `UniversityContactController` (global) and `UniversityController::contactsUniversity()`.
    `UniversityContact` entity (described partner, owning institution, main flag,
    optional linked account). Automatic per-institution scoping. Deletion is
    protected when the contact is referenced by an agreement.

### Open portal access (invitations)

**What it's for.** Open partner-side access for a contact so they collaborate
directly (for example to approve an agreement). In one click, the system invites
the contact, links them to an existing account, or reports a conflict.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** From a partner contact, "Open access" sends an email invitation;
a "Resend" action re-issues it. Both are rate-limited to avoid repeated sends.

**Use case.**
> The coordinator invites the partner's Erasmus officer so she can review an
> agreement in her own portal.

??? note "Internal details (AroundLink team)"
    `invitePartnerContact()` / `resendPartnerContactInvite()`. Create-or-link-or-invite
    flow. The same mechanism fires automatically when a bilateral agreement is
    submitted to a partner.

## Consolidated agreements view

**What it's for.** A unified view merging Erasmus (IIA) and bilateral agreements
across all your partners, to see and filter in one place each agreement's status,
validity years, signing date and approval state.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** A toggle switches the directory to this normalised view, one row
per agreement. Each row shows the partner, the source (IIA or bilateral), the
type, the status (active / inactive / terminated), local and partner approval, and
the validity years.

**Use case.**
> The office filters "All agreements" on "Expired" to plan renewals.

??? note "Internal details (AroundLink team)"
    `UniversityController::agreementsData()`. IIA rows come from `Exchange`,
    bilateral rows from the bilateral repository. Agreement detail is documented on
    the dedicated [agreements](accords.md) page.

## Institution lookup (autocomplete)

**What it's for.** Speed up data entry by suggesting known institutions as you
type, to attach partners and agreements to the right, correctly-named institution.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** A field suggests the institutions matching your input;
autocomplete is built into the relevant forms.

**Use case.**
> Typing "sorbon" suggests "Sorbonne Université" with its identifiers.

??? note "Internal details (AroundLink team)"
    `UniversityLookupController` + `UniversityLookupService`. JSON endpoint exposed
    to the forms.

## Partner student content

**What it's for.** Compose the practical information students see about a partner
(description and content blocks grouped by category), to give consistent guidance
approved by the office.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** An editor with a description field and the add, edit or delete of
content blocks grouped by sub-category. A bulk import can also load this content
from a file.

**Use case.**
> The office fills in the "Housing" and "Visa" blocks of a partner so they appear
> on its student page.

??? note "Internal details (AroundLink team)"
    `cmsUniversity()`, `deleteUniversityCmsBlock()`, `studentInfoImport()`.
    `UniversityCms` blocks (sub-category, content, position). Categories depend on
    the CMS reference data.

## Partner document library

**What it's for.** Keep the files attached to a partner (signed agreements,
brochures…), to gather all partner documents in one place.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** You upload named documents to a partner (duplicate names are
rejected), list them, and delete them individually.

**Use case.**
> The coordinator uploads the signed cooperation-agreement PDF to the partner
> file.

??? note "Internal details (AroundLink team)"
    `documentsUniversity()` / `deleteDocument()`. `UniversityFile` entity
    (university document type), handled via the file manager.

## Partner course catalogue

**What it's for.** Maintain the list of courses available at a partner for the
exchange, so students and the office know what can be studied there.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** You add courses via a form and delete them per partner; they are
listed by code.

**Use case.**
> The office records the 12 English-taught master's courses a partner offers to
> incoming students.

??? note "Internal details (AroundLink team)"
    `courses()` / `courseDelete()`. `Course` entity attached to the university,
    listed by code via the dedicated repository.

## Partner web & social links

**What it's for.** Record a partner's website and social networks, so students and
staff can reach its official channels.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** A form edits the website, Instagram, LinkedIn, Twitter and
Facebook, with a save confirmation and a clear flag when something is wrong.

**Use case.**
> The coordinator adds a partner's Instagram so it appears on the student page.

??? note "Internal details (AroundLink team)"
    `linksUniversity()`. Link fields carried by the `University` entity.

## Student-feedback moderation

**What it's for.** Review, accept (and publish) or refuse the feedback students
leave about a partner, controlling what future students see while keeping a record
of each decision.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** A view by status (pending / accepted / refused) with counters.
Accepting can publish the review (visible to students) or keep it hidden; refusing
hides it and records a reason. Each decision writes a history entry with the
author.

**Use case.**
> A coordinator reads a pending review, publishes the positive ones and refuses an
> inappropriate one with a reason.

??? note "Internal details (AroundLink team)"
    `feedbackUniversity()` + accept / refuse actions. Statuses pending / accepted /
    refused, publication flag, moderation history. Moderation is only possible on a
    partner you track.

## Preview as student

**What it's for.** Show the office exactly what a student sees on a partner's page
— places by category, level and field, requirements, published reviews — to verify
the file before students rely on it.

**Who it's for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** The preview displays the partner's student page, with place
distributions gathered across all agreement types, filterable by year, level and
field. With no student profile, filters start on "All".

**Use case.**
> Before a campaign opens, the coordinator previews a partner to confirm the
> display of places and requirements.

??? note "Internal details (AroundLink team)"
    `studentPreview()`. Reuses the same builders as the real student view (places,
    requirements, agreement table, map).

## Import partner institutions

**What it's for.** Bulk-load or refresh many partners from an Excel file, with
strict header checking so a badly-filled template doesn't silently import zero
rows.

**Who it's for.** <span class="al-audience">RI manager / admin</span>

**How it works.** You upload the file; headers are checked up front (missing or
unknown columns flagged); rows are imported and a failing row is skipped without
blocking the others. Re-importing an existing institution refreshes its filled-in
fields. A summary reports creations, updates and skipped rows.

**Use case.**
> The office uploads 300 partners: 280 created, 20 updated, a header typo caught
> before any save.

??? note "Internal details (AroundLink team)"
    `universitiesImport()` + header validation. `UniversityImporter` (created /
    updated / linked / processed counters). A preview is available before
    confirmation. Values from the file are escaped on display.

## Import partner contacts

**What it's for.** Bulk-load partner contacts from a CSV or Excel file, matching
them to partners by email domain, with a preview before writing.

**Who it's for.** <span class="al-audience">RI manager / admin</span>

**How it works.** You upload the file, a preview is shown without writing anything,
then you confirm. A failing row is skipped, the others continue. The summary
reports creations, updates, skipped rows and email domains matching no known
partner.

**Use case.**
> The office uploads a contact list: each one joins the right partner, and 3
> unknown domains are flagged.

??? note "Internal details (AroundLink team)"
    `UniversityContactsImportController`. `UniversityContactsImporter` (not-found
    domains, created / updated contacts). Preview before confirmation.
