# Suivi des mobilités

Une fois le [parcours](parcours.md) branché, le suivi répond à la seule question qu'on se
pose en ouvrant un dossier : **où en est cet étudiant, et ai-je quelque chose à faire ?**

Le même suivi sert dans les deux sens — les étudiants que vous envoyez et ceux que vous
accueillez — avec les mêmes mots, les mêmes vues et les mêmes filtres.

## Les trois phases d'une mobilité

**À quoi ça sert.** Ranger les dossiers dans l'ordre du temps plutôt que dans l'ordre des
étapes. On ne pilote pas de la même façon quelqu'un qui n'est pas parti et quelqu'un qui est
rentré.

**Pour qui.** <span class="al-audience">toute l'équipe mobilité</span>

**Comment ça marche.** Chaque étape d'un parcours déclare sa phase, et la phase d'un dossier
est **la première qui n'est pas bouclée**. Elle n'est donc pas déclarative : elle se déduit
du travail réellement fait.

| Phase | Lu sur un dossier | Ce qu'elle couvre |
|---|---|---|
| **Before the mobility** | *Not departed* | tout ce qui précède le départ : pièces, contrat d'études, assurance |
| **During the mobility** | *On site* | le séjour : arrivée confirmée, cours, suivi sur place |
| **After the mobility** | *Returned* | le retour : attestation de départ, relevé de notes, avis |
| **Closed** | *Closed* | le dossier est clos |

!!! info "Une phase se déduit, elle ne se saisit pas"
    Vous ne déplacez pas un étudiant d'une phase à l'autre à la main. Faites avancer les
    étapes — ou laissez les reflets se cocher — et la phase suit. Un dossier terminé le dit
    même sans date de clôture.

## Deux vues du même suivi

**À quoi ça sert.** Le tableau pour traiter, le kanban pour voir venir.

**Comment ça marche.** Les deux vues partagent la même barre d'outils : recherche, tri,
filtres, choix des colonnes, vues enregistrées et export.

Le **tableau** aligne les dossiers en lignes, avec l'avancement chiffré, l'étape en cours et
qui est attendu. Huit colonnes facultatives s'ajoutent et se trient : **Destination**,
**City**, **Country**, **Region**, **Period**, **Level**, **Field of study**,
**Agreement**, **Workflow**.

Le **kanban** donne une colonne par phase et une carte par étudiant. Chaque colonne défile
dans elle-même, son titre reste visible, et la jauge en tête dit combien de dossiers ont
**franchi** l'étape — reflets compris. Vous choisissez jusqu'à treize informations à faire
apparaître sur les cartes, et toute la carte mène au dossier.

La recherche du kanban **propose des filtres pendant que vous tapez** : Destination, City,
Country, Region, Period, Level, Field of study, Agreement, Phase.

!!! tip "L'export reprend ce que vous avez sous les yeux"
    Le bouton **Export what is on screen** reprend vos filtres, vos colonnes affichées et
    votre tri. Il est disponible sur les deux vues et dans les deux sens.

## Où le trouver

**Comment ça marche.** Le suivi apparaît à quatre endroits, et c'est toujours le même écran :

- **l'onglet Mobility d'une campagne** — tous les sortants de cette campagne. Si aucun
  parcours n'est branché, l'onglet dit ce qui manque et propose de le brancher sur place ;
- **une session d'accueil** — tous les entrants de cette session ;
- **l'onglet Mobility d'une fiche étudiant** — un bloc par mobilité : un étudiant parti deux
  fois a deux dossiers, chacun avec ses dates et son avancement ;
- **le tableau de bord**, qui en donne le résumé par phase.

L'en-tête d'une mobilité se lit toujours de la même façon : **où**, **quoi**, **quand** — le
partenaire avec son logo, la famille d'accord, la période. Et le fil d'Ariane descend jusqu'à
la session ouverte.

![Le suivi d'une campagne en vue kanban](../assets/screenshots/onboarding-kanban.png)

*Une colonne par phase, une carte par étudiant. La jauge en tête de colonne compte ceux qui ont franchi l'étape.*

## La frise de la mobilité

**À quoi ça sert.** Lire une mobilité dans le temps, pas en liste : du premier vœu à la
clôture.

**Comment ça marche.** La frise porte de vraies dates et distingue ses deux sources — ce qui
vient de la campagne et ce qui vient du parcours. Elle ne remonte pas le temps, et le jour
même n'est pas compté comme passé. Les dates de campagne y figurent même si l'étudiant n'a
déposé aucun vœu.

C'est aussi ce que l'[agenda](agenda.md) d'un étudiant affiche : la frise datée de sa
mobilité, rangée en **en retard**, **à venir** et **passé**.

## Qui est attendu

**Comment ça marche.** Sur chaque ligne et chaque carte, **Waiting on** dit qui tient la
balle : l'étudiant, vous, ou personne quand l'étape est un reflet. Une étape que rien ne
bloque est **due**, pas en attente — la nuance évite de chercher un blocage qui n'existe pas.

Les raccourcis mènent directement à l'objet nommé : le nom d'un étudiant ouvre sa fiche, le
nom d'un parcours ouvre son atelier, la pastille d'un relevé ouvre l'écran de saisie.

**Cas d'usage.**
> Fin septembre, la coordinatrice ouvre l'onglet Mobility de la campagne. Le kanban montre
> quatre dossiers encore *Not departed* alors que les cours ont commencé. Elle filtre sur
> **Waiting on : vous**, voit trois contrats d'études qui attendent sa signature, les traite,
> et les trois cartes passent d'elles-mêmes en *On site*.
