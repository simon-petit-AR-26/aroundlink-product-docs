# Architecture & technology

!!! info "Who this page is for"
    A **technical** page for **IT teams** (integration, due diligence, operations). It
    describes the technologies AroundLink is made of, at product level — no
    configuration, no secret.

## Overview

AroundLink is a **multi-tenant web application (SaaS)** in two **separate** parts:

- a web **interface** — what your users see at `app.aroundlink.com`;
- a **JSON API** — the application core, carrying every business rule, which the
  interface queries for each screen.

The interface only reaches the database through the API. Exchanges with the European
*Erasmus Without Paper* network go through the same API, and your own systems can use it
— see [Emails & connectors](../etablissement/emails.md).

## The interface (front end)

| Technology | Role |
| --- | --- |
| **Next.js 16** / **React 19** | Web application, in **TypeScript**. |
| **Tailwind CSS** | Styling, in-house design system. |
| **TanStack Query** | Exchanges with the API, caching of displayed data. |
| **Recharts** | Dashboard and statistics charts. |
| **Leaflet** | Partner maps and the [Atlas](../atlas/atlas.md). |

Tables, filters and saved views are built in-house, with no third-party grid library.

## The application core (back end)

| Technology | Role |
| --- | --- |
| **PHP 8.3+** / **Symfony 7** | Application core: security, business rules, validation. |
| **API Platform** | Exposing and documenting the API. |
| **Doctrine ORM** | Data access and schema migrations. |
| **Symfony Messenger** | **Asynchronous** processing (emails, notifications, EWP syncs). |
| **JWT** | Authentication of the interface against the API: stateless, no server-side session. |

## Database

- **PostgreSQL 16**. The schema is versioned through **migrations**, reproducible from
  one environment to another.
- Public identifiers of sensitive objects are **UUIDs** — non-guessable,
  non-enumerable — rather than sequential integers.

## Documents and emails

**Emails** and **PDF documents** (certificates, learning agreements, transcripts,
templates) are produced on the server, from templates. That is where, and only where,
the **Twig** template engine is still used: the former interface it rendered is
switched off in production.

## Integrations & services

| Service | Usage |
| --- | --- |
| **Mailjet** | Sending emails. |
| **Gotenberg** / **mPDF** | PDF document generation. |
| **Sentry** | Error monitoring, on the interface as on the API. |
| **EWP registry** | Mirror of the EWP network catalogue (institutions, keys, API versions). |
| **ROR registry** | Reference identity of the institutions in the [Atlas](../atlas/atlas.md). |

## Runtime & deployment

- **FrankenPHP** (Caddy-based application server) in **worker mode**: the core stays
  loaded in memory between requests.
- **Docker** images; at start-up, the application waits for the database then applies
  the migrations.
- **Production is hosted in France, at OVHcloud**.
- Runs **behind an HTTPS proxy**.

## Asynchronous processing

What must not keep the user waiting — sending emails, notifications, EWP
synchronisations, scheduled reminders, closing campaigns at the set time — goes through
**Symfony Messenger** and scheduled tasks, processed in the background.

## API

- **The AroundLink API** is documented in **OpenAPI** format, available online:
  [api.aroundlink.com/apis/docs](https://api.aroundlink.com/apis/docs).
- **The EWP API** (*Erasmus Without Paper* network) — endpoints, directions and versions
  in the [API reference](../ewp/reference-api.md).
