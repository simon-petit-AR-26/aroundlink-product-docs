# Authentification unique (DSI)

!!! info "À qui s'adresse cette page"
    Cette page est **technique** : elle s'adresse aux **DSI et équipes
    d'infrastructure** qui veulent savoir comment leurs utilisateurs se
    connectent à AroundLink. Pour la valeur métier, voir la page
    [Vue d'ensemble](plateforme.md).

Les utilisateurs d'AroundLink — personnel des relations internationales comme
étudiants — peuvent se connecter avec le **compte de leur établissement**, sans
mot de passe supplémentaire à créer ni à gérer.

Le raccordement se configure **par établissement**. Chacun choisit son mode :
authentification unique seule, ou authentification unique et mot de passe en
parallèle le temps de la transition.

## Fournisseurs d'identité

| Fournisseur | État | Guide |
| --- | --- | --- |
| **Microsoft Entra ID** (Azure AD) | ✅ Disponible | [Guide de raccordement](sso-microsoft.md) |
| **Shibboleth / SAML 2.0** (RENATER, eduGAIN, SWITCHaai…) | 🗺️ Feuille de route | — |
| **Google Workspace** | 🗺️ Feuille de route | — |

!!! note "Feuille de route"
    **Microsoft Entra ID** est le fournisseur raccordable aujourd'hui. La
    fédération d'identité universitaire (Shibboleth / SAML, RENATER, eduGAIN) et
    Google Workspace figurent sur notre feuille de route, sans date annoncée à ce
    stade.

    Si votre établissement s'authentifie par l'une de ces voies, dites-le-nous :
    les demandes des établissements décident de l'ordre dans lequel nous les
    ouvrons. En attendant, la connexion par mot de passe reste disponible, avec
    réinitialisation par lien à usage unique — voir
    [Sécurité &amp; données](securite.md).

![Écran de connexion avec l'authentification unique](../assets/screenshots/connexion.png)

*L'écran de connexion tel que vos utilisateurs le voient : le mot de passe reste disponible, et le bouton du bas ouvre l'authentification par le compte de l'université. Une fois l'authentification unique imposée, seul ce bouton subsiste.*

## Ce qui vaut pour tous les fournisseurs

Les points suivants ne dépendent pas du protocole. Ils valent aujourd'hui pour
Microsoft, et vaudront pour les fournisseurs que nous ajouterons.

### Les comptes doivent exister au préalable

!!! danger "Le prérequis le plus souvent découvert trop tard"
    L'authentification unique **connecte** des comptes, elle ne les **crée pas**.
    Un utilisateur absent d'AroundLink se voit refuser l'entrée, même avec un
    compte institutionnel parfaitement valide.

Les comptes sont créés en amont par l'établissement : import de la liste des
étudiants, ou création par le bureau des relations internationales. Voir
[Paramètres &amp; équipe](../etablissement/parametres.md).

Il n'y a **aucune synchronisation d'annuaire** (pas de SCIM), et **aucune
synchronisation des groupes ni des rôles** : les droits AroundLink s'attribuent
dans AroundLink.

### Le parcours de connexion

Le bouton **« Se connecter avec Microsoft »** est présent sur la page d'accueil, pour tout
le monde et en permanence. Il n'y a rien à chercher ni à déclarer au préalable.

Ce qui se passe ensuite dépend d'une seule chose : **le compte Microsoft est-il relié à un
compte AroundLink ?**

1. **Oui** — l'utilisateur entre. Les règles de votre annuaire s'appliquent au passage
   (mot de passe, double facteur, accès conditionnel) : elles sont à vous, pas à nous.
2. **Non** — l'entrée est refusée, avec l'explication : se connecter d'abord par mot de
   passe, puis relier son compte depuis son profil.

La reconnaissance porte sur **le compte relié**, jamais sur l'adresse e-mail seule. C'est ce
qui permet d'ouvrir la connexion Microsoft à tous sans vérification préalable.

### Les réglages, par établissement

Dans le cas courant, **il n'y a aucun réglage** : chacun relie son compte lui-même. Les
réglages ci-dessous ne concernent que les établissements qui veulent **imposer**
l'authentification unique.

| Réglage | Effet |
| --- | --- |
| **Activation** | Vos utilisateurs sont reliés automatiquement à leur première connexion, d'après leur adresse. |
| **Mode strict** | Supprime la connexion par mot de passe : votre annuaire devient la seule voie d'entrée. |
| **Domaines e-mail autorisés** | Les domaines dont les adresses déclenchent cette liaison automatique. Obligatoire dès l'activation. |

!!! danger "Pourquoi les domaines sont obligatoires"
    Sans domaine déclaré, personne n'est relié à sa première connexion. Combiné au mode
    strict, qui retire le mot de passe, vos utilisateurs se retrouveraient enfermés dehors.
    La plateforme refuse donc une activation sans domaine.

!!! warning "Ne pas activer le mode strict en premier"
    Le mode strict retire le repli par mot de passe. Activez-le seulement après avoir
    vérifié qu'au moins un compte entre réellement par l'authentification unique.

### Départs et arrivées

| Événement chez vous | Effet dans AroundLink |
| --- | --- |
| Compte institutionnel désactivé (départ) | La personne ne peut plus se connecter, immédiatement. |
| Règles d'authentification modifiées (MFA, mot de passe) | Rien à faire côté AroundLink : ces règles sont les vôtres. |
| Nouvel arrivant | Son compte AroundLink doit être créé au préalable. |

### Comptes d'administration AroundLink

Les comptes internes de l'éditeur ne passent **jamais** par l'authentification
unique d'un client, par construction.

---

Voir aussi : [Microsoft Entra ID — guide de raccordement](sso-microsoft.md) ·
[Sécurité &amp; données](securite.md) ·
[Vue d'ensemble de la plateforme](plateforme.md)
