# Bourse de mobilité

La bourse de mobilité gère le volet financier Erasmus+ — et celui de vos autres
financements : vos programmes de bourse, l'attribution aux étudiants, les pièces qui
conditionnent chaque versement, le circuit de paiement jusqu'au comptable, et le fichier
attendu par le Beneficiary Module de la Commission.

## Les programmes de bourse

**À quoi ça sert.** Ranger chaque financement à part : la convention Erasmus+ de l'année,
une bourse régionale, une aide de campus. Chacun a son budget, ses barèmes et ses dossiers.

**Pour qui.** <span class="al-audience">service bourse / coordinateur RI</span>

**Comment ça marche.** **Bourse** ouvre la liste de vos programmes ; **New program** en
crée un : nom, année académique, type (**Erasmus+ KA131** ou **Other (regional,
campus…)**), numéro de convention de subvention, dates de début et de fin, et statut :

| Statut | Ce qu'il permet |
|---|---|
| **Draft** | le programme se prépare |
| **Open** | il accepte des bourses |
| **Closed** | plus aucune nouvelle bourse |

Un étudiant a au plus une bourse par programme. L'année est portée par le programme : on ne
la choisit pas sur l'écran.

**Cas d'usage.**
> Le service bourse crée « Erasmus+ KA131 2026-2027 » avec le numéro de sa convention, le
> laisse en Draft le temps de saisir ses barèmes, puis l'ouvre.

## L'écran d'un programme

**À quoi ça sert.** Voir où en est l'argent et où en est chaque dossier, sur un seul écran.

**Pour qui.** <span class="al-audience">service bourse / coordinateur RI</span>

**Comment ça marche.** En tête, quatre indicateurs : **Agency allocation** (la dotation de
l'agence), **Engaged (signed GA)**, **Paid (advances + balances)** et **Docs pending**.
Si le programme est découpé en enveloppes, le tableau **Budget by category** donne pour
chacune le prévu, l'engagé, le versé et le **reste**.

La barre **Pipeline** compte les dossiers par statut et l'attente la plus ancienne ; un clic
filtre la liste. Les dossiers se lisent en **Kanban** ou en **Table** :

| Colonne | Statuts qu'elle regroupe |
|---|---|
| **Before award** | To award, Zero grant, Waiting list |
| **Contract** | Contract to generate, Contract sent, Contract signed |
| **Advance** | Advance to pay, Advance paid |
| **In mobility** | In mobility |
| **Final documents** | Final documents expected, Certificate received, Balance to pay, Balance paid |
| **Closed** | Closed |

Des encarts signalent ce qui demande un geste : les dossiers trop versés, les dossiers qui
attendent leurs pièces de fin de mobilité (**Remind** relance les étudiants), et les
documents qui ne servent plus et peuvent être supprimés.

**Cas d'usage.**
> En septembre, la responsable ouvre son programme : la barre Pipeline montre 12 dossiers
> en « Advance to pay » dont le plus ancien attend depuis 9 jours. Un clic, et ce sont eux
> que la liste affiche.

## Attribuer les bourses

**À quoi ça sert.** Créer les dossiers à partir des mobilités déjà enregistrées, et fixer
les montants sans calcul à la main.

**Pour qui.** <span class="al-audience">service bourse</span>

**Comment ça marche.**

- **Add students** propose les étudiants qui ont une affectation active vers un pays doté
  d'un barème — destination, période, type suggéré — ; ceux qui ont déjà une bourse sont
  grisés. **Add N** crée les dossiers.
- **New grant** crée un dossier à l'unité. À côté du montant, **Suggest** calcule une
  proposition et la détaille : séjour, voyage, compléments stage, inclusion et voyage
  durable, total, puis avance et solde.
- En vue **Table**, cocher des dossiers ouvre une barre de décision : un montant (ou le
  barème), puis **Award**, **Zero grant** ou **Hold** pour toute la sélection.
- **Import CSV** charge des bourses en lot, avec un aperçu qui signale chaque ligne en
  erreur ; une cellule de montant vide reçoit le montant suggéré.

**Les garde-fous du budget.** Créer une bourse, importer ou attribuer en lot refuse ce qui
dépasserait la dotation de l'année — « This grant would exceed the remaining allocation for
the year by X € » — ou l'enveloppe concernée. Sans dotation saisie, l'écran le dit au lieu
de laisser passer.

**Cas d'usage.**
> La responsable ajoute d'un coup les 48 étudiants placés pour l'année, coche ceux qui
> partent en Allemagne et clique sur **Award** avec le barème : 14 dossiers passent en
> « Contract to generate ».

## Le dossier d'une bourse

**À quoi ça sert.** Tout ce qui concerne la bourse d'un étudiant, de l'attribution au solde.

**Pour qui.** <span class="al-audience">service bourse</span>

**Comment ça marche.** Le dossier porte le détail financier, les coordonnées bancaires, les
documents et six jalons datés : **Grant Agreement signed**, **Learning Agreement signed**,
**Arrival confirmed**, **Certificate of attendance**, **Transcript of Records**, **EU Survey
received**.

Le statut se déduit de ces jalons et des versements, dans l'ordre : un dossier n'atteint
**Closed** qu'après le versement du solde et la réception des pièces finales.

**Les conditions de versement.** Chaque pièce peut, selon vos réglages, **ne rien bloquer**,
**bloquer l'avance** ou **bloquer le solde**. Le dossier nomme ce qui manque pour chaque
versement ; passer outre demande un motif. Un versement enregistré ne se réécrit plus :
pour le corriger, on recalcule la bourse.

Un dossier se **supprime** tant que rien n'a été versé ; ensuite, il s'**annule** (motif
obligatoire) et peut être **rouvert**. Son **historique** dit qui a changé quoi, et quand.

**Cas d'usage.**
> L'avance d'un étudiant reste bloquée : le dossier indique que le Learning Agreement n'est
> pas signé. Il l'est le lendemain, et l'avance devient versable.

## Les barèmes et les règles

**À quoi ça sert.** Poser une fois pour toutes les règles de calcul et de versement du
programme.

**Pour qui.** <span class="al-audience">service bourse</span>

**Comment ça marche.** **Rates** ouvre les réglages du programme : budget et enveloppes,
durée financée, taux de séjour, barème de voyage, compléments, pourcentage d'avance,
documents demandés, blocages de versement — avec ce qui s'écarte du réglage par défaut de la
Commission —, relances (premier rappel après la fin de mobilité, puis tous les N jours) et
clôture du programme.

**Cas d'usage.**
> Pour sa bourse régionale, l'école fixe l'avance à 70 % et décide que le relevé de notes
> ne bloque rien.

## Payer : demandes, approbation, comptabilité

**À quoi ça sert.** Faire passer l'argent par trois mains distinctes : qui prépare, qui
approuve, qui vire.

**Pour qui.** <span class="al-audience">service bourse · approbateur · comptable</span>

**Comment ça marche.**

1. **Préparer.** **Payments ▸ New payment request** : avance ou solde, puis les dossiers à
   payer. Ceux qui ne peuvent pas l'être disent pourquoi (bloqué, déjà dans une demande,
   dossier annulé). **Submit for approval** envoie la demande.
2. **Approuver.** La personne qui porte la fonction **Payment approval** la voit dans
   **Awaiting your approval**, puis **Approve** ou **Send back** avec un motif.
3. **Virer.** Le comptable ouvre **Payments**, une rubrique à lui sous **Institution** : les
   lots approuvés à virer, avec bénéficiaire, IBAN, BIC, référence et montant. **Mark as
   paid** enregistre le virement, **Attach receipt** joint la preuve. Il ne voit aucun
   dossier d'étudiant.

| Statut d'une demande | |
|---|---|
| **In preparation** | en cours de constitution |
| **Submitted** | en attente d'approbation |
| **Returned for correction** | renvoyée avec un motif |
| **Approved** | à virer |
| **Paid** | virée |

L'étudiant est prévenu quand un versement est enregistré, et confirme qu'il l'a reçu — ou
signale un écart, qui remonte dans **Reported by students**.

**Cas d'usage.**
> La gestionnaire prépare la demande des avances d'octobre, la directrice l'approuve, le
> comptable vire et marque payé : les 14 dossiers passent en « Advance paid ».

## Le Beneficiary Module de la Commission

**À quoi ça sert.** Produire le fichier attendu par le Beneficiary Module sans le refaire à
la main, et vérifier que les deux restent d'accord.

**Pour qui.** <span class="al-audience">service bourse</span>

**Comment ça marche.** **Erasmus & mail merge** ouvre l'écran d'export :

- **Erasmus file** — pour tout le programme ou une sélection, au gabarit exact du
  Beneficiary Module. Un contrôle passe avant : les lignes qui seraient refusées sont
  retenues, et un défaut bloquant empêche le téléchargement.
- **Mail merge file** — le fichier de publipostage des conventions ; les dossiers exportés
  passent en « Contract sent ».
- **Export history** — quel fichier, par qui, quand.

**Re-import BM file** relie vos dossiers aux identifiants d'activité du Beneficiary Module,
et **Compare with BM** montre les écarts, en lecture seule, avec **Download the
differences**. **Export**, sur l'écran du programme, ne donne que la liste affichée.

**Cas d'usage.**
> Avant le rapport intermédiaire, la responsable compare son programme au Beneficiary
> Module : deux montants diffèrent, elle les corrige et exporte le fichier Erasmus.

## Côté étudiant

L'onglet **Bourse** de son profil lui demande s'il candidate à une bourse Erasmus+
(répondre non ne le sort pas d'Erasmus+), lui montre sa bourse et lui fait confirmer chaque
versement reçu. Voir l'[espace étudiant](../etudiant/decouverte-candidature.md).
