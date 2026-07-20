# Bourse de mobilité

Le module Bourse de mobilité gère l'ensemble du volet financier Erasmus+ de votre
établissement : dotation annuelle, attribution des bourses aux étudiants, suivi des
versements, checklist des pièces justificatives et export vers le rapport officiel. Les
règles Erasmus+ (documents conditionnant chaque versement, garde-fous budgétaires,
barèmes par pays) sont appliquées automatiquement, ce qui sécurise vos audits.

!!! note "Module réservé aux offres payantes"
    La Bourse de mobilité fait partie de l'offre payante d'AroundLink. Elle n'est
    accessible qu'aux établissements ayant souscrit à cette formule.

## Tableau de bord Finance

**À quoi ça sert.** La page d'accueil du module : une vue par année académique qui réunit
les indicateurs budgétaires, le suivi des bourses et le tableau des dossiers, pour que le
bureau ait la situation financière Erasmus+ sous les yeux d'un seul coup d'œil.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Le coordinateur choisit l'année académique ; le tableau de bord
affiche alors la dotation, les montants engagés et versés, le budget restant et
l'avancement des dossiers de bourse.

**Cas d'usage.**
> En début d'année, le coordinateur ouvre le tableau de bord et voit d'un coup d'œil
> combien de sa dotation est déjà engagée et combien reste disponible.

## Dotation Erasmus+ (budget)

**À quoi ça sert.** Enregistre la dotation Erasmus+ totale de l'établissement pour
l'année académique et affiche en temps réel des chiffres consolidés — dotation, montant
engagé sur les bourses, montant réellement versé, reste disponible — pour que le bureau
ne sur-engage jamais son financement.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Le coordinateur saisit le montant de la dotation pour l'année ; le
module calcule et affiche automatiquement le montant engagé, le montant versé et le reste
disponible, consolidés à l'échelle de l'établissement (tous campus confondus).

**Cas d'usage.**
> Le coordinateur enregistre une dotation de 120 000 € ; à mesure que les bourses sont
> créées, le tableau de bord affiche 80 000 € engagés, 45 000 € versés, 40 000 € restants.

??? note "Détails internes (équipe AroundLink)"
    Le résumé consolide : dotation (somme des lignes de tous les campus), montant engagé
    (somme des montants attribués des bourses hors brouillon), montant versé
    (acompte + solde), reste (dotation − engagé), nombre de dossiers en attente de
    documents. La saisie est déterministe : elle met à jour la ligne existante de
    l'établissement (rattachée au campus principal à la création) pour éviter tout
    doublon. Format d'année BM : `YYYY-YYYY`. Verrouillage des lignes disponible pour les
    contrôles concurrents.

## Gestion des bourses et cycle de vie

**À quoi ça sert.** Le dossier central de bourse : un dossier par étudiant et par année,
qui porte le type de mobilité, les dates, le montant attribué, les versements et la
checklist des 7 pièces Erasmus+. Son statut avance automatiquement au fil des signatures
et des versements, si bien que le bureau sait toujours où en est chaque dossier sans tenue
de compte manuelle.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Le coordinateur crée une bourse pour un étudiant, renseigne le type
de mobilité, les dates et le montant. Le statut n'est pas piloté à la main : le dossier
démarre « en attente de convention », puis passe seul en « actif » quand la convention et
le contrat pédagogique sont signés et l'acompte versé, en « documents attendus » à la fin
de la mobilité, et se clôture quand toutes les pièces finales sont reçues.

**Cas d'usage.**
> Le coordinateur crée une bourse pour une mobilité d'études vers Berlin ; à mesure que la
> convention et le contrat pédagogique sont signés et l'acompte versé, la bourse passe
> seule en « actif », puis se clôture d'elle-même une fois l'attestation de séjour, le
> relevé de notes et le rapport final reçus.

??? note "Détails internes (équipe AroundLink)"
    Statuts (`GrantStatusEnum`) : draft, ga_pending, active, docs_pending, closed. Un
    nouveau dossier démarre toujours en ga_pending (le statut envoyé est ignoré).
    Transitions automatiques (`GrantDocumentSyncer`) enchaînées en une passe : ga_pending
    → active (convention + LA signés + acompte versé) ; active → docs_pending (date de fin
    dépassée) ; docs_pending → closed (toutes les pièces finales reçues, ToR et rapport
    final adossés à un fichier validé) ; retour à docs_pending si une pièce disparaît.

    Checklist en 7 jalons répartis par étape : avant (convention, LA, test de langue),
    début (arrivée), fin (attestation de séjour, ToR, rapport final). Un seul dossier par
    (étudiant, année). Suppression possible uniquement tant qu'aucun fonds n'est engagé
    (statut ga_pending). Champs complémentaires Mobility Tool+ : niveau EQF et langue
    d'enseignement (repris de l'accord), scores OLS, besoins spécifiques, moins
    d'opportunités.

## Garde-fous budgétaires

**À quoi ça sert.** Empêche le bureau d'attribuer plus de bourses que la dotation
Erasmus+ ne le permet, y compris lorsque deux coordinateurs agissent en même temps.
Distingue clairement « dotation non renseignée » (action à mener) de « dotation épuisée ».

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** À la création ou à la modification d'une bourse, le module vérifie
que le montant demandé ne dépasse pas le reste disponible et bloque l'opération le cas
échéant, avec un message explicite. Seules les hausses d'engagement sont bloquées :
corriger un montant à la baisse ou l'effacer reste toujours possible.

**Cas d'usage.**
> Deux coordinateurs tentent en même temps d'ajouter des bourses de 5 000 € alors qu'il ne
> reste que 6 000 € : la première passe, la seconde est refusée avec « budget
> insuffisant ».

??? note "Détails internes (équipe AroundLink)"
    Les bourses en brouillon ou sans montant ne touchent pas au budget. Deux messages
    distincts : « aucune dotation configurée… » et « budget insuffisant… ». À la
    modification, seul le supplément d'engagement (nouveau − ancien) est contrôlé. La
    persistance se fait sous verrou budgétaire pour sérialiser les créations concurrentes.

## Conditions de versement

**À quoi ça sert.** Applique les règles Erasmus+ qui conditionnent chaque tranche de
versement, pour que le bureau ne puisse pas enregistrer un paiement avant que les
documents requis n'existent. Protège la conformité en cas de contrôle.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Au moment d'enregistrer un versement, le module bloque une hausse
de l'acompte tant que la convention et le contrat pédagogique ne sont pas signés, et une
hausse du solde tant que l'attestation de fin de séjour et le rapport final ne sont pas
reçus. Il garantit aussi qu'aucun versement n'est saisi sans montant attribué et que le
total versé ne dépasse pas le montant attribué.

**Cas d'usage.**
> Le coordinateur tente d'enregistrer l'acompte avant la signature du contrat pédagogique :
> « Versement de l'acompte bloqué — la convention et le contrat pédagogique doivent être
> signés au préalable ».

??? note "Détails internes (équipe AroundLink)"
    Évalué après toutes les modifications de la fiche, ce qui permet de signer la
    convention/le LA et de saisir l'acompte dans la même sauvegarde. Les verrous
    documentaires ne s'appliquent qu'aux hausses de montant versé : une correction à la
    baisse ou un effacement reste permis. Cohérence (acompte + solde) ≤ montant attribué.

## Calcul du montant de bourse

**À quoi ça sert.** Calcule le montant de bourse suggéré à partir du barème officiel
Erasmus+ (taux mensuel par pays × durée, ou taux journalier pour les programmes intensifs
mixtes), pour que le bureau ne calcule plus les montants à la main et reste aligné sur les
taux des agences nationales, révisés chaque année.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Pendant la saisie, le module propose en temps réel un montant à
partir de l'établissement, du type de mobilité et des dates. Pour une mobilité d'études ou
de stage, le calcul applique le taux mensuel du pays d'accueil à la durée ; pour un
programme intensif mixte, un taux journalier à la durée en jours.

**Cas d'usage.**
> Le coordinateur saisit une mobilité d'études vers l'Allemagne du 01/09 au 31/12 ; le
> formulaire affiche instantanément le montant suggéré, calculé à partir du taux du groupe
> de pays et de 4 mois.

??? note "Détails internes (équipe AroundLink)"
    SMS/SMP : taux mensuel × mois arrondis (mois calendaires + 1 si jours résiduels > 15).
    BIP : taux journalier × jours inclusifs (fin − début + 1). Les taux sont lus dans la
    table `bm_rates` (par pays et par année, format `YYYY-YYYY`), ce qui permet une mise à
    jour annuelle sans redéploiement. Un montant ne peut être calculé que si un taux est
    configuré pour le pays et l'année.

## Import CSV des bourses

**À quoi ça sert.** Permet de créer de nombreuses bourses d'un coup à partir d'un tableur,
plutôt qu'une par une, avec un flux « vérifier puis confirmer » qui signale les erreurs et
avertissements ligne par ligne et refuse tout dépassement de la dotation.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Le coordinateur télécharge un modèle de fichier, le remplit,
l'envoie pour prévisualisation — il obtient un rapport par ligne (erreurs, avertissements,
montant suggéré si la case est vide) — puis confirme pour créer les bourses valides. Une
ligne invalide n'empêche pas les autres d'être importées.

**Cas d'usage.**
> Le coordinateur importe 40 bourses depuis un tableur ; 3 lignes signalent un dépassement
> de la dotation et sont écartées, 37 sont créées.

??? note "Détails internes (équipe AroundLink)"
    Le statut n'est pas pilotable à l'import : toute bourse importée démarre en ga_pending.
    Détection automatique du séparateur (`, ; tab`), gestion du BOM UTF-8, montant vide →
    suggestion calculée. Garde budgétaire cumulative : l'import suit la consommation ligne
    à ligne et refuse une ligne qui ferait passer le reste sous zéro. Import stateless (le
    fichier est ré-analysé à la confirmation) ; chaque ligne valide est persistée dans sa
    propre transaction.

## Export (Beneficiary Module) et journal d'audit

**À quoi ça sert.** Produit le fichier CSV riche dont le bureau a besoin pour remonter les
mobilités dans le Beneficiary Module Erasmus+ (identités officielles des organismes,
domaine d'études ISCED, données du participant, identifiant unique de mobilité, bande de
distance, indicateurs dérivés), ainsi qu'un export du journal des modifications (qui a
changé quoi, quand) pour l'audit interne.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur ; finance et conformité</span>

**Comment ça marche.** Le coordinateur exporte, pour l'année choisie, le CSV des bourses
prêt à être remonté dans le Beneficiary Module, et séparément le journal d'audit qui
retrace chaque modification avec son auteur et sa date.

**Cas d'usage.**
> Au moment du reporting, le coordinateur exporte les bourses de l'année pour les remonter
> dans le Beneficiary Module, et sort le journal d'audit pour l'auditeur interne.

??? note "Détails internes (équipe AroundLink)"
    L'export réutilise la sérialisation des bourses et des résolveurs (identité officielle
    via le registre ECHE, domaine ISCED, distance à vol d'oiseau → bande Erasmus+, codes
    niveau d'études EQF→BM, type d'activité, indicateurs long terme/BIP/doctorat/
    international). Réponses en flux, toujours cadrées sur une année. Neutralisation
    anti-injection de formule sur les cellules texte.

## Sélection des étudiants éligibles

**À quoi ça sert.** À la création d'une bourse, ne propose que les étudiants réellement
éligibles à une bourse Erasmus+ (affectation active vers un pays du programme couvert par
le barème) et signale ceux qui ont déjà une bourse, pour éviter les dossiers invalides ou
en double.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Dans la fenêtre de création, le module affiche la liste des
étudiants éligibles de l'année et de l'établissement, avec pour chacun le type de mobilité
suggéré, l'établissement d'accueil, et une indication s'ils ont déjà une bourse.

**Cas d'usage.**
> Dans la fenêtre « nouvelle bourse », le coordinateur ne voit que les 22 étudiants
> éligibles ; 3 ont déjà une bourse et sont signalés comme tels.

??? note "Détails internes (équipe AroundLink)"
    Filtre d'éligibilité (`GrantEligibilityResolver`) : exclut les étudiants sans
    affectation active ou dont la destination n'est pas couverte par le barème. Chaque
    entrée porte le type de mobilité suggéré, l'établissement d'accueil et l'indicateur
    `has_grant`. Tri par nom, pas de pré-remplissage des dates (saisies manuellement).
