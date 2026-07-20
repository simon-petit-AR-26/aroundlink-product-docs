# Dashboards

The dashboards give the International Relations Office an immediate view of its
mobility: what needs action today on one side, the big steering trends on the
other. Two complementary pages, each walled off to your institution.

## Operational dashboard

**What it's for.** This is the coordinator's landing page: at a glance you see
what is waiting to be handled (documents, learning agreements, transcripts)
without scrolling through long lists. It turns "where do we stand?" into a single
look.

**Who it's for.** <span class="al-audience">coordinator / IR manager</span>

**How it works.** The page shows seven key indicators — outgoing and incoming
students, partners, available places, documents pending validation, Learning
Agreements pending, transcripts of records pending — plus a student-pipeline
chart. Each indicator is clickable and leads straight to the relevant queue. You
can add, hide and resize blocks from a widget catalog.

**Use case.**
> Monday morning, a coordinator sees "12 documents pending validation" and clicks
> to land directly on the queue to process.

??? note "Internal details (AroundLink team)"
    KPIs: outgoing, incoming, partners, available places, pending documents,
    pending OLAs, pending ToRs. The indicator set is cached per coordinator for
    30 s (each KPI is a separate query). `/mobility/` redirects to the dashboard.
    Widgets come from `DashboardWidgetRegistry`; data walled off to the
    coordinator's institution. Controller: `DashboardController`.

## Pilotage (strategic) dashboard for the DRI

**What it's for.** This is the strategic cockpit for the Director of International
Relations. It groups metrics into blocks — Overview, Decision, Financial,
Inclusion — to inform structural decisions rather than day-to-day work: growth
trends, destinations under pressure, underused agreements, budget consumption,
inclusion.

**Who it's for.** <span class="al-audience">IR manager (director)</span>

**How it works.** Pilotage is a modular dashboard: you choose which blocks are
shown from tiles, charts, gauges, lists, a funnel and a map. It offers, for
example, mobility growth, breakdown by type, study level, destinations under
pressure, underused agreements, place occupancy rate, campaign funnel, top
partners, an Erasmus budget-used gauge and inclusion. The page is read-only and
stays walled off to your institution.

**Use case.**
> A DRI reviews the "Underused agreements" list to decide which partnerships to
> renegotiate next year.

??? note "Internal details (AroundLink team)"
    Block categories: Overview / Decision / Financial / Inclusion. Widget types:
    tile, chart, gauge, list, funnel, map. Same `DashboardWidgetRegistry` and
    `DashboardMetricsService` as the operational dashboard; Tabler icons (`ti-*`).
    Controller: `DashboardPilotageController` (route `/mobility/pilotage`,
    `ROLE_MOBILITY`).
