# Connexion Microsoft

Vos utilisateurs — personnel comme étudiants — peuvent se connecter à AroundLink avec leur
**compte Microsoft**, professionnel ou personnel, sans mot de passe supplémentaire à retenir.

Depuis septembre 2026, **il n'y a plus rien à configurer dans le cas courant**. Chacun relie
son compte lui-même, en deux clics, depuis son profil.

## Le cas courant : chacun relie son compte

**À quoi ça sert.** Se connecter d'un clic, sans mot de passe, sans démarche auprès de sa
DSI ni de nous.

**Pour qui.** <span class="al-audience">tout utilisateur d'AroundLink</span>

**Comment ça marche.** En trois temps.

1. L'utilisateur se connecte à AroundLink **avec son mot de passe**, comme d'habitude.
2. Depuis son profil, il relie son compte Microsoft — professionnel ou personnel.
3. À partir de là, le bouton **« Se connecter avec Microsoft »** de la page d'accueil le fait
   entrer directement.

Il peut délier son compte quand il veut, et retrouver sa connexion par mot de passe.

!!! warning "Une adresse e-mail identique ne suffit jamais"
    La connexion reconnaît **le compte Microsoft relié**, pas l'adresse qu'il porte.
    Quelqu'un qui arriverait avec un compte Microsoft ayant la même adresse e-mail qu'un de
    vos utilisateurs n'entrerait pas : il verrait *« Ce compte Microsoft n'est relié à aucun
    compte AroundLink. Connectez-vous avec votre mot de passe, puis reliez-le depuis votre
    profil. »*

    C'est ce qui permet d'ouvrir la connexion Microsoft à tous sans rien vérifier en amont.

**Les messages que vos utilisateurs peuvent voir :**

| Message | Ce qu'il veut dire |
|---|---|
| *Ce compte Microsoft n'est relié à aucun compte AroundLink* | Il faut d'abord se connecter par mot de passe et relier son compte |
| *Ce compte Microsoft est déjà relié à un autre compte AroundLink* | Le compte Microsoft ne peut servir qu'à une seule identité AroundLink |
| *Ce compte se connecte avec Microsoft — il n'y a pas de mot de passe à définir* | Le compte a été créé en SSO imposé, sans mot de passe |

**Cas d'usage.**
> Une coordinatrice en a assez de retenir un mot de passe de plus. Elle se connecte, ouvre
> son profil, relie son compte de l'école, et se connecte d'un clic depuis ce jour — sans
> avoir eu à demander quoi que ce soit à personne.

## Le cas du SSO imposé

**À quoi ça sert.** Faire de la connexion Microsoft **le seul moyen d'entrer** pour votre
établissement — plus de mots de passe à gérer, et les départs sont traités dans votre
annuaire, pas chez nous.

**Pour qui.** <span class="al-audience">DSI</span>

**Comment ça marche.** C'est le seul cas qui demande un échange avec notre équipe. Vos
utilisateurs n'ont alors rien à relier : la liaison se fait **à leur première connexion**,
automatiquement, à partir de leur adresse e-mail.

### Ce que nous attendons de vous

| | Quoi | Où le trouver |
|---|---|---|
| **1** | Votre **identifiant de locataire** Microsoft | Portail Microsoft Entra ▸ Vue d'ensemble ▸ ID de locataire |
| **2** | La liste de vos **domaines e-mail** autorisés | Vous seul la connaissez |

### Ce que nous faisons ensuite

Nous enregistrons votre configuration et l'activons. À partir de là, toute personne de votre
établissement qui arrive avec une adresse d'un domaine autorisé est reliée à son compte
AroundLink à sa première connexion.

!!! danger "Les domaines autorisés ne sont pas facultatifs"
    Une configuration activée **doit** déclarer au moins un domaine. Sans domaine, personne
    n'est relié à sa première connexion — et comme le SSO imposé retire le mot de passe, vos
    utilisateurs se retrouveraient enfermés dehors. La plateforme refuse donc une
    configuration activée sans domaine.

!!! warning "Les comptes doivent exister au préalable"
    L'authentification unique vérifie **qui vous êtes**. Elle ne décide pas que vous avez le
    droit d'entrer. Un utilisateur qui n'existe pas encore dans AroundLink sera refusé, même
    avec un compte Microsoft parfaitement valide. Créez ou importez vos comptes avant
    d'activer.

**Cas d'usage.**
> L'université impose son annuaire pour tous ses outils. Sa DSI nous transmet son identifiant
> de locataire et ses deux domaines. Nous activons. Les deux cents comptes déjà créés dans
> AroundLink se relient tout seuls au fil des premières connexions, sans que personne ait à
> faire quoi que ce soit.

## Ce que nous lisons de votre annuaire

| | |
| --- | --- |
| **Données lues** | nom, adresse e-mail, identifiant de compte Microsoft |
| **Données non demandées** | messagerie, fichiers, calendrier, annuaire, groupes, appartenances |
| **Mots de passe** | ne transitent jamais par AroundLink |
| **Application à déclarer chez vous** | aucune |
| **Portée** | personnel de l'établissement **et** étudiants |
