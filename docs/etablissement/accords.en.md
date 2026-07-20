# Agreements & place distribution

The Agreements module brings together everything an institution can offer its
students: Erasmus+/IIA exchanges, non-network bilateral agreements, double degrees
and paying mobilities. Every agreement carries its places, finely distributed by
year, level, period and field, feeding directly into the catalogue students see.

## Exchange offers (inter-institutional agreements / IIA)

**What it's for.** This is the reference catalogue of the mobilities a student can
apply to: an exchange signed with a partner institution, describing academic levels,
languages, subject areas (ISCED), requirements and the number of places. The same
record doubles as the Erasmus+/IIA file, so the information is never managed twice.

**Who it's for.** <span class="al-audience">IRO manager / coordinator</span>

**How it works.** The coordinator creates or imports an exchange, then attaches one or
more mobility blocks (studies, traineeship, staff), each specifying the expected
languages, subject areas, requirements and a place allotment. Dedicated pages let you
view the information, conditions, approval status and history, sync the EWP factsheet
and notify the partner. A student's eligibility (level, period, GPA, language scores)
is checked automatically at application time.

**Use case.**
> The IRO records an Erasmus+ exchange with TU Munich: 3 Master places in engineering,
> English B2 required, IIA identifier synced with the partner over EWP.

??? note "Internal details (AroundLink team)"
    `Exchange` entity (implements `DistributesPlaces`). Its `agreementType`
    (`AgreementTypeEnum`, Erasmus+ or bilateral variants of exchange/DD/traineeship) maps
    to a `MobilityCategoryEnum` for the student view. EWP/IIA fields: iiaId, iiaCode, HEI
    ids, local/partner approval statuses, signatories, signing dates, hash, in-effect,
    terminated. `MobilitySpec` blocks (type, sending/receiving parties + ounit, contacts,
    `mobilitiesPerYear` cap, months/days, blended) with `MobilitySpecLanguage`,
    `MobilitySpecSubjectArea` (ISCED via DetailedLabel + clarification) and
    `MobilitySpecRequirement`. Eligibility computed by `Exchange::getRequirementsErrors()`.

## Place distribution (allocation matrix)

**What it's for.** Rather than a single overall number, the institution spreads its
negotiated places across a precise grid: academic year, academic level, mobility period
and subject area (ISCED). This distribution feeds the places table shown to students and
enforces each agreement's annual cap.

**Who it's for.** <span class="al-audience">IRO manager / coordinator</span>

**How it works.** On an exchange's place-distribution page, the coordinator fills in a
matrix (year × field × level × period). The system checks each mobility block's annual
cap before saving, updates the affected cells and groups levels by EQF framework so
related programmes stay together. The result is immediately visible to students.

**Use case.**
> A partner grants 4 places: the office assigns 2 to Master / Semester 1 and 2 to
> Master / Semester 2 for 2026/2027; the student sees exactly that breakdown on the
> partner's page.

??? note "Internal details (AroundLink team)"
    Matrix storage: `MobilitySpecPeriodPlace` (year, level, period, places) and
    `MobilitySpecPool` (per-level aggregate, keeps `hasSlotManagementConfigured()`
    accurate). A per-period counter `MobilitySpecPlaces` (with remaining places) is also
    maintained and drives campaign placement. Saving posts
    `period[year][isced][level][period]`; each `MobilitySpec`'s `mobilitiesPerYear` cap is
    checked before any write. Student view built by `Exchange::getStudentPlacesMatrix()`
    and `getPlaceDistributionEntries()`. Grouping by `AcademicLevel::getEqfLevel()`.

## A unified places engine

**What it's for.** Every agreement type — exchange, bilateral, double degree, paying
mobility — presents its places to students and to the administration in the same way.
The catalogue stays consistent whatever the underlying contract type.

**Who it's for.** <span class="al-audience">admin</span>

**How it works.** Each agreement type exposes its places in a common form, grouped by
mobility category (Exchange, Double Degree, Internship, Paying mobility) then by field,
year, level and period. The same construction feeds the student page and the coordinator
preview, which therefore always stay in sync.

**Use case.**
> A partner offers both an Erasmus exchange and a double degree: the student sees two
> category tabs, each with its own places grid.

??? note "Internal details (AroundLink team)"
    `App\Places` socle: `DistributesPlaces` interface, `PlaceDistributionEntry` DTO,
    `AgreementPlaceDistribution` adapter. Per-type providers (`BilateralPlacesProvider`,
    `DoubleDegreePlacesProvider`, `PayingPlacesProvider`) aggregated by
    `StudentPlacesViewBuilder`. Student category = `MobilityCategoryEnum` (EXCHANGE,
    DOUBLE_DEGREE, INTERNSHIP, PAID_MOBILITY), distinct from the contract type
    `AgreementTypeEnum`.

## Bilateral agreements

**What it's for.** Manages non-Erasmus partnerships built on a genuine negotiation
between two institutions — one owner (paying offer), one partner (free offer) — with
their own place distribution. Covers cooperation outside the EWP/Erasmus network.

**Who it's for.** <span class="al-audience">IRO manager / partner</span>

**How it works.** The owning institution drafts an agreement, then submits it; the
partner reviews, approves or modifies it. Any edit by either side restarts the cycle
until both approvals line up: the agreement then becomes active. A place-distribution
matrix is filled in for student mobilities. An import with preview is available.

**Use case.**
> A French school signs a bilateral exchange with a Brazilian partner outside Erasmus;
> both coordinators approve in the tool, then the French side distributes 2 Master
> places in Semester 1.

??? note "Internal details (AroundLink team)"
    `BilateralAgreement` (keyed by `agreementId`, forward/reverse rows per direction),
    status `BilateralAgreementStatusEnum{DRAFT, PENDING_PARTNER, IN_NEGOTIATION,
    PENDING_INTERNAL, ACTIVE, EXPIRED, RENEWAL, OPEN_ENDED}`. Places in
    `BilateralAgreementPeriodPlace` (agreementId, subjectArea/ISCED, year, level, period,
    places). Submit/approve workflow in `BilateralAgreementWorkflow`, CSRF-guarded.
    Submission mirrors contacts into the partner's Relationship section.

## Double degrees

**What it's for.** Manages double-degree partnerships, where a student earns a degree at
both institutions over several years: yearly phases, joint curriculum, graduation
conditions and common jury. A different framework from a simple exchange.

**Who it's for.** <span class="al-audience">IRO manager / partner</span>

**How it works.** Same two-sided negotiation as bilateral agreements (drafting,
submission, approval), with an invitation sent to the partner signatory at submission.
The agreement carries curriculum, graduation, jury, EQF level and duration information,
plus yearly phases (Year 1 / Year 2). Places are distributed via a dedicated matrix. An
import with preview is available.

**Use case.**
> A Master double degree with Georgia Tech over 2 years: the student goes abroad in year
> 2; the office tracks each phase and distributes the yearly places.

??? note "Internal details (AroundLink team)"
    `DoubleDegreeAgreement` (keyed by `agreementId`), status `DoubleDegreeStatusEnum`
    (same 8 states as bilateral), fields: durationYears, yearlyPlaces, partnerDegreeName,
    jointCurriculum, sender/receiver graduation conditions, commonJury, eqfLevel,
    `fundingProgram`. Phases `DoubleDegreePhase{YEAR_1, YEAR_2}`. Transcripts (ToR) are
    collected the classic way, via the student's document upload. Places in
    `DoubleDegreePeriodPlace`. Workflow `DoubleDegreeWorkflow`.

## Paying mobility (study abroad)

**What it's for.** Manages fee-based "study abroad" placements, where the student pays
tuition to the host institution and the home institution owns the agreement end to end.
Distinguishes fee-generating mobility from free Erasmus exchange.

**Who it's for.** <span class="al-audience">IRO manager (creation) · student (viewing the price)</span>

**How it works.** The coordinator drafts then publishes the agreement (a single owner,
with no two-sided negotiation phase): fee amount, currency, subtype (individual placement
or high volume), duration and mobility type. They then distribute places via the
distribution matrix. When an institution offers paying mobility, these offers are visible
to students (in "Find Exchange") with their indicative price, so the student knows the cost
before applying. An import with preview is available.

**Use case.**
> A partner in the US where the student pays $12,000 in tuition: the office records it as
> a "study abroad" paying agreement and publishes 5 places for the year.

??? note "Internal details (AroundLink team)"
    `PayingMobilityAgreement` (keyed by `agreementId`), status `PayingMobilityStatusEnum{DRAFT,
    ACTIVE, EXPIRED, OPEN_ENDED, MODIFIED}` (no negotiation states — single-sided). Fields:
    `agreementSubtype` (STUDY_ABROAD, HIGH_VOLUME), totalFeeAmount, currency, mobilityType.
    `publish()` action (no submit/approve). Places in `PayingMobilityPeriodPlace`. Workflow
    `PayingMobilityWorkflow`. Module reserved for the paying plan.

## Agreement CSV imports

**What it's for.** Lets you load agreements in bulk from a spreadsheet rather than one by
one, with a preview-and-correct step before validation to catch bad rows. Speeds up
onboarding of large partner portfolios.

**Who it's for.** <span class="al-audience">IRO manager</span>

**How it works.** Each agreement family (exchanges, IIA, bilateral, double degree, paying)
has its own import page. The file is first parsed and checked row by row in a preview,
where each row can be corrected, before a final validation that saves everything. File
templates are downloadable.

**Use case.**
> An office pastes 80 exchanges from a legacy spreadsheet, fixes 3 flagged rows in the
> preview, then validates.

??? note "Internal details (AroundLink team)"
    Importers: `ExchangesImporter`, `IiaAgreementImporter`, `BilateralAgreementImporter`,
    `DoubleDegreeImporter`, `PayingMobilityImporter`. Common three-step flow: preview
    (parse + validation), single-row correction, confirm (persistence).
