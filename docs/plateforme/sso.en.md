# Microsoft single sign-on (IT departments)

!!! info "Who this page is for"
    This page is **technical**: it addresses **IT departments and infrastructure
    teams** evaluating or setting up single sign-on between their Microsoft
    directory and AroundLink. For the business value, see the
    [Overview](plateforme.md).

AroundLink supports **single sign-on through Microsoft Entra ID** (formerly Azure
AD), over **OpenID Connect**. Your users sign in with their institutional
account; no additional password is created, and no credential ever passes
through AroundLink.

## At a glance

| | |
| --- | --- |
| **Protocol** | OpenID Connect (Authorization Code, `response_mode=query`) |
| **Identity provider** | Microsoft Entra ID / Azure AD, v2.0 endpoint |
| **Scopes requested** | `openid`, `profile`, `email` — **and nothing else** |
| **Data read** | name, email address, Microsoft object identifier (`oid`) |
| **Data never requested** | mail, files, calendar, directory, groups, memberships |
| **App registration to create on your side** | **none** — see below |
| **Passwords** | never pass through AroundLink |
| **Covers** | institution staff **and** students |

!!! tip "The part that usually surprises people"
    You have **no application to register** in your directory. AroundLink is
    registered once, as a multi-tenant application. Your institution simply
    **authorises** it inside its own directory, in one click, through a link we
    provide.

## Setup procedure

Allow half a day, most of which is waiting between exchanges.

### Step 1 — You send us your tenant ID

The *Tenant ID* of your Microsoft directory: either a GUID
(`11111111-2222-3333-4444-555555555555`) or your verified domain
(`your-university.edu`).

Where to find it: **Microsoft Entra portal ▸ Overview ▸ Tenant ID**.

!!! warning "Rejected values"
    The generic values `common`, `organizations` and `consumers` are **refused**
    by the platform. A specific tenant is required — that is what guarantees only
    your users can sign in.

### Step 2 — You tell us your email domains

The list of domains allowed to sign in (`your-university.edu`,
`students.your-university.edu`…). It is **mandatory**: an enabled configuration
with no domain is refused at save time.

This list is a **second line of defence**, independent of the tenant check: even
an account from the right directory is refused if its address does not belong to
a declared domain.

### Step 3 — We record the configuration

The AroundLink team enters the tenant and the domains in the admin console, then
runs a **configuration test**: the platform queries your tenant's OpenID Connect
discovery document and confirms it is reachable and complete. Immediate result,
before anything is enabled.

### Step 4 — Your administrator authorises AroundLink

We send you an **admin consent** link prepared for your tenant. A global
administrator of your directory opens it, reads the requested permissions
(`openid`, `profile`, `email`) and accepts.

That is the only action required on your side, and it happens **once**.

Two redirect URLs are used by the flow. Their exact values are shown in the
AroundLink admin console and are given to you at this step:

| Purpose | Path |
| --- | --- |
| Authentication callback | `/sso/check` |
| Admin consent callback | `/sso/consent-callback` |

### Step 5 — Accounts must exist in AroundLink

!!! danger "Prerequisite not to miss"
    Single sign-on **connects** accounts, it does not **create** them. A user
    whose account does not yet exist in AroundLink is told "your Microsoft
    account is not provisioned" and cannot get in.

Accounts are created beforehand by the institution: importing the student list,
or creation by the international office. See
[Settings &amp; team](../etablissement/parametres.md).

On the **first** sign-in, AroundLink matches the Microsoft account to the
existing one **by email address**, then stores the immutable Microsoft
identifier. Later sign-ins rely on that identifier: an address change on your
side does not break the link.

### Step 6 — Enable, then optionally switch to strict mode

We enable single sign-on. At this point both routes coexist: password **and**
Microsoft.

Once you have confirmed that sign-in works for your users, you can ask for
**strict mode**, which removes password sign-in for every account of the
institution.

!!! warning "Do not start with strict mode"
    Strict mode removes the password fallback. Turn it on only after checking
    that at least one account really signs in through Microsoft.

## What the user experiences

1. They open AroundLink and type their work email address.
2. The platform recognises the domain and determines whether the institution uses
   single sign-on.
3. They are redirected to the Microsoft sign-in page — yours, with their address
   already filled in. Your own rules apply there: password, MFA, conditional
   access.
4. Microsoft sends them back to AroundLink, signed in, on the home page for their
   role.

There is no "SSO" button to hunt for: the email address alone routes the user.

## Per-institution settings

| Setting | Effect |
| --- | --- |
| **Enabled** | Opens Microsoft sign-in for the institution. |
| **Strict mode** | Removes password sign-in: Microsoft becomes the only way in. |
| **Allowed email domains** | Whitelist of accepted domains. Mandatory once enabled. |

The date of the **last successful sign-in** is recorded, so you can tell at a
glance that a connection is still alive.

## Checks performed on every sign-in

Each authentication goes through the following checks; failing any one of them
stops the sign-in.

- **`state` parameter** verified — protects against request forgery.
- **Single-use `nonce`**, compared with the value issued on the way out —
  protects against token replay.
- **Token tenant** (`tid`) compared with the configured tenant — a token issued
  by another directory is rejected.
- **Object identifier** (`oid`) required — it is the stable matching key.
- **Account membership** of the configured institution.
- **Email domain** present in the allowed list.
- **Initial matching refused** when no domain list is defined — the email address
  is a value a tenant administrator can change, so it cannot bind an account on
  its own.

A link to a Microsoft account is stored **only after** every one of these checks
has passed: a rejected user leaves nothing behind. One Microsoft account can be
attached to a single AroundLink account, a constraint enforced in the database.

## Account lifecycle

| Event on your side | Effect in AroundLink |
| --- | --- |
| Microsoft account disabled (leaver) | The person can no longer sign in, immediately. |
| Password changed, MFA added | Nothing to do in AroundLink: those rules are yours. |
| Email address changed | Sign-in keeps working (matching is on the Microsoft identifier, not the address). |
| New joiner | Their AroundLink account must be created first — see step 5. |

## Known limitations

Stated plainly, to avoid late surprises.

- **Microsoft Entra ID only.** Google Workspace, SAML 2.0, Shibboleth, RENATER
  and eduGAIN are **not** supported today. If your institution authenticates
  through one of those, let's discuss it — it is not available at present.
- **No automatic provisioning.** No directory synchronisation, no SCIM. Accounts
  are created by import or by the international office.
- **No group or role synchronisation.** AroundLink permissions are granted inside
  AroundLink — see [Settings &amp; team](../etablissement/parametres.md).
- **AroundLink administration accounts excluded.** The vendor's internal accounts
  never sign in through a customer's single sign-on, by design.

## Frequently asked questions

**Do we need to create an app registration?**
No. You authorise ours, in one click.

**Exactly which permissions are we granting?**
`openid`, `profile`, `email`. No access to mail, files, calendar or directory.

**Does AroundLink see our passwords?**
Never. Authentication happens at Microsoft; we only receive a signed identity
token.

**Do our MFA and conditional access policies apply?**
Yes, in full. Sign-in takes place on your Microsoft pages, under your rules.

**Can an account from another institution get in?**
No. Two independent barriers: the tenant that issued the token, and the allowed
email domain list.

**Can we roll back?**
Yes. Disabling restores password sign-in.

**Can we test before opening it to everyone?**
Yes. The configuration test validates the connection without enabling anything,
and enabling without strict mode keeps the password fallback while you check.

---

See also: [Security &amp; data](securite.md) ·
[Platform overview](plateforme.md)
