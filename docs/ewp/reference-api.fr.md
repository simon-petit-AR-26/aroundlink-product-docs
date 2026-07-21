# Référence des API EWP (DSI / intégrateurs)

!!! info "À qui s'adresse cette page"
    Cette page est **technique** : elle s'adresse aux **DSI, équipes d'intégration
    et partenaires** qui connectent leur système à AroundLink via le réseau EWP.
    Pour comprendre la valeur métier de chaque brique, voir la page
    [Vue d'ensemble](ewp.md).

AroundLink implémente les API du réseau **EWP (Erasmus Without Paper)** pour échanger
accords, contrats pédagogiques, relevés de notes et nominations avec les
universités partenaires, sans intervention manuelle.

## Principes

- **Toutes les API entrantes** (un partenaire nous appelle) sont exposées sous
  `‌/ewp/{hei-id}/…`, où `{hei-id}` est l'identifiant HEI de l'établissement client
  AroundLink concerné.
- **Deux sens** :
    - *Entrant* — le système du partenaire (ou le Registre EWP) appelle AroundLink.
    - *Sortant* — AroundLink appelle le partenaire (récupération / notification).
- **Authentification** — les échanges sont signés (HTTP Signature, mécanisme
  standard EWP côté client et serveur). L'appelant est identifié par sa clé
  publique déclarée au Registre EWP ; c'est cette identité qui **cloisonne** les
  données (un partenaire ne voit que les objets qui le concernent).
- **Découverte** — un partenaire trouve l'établissement et ses services via le
  **manifeste** ; il peut vérifier la connectivité et l'authentification via
  **Echo** avant tout échange réel.
- **CNR** (*Change Notification Receiver*) — notifications légères « telle donnée a
  changé, viens la re-chercher » ; elles maintiennent les deux copies synchronisées.

## Comment tester la connexion

Un appel **signé** vers `‌/ewp/{hei-id}/echo` renvoie les paramètres transmis et
l'identité HEI **authentifiée** de l'appelant. Un `200` avec le bon HEI confirme que
le lien et la signature fonctionnent — l'étape à faire en premier lors d'un
raccordement.

## Endpoints entrants (partenaire → AroundLink)

Chemins relatifs à `‌/ewp/{hei-id}`.

### Découverte & diagnostic

| Endpoint | Méthode | API (version) | Rôle |
| --- | --- | --- | --- |
| `/manifest.xml` | GET | Discovery v6 | Manifeste : liste les API implémentées, leurs URL et versions, le contact et les clés publiques de signature. Point d'entrée de tout raccordement. |
| `/echo` | GET · POST | Echo v2 | Test de connectivité + d'authentification ; renvoie l'appelant authentifié. |
| `/institutions` | GET · POST | Institutions v2 | Résout un ou plusieurs identifiants HEI en nom d'établissement (jusqu'à 10). |
| `/factsheet` | GET · POST | Factsheet v1.2 | Sert la fiche pratique de l'établissement (dates limites, contacts logement/visa, délais). |

### IIA — accords inter-établissements

| Endpoint | Méthode | API (version) | Rôle |
| --- | --- | --- | --- |
| `/iias/index` | GET · POST | IIAs v7 | Liste les identifiants d'accords partagés avec l'appelant (filtres : partenaire, année, modifiés depuis). |
| `/iias/get` | GET · POST | IIAs v7 | Contenu complet d'un ou plusieurs accords (jusqu'à 100), avec le hash de version. |
| `/iias/approval` | GET · POST | iias-approval v2 | Notre approbation (id + hash de la version approuvée) pour les accords de l'appelant. |
| `/iias/stats` | GET | IIAs v7 | Statistiques d'approbation (récupérables, approuvés d'un côté / des deux…). |
| `/iia-cnr` | POST | iia-cnr v3 | Notification : un accord a changé chez le partenaire → nous le re-récupérons pour revue. |
| `/iia-approval-cnr` | POST | iia-approval-cnr v2 | Notification : le partenaire a approuvé → nous re-récupérons son approbation. |

### OLA — contrats pédagogiques (mobilités sortantes)

| Endpoint | Méthode | API (version) | Rôle |
| --- | --- | --- | --- |
| `/omobility-las/index` | GET · POST | omobility-las v1.2 | Liste les contrats pédagogiques de nos étudiants sortants pour l'établissement d'accueil appelant. |
| `/omobility-las/get` | GET · POST | omobility-las v1.2 | Contenu complet d'un contrat (cours, signatures, propositions de changement). Réservé à l'établissement d'accueil. |
| `/omobility-las/update` | POST | omobility-las v1.2 | L'établissement d'accueil approuve ou demande des modifications (signature / commentaire). |
| `/omobility-las/stats` | GET | omobility-las v1.2 | Compteurs par année (approuvés / rejetés / en attente). |
| `/omobility-la-cnr` | POST | omobility-la-cnr v1 | Notification : un contrat a changé côté partenaire → re-récupération. |

### ToR — relevés de notes (mobilités entrantes)

| Endpoint | Méthode | API (version) | Rôle |
| --- | --- | --- | --- |
| `/imobility-tors/index` | GET · POST | imobility-tors v1 | Liste les relevés des étudiants entrants pour l'établissement d'origine appelant. |
| `/imobility-tors/get` | GET · POST | imobility-tors v1 | Relevé officiel au format **ELMO** (cours, notes, ECTS). Réservé à l'établissement d'origine. |
| `/imobility-tors/stats` | GET | imobility-tor-stats v1 | Compteurs de relevés par année. |
| `/imobility-tor-cnr` | POST | imobility-tor-cnr v1 | Notification : un relevé a changé → re-récupération. |

### Nominations (mobilités sortantes)

| Endpoint | Méthode | API (version) | Rôle |
| --- | --- | --- | --- |
| `/omobilities/index` | GET · POST | omobilities v3 | Liste les nominations d'étudiants que nous envoyons à l'établissement d'accueil appelant. |
| `/omobilities/get` | GET · POST | omobilities v3 | Détail d'une nomination (identité étudiant, champ ISCED-F, niveau EQF, accord lié, statut). Réservé à l'accueil. |
| `/omobilities/update` | POST | omobilities v3 | L'établissement d'accueil accepte ou refuse la nomination ; la décision revient dans AroundLink. |
| `/omobility-cnr` | POST | omobility-cnr v1 | Notification : une nomination a changé → re-récupération. |

## Appels sortants (AroundLink → partenaire)

Déclenchés automatiquement par AroundLink (à l'édition d'un objet, ou à réception
d'une CNR). Ils utilisent l'URL du service du partenaire, résolue via le Registre
EWP, et sont signés avec nos identifiants.

| Action | Déclenchement | Effet |
| --- | --- | --- |
| Récupérer un accord (IIA) | CNN reçue / synchronisation | Récupère la version du partenaire et prépare une revue. |
| Récupérer une approbation IIA | CNR d'approbation reçue | Met à jour l'état d'approbation du partenaire. |
| Notifier un changement d'IIA | Édition d'un accord chez nous | Envoie une `iia-cnr` au partenaire. |
| Récupérer / notifier un OLA | Édition / CNR | Synchronise le contrat pédagogique. |
| Récupérer un relevé (ToR) | CNR reçue | Met à jour le relevé. |
| Récupérer une nomination | CNR reçue | Met à jour la nomination et sa décision. |
| Récupérer une factsheet partenaire | Action manuelle du bureau RI | Importe les dates/contacts du partenaire dans AroundLink. |

## Fondations

- **Signature HTTP (client + serveur)** — chaque requête et réponse est signée et
  vérifiée (fenêtre temporelle courte). L'empreinte de clé identifie l'appelant et
  sert au cloisonnement des données.
- **Registre EWP (miroir local)** — catalogue des établissements, API, versions et
  clés publiques du réseau ; sert à résoudre l'URL d'un partenaire avant un appel
  sortant et à identifier l'appelant d'un appel entrant.
- **Liste ECHE (miroir)** — la charte Erasmus, utilisée comme source
  d'établissements.

!!! tip "Bonnes pratiques de raccordement"
    1. Ajouter l'établissement (son HEI ID) côté partenaire. 2. Lire le
    `manifest.xml` pour découvrir les services et clés. 3. Valider la liaison avec
    `echo` **signé**. 4. Passer aux échanges réels (IIA, OLA, ToR, nominations).

## Références externes

### API REST AroundLink

Au-delà d'EWP, AroundLink expose sa propre **API REST** (API Platform / Hydra) pour
ses ressources métier (accords, étudiants, contrats pédagogiques, relevés…). Sa
documentation **interactive** — contrat, ressources et schémas, toujours à jour —
est générée automatiquement :

- :material-api: [Documentation de l'API AroundLink (instance de démo)](https://demo.aroundlink.com/api/docs)

### Spécifications officielles EWP

La documentation généraliste et les spécifications du réseau EWP sont **publiques**
et maintenues par le consortium — utile pour un DSI qui veut le détail des schémas :

- :octicons-book-24: [Guide développeurs EWP](https://developers.erasmuswithoutpaper.eu/)
- :octicons-mark-github-16: [Organisation GitHub — toutes les spécifications](https://github.com/erasmus-without-paper)
- :octicons-shield-24: [Architecture & sécurité](https://github.com/erasmus-without-paper/ewp-specs-architecture)
- :octicons-git-branch-24: [Le processus de mobilité expliqué](https://github.com/erasmus-without-paper/ewp-specs-mobility-flowcharts)
- Spécification de chaque API dans un dépôt `ewp-specs-api-<nom>`, p. ex.
  [IIAs](https://github.com/erasmus-without-paper/ewp-specs-api-iias) ·
  [Institutions](https://github.com/erasmus-without-paper/ewp-specs-api-institutions) ·
  [Outgoing Mobilities](https://github.com/erasmus-without-paper/ewp-specs-api-omobilities)

!!! note
    Les versions d'API listées plus haut correspondent à l'implémentation actuelle
    d'AroundLink ; en cas de doute sur un schéma, **les spécifications officielles
    font foi**.
