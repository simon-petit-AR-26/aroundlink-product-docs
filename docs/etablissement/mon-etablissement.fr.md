# Mon établissement (Resource Hub)

« Mon établissement » est l'espace où le bureau des relations internationales met à
jour toutes les informations pratiques que verront ses étudiants sortants et
entrants : identité, fiche pratique, cours, liens utiles, bibliothèque de documents
et FAQ. Vous y voyez votre établissement exactement comme vos partenaires le voient,
et vous y modérez les avis étudiants publiés.

## Éditeur de contenu « Mon établissement »

**À quoi ça sert.** C'est le point unique pour tenir à jour la base de connaissances
destinée aux étudiants. Vous y gérez l'identité de l'établissement et tous les
contenus pratiques, avec une visibilité réglable par audience (entrants, sortants,
mobilité libre). Un seul endroit pour que l'information visible par les étudiants
reste juste et à jour.

**Pour qui.** <span class="al-audience">coordinateur / gestionnaire RI</span>

**Comment ça marche.** La page est organisée en trois onglets. **Information** :
les champs d'identité (code, nom, pays…), le logo et les accréditations.
**Informations étudiants** : un conteneur de six sous-onglets — fiche pratique,
cours, liens, avis, bibliothèque et FAQ — où chaque élément porte ses audiences de
visibilité. **Factsheet IIA** : votre propre factsheet EWP (synchronisation,
calendrier, coordinateurs…). Les contenus se rédigent sous forme de blocs rattachés
à des catégories et sous-catégories.

**Cas d'usage.**
> Un coordinateur ajoute un lien « Coût de la vie à Lisbonne » visible uniquement
> par les étudiants entrants, puis dépose un PDF de bienvenue dans la bibliothèque.

!!! note "Côté étudiant"
    Les documents et ressources que vous rendez visibles apparaissent dans l'espace
    « Ressources » du portail étudiant — voir la documentation du portail étudiant.

??? note "Détails internes (équipe AroundLink)"
    Préfixe d'URL conservé à `/mobility/resource-hub` (compatibilité ascendante).
    Les blocs de contenu (`UniversityCms`) sont rattachés à une `CmsSubCategory`
    puis à une `CmsCategory` (catégories semées par migration, pas par fixtures —
    un rechargement de fixtures les purge). `Faq` et `UniversityLink` portent des
    `visibilityAudiences` (incoming / outgoing / mobility_free). Contrôleur :
    `MyInstitutionController`. AROUNDLINK-380 / -402.

### Fiche pratique, cours, liens, bibliothèque et FAQ

**À quoi ça sert.** Ces sous-onglets constituent le contenu pratique que l'étudiant
consulte avant et pendant sa mobilité : présentation de l'établissement, offre de
cours, liens externes, documents téléchargeables et questions fréquentes.

**Comment ça marche.** Chaque sous-onglet propose une gestion complète (ajout,
modification, suppression) de ses éléments, avec le réglage de visibilité par
audience. La bibliothèque accepte des fichiers téléchargeables ; la FAQ se rédige
en questions-réponses.

### Factsheet IIA (EWP)

**À quoi ça sert.** L'onglet « Factsheet IIA » présente la factsheet EWP de votre
propre établissement — celle que le réseau et vos partenaires consultent : calendrier
de nomination, coordinateurs, informations de contact. Vous la gardez synchronisée
depuis cet écran.

**Comment ça marche.** L'onglet affiche votre factsheet EWP et ses informations
associées (synchronisation, calendrier, coordinateurs). C'est la contrepartie, côté
« nous », de la fiche que vous consultez chez un partenaire.

## Modération des avis étudiants

**À quoi ça sert.** Vous collectez les avis d'étudiants de retour de mobilité (note,
thème, texte libre, photos) et vous les modérez avant qu'ils n'apparaissent aux
futurs étudiants. C'est une couche d'avis de première main, fiable, pour aider au
choix de destination.

**Pour qui.** <span class="al-audience">coordinateur / gestionnaire RI</span>

**Comment ça marche.** Un avis porte une note, un thème, le nom de l'auteur, le type
de pays, un contenu et d'éventuelles photos. Depuis le sous-onglet « avis », vous
acceptez ou refusez chaque contribution ; les avis acceptés et publics remontent
ensuite vers les étudiants.

**Cas d'usage.**
> Un étudiant de retour d'Antalya laisse un avis 4 étoiles avec photos ; le
> coordinateur l'approuve, et il s'affiche sur la page Antalya pour les candidats
> de l'année suivante.

??? note "Détails internes (équipe AroundLink)"
    Entité `Feedback` (+ `FeedbackHistory`, `FeedbackPhoto`) avec `FeedbackStatusEnum`
    et un indicateur `isPublic`. Actions accept / refuse dans `MyInstitutionController`
    (sous-onglet avis). AROUNDLINK-548.
