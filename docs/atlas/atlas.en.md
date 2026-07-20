# Atlas — World directory

Atlas is a worldwide directory of higher-education institutions: a single place to
search for any institution, locate it on a world map, and immediately see whether it
is already a partner or reachable through the Erasmus/EWP network. "Who else is out
there?" becomes a map you explore, rather than a spreadsheet.

## World directory (table / cards / map)

**What it's for.** Atlas gathers every higher-education institution in the world into
a searchable directory. You look up any institution, see where it sits on a map, and
tell at a glance which ones are already your partners from those reachable through the
EWP network.

**Who it's for.** <span class="al-audience">coordinator / IR manager</span>

**How it works.** A single page offers three synchronized views: table, cards and an
interactive world map. You filter by free text (name, city), country, institution
type and EWP factsheet status. Each row shows its network status and marks the
institutions already partnered with your institution. The page is read-only: you
consult it, you don't create or edit a record here.

**Use case.**
> A coordinator searches "Antalya", filters to Turkey, sees on the map which nearby
> universities already expose an EWP factsheet, and spots that one of them is already
> a partner.

??? note "Internal details (AroundLink team)"
    The directory is built from open registries (ROR / Wikidata) and enriched by
    AroundLink. Data served client-side from the JSON API `/mobility/api/atlas/*`
    (read, `ROLE_MOBILITY`). Per-row network status: partner / synced / declared /
    none. The map view is capped (with viewport-bbox filtering: zoom to see more);
    country/type browse pages are cached 1h; the "partner" flag is computed per
    request. Controllers: `AtlasController` (page), `AtlasApiController` (API).
    AROUNDLINK-324 / -492 / -493.

## Live factsheet on demand

**What it's for.** From any institution in the network, you open its EWP factsheet
live — nomination deadlines, application contacts — without waiting for a bulk sync.
The directory fills in over time as institutions are consulted.

**Who it's for.** <span class="al-audience">coordinator / IR manager</span>

**How it works.** Opening an institution's record fetches its factsheet live (if
declared), then shows the nomination calendar (autumn / spring) and application
contact details (email, phone). A successful lookup updates the institution's cached
summary, so the directory fills in as it is used.

**Use case.**
> Before nominating their students, a coordinator opens a partner's factsheet to
> confirm the spring nomination deadline.

??? note "Internal details (AroundLink team)"
    Complements the bulk `ewp:atlas:sync` sync. Requires your institution to have an
    EWP HEI id. A successful lookup stamps `factsheetSyncedAt`; the record is not
    persisted beyond that summary. Route: `/mobility/atlas/hei/{heiId}`
    (`AtlasController`).
