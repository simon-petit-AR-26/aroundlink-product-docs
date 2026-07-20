# Documents & validation

Le module Documents rassemble, au même endroit, tout ce que votre bureau des
relations internationales doit produire, contrôler et valider pendant une mobilité :
contrat pédagogique (Learning Agreement / OLA), relevé de notes (Transcript of
Records), pièces administratives des étudiants et modèles de documents officiels.
Objectif : un flux clair, une seule file d'attente pour les validations, et des
règles Erasmus+ appliquées automatiquement.

## Contrat pédagogique (Learning Agreement / OLA)

**À quoi ça sert.** Le Learning Agreement décrit le programme de cours qu'un étudiant
suivra à l'étranger. Cette vue permet au bureau de suivre chaque contrat, de voir en un
coup d'œil ceux qui sont en attente, validés ou à corriger, et de faire respecter la
signature des deux établissements avant qu'un contrat ne devienne définitif.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Le coordinateur ouvre la liste des OLA, filtre par statut et
consulte chaque contrat dans une fenêtre qui affiche son historique. Il peut demander
des modifications — le contrat repart alors en brouillon avec un commentaire pour
l'étudiant — ou l'approuver. Pour un accord classique, chaque établissement signe de
son côté, dans n'importe quel ordre, et le contrat n'est validé qu'une fois les deux
signatures posées ; pour un accord EWP, l'approbation transmet le contrat à
l'établissement d'accueil selon le flux séquentiel du réseau.

**Cas d'usage.**
> Le coordinateur relit l'OLA de départ de Marie (3 cours, 18 ECTS), lui demande de
> remplacer un cours, puis signe au nom de l'établissement d'envoi ; dès que le
> partenaire signe à son tour, l'OLA passe « Validé ».

??? note "Détails internes (équipe AroundLink)"
    Statuts (`LearningAgreementStatus`) : Draft, Selected by student, Pending sending
    school validation, Pending receiving school validation, Validated, Refused by
    receiving school. Étapes (`LearningAgreementStep`, formulation officielle OLA) :
    Before / During / After the mobility (1/3, 2/3, 3/3).

    Accord non-EWP = signature parallèle (`sendingSchoolSignedAt` /
    `receivingSchoolSignedAt`), validation dès `areBothSchoolsSigned()` ; accord EWP =
    progression séquentielle via le statut. Un refus renvoie l'OLA en brouillon,
    ré-éditable par l'étudiant. Les tables d'avenants (A2/B2) déclenchent un nouveau
    cycle de signature (`resetForAmendments()`).

    À la validation complète, la date de signature du LA est reportée sur la bourse
    liée (pont vers le module Bourse de mobilité). Chaque action de mutation vérifie
    l'appartenance de l'étudiant au périmètre du coordinateur.

## Génération PDF : OLA & relevé de notes

**À quoi ça sert.** Produit le PDF officiel du contrat pédagogique ou du relevé de
notes à partir du modèle de document de l'établissement (en-tête, mise en page), avec
le tableau de cours de l'étudiant inséré automatiquement. Le bureau obtient un document
prêt à archiver, aux couleurs de l'établissement.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Depuis la liste des OLA, le coordinateur télécharge le PDF du
contrat pédagogique ou du relevé de notes. Le contrat n'est téléchargeable qu'une fois
pleinement validé ; le relevé de notes une fois le relevé lui-même validé. Le système
remplit le modèle avec les cours (et les notes, pour le relevé).

**Cas d'usage.**
> Après la double signature, le coordinateur télécharge le Learning Agreement en PDF,
> à l'en-tête de l'établissement, pour le dossier de l'étudiant.

??? note "Détails internes (équipe AroundLink)"
    Le PDF réutilise le modèle actif de l'établissement pour le type demandé (voir
    « Modèles de documents »). Les jetons `{{COURSES_TABLE}}` /
    `{{COURSES_TABLE_WITH_GRADES}}` sont résolus avec les cours de l'accord. Si aucun
    modèle actif du type n'existe, un message renvoie vers Paramètres → Modèles de
    documents.

## Relevé de notes (Transcript of Records)

**À quoi ça sert.** Gère le relevé de notes de l'étudiant entrant que l'établissement
d'accueil doit renvoyer à l'établissement d'origine. Le coordinateur relit les notes
saisies et le relevé officiel déposé, puis valide ou demande des corrections.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur (validation) ; étudiant (saisie)</span>

**Comment ça marche.** L'étudiant saisit chaque note selon le système de notation choisi
et dépose le relevé officiel. Le coordinateur ouvre le relevé dans une fenêtre qui
affiche l'historique et le document déposé, puis valide — le relevé devient
téléchargeable — ou renvoie le dossier à l'étudiant pour correction.

**Cas d'usage.**
> Un étudiant entrant dépose son relevé officiel et saisit ses notes ; le coordinateur
> vérifie, valide, et le relevé de notes est prêt à être transmis à l'université
> d'origine.

??? note "Détails internes (équipe AroundLink)"
    Statuts (`TranscriptOfRecordStatus`) : Pending student filling grades, Pending
    validation by school, Validated by receiving/sending school, Refused by
    receiving/sending school. La soumission étudiante exige une note valide (selon
    `GradingSystemEnum`) pour chaque cours.

    La validation métier « fait foi » : approuver aligne le fichier officiel déposé sur
    l'état validé, ce qui coche la pièce « relevé de notes » côté Bourse et satisfait la
    condition de clôture. Une demande de modification décoche la Bourse.

## File de validation (Validation Hub)

**À quoi ça sert.** Une file d'attente unique où le coordinateur valide tout ce que
l'étudiant soumet pendant sa mobilité — pièces administratives, contrats pédagogiques,
relevés de notes et témoignages sur les partenaires — sans avoir à parcourir plusieurs
écrans. Les éléments en attente depuis longtemps sont signalés comme urgents, et chaque
décision est archivée avec son auteur, son issue et le motif de refus.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** La file regroupe les documents en attente, les OLA qui attendent
la signature de l'établissement, les relevés de notes et les témoignages, avec des
compteurs (en attente / étudiants concernés / urgents). Le coordinateur ouvre chaque
élément et décide de valider ou refuser ; un commentaire est requis en cas de refus. Un
onglet « Historique » liste les décisions passées avec leur motif.

**Cas d'usage.**
> Lundi matin, le coordinateur voit 12 éléments en attente dont 3 urgents : il valide
> deux passeports, signe un OLA au nom de l'établissement d'envoi et refuse une
> attestation d'assurance illisible avec un commentaire — le tout depuis la même file.

??? note "Détails internes (équipe AroundLink)"
    Quatre types d'éléments (StudentFile, LearningAgreement non-EWP en attente de
    signature, TranscriptOfRecord, Feedback). Motif conservé selon le type
    (`refusal_reason` pour les pièces, ligne d'historique pour LA/ToR/Feedback, ticket
    AROUNDLINK-548). Urgent = en attente ≥ 7 jours.

    Garde métier : une attestation d'arrivée/de départ ne peut être validée que si
    l'étudiant a déclaré la date correspondante (elle conditionne le versement de la
    bourse). Modération des témoignages : valider peut aussi publier ; refuser masque
    toujours. Les nominations ne passent pas par cette file.

## Pièces administratives des étudiants

**À quoi ça sert.** Page centrale listant toutes les pièces déposées par les étudiants
(passeport, assurance, tests de langue, attestations d'arrivée/de départ, etc.) avec
leur statut. Le bureau valide ou refuse les pièces une par une ou en lot, enregistre les
dates d'arrivée et lance des campagnes de relance vers les étudiants dont les documents
manquent ou ont été refusés.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Le coordinateur filtre la liste des pièces, en valide ou refuse
plusieurs d'un coup, renseigne la date d'arrivée d'un étudiant, estime le nombre
d'étudiants qui seraient relancés, puis déclenche une campagne de relance en un clic.

**Cas d'usage.**
> Le coordinateur filtre sur « Refusé », sélectionne 8 pièces, les refuse en lot avec un
> commentaire, puis envoie une relance aux étudiants concernés.

??? note "Détails internes (équipe AroundLink)"
    Statuts (`StudentFileStatusEnum`) : Pending / Validated / Refused (avec
    `refusal_reason`). Les validations en lot re-vérifient l'appartenance de chaque
    fichier au périmètre du coordinateur. La date d'arrivée refuse les dates futures et
    pilote le versement du solde de bourse. La validation d'une pièce peut alimenter la
    checklist de la bourse liée.

## Modèles de documents

**À quoi ça sert.** Permet à chaque établissement de concevoir ses propres modèles de
documents réutilisables (lettre de nomination, contrat pédagogique, lettre
d'acceptation, certificat de scolarité, relevé de notes, certificat de visa, attestation
de logement) avec des champs `{{…}}` qui se remplissent automatiquement avec les données
réelles d'un étudiant.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Le coordinateur liste, crée et modifie ses modèles, compose le
corps du document à l'aide des variables proposées, prévisualise la mise en page en PDF
(jetons encore visibles) pour vérifier l'espacement et la pagination, puis génère un PDF
rempli pour un étudiant donné. Il peut activer/désactiver un modèle ou le supprimer. Les
modèles institutionnels mis à disposition sont visibles en lecture seule.

**Cas d'usage.**
> Le coordinateur crée un modèle « Lettre d'acceptation » avec le logo de
> l'établissement, vérifie l'aperçu, puis le génère rempli pour un étudiant entrant en
> un clic.

??? note "Détails internes (équipe AroundLink)"
    Types (`DocumentTemplateTypeEnum`, ensemble fermé, contrôlé en base) :
    nomination_letter, learning_agreement, acceptance_letter, enrollment_certificate,
    transcript, visa_certificate, housing_certificate. Champs : nom, type, type de
    mobilité (défaut « ALL »), contenu, actif/inactif, propriétaire, université de
    rattachement.

    Chaque coordinateur possède son propre pool ; les modèles institutionnels
    (propriétaire vide) sont visibles pour les coordinateurs de l'université ciblée mais
    modifiables uniquement côté administration. La génération est restreinte aux
    étudiants de l'université du coordinateur. Variables issues de `DocumentVariableEnum`.

## Activer / désactiver des types de documents

**À quoi ça sert.** Permet à chaque établissement d'activer ou de désactiver certains
types de documents, pour qu'un type inutile cesse d'apparaître sur la page de dépôt des
étudiants et dans les listes déroulantes. Par défaut, tous les types sont actifs.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Dans Paramètres → Documents, chaque type de document dispose d'un
interrupteur ON/OFF enregistré par établissement.

**Cas d'usage.**
> Un établissement qui n'émet jamais d'attestation de logement désactive ce type : il
> disparaît de la checklist de tous ses étudiants.

??? note "Détails internes (équipe AroundLink)"
    Désactivation par présence d'une ligne `DisabledDocumentType`, unique par (université,
    type de fichier). Aucune ligne = type actif (comportement par défaut préservé). La
    liste des types désactivés pilote l'affichage côté étudiant.

## Revue des mises à jour d'accord (IIA)

**À quoi ça sert.** Lorsqu'un établissement partenaire pousse des modifications sur un
accord inter-établissements (IIA) via le réseau EWP, cette revue affiche un comparatif
champ par champ et permet d'accepter ou de rejeter sélectivement les changements avant
qu'ils ne modifient les données locales.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.** Le coordinateur ouvre la mise à jour en attente et voit le
comparatif entre sa version et celle du partenaire. Il coche les champs à accepter et
applique — un décompte des champs appliqués/ignorés est affiché — ou rejette la mise à
jour, auquel cas ses données restent inchangées.

**Cas d'usage.**
> Le partenaire modifie les ECTS et les langues de l'accord ; le coordinateur accepte le
> changement de langue mais rejette celui des ECTS — seul le champ accepté est écrit
> localement.

??? note "Détails internes (équipe AroundLink)"
    Statuts de la mise à jour en attente (`ExchangeIiaPendingUpdateStatusEnum`) :
    PENDING_REVIEW / REJECTED. L'application n'est possible que tant que la mise à jour
    est en revue. Auteur, horodatage et notes de revue sont conservés. Retour à la liste
    des accords après décision.
