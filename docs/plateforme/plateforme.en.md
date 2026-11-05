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

## What you write about a partner is yours

**What it is for.** Separating what describes a partner institution from what
**you**, as a client, have recorded about them. Two institutions can work with the
same partner without ever seeing each other's notes.

**Who it is for.** <span class="al-audience">RI manager / coordinator</span>

**How it works.** The content you enter about a partner carries your institution's
mark and never leaves your workspace:

- the **information you publish to your students** about that partner (resources,
  links, FAQ);
- the **course catalogue** you maintain for them;
- the **language scores** you declare as a requirement;
- the **files** you upload to their record, which keep track of who added them.

Another client working with the same partner keeps their own version of all this,
with no interference.

**Use case.**
> Two French institutions send students to the same Spanish university. Each keeps
> its own course catalogue and its own guidance there, never seeing the other's.

!!! info "Identity belongs to the institution"
    A partner's name, country, city, address, email address, website and
    accreditations can only be edited **by that institution itself**, from its own
    workspace. You cannot change them from their record: this identity is unique and
    serves everyone — search, Atlas, ROR matching, EWP exchanges. What you control on
    their record is your own layer: your internal code and your tags.

    Official identifiers — ROR, Erasmus code, EWP id, SCHAC — cannot be edited by
    anyone: they are the reference.

## Account types

**What it is for.** Three user profiles coexist, each with its own space and
rights, so that each party only sees what concerns them.

**Who it is for.** <span class="al-audience">IRO coordinator · student · partner</span>

**How it works.** There are:

- the **IRO coordinator** (mobility officer) who works in the institution workspace;
- the **student** who accesses their [personal space](../etudiant/decouverte-candidature.md);
- the **partner** — a contact at a partner institution. They receive their access when you
  nominate a student to them: they land in **their own space**, where they only find the
  students you send them and your fiche, never the rest of yours.

**Use case.**
> A school nominates three students to a partner. Its Erasmus officer receives the message,
> opens their access, and reviews the three files — seeing nothing else.


## Team roles & permissions (RBAC)

**What it is for.** Within an institution, you define custom team roles and set, section
by section, what each role can do. A large IRO can delegate without opening everything to
everyone.

**Who it is for.** <span class="al-audience">IRO coordinator (institution administrator)</span>

**How it works.** A role says **who it covers** — business domains, outgoing or incoming,
campuses, promotions — then **what it can do**, section by section of the menu, with four
levels: **None**, **View**, **Prepare** (the file moves forward inside your institution),
**Decide** (it leaves the tool: validate, send, export). Setting a category is enough,
everything inside follows; refine section by section if needed. A user without rights does
not see the menu entry and cannot reach it through a direct address either. Details in
[Settings & team](../etablissement/parametres.md#roles-permissions).

**Use case.**
> The head of office creates an "Incoming officer" role: incoming only, Lyon campus,
> "Decide" on documents, "View" on agreements, "None" on grants.


## Sign-in & single sign-on (SSO)

**What it is for.** Your staff and students sign in with the account they already have —
Microsoft or Google — rather than with one more password. Your institution can also enforce
it.

**Who it is for.** <span class="al-audience">The institution's staff and students</span>

**How it works.** The sign-in screen offers everyone, at all times, the password and the
**Sign in with Microsoft** and **Sign in with Google** buttons. Each user **links their own**
account from their profile, once, then signs in with it. Password sign-in offers a reset by
link.

**Use case.**
> A coordinator links her work Microsoft account from her profile. The next day she clicks
> "Sign in with Microsoft" and gets in without a password.

!!! info "Are you in IT?"
    Protocol, requested permissions, enforced sign-in, security checks:
    **[Single sign-on (IT)](sso.md)**.


## Application access (API key & EWP network)

**What it is for.** Machine access, separate from a user's sign-in, links AroundLink to
your own systems and authenticates exchanges with universities of the
[EWP](../ewp/ewp.md) network.

**Who it is for.** <span class="al-audience">IT / integrations · partner universities' systems</span>

**How it works.** Two kinds of keys, under **Settings ▸ Connectors ▸ API**:

| Key | Who owns it | What for |
|---|---|---|
| **Integration key** | the **institution**, not a person — it survives the departure of whoever created it | a system that runs on its own, such as your student information system; it only has its role's rights |
| **Personal key** | **one person** | occasional use; it acts with all of that person's rights |

A key is shown **only once**, when it is created: copy it straight away. Each row shows
the date of last use — an old date means an integration that has stopped. Replacing or
revoking a key cuts the old one off at once. The EWP network has its own, separate
authentication.

The API is documented in OpenAPI format:
[api.aroundlink.com/apis/docs](https://api.aroundlink.com/apis/docs); for the EWP network,
see the [API reference](../ewp/reference-api.md).


## Contextual help

**What it is for.** Give every screen its own instructions, without leaving the
page or hunting through separate documentation.

**Who it is for.** <span class="al-audience">every signed-in user</span>

**How it works.** A "?" button sits at the top right of every page. It opens a
panel explaining what you can do here, in French and in English, sometimes with a
short video. The panel closes as soon as you change page: what you read always
matches the screen in front of you.

Each text ends with a booking link: if the explanation is not enough, you book a
fifteen-minute slot with the AroundLink team.

**Use case.**
> A new team member opens the place-distribution screen, clicks "?", understands
> how the grid works, and fills it in without having to ask.

## Service marketplace

**What it is for.** A catalog of third-party services (insurance, housing,
banking…) that can be shown to students, switchable on per institution. A value-add
space, shown only where it is enabled.

**Who it is for.** <span class="al-audience">Student (browsing) · AroundLink (curation)</span>

**How it works.** The catalog of providers and offers is maintained by AroundLink; a
per-institution switch decides whether the marketplace appears to that institution's
students. When on, students see the offers in their
[Services space](../etudiant/pendant-apres-mobilite.md), sorted by category and saveable
to their favourites. An institution can individually set aside an offer it does not want
shown to its students. This is display + affiliation (links and promo codes to the
provider): no payment goes through AroundLink — the student subscribes on the partner's
site.

**Use case.**
> AroundLink adds a "Student health insurance — from €9/month" offer; it appears to
> students of marketplace-enabled institutions.

