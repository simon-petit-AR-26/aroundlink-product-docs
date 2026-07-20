# Espace étudiant — Pendant & après la mobilité

Une fois l'étudiant placé, l'espace étudiant devient son poste de pilotage pour
la mobilité elle-même : suivi de l'exchange, contrat pédagogique (OLA), relevé
de notes, attestations, ressources, services, et communication directe avec le
bureau des relations internationales. L'objectif reste le même : autonomie de
l'étudiant et sérénité pour le gestionnaire RI.

## Mon exchange

**À quoi ça sert.** Une fois placé, c'est la page opérationnelle de l'étudiant
pour la mobilité : elle affiche l'établissement d'accueil, les dates de
mobilité, le contact partenaire et les avis publiés, et permet de déposer les
attestations d'arrivée et de départ. L'étudiant peut aussi télécharger une
attestation d'affectation officielle.

**Pour qui.** <span class="al-audience">étudiant</span>

**Comment ça marche.** La page charge l'affectation approuvée de l'étudiant et
présente les formulaires de dépôt des attestations d'arrivée et de départ ;
l'enregistrement est bloqué une fois le document validé par le coordinateur. La
durée de mobilité s'appuie sur les vraies dates d'attestation lorsqu'elles sont
saisies, sinon sur des dates provisoires dérivées de l'année scolaire. Un bouton
génère l'attestation d'affectation en PDF, à partir du modèle de lettre de
nomination configuré par l'établissement lorsqu'il existe.

**Cas d'usage.**
> À son arrivée à l'étranger, un étudiant dépose son attestation d'arrivée signée
> et télécharge son attestation d'affectation officielle pour le guichet
> d'inscription de l'établissement d'accueil.

??? note "Détails internes (équipe AroundLink)"
    Les attestations d'arrivée (COA) et de départ (COD) sont gérées par leurs
    gestionnaires dédiés ; une fois validées, elles sont verrouillées côté
    étudiant. L'attestation d'affectation vérifie que le document appartient bien
    à l'étudiant connecté avant génération, et se replie sur une mise en page
    intégrée si aucun modèle de lettre de nomination n'est configuré. Le contact
    partenaire principal et jusqu'à 6 avis publiés (acceptés et publics)
    complètent la page.

## Contrat pédagogique (OLA)

**À quoi ça sert.** L'étudiant construit son Learning Agreement (contrat
pédagogique en ligne, OLA) en choisissant ses cours dans l'établissement
d'accueil, regroupés par domaine. Il voit le total d'ECTS, enregistre des
brouillons, puis soumet — ce qui vaut sa signature. Le contrat validé est
téléchargeable en PDF.

**Pour qui.** <span class="al-audience">étudiant</span>

**Comment ça marche.** L'espace charge l'affectation approuvée et le dernier OLA
(en crée un brouillon si nécessaire). Les cours proposés par le partenaire sont
présentés par domaine ; l'étudiant peut aussi ajouter un nouveau cours.
L'enregistrement en brouillon conserve le statut brouillon ; la soumission
enregistre la signature de l'étudiant et fait passer le statut à
« Sélectionné par l'étudiant ». Modifier les cours réinitialise les signatures
d'établissement déjà apposées, pour éviter toute validation sur une version
obsolète. Le téléchargement n'est possible qu'une fois l'OLA entièrement validé.

**Cas d'usage.**
> Un étudiant choisit 6 cours (30 ECTS) répartis sur deux domaines, soumet son
> OLA, puis télécharge plus tard le PDF signé par les trois parties.

??? note "Détails internes (équipe AroundLink)"
    Un même mécanisme de résolution garantit que l'affichage de la page et toutes
    les écritures asynchrones portent sur le dernier OLA (protection contre les
    affectations multiples). Le téléchargement s'appuie sur le modèle de
    document de type Learning Agreement de l'établissement et n'est servi que
    lorsque l'OLA est entièrement validé. Un fil d'historique retrace les
    actions.

## Relevé de notes (Transcript of Records)

**À quoi ça sert.** Après la mobilité, l'étudiant enregistre les notes obtenues
pour chaque cours de l'OLA, choisit le système de notation, téléverse
éventuellement le relevé officiel et le soumet pour validation par son
établissement. C'est ce qui referme la boucle académique de l'exchange.

**Pour qui.** <span class="al-audience">étudiant</span>

**Comment ça marche.** La page nécessite une affectation approuvée et un OLA
existant. Elle affiche les cours de l'OLA, des statistiques de relevé, les
systèmes de notation, un formulaire de téléversement et l'historique. À la
soumission, l'espace vérifie que chaque cours a une note valide pour le système
choisi, enregistre les notes, téléverse le cas échéant le relevé officiel, puis
enregistre le relevé au statut « En attente de validation par l'établissement ».

**Cas d'usage.**
> Un étudiant de retour saisit les notes ECTS de ses 6 cours, téléverse le relevé
> officiel de l'établissement d'accueil, et soumet pour validation.

??? note "Détails internes (équipe AroundLink)"
    La validation des notes dépend du système de notation choisi ; les
    statistiques sont calculées par le gestionnaire de relevés. Le fichier est
    enregistré avec le type « Transcript of Records ». Le téléchargement PDF du
    relevé validé est servi depuis le module de contrat pédagogique.

## Ressources

**À quoi ça sert.** Une bibliothèque où l'étudiant trouve les documents et guides
que son établissement a publiés pour les étudiants sortants (livrets, listes de
contrôle, informations pré-départ).

**Pour qui.** <span class="al-audience">étudiant</span>

**Comment ça marche.** La page liste les fichiers de l'établissement destinés au
public « sortant ». Elle reste vide si aucun établissement de rattachement n'est
disponible pour l'étudiant.

**Cas d'usage.**
> Un étudiant télécharge le guide pré-départ Erasmus de son établissement.

??? note "Détails internes (équipe AroundLink)"
    Le filtre d'audience cible les fichiers visibles par le public sortant.

## Services

**À quoi ça sert.** Une place de marché de services tiers (logement, assurance,
banque…) proposés aux étudiants, affichée uniquement lorsque l'établissement a
activé la marketplace.

**Pour qui.** <span class="al-audience">étudiant</span>

**Comment ça marche.** L'accès est conditionné à l'activation de la marketplace
par l'établissement. Les offres sont présentées à titre informatif, avec des liens
d'affiliation (et, selon les cas, des codes promo) vers le prestataire. Aucun
paiement n'a lieu dans AroundLink : pour souscrire, l'étudiant est redirigé vers le
site du partenaire.

**Cas d'usage.**
> Un étudiant repère une offre d'assurance avec un code promo, clique et finalise sa
> souscription directement sur le site du prestataire.

??? note "Détails internes (équipe AroundLink)"
    Affichage + affiliation (liens et codes promo vers le prestataire) ; aucun
    paiement ne transite par la plateforme. Option activable par établissement ;
    seules les offres actives sont affichées.

## Messagerie avec le bureau des relations internationales

**À quoi ça sert.** Une messagerie intégrée permet à l'étudiant d'échanger en
tête-à-tête avec son bureau des relations internationales / coordinateur, avec
boîte de réception, fils de discussion, réponses et badge de messages non lus.

**Pour qui.** <span class="al-audience">étudiant / coordinateur</span>

**Comment ça marche.** La boîte de réception liste les conversations ; ouvrir un
fil le marque comme lu ; répondre envoie un message. Un écran « Nouveau message »
présente les destinataires joignables, et démarrer une conversation vérifie que
l'étudiant peut bien contacter ce destinataire avant de créer le fil. Un
compteur alimente le badge de messages non lus.

**Cas d'usage.**
> Un étudiant écrit à son coordinateur pour une question sur un document manquant,
> et voit la réponse avec un badge de non-lu à sa prochaine connexion.

??? note "Détails internes (équipe AroundLink)"
    Fonctionnement identique au côté RI. Le rôle étudiant est exigé au niveau du
    module. La participation au fil est vérifiée à chaque ouverture et chaque
    réponse. Un endpoint de comptage alimente le badge.

## Notifications

**À quoi ça sert.** Un fil de notifications intégré tient l'étudiant informé des
événements de son parcours (propositions, validations, messages), avec lecture à
l'ouverture, une action « tout marquer comme lu » et un compteur de non-lus en
direct.

**Pour qui.** <span class="al-audience">étudiant</span>

**Comment ça marche.** La page liste les notifications les plus récentes ; ouvrir
l'une d'elles la marque comme lue ; « tout marquer comme lu » traite l'ensemble
et revient à la page précédente. Un compteur alimente le badge.

**Cas d'usage.**
> Un étudiant reçoit une notification lui indiquant que son OLA a été validé et
> clique pour en voir le détail.

??? note "Détails internes (équipe AroundLink)"
    Fonctionnement identique au côté mobilité. Le rôle étudiant est exigé au
    niveau du module. Une vérification d'appartenance protège l'ouverture d'une
    notification.
