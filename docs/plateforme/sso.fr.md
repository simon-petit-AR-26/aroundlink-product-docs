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

1. L'utilisateur saisit son adresse e-mail professionnelle.
2. AroundLink reconnaît le domaine et détermine le mode de connexion de
   l'établissement.
3. Selon la configuration, il est envoyé chez son fournisseur d'identité — où
   s'appliquent **vos** règles (mot de passe, MFA, accès conditionnel) — ou il
   saisit son mot de passe AroundLink.

Il n'y a pas de bouton d'authentification unique à chercher : l'adresse e-mail
suffit à orienter l'utilisateur.

### Les réglages, par établissement

| Réglage | Effet |
| --- | --- |
| **Activation** | Ouvre l'authentification unique pour l'établissement. |
| **Mode strict** | Supprime la connexion par mot de passe : le fournisseur d'identité devient la seule voie d'entrée. |
| **Domaines e-mail autorisés** | Liste blanche des domaines admis, en complément du contrôle d'appartenance. Obligatoire dès l'activation. |

!!! warning "Ne pas activer le mode strict en premier"
    Le mode strict retire le repli par mot de passe. Activez-le seulement après
    avoir vérifié qu'au moins un compte se connecte réellement par
    l'authentification unique.

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
