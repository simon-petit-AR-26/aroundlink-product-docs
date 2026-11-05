# Connexion Microsoft

Vos utilisateurs — personnel comme étudiants — peuvent se connecter à AroundLink avec leur
**compte Microsoft**, professionnel ou personnel, sans mot de passe supplémentaire à retenir.

**Il n'y a rien à configurer dans le cas courant.** Chacun relie
son compte lui-même, en deux clics, depuis son profil.

## Le cas courant : chacun relie son compte

**À quoi ça sert.** Se connecter d'un clic, sans mot de passe, sans démarche auprès de sa
DSI ni de nous.

**Pour qui.** <span class="al-audience">tout utilisateur d'AroundLink</span>

**Comment ça marche.** En trois temps.

1. L'utilisateur se connecte à AroundLink **avec son mot de passe**, comme d'habitude.
2. Depuis son profil, **Link my Microsoft account** relie son compte — professionnel ou
   personnel. Microsoft affiche toujours son sélecteur de comptes.
3. À partir de là, le bouton **Sign in with Microsoft** de la page de connexion le fait
   entrer directement.

**Unlink Microsoft account** délie le compte, à condition qu'il garde un autre moyen
d'entrer : un mot de passe utilisable, ou un compte Google relié. Si votre établissement
impose Microsoft, le bouton est grisé : « You need your Microsoft account to sign in. »

!!! warning "Une adresse e-mail identique ne suffit jamais"
    La connexion reconnaît **le compte Microsoft relié**, pas l'adresse qu'il porte.
    Quelqu'un qui arriverait avec un compte Microsoft ayant la même adresse e-mail qu'un de
    vos utilisateurs n'entrerait pas : il verrait « This Microsoft account is not linked to
    any AroundLink account. Sign in with your password, then link it from your profile. »

    C'est ce qui permet d'ouvrir la connexion Microsoft à tous sans rien vérifier en amont.

**Les messages que vos utilisateurs peuvent voir :**

| Message | Ce qu'il veut dire |
|---|---|
| *This Microsoft account is not linked to any AroundLink account…* | Il faut d'abord se connecter par mot de passe et relier son compte |
| *This Microsoft account is already linked to another AroundLink account.* | Le compte Microsoft ne peut servir qu'à une seule identité AroundLink |
| *This email domain is not allowed to sign in with Microsoft.* | L'adresse n'appartient à aucun des domaines autorisés de l'établissement |
| *Your Microsoft account could not be matched to your AroundLink account…* | La liaison automatique n'a pas trouvé le compte : votre administrateur doit vérifier qu'il existe |
| *This account signs in with Microsoft — there is no password to set.* | Votre établissement a supprimé la connexion par mot de passe (mode strict) |

**Cas d'usage.**
> Une coordinatrice en a assez de retenir un mot de passe de plus. Elle se connecte, ouvre
> son profil, relie son compte de l'école, et se connecte d'un clic depuis ce jour — sans
> avoir eu à demander quoi que ce soit à personne.

## Le cas du SSO imposé

**À quoi ça sert.** Relier automatiquement tous vos utilisateurs à leur compte Microsoft —
et, si vous le voulez, faire de Microsoft **le seul moyen d'entrer** : plus de mots de passe
à gérer, et les départs sont traités dans votre annuaire, pas chez nous.

**Pour qui.** <span class="al-audience">DSI</span>

**Comment ça marche.** C'est le seul cas qui demande un échange avec notre équipe. Deux
réglages distincts, que nous activons pour vous :

| Réglage | Effet |
|---|---|
| **Activation** | Vos utilisateurs n'ont rien à relier : la liaison se fait **à leur première connexion**, d'après l'identifiant de connexion de leur compte Microsoft. |
| **Mode strict** | Supprime la connexion par mot de passe : votre annuaire devient la seule voie d'entrée. |

Voir aussi [Les réglages, par établissement](sso.md#les-reglages-par-etablissement).

### Ce que nous attendons de vous

| | Quoi | Où le trouver |
|---|---|---|
| **1** | Votre **identifiant de locataire** Microsoft — ou votre nom de domaine principal | Portail Microsoft Entra ▸ Vue d'ensemble ▸ ID de locataire |
| **2** | La liste de vos **domaines e-mail** autorisés | Vous seul la connaissez |
| **3** | Si votre locataire l'exige, le **consentement administrateur** | Nous vous envoyons un lien : un administrateur de votre locataire l'accorde une fois, sur la page de Microsoft |

### Ce que nous faisons ensuite

Nous enregistrons votre configuration et l'activons. À partir de là, toute personne de votre
établissement qui arrive avec une adresse d'un domaine autorisé est reliée à son compte
AroundLink à sa première connexion.

!!! danger "Les domaines autorisés ne sont pas facultatifs"
    Une configuration activée **doit** déclarer au moins un domaine. Sans domaine, personne
    n'est relié à sa première connexion — et, combiné au mode strict qui retire le mot de
    passe, vos utilisateurs se retrouveraient enfermés dehors. La plateforme refuse donc une
    configuration activée sans domaine.

!!! warning "Les comptes doivent exister au préalable"
    L'authentification unique vérifie **qui vous êtes**. Elle ne décide pas que vous avez le
    droit d'entrer. Un utilisateur qui n'existe pas encore dans AroundLink sera refusé, même
    avec un compte Microsoft parfaitement valide. Créez ou importez vos comptes avant
    d'activer.

**Cas d'usage.**
> L'université impose son annuaire pour tous ses outils. Sa DSI nous transmet son identifiant
> de locataire et ses deux domaines. Nous activons. Les deux cents comptes déjà créés dans
> AroundLink se relient tout seuls au fil des premières connexions ; une fois les premières
> connexions vérifiées, le mode strict est activé.

## Ce que nous lisons de votre annuaire

| | |
| --- | --- |
| **Données lues** | nom, adresse e-mail, identifiant de compte Microsoft |
| **Données non demandées** | messagerie, fichiers, calendrier, annuaire, groupes, appartenances |
| **Mots de passe** | ne transitent jamais par AroundLink |
| **Application à déclarer chez vous** | aucune |
| **Portée** | personnel de l'établissement **et** étudiants |
