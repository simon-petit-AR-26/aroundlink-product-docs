# Architecture & technologies

!!! info "À qui s'adresse cette page"
    Page **technique**, destinée aux **équipes IT / DSI** (intégration, due
    diligence, exploitation). Elle décrit les technologies qui composent AroundLink,
    à un niveau produit — sans configuration ni secret.

## Vue d'ensemble

AroundLink est une application **web multi-établissement (SaaS)** en deux parties
**séparées** :

- une **interface** web — ce que vos utilisateurs voient à `app.aroundlink.com` ;
- une **API JSON** — le cœur applicatif, qui porte toutes les règles métier et que
  l'interface interroge pour chaque écran.

L'interface ne parle à la base de données qu'à travers l'API. Les échanges du réseau
européen *Erasmus Without Paper* passent par la même API, et vos propres systèmes
peuvent l'utiliser — voir [Emails & connecteurs](../etablissement/emails.md).

## L'interface (front)

| Technologie | Rôle |
| --- | --- |
| **Next.js 16** / **React 19** | Application web, en **TypeScript**. |
| **Tailwind CSS** | Mise en forme, système de design maison. |
| **TanStack Query** | Échanges avec l'API, mise en cache des données affichées. |
| **Recharts** | Graphiques des tableaux de bord et des statistiques. |
| **Leaflet** | Cartes des partenaires et de l'[Atlas](../atlas/atlas.md). |

Les tableaux, filtres et vues enregistrées sont développés en interne, sans
bibliothèque de grille tierce.

## Le cœur applicatif (back)

| Technologie | Rôle |
| --- | --- |
| **PHP 8.3+** / **Symfony 7** | Cœur applicatif : sécurité, règles métier, validation. |
| **API Platform** | Exposition et documentation de l'API. |
| **Doctrine ORM** | Accès aux données et migrations de schéma. |
| **Symfony Messenger** | Traitements **asynchrones** (e-mails, notifications, synchronisations EWP). |
| **JWT** | Authentification de l'interface auprès de l'API : sans état, sans session côté serveur. |

## Base de données

- **PostgreSQL 16**. Le schéma est versionné par des **migrations**, reproductibles
  d'un environnement à l'autre.
- Les identifiants publics des objets sensibles sont des **UUID** — non devinables,
  non énumérables — plutôt que des entiers séquentiels.

## Documents et e-mails

Les **e-mails** et les **documents PDF** (attestations, contrats pédagogiques, relevés,
modèles) sont produits côté serveur, à partir de gabarits. C'est là, et seulement là,
que le moteur de gabarits **Twig** sert encore : l'ancienne interface qu'il rendait
est éteinte en production.

## Intégrations & services

| Service | Usage |
| --- | --- |
| **Mailjet** | Envoi des e-mails. |
| **Gotenberg** / **mPDF** | Génération des documents PDF. |
| **Sentry** | Supervision des erreurs, côté interface comme côté API. |
| **Registre EWP** | Miroir du catalogue du réseau EWP (établissements, clés, versions d'API). |
| **Registre ROR** | Identité de référence des établissements de l'[Atlas](../atlas/atlas.md). |

## Exécution & déploiement

- **FrankenPHP** (serveur applicatif basé sur Caddy) en **mode worker** : le cœur
  reste chargé en mémoire entre les requêtes.
- Images **Docker** ; au démarrage, l'application attend la base puis applique les
  migrations.
- La **production est hébergée en France, chez OVHcloud**.
- Fonctionne **derrière un proxy HTTPS**.

## Traitements asynchrones

Ce qui ne doit pas faire attendre l'utilisateur — envoi d'e-mails, notifications,
synchronisations EWP, relances programmées, fermeture des campagnes à l'heure dite —
passe par **Symfony Messenger** et des tâches planifiées, traitées en arrière-plan.

## API

- **L'API AroundLink** est documentée au format **OpenAPI**, consultable en ligne :
  [api.aroundlink.com/apis/docs](https://api.aroundlink.com/apis/docs).
- **L'API EWP** (réseau *Erasmus Without Paper*) — points d'accès, sens et versions
  dans la [Référence des API](../ewp/reference-api.md).
