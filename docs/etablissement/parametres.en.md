# Settings & team

**Settings** bring together your institution's administrative configuration: its
structure (campuses, organizational units, academic levels), team and permissions
management, the user directory, personalised working views, and the connection to
external systems. It is the control centre of the international relations office.

## Campuses

**What it's for.** Declare your institution's campuses (name, city, country, one
main campus), to attach students to a campus and reflect your real structure.

**Who it's for.** <span class="al-audience">RI manager / admin</span>

**How it works.** A management screen (Settings ▸ Institution) lists the campuses
with the number of students attached to each. Deletion is blocked while students
are still attached, to prevent any loss of link.

**Use case.**
> A multi-site school declares its Paris and Lyon campuses, then assigns students
> to each.

??? note "Internal details (AroundLink team)"
    `CampusesController`. `Campus` entity (university, name, city, country, main
    flag). Deletion checks the number of attached students. Ownership is checked on
    edit and delete.

## Organizational units (OUnits)

**What it's for.** Maintain your institution's EWP organizational units (faculties,
departments), so Erasmus (EWP) data exchange references the correct
sub-structures.

**Who it's for.** <span class="al-audience">RI manager / admin</span>

**How it works.** A management screen lists the units, each with a name, an
optional description and an identifier. It works like the campuses screen.

**Use case.**
> The office declares the "Faculty of Engineering" as a unit with its EWP
> identifier.

??? note "Internal details (AroundLink team)"
    `OunitsController`. `Ounit` entity (university, name, description, unit
    identifier). Screen modelled on the campuses one.

## Custom academic levels

**What it's for.** Name your academic levels with your own vocabulary (for example
"Aéro 4", "M1 Ingé") while keeping a standard mapping (EQF) behind the scenes — so
dropdowns are familiar to your team and EWP exchange stays standards-compliant.

**Who it's for.** <span class="al-audience">RI manager / admin</span>

**How it works.** A management screen (Settings ▸ Institution) lets you create,
edit and delete your level labels, each mapped to an EQF level. Each row shows how
many places or agreements use that level. Duplicate labels are rejected.

**Use case.**
> An engineering school defines "Aéro 4" mapped to EQF 7, to filter campaigns and
> agreements by its real level names.

??? note "Internal details (AroundLink team)"
    `AcademicLevelSettingsController`. `AcademicLevelCustom` entity (university,
    label unique per institution, EQF level). Consuming entities store the standard
    EQF value, not the label, to preserve EWP/OLA export compatibility.

## Key to connect external systems

**What it's for.** Give your institution a key to connect AroundLink to your
external systems (data exchange, integrations), with the ability to renew it when
needed.

**Who it's for.** <span class="al-audience">admin</span>

**How it works.** A page shows your connection key and offers a "Regenerate" action
that replaces the existing key with a new one. Keep this key confidential: share it
only with the people configuring your integrations.

**Use case.**
> After a change in the technical team, the admin regenerates the key to revoke the
> old one.

!!! warning "Confidentiality"
    A connection key is a sensitive credential. Never share it publicly, and
    regenerate it if you believe it may have been exposed.

??? note "Internal details (AroundLink team)"
    `ApiKeyController`. The key is created on first visit and renewable in one
    click. Attached to the user's account.

## Saved views

**What it's for.** Save a table configuration (chosen columns, widths, filters,
sort order) on a given page, then reapply it in one click. Each coordinator
instantly recovers their working layout without rebuilding it every time.

**Who it's for.** <span class="al-audience">RI manager</span>

**How it works.** On a table page, you adjust the columns, filters and sort, then
save that layout as a view. You can then switch between your views in one click.
Views are private to your institution.

**Use case.**
> A coordinator saves a "Spain partners — active agreements" view with its columns
> and filters, and reopens it in one click each session.

## Team & invitations

**What it's for.** Manage your office's members: prepare their accounts ahead of
time, then open access at the right moment. Ideal for a grouped start on launch
day.

**Who it's for.** <span class="al-audience">admin</span>

**How it works.** You create the team's accounts in a "pending" state, with no
email sent. When ready, you open access individually or for all pending accounts
at once: each member then receives their invitation. Sends are error-tolerant — a
single failure does not interrupt the whole batch.

**Use case.**
> During setup, the admin prepares 8 accounts (pending), then clicks "Send all
> access" on launch day.

??? note "Internal details (AroundLink team)"
    `SettingsController::team()` and access sends. Access status (pending /
    invited…). Invitations go out via a dedicated email. Each new member is also
    linked to the existing partner contacts that concern them.

## Roles & permissions

**What it's for.** Define precisely who can see and edit what, through custom roles
and a per-module permission matrix. Each institution tailors access to its
organisation.

**Who it's for.** <span class="al-audience">admin</span>

**How it works.** You create roles, then set, for each role and each module of the
application, an access level (for example read or read/write) in a matrix. Changes
apply to all members holding the role.

**Use case.**
> The admin creates a "Coordinator" role with write access to partners but
> read-only access to settings.

??? note "Internal details (AroundLink team)"
    `SettingsController::roles()`. Roles per institution, permission matrix by
    module and access level. Permissions drive access to the various areas of the
    Mobility space.

## User directory

**What it's for.** A read-only overview of all the users linked to your institution
— students, team members and invited partner users — filterable by type, status
and free-text search.

**Who it's for.** <span class="al-audience">RI manager / admin</span>

**How it works.** A page gathers all the organisation's users and lets you filter
them by category, status or name/email. It is reserved for paid mobility plans.

**Use case.**
> The admin searches a user by email to check their status and category.

??? note "Internal details (AroundLink team)"
    `SettingsController::users()`. Read-only aggregated view built by a dedicated
    service, reserved for institutions on a paid plan.
