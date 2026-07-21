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

## Types de comptes

**À quoi ça sert.** Trois profils d'utilisateurs cohabitent, chacun avec son espace
et ses droits, pour que chaque acteur ne voie que ce qui le concerne.

**Pour qui.** <span class="al-audience">Coordinateur RI · étudiant · partenaire invité</span>

**Comment ça marche.** On distingue :

- le **coordinateur RI** (gestionnaire de mobilité) qui administre l'espace
  établissement ;
- l'**étudiant** qui accède à son [espace personnel](../etudiant/decouverte-candidature.md) ;
- le **partenaire invité** — un contact d'un établissement partenaire à qui l'on
  ouvre un accès pour collaborer (par exemple approuver un accord bilatéral).

**Cas d'usage.**
> Un établissement invite le responsable Erasmus d'un partenaire ; celui-ci se
> connecte à son propre espace pour approuver un accord, sans rien voir d'autre.

??? note "Détails internes (équipe AroundLink)"
    Comptes distincts `AdminUser` (équipe AroundLink), `MobilityUser` (coordinateurs)
    et `StudentUser` (étudiants), tous dérivés d'un socle `User` commun. Les comptes
    partenaires sont des `MobilityUser` rattachés à l'établissement partenaire.

## Rôles & permissions de l'équipe (RBAC)

**À quoi ça sert.** Au sein d'un établissement, on peut définir des rôles d'équipe
sur mesure et régler, module par module, si chaque rôle a un accès nul, en lecture,
ou en écriture. Cela permet à un grand service RI de déléguer en toute sécurité.

**Pour qui.** <span class="al-audience">Coordinateur RI (administrateur de l'établissement)</span>

**Comment ça marche.** Un éditeur en forme de matrice croise les rôles de
l'établissement (en lignes) et les grands modules fonctionnels (en colonnes) —
Établissement, Documents, Formulaires, Workflow, Intégrations, Permissions
d'équipe — chaque case valant Aucun / Lecture / Écriture. Les droits sont appliqués
partout : un utilisateur sans droit ne voit pas l'entrée de menu et ne peut pas non
plus y accéder par une adresse directe.

**Cas d'usage.**
> Le responsable RI donne au rôle « Assistant » la lecture partout, mais l'écriture
> uniquement sur les Documents.

??? note "Détails internes (équipe AroundLink)"
    Rôles + matrice de permissions par établissement ; 6 modules
    (`institution`, `documents`, `forms`, `workflow`, `integrations`,
    `team_permissions`) × 3 niveaux (aucun/lecture/écriture). L'application est
    faite côté serveur (le menu ne fait que masquer). Réf. AROUNDLINK-348.

## Connexion & authentification unique (SSO)

**À quoi ça sert.** Les établissements peuvent laisser leur personnel (et leurs
étudiants) se connecter avec leur compte Microsoft/Azure institutionnel existant,
au lieu d'un mot de passe séparé — au choix, cela peut être imposé. Moins de mots
de passe à gérer, et une conformité aux exigences de la DSI.

**Pour qui.** Configuré par l'équipe AroundLink par établissement ; utilisé par le
personnel et les étudiants de l'établissement

**Comment ça marche.** À la connexion, la plateforme reconnaît l'établissement à
partir de l'adresse e-mail saisie ; si l'authentification unique est activée (ou
imposée), l'utilisateur est redirigé vers la page de connexion Microsoft, sinon il
peut utiliser un mot de passe. La connexion par mot de passe propose aussi une
réinitialisation classique.

**Cas d'usage.**
> Un coordinateur d'une université sous Azure clique sur « Se connecter », saisit
> son e-mail professionnel, et est automatiquement dirigé vers l'authentification
> Microsoft.

??? note "Détails internes (équipe AroundLink)"
    Configuration SSO par établissement (identifiant de tenant, activation,
    imposition, domaines e-mail autorisés). Flux Microsoft/Azure OpenID Connect.
    La configuration et le test se font depuis l'espace d'administration AroundLink.
    Les détails d'implémentation de l'authentification ne sont pas exposés ici.

## Accès applicatif (clé API & réseau EWP)

**À quoi ça sert.** Des canaux d'accès machine, séparés de la session
utilisateur, permettent de connecter AroundLink à des systèmes externes et
d'authentifier les échanges avec les universités partenaires du réseau
[EWP](../ewp/ewp.md).

**Pour qui.** <span class="al-audience">DSI / intégrations · systèmes des universités partenaires</span>

**Comment ça marche.** Chaque établissement dispose d'une clé API régénérable
(gérée dans [Paramètres](../etablissement/parametres.md)) pour ses intégrations, et
d'une authentification dédiée pour le réseau EWP. Ces accès machine sont
volontairement distincts de la connexion via le navigateur. L'API REST est
documentée de façon interactive (ressources, schémas, opérations) — voir la
[documentation de l'API (démo)](https://demo.aroundlink.com/api/docs) et, pour le
réseau EWP, la [référence des API EWP](../ewp/reference-api.md).

??? note "Détails internes (équipe AroundLink)"
    Surface `/api/*` sans état (JWT / clé API) séparée des API internes de
    l'application ; authentification partenaire EWP par signature de requête. Ne
    jamais divulguer une clé.

## Offres : établissement payant / gratuit

**À quoi ça sert.** Chaque établissement est soit un client payant, soit un client
gratuit ; certains modules premium (par exemple la [bourse de
mobilité](../etablissement/bourse.md) ou la création d'[accords
bilatéraux](../etablissement/accords.md)) sont réservés aux clients payants. C'est
le mécanisme commercial de la plateforme.

**Pour qui.** <span class="al-audience">Établissement client (défini par AroundLink)</span>

**Comment ça marche.** L'offre de l'établissement (payante par défaut, ou gratuite)
conditionne l'accès aux modules premium — masqués dans le menu et bloqués à l'accès
direct pour un client gratuit. Cette offre est indépendante des frais de scolarité
éventuels payés par l'étudiant.

**Cas d'usage.**
> Un partenaire en offre gratuite peut relire et approuver un accord bilatéral qu'un
> établissement payant lui a soumis, mais ne peut pas ouvrir les modules premium.

??? note "Détails internes (équipe AroundLink)"
    `MobilityPlanEnum` (payant/gratuit), appliqué côté serveur par un contrôle
    d'accès dédié. Modèle réutilisable pour tout futur module premium.

## Marketplace de services

**À quoi ça sert.** Un catalogue de services tiers (assurance, logement, banque…)
que l'on peut présenter aux étudiants, activable établissement par établissement.
Un espace de valeur ajoutée, affiché uniquement là où il est activé.

**Pour qui.** <span class="al-audience">Étudiant (côté consultation) · AroundLink (curation)</span>

**Comment ça marche.** Le catalogue de prestataires et d'offres est tenu à jour par
AroundLink ; un interrupteur par établissement décide si la marketplace apparaît
aux étudiants de cet établissement. Quand elle est active, les étudiants voient les
offres dans leur [espace Services](../etudiant/pendant-apres-mobilite.md). Il s'agit
d'affichage + affiliation (liens et codes promo vers le prestataire) : aucun paiement
ne transite par AroundLink, l'étudiant souscrit sur le site du partenaire.

**Cas d'usage.**
> AroundLink ajoute une offre « Assurance santé étudiante — dès 9 €/mois » ; elle
> apparaît aux étudiants des établissements ayant activé la marketplace.

??? note "Détails internes (équipe AroundLink)"
    Interrupteur `University.marketplaceEnabled`. Offres/​prestataires gérés côté
    AroundLink (hors du présent site) ; affichage étudiant conditionné au drapeau.
