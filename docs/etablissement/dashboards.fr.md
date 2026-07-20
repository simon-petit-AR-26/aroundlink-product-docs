# Tableaux de bord

Les tableaux de bord donnent au bureau des relations internationales une vue
immédiate de sa mobilité : ce qui demande une action aujourd'hui d'un côté, les
grandes tendances de pilotage de l'autre. Deux pages complémentaires, chacune
cloisonnée à votre établissement.

## Tableau de bord opérationnel

**À quoi ça sert.** C'est la page d'accueil du coordinateur : d'un coup d'œil,
vous voyez ce qui attend d'être traité (documents, contrats pédagogiques, relevés
de notes) sans parcourir de longues listes. Elle transforme « où en est-on ? » en
un simple regard.

**Pour qui.** <span class="al-audience">coordinateur / gestionnaire RI</span>

**Comment ça marche.** La page affiche sept indicateurs clés — étudiants sortants
et entrants, partenaires, places disponibles, documents en attente de validation,
Learning Agreements en attente, relevés de notes en attente — ainsi qu'un graphique
de suivi du pipeline étudiant. Chaque indicateur est cliquable et mène directement
vers la file concernée. Vous pouvez ajouter, masquer et redimensionner les blocs
depuis un catalogue de widgets.

**Cas d'usage.**
> Lundi matin, un coordinateur voit « 12 documents en attente de validation » et
> clique pour arriver directement sur la file à traiter.

??? note "Détails internes (équipe AroundLink)"
    KPIs : sortants, entrants, partenaires, places disponibles, documents en
    attente, OLA en attente, ToR en attente. Le jeu d'indicateurs est mis en cache
    par coordinateur pendant 30 s (chaque KPI est une requête distincte).
    `/mobility/` redirige vers le tableau de bord. Widgets fournis par
    `DashboardWidgetRegistry` ; données cloisonnées à l'établissement du coordinateur.
    Contrôleur : `DashboardController`.

## Tableau de bord Pilotage (DRI)

**À quoi ça sert.** C'est le cockpit stratégique du directeur des relations
internationales. Il regroupe les métriques en blocs — Vue d'ensemble, Décision,
Financier, Inclusion — pour éclairer les arbitrages de fond plutôt que le quotidien :
tendances de croissance, destinations sous tension, accords sous-utilisés,
consommation du budget, inclusion.

**Pour qui.** <span class="al-audience">gestionnaire RI (direction)</span>

**Comment ça marche.** Le pilotage est un tableau de bord modulaire : vous
choisissez les blocs affichés parmi des tuiles, graphiques, jauges, listes,
entonnoir et carte. On y trouve par exemple la croissance de la mobilité, la
répartition par type, le niveau d'études, les destinations sous tension, les
accords sous-utilisés, le taux d'occupation des places, l'entonnoir de campagne,
les meilleurs partenaires, la jauge de budget Erasmus consommé et l'inclusion.
La page est en lecture seule et reste cloisonnée à votre établissement.

**Cas d'usage.**
> Un DRI consulte la liste « Accords sous-utilisés » pour décider quels
> partenariats renégocier l'an prochain.

??? note "Détails internes (équipe AroundLink)"
    Catégories de blocs : Overview / Decision / Financial / Inclusion. Types de
    widgets : tuile, graphique, jauge, liste, entonnoir, carte. Même
    `DashboardWidgetRegistry` et `DashboardMetricsService` que le tableau de bord
    opérationnel ; icônes Tabler (`ti-*`). Contrôleur : `DashboardPilotageController`
    (route `/mobility/pilotage`, `ROLE_MOBILITY`).
