# Microsoft sign-in

Your users — staff and students alike — can sign in to AroundLink with their **Microsoft
account**, work or personal, with no extra password to remember.

**There is nothing to configure in the common case.** Each person links
their own account, in two clicks, from their profile.

## The common case: everyone links their own account

**What it's for.** Signing in with one click, with no password, without going through IT or
us.

**Who it's for.** <span class="al-audience">every AroundLink user</span>

**How it works.** In three steps.

1. The user signs in to AroundLink **with their password**, as usual.
2. From their profile, **Link my Microsoft account** links their account — work or
   personal. Microsoft always shows its account picker.
3. From then on, the **Sign in with Microsoft** button on the sign-in page lets them straight
   in.

**Unlink Microsoft account** unlinks it, provided they keep another way in: a usable
password, or a linked Google account. If your institution enforces Microsoft, the button is
greyed out: "You need your Microsoft account to sign in."

!!! warning "An identical email address is never enough"
    Sign-in recognises **the linked Microsoft account**, not the address it carries. Someone
    arriving with a Microsoft account bearing the same email address as one of your users
    would not get in: they would see "This Microsoft account is not linked to any
    AroundLink account. Sign in with your password, then link it from your profile."

    That is what makes it possible to open Microsoft sign-in to everyone without checking
    anything beforehand.

**Messages your users may see:**

| Message | What it means |
|---|---|
| *This Microsoft account is not linked to any AroundLink account…* | They must first sign in with their password and link their account |
| *This Microsoft account is already linked to another AroundLink account.* | A Microsoft account can only serve one AroundLink identity |
| *This email domain is not allowed to sign in with Microsoft.* | The address belongs to none of the institution's allowed domains |
| *Your Microsoft account could not be matched to your AroundLink account…* | Automatic linking did not find the account: your administrator must check it exists |
| *This account signs in with Microsoft — there is no password to set.* | Your institution has removed password sign-in (strict mode) |

**Use case.**
> A coordinator is tired of remembering one more password. She signs in, opens her profile,
> links her school account, and signs in with one click from that day on — without having
> to ask anyone for anything.

## The forced-SSO case

**What it's for.** Automatically link all your users to their Microsoft account — and, if
you wish, make Microsoft **the only way in**: no more passwords to manage, and leavers are
handled in your directory, not with us.

**Who it's for.** <span class="al-audience">IT department</span>

**How it works.** This is the only case that requires an exchange with our team. Two
separate settings, which we turn on for you:

| Setting | Effect |
|---|---|
| **Activation** | Your users have nothing to link: linking happens **at their first sign-in**, based on their Microsoft account's sign-in name. |
| **Strict mode** | Removes password sign-in: your directory becomes the only way in. |

See also [Settings, per institution](sso.md#settings-per-institution).

### What we need from you

| | What | Where to find it |
|---|---|---|
| **1** | Your Microsoft **tenant ID** — or your primary domain name | Microsoft Entra portal ▸ Overview ▸ Tenant ID |
| **2** | The list of your allowed **email domains** | Only you know it |
| **3** | If your tenant requires it, **admin consent** | We send you a link: an administrator of your tenant grants it once, on Microsoft's page |

### What we do next

We record your configuration and turn it on. From then on, anyone from your institution who
arrives with an address from an allowed domain is linked to their AroundLink account at
their first sign-in.

!!! danger "Allowed domains are not optional"
    An active configuration **must** declare at least one domain. With no domain, nobody is
    linked at their first sign-in — and, combined with strict mode, which removes the
    password, your users would be locked out. The platform therefore refuses an active
    configuration with no domain.

!!! warning "Accounts must exist beforehand"
    Single sign-on verifies **who you are**. It does not decide that you are allowed in. A
    user who does not yet exist in AroundLink will be refused, even with a perfectly valid
    Microsoft account. Create or import your accounts before turning it on.

**Use case.**
> The university enforces its directory for all its tools. Its IT department sends us its
> tenant ID and its two domains. We turn it on. The two hundred accounts already created in
> AroundLink link themselves as people first sign in; once those first sign-ins are checked,
> strict mode is turned on.

## What we read from your directory

| | |
| --- | --- |
| **Data read** | name, email address, Microsoft account identifier |
| **Data not requested** | mail, files, calendar, directory, groups, memberships |
| **Passwords** | never pass through AroundLink |
| **Application to declare on your side** | none |
| **Scope** | institution staff **and** students |
