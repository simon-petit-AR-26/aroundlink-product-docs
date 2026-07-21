# Security & data

!!! info "Who this page is for"
    A **technical** page for **CIOs / CISOs** evaluating AroundLink. It describes the
    security measures **at a product level**. It deliberately contains no
    configuration detail, secret or exploitable element. More detailed security
    documentation can be provided on request in an appropriate setting.

## Authentication

- **Microsoft / Azure SSO (OpenID Connect)** — institutions can let their users sign
  in with their existing institutional account; single sign-on can be **enforced**
  per institution, with **allowed email domains**. See the [Overview](plateforme.md).
- **Password sign-in** (when SSO is not enforced) — passwords are **hashed** (never
  stored in clear text), with a **strength check** at creation and **reset** via a
  single-use, time-limited link.
- **Rate limiting** on sign-in and reset attempts, to slow down brute-force attacks.

## Authorisation & isolation

- **Multi-tenant isolation** — every query is automatically restricted to the data of
  the signed-in user's institution; one institution never sees another's data.
- **Roles & permissions (RBAC)** — per-module rights (none / read / write),
  **enforced server-side** (hiding a menu is not enough: direct access is blocked
  too). See the [Overview](plateforme.md).
- **Ownership checks** on objects accessed by identifier, on top of tenant isolation,
  to prevent access to someone else's resource.

## API & network

- **Application API** — authentication via **JWT token** (RSA-key signed) and
  regenerable **API keys**, on a channel **separate from the browser session**.
- **EWP network** — every incoming and outgoing exchange is **signed and verified**
  (RSA HTTP signatures, the EWP standard); the caller is identified by its public key
  declared in the EWP Registry, which governs data access.

## Data protection

- **Encryption in transit** — the application runs behind **HTTPS** (trusted proxies
  configured).
- **Non-enumerable identifiers** — sensitive objects (placements, agreements, student
  files…) are referenced by **UUID**.
- **CSRF protection** on forms and sensitive actions.
- **Validated-document locking** — a validated document can no longer be altered or
  deleted on the student side.
- **Minimisation** — only the data needed for the mobility process is collected;
  students' personal data (identity, contact details, grades) is handled solely in
  that context.

## Monitoring & continuity

- **Application error monitoring** (Sentry) to detect and diagnose incidents.
- **Database backups** on demand, with **retention** and download, from the admin
  console.
- **Logging & history** — key decisions (document validations, agreement changes,
  nomination decisions) keep a timestamped history with the author.

## Compliance & hosting

- AroundLink operates within the **Erasmus+ / EWP** framework, the European mobility
  interoperability standard.
- **Production is hosted on OVHcloud, in Europe**, consistent with **GDPR** for
  students' personal data.

!!! note
    This page is an overview. For a security questionnaire, an audit or contractual
    details, contact the AroundLink team.
