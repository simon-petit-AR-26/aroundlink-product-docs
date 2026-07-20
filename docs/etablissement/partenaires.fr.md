# Partenaires & fiches établissement

Le module **Partenaires** rassemble en un seul endroit tous les établissements
avec lesquels votre bureau des relations internationales travaille : où ils se
trouvent, quels accords vous lient, combien de places restent ouvertes et l'état
de leurs données officielles. Chaque partenaire dispose d'une fiche complète que
vos étudiants et votre équipe consultent tout au long de l'année.

## Annuaire des partenaires

**À quoi ça sert.** Un tableau unique et filtrable de tous vos établissements
partenaires. Il donne une vue d'ensemble immédiate — pays, ville, accréditations,
étiquettes, langues, niveaux, places restantes, nombre et type d'accords — et
sert de point d'entrée vers chaque fiche partenaire.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** L'annuaire liste les partenaires que votre établissement
suit (ceux avec qui vous avez un accord ou que vous avez créés). Vous filtrez la
liste directement depuis la barre de recherche, puis cliquez sur une ligne pour
ouvrir la fiche. Un bouton bascule le même tableau vers la vue consolidée des
accords.

**Cas d'usage.**
> Un coordinateur filtre sur « Espagne + accords actifs », puis ouvre la fiche
> d'une université pour vérifier ses contacts.

??? note "Détails internes (équipe AroundLink)"
    Contrôleur `UniversityController::universities()`. La visibilité repose sur la
    relation « suivi » (`trackedBy`) ou l'existence d'un `Exchange` avec le client.
    Les relations de la grille (factsheet, contacts, échanges) sont pré-chargées
    en lot pour éviter les requêtes N+1. Les étiquettes affichées sont uniquement
    celles de l'établissement courant. Un badge signale les mises à jour IIA en
    attente.

## Créer un établissement partenaire

**À quoi ça sert.** Enregistrer un nouveau partenaire encore absent de la
plateforme, en saisissant son identité, sa localisation, ses identifiants
officiels et au moins un contact principal. Le partenaire devient aussitôt
visible dans l'annuaire et disponible pour les accords.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Un formulaire pré-remplit une fiche contact principale
(obligatoire). À l'enregistrement, le partenaire est automatiquement rattaché à
votre établissement et ses contacts sont reliés aux comptes existants qui
correspondent. Vous êtes ensuite redirigé vers la fiche complète pour poursuivre
la saisie.

**Cas d'usage.**
> Le bureau signe un nouveau partenaire au Portugal ; le coordinateur l'ajoute
> avec son code Erasmus et le coordinateur d'accueil comme contact principal.

??? note "Détails internes (équipe AroundLink)"
    `UniversityController::newUniversity()`. Le rattachement explicite au client
    est nécessaire pour que l'établissement apparaisse dans l'annuaire. La liaison
    contact–compte s'effectue après l'enregistrement. Les doublons (code,
    identifiant EWP, e-mail de contact) sont signalés par un message.

## Fiche établissement (Informations)

**À quoi ça sert.** La carte d'identité éditable d'un partenaire : description,
accréditations, liens, étiquettes privées, code interne, logo et photo. Tout ce
que le bureau souhaite retenir sur un partenaire est centralisé ici.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Une page réunit le formulaire d'informations, l'envoi du
logo et de la photo, ainsi que le bloc des scores de langue attendus. Les champs
descriptifs sont modifiables ; les identifiants techniques officiels restent en
lecture seule. L'enregistrement ne touche qu'à vos propres étiquettes et à votre
code interne pour ce partenaire ; les données des autres établissements sur un
partenaire partagé ne sont jamais modifiées.

**Cas d'usage.**
> Le coordinateur étiquette Bologne comme « Prioritaire » et note la référence
> interne du bureau pour cet établissement.

??? note "Détails internes (équipe AroundLink)"
    `UniversityController::informationUniversity()`. Entité `University` : code,
    nom, pays, ville, adresse, e-mail, type d'école (école de commerce /
    d'ingénieurs / université), plan de mobilité (payant / gratuit),
    accréditations (22 valeurs : AACSB, EQUIS, CTI, Qualiopi…), identifiants EWP
    (HEI ID, SCHAC, code Erasmus, ROR). Logo et photo gérés via `UniversityFile`.
    Un message d'erreur s'affiche systématiquement en cas d'échec de validation.

### Étiquettes partenaires

**À quoi ça sert.** Définir vos propres libellés colorés (par exemple
« Prioritaire », « Double diplôme », « À surveiller ») et les appliquer aux
partenaires pour les regrouper et les filtrer. Les étiquettes sont privées à
l'établissement qui les crée.

**Pour qui.** <span class="al-audience">gestionnaire RI / admin</span>

**Comment ça marche.** Un écran de gestion (Paramètres ▸ Établissement) permet de
créer, modifier et supprimer des étiquettes, chacune avec un nom et une couleur.
Les étiquettes s'appliquent depuis la fiche partenaire et apparaissent en badges
et en filtres dans l'annuaire.

**Cas d'usage.**
> Le bureau crée une étiquette rouge « Suspendu » et l'applique à deux partenaires
> dont les accords ont expiré.

??? note "Détails internes (équipe AroundLink)"
    `PartnerTagsController`. Entité `PartnerTag` (propriétaire, nom, couleur,
    relation N-N vers les universités). La propriété est vérifiée à la
    modification et à la suppression.

### Code interne du partenaire

**À quoi ça sert.** Enregistrer votre propre identifiant interne pour chaque
partenaire, distinct du code officiel, afin de faire correspondre les partenaires
à vos tableurs ou outils de gestion existants.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Ce n'est pas un écran séparé : un simple champ sur la fiche
partenaire. Laissé vide, il efface le code ; renseigné, il crée ou met à jour une
référence propre à votre établissement. Il apparaît en colonne dans l'annuaire.

**Cas d'usage.**
> Le coordinateur enregistre la référence interne « IT-BOL-01 » pour Bologne.

??? note "Détails internes (équipe AroundLink)"
    Entité `PartnerInternalCode` (établissement, partenaire, code), unique par
    couple établissement/partenaire. Géré en ligne dans la fiche Informations.

### Scores de langue attendus

**À quoi ça sert.** Consigner les seuils de tests de langue qu'un partenaire
attend des étudiants entrants (par exemple IELTS 6.5, TOEFL 90, B2), sur la même
échelle que celle que les étudiants déclarent — pour comparer directement les deux
lors de la sélection.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Un bloc de gestion (ajout, modification, suppression via
une fenêtre) sur la fiche partenaire. Chaque entrée reprend la structure des
scores étudiants : type de test, note globale, les quatre sous-scores et un
niveau CECRL optionnel.

**Cas d'usage.**
> Le coordinateur note « Lund : IELTS 6.5 / B2 » ; un étudiant à IELTS 6.0 est
> alors signalé sous le seuil.

??? note "Détails internes (équipe AroundLink)"
    `UniversityLanguageScoreController`. Entité `UniversityLanguageScore`,
    structure identique à celle des scores étudiants, rattachée à l'université.

## Contacts partenaires

**À quoi ça sert.** Un annuaire des personnes avec qui le bureau échange chez
chaque partenaire, dont un contact désigné comme principal. Ces contacts
alimentent les listes déroulantes des accords et des signataires.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Deux entrées : une liste globale de vos contacts et un
onglet « Relation » par partenaire. Chaque contact possède nom, e-mail,
téléphone, fonction et un indicateur « principal ». À l'enregistrement, un contact
est automatiquement relié à un compte existant qui lui correspond.

**Cas d'usage.**
> Le coordinateur ajoute la responsable Erasmus d'un partenaire et la marque
> comme contact principal.

??? note "Détails internes (équipe AroundLink)"
    `UniversityContactController` (global) et `UniversityController::contactsUniversity()`.
    Entité `UniversityContact` (partenaire décrit, établissement propriétaire,
    indicateur principal, compte lié éventuel). Filtrage automatique par
    établissement. La suppression est protégée si le contact est référencé par un
    accord.

### Ouvrir un accès au portail (invitations)

**À quoi ça sert.** Ouvrir un accès côté partenaire pour un contact, afin qu'il
collabore directement (par exemple pour approuver un accord). En un clic, le
système invite le contact, le relie à un compte existant, ou signale un conflit.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Depuis un contact partenaire, « Ouvrir l'accès » envoie une
invitation par e-mail ; une action « Renvoyer » réémet l'invitation. Les deux
sont limitées en fréquence pour éviter les envois répétés.

**Cas d'usage.**
> Le coordinateur invite la responsable Erasmus du partenaire afin qu'elle
> examine un accord dans son propre portail.

??? note "Détails internes (équipe AroundLink)"
    `invitePartnerContact()` / `resendPartnerContactInvite()`. Flux
    créer-ou-relier-ou-inviter. Le même mécanisme se déclenche automatiquement à
    la soumission d'un accord bilatéral à un partenaire.

## Vue consolidée des accords

**À quoi ça sert.** Une vue unifiée qui fusionne les accords Erasmus (IIA) et les
accords bilatéraux de tous vos partenaires, pour voir et filtrer en un seul
endroit le statut, les années de validité, la date de signature et l'état
d'approbation de chaque accord.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Un bouton bascule l'annuaire vers cette vue normalisée, une
ligne par accord. Chaque ligne indique le partenaire, l'origine (IIA ou
bilatéral), le type, le statut (actif / inactif / résilié), l'approbation locale
et partenaire, et les années de validité.

**Cas d'usage.**
> Le bureau filtre « Tous les accords » sur « Expiré » pour planifier les
> renouvellements.

??? note "Détails internes (équipe AroundLink)"
    `UniversityController::agreementsData()`. Les lignes IIA proviennent des
    `Exchange`, les lignes bilatérales du dépôt bilatéral. Le détail des accords
    est documenté sur la page dédiée aux [accords](accords.md).

## Recherche d'établissement (autocomplétion)

**À quoi ça sert.** Accélérer la saisie en suggérant des établissements connus au
fur et à mesure de la frappe, pour rattacher partenaires et accords au bon
établissement, correctement nommé.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Un champ propose les établissements correspondant à votre
saisie ; l'autocomplétion est intégrée aux formulaires concernés.

**Cas d'usage.**
> En tapant « sorbon », la liste suggère « Sorbonne Université » avec ses
> identifiants.

??? note "Détails internes (équipe AroundLink)"
    `UniversityLookupController` + `UniversityLookupService`. Point d'accès JSON
    exposé aux formulaires.

## Contenus étudiants du partenaire

**À quoi ça sert.** Composer les informations pratiques que les étudiants voient
au sujet d'un partenaire (description et blocs de contenu classés par catégorie),
pour offrir un accompagnement cohérent et validé par le bureau.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Un éditeur avec un champ de description et l'ajout, la
modification ou la suppression de blocs de contenu classés par sous-catégorie. Un
import groupé permet aussi de charger ces contenus depuis un fichier.

**Cas d'usage.**
> Le bureau renseigne les blocs « Logement » et « Visa » d'un partenaire pour
> qu'ils apparaissent sur sa page étudiante.

??? note "Détails internes (équipe AroundLink)"
    `cmsUniversity()`, `deleteUniversityCmsBlock()`, `studentInfoImport()`. Blocs
    `UniversityCms` (sous-catégorie, contenu, position). Les catégories dépendent
    des données de référence CMS.

## Bibliothèque de documents du partenaire

**À quoi ça sert.** Conserver les fichiers rattachés à un partenaire (accords
signés, brochures…), pour regrouper tous les documents partenaires au même
endroit.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Vous envoyez des documents nommés à un partenaire (les noms
en double sont refusés), vous les listez et les supprimez individuellement.

**Cas d'usage.**
> Le coordinateur téléverse le PDF de l'accord de coopération signé sur la fiche
> du partenaire.

??? note "Détails internes (équipe AroundLink)"
    `documentsUniversity()` / `deleteDocument()`. Entité `UniversityFile` (type
    document université), gérée via le gestionnaire de fichiers.

## Catalogue de cours du partenaire

**À quoi ça sert.** Tenir la liste des cours disponibles chez un partenaire pour
l'échange, afin que les étudiants et le bureau sachent ce qui peut y être étudié.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Vous ajoutez des cours via un formulaire et vous les
supprimez par partenaire ; ils sont listés par code.

**Cas d'usage.**
> Le bureau enregistre les 12 cours de master enseignés en anglais qu'un
> partenaire propose aux entrants.

??? note "Détails internes (équipe AroundLink)"
    `courses()` / `courseDelete()`. Entité `Course` rattachée à l'université,
    listée par code via le dépôt dédié.

## Liens web & réseaux sociaux du partenaire

**À quoi ça sert.** Enregistrer le site web et les réseaux sociaux d'un partenaire,
pour que étudiants et personnel accèdent à ses canaux officiels.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Un formulaire édite le site web, Instagram, LinkedIn,
Twitter et Facebook, avec confirmation d'enregistrement et signalement clair en
cas d'erreur.

**Cas d'usage.**
> Le coordinateur ajoute l'Instagram d'un partenaire pour qu'il apparaisse sur la
> page étudiante.

??? note "Détails internes (équipe AroundLink)"
    `linksUniversity()`. Champs de liens portés par l'entité `University`.

## Modération des avis étudiants

**À quoi ça sert.** Examiner, accepter (et publier) ou refuser les avis que les
étudiants laissent sur un partenaire, en maîtrisant ce que les futurs étudiants
voient tout en gardant une trace de chaque décision.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Une vue par statut (en attente / accepté / refusé) avec
compteurs. L'acceptation peut publier l'avis (visible des étudiants) ou le garder
masqué ; le refus le masque et consigne un motif. Chaque décision enregistre une
entrée d'historique avec l'auteur.

**Cas d'usage.**
> Un coordinateur lit un avis en attente, publie les avis positifs et refuse un
> avis inapproprié en indiquant un motif.

??? note "Détails internes (équipe AroundLink)"
    `feedbackUniversity()` + actions accepter / refuser. Statuts en attente /
    accepté / refusé, indicateur de publication, historique de modération. La
    modération n'est possible que sur un partenaire que vous suivez.

## Aperçu côté étudiant

**À quoi ça sert.** Montrer au bureau exactement ce qu'un étudiant voit sur la page
d'un partenaire — places par catégorie, niveau et discipline, exigences, avis
publiés — pour vérifier la fiche avant que les étudiants s'y fient.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** L'aperçu affiche la page étudiante du partenaire, avec les
distributions de places réunies pour tous les types d'accords, filtrables par
année, niveau et discipline. Sans profil étudiant, les filtres démarrent sur
« Tous ».

**Cas d'usage.**
> Avant l'ouverture d'une campagne, le coordinateur prévisualise un partenaire
> pour confirmer l'affichage des places et des exigences.

??? note "Détails internes (équipe AroundLink)"
    `studentPreview()`. Réutilise les mêmes constructeurs que la vue étudiante
    réelle (places, exigences, tableau d'accords, carte).

## Importer des établissements partenaires

**À quoi ça sert.** Charger ou actualiser en masse de nombreux partenaires depuis
un fichier Excel, avec une vérification stricte de l'en-tête pour qu'un modèle mal
rempli n'importe pas silencieusement zéro ligne.

**Pour qui.** <span class="al-audience">gestionnaire RI / admin</span>

**Comment ça marche.** Vous téléversez le fichier ; les en-têtes sont vérifiés en
amont (colonnes manquantes ou inconnues signalées) ; les lignes sont importées et
une ligne en erreur est ignorée sans bloquer les autres. Réimporter un
établissement existant actualise ses champs renseignés. Un bilan indique les
créations, mises à jour et lignes ignorées.

**Cas d'usage.**
> Le bureau téléverse 300 partenaires : 280 créés, 20 mis à jour, une faute de
> frappe dans l'en-tête détectée avant tout enregistrement.

??? note "Détails internes (équipe AroundLink)"
    `universitiesImport()` + validation des en-têtes. `UniversityImporter`
    (compteurs créés / mis à jour / reliés / traités). Une prévisualisation est
    disponible avant confirmation. Les valeurs issues du fichier sont
    échappées à l'affichage.

## Importer des contacts partenaires

**À quoi ça sert.** Charger en masse des contacts partenaires depuis un fichier
CSV ou Excel, en les rattachant aux partenaires par domaine e-mail, avec un aperçu
avant écriture.

**Pour qui.** <span class="al-audience">gestionnaire RI / admin</span>

**Comment ça marche.** Vous téléversez le fichier, un aperçu s'affiche sans rien
écrire, puis vous confirmez. Une ligne en erreur est ignorée, les autres se
poursuivent. Le bilan indique les créations, mises à jour, lignes ignorées et les
domaines e-mail ne correspondant à aucun partenaire connu.

**Cas d'usage.**
> Le bureau téléverse une liste de contacts : chacun rejoint le bon partenaire, et
> 3 domaines inconnus sont signalés.

??? note "Détails internes (équipe AroundLink)"
    `UniversityContactsImportController`. `UniversityContactsImporter` (domaines
    introuvables, contacts créés / mis à jour). Prévisualisation avant
    confirmation.
