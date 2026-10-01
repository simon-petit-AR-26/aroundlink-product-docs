# Microsoft sign-in

Your users — staff and students alike — can sign in to AroundLink with their **Microsoft
account**, work or personal, with no extra password to remember.

Since September 2026, **there is nothing to configure in the common case**. Each person links
their own account, in two clicks, from their profile.

## The common case: everyone links their own account

**What it's for.** Signing in with one click, no password, no request to your IT department
or to us.

**Who it's for.** <span class="al-audience">every AroundLink user</span>

**How it works.** In three steps.

1. The user signs in to AroundLink **with their password**, as usual.
2. From their profile, they link their Microsoft account — work or personal.
3. From then on, the **"Sign in with Microsoft"** button on the home page lets them straight
   in.

They can unlink it whenever they want and go back to signing in with their password.

!!! warning "A matching email address is never enough"
    Sign-in recognises **the linked Microsoft account**, not the address it carries. Someone
    turning up with a Microsoft account bearing the same email as one of your users would not
    get in: they would see *"This Microsoft account is not linked to any AroundLink account.
    Sign in with your password, then link it from your profile."*

    That is what makes it safe to open Microsoft sign-in to everyone without checking
    anything upfront.

**The messages your users may see:**

| Message | What it means |
|---|---|
| *This Microsoft account is not linked to any AroundLink account* | They must sign in with their password first and link their account |
| *This Microsoft account is already linked to another AroundLink account* | A Microsoft account can serve only one AroundLink identity |
| *This account signs in with Microsoft — there is no password to set* | The account was created under forced SSO, with no password |

**Use case.**
> A coordinator has had enough of remembering one more password. She signs in, opens her
> profile, links her school account, and signs in with one click from that day on — without
> having had to ask anyone for anything.

## The forced-SSO case

**What it's for.** Making Microsoft sign-in **the only way in** for your institution — no
passwords to manage, and leavers handled in your directory, not with us.

**Who it's for.** <span class="al-audience">IT department</span>

**How it works.** This is the only case that calls for an exchange with our team. Your users
then have nothing to link: linking happens **at their first sign-in**, automatically, from
their email address.

### What we need from you

| | What | Where to find it |
|---|---|---|
| **1** | Your Microsoft **tenant identifier** | Microsoft Entra portal ▸ Overview ▸ Tenant ID |
| **2** | The list of your allowed **email domains** | Only you know it |

### What we do next

We record your configuration and enable it. From then on, anyone from your institution
arriving with an address on an allowed domain is linked to their AroundLink account at first
sign-in.

!!! danger "Allowed domains are not optional"
    An enabled configuration **must** declare at least one domain. With no domain, nobody is
    linked at first sign-in — and since forced SSO removes the password, your users would be
    locked out. The platform therefore refuses an enabled configuration with no domain.

!!! warning "Accounts must exist beforehand"
    Single sign-on verifies **who you are**. It does not decide that you are allowed in. A
    user who does not yet exist in AroundLink will be refused, even with a perfectly valid
    Microsoft account. Create or import your accounts before enabling.

**Use case.**
> The university mandates its directory for every tool. Its IT department sends us the tenant
> identifier and two domains. We enable it. The two hundred accounts already in AroundLink
> link themselves over the first few sign-ins, with nobody having to do anything.

## What we read from your directory

| | |
| --- | --- |
| **Data read** | name, email address, Microsoft account identifier |
| **Data not requested** | mail, files, calendar, directory, groups, memberships |
| **Passwords** | never pass through AroundLink |
| **Application to declare on your side** | none |
| **Scope** | institution staff **and** students |
