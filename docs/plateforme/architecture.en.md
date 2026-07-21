# Architecture & technology

!!! info "Who this page is for"
    A **technical** page for **IT teams / CIOs** (integration, due diligence,
    operations). It describes the technologies AroundLink is built on, at a product
    level — with no configuration or secrets.

## Overview

AroundLink is a **multi-tenant web application (SaaS)**, built around a **Symfony
(PHP)** core and a **PostgreSQL** database. The application is **API-first**: the
same business data is exposed through a REST API (see the [EWP API
reference](../ewp/reference-api.md) and the AroundLink REST API), enabling the
integrated web interface, decoupled front-ends (React/Next.js) and the
machine-to-machine exchanges of the EWP network alike.

## Application core (backend)

| Technology | Version | Role |
| --- | --- | --- |
| PHP | ≥ 8.3 | Backend language. |
| Symfony | 7.2 | Application framework (HTTP, security, forms, validation…). |
| API Platform | 4.1 | REST API exposure (Hydra / JSON-LD contract, CRUD operations). |
| Doctrine ORM / DBAL | 3.x | Data access, schema migrations, data sets. |
| Symfony Messenger | 7.2 | **Asynchronous** processing (emails, notifications, EWP syncs). |
| Symfony UX (Stimulus) | 2.x | Browser interactivity without a heavy build (AssetMapper / importmap). |
| Twig | 3.x | Templates for the integrated interface pages. |

## Database

- **PostgreSQL 16**. The schema is versioned with **Doctrine migrations**
  (reproducible across environments).
- Public identifiers of sensitive objects use **UUIDs** (non-guessable /
  non-enumerable) rather than sequential integers.

## Interface & front-end components

The integrated interface (institution and student spaces) is rendered with **Twig +
Stimulus**, with:

- **ag-Grid** — data grids (sorting, columns, filters, saved views);
- **Chart.js** — dashboard charts;
- **Leaflet** (+ MarkerCluster, MapTiler basemap) — partner and [Atlas](../atlas/atlas.md) directory maps;
- **CKEditor** — rich content editing (CMS editor, document templates);
- autocompletion and live components via **Symfony UX**.

!!! note "Front / back separation"
    The API-first architecture enables a **decoupled front-end** (a React/Next.js app
    consuming the API) alongside the existing Twig interface. Both coexist during the
    transition.

## Integrations & services

| Service | Use |
| --- | --- |
| **Mailjet** | Email delivery + tracking (opens, clicks, bounces) for communications and reminders. |
| **Gotenberg** / **mPDF** | PDF document generation (certificates, agreements, templates). |
| **MapTiler** (via Leaflet) | Basemaps for the Atlas directory. |
| **Sentry** | Application error monitoring. |
| **EWP Registry** | Mirror of the EWP network catalogue (institutions, keys, API versions). |
| **spatie/simple-excel** | Reading CSV / Excel imports (partners, agreements, grants…). |

## Runtime & deployment

- **FrankenPHP** (a Caddy-based application server) in **worker mode**: the Symfony
  kernel stays loaded between requests for better performance.
- Multi-stage **Docker** image (reproducible build), boot that waits for the database
  then applies migrations.
- Deployable on any containerised infrastructure (the demo instance runs on Railway;
  the production target aims for hosting in Europe).
- Runs **behind an HTTPS proxy** (trusted proxies configured).

## Asynchronous processing

Tasks that must not block the user (sending emails, notifications, EWP
fetches/notifications, grant status updates) go through **Symfony Messenger** and are
processed in the background.

## API

- **REST API** (API Platform, Hydra / JSON-LD contract) — see the interactive
  documentation linked from the [EWP API reference](../ewp/reference-api.md).
- **EWP API** (*Erasmus Without Paper* network) — endpoints, direction and versions
  in the same reference.
