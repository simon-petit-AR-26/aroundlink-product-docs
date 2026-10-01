# Single sign-on (IT departments)

!!! info "Who this page is for"
    This page is **technical**: it addresses **IT departments and infrastructure
    teams** who want to know how their users sign in to AroundLink. For the
    business value, see the [Overview](plateforme.md).

AroundLink users — international office staff and students alike — can sign in
with their **institutional account**, with no extra password to create or
manage.

The connection is configured **per institution**. Each one picks its mode:
single sign-on alone, or single sign-on alongside passwords during the
transition.

## Identity providers

| Provider | Status | Guide |
| --- | --- | --- |
| **Microsoft Entra ID** (Azure AD) | ✅ Available | [Onboarding guide](sso-microsoft.md) |
| **Shibboleth / SAML 2.0** (RENATER, eduGAIN, SWITCHaai…) | 🗺️ On the roadmap | — |
| **Google Workspace** | 🗺️ On the roadmap | — |

!!! note "Roadmap"
    **Microsoft Entra ID** is the provider you can connect today. Academic
    identity federation (Shibboleth / SAML, RENATER, eduGAIN) and Google
    Workspace are on our roadmap, with no announced date at this stage.

    If your institution authenticates through one of those, do tell us: what
    institutions ask for decides the order in which we open them. In the
    meantime, password sign-in remains available, with single-use reset links —
    see [Security &amp; data](securite.md).

![The sign-in screen with single sign-on](../assets/screenshots/connexion.png)

*The sign-in screen as your users see it: password sign-in stays available, and the button at the bottom opens authentication through the university account. Once single sign-on is enforced, only that button remains.*

## What holds for every provider

The following does not depend on the protocol. It holds for Microsoft today, and
will hold for the providers we add.

### Accounts must exist beforehand

!!! danger "The prerequisite most often discovered too late"
    Single sign-on **connects** accounts, it does not **create** them. A user who
    is absent from AroundLink is refused entry, even with a perfectly valid
    institutional account.

Accounts are created beforehand by the institution: importing the student list,
or creation by the international office. See
[Settings &amp; team](../etablissement/parametres.md).

There is **no directory synchronisation** (no SCIM) and **no group or role
synchronisation**: AroundLink permissions are granted inside AroundLink.

### The sign-in journey

The **"Sign in with Microsoft"** button sits on the home page, for everyone, permanently.
There is nothing to look for and nothing to declare upfront.

What happens next depends on one thing only: **is the Microsoft account linked to an
AroundLink account?**

1. **Yes** — the user gets in. Your directory's rules apply along the way (password,
   multi-factor, conditional access): they are yours, not ours.
2. **No** — entry is refused, with the explanation: sign in with a password first, then link
   the account from your profile.

Recognition is on **the linked account**, never on the email address alone. That is what
makes it safe to open Microsoft sign-in to everyone with no upfront check.

### Settings, per institution

In the common case there are **no settings**: each person links their own account. The
settings below concern only institutions that want to **mandate** single sign-on.

| Setting | Effect |
| --- | --- |
| **Enable** | Your users are linked automatically at first sign-in, from their address. |
| **Strict mode** | Removes password sign-in: your directory becomes the only way in. |
| **Allowed email domains** | The domains whose addresses trigger that automatic linking. Required as soon as you enable. |

!!! danger "Why domains are required"
    With no domain declared, nobody is linked at first sign-in. Combined with strict mode,
    which removes the password, your users would be locked out. The platform therefore
    refuses an enabled configuration with no domain.

!!! warning "Do not turn on strict mode first"
    Strict mode removes the password fallback. Turn it on only after checking that at least
    one account really gets in through single sign-on.

### Leavers and joiners

| Event on your side | Effect in AroundLink |
| --- | --- |
| Institutional account disabled (leaver) | The person can no longer sign in, immediately. |
| Authentication rules changed (MFA, password) | Nothing to do in AroundLink: those rules are yours. |
| New joiner | Their AroundLink account must be created first. |

### AroundLink administration accounts

The vendor's internal accounts **never** sign in through a customer's single
sign-on, by design.

---

See also: [Microsoft Entra ID — onboarding guide](sso-microsoft.md) ·
[Security &amp; data](securite.md) ·
[Platform overview](plateforme.md)
