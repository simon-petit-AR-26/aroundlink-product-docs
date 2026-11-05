# Sécurité & données

!!! info "À qui s'adresse cette page"
    Page **technique**, pour les **DSI / RSSI** évaluant AroundLink. Elle décrit les
    mesures de sécurité **au niveau produit**. Elle ne contient volontairement aucun
    détail de configuration, secret ou élément exploitable. Une documentation de
    sécurité plus détaillée peut être fournie sur demande dans un cadre approprié.

## Authentification

- **Authentification unique Microsoft et Google (OpenID Connect)** — les utilisateurs
  se connectent avec leur compte institutionnel existant ; l'authentification unique
  peut être **imposée** par établissement, avec des **domaines e-mail autorisés**.
  Procédure de raccordement, permissions demandées et contrôles effectués :
  [Authentification unique (DSI)](sso.md).
- **Connexion par mot de passe** (lorsque le SSO n'est pas imposé) — mots de passe
  **hachés** (jamais stockés en clair), **minimum de 12 caractères**, **contrôle de
  robustesse** à la création, et **réinitialisation** par lien à usage unique et durée
  limitée. Un changement de mot de passe **prévient le titulaire du compte** et **ferme ses
  sessions sur tous ses appareils**.
- **Durée de session** — une session dure au plus six heures et ne passe jamais d'un
  jour sur l'autre ; elle ne s'interrompt pas pour inactivité, pour ne pas perdre une
  saisie en cours. Un compte désactivé est bloqué dès la requête suivante.
- **Limitation de débit** (*rate limiting*) sur les tentatives de connexion et de
  réinitialisation, pour freiner les attaques par force brute.

## Autorisation & cloisonnement

- **Isolation multi-établissement** — chaque requête est automatiquement restreinte
  aux données de l'établissement de l'utilisateur connecté ; un établissement ne voit
  jamais les données d'un autre.
- **Rôles & permissions (RBAC)** — quatre niveaux (aucun / consulter / préparer /
  décider) sur chaque rubrique et chaque fonction, et un périmètre par rôle,
  **appliqués côté serveur** (le masquage de menu ne suffit pas : l'accès direct est
  également bloqué). Voir la [Vue d'ensemble](plateforme.md).
- **Contrôles d'appartenance** sur les objets accessibles par identifiant, en
  complément du cloisonnement, pour empêcher l'accès à une ressource d'autrui.

## API & réseau

- **API applicative** — **clés d'API** échangées contre un **jeton JWT** signé, de
  courte durée. Une **clé d'intégration** appartient à l'établissement et n'a que les
  droits de son rôle ; une clé révoquée n'obtient plus de jeton, et celui qu'elle détenait
  expire dans l'heure.
- **Réseau EWP** — chaque échange entrant et sortant est **signé et vérifié**
  (signatures HTTP RSA, standard EWP) ; l'appelant est identifié par sa clé publique
  déclarée au Registre EWP, ce qui conditionne l'accès aux données.

## Protection des données

- **Chiffrement en transit** — l'application fonctionne derrière **HTTPS** (proxies
  de confiance configurés).
- **Identifiants non énumérables** — les objets sensibles (affectations, contrats,
  fichiers étudiants…) sont référencés par **UUID**.
- **Protection CSRF** sur les formulaires et actions sensibles.
- **Verrouillage des documents validés** — une pièce validée ne peut plus être
  altérée ou supprimée côté étudiant.
- **Minimisation** — seules les données nécessaires au processus de mobilité sont
  collectées ; les données personnelles des étudiants (identité, coordonnées, notes)
  sont manipulées dans ce seul cadre.

## Supervision & continuité

- **Supervision des erreurs** applicatives (Sentry) pour détecter et diagnostiquer
  les incidents.
- **Sauvegardes de base de données** à la demande, avec **rétention** et
  téléchargement, depuis la console d'administration.
- **Journalisation & historique** — les décisions clés (validations de documents,
  changements d'accords, décisions de nomination) conservent un historique horodaté
  avec l'auteur, gardé cinq ans et consultable par l'établissement dans **Settings ▸
  History**.

## Conformité & hébergement

- AroundLink s'inscrit dans le cadre **Erasmus+ / EWP**, le standard européen
  d'interopérabilité de la mobilité.
- La **production est hébergée en France, chez OVHcloud** — hébergeur français,
  soumis au droit français et européen. Les données personnelles des étudiants ne
  quittent pas l'Union européenne, conformément au **RGPD**.

!!! note
    Cette page est un aperçu. Pour un questionnaire de sécurité, un audit ou des
    précisions contractuelles, contactez l'équipe AroundLink.
