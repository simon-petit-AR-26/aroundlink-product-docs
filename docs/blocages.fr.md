# Quand quelque chose ne passe pas

Les situations qu'on rencontre vraiment, avec leur cause et ce qu'il faut faire. Elles ont
presque toutes la même origine : **une condition posée en amont n'est pas remplie**, et
l'écran refuse plutôt que de deviner.

## Côté étudiant

### « Je ne vois aucune campagne »

Trois causes possibles, dans cet ordre de fréquence.

**La campagne n'est pas ouverte.** Seul l'état **Ouverte** accepte des vœux. Une campagne
« Prête » est visible de vous, pas de vos étudiants.

**L'étudiant ne fait pas partie du vivier.** Les critères de la campagne — niveau, parcours,
campus, tags, filtres — ne le retiennent pas. Ouvrez la campagne, regardez la liste des
participants : s'il n'y est pas, ajoutez-le à la main.

**L'étudiant n'a pas de profil.** Sans dossier, il n'existe pour aucune campagne.

### « Je ne peux pas valider mes vœux »

Vous avez posé un **minimum de vœux** et il ne l'a pas atteint. Le minimum bloque autant que
le maximum.

### « Je ne trouve aucune destination »

Le vivier de destinations de la campagne est vide, ou aucune place n'est posée sur les
accords qu'il retient. Vérifiez la matrice des places avant de chercher ailleurs : une
destination sans place ne s'affiche pas.

Vérifiez aussi la **période** : une place existe toujours pour une période donnée.

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

C'est le blocage le plus fréquent, et il est toujours expliqué : le compte rendu **nomme**
les étudiants qui bloquent et la raison.

| Message | Ce qu'il faut faire |
|---|---|
| L'étudiant n'a **pas de parcours** | Rattachez-le à un parcours. Si votre établissement n'en utilise pas, créez-en un par niveau. |
| L'étudiant n'a **pas de classement** | Importez le classement avant de relancer. Le tour ne le fabrique pas. |
| L'étudiant n'a **pas de profil** | Il n'a rien à placer. |
| Son **dossier est incomplet** | Complétez-le, ou réglez la campagne sur « signaler » plutôt que « bloquer ». |

!!! tip "Le tour n'est pas un geste unique"
    Corrigez ce qui bloque et relancez-le autant de fois que nécessaire.

### « Je ne peux pas supprimer cette campagne »

Seule une campagne en **brouillon** se supprime. Une campagne ouverte porte déjà des vœux.

### « Je ne peux pas rouvrir cette campagne »

Seule une campagne **terminée** se rouvre. Et si vous la rouvrez sans repousser sa date de
fin, elle se refermera dès le lendemain matin.

### « Ma campagne s'est fermée toute seule »

Sa date de fin est passée. C'est le fonctionnement normal depuis septembre 2026 : le
lendemain du dernier jour, la campagne se clôt, les vœux en brouillon deviennent des vœux et
vous recevez le bilan. Rouvrez-la et repoussez la date si c'était prématuré.

### « Mes compteurs de places ne disent pas la même chose que mon export »

Depuis septembre 2026, tous les compteurs de places ne portent plus que sur les mobilités
**sortantes** — celles que vous envoyez. Les places que vos partenaires ouvrent chez eux ne
gonflent plus vos totaux. Si un chiffre vous surprend, c'est probablement qu'il était faux
avant.

## Côté partenaire

### « Je ne peux pas relancer ce partenaire »

Une relance par vingt-quatre heures. Le bouton se grise ensuite, et il vous dira quand.

### « Je ne peux pas nominer cet étudiant sur cet accord »

Une nomination est déjà en cours sur cet accord pour lui. Retirez-la d'abord si vous voulez
la refaire.

### « Ce partenaire n'apparaît pas dans ma campagne »

Le vivier de destinations ne le retient pas : vérifiez les types d'accord, les périodes et
les filtres d'établissement de la campagne. Vérifiez aussi qu'il n'est pas archivé ou masqué.

### « Je ne peux pas refuser cette nomination »

Un refus demande un motif. Il sera transmis à l'établissement qui vous a nommé l'étudiant.

## Côté accès et permissions

### « Cet écran est en lecture seule »

Votre rôle vous donne le niveau **Consulter** sur cette section. Un bandeau le dit en haut de
l'écran. Votre écran [Mes permissions](etablissement/parametres.md) vous dit exactement ce
que vous pouvez faire et sur qui.

### « Cet étudiant est hors de mon périmètre »

Votre rôle est limité à une direction, un campus ou des promotions qui ne le couvrent pas.
Ce n'est pas une panne : c'est le périmètre défini par votre administrateur.

### « Une partie de ma sélection n'a pas été traitée »

Votre action portait sur des lignes hors de votre périmètre. Elles sont écartées, et
l'écran vous dit lesquelles.

### « Je ne peux pas me connecter avec mon compte de l'établissement »

L'authentification unique vérifie **qui vous êtes**, elle ne décide pas que vous avez le
droit d'entrer. Votre compte doit exister dans AroundLink au préalable. Voir
[Qui fournit quoi](plateforme/sso-microsoft.md).

## Côté documents

### « Je ne peux pas enregistrer ce score de langue »

Un score demande toujours une pièce justificative. Le fichier et la date sont obligatoires.

### « On me demande un motif pour modifier le contrat pédagogique »

Tout composant ajouté ou retiré après validation demande une justification. C'est une
exigence du contrat, pas un réglage.
