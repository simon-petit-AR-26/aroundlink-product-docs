# Atlas — Annuaire mondial

Atlas est un annuaire mondial des établissements d'enseignement supérieur : un seul
endroit pour rechercher n'importe quel établissement, le situer sur une carte du
monde, et voir immédiatement s'il est déjà partenaire ou joignable via le réseau
Erasmus/EWP. « Qui d'autre existe ? » devient une carte que l'on explore, plutôt
qu'un tableur.

## Annuaire mondial (tableau / cartes / carte)

**À quoi ça sert.** Atlas rassemble tous les établissements d'enseignement supérieur
du monde dans un annuaire consultable. Vous y cherchez n'importe quel établissement,
voyez où il se trouve sur une carte, et distinguez d'un coup d'œil ceux qui sont
déjà vos partenaires de ceux qui sont accessibles via le réseau EWP.

**Pour qui.** <span class="al-audience">coordinateur / gestionnaire RI</span>

**Comment ça marche.** Une seule page propose trois vues synchronisées : tableau,
cartes et carte du monde interactive. Vous filtrez par texte libre (nom, ville),
pays, type d'établissement et statut de factsheet EWP. Chaque ligne indique son
statut réseau et signale d'un repère les établissements déjà partenaires de votre
établissement. La page est en lecture seule : on y consulte, on n'y crée ni ne
modifie de fiche.

**Cas d'usage.**
> Un coordinateur cherche « Antalya », filtre sur la Turquie, voit sur la carte
> quelles universités proches exposent déjà une factsheet EWP et repère que l'une
> d'elles est déjà partenaire.

??? note "Détails internes (équipe AroundLink)"
    L'annuaire est construit à partir de registres ouverts (ROR / Wikidata) et
    enrichi par AroundLink. Données servies côté client depuis l'API JSON
    `/mobility/api/atlas/*` (lecture, `ROLE_MOBILITY`). Statut réseau par ligne :
    partenaire / synced / declared / none. La vue carte est plafonnée (avec filtrage
    par cadre de vue : zoomer pour voir davantage) ; les pages de navigation par
    pays/type sont mises en cache 1 h ; le repérage « partenaire » est calculé à
    chaque requête. Contrôleurs : `AtlasController` (page), `AtlasApiController`
    (API). AROUNDLINK-324 / -492 / -493.

## Factsheet en direct à la demande

**À quoi ça sert.** Depuis n'importe quel établissement du réseau, vous ouvrez sa
factsheet EWP en direct — délais de nomination, contacts de candidature — sans
attendre une synchronisation groupée. L'annuaire se complète au fil des consultations.

**Pour qui.** <span class="al-audience">coordinateur / gestionnaire RI</span>

**Comment ça marche.** Ouvrir la fiche d'un établissement récupère sa factsheet en
direct (si elle est déclarée), puis affiche le calendrier de nomination (automne /
printemps) et les coordonnées de candidature (e-mail, téléphone). Une consultation
réussie met à jour le résumé mis en cache de l'établissement, si bien que l'annuaire
se remplit au fur et à mesure.

**Cas d'usage.**
> Avant de nominer ses étudiants, un coordinateur ouvre la factsheet d'un partenaire
> pour confirmer la date limite de nomination du printemps.

??? note "Détails internes (équipe AroundLink)"
    Complète la synchronisation groupée `ewp:atlas:sync`. Nécessite que votre
    établissement dispose d'un identifiant HEI EWP. Une consultation réussie estampille
    `factsheetSyncedAt` ; la fiche n'est pas persistée au-delà de ce résumé.
    Route : `/mobility/atlas/hei/{heiId}` (`AtlasController`).
