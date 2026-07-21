# Architecture & technologies

!!! info "À qui s'adresse cette page"
    Page **technique**, destinée aux **équipes IT / DSI** (intégration, due
    diligence, exploitation). Elle décrit les technologies qui composent AroundLink,
    à un niveau produit — sans configuration ni secret.

## Vue d'ensemble

AroundLink est une application **web multi-établissement (SaaS)**, construite autour
d'un cœur **Symfony (PHP)** et d'une base **PostgreSQL**. L'application est
**API-first** : les mêmes données métier sont exposées via une API REST (voir la
[Référence des API EWP](../ewp/reference-api.md) et l'API REST AroundLink), ce qui
permet aussi bien l'interface web intégrée que des interfaces découplées (front
React/Next.js) et les échanges machine-à-machine du réseau EWP.

## Cœur applicatif (backend)

| Technologie | Version | Rôle |
| --- | --- | --- |
| PHP | ≥ 8.3 | Langage du backend. |
| Symfony | 7.2 | Framework applicatif (HTTP, sécurité, formulaires, validation…). |
| API Platform | 4.1 | Exposition de l'API REST (contrat Hydra / JSON-LD, opérations CRUD). |
| Doctrine ORM / DBAL | 3.x | Accès aux données, migrations de schéma, jeux de données. |
| Symfony Messenger | 7.2 | Traitements **asynchrones** (e-mails, notifications, synchronisations EWP). |
| Symfony UX (Stimulus) | 2.x | Interactivité côté navigateur sans build lourd (AssetMapper / importmap). |
| Twig | 3.x | Gabarits des pages de l'interface intégrée. |

## Base de données

- **PostgreSQL 16**. Le schéma est versionné par des **migrations Doctrine**
  (reproductibles d'un environnement à l'autre).
- Les identifiants publics des objets sensibles utilisent des **UUID** (non
  devinables / non énumérables) plutôt que des entiers séquentiels.

## Interface & composants front

L'interface intégrée (espaces établissement et étudiant) est rendue en **Twig +
Stimulus**, avec :

- **ag-Grid** — grilles de données (tri, colonnes, filtres, vues enregistrées) ;
- **Chart.js** — graphiques des tableaux de bord ;
- **Leaflet** (+ MarkerCluster, fond de carte MapTiler) — cartes des partenaires et
  de l'annuaire [Atlas](../atlas/atlas.md) ;
- **CKEditor** — édition de contenu riche (éditeur CMS, modèles de documents) ;
- autocomplétions et composants temps réel via **Symfony UX**.

!!! note "Séparation front / back"
    L'architecture API-first permet un **front découplé** (application React/Next.js
    consommant l'API) en parallèle de l'interface Twig existante. Les deux
    coexistent pendant la transition.

## Intégrations & services

| Service | Usage |
| --- | --- |
| **Mailjet** | Envoi des e-mails + suivi (ouvertures, clics, rebonds) des communications et relances. |
| **Gotenberg** / **mPDF** | Génération des documents PDF (attestations, contrats, modèles). |
| **MapTiler** (via Leaflet) | Fonds de carte de l'annuaire Atlas. |
| **Sentry** | Supervision des erreurs applicatives. |
| **Registre EWP** | Miroir du catalogue du réseau EWP (établissements, clés, versions d'API). |
| **spatie/simple-excel** | Lecture des imports CSV / Excel (partenaires, accords, bourses…). |

## Exécution & déploiement

- **FrankenPHP** (serveur applicatif basé sur Caddy) en **mode worker** : le noyau
  Symfony reste chargé entre les requêtes, pour de meilleures performances.
- Image **Docker** multi-étapes (build reproductible), démarrage qui attend la base
  puis applique les migrations.
- Déployable sur une infrastructure conteneurisée ; la **production est hébergée
  chez OVHcloud (Europe)**.
- Fonctionne **derrière un proxy HTTPS** (proxies de confiance configurés).

## Traitements asynchrones

Les tâches qui ne doivent pas bloquer l'utilisateur (envoi d'e-mails, notifications,
récupérations / notifications EWP, mises à jour de statut de bourse) passent par
**Symfony Messenger** et sont traitées en arrière-plan.

## API

- **API REST** (API Platform, contrat Hydra / JSON-LD) — voir la documentation
  interactive liée depuis la [Référence des API EWP](../ewp/reference-api.md).
- **API EWP** (réseau *Erasmus Without Paper*) — endpoints, sens et versions dans la
  même référence.
