# Espace étudiant — Découverte & candidature

L'espace étudiant accompagne chaque étudiant depuis sa première connexion
jusqu'au dépôt de sa candidature. Il réunit un tableau de bord de suivi, la
gestion du profil, un moteur de recherche des établissements partenaires et
tout le parcours de vœux d'une campagne de mobilité. Objectif : donner à
l'étudiant une expérience claire et autonome, et alléger le travail du
gestionnaire RI.

## Tableau de bord de mobilité

**À quoi ça sert.** C'est la page d'accueil de l'étudiant. Elle montre où il en
est dans l'ensemble de son parcours de mobilité, sous forme de frise visuelle,
et met en avant la prochaine action à réaliser. L'étudiant garde une vision
d'ensemble sans avoir à comprendre les rouages administratifs.

**Pour qui.** <span class="al-audience">étudiant</span>

**Comment ça marche.** À chaque connexion, l'espace détermine automatiquement le
statut de l'étudiant et l'affiche sur une frise de onze étapes, de « Connecté »
jusqu'à « Mobilité terminée ». Chaque étape franchie est marquée comme complétée,
l'étape en cours est mise en avant et renvoie directement vers la bonne page.
Avant toute affectation, le tableau de bord suggère quelques établissements
partenaires à explorer ; une fois l'étudiant placé, il affiche l'établissement
d'accueil confirmé et une liste de contrôle des étapes de mobilité.

**Cas d'usage.**
> Un étudiant qui vient de soumettre ses vœux se connecte et voit l'étape
> « Candidature en cours » surlignée, avec un lien direct vers la campagne.

??? note "Détails internes (équipe AroundLink)"
    Le statut n'est jamais stocké : il est recalculé à chaque affichage par le
    résolveur de statut. La frise s'appuie sur les étapes de `StudentStatusEnum`
    (Connected, Campaign, Proposition, Nomination, Partner acceptation,
    Preparation, During/After mobility, Mobility finished). Les cartes
    partenaires réutilisent le même chargement d'images (photo de profil
    prioritaire sur le logo) et le même mécanisme de favoris que le moteur de
    recherche. La liste de contrôle de mobilité affiche les sous-étapes (OLA
    1/2/3, documents, attestation d'arrivée, feedback, relevé de notes, EU
    Survey).

## Profil — Informations personnelles

**À quoi ça sert.** L'étudiant y gère son identité et ses informations
académiques, réutilisées tout au long du processus de mobilité : nom, contacts,
numéro d'urgence, nationalité, informations de naissance, numéro étudiant,
niveau académique, campus et domaine d'études. Il y gère aussi sa photo de
profil.

**Pour qui.** <span class="al-audience">étudiant</span>

**Comment ça marche.** L'étudiant complète un formulaire de profil et peut
téléverser une photo (PNG ou JPG). Le champ de niveau académique s'adapte à
l'établissement : si celui-ci a configuré ses propres programmes (par exemple
« Aéro 4 »), ce sont eux qui s'affichent ; sinon, un niveau générique est
proposé. Le domaine d'études repose sur la nomenclature ISCED.

**Cas d'usage.**
> Avant son départ, un étudiant met à jour son email personnel et son numéro
> d'urgence, puis téléverse une photo d'identité.

??? note "Détails internes (équipe AroundLink)"
    Champs du formulaire : civilité, prénom/nom, numéro étudiant, INE, email,
    email personnel, téléphone, numéro d'urgence, lieu/pays/date de naissance,
    nationalité, niveau académique (avec prise en charge des programmes
    personnalisés), campus, domaine détaillé (ISCED). La suppression de la photo
    est protégée par jeton CSRF. Les variables de la page sont assemblées par le
    gestionnaire de profil étudiant.

## Profil — Documents & scores de langue

**À quoi ça sert.** C'est le coffre-fort documentaire de l'étudiant. Il y
téléverse les documents administratifs demandés et des pièces complémentaires,
et y enregistre ses scores de tests de langue (avec le certificat associé)
exigés par les établissements partenaires. Une fois validé par l'établissement,
un document est verrouillé et ne peut plus être modifié.

**Pour qui.** <span class="al-audience">étudiant</span>

**Comment ça marche.** La page liste les types de documents requis par
l'établissement et par la campagne en cours, indique ceux qui sont déjà
téléversés et propose l'ajout de documents complémentaires. Un formulaire dédié
permet d'enregistrer un score de langue accompagné de sa pièce justificative.
Les cartes d'attestation d'arrivée et de départ permettent aussi de saisir les
dates correspondantes.

**Cas d'usage.**
> Un étudiant téléverse son certificat d'anglais B2 et saisit le score, puis
> ajoute la copie de passeport demandée par la campagne.

??? note "Détails internes (équipe AroundLink)"
    Les types de fichiers requis proviennent du vérificateur de documents de
    campagne. Un document validé est verrouillé côté étudiant : verrouillage
    appliqué à la suppression et à la mise à jour des dates. Les saisies de dates
    d'arrivée/départ refusent une date future. La suppression d'un score retire
    aussi le PDF associé du stockage.

## Profil — Bourse de mobilité

**À quoi ça sert.** Vue en lecture seule des bourses de mobilité rattachées à
l'exchange de l'étudiant, pour qu'il visualise le soutien financier qui lui a
été accordé.

**Pour qui.** <span class="al-audience">étudiant</span>

**Comment ça marche.** L'onglet liste les bourses associées au profil de
l'étudiant, de la plus récente à la plus ancienne. L'étudiant consulte le
montant et l'état de sa bourse ; il n'y a pas de saisie depuis cet écran.

**Cas d'usage.**
> Un étudiant consulte le montant et le statut de sa bourse Erasmus+.

??? note "Détails internes (équipe AroundLink)"
    Écran en consultation uniquement (aucune édition côté étudiant). Les données
    proviennent des enregistrements de bourse de mobilité liés au profil.

## Profil — Avis sur l'établissement partenaire

**À quoi ça sert.** Une fois placé, l'étudiant peut déposer un avis (thème,
note, contenu, avec photos optionnelles) sur son établissement d'accueil, pour
aider les futurs étudiants. Il suit ses propres avis au fil de la modération
(En attente / Accepté / Refusé).

**Pour qui.** <span class="al-audience">étudiant</span>

**Comment ça marche.** L'espace identifie automatiquement l'établissement
d'accueil de l'étudiant ; sans affectation, le formulaire reste masqué derrière
un état vide. Au dépôt, un même thème ne peut être noté qu'une fois. L'avis part
en modération avant toute publication, et des onglets récapitulent les avis de
l'étudiant par statut.

**Cas d'usage.**
> Un étudiant de retour rédige un avis « Logement » avec deux photos de la
> résidence ; il est transmis au coordinateur pour modération.

??? note "Détails internes (équipe AroundLink)"
    L'avis est créé au statut « En attente » ; seul le coordinateur peut
    l'accepter ou le refuser. Une photo d'avis est visible par son auteur en
    toutes circonstances, par le coordinateur modérateur, et par les autres
    utilisateurs uniquement lorsque l'avis est accepté et publié. Un avis soumis
    est définitif côté étudiant.

## Rechercher un exchange (moteur de recherche partenaires)

**À quoi ça sert.** C'est le hub de découverte : l'étudiant parcourt tous les
établissements partenaires de son établissement, sur une carte et sous forme de
cartes, et affine par période, niveau d'études, domaine ISCED, type de mobilité,
langue et niveau de langue. C'est là qu'il explore ses destinations possibles.

**Pour qui.** <span class="al-audience">étudiant</span>

**Comment ça marche.** La page charge les établissements partenaires et initialise
une carte. Les filtres sont dynamiques et propres à chaque établissement : seules
les périodes, domaines, types de mobilité et langues réellement présents dans les
accords actifs sont proposés, en couvrant aussi bien les accords Erasmus (IIA)
que les accords bilatéraux, doubles diplômes et payants. Un bouton « Correspond à
mon profil » présélectionne le niveau et le domaine de l'étudiant. Le filtrage se
fait en direct, sans rechargement complet de la page.

**Cas d'usage.**
> Un étudiant de 4e année en aéronautique clique sur « Correspond à mon profil »
> et voit aussitôt les seuls partenaires offrant son niveau et son domaine pour
> un semestre d'hiver.

??? note "Détails internes (équipe AroundLink)"
    La mobilité payante est stockée dans une table dédiée ; une puce et des prix
    indicatifs apparaissent lorsque l'établissement en publie. Les facettes sont
    fusionnées à partir des accords IIA et des accords bilatéraux/DD/payants. Les
    puces de niveau utilisent les libellés personnalisés de l'établissement (Aéro
    3…) mappés vers une valeur de niveau représentative. L'endpoint
    d'autocomplétion renvoie la carte et les cartes de résultats déjà rendues.

## Fiche établissement partenaire

**À quoi ça sert.** La page complète d'un partenaire : description, documents,
carte, exigences linguistiques, avis publiés et — pièce maîtresse — un tableau
« profil d'abord » montrant les places disponibles par type d'accord (Échange /
Double diplôme / Accord payant), réparties par période, filtrées par défaut sur
le niveau et le domaine de l'étudiant.

**Pour qui.** <span class="al-audience">étudiant</span>

**Comment ça marche.** La page charge tous les accords avec ce partenaire et
présélectionne celui qui correspond au contexte de navigation venu du moteur de
recherche. Elle construit les exigences linguistiques, fusionne les
distributions de places des accords Erasmus, bilatéraux et doubles diplômes en
une seule matrice, et affiche une ligne par type d'accord. Le niveau, le domaine
et l'année restent ajustables, et le profil de l'étudiant les préremplit. Une
sous-page liste tous les avis publiés.

**Cas d'usage.**
> Un étudiant ouvre la fiche d'un partenaire, voit 3 places d'études pour
> « Aéro 5 » sur la période de printemps sous l'accord d'échange, et lit
> 4 avis publiés.

??? note "Détails internes (équipe AroundLink)"
    Les places proviennent des fournisseurs de distribution (socle, bilatéral,
    double diplôme) assemblés par le constructeur de tableau d'accords. Seuls les
    avis acceptés et publics sont affichés. Les exigences linguistiques sont
    aussi exposées par une petite API JSON (`/api/student/.../requirements`) qui
    alimente la carte d'exigences ; cet endpoint applique explicitement le rôle
    étudiant car il vit hors du pare-feu `^/student`. Un état de repli protège
    l'affichage lorsque l'étudiant n'a pas encore de profil.

## Favoris

**À quoi ça sert.** L'étudiant peut mettre en favori les établissements
partenaires qui l'intéressent, pour les retrouver rapidement au moment de
construire ses vœux.

**Pour qui.** <span class="al-audience">étudiant</span>

**Comment ça marche.** Un bouton bascule ajoute ou retire un établissement des
favoris et met à jour la liste à la volée. L'icône apparaît sur les cartes du
tableau de bord, les résultats de recherche et les fiches partenaires.

**Cas d'usage.**
> Un étudiant met en favori trois établissements pendant sa navigation, puis
> revoit sa présélection avant de construire ses vœux.

??? note "Détails internes (équipe AroundLink)"
    Les identifiants de favoris sont propagés dans le tableau de bord et le
    moteur de recherche pour l'état des cartes. Le bouton renvoie un fragment de
    liste de favoris déjà rendu.

## Vœux de campagne (candidature)

**À quoi ça sert.** C'est le cœur de la candidature. Pendant une campagne
ouverte, l'étudiant recherche les exchanges éligibles, construit une liste de
vœux ordonnée, l'enregistre en brouillon pendant qu'il rassemble ses documents,
puis la soumet définitivement. C'est ainsi qu'il postule officiellement à ses
places de mobilité.

**Pour qui.** <span class="al-audience">étudiant</span>

**Comment ça marche.** La page liste les campagnes auxquelles l'étudiant est
inscrit. En ouvrant l'une d'elles, il voit ses vœux ordonnés, une recherche
d'exchanges éligibles et les éventuels documents requis manquants.
L'enregistrement propose deux modes : brouillon (sans blocage) et soumission
définitive (qui vérifie les exigences des exchanges et la présence des documents
requis avant d'accepter).

**Cas d'usage.**
> Un étudiant classe 5 choix, téléverse le dernier relevé requis, puis soumet
> définitivement et reçoit une confirmation « Vos vœux ont été soumis ».

??? note "Détails internes (équipe AroundLink)"
    L'éligibilité et la recherche s'appuient sur la recherche d'exchanges de
    campagne. La barrière des documents requis n'est appliquée qu'en soumission
    définitive. L'enregistrement remplace puis recrée les vœux, ordonnés par
    position. Accéder à une campagne à laquelle l'étudiant n'est pas inscrit est
    refusé.

## Proposition — Accepter ou refuser

**À quoi ça sert.** Lorsque l'établissement propose une place à l'étudiant
(un vœu affecté), celui-ci voit la proposition et prend la décision engageante
de l'accepter ou de la refuser.

**Pour qui.** <span class="al-audience">étudiant</span>

**Comment ça marche.** Sur la page des vœux, la proposition affectée est mise en
avant. Accepter et refuser sont deux actions confirmées depuis une fenêtre
modale. Chaque décision vérifie que le vœu appartient bien à l'étudiant et
déclenche un email de confirmation de décision.

**Cas d'usage.**
> Un étudiant reçoit une proposition pour son 2e choix, clique sur « Accepter »
> dans la modale, et reçoit un email de confirmation.

??? note "Détails internes (équipe AroundLink)"
    Les deux actions sont protégées par jeton CSRF et irréversibles. L'email de
    décision est envoyé après validation ; un échec d'envoi n'annule pas la
    décision déjà enregistrée.
