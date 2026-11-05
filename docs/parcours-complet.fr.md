# Une mobilité de bout en bout

Cette page suit **une mobilité entière**, du premier réglage au relevé de notes, en disant à
chaque étape **qui agit** et **ce qui déclenche la suivante**.

Le reste de la documentation décrit les écrans un par un. Celle-ci décrit l'enchaînement —
c'est souvent ce qui manque quand on cherche pourquoi un dossier n'avance pas.

## Avant toute campagne : le terrain

Rien de ce qui suit ne fonctionne si ces quatre choses n'existent pas.

| Ce qu'il faut | Qui le prépare | Sans quoi |
|---|---|---|
| **Vos partenaires** et leurs **accords** | Coordinateur | Aucune destination à proposer |
| **Des places** posées dans la matrice | Coordinateur | Les destinations existent mais n'ouvrent rien |
| **Vos libellés de niveau** (*Custom label* : un par promotion, ou un par niveau), **portés par chaque étudiant** | Administrateur, dans **Paramètres ▸ Academic levels** | Le tour d'affectation refuse de démarrer |
| **Vos périodes** de mobilité | Administrateur | Les places n'ont pas de colonne où se poser |

!!! tip "L'erreur de démarrage la plus fréquente"
    Créer une campagne avant d'avoir posé des places. La campagne s'ouvre, les étudiants la
    voient, et ne trouvent aucune destination. Vérifiez la matrice avant d'ouvrir.

## 1. La campagne s'ouvre

**Qui agit :** le coordinateur.

Il crée la campagne, choisit **qui participe** et **où l'on peut partir**, règle le nombre de
vœux, les documents requis et les quelques options qui ne se reprennent pas ensuite. Voir
[Paramétrer une campagne, réglage par réglage](etablissement/campagnes.md).

La campagne passe de **Brouillon** à **Prête**, puis à **Ouverte**. Une campagne **Prête**
s'ouvre d'elle-même à son heure d'ouverture, et les étudiants sont alors invités ; une
campagne restée en **Brouillon** ne s'ouvre jamais seule.

**Ce qui déclenche la suite :** seul l'état **Ouverte** accepte des vœux. Une campagne
« Prête » est déjà visible des étudiants, mais elle ne se remplit pas.

## 2. L'étudiant dépose ses vœux

**Qui agit :** l'étudiant.

Il découvre les destinations, en met de côté en favori, et les verse dans ses vœux, qu'il
classe par ordre de préférence. Il ne voit que les destinations où une place est planifiée
pour lui. Tant que la campagne est ouverte, il peut revenir sur sa liste.

Si vous avez posé un **minimum de vœux**, sa liste ne s'enregistre pas tant qu'il ne l'a pas
atteint. Si vous avez activé la réponse « je ne souhaite pas partir », il peut aussi la
donner — sans avoir à se justifier.

**Ce qui déclenche la suite :** la clôture de la campagne, à son heure de fin ou par vous.
Ses vœux sont alors figés.

## 3. L'affectation

**Qui agit :** le coordinateur.

Deux chemins, qui coexistent.

**Le tour automatique** (**Match all students**) sert les étudiants dans l'ordre du
classement : le premier classé obtient son meilleur vœu disponible, et ce qui reste va au
suivant. Il exige de chaque participant un profil, un libellé de niveau et un classement
importé — voir [Ce que le matchmaking exige](etablissement/campagnes.md). Il peut être
relancé autant de fois que nécessaire. Il produit des **propositions du système**, que vous
confirmez une à une.

**L'affectation à la main** vous laisse placer qui vous voulez, où vous voulez, classé ou
non — avec trois limites : une période est obligatoire, un étudiant déjà nominé ne se
réaffecte pas, et si la campagne exige un dossier complet, elle l'exige aussi à la main.

**Ce qui déclenche la suite :** **Send proposals** envoie aux étudiants les propositions
confirmées.

## 4. L'étudiant accepte — ou pas

**Qui agit :** l'étudiant, sauf si vous avez choisi l'affectation directe.

Il reçoit sa proposition, l'accepte ou la refuse ; un e-mail confirme sa réponse. Refuser
clôt aussi ses autres vœux de la campagne. Si vous avez réglé la campagne sur
**affectation directe**, cette étape disparaît : l'envoi crée l'affectation.

**Ce qui déclenche la suite :** l'acceptation.

## 5. La nomination chez le partenaire

**Qui agit :** le coordinateur, puis l'établissement d'accueil.

Vous nominez l'étudiant auprès de sa destination ; il faut pour cela un contact chez le
partenaire. Le partenaire répond par la plateforme ou par le réseau EWP, et sa réponse
s'enregistre d'elle-même. S'il vous confirme par e-mail ou par téléphone, **Confirm
manually** l'enregistre en précisant le canal.

Tant qu'il n'a pas répondu, vous pouvez le **relancer** (une fois par vingt-quatre heures)
ou **retirer** la nomination, ce qui rend l'étudiant disponible pour une autre destination.

Un refus s'accompagne toujours d'un motif, transmis à l'établissement qui a nommé.

**Ce qui déclenche la suite :** la confirmation du partenaire. Si un
[parcours de mobilité](etablissement/parcours.md) est branché sur la campagne, l'étudiant y
entre à ce moment : c'est lui qui fournit les tâches de l'étape suivante.

## 6. Le dossier se remplit

**Qui agit :** l'étudiant dépose, le coordinateur valide.

Documents contractuels, scores de langue, contrat pédagogique. Chaque pièce attendue est
listée, et l'étudiant voit ce qui lui manque. Vous relancez ceux qui traînent depuis la
barre de sélection de votre liste, sans tenir de liste à part.

Un dossier incomplet compte dès l'affectation (étape 3) : selon le réglage de la campagne,
il la **bloque** ou se contente d'être **signalé**.

**Ce qui déclenche la suite :** le dossier est complet, et les dates approchent.

## 7. Le départ, puis le séjour

**Qui agit :** tout le monde, peu à la fois.

L'étudiant part. Son contrat pédagogique peut être modifié en cours de route — tout
changement de composant demande un motif. Les échéances de la période apparaissent dans
l'[agenda](etablissement/agenda.md), et dans le calendrier auquel chacun s'est abonné.

## 8. Le retour

**Qui agit :** l'étudiant, puis son établissement.

L'étudiant saisit la note obtenue à chaque cours de son contrat pédagogique, choisit le
système de notation et peut joindre le **relevé de notes** officiel de l'établissement
d'accueil. Son établissement le valide ou demande une correction.

L'étudiant dépose aussi son **avis** sur l'établissement d'accueil — et peut autoriser la
publication de ses photos. L'avis est modéré dans vos [validations](etablissement/validations.md)
avant d'être publié. Ceux qui n'ont pas répondu se relancent comme les documents.

**Ce qui clôt la boucle :** l'avis alimente la fiche du partenaire, que les étudiants
suivants liront avant de faire leurs vœux.
