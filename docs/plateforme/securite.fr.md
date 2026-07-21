# Sécurité & données

!!! info "À qui s'adresse cette page"
    Page **technique**, pour les **DSI / RSSI** évaluant AroundLink. Elle décrit les
    mesures de sécurité **au niveau produit**. Elle ne contient volontairement aucun
    détail de configuration, secret ou élément exploitable. Une documentation de
    sécurité plus détaillée peut être fournie sur demande dans un cadre approprié.

## Authentification

- **SSO Microsoft / Azure (OpenID Connect)** — les établissements peuvent laisser
  leurs utilisateurs se connecter avec leur compte institutionnel existant ;
  l'authentification unique peut être **imposée** par établissement, avec des
  **domaines e-mail autorisés**. Voir la [Vue d'ensemble](plateforme.md).
- **Connexion par mot de passe** (lorsque le SSO n'est pas imposé) — mots de passe
  **hachés** (jamais stockés en clair), **contrôle de robustesse** à la création, et
  **réinitialisation** par lien à usage unique et durée limitée.
- **Limitation de débit** (*rate limiting*) sur les tentatives de connexion et de
  réinitialisation, pour freiner les attaques par force brute.

## Autorisation & cloisonnement

- **Isolation multi-établissement** — chaque requête est automatiquement restreinte
  aux données de l'établissement de l'utilisateur connecté ; un établissement ne voit
  jamais les données d'un autre.
- **Rôles & permissions (RBAC)** — droits par module (aucun / lecture / écriture),
  **appliqués côté serveur** (le masquage de menu ne suffit pas : l'accès direct est
  également bloqué). Voir la [Vue d'ensemble](plateforme.md).
- **Contrôles d'appartenance** sur les objets accessibles par identifiant, en
  complément du cloisonnement, pour empêcher l'accès à une ressource d'autrui.

## API & réseau

- **API applicative** — authentification par **jeton JWT** (signé par clés RSA) et
  **clés API** régénérables, sur un canal **distinct de la session navigateur**.
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
  avec l'auteur.

## Conformité & hébergement

- AroundLink s'inscrit dans le cadre **Erasmus+ / EWP**, le standard européen
  d'interopérabilité de la mobilité.
- L'application est **déployable sur une infrastructure au choix** ; la cible de
  production vise un **hébergement en Europe**, cohérent avec le **RGPD** pour les
  données personnelles des étudiants.

!!! note
    Cette page est un aperçu. Pour un questionnaire de sécurité, un audit ou des
    précisions contractuelles, contactez l'équipe AroundLink.
