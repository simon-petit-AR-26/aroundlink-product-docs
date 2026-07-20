# Accords & distribution des places

Le module Accords rassemble tout ce qu'un établissement peut proposer à ses
étudiants : échanges Erasmus+/IIA, agreements bilatéraux hors réseau, doubles
diplômes et mobilités payantes. Chaque accord porte ses places, réparties finement
par année, niveau, période et domaine, pour alimenter directement le catalogue vu
par l'étudiant.

## Offres d'échange (accords inter-établissements / IIA)

**À quoi ça sert.** C'est le catalogue de référence des mobilités qu'un étudiant peut
demander : un échange signé avec un établissement partenaire, décrivant les niveaux
d'études, les langues, les domaines (ISCED), les prérequis et le nombre de places.
La même fiche sert de dossier Erasmus+/IIA, ce qui évite de gérer deux fois la même
information.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Le coordinateur crée ou importe un échange, puis lui rattache
un ou plusieurs blocs de mobilité (études, stage, personnel), chacun précisant les
langues attendues, les domaines, les prérequis et un contingent de places. Des pages
dédiées permettent de consulter les informations, les conditions, l'état
d'approbation, l'historique, de synchroniser la factsheet EWP et de notifier le
partenaire. L'éligibilité d'un étudiant (niveau, période, GPA, scores de langue) est
vérifiée automatiquement au moment de la demande.

**Cas d'usage.**
> Le bureau RI enregistre un échange Erasmus+ avec TU Munich : 3 places de Master en
> ingénierie, anglais B2 exigé, identifiant IIA synchronisé avec le partenaire via EWP.

??? note "Détails internes (équipe AroundLink)"
    Entité `Exchange` (implémente `DistributesPlaces`). Le `agreementType`
    (`AgreementTypeEnum`, variantes Erasmus+ ou bilatérales d'échange/DD/stage) est
    mappé vers une `MobilityCategoryEnum` pour la vue étudiant. Champs EWP/IIA : iiaId,
    iiaCode, HEI ids, statuts d'approbation locale/partenaire, signataires, dates de
    signature, hash, in-effect, terminated. Blocs `MobilitySpec` (type, parties
    émettrice/réceptrice + ounit, contacts, plafond `mobilitiesPerYear`, mois/jours,
    blended) avec `MobilitySpecLanguage`, `MobilitySpecSubjectArea` (ISCED via
    DetailedLabel + clarification) et `MobilitySpecRequirement`. Éligibilité calculée
    par `Exchange::getRequirementsErrors()`.

## Distribution des places (matrice de répartition)

**À quoi ça sert.** Plutôt qu'un chiffre global, l'établissement répartit les places
négociées sur une grille précise : année universitaire, niveau d'études, période de
mobilité et domaine (ISCED). C'est cette répartition qui alimente le tableau des
places affiché à l'étudiant et qui garantit le respect du plafond annuel de chaque
accord.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Sur la page de distribution des places d'un échange, le
coordinateur remplit une matrice (année × domaine × niveau × période). Le système
contrôle le plafond annuel de chaque bloc de mobilité avant d'enregistrer, met à jour
les cellules concernées et regroupe les niveaux par cadre EQF pour que les programmes
apparentés restent ensemble. Le résultat est immédiatement visible côté étudiant.

**Cas d'usage.**
> Un partenaire accorde 4 places : le bureau en affecte 2 en Master / Semestre 1 et
> 2 en Master / Semestre 2 pour 2026/2027 ; l'étudiant voit exactement cette
> répartition sur la fiche du partenaire.

??? note "Détails internes (équipe AroundLink)"
    Stockage matriciel : `MobilitySpecPeriodPlace` (année, niveau, période, places) et
    `MobilitySpecPool` (agrégat par niveau, garde `hasSlotManagementConfigured()` à
    jour). Un compteur par période `MobilitySpecPlaces` (avec places restantes) est
    également maintenu et sert au processus d'affectation des campagnes. La sauvegarde
    envoie `period[année][isced][niveau][période]` ; le plafond `mobilitiesPerYear` de
    chaque `MobilitySpec` est vérifié avant toute écriture. Vue étudiant construite par
    `Exchange::getStudentPlacesMatrix()` et `getPlaceDistributionEntries()`. Regroupement
    par `AcademicLevel::getEqfLevel()`.

## Un moteur de places unifié

**À quoi ça sert.** Tous les types d'accords — échange, bilatéral, double diplôme,
mobilité payante — présentent leurs places à l'étudiant et à l'administration de la
même façon. Le catalogue reste cohérent quel que soit le type de contrat sous-jacent.

**Pour qui.** <span class="al-audience">admin</span>

**Comment ça marche.** Chaque type d'accord expose ses places sous une forme commune,
regroupée par catégorie de mobilité (Échange, Double diplôme, Stage, Mobilité payante)
puis par domaine, année, niveau et période. La même construction alimente la page
étudiant et l'aperçu coordinateur, qui restent ainsi toujours synchronisés.

**Cas d'usage.**
> Un partenaire propose à la fois un échange Erasmus et un double diplôme : l'étudiant
> voit deux onglets de catégorie, chacun avec sa propre grille de places.

??? note "Détails internes (équipe AroundLink)"
    Socle `App\Places` : interface `DistributesPlaces`, DTO `PlaceDistributionEntry`,
    adaptateur `AgreementPlaceDistribution`. Fournisseurs par type
    (`BilateralPlacesProvider`, `DoubleDegreePlacesProvider`, `PayingPlacesProvider`)
    agrégés par `StudentPlacesViewBuilder`. Catégorie étudiant = `MobilityCategoryEnum`
    (EXCHANGE, DOUBLE_DEGREE, INTERNSHIP, PAID_MOBILITY), distincte du type de contrat
    `AgreementTypeEnum`.

## Agreements bilatéraux

**À quoi ça sert.** Gère les partenariats hors Erasmus reposant sur une véritable
négociation entre deux établissements — l'un porteur (offre payante), l'autre partenaire
(offre gratuite) — avec leur propre distribution des places. Couvre les coopérations
en dehors du réseau EWP/Erasmus.

**Pour qui.** <span class="al-audience">gestionnaire RI / partenaire</span>

**Comment ça marche.** L'établissement porteur rédige un accord, puis le soumet ; le
partenaire l'examine, l'approuve ou le modifie. Toute modification par l'un des deux
côtés relance le cycle jusqu'à ce que les deux approbations coïncident : l'accord
devient alors actif. Une matrice de distribution des places est renseignée pour les
mobilités étudiantes. Un import avec aperçu est disponible.

**Cas d'usage.**
> Une école française signe un échange bilatéral avec un partenaire brésilien hors
> Erasmus ; les deux coordinateurs approuvent dans l'outil, puis le côté français
> répartit 2 places de Master en Semestre 1.

??? note "Détails internes (équipe AroundLink)"
    `BilateralAgreement` (clé `agreementId`, lignes aller/retour par direction), statut
    `BilateralAgreementStatusEnum{DRAFT, PENDING_PARTNER, IN_NEGOTIATION, PENDING_INTERNAL,
    ACTIVE, EXPIRED, RENEWAL, OPEN_ENDED}`. Places dans `BilateralAgreementPeriodPlace`
    (agreementId, subjectArea/ISCED, année, niveau, période, places). Workflow
    submit/approve dans `BilateralAgreementWorkflow`, protégé par jeton CSRF. La
    soumission recopie les contacts vers la section Relation du partenaire.

## Doubles diplômes

**À quoi ça sert.** Gère les partenariats de double diplôme, où l'étudiant obtient un
diplôme dans les deux établissements sur plusieurs années : phases annuelles, cursus
commun, conditions de diplomation et jury commun. Un cadre différent d'un simple
échange.

**Pour qui.** <span class="al-audience">gestionnaire RI / partenaire</span>

**Comment ça marche.** Même négociation bilatérale que les accords bilatéraux (rédaction,
soumission, approbation), avec une invitation adressée au signataire partenaire lors de
la soumission. L'accord porte les informations de cursus, de diplomation, de jury, de
niveau EQF et de durée, ainsi que des phases annuelles (Année 1 / Année 2). Les places
sont réparties via une matrice dédiée. Un import avec aperçu est disponible.

**Cas d'usage.**
> Un double diplôme de Master avec Georgia Tech sur 2 ans : l'étudiant part en 2ᵉ année ;
> le bureau suit chaque phase et distribue les places annuelles.

??? note "Détails internes (équipe AroundLink)"
    `DoubleDegreeAgreement` (clé `agreementId`), statut `DoubleDegreeStatusEnum` (mêmes
    8 états que le bilatéral), champs : durationYears, yearlyPlaces, partnerDegreeName,
    jointCurriculum, conditions de diplomation émetteur/récepteur, commonJury, eqfLevel,
    `fundingProgram`. Phases `DoubleDegreePhase{YEAR_1, YEAR_2}`. Les relevés de notes
    (ToR) se collectent de façon classique, via le dépôt de documents de l'étudiant. Places
    dans `DoubleDegreePeriodPlace`. Workflow `DoubleDegreeWorkflow`.

## Mobilité payante (study abroad)

**À quoi ça sert.** Gère les placements payants de type « study abroad », où l'étudiant
règle des frais de scolarité à l'établissement d'accueil et où l'établissement d'origine
maîtrise l'accord de bout en bout. Distingue la mobilité génératrice de frais de
l'échange Erasmus gratuit.

**Pour qui.** <span class="al-audience">gestionnaire RI (création) · étudiant (consultation du prix)</span>

**Comment ça marche.** Le coordinateur rédige puis publie l'accord (un seul propriétaire,
sans phase de négociation à deux) : montant des frais, devise, sous-type (placement
individuel ou gros flux), durée et type de mobilité. Il répartit ensuite les places via
la matrice de distribution. Lorsqu'un établissement propose de la mobilité payante, ces
offres sont visibles côté étudiant (dans « Find Exchange ») avec leur prix indicatif, pour
que l'étudiant connaisse le coût avant de candidater. Un import avec aperçu est disponible.

**Cas d'usage.**
> Un partenaire aux États-Unis où l'étudiant paie 12 000 $ de frais : le bureau
> l'enregistre comme accord payant « study abroad » et publie 5 places pour l'année.

??? note "Détails internes (équipe AroundLink)"
    `PayingMobilityAgreement` (clé `agreementId`), statut `PayingMobilityStatusEnum{DRAFT,
    ACTIVE, EXPIRED, OPEN_ENDED, MODIFIED}` (pas d'états de négociation — un seul côté).
    Champs : `agreementSubtype` (STUDY_ABROAD, HIGH_VOLUME), totalFeeAmount, currency,
    mobilityType. Action `publish()` (pas de submit/approve). Places dans
    `PayingMobilityPeriodPlace`. Workflow `PayingMobilityWorkflow`. Module réservé au plan
    payant.

## Imports CSV des accords

**À quoi ça sert.** Permet de charger des accords en masse depuis un tableur plutôt qu'un
par un, avec une étape d'aperçu et de correction avant validation pour intercepter les
lignes erronées. Accélère l'intégration de grands portefeuilles de partenaires.

**Pour qui.** <span class="al-audience">gestionnaire RI</span>

**Comment ça marche.** Chaque famille d'accords (échanges, IIA, bilatéral, double diplôme,
payant) dispose d'une page d'import. Le fichier est d'abord analysé et contrôlé ligne par
ligne dans un aperçu, où chaque ligne peut être corrigée, avant une validation finale qui
enregistre l'ensemble. Des modèles de fichier sont téléchargeables.

**Cas d'usage.**
> Un bureau colle 80 échanges depuis un ancien tableur, corrige 3 lignes signalées dans
> l'aperçu, puis valide.

??? note "Détails internes (équipe AroundLink)"
    Importeurs : `ExchangesImporter`, `IiaAgreementImporter`, `BilateralAgreementImporter`,
    `DoubleDegreeImporter`, `PayingMobilityImporter`. Parcours commun en trois étapes :
    aperçu (analyse + validation), correction d'une ligne, confirmation (persistance).
