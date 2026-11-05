# Plateforme & sécurité

AroundLink est une plateforme **SaaS multi-établissement**. Cette page décrit le
modèle transverse : l'isolation des données, les types de comptes, la gestion des
droits, la connexion, et les offres commerciales. Le fonctionnement fin de chaque
écran est décrit dans les modules dédiés — ici on pose le cadre.

## Isolation des données (multi-établissement)

**À quoi ça sert.** Chaque établissement client ne voit que ses propres données —
étudiants, partenaires, accords, campagnes, communications, vues. Les données d'un
établissement ne sont jamais visibles par un autre. C'est la garantie de confiance
fondamentale de la plateforme.

**Pour qui.** <span class="al-audience">Tous les utilisateurs de l'espace établissement</span>

**Comment ça marche.** Quand un coordinateur est connecté, la plateforme restreint
automatiquement tout ce qu'il consulte à son propre établissement. Les données
réellement partagées (comme l'annuaire mondial [Atlas](../atlas/atlas.md)) sont
traitées séparément et clairement identifiées comme telles.

**Cas d'usage.**
> Deux universités clientes utilisent AroundLink le même jour ; aucune ne peut voir
> les étudiants, accords ou bourses de l'autre.

## Ce que vous écrivez sur un partenaire vous appartient

**À quoi ça sert.** Distinguer ce qui décrit un établissement partenaire de ce que
**vous**, en tant que client, avez consigné à son sujet. Deux écoles peuvent
travailler avec le même partenaire sans jamais voir les notes de l'autre.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Les contenus que vous renseignez sur un partenaire portent
la marque de votre établissement et ne sortent pas de chez vous :

- les **informations destinées à vos étudiants** sur ce partenaire (ressources,
  liens, foire aux questions) ;
- le **catalogue de cours** que vous tenez à jour pour lui ;
- les **scores de langue** que vous déclarez comme exigence ;
- les **fichiers** que vous déposez sur sa fiche, qui gardent trace de leur auteur.

Un autre client travaillant avec le même partenaire tient sa propre version de ces
contenus, sans interférence.

**Cas d'usage.**
> Deux écoles françaises envoient des étudiants à la même université espagnole.
> Chacune y maintient son catalogue de cours et ses consignes, sans jamais voir
> ceux de l'autre.

!!! info "L'identité appartient à l'établissement"
    Le nom, le pays, la ville, l'adresse, l'adresse e-mail, le site web et les
    accréditations d'un partenaire ne sont modifiables **que par cet établissement
    lui-même**, depuis son propre espace. Vous ne pouvez pas les changer depuis sa
    fiche : cette identité est unique et sert à tous — recherche, Atlas,
    correspondance ROR, échanges EWP. Ce que vous maîtrisez sur sa fiche, c'est
    votre propre couche : votre code interne et vos tags.

    Les identifiants officiels — ROR, code Erasmus, identifiant EWP, SCHAC — ne
    sont modifiables par personne : ils font foi.

## Types de comptes

**À quoi ça sert.** Trois profils d'utilisateurs cohabitent, chacun avec son espace
et ses droits, pour que chaque acteur ne voie que ce qui le concerne.

**Pour qui.** <span class="al-audience">Coordinateur RI · étudiant · partenaire</span>

**Comment ça marche.** On distingue :

- le **coordinateur RI** (gestionnaire de mobilité) qui travaille dans l'espace
  établissement ;
- l'**étudiant** qui accède à son [espace personnel](../etudiant/decouverte-candidature.md) ;
- le **partenaire** — un contact d'un établissement partenaire. Il reçoit son accès quand
  vous lui nommez un étudiant : il arrive dans **son propre espace**, où il ne retrouve que
  les étudiants que vous lui envoyez et votre fiche, jamais le reste du vôtre.

**Cas d'usage.**
> Une école nomme trois étudiants chez un partenaire. Sa responsable Erasmus reçoit le
> message, ouvre son accès, et consulte les trois dossiers — sans rien voir d'autre.


## Rôles & permissions de l'équipe (RBAC)

**À quoi ça sert.** Au sein d'un établissement, on définit des rôles d'équipe sur mesure
et l'on règle, rubrique par rubrique, ce que chaque rôle peut faire. Un grand service RI
délègue ainsi sans tout ouvrir à tout le monde.

**Pour qui.** <span class="al-audience">Coordinateur RI (administrateur de l'établissement)</span>

**Comment ça marche.** Un rôle dit **sur qui** il porte — domaines métier, sortants ou
entrants, campus, promotions — puis **ce qu'il peut faire**, rubrique par rubrique du menu,
avec quatre niveaux : **Aucun**, **Consulter**, **Préparer** (le dossier avance chez vous),
**Décider** (il sort de l'outil : valider, envoyer, exporter). Régler une catégorie suffit,
tout ce qu'elle contient suit ; on affine section par section si besoin. Un utilisateur sans
droit ne voit pas l'entrée de menu et ne peut pas non plus y accéder par une adresse
directe. Le détail est dans [Paramètres & équipe](../etablissement/parametres.md#roles-permissions).

**Cas d'usage.**
> La responsable crée un rôle « Chargé des entrants » : entrants seulement, campus de Lyon,
> « Décider » sur les documents, « Consulter » sur les accords, « Aucun » sur la bourse.


## Connexion & authentification unique (SSO)

**À quoi ça sert.** Votre personnel et vos étudiants se connectent avec le compte qu'ils
ont déjà — Microsoft ou Google — plutôt qu'avec un mot de passe de plus. Votre
établissement peut aussi l'imposer.

**Pour qui.** <span class="al-audience">Personnel et étudiants de l'établissement</span>

**Comment ça marche.** L'écran de connexion propose à tout le monde, en permanence, le mot
de passe et les boutons **Sign in with Microsoft** et **Sign in with Google**. Chaque
utilisateur **rattache lui-même** son compte depuis son profil, une fois, puis se connecte
avec. La connexion par mot de passe propose une réinitialisation par lien.

**Cas d'usage.**
> Une coordinatrice rattache son compte Microsoft professionnel depuis son profil. Le
> lendemain, elle clique sur « Sign in with Microsoft » et entre sans mot de passe.

!!! info "Vous êtes DSI ?"
    Protocole, permissions demandées, authentification imposée, contrôles de sécurité :
    **[Authentification unique (DSI)](sso.md)**.


## Accès applicatif (clé API & réseau EWP)

**À quoi ça sert.** Des accès machine, séparés de la connexion d'un utilisateur, relient
AroundLink à vos propres systèmes et authentifient les échanges avec les universités du
réseau [EWP](../ewp/ewp.md).

**Pour qui.** <span class="al-audience">DSI / intégrations · systèmes des universités partenaires</span>

**Comment ça marche.** Deux sortes de clés, dans **Paramètres ▸ Connectors ▸ API** :

| Clé | À qui elle appartient | Pour quoi |
|---|---|---|
| **Clé d'intégration** | à **l'établissement**, pas à une personne — elle survit au départ de celui qui l'a créée | un système qui tourne seul, comme votre logiciel de scolarité ; elle n'a que les droits de son rôle |
| **Clé personnelle** | à **une personne** | un usage ponctuel ; elle agit avec tous les droits de cette personne |

Une clé n'est affichée **qu'une fois**, à sa création : copiez-la tout de suite. Chaque
ligne montre la date de dernier usage — une date ancienne signale une intégration arrêtée.
Remplacer ou révoquer une clé coupe l'ancienne aussitôt. Le réseau EWP a sa propre
authentification, distincte.

L'API est documentée au format OpenAPI :
[api.aroundlink.com/apis/docs](https://api.aroundlink.com/apis/docs) ; pour le réseau EWP,
voir la [référence des API](../ewp/reference-api.md).


## Aide contextuelle

**À quoi ça sert.** Donner à chaque écran son mode d'emploi, sans quitter la page
ni chercher dans une documentation séparée.

**Pour qui.** <span class="al-audience">tous les utilisateurs connectés</span>

**Comment ça marche.** Un bouton « ? » est présent en haut à droite de chaque
page. Il ouvre un panneau qui explique ce que vous pouvez faire ici, en français
et en anglais, parfois accompagné d'une courte vidéo. Le panneau se ferme dès que
vous changez de page : ce que vous lisez correspond toujours à l'écran devant vous.

Chaque texte se termine par un lien de prise de rendez-vous : si l'explication ne
suffit pas, vous réservez un créneau de quinze minutes avec l'équipe AroundLink.

**Cas d'usage.**
> Un nouveau membre de l'équipe ouvre l'écran de distribution des places, clique
> sur « ? », comprend la logique de la grille, et saisit sans avoir à demander.

## Marketplace de services

**À quoi ça sert.** Un catalogue de services tiers (assurance, logement, banque…)
que l'on peut présenter aux étudiants, activable établissement par établissement.
Un espace de valeur ajoutée, affiché uniquement là où il est activé.

**Pour qui.** <span class="al-audience">Étudiant (côté consultation) · AroundLink (curation)</span>

**Comment ça marche.** Le catalogue de prestataires et d'offres est tenu à jour par
AroundLink ; un interrupteur par établissement décide si la marketplace apparaît
aux étudiants de cet établissement. Quand elle est active, les étudiants voient les
offres dans leur [espace Services](../etudiant/pendant-apres-mobilite.md), classées
par catégorie et qu'ils peuvent mettre en favori. Un établissement peut écarter
individuellement une offre qu'il ne souhaite pas voir proposée à ses étudiants. Il
s'agit d'affichage + affiliation (liens et codes promo vers le prestataire) : aucun
paiement ne transite par AroundLink, l'étudiant souscrit sur le site du partenaire.

**Cas d'usage.**
> AroundLink ajoute une offre « Assurance santé étudiante — dès 9 €/mois » ; elle
> apparaît aux étudiants des établissements ayant activé la marketplace.

