# Platform & security

AroundLink is a **multi-tenant SaaS** platform. This page describes the
cross-cutting model: data isolation, account types, permissions, sign-in, and
commercial plans. The detailed behaviour of each screen lives in the dedicated
modules — this page sets the frame.

## Data isolation (multi-tenancy)

**What it is for.** Each client institution only ever sees its own data — students,
partners, agreements, campaigns, communications, views. One institution's data is
never visible to another. This is the platform's fundamental trust guarantee.

**Who it is for.** <span class="al-audience">All institution-workspace users</span>

**How it works.** When a coordinator is signed in, the platform automatically
restricts everything they see to their own institution. Genuinely shared data (such
as the global [Atlas](../atlas/atlas.md) directory) is handled separately and
clearly identified as such.

**Use case.**
> Two client universities use AroundLink on the same day; neither can see the
> other's students, agreements or grants.

## Account types

**What it is for.** Three user profiles coexist, each with its own space and
permissions, so every actor only sees what concerns them.

**Who it is for.** <span class="al-audience">IRO coordinator · student · invited partner</span>

**How it works.** There are:

- the **IRO coordinator** (mobility officer) who runs the institution workspace;
- the **student** who accesses their [personal space](../etudiant/decouverte-candidature.md);
- the **invited partner** — a contact at a partner institution granted access to
  collaborate (for example, to approve a bilateral agreement).

**Use case.**
> An institution invites a partner's Erasmus officer; they sign in to their own
> space to approve an agreement, seeing nothing else.

??? note "Internal details (AroundLink team)"
    Distinct `AdminUser` (AroundLink team), `MobilityUser` (coordinators) and
    `StudentUser` (students) accounts, all derived from a shared `User` base.
    Partner accounts are `MobilityUser`s attached to the partner institution.

## Team roles & permissions (RBAC)

**What it is for.** Within an institution, you can define custom team roles and set,
module by module, whether each role has no access, read, or write. This lets a large
IRO delegate safely.

**Who it is for.** <span class="al-audience">IRO coordinator (institution administrator)</span>

**How it works.** A matrix editor crosses the institution's roles (rows) with the
main functional modules (columns) — Institution, Documents, Forms, Workflow,
Integrations, Team permissions — each cell being None / Read / Write. Permissions
are enforced everywhere: a user without a right neither sees the menu entry nor can
reach it via a direct address.

**Use case.**
> The head of the IRO gives the "Assistant" role read access everywhere, but write
> access only on Documents.

??? note "Internal details (AroundLink team)"
    Roles + a per-institution permission matrix; 6 modules (`institution`,
    `documents`, `forms`, `workflow`, `integrations`, `team_permissions`) × 3 levels
    (none/read/write). Enforcement is server-side (the menu only hides). Ref.
    AROUNDLINK-348.

## Sign-in & single sign-on (SSO)

**What it is for.** Institutions can let their staff (and students) sign in with
their existing Microsoft/Azure institutional account instead of a separate password
— and can enforce it. Fewer passwords to manage and compliance with IT
requirements.

**Who it is for.** Configured by the AroundLink team per institution; used by the
institution's staff and students

**How it works.** At sign-in, the platform recognises the institution from the email
address entered; if single sign-on is enabled (or enforced), the user is redirected
to the Microsoft sign-in page, otherwise they can use a password. Password sign-in
also offers standard password reset.

**Use case.**
> A coordinator at an Azure university clicks "Sign in", enters their work email, and
> is automatically routed to Microsoft authentication.

??? note "Internal details (AroundLink team)"
    Per-institution SSO configuration (tenant id, enable, enforce, allowed email
    domains). Microsoft/Azure OpenID Connect flow. Configuration and testing happen
    from the AroundLink admin space. Authentication implementation details are not
    exposed here.

## Application access (API key & EWP network)

**What it is for.** Machine-access channels, separate from the user session, let you
connect AroundLink to external systems and authenticate exchanges with partner
universities on the [EWP](../ewp/ewp.md) network.

**Who it is for.** <span class="al-audience">IT / integrations · partner university systems</span>

**How it works.** Each institution has a regenerable API key (managed in
[Settings](../etablissement/parametres.md)) for its integrations, plus dedicated
authentication for the EWP network. These machine accesses are deliberately distinct
from browser sign-in. The REST API has interactive documentation (resources, schemas,
operations) — see the [API documentation (demo)](https://demo.aroundlink.com/api/docs)
and, for the EWP network, the [EWP API reference](../ewp/reference-api.md).

??? note "Internal details (AroundLink team)"
    Stateless `/api/*` surface (JWT / API key) separate from the app's internal
    APIs; EWP partner authentication via request signature. Never disclose a key.

## Plans: paid / free institution

**What it is for.** Each institution is either a paying or a free client; some
premium modules (for example [mobility grants](../etablissement/bourse.md) or
creating [bilateral agreements](../etablissement/accords.md)) are reserved to paying
clients. This is the platform's commercial gating.

**Who it is for.** <span class="al-audience">Client institution (set by AroundLink)</span>

**How it works.** The institution's plan (paid by default, or free) governs access
to premium modules — hidden in the menu and blocked on direct access for a free
client. This plan is independent of any tuition fees paid by the student.

**Use case.**
> A free-plan partner can review and approve a bilateral agreement a paying
> institution submitted to it, but cannot open premium modules.

??? note "Internal details (AroundLink team)"
    `MobilityPlanEnum` (paid/free), enforced server-side by a dedicated access
    check. Reusable pattern for any future premium module.

## Service marketplace

**What it is for.** A catalog of third-party services (insurance, housing,
banking…) that can be shown to students, switchable on per institution. A value-add
space, shown only where it is enabled.

**Who it is for.** <span class="al-audience">Student (browsing) · AroundLink (curation)</span>

**How it works.** The catalog of providers and offers is maintained by AroundLink; a
per-institution switch decides whether the marketplace appears to that institution's
students. When on, students see the offers in their
[Services space](../etudiant/pendant-apres-mobilite.md). This is display + affiliation
(links and promo codes to the provider): no payment goes through AroundLink — the student
subscribes on the partner's site.

**Use case.**
> AroundLink adds a "Student health insurance — from €9/month" offer; it appears to
> students of marketplace-enabled institutions.

??? note "Internal details (AroundLink team)"
    `University.marketplaceEnabled` switch. Offers/providers managed on the
    AroundLink side (outside this site); student display gated on the flag.
