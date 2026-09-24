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

![Écran des campus](../assets/screenshots/parametres-campus.png)

*Vos sites physiques, avec le nombre d'étudiants rattachés à chacun.*

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

![Niveaux d'études personnalisés](../assets/screenshots/parametres-niveaux.png)

*Vos propres libellés de niveaux, chacun rattaché à un niveau européen, avec le nombre d'étudiants, d'établissements et de places qui en dépendent.*

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

## Suppressions protégées

**À quoi ça sert.** Vous empêcher de supprimer un réglage encore utilisé quelque
part, et vous dire précisément où il sert.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Vos campus, périodes, niveaux d'études, types de documents
et tags affichent un compteur d'utilisation. Tant qu'il n'est pas à zéro, la
suppression est refusée et le détail vous indique ce qui s'y rattache — un accord,
une campagne, un dossier étudiant.

Vous restez libre de renommer un élément à tout moment : le changement se propage
partout où il apparaît, sans rien casser.

**Cas d'usage.**
> Le coordinateur veut supprimer une période devenue inutile ; le compteur lui
> montre qu'elle sert encore dans trois accords, qu'il ajuste avant de recommencer.

## Tags

**À quoi ça sert.** Créer vos propres étiquettes pour organiser vos étudiants et
vos établissements partenaires selon vos critères à vous — une promotion, un
programme, un groupe de destinations, un point de vigilance.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Chaque tag porte un nom et une couleur, et s'applique à
l'un des trois périmètres suivants :

- **Général** — proposé à la fois sur les étudiants et sur les partenaires
- **Étudiant** — proposé sur les étudiants uniquement
- **Établissement** — proposé sur les partenaires uniquement, et utilisable comme
  filtre de campagne

Une fois vos tags créés, vous les posez depuis les listes d'étudiants ou de
partenaires. Sélectionnez plusieurs lignes pour en ajouter ou en retirer à
l'ensemble de la sélection en une seule fois.

![Écran des tags](../assets/screenshots/parametres-tags.png)

*Vos tags, leur périmètre et leur couleur, avec le nombre d'établissements et d'étudiants sur lesquels chacun est posé.*

**Cas d'usage.**
> Le coordinateur crée un tag « Échange double diplôme » sur le périmètre
> Établissement, l'applique à ses douze partenaires concernés, puis s'en sert
> pour restreindre les destinations d'une campagne.

!!! warning "Périmètre et filtres de campagne"
    Un tag change de périmètre après avoir été utilisé dans une campagne cesse
    d'y être pris en compte. Vérifiez vos campagnes en cours avant de modifier le
    périmètre d'un tag existant.

## Filtres étudiants

**À quoi ça sert.** Décrire vos étudiants avec vos propres critères — et, quand
vous le décidez, rendre ces critères visibles à vos étudiants dans leur recherche
de destination.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Un filtre étudiant porte un nom et une couleur, et
s'applique aux étudiants ou aux établissements. Vous le posez depuis la fiche
d'un étudiant, juste à côté de ses tags, et vous le retrouvez comme colonne dans
vos listes : elle se trie et se filtre comme ses voisines.

La différence avec un tag tient en une phrase : **un tag reste chez vous, un
filtre étudiant se montre**. Cochez « Visible aux étudiants » et la valeur
apparaît dans « Find your exchange », où vos étudiants la choisissent comme un
pays ou une langue. « Match my profile » présélectionne alors les valeurs que
l'étudiant porte déjà.

![Filtres étudiants](../assets/screenshots/parametres-filtres-etudiants.png)

*Vos filtres, leur couleur, et le nombre d'établissements et d'étudiants sur lesquels chacun est posé.*

**Cas d'usage.**
> Le coordinateur crée le filtre « Double diplôme », le pose sur les étudiants
> concernés et le rend visible. Un étudiant qui le porte ouvre sa recherche de
> destination : le filtre est déjà coché, et il ne voit que les destinations qui
> le concernent.

!!! tip "Tag ou filtre étudiant ?"
    Posez-vous la question de qui doit voir la valeur. Un point de vigilance
    interne, un rappel d'équipe, un suivi administratif : c'est un tag. Une
    caractéristique que l'étudiant reconnaît et sur laquelle il choisit sa
    destination : c'est un filtre étudiant.

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

![Périodes de mobilité](../assets/screenshots/parametres-periodes.png)

*Vos périodes, avec le nombre d'établissements et de places qui s'appuient sur chacune.*

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

## Ce que vos étudiants voient

**À quoi ça sert.** Régler deux informations sensibles que vos étudiants voient — ou ne
voient pas — sans que cela change quoi que ce soit pour votre équipe.

**Pour qui.** <span class="al-audience">admin</span>

**Comment ça marche.** Deux interrupteurs, indépendants l'un de l'autre.

**Le classement.** Par défaut, un étudiant voit son rang dans sa promotion sur son propre
profil. Vous pouvez le lui masquer : vous et votre équipe continuez de le voir, lui non.

**Le nombre de places.** Par défaut, vos étudiants voient combien de places vous ouvrez sur
chaque partenaire et chaque période. Vous pouvez n'afficher que l'existence d'une place
disponible, sans le nombre.

![Réglages de la vue étudiante](../assets/screenshots/parametres-vue-etudiante.png)

*Les deux interrupteurs, avec sous chacun la phrase qui dit ce que l'étudiant verra.*

**Cas d'usage.**
> L'établissement ne souhaite pas que le classement circule entre étudiants avant la
> commission. L'admin le masque le temps de la campagne, et le rétablit ensuite — les
> coordinateurs, eux, l'ont vu tout du long.

## Rôles & permissions

**À quoi ça sert.** Définir qui peut faire quoi, et **sur qui** — en adaptant les accès à
votre organisation plutôt qu'à un découpage imposé.

**Pour qui.** <span class="al-audience">admin</span>

**Comment ça marche.** Un rôle se construit en deux temps.

**D'abord son périmètre**, c'est-à-dire ce sur quoi il porte. Quatre questions, dans cet
ordre : les **domaines métier** concernés, la **direction** (sortants seulement, entrants
seulement, ou les deux), les **campus**, les **promotions**. Les listes proposées sont
celles de vos propres réglages, jamais une liste générique. Ne rien cocher sur les campus ou
les promotions signifie « tous ».

Le métier se choisit en premier parce qu'il élague la suite : régler des droits puis
découvrir que la moitié disparaît serait du travail jeté.

**Ensuite ses droits**, ligne par ligne, avec quatre niveaux :

| Niveau | Ce qu'il permet |
|---|---|
| **Aucun** | Rien. Posé sur une catégorie, il ferme tout ce qu'elle contient. |
| **Consulter** | Consulter et chercher. Aucune modification ne sort de l'outil. |
| **Préparer** | Créer, modifier, déposer — le dossier avance, à l'intérieur. |
| **Décider** | Valider, refuser, envoyer, supprimer, exporter — cela sort de l'outil. |

La frontière utile est celle-ci : **« Préparer » fait avancer un dossier chez vous,
« Décider » le fait sortir**. Les quatre niveaux sont posés côte à côte sur chaque ligne,
sans menu déroulant : voir la valeur voisine fait partie de l'information.

![Le sélecteur de niveaux](../assets/screenshots/parametres-role-niveaux.png)

*Une ligne de droits : les quatre niveaux alignés, celui qui s'applique en couleur, et la flèche qui rend la ligne à ce dont elle hérite.*

![Le périmètre d'un rôle](../assets/screenshots/parametres-role-perimetre.png)

*L'étape du périmètre : les domaines métier, la direction, les campus et les promotions. Ne rien cocher sur les campus ou les promotions revient à tous les couvrir.*

![L'arbre des droits](../assets/screenshots/parametres-roles.png)

*L'arbre complet : chaque section de l'application, et sous elle les actions qu'un rôle peut porter.*

**Comparer deux rôles.** Un bouton affiche le même arbre avec une colonne par rôle. C'est
ainsi qu'on répond à « qui peut valider une bourse, au juste ? » sans ouvrir les rôles un
par un — et qu'on découvre à temps que personne ne le peut, parce que chacun croyait que
c'était l'autre.

![Comparaison de rôles](../assets/screenshots/parametres-roles-comparaison.png)

*Le même arbre, une colonne par rôle : on lit d'un trait qui décide, qui prépare et qui ne voit rien.*

**Un filet.** Vous ne pouvez pas retirer le dernier administrateur de votre établissement.

**Ce que voient les autres.** Quand un droit manque, l'écran le dit au lieu de faire
semblant : un bandeau annonce la lecture seule, et une mention explique qu'un étudiant est
hors de votre périmètre.

**Cas d'usage.**
> La responsable crée un rôle « Chargé des entrants » : périmètre limité aux entrants et au
> campus de Lyon, « Décider » sur les documents, « Consulter » sur les accords, « Aucun »
> sur la bourse.

## Mes permissions

**À quoi ça sert.** Voir soi-même ce qu'on a le droit de faire, et sur qui.

**Pour qui.** <span class="al-audience">tout membre de l'équipe</span>

**Comment ça marche.** L'écran énonce vos droits en clair et rappelle votre périmètre.

Il n'est protégé par aucune permission, et c'est volontaire : plus un rôle est restreint,
plus la personne a besoin de comprendre pourquoi un écran lui est fermé. Sans lui, chaque
restriction ressemble à une panne, et quelqu'un doit aller lire la configuration à sa place.

![Mes permissions](../assets/screenshots/parametres-mes-permissions.png)

*Vos droits énoncés en phrases — de qui vous voyez les dossiers, et ce que vous pouvez faire dans chaque section.*

## Fiche d'un contact

**À quoi ça sert.** Réunir sur un seul écran tout ce que vous savez d'un contact, qu'il
soit une personne de votre annuaire, un membre de votre équipe, ou les deux.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Un contact d'annuaire et un compte de connexion désignaient
auparavant deux fiches distinctes, sans lien entre elles. C'est désormais **un seul
contact, une seule page** : vos grilles de contacts et la liste de votre équipe mènent au
même endroit, et vous y voyez aussi bien ses coordonnées que l'état de son accès.

## Annuaire des utilisateurs

**À quoi ça sert.** Une vue d'ensemble, en lecture seule, de tous les
utilisateurs liés à votre établissement — étudiants, membres de l'équipe et
utilisateurs partenaires invités — filtrable par type, statut et recherche libre.

**Pour qui.** <span class="al-audience">gestionnaire RI / admin</span>

**Comment ça marche.** Une page regroupe l'ensemble des utilisateurs de
l'organisation et permet de les filtrer par catégorie, par statut ou par
nom/e-mail. Elle est réservée aux plans de mobilité payants.

![Écran d'import](../assets/screenshots/parametres-imports.png)

*Un import : le modèle à télécharger, les colonnes obligatoires, et l'aperçu ligne par ligne avant confirmation.*

**Cas d'usage.**
> L'admin recherche un utilisateur par e-mail pour vérifier son statut et sa
> catégorie.

??? note "Détails internes (équipe AroundLink)"
    `SettingsController::users()`. Vue agrégée en lecture seule construite par un
    service dédié, réservée aux établissements en plan payant.
