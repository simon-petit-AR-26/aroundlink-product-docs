# Campagnes de mobilité

Le module Campagnes structure les sessions de candidature : les étudiants éligibles
classent un nombre défini de vœux parmi les offres du catalogue, et le bureau RI pilote
l'ensemble — de l'ouverture au placement final — sans reconstituer la liste à la main.

## Campagnes de mobilité

**À quoi ça sert.** Permet à un bureau des relations internationales d'organiser une
session de candidature cadrée, où les étudiants classent un nombre fixe de vœux d'échange
dans une période donnée. La campagne détermine automatiquement quels étudiants et quelles
offres partenaires en font partie, ce qui évite de sélectionner chaque participant
manuellement.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Le coordinateur crée une campagne en choisissant l'année
universitaire, le nombre de vœux autorisés, les niveaux d'études visés, les périodes de
mobilité, les types d'accords éligibles et un filtre optionnel par tag de partenaire. À
l'enregistrement, le système constitue automatiquement le vivier d'étudiants participants
et le vivier d'offres éligibles selon ces critères. La campagne passe de Brouillon à
Prête (ouverture aux étudiants), puis Ouverte et Terminée ; seule une campagne en
brouillon reste modifiable.

**Cas d'usage.**
> Le bureau RI ouvre une campagne « 2026/2027 – Semestre 1 – Master », 5 vœux autorisés,
> limitée aux partenaires Erasmus+ tagués « Ingénierie » ; tous les étudiants de Master
> avec une période Semestre 1 sont inscrits automatiquement.

??? note "Détails internes (équipe AroundLink)"
    Entité `Campaign` : `wishesNumber`, `academicLevels`, `periods` (M2M `MobilityPeriod`),
    `agreementTypes` (`AgreementTypeEnum`), `requiredFileTypes` (documents à faire valider
    avant de soumettre des vœux), `filterPartnerTags`. Statut `CampaignStatusEnum{DRAFT,
    READY, OPENED, FINISHED}`. `CampaignManager::handleCampaign()` reconstruit les relations
    à chaque création/édition. Sélection via
    `AcademicLevelResolver::expandLevelsToEqfSiblingValues()` (un niveau tire ses voisins
    EQF) ; un échange sans place sur les périodes de la campagne est écarté.

## Vœux, propositions et affectations

**À quoi ça sert.** Transforme la liste de vœux classés de chaque étudiant en une
affectation confirmée, en respectant les places réellement disponibles et le rang de
l'étudiant. Automatise l'attribution « qui va où » que les bureaux gèrent sinon sur
tableur, tout en laissant le coordinateur ajuster et l'étudiant accepter ou refuser.

**Pour qui.** <span class="al-audience">coordinateur / étudiant</span>

**Comment ça marche.** Les étudiants soumettent une liste de vœux ordonnée. Le
coordinateur lance l'attribution automatique, qui traite les étudiants par rang (GPA) et
propose à chacun le premier vœu disposant encore d'une place sur sa période ; ceux qui ne
peuvent être placés sont signalés. Le coordinateur peut ensuite pré-affecter (forcer),
refuser ou annuler une proposition — chaque action recalcule le reste — puis envoyer les
propositions aux étudiants, qui acceptent (créant une nomination auprès du partenaire) ou
refusent (ce qui annule leurs autres vœux et libère la place). Quand une proposition est
envoyée ou qu'un étudiant est affecté, celui-ci peut être prévenu — par e-mail et/ou dans
l'application ; ces notifications sont paramétrables et peuvent être désactivées par
l'établissement.

**Cas d'usage.**
> Deux étudiants classent Berlin en vœu n°1 : le mieux classé (GPA) reçoit la proposition,
> l'autre bascule automatiquement sur son vœu n°2. Le coordinateur pré-affecte ensuite un
> cas particulier, et le système redistribue la place libérée.

??? note "Détails internes (équipe AroundLink)"
    `CampaignWish.status` = `WishStatusEnum{DRAFT_STUDENT, SUBMITTED_BY_STUDENT,
    SYSTEM_PROPOSAL, SYSTEM_NOT_ENOUGH_PLACES, COORDINATOR_PROPOSAL,
    COORDINATOR_PROPOSAL_SENT_TO_STUDENT, ACCEPTED_BY_STUDENT, REFUSED_BY_COORDINATOR,
    REFUSED_BY_STUDENT, CANCELLED_AFTER_REFUSAL}`. Comptage des places via
    `MobilitySpecPlaces` (compteur par période). `MatchmakingService` traite les étudiants
    par rang. À l'acceptation, `CampaignWishesManager::acceptWish()` réutilise ou crée un
    `ExchangeAffectation` au statut `PENDING` (nomination EWP vers le partenaire), dans une
    transaction ; le lien vœu ↔ affectation est unique. Une re-nomination après refus/annulation
    repasse en `PENDING` sans jamais rétrograder un `APPROVED`. Le drapeau
    `matchMakingCompleted` empêche de relancer l'attribution globale.

## Suivi, résultats et exports

**À quoi ça sert.** Offre au coordinateur un tableau de bord opérationnel de la campagne
en cours (qui a soumis, qui est placé, complétude des dossiers), des vues résultats et
acceptés, ainsi que des exports CSV pour la suite du traitement. Une campagne devient un
processus traçable et exploitable.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** La page de suivi agrège les participants, leurs vœux par rang, les
propositions et affectations, avec des graphiques et un compteur de dossiers complets. Des
pages dédiées présentent les résultats et les acceptés, et deux exports produisent la liste
de tous les vœux et celle des affectations finales.

**Cas d'usage.**
> À mi-parcours, le coordinateur constate que 60 % des étudiants ont soumis leurs vœux et
> que 12 sont placés ; après clôture, il exporte les affectations finales pour l'équipe
> mobilité.

??? note "Détails internes (équipe AroundLink)"
    `trackCampaign()` : graphiques via `ChartBuilderInterface`, vœux regroupés par rang,
    complétude dérivée des propositions/affectations existantes. Exports via
    `CampaignExportService` (`exportAllWishes`, `exportFinalAssignments`). Aperçu live
    (`/preview`) pour les compteurs du formulaire de création.

!!! note "Relances documentaires"
    Les rappels automatiques aux étudiants dont le dossier est incomplet sont couverts par
    les [relances documentaires](communications.md).
