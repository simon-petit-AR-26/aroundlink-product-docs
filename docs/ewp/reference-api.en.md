# EWP API reference (IT / integrators)

!!! info "Who this page is for"
    This page is **technical**: it is aimed at **IT departments, integration teams
    and partners** connecting their system to AroundLink over the EWP network. For
    the business value of each building block, see the [Overview](ewp.md) page.

AroundLink implements the **EWP (Erasmus Without Paper)** network APIs to exchange
agreements, learning agreements, transcripts and nominations with partner
universities, without manual intervention.

## Principles

- **All incoming APIs** (a partner calls us) are exposed under `‌/ewp/{hei-id}/…`,
  where `{hei-id}` is the HEI identifier of the relevant AroundLink client
  institution.
- **Two directions**:
    - *Incoming* — the partner's system (or the EWP Registry) calls AroundLink.
    - *Outgoing* — AroundLink calls the partner (fetch / notify).
- **Authentication** — exchanges are signed (HTTP Signature, the standard EWP
  mechanism on both client and server). The caller is identified by its public key
  declared in the EWP Registry; that identity is what **scopes** the data (a partner
  only sees the objects that concern it).
- **Discovery** — a partner finds the institution and its services via the
  **manifest**; it can check connectivity and authentication via **Echo** before any
  real exchange.
- **CNR** (*Change Notification Receiver*) — lightweight "this object changed, come
  and re-fetch it" notifications; they keep both copies in sync.

## How to test the connection

A **signed** call to `‌/ewp/{hei-id}/echo` returns the parameters passed and the
**authenticated** HEI identity of the caller. A `200` with the correct HEI confirms
that the link and signature work — the first step of any onboarding.

## Incoming endpoints (partner → AroundLink)

Paths relative to `‌/ewp/{hei-id}`.

### Discovery & diagnostics

| Endpoint | Method | API (version) | Role |
| --- | --- | --- | --- |
| `/manifest.xml` | GET | Discovery v6 | Manifest: lists the implemented APIs, their URLs and versions, the contact and the signing public keys. Entry point of any onboarding. |
| `/echo` | GET · POST | Echo v2 | Connectivity + authentication test; echoes back the authenticated caller. |
| `/institutions` | GET · POST | Institutions v2 | Resolves one or more HEI identifiers to institution names (up to 10). |
| `/factsheet` | GET · POST | Factsheet v1.2 | Serves the institution's fact sheet (deadlines, housing/visa contacts, turnaround limits). |

### IIA — inter-institutional agreements

| Endpoint | Method | API (version) | Role |
| --- | --- | --- | --- |
| `/iias/index` | GET · POST | IIAs v7 | Lists the identifiers of agreements shared with the caller (filters: partner, year, modified since). |
| `/iias/get` | GET · POST | IIAs v7 | Full content of one or more agreements (up to 100), with the version hash. |
| `/iias/approval` | GET · POST | iias-approval v2 | Our approval (id + hash of the approved version) for the caller's agreements. |
| `/iias/stats` | GET | IIAs v7 | Approval statistics (fetchable, approved by one / both sides…). |
| `/iia-cnr` | POST | iia-cnr v3 | Notification: an agreement changed on the partner side → we re-fetch it for review. |
| `/iia-approval-cnr` | POST | iia-approval-cnr v2 | Notification: the partner approved → we re-fetch its approval. |

### OLA — learning agreements (outgoing mobilities)

| Endpoint | Method | API (version) | Role |
| --- | --- | --- | --- |
| `/omobility-las/index` | GET · POST | omobility-las v1.2 | Lists our outgoing students' learning agreements for the calling receiving institution. |
| `/omobility-las/get` | GET · POST | omobility-las v1.2 | Full content of a learning agreement (courses, signatures, change proposals). Restricted to the receiving institution. |
| `/omobility-las/update` | POST | omobility-las v1.2 | The receiving institution approves or requests changes (signature / comment). |
| `/omobility-las/stats` | GET | omobility-las v1.2 | Per-year counters (approved / rejected / pending). |
| `/omobility-la-cnr` | POST | omobility-la-cnr v1 | Notification: a learning agreement changed on the partner side → re-fetch. |

### ToR — transcripts of records (incoming mobilities)

| Endpoint | Method | API (version) | Role |
| --- | --- | --- | --- |
| `/imobility-tors/index` | GET · POST | imobility-tors v1 | Lists the transcripts of incoming students for the calling home institution. |
| `/imobility-tors/get` | GET · POST | imobility-tors v1 | Official transcript in **ELMO** format (courses, grades, ECTS). Restricted to the home institution. |
| `/imobility-tors/stats` | GET | imobility-tor-stats v1 | Transcript counters per year. |
| `/imobility-tor-cnr` | POST | imobility-tor-cnr v1 | Notification: a transcript changed → re-fetch. |

### Nominations (outgoing mobilities)

| Endpoint | Method | API (version) | Role |
| --- | --- | --- | --- |
| `/omobilities/index` | GET · POST | omobilities v3 | Lists the student nominations we send to the calling receiving institution. |
| `/omobilities/get` | GET · POST | omobilities v3 | Nomination detail (student identity, ISCED-F field, EQF level, linked agreement, status). Restricted to the receiving institution. |
| `/omobilities/update` | POST | omobilities v3 | The receiving institution accepts or rejects the nomination; the decision flows back into AroundLink. |
| `/omobility-cnr` | POST | omobility-cnr v1 | Notification: a nomination changed → re-fetch. |

## Outgoing calls (AroundLink → partner)

Triggered automatically by AroundLink (when an object is edited, or when a CNR is
received). They use the partner's service URL, resolved via the EWP Registry, and
are signed with our credentials.

| Action | Trigger | Effect |
| --- | --- | --- |
| Fetch an agreement (IIA) | CNR received / sync | Fetches the partner's version and prepares a review. |
| Fetch an IIA approval | Approval CNR received | Updates the partner's approval state. |
| Notify an IIA change | An agreement edited on our side | Sends an `iia-cnr` to the partner. |
| Fetch / notify an OLA | Edit / CNR | Synchronises the learning agreement. |
| Fetch a transcript (ToR) | CNR received | Updates the transcript. |
| Fetch a nomination | CNR received | Updates the nomination and its decision. |
| Fetch a partner factsheet | Manual action by the IRO | Imports the partner's deadlines/contacts into AroundLink. |

## Foundations

- **HTTP signature (client + server)** — every request and response is signed and
  verified (short time window). The key fingerprint identifies the caller and drives
  data scoping.
- **EWP Registry (local mirror)** — catalogue of the network's institutions, APIs,
  versions and public keys; used to resolve a partner's URL before an outgoing call
  and to identify the caller of an incoming call.
- **ECHE list (mirror)** — the Erasmus Charter, used as an institution source.

!!! tip "Onboarding good practice"
    1. Add the institution (its HEI ID) on the partner side. 2. Read the
    `manifest.xml` to discover services and keys. 3. Validate the link with a
    **signed** `echo`. 4. Move on to the real exchanges (IIA, OLA, ToR, nominations).

## External references

### AroundLink REST API

Beyond EWP, AroundLink exposes its own **REST API** (API Platform / Hydra) for its
business resources (agreements, students, learning agreements, transcripts…). Its
**interactive** documentation — contract, resources and schemas, always up to date —
is generated automatically:

- :material-api: [AroundLink API documentation (demo instance)](https://demo.aroundlink.com/api/docs)

### Official EWP specifications

The EWP network's general documentation and specifications are **public** and
maintained by the consortium — useful for an IT team that wants the schema detail:

- :octicons-book-24: [EWP Developers Guide](https://developers.erasmuswithoutpaper.eu/)
- :octicons-mark-github-16: [GitHub organisation — all specifications](https://github.com/erasmus-without-paper)
- :octicons-shield-24: [Architecture & security](https://github.com/erasmus-without-paper/ewp-specs-architecture)
- :octicons-git-branch-24: [The mobility process explained](https://github.com/erasmus-without-paper/ewp-specs-mobility-flowcharts)
- Each API's specification lives in an `ewp-specs-api-<name>` repository, e.g.
  [IIAs](https://github.com/erasmus-without-paper/ewp-specs-api-iias) ·
  [Institutions](https://github.com/erasmus-without-paper/ewp-specs-api-institutions) ·
  [Outgoing Mobilities](https://github.com/erasmus-without-paper/ewp-specs-api-omobilities)

!!! note
    The API versions listed above match AroundLink's current implementation; if in
    doubt about a schema, **the official specifications prevail**.
