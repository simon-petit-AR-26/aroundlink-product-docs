# Réseau EWP (Erasmus Without Paper)

EWP (Erasmus Without Paper) est le standard européen d'interopérabilité qui permet
aux services des relations internationales d'échanger leurs données de mobilité de
façon entièrement numérique, sans papier ni e-mails manuels. AroundLink connecte
votre établissement à ce réseau : vos accords inter-établissements, contrats
pédagogiques, relevés de notes et nominations circulent directement de logiciel à
logiciel avec vos universités partenaires. Concrètement, un accord signé chez vous
apparaît chez le partenaire, une note saisie ici part vers l'université d'origine de
l'étudiant, et chaque changement notifie l'autre côté automatiquement.

## Découverte / Manifest

**À quoi ça sert.** Le manifest est la carte de visite numérique de votre
établissement sur le réseau EWP. Il indique à toutes les universités partenaires
quels services vous proposez et comment vous joindre de façon fiable. Sans lui,
aucun partenaire ne peut vous découvrir ni échanger quoi que ce soit avec vous.

**Pour qui.** <span class="al-audience">établissement partenaire / admin</span>

**Comment ça marche.** AroundLink publie et tient à jour ce manifest pour votre
établissement. Un partenaire (ou l'annuaire central du réseau) le consulte pour
savoir que vous savez échanger accords, contrats pédagogiques, relevés de notes et
nominations, puis établit une relation de confiance. Tout est automatique : vous
n'avez rien à publier manuellement.

**Cas d'usage.**
> Une université espagnole vous ajoute comme partenaire ; son logiciel lit votre
> manifest et découvre aussitôt qu'il peut vous envoyer un accord numérique.

??? note "Détails internes (équipe AroundLink)"
    Discovery API v6. Le manifest est servi sur `/ewp/{ewpHeiId}/manifest.xml`,
    identifié par le HEI ID de l'université cliente. Il déclare 15 entrées d'API :
    discovery, echo, institutions, omobilities, omobility-cnr, omobility-las,
    omobility-la-cnr, iias, iia-cnr, iias-approval, iia-approval-cnr, imobility-tors,
    imobility-tor-stats, imobility-tor-cnr et factsheet, chacune avec sa version et
    son URL. Le manifest est auto-validé avant publication (503 si invalide) et mis
    en cache 1 h. Seules les universités clientes AroundLink exposent un manifest ;
    les établissements partenaires seuls renvoient 404. Le provisioning d'un
    établissement (clés incluses) se fait via une commande console dédiée.

## Echo

**À quoi ça sert.** Echo est un test de connectivité : il confirme que votre
établissement et un partenaire arrivent bien à se joindre et à s'authentifier
mutuellement. C'est l'outil de diagnostic utilisé au moment de brancher un nouveau
partenaire, avant que les vraies données ne circulent.

**Pour qui.** <span class="al-audience">établissement partenaire / admin</span>

**Comment ça marche.** Un appel de test renvoie exactement les informations
envoyées, accompagnées de l'identité vérifiée de l'appelant. Une réponse correcte
prouve que la liaison et la confiance entre les deux établissements fonctionnent.

**Cas d'usage.**
> Lors de l'intégration d'un partenaire, l'équipe envoie un appel Echo ; une réponse
> réussie confirme que la poignée de main de confiance est opérationnelle.

??? note "Détails internes (équipe AroundLink)"
    Echo API v2, exposé sur `/ewp/{ewpHeiId}/echo`. La réponse renvoie l'identité
    (HEI ID) réellement authentifiée de l'appelant, jamais une valeur fournie par le
    client. Les réponses EWP ne sont jamais compressées (les empreintes d'intégrité
    se calculent sur le corps non compressé). Sert de sonde de connectivité et de
    validation de la chaîne d'authentification.

## Institutions

**À quoi ça sert.** Cette brique publie l'identité de base de votre établissement
(son nom officiel) à partir de son identifiant. Elle permet aux partenaires
d'afficher un nom lisible au lieu d'un code technique dans leurs écrans.

**Pour qui.** <span class="al-audience">établissement partenaire</span>

**Comment ça marche.** Un partenaire fournit un ou plusieurs identifiants
d'établissement et reçoit en retour les noms correspondants. Ses interfaces peuvent
alors présenter vos accords et mobilités avec un intitulé humain.

**Cas d'usage.**
> Un partenaire affiche « Institut Polytechnique des Sciences Avancées » à côté d'un
> accord entrant, plutôt que l'identifiant technique de l'établissement.

??? note "Détails internes (équipe AroundLink)"
    Institutions API v2 (déclarée 2.2.0), jusqu'à 10 HEI IDs par requête
    (`max-hei-ids=10`). La réponse actuelle est minimale (hei-id + nom en anglais) ;
    les informations riches (adresses, contacts, calendriers) sont portées par
    l'API Factsheet plutôt qu'ici.

## Factsheet (fiche établissement)

La factsheet est la fiche pratique de votre établissement : dates de nomination et
de candidature, contacts logement / visa / assurance, accessibilité, délais de
décision et de relevé de notes. AroundLink couvre trois usages complémentaires.

### Publier votre factsheet

**À quoi ça sert.** Vous diffusez à tout le réseau vos informations pratiques, pour
que les partenaires renseignent leurs étudiants sortants sans avoir à vous écrire.

**Pour qui.** <span class="al-audience">établissement partenaire</span>

**Comment ça marche.** Dès qu'un partenaire demande votre fiche, AroundLink la
génère à partir des informations saisies par votre service et la renvoie dans un
format conforme au réseau.

**Cas d'usage.**
> Un partenaire consulte votre factsheet et voit vos dates limites de candidature
> sans avoir à envoyer un e-mail au bureau des relations internationales.

### Éditer votre factsheet

**À quoi ça sert.** Vous maintenez, depuis un simple formulaire, le contenu de la
fiche qui sera diffusée à l'ensemble de vos partenaires.

**Pour qui.** <span class="al-audience">gestionnaire RI</span>

**Comment ça marche.** Depuis l'écran dédié de votre espace, vous remplissez et
mettez à jour les rubriques de la fiche. Les champs mal renseignés (par exemple un
numéro de téléphone sans indicatif) sont signalés avant enregistrement.

**Cas d'usage.**
> Le gestionnaire RI met à jour les dates de nomination du semestre de printemps ;
> la nouvelle fiche est aussitôt disponible pour les partenaires.

### Récupérer la factsheet d'un partenaire

**À quoi ça sert.** Vous importez à la demande la fiche pratique d'un partenaire,
pour retrouver ses dates et contacts directement dans AroundLink au lieu de les
chercher ailleurs.

**Pour qui.** <span class="al-audience">gestionnaire RI</span>

**Comment ça marche.** Depuis la fiche d'un établissement partenaire, une action de
synchronisation va chercher sa factsheet sur le réseau et la stocke chez vous. Les
champs que vous avez verrouillés manuellement ne sont jamais écrasés ; si le
partenaire n'expose pas de fiche, vos données saisies à la main sont conservées.

**Cas d'usage.**
> Avant une campagne, le gestionnaire synchronise la factsheet d'un partenaire pour
> afficher ses délais de décision directement dans le dossier de l'accord.

??? note "Détails internes (équipe AroundLink)"
    Factsheet API v1.2, `max-hei-ids=1`, authentification client anonyme autorisée
    (donnée publique). Publication (entrant) sur `/ewp/{ewpHeiId}/factsheet` ; les
    blocs optionnels vides retombent sur le contact de l'établissement puis sur des
    valeurs de repli pour rester conformes au schéma. Édition interne via
    `/mobility/ewp-factsheet` (ROLE_MOBILITY + MODULE_WRITE:institution), une
    factsheet par université. Récupération (sortant) via un service de
    synchronisation qui interroge d'abord le registre pour vérifier que le partenaire
    expose bien l'API, puis mappe la réponse sur l'entité `EwpFactsheet` — les
    champs verrouillés et 6 champs locaux hors schéma EWP ne sont jamais touchés
    (ticket AROUNDLINK-324). Déclenchable depuis l'écran accord ou en ligne de
    commande.

## IIA — accords inter-établissements

L'échange d'accords inter-établissements (IIA) est la fonction phare : négocier,
comparer et signer des accords Erasmus+ bilatéraux sans papier, avec une copie
partagée entre les deux établissements. Cela correspond aux **accords** dans
AroundLink.

**À quoi ça sert.** Vous gérez tout le cycle de vie d'un accord — contenu,
conditions de mobilité, contacts, dates de signature — de façon numérique et
partagée avec le partenaire. Fini les versions PDF divergentes échangées par e-mail :
les deux côtés travaillent sur une même référence.

**Pour qui.** <span class="al-audience">gestionnaire RI / établissement partenaire</span>

**Comment ça marche.** Le partenaire peut lister et consulter les accords qu'il
partage avec vous. Chaque établissement approuve la version exacte qu'il a sous les
yeux ; quand les deux ont approuvé, l'accord est en vigueur. Toute modification d'un
côté notifie automatiquement l'autre, qui récupère la version fraîche.

**Cas d'usage.**
> Vous ajustez le nombre de places d'un accord ; le partenaire est notifié, récupère
> la nouvelle version, l'approuve, et l'accord bascule « en vigueur » des deux côtés.

### Notification de changement (CNR) et revue

**À quoi ça sert.** Lorsqu'un partenaire modifie un accord, vous êtes prévenu et
vous décidez champ par champ ce que vous acceptez, plutôt que de subir un écrasement
automatique. C'est le garde-fou qui protège l'intégrité de vos données.

**Pour qui.** <span class="al-audience">gestionnaire RI</span>

**Comment ça marche.** Une notification de changement déclenche la récupération de la
version du partenaire. AroundLink prépare une comparaison côte à côte et met la
proposition en attente de revue (jamais appliquée automatiquement) ; le coordinateur
est averti par e-mail. Il accepte les champs souhaités, l'accord repasse alors en
brouillon pour une nouvelle approbation, ou rejette sans toucher à ses données.

**Cas d'usage.**
> Un partenaire change une langue d'enseignement ; le coordinateur voit la
> différence, accepte cette seule modification et laisse le reste inchangé.

??? note "Détails internes (équipe AroundLink)"
    IIAs API v7.0.1, `max-iia-ids=100`. Entités : `Exchange`. Endpoints entrants :
    `iias/index` (filtres partenaire, année académique reçue, modified_since),
    `iias/get` (contenu complet), `iias/approval` (empreinte iia-hash),
    `iias/stats` (compteurs par état d'approbation). L'iia-hash v7 ne couvre que les
    champs « stratégiques » (mobilités, langues, ISCED, EQF) et exclut contacts, PDF,
    in-effect, iia-code. Cloisonnement multi-locataire : chaque endpoint ne renvoie
    que les accords où l'appelant authentifié est le partenaire, pour ne pas exposer
    de volume ou de contenu vis-à-vis d'un tiers.

    Notifications de changement : iia-cnr v3, iia-approval-cnr v2. Entrant — une
    notification `iia-cnr` déclenche une re-récupération de l'accord, un diff, puis un
    `ExchangeIiaPendingUpdate` en statut PENDING_REVIEW + e-mail coordinateur ;
    l'idempotence se base sur l'empreinte complète de la charge utile (pas sur
    l'iia-hash). Si l'accord est inconnu, une coquille minimale d'Exchange est créée.
    Sortant — l'édition d'un accord chez nous émet un `iia-cnr` vers le partenaire ;
    une notification `iia-approval-cnr` entrante re-récupère l'approbation du
    partenaire. Revue interne via `/mobility/iia-reviews` : diff granulaire au champ
    (y compris ajout/retrait de mobility-specs), application sélective qui recalcule
    l'iia-hash et remet l'approbation à DRAFT.

## OLA — contrats pédagogiques (Learning Agreements)

Échange et co-signature numériques des contrats pédagogiques (OLA) des étudiants que
vous envoyez en mobilité. Voir aussi la page [Learning Agreement](../etablissement/documents.md).

**À quoi ça sert.** Vous publiez les contrats pédagogiques de vos étudiants sortants
— cours suivis, cours reconnus au retour, signatures — pour que l'université
d'accueil les relise et les signe en ligne. L'aller-retour de validation se fait sans
papier.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur / établissement partenaire</span>

**Comment ça marche.** L'université d'accueil peut lister et récupérer les contrats
de vos étudiants, puis les approuver ou demander des modifications. À l'approbation,
sa signature est enregistrée ; quand les deux côtés ont signé, le contrat est
validé. Si le partenaire signale un changement de son côté, AroundLink récupère
automatiquement la version à jour.

**Cas d'usage.**
> L'université d'accueil approuve le contrat pédagogique d'un étudiant en ligne ; le
> statut passe à « validé » dans AroundLink et la reconnaissance est enclenchée.

??? note "Détails internes (équipe AroundLink)"
    omobility-las API v1.2. Entité : `LearningAgreement` (AroundLink est
    l'établissement d'envoi). Endpoints entrants : `omobility-las/index`,
    `omobility-las/get` (contenu complet, Tables A/B, avenants A2/B2, signatures,
    changes-proposal), `omobility-las/update` (approve/comment du partenaire),
    `omobility-las/stats`. Cloisonnement : seul le HEI d'accueil authentifié peut
    récupérer un contrat, pour protéger les données personnelles de l'étudiant.
    Garde d'édition concurrente : une proposition périmée renvoie un conflit (409).
    Notification de changement : omobility-la-cnr v1 — entrant, `fetchOla` récupère la
    version fraîche et fusionne signatures + état de validation (AROUNDLINK-519) ;
    sortant, `sendOlaCnr` prévient le HEI d'accueil quand notre contrat change.
    Table B complétée automatiquement à la validation.

## Transcript (ToR — relevé de notes)

Envoi numérique des relevés de notes des étudiants que vous **accueillez**, vers leur
université d'origine. Voir aussi [Transcript of Records](../etablissement/documents.md).

**À quoi ça sert.** Vous transmettez le relevé officiel (cours, notes, crédits ECTS,
réussite / échec) de vos étudiants entrants, pour que leur établissement d'origine
importe les résultats et accorde la reconnaissance sans relevé papier.

**Pour qui.** <span class="al-audience">coordinateur / établissement partenaire</span>

**Comment ça marche.** L'établissement d'origine peut lister et récupérer les relevés
de ses étudiants qui ont étudié chez vous. Le relevé est transmis dans un format
européen normalisé, prêt à être importé et reconnu automatiquement.

**Cas d'usage.**
> À l'issue des examens, le logiciel du partenaire récupère le relevé de son étudiant
> et reconnaît automatiquement les crédits obtenus.

??? note "Détails internes (équipe AroundLink)"
    imobility-tors v1, imobility-tor-stats v1, imobility-tor-cnr v1. Entités :
    `TranscriptOfRecord` + `ExchangeAffectation` (AroundLink est l'établissement
    d'accueil). Endpoints entrants : `imobility-tors/index`, `imobility-tors/get`
    (relevé au format ELMO / EMREX, identité apprenant via ESI, cours notés),
    `imobility-tors/stats`. L'accès aux données requiert une authentification ; le
    cloisonnement s'appuie sur le HEI appelant. Notification de changement
    imobility-tor-cnr côté entrant (avec re-récupération `fetchTor` possible côté
    sortant). Seuls les cours notés sont émis ; les codes pays sont normalisés en ISO.

## Nominations (mobilités sortantes)

Nomination numérique des étudiants que vous envoyez à un partenaire, et réception de
sa décision. Voir aussi [affectation](../etablissement/campagnes.md).

**À quoi ça sert.** Vous transmettez chaque nomination d'étudiant sortant (identité,
domaine d'études, niveau, accord de rattachement) pour que l'université d'accueil
l'accepte ou la refuse numériquement, avec un historique tracé de la décision.

**Pour qui.** <span class="al-audience">gestionnaire RI / établissement partenaire</span>

**Comment ça marche.** L'université d'accueil peut lister et consulter les
nominations que vous lui adressez, puis les approuver ou les rejeter. La décision
revient dans AroundLink et met à jour le statut de l'étudiant, avec la trace du
signataire ou du motif de refus.

**Cas d'usage.**
> Vous nommez une étudiante à Milan ; le bureau milanais approuve via le réseau et le
> statut de l'étudiante passe à « approuvé » dans AroundLink, avec le signataire.

??? note "Détails internes (équipe AroundLink)"
    omobilities API v3, omobility-cnr v1. Entité : `ExchangeAffectation`. Endpoints
    entrants : `omobilities/index`, `omobilities/get` (contenu `student-mobility` :
    étudiant, ISCED-F accord + nominé, niveau EQF, HEI d'envoi/accueil, lien IIA, type
    d'activité, statut), `omobilities/update` (approve/reject du partenaire, écrit une
    ligne d'historique avec signataire ou commentaire). Le statut suit
    `ExchangeAffectationStatus` (valeurs alignées 1:1 sur le réseau ; nomination non
    décidée = pending). Cloisonnement : le `get` ne dévoile qu'aux HEI d'accueil
    authentifiés. Notification de changement omobility-cnr côté entrant.

## Fondations techniques

**À quoi ça sert.** Sous chaque échange se trouvent les mécanismes qui garantissent
que les données arrivent au bon partenaire, intactes et de source certifiée. Ils
sont invisibles pour l'utilisateur mais indispensables à la confiance du réseau.

**Pour qui.** <span class="al-audience">admin</span>

**Comment ça marche.** Chaque message échangé est signé et vérifié, de sorte que
chaque établissement sait avec certitude qui lui parle. Un annuaire central du réseau
permet de retrouver l'adresse et l'identité de chaque partenaire avant de lui
transmettre quoi que ce soit.

**Cas d'usage.**
> Avant d'envoyer un accord, AroundLink consulte l'annuaire pour localiser le
> partenaire et signe le message afin qu'il soit accepté comme authentique.

??? note "Détails internes (équipe AroundLink)"
    Signature HTTP EWP (authentification serveur et client) : chaque requête et
    réponse est signée, et l'identité de l'appelant est résolue en HEI ID, base du
    cloisonnement multi-locataire de tous les endpoints. Registre EWP : un miroir
    local du catalogue du réseau (établissements, APIs, versions, clés publiques)
    sert à résoudre l'URL d'un endpoint partenaire avant un appel sortant et à
    identifier l'appelant. Hub sortant `EwpClientService` : centralise les appels
    signés (récupération d'accords, d'approbations, de mobilités, de contrats
    pédagogiques, de relevés, de factsheets ; envoi de notifications de changement).
    ECHE : miroir de la liste publique de la Charte Erasmus (Erasmus Charter for
    Higher Education) utilisé comme source de recherche d'établissements. Modèle
    actuel d'une paire de clés par établissement (piste d'évolution : séparer clés
    client et serveur, ticket AROUNDLINK-537).
