# Paramètres & équipe

Les **Paramètres** rassemblent la configuration administrative de votre
établissement : sa structure (campus, composantes, niveaux d'études), la gestion
de l'équipe et de ses droits, l'annuaire des utilisateurs, les vues de travail
personnalisées et la connexion aux systèmes externes. C'est le centre de contrôle
du bureau des relations internationales.

## Campus

**À quoi ça sert.** Déclarer les campus de votre établissement (nom, ville, pays,
un campus principal), afin de rattacher les étudiants à un campus et de refléter
votre structure réelle.

**Pour qui.** <span class="al-audience">gestionnaire RI / admin</span>

**Comment ça marche.** Un écran de gestion (Paramètres ▸ Établissement) liste les
campus avec le nombre d'étudiants rattachés à chacun. La suppression est bloquée
si des étudiants y sont encore rattachés, pour éviter toute perte de lien.

**Cas d'usage.**
> Une école multi-sites déclare les campus de Paris et de Lyon, puis y affecte
> ses étudiants.

??? note "Détails internes (équipe AroundLink)"
    `CampusesController`. Entité `Campus` (université, nom, ville, pays,
    indicateur principal). La suppression vérifie le nombre d'étudiants
    rattachés. La propriété est contrôlée à la modification et à la suppression.

## Composantes (OUnits)

**À quoi ça sert.** Tenir à jour les composantes EWP de votre établissement
(facultés, départements), pour que les échanges de données Erasmus (EWP) fassent
référence aux bonnes sous-structures.

**Pour qui.** <span class="al-audience">gestionnaire RI / admin</span>

**Comment ça marche.** Un écran de gestion liste les composantes, chacune avec un
nom, une description optionnelle et un identifiant. Le fonctionnement reprend
celui des campus.

**Cas d'usage.**
> Le bureau déclare la « Faculté d'ingénierie » comme composante avec son
> identifiant EWP.

??? note "Détails internes (équipe AroundLink)"
    `OunitsController`. Entité `Ounit` (université, nom, description, identifiant
    de composante). Écran calqué sur celui des campus.

## Niveaux d'études personnalisés

**À quoi ça sert.** Nommer vos niveaux d'études avec votre propre vocabulaire (par
exemple « Aéro 4 », « M1 Ingé ») tout en conservant en arrière-plan une
correspondance standard (EQF) — pour que les listes déroulantes soient familières
à votre équipe et que les échanges EWP restent conformes aux standards.

**Pour qui.** <span class="al-audience">gestionnaire RI / admin</span>

**Comment ça marche.** Un écran de gestion (Paramètres ▸ Établissement) permet de
créer, modifier et supprimer vos libellés de niveaux, chacun associé à un niveau
EQF. Chaque ligne indique combien de places ou d'accords utilisent ce niveau. Les
libellés en double sont refusés.

**Cas d'usage.**
> Une école d'ingénieurs définit « Aéro 4 » associé à l'EQF 7, afin de filtrer
> campagnes et accords par ses véritables intitulés de niveau.

??? note "Détails internes (équipe AroundLink)"
    `AcademicLevelSettingsController`. Entité `AcademicLevelCustom` (université,
    libellé unique par établissement, niveau EQF). Les entités consommatrices
    enregistrent la valeur EQF standard, pas le libellé, afin de préserver la
    compatibilité des exports EWP/OLA.

## Clé de connexion aux systèmes externes

**À quoi ça sert.** Fournir à votre établissement une clé permettant de connecter
AroundLink à vos systèmes externes (échanges de données, intégrations), avec la
possibilité de la renouveler si nécessaire.

**Pour qui.** <span class="al-audience">admin</span>

**Comment ça marche.** Une page présente votre clé de connexion et propose une
action « Régénérer » qui remplace la clé existante par une nouvelle. Conservez
cette clé confidentielle : ne la partagez qu'avec les personnes qui configurent
vos intégrations.

**Cas d'usage.**
> Après un changement d'équipe technique, l'admin régénère la clé pour révoquer
> l'ancienne.

!!! warning "Confidentialité"
    Une clé de connexion est un identifiant sensible. Ne la diffusez jamais
    publiquement et régénérez-la si vous pensez qu'elle a pu être exposée.

??? note "Détails internes (équipe AroundLink)"
    `ApiKeyController`. La clé est créée à la première visite et renouvelable en
    un clic. Rattachée au compte de l'utilisateur.

## Vues enregistrées

**À quoi ça sert.** Enregistrer une configuration de tableau (colonnes choisies,
largeurs, filtres, ordre de tri) sur une page donnée, puis la réappliquer en un
clic. Chaque coordinateur retrouve instantanément sa mise en page de travail sans
la reconstruire à chaque fois.

**Pour qui.** <span class="al-audience">gestionnaire RI</span>

**Comment ça marche.** Sur une page à tableau, vous ajustez les colonnes, les
filtres et le tri, puis vous enregistrez cette disposition comme une vue. Vous
pouvez ensuite basculer d'un clic entre vos vues. Les vues sont propres à votre
établissement.

**Cas d'usage.**
> Un coordinateur enregistre une vue « Partenaires Espagne — accords actifs » avec
> ses colonnes et filtres, et la rouvre en un clic à chaque session.

## Équipe & invitations

**À quoi ça sert.** Gérer les membres de votre bureau : préparer leurs comptes en
amont, puis leur ouvrir l'accès au bon moment. Idéal pour un démarrage groupé le
jour du lancement.

**Pour qui.** <span class="al-audience">admin</span>

**Comment ça marche.** Vous créez les comptes de l'équipe dans un état « en
attente », sans envoi d'e-mail. Le jour venu, vous ouvrez l'accès individuellement
ou pour tous les comptes en attente à la fois : chaque membre reçoit alors son
invitation. Les envois sont tolérants aux erreurs — un échec isolé n'interrompt
pas l'ensemble.

**Cas d'usage.**
> Pendant la mise en route, l'admin prépare 8 comptes (en attente), puis clique
> sur « Envoyer tous les accès » le jour du lancement.

??? note "Détails internes (équipe AroundLink)"
    `SettingsController::team()` et envois d'accès. Statut d'accès (en attente /
    invité…). Les invitations partent via un e-mail dédié. Chaque nouveau membre
    est aussi relié aux contacts partenaires existants qui le concernent.

## Rôles & permissions

**À quoi ça sert.** Définir précisément qui peut voir et modifier quoi, grâce à des
rôles personnalisés et une matrice de droits par module. Chaque établissement
adapte les accès à son organisation.

**Pour qui.** <span class="al-audience">admin</span>

**Comment ça marche.** Vous créez des rôles, puis vous réglez, pour chaque rôle et
chaque module de l'application, un niveau d'accès (par exemple lecture ou
lecture/écriture) dans une matrice. Les modifications s'appliquent à tous les
membres portant le rôle.

**Cas d'usage.**
> L'admin crée un rôle « Coordinateur » avec accès en écriture aux partenaires
> mais en lecture seule aux paramètres.

??? note "Détails internes (équipe AroundLink)"
    `SettingsController::roles()`. Rôles par établissement, matrice de permissions
    par module et niveau d'accès. Les droits pilotent l'accès aux différentes
    zones de l'espace Mobilité.

## Annuaire des utilisateurs

**À quoi ça sert.** Une vue d'ensemble, en lecture seule, de tous les
utilisateurs liés à votre établissement — étudiants, membres de l'équipe et
utilisateurs partenaires invités — filtrable par type, statut et recherche libre.

**Pour qui.** <span class="al-audience">gestionnaire RI / admin</span>

**Comment ça marche.** Une page regroupe l'ensemble des utilisateurs de
l'organisation et permet de les filtrer par catégorie, par statut ou par
nom/e-mail. Elle est réservée aux plans de mobilité payants.

**Cas d'usage.**
> L'admin recherche un utilisateur par e-mail pour vérifier son statut et sa
> catégorie.

??? note "Détails internes (équipe AroundLink)"
    `SettingsController::users()`. Vue agrégée en lecture seule construite par un
    service dédié, réservée aux établissements en plan payant.
