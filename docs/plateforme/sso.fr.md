# Authentification unique Microsoft (DSI)

!!! info "À qui s'adresse cette page"
    Cette page est **technique** : elle s'adresse aux **DSI et équipes
    d'infrastructure** qui évaluent ou mettent en place l'authentification unique
    entre leur annuaire Microsoft et AroundLink. Pour la valeur métier, voir la
    page [Vue d'ensemble](plateforme.md).

AroundLink prend en charge l'**authentification unique via Microsoft Entra ID**
(anciennement Azure AD), en **OpenID Connect**. Vos utilisateurs se connectent
avec leur compte institutionnel ; aucun mot de passe supplémentaire n'est créé,
et aucun identifiant ne transite par AroundLink.

## En résumé

| | |
| --- | --- |
| **Protocole** | OpenID Connect (*Authorization Code*, `response_mode=query`) |
| **Fournisseur d'identité** | Microsoft Entra ID / Azure AD, point de terminaison v2.0 |
| **Périmètres demandés** | `openid`, `profile`, `email` — **et rien d'autre** |
| **Données lues** | nom, adresse e-mail, identifiant d'objet Microsoft (`oid`) |
| **Données non demandées** | messagerie, fichiers, calendrier, annuaire, groupes, appartenances |
| **Enregistrement d'application à créer chez vous** | **aucun** — voir ci-dessous |
| **Mots de passe** | ne transitent jamais par AroundLink |
| **Portée** | personnel de l'établissement **et** étudiants |

!!! tip "Le point qui surprend souvent"
    Vous **n'avez pas d'application à déclarer** dans votre annuaire. AroundLink
    est enregistrée une seule fois, en application multi-locataire. Votre
    établissement l'**autorise** dans son propre annuaire, en un clic, via un lien
    que nous vous fournissons.

## Procédure de mise en place

Comptez une demi-journée, dont l'essentiel est de l'attente entre deux échanges.

### Étape 1 — Vous nous transmettez votre identifiant de locataire

C'est le *Tenant ID* de votre annuaire Microsoft : un GUID
(`11111111-2222-3333-4444-555555555555`) ou votre domaine vérifié
(`votre-universite.fr`).

Où le trouver : **portail Microsoft Entra ▸ Vue d'ensemble ▸ ID de locataire**.

!!! warning "Valeurs refusées"
    Les valeurs génériques `common`, `organizations` et `consumers` sont
    **rejetées** par la plateforme. Un locataire précis est exigé : c'est ce qui
    garantit que seuls vos utilisateurs peuvent entrer.

### Étape 2 — Vous nous indiquez vos domaines e-mail

La liste des domaines autorisés à se connecter (`votre-universite.fr`,
`etu.votre-universite.fr`…). Elle est **obligatoire** : une configuration active
sans domaine est refusée à l'enregistrement.

Cette liste est une **défense supplémentaire**, indépendante du contrôle de
locataire : même un compte du bon annuaire est refusé si son adresse ne relève
pas d'un domaine déclaré.

### Étape 3 — Nous enregistrons la configuration

L'équipe AroundLink saisit le locataire et les domaines dans l'espace
d'administration, puis lance un **test de configuration** : la plateforme
interroge le document de découverte OpenID Connect de votre locataire et
vérifie qu'il est joignable et complet. Résultat immédiat, avant toute
activation.

### Étape 4 — Votre administrateur autorise AroundLink

Nous vous envoyons un lien de **consentement administrateur** préparé pour votre
locataire. Un administrateur général de votre annuaire l'ouvre, lit les
permissions demandées (`openid`, `profile`, `email`) et accepte.

C'est la seule action requise de votre côté, et elle ne se fait **qu'une fois**.

Deux URL de redirection sont utilisées par le flux. Leurs valeurs exactes sont
affichées dans l'espace d'administration AroundLink et vous sont communiquées à
cette étape :

| Usage | Chemin |
| --- | --- |
| Retour d'authentification | `/sso/check` |
| Retour de consentement administrateur | `/sso/consent-callback` |

### Étape 5 — Les comptes doivent exister dans AroundLink

!!! danger "Prérequis à ne pas manquer"
    L'authentification unique **connecte** des comptes, elle ne les **crée pas**.
    Un utilisateur dont le compte n'existe pas encore dans AroundLink reçoit
    « votre compte Microsoft n'est pas provisionné » et ne peut pas entrer.

Les comptes sont créés en amont par l'établissement : import de la liste des
étudiants, ou création par le bureau des relations internationales. Voir
[Paramètres &amp; équipe](../etablissement/parametres.md).

À la **première** connexion, AroundLink rapproche le compte Microsoft du compte
existant **par l'adresse e-mail**, puis mémorise l'identifiant Microsoft
immuable. Les connexions suivantes s'appuient sur cet identifiant : un
changement d'adresse chez vous ne casse pas le lien.

### Étape 6 — Activation, puis éventuellement passage en mode strict

Nous activons l'authentification unique. À ce stade, les deux modes de connexion
coexistent : mot de passe **et** Microsoft.

Quand vous avez confirmé que la connexion fonctionne pour vos utilisateurs, vous
pouvez demander le **mode strict**, qui supprime la connexion par mot de passe
pour tous les comptes de l'établissement.

!!! warning "Ne pas activer le mode strict en premier"
    Le mode strict retire le repli par mot de passe. Activez-le seulement après
    avoir vérifié qu'au moins un compte se connecte réellement via Microsoft.

## Le parcours vu par l'utilisateur

1. Il ouvre AroundLink et saisit son adresse e-mail professionnelle.
2. La plateforme reconnaît le domaine et détermine si l'établissement est en
   authentification unique.
3. Il est redirigé vers la page de connexion Microsoft — celle de votre
   établissement, avec son adresse déjà pré-remplie. Il y retrouve vos propres
   règles : mot de passe, MFA, accès conditionnel.
4. Microsoft le renvoie sur AroundLink, connecté, sur la page d'accueil de son
   rôle.

Il n'y a pas de bouton « connexion SSO » à chercher : l'adresse e-mail suffit à
orienter l'utilisateur.

## Réglages par établissement

| Réglage | Effet |
| --- | --- |
| **Activation** | Ouvre la connexion Microsoft pour l'établissement. |
| **Mode strict** | Supprime la connexion par mot de passe : Microsoft devient la seule voie d'entrée. |
| **Domaines e-mail autorisés** | Liste blanche des domaines admis. Obligatoire dès l'activation. |

La date de la **dernière connexion réussie** est enregistrée, ce qui permet de
vérifier d'un coup d'œil qu'un raccordement est toujours vivant.

## Contrôles effectués à chaque connexion

Chaque authentification passe les vérifications suivantes ; l'échec de l'une
d'elles interrompt la connexion.

- **Paramètre `state`** vérifié — protège contre la falsification de requête.
- **`nonce`** à usage unique, comparé à la valeur émise à l'aller — protège
  contre le rejeu d'un jeton.
- **Locataire du jeton** (`tid`) comparé au locataire configuré — un jeton émis
  par un autre annuaire est rejeté.
- **Identifiant d'objet** (`oid`) exigé — c'est la clé stable du rapprochement.
- **Appartenance du compte** à l'établissement configuré.
- **Domaine e-mail** présent dans la liste autorisée.
- **Rapprochement initial** refusé si aucune liste de domaines n'est définie —
  l'adresse e-mail est une valeur modifiable par un administrateur de locataire,
  elle ne peut pas à elle seule lier un compte.

Un lien vers un compte Microsoft n'est enregistré **qu'après** que tous ces
contrôles ont réussi : un utilisateur refusé ne laisse aucune trace derrière lui.
Un même compte Microsoft ne peut être rattaché qu'à un seul compte AroundLink,
contrainte garantie en base.

## Cycle de vie des comptes

| Événement chez vous | Effet dans AroundLink |
| --- | --- |
| Compte Microsoft désactivé (départ) | La personne ne peut plus se connecter, immédiatement. |
| Mot de passe modifié, MFA ajouté | Rien à faire côté AroundLink : ces règles sont les vôtres. |
| Adresse e-mail modifiée | La connexion continue de fonctionner (rapprochement sur l'identifiant Microsoft, pas sur l'adresse). |
| Nouvel arrivant | Son compte AroundLink doit être créé au préalable — voir l'étape 5. |

## Limites connues

Annoncées franchement, pour éviter les mauvaises surprises en fin de projet.

- **Microsoft Entra ID uniquement.** Google Workspace, SAML 2.0, Shibboleth,
  RENATER et eduGAIN ne sont **pas** pris en charge à ce jour. Si votre
  établissement s'authentifie par l'une de ces voies, parlons-en : ce n'est pas
  disponible aujourd'hui.
- **Pas de provisionnement automatique.** Aucune synchronisation d'annuaire ni
  SCIM. Les comptes sont créés par import ou par le bureau des relations
  internationales.
- **Pas de synchronisation des groupes ni des rôles.** Les droits AroundLink sont
  attribués dans AroundLink — voir [Paramètres &amp; équipe](../etablissement/parametres.md).
- **Comptes d'administration AroundLink exclus.** Les comptes internes de
  l'éditeur ne passent pas par l'authentification unique d'un client, par
  construction.

## Questions fréquentes

**Devons-nous créer un enregistrement d'application ?**
Non. Vous autorisez la nôtre, en un clic.

**Quelles permissions accordons-nous exactement ?**
`openid`, `profile`, `email`. Aucun accès à la messagerie, aux fichiers, au
calendrier ou à l'annuaire.

**AroundLink voit-elle nos mots de passe ?**
Jamais. L'authentification a lieu chez Microsoft ; nous recevons uniquement un
jeton d'identité signé.

**Notre MFA et notre accès conditionnel s'appliquent-ils ?**
Oui, intégralement. La connexion se déroule sur vos pages Microsoft, sous vos
règles.

**Un compte d'un autre établissement peut-il entrer ?**
Non. Deux barrières indépendantes : le locataire d'émission du jeton et la liste
des domaines e-mail autorisés.

**Peut-on revenir en arrière ?**
Oui. La désactivation rétablit la connexion par mot de passe.

**Peut-on tester avant d'ouvrir à tout le monde ?**
Oui. Le test de configuration valide le raccordement sans rien activer, et
l'activation sans mode strict laisse le mot de passe en repli le temps de la
vérification.

---

Voir aussi : [Sécurité &amp; données](securite.md) ·
[Vue d'ensemble de la plateforme](plateforme.md)
