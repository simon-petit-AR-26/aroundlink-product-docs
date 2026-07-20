# AroundLink product documentation

**AroundLink** is the international student mobility platform (Erasmus+ / EWP) used
by the International Relations (IRO) offices of higher-education institutions. It
brings partners, agreements, application campaigns, contractual documents, grants
and data exchange with the European network into one place — replacing scattered
spreadsheets and emails with a single, auditable, compliant process.

This documentation lists **every feature** of the tool and, for each one, its
**business value**. It serves two audiences:

- **IRO managers and officers** (customers): understand what the tool does and the
  value it brings, without technical jargon.
- **AroundLink teams** (internal): a complete view of the product scope.

!!! tip "How to read a feature card"
    Every feature follows the same format: **what it is for**, **who it is for**,
    **how it works**, a concrete **use case**, and a collapsible _"Internal
    details"_ block reserved for (non-sensitive) operational context. The default
    tone is business-value first; technical detail stays collapsed.

## The three spaces

<div class="grid cards" markdown>

-   :material-office-building: __Institution workspace__

    ---

    The IRO team's workspace: partners and agreements, mobility campaigns,
    documents (Learning Agreement, transcripts), Erasmus+ grants, communications
    and steering.

    [:octicons-arrow-right-24: Dashboards](etablissement/dashboards.md)

-   :material-school: __Student portal__

    ---

    The student journey, from discovering destinations to applying, then during and
    after the mobility (learning agreement, certificates, transcript of records).

    [:octicons-arrow-right-24: Discover &amp; apply](etudiant/decouverte-candidature.md)

-   :material-earth: __Atlas &amp; EWP network__

    ---

    The world directory of institutions and the integration with the _Erasmus
    Without Paper_ network to exchange agreements, learning agreements and
    transcripts without paper.

    [:octicons-arrow-right-24: Atlas](atlas/atlas.md) ·
    [:octicons-arrow-right-24: EWP](ewp/ewp.md)

</div>

## A word on multi-tenancy

AroundLink is a **multi-tenant SaaS** platform: each client institution only ever
sees its own data (students, agreements, campaigns…), fully isolated from every
other institution. Three account types coexist — **IRO coordinator**, **student**
and **invited partner** — each with its own space and permissions. See
[Platform &amp; security](plateforme/plateforme.md).

## Contents

- **[Institution workspace](etablissement/dashboards.md)** — partners, agreements,
  campaigns, documents, grants, communications, settings.
- **[Student portal](etudiant/decouverte-candidature.md)** — profile, search,
  application, mobility, learning agreement, transcript of records.
- **[Atlas — World directory](atlas/atlas.md)** — the directory of institutions
  worldwide.
- **[EWP network](ewp/ewp.md)** — data exchange with partner universities.
- **[Platform &amp; security](plateforme/plateforme.md)** — accounts, roles, SSO,
  plans.
- **[Glossary](annexes/glossaire.md)** — EWP, IIA, OLA, ToR, EQF, ISCED…
