# Quand quelque chose ne passe pas

Les situations qu'on rencontre vraiment, avec leur cause et ce qu'il faut faire. Elles ont
presque toutes la même origine : **une condition posée en amont n'est pas remplie**, et
l'écran refuse plutôt que de deviner.

## Côté étudiant

### « Je ne vois aucune campagne »

Trois causes possibles, dans cet ordre de fréquence.

**La campagne est encore en brouillon.** Un étudiant voit une campagne **Prête**, **Ouverte**
ou **Terminée** — jamais un **Brouillon**. Seule **Ouverte** accepte des vœux.

**L'étudiant ne fait pas partie du vivier.** Les critères de la campagne — niveau, année
scolaire, libellé de niveau, campus, tags, filtres — ne le retiennent pas, ou il a déjà une
affectation. Ouvrez la campagne, regardez la liste des participants : s'il n'y est pas,
ajoutez-le à la main.

**L'étudiant n'a pas de profil.** Sans dossier, il n'existe pour aucune campagne.

### « Je ne peux pas valider mes vœux »

Vous avez posé un **minimum de vœux** et il ne l'a pas atteint : sa liste ne s'enregistre
pas. Le minimum bloque autant que le maximum. Le message qu'il reçoit dit aussi ce qui
manque pour une destination — un score de langue, un document.

### « Je ne trouve aucune destination »

L'étudiant ne voit que les destinations où une place est **planifiée pour lui** : sa ligne
de la matrice — année, niveau, libellé de niveau, semestre. Vérifiez la matrice des places
avant de chercher ailleurs.

Restent écartés aussi : les partenaires masqués ou archivés, son propre campus, et les
partenaires dont les **filtres étudiants** ne croisent pas les siens — quand l'étudiant et
le partenaire portent des filtres, ils doivent en partager au moins un.

### « Je ne vois plus mon classement »

C'est volontaire, si votre établissement a masqué le classement aux étudiants. Le réglage
est dans [Ce que vos étudiants voient](etablissement/parametres.md) — vous et votre équipe
continuez de le voir.

### « Je n'ai pas reçu mes accès »

Un accès ouvert n'est pas un accès reçu. Regardez la colonne d'état de l'accès sur votre
liste d'étudiants : elle dit s'il est parti et quand. Et la colonne **Connected** dit s'il
s'est déjà connecté — ce sont deux questions différentes.

## Côté campagne

### « Le tour d'affectation refuse de démarrer »

Le compte rendu **nomme** les étudiants qui bloquent et la raison. Trois raisons empêchent
le départ :

| Message | Ce qu'il faut faire |
|---|---|
| **no student record** — pas de profil | Il n'a rien à placer. |
| **no level track** — pas de libellé de niveau | Rattachez-le à un libellé de niveau (*Custom level*). Si votre établissement n'en utilise pas, créez-en un par niveau. |
| **no imported class rank** — pas de classement | Importez le classement avant de relancer. Le tour ne le fabrique pas. |

Un **dossier incomplet** n'empêche pas le départ. Si la campagne est réglée sur **Block the
assignment until everything is in hand**, l'étudiant est mis de côté et nommé dans le compte
rendu ; avec **Show it, assign anyway (recommended)**, il est placé et signalé. Les
étudiants qui ont répondu « je ne souhaite pas partir » ne bloquent jamais.

!!! tip "Le tour n'est pas un geste unique"
    Corrigez ce qui bloque et relancez-le autant de fois que nécessaire.

### « Je ne peux pas supprimer cette campagne »

Seule une campagne en **brouillon** se supprime. Une campagne ouverte porte déjà des vœux.

### « Je ne peux pas rouvrir cette campagne »

Seule une campagne **terminée** se rouvre. Rouverte après son heure de fin, elle **reste
ouverte** jusqu'à ce que vous la clôturiez : la clôture automatique ne la referme pas.

### « Ma campagne s'est fermée toute seule »

Son heure de fin est passée : la campagne se clôt à la minute fixée, les vœux sont figés et
vous recevez le bilan. Rouvrez-la si c'était prématuré.

### « Mes compteurs de places ne disent pas la même chose que mon export »

Les compteurs de places portent sur les mobilités **sortantes** — celles que vous envoyez.
Les places que vos partenaires ouvrent chez eux ne gonflent pas vos totaux ; l'accord les
montre à part, dans une jauge des entrants.

## Côté partenaire

### « Je ne peux pas relancer ce partenaire »

Une relance par vingt-quatre heures. Le bouton se grise ensuite, et son infobulle donne la
date de la dernière relance.

### « Je ne peux pas nominer cet étudiant sur cet accord »

Deux causes. **Aucun contact chez ce partenaire** : « No contact for this partner — add one
to be able to nominate. » Ajoutez un contact sur sa fiche. **L'étudiant est déjà nominé** :
seule une affectation pas encore nominée se nomine. Pour recommencer, retirez la nomination,
puis réaffectez-le.

### « Ce partenaire n'apparaît pas dans ma campagne »

Le vivier de destinations ne le retient pas : vérifiez les types d'accord, les périodes, le
niveau, l'année scolaire, le type de mobilité et les filtres d'établissement de la campagne,
et que l'accord est actif. Vérifiez aussi qu'il n'est pas archivé ou masqué.

### « Je ne peux pas refuser cette nomination »

Un refus demande un motif. Il sera transmis à l'établissement qui vous a nommé l'étudiant.

## Côté accès et permissions

### « Cet écran est en lecture seule »

Votre rôle vous donne le niveau **Consulter** sur cette section. Un bandeau le dit en haut de
l'écran. Votre écran [Mes permissions](etablissement/parametres.md) vous dit exactement ce
que vous pouvez faire et sur qui.

### « Cet étudiant est hors de mon périmètre »

Votre rôle est limité à un domaine métier, une direction, un campus ou des promotions qui ne
le couvrent pas. Ce n'est pas une panne : c'est le périmètre défini par votre administrateur.

### « Une partie de ma sélection n'a pas été traitée »

Votre action portait sur des lignes hors de votre périmètre. Elles sont écartées, et l'écran
indique combien.

### « Je ne peux pas me connecter avec mon compte de l'établissement »

L'authentification unique vérifie **qui vous êtes**, elle ne décide pas que vous avez le
droit d'entrer. Votre compte doit exister dans AroundLink au préalable. Voir
[Qui fournit quoi](plateforme/sso-microsoft.md).

## Côté documents

### « Je ne peux pas enregistrer ce score de langue »

Un score demande toujours une pièce justificative. Quand l'étudiant le saisit lui-même, la
date du test est aussi obligatoire.

### « On me demande un motif pour modifier le contrat pédagogique »

Tout composant ajouté ou retiré après validation demande une justification. C'est une
exigence du contrat, pas un réglage.
