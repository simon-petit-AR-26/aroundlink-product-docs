# Réseau EWP (Erasmus Without Paper)

EWP (Erasmus Without Paper) est le standard européen d'interopérabilité qui permet
aux services des relations internationales d'échanger leurs données de mobilité de
façon entièrement numérique, sans papier ni e-mails manuels. AroundLink connecte
votre établissement à ce réseau : vos accords inter-établissements, contrats
pédagogiques, relevés de notes et nominations circulent directement de logiciel à
logiciel avec vos universités partenaires. Concrètement, un accord signé chez vous
apparaît chez le partenaire, une note saisie ici part vers l'université d'origine de
l'étudiant, et chaque changement notifie l'autre côté automatiquement.

!!! info "Vous êtes DSI / intégrateur ?"
    Cette page décrit la **valeur** de chaque brique. Pour la liste des endpoints,
    méthodes, versions d'API et les liens vers les spécifications officielles EWP,
    voir la [Référence des API EWP](reference-api.md).

## Découverte / Manifest

**À quoi ça sert.** Le manifest est la carte de visite numérique de votre
établissement sur le réseau EWP. Il indique à toutes les universités partenaires
quels services vous proposez et comment vous joindre de façon fiable. Sans lui,
aucun partenaire ne peut vous découvrir ni échanger quoi que ce soit avec vous.

**Pour qui.** <span class="al-audience">établissement partenaire / admin</span>

**Comment ça marche.** AroundLink publie et tient à jour ce manifest pour votre
établissement. Un partenaire (ou l'annuaire central du réseau) le consulte pour
savoir que vous savez échanger accords, contrats pédagogiques, relevés de notes et
nominations, puis établit une relation de confiance. Tout est automatique : vous
n'avez rien à publier manuellement.

**Cas d'usage.**
> Une université espagnole vous ajoute comme partenaire ; son logiciel lit votre
> manifest et découvre aussitôt qu'il peut vous envoyer un accord numérique.


## Echo

**À quoi ça sert.** Echo est un test de connectivité : il confirme que votre
établissement et un partenaire arrivent bien à se joindre et à s'authentifier
mutuellement. C'est l'outil de diagnostic utilisé au moment de brancher un nouveau
partenaire, avant que les vraies données ne circulent.

**Pour qui.** <span class="al-audience">établissement partenaire / admin</span>

**Comment ça marche.** Un appel de test renvoie exactement les informations
envoyées, accompagnées de l'identité vérifiée de l'appelant. Une réponse correcte
prouve que la liaison et la confiance entre les deux établissements fonctionnent.

**Cas d'usage.**
> Lors de l'intégration d'un partenaire, l'équipe envoie un appel Echo ; une réponse
> réussie confirme que la poignée de main de confiance est opérationnelle.


## Institutions

**À quoi ça sert.** Cette brique publie l'identité de base de votre établissement
(son nom officiel) à partir de son identifiant. Elle permet aux partenaires
d'afficher un nom lisible au lieu d'un code technique dans leurs écrans.

**Pour qui.** <span class="al-audience">établissement partenaire</span>

**Comment ça marche.** Un partenaire fournit un ou plusieurs identifiants
d'établissement et reçoit en retour les noms correspondants. Ses interfaces peuvent
alors présenter vos accords et mobilités avec un intitulé humain.

**Cas d'usage.**
> Un partenaire affiche « Institut Polytechnique des Sciences Avancées » à côté d'un
> accord entrant, plutôt que l'identifiant technique de l'établissement.


## Factsheet (fiche établissement)

La factsheet est la fiche pratique de votre établissement : dates de nomination et
de candidature, contacts logement / visa / assurance, accessibilité, délais de
décision et de relevé de notes. AroundLink couvre trois usages complémentaires.

### Publier votre factsheet

**À quoi ça sert.** Vous diffusez à tout le réseau vos informations pratiques, pour
que les partenaires renseignent leurs étudiants sortants sans avoir à vous écrire.

**Pour qui.** <span class="al-audience">établissement partenaire</span>

**Comment ça marche.** Dès qu'un partenaire demande votre fiche, AroundLink la
génère à partir des informations saisies par votre service et la renvoie dans un
format conforme au réseau.

**Cas d'usage.**
> Un partenaire consulte votre factsheet et voit vos dates limites de candidature
> sans avoir à envoyer un e-mail au bureau des relations internationales.

### Éditer votre factsheet

**À quoi ça sert.** Vous maintenez, depuis un simple formulaire, le contenu de la
fiche qui sera diffusée à l'ensemble de vos partenaires.

**Pour qui.** <span class="al-audience">gestionnaire RI</span>

**Comment ça marche.** Depuis l'écran dédié de votre espace, vous remplissez et
mettez à jour les rubriques de la fiche. Les champs mal renseignés (par exemple un
numéro de téléphone sans indicatif) sont signalés avant enregistrement.

**Cas d'usage.**
> Le gestionnaire RI met à jour les dates de nomination du semestre de printemps ;
> la nouvelle fiche est aussitôt disponible pour les partenaires.

### Récupérer la factsheet d'un partenaire

**À quoi ça sert.** Vous importez à la demande la fiche pratique d'un partenaire,
pour retrouver ses dates et contacts directement dans AroundLink au lieu de les
chercher ailleurs.

**Pour qui.** <span class="al-audience">gestionnaire RI</span>

**Comment ça marche.** Depuis la fiche d'un établissement partenaire, une action de
synchronisation va chercher sa factsheet sur le réseau et la stocke chez vous. Les
champs que vous avez verrouillés manuellement ne sont jamais écrasés ; si le
partenaire n'expose pas de fiche, vos données saisies à la main sont conservées.

**Cas d'usage.**
> Avant une campagne, le gestionnaire synchronise la factsheet d'un partenaire pour
> afficher ses délais de décision directement dans le dossier de l'accord.


## IIA — accords inter-établissements

L'échange d'accords inter-établissements (IIA) est la fonction phare : négocier,
comparer et signer des accords Erasmus+ bilatéraux sans papier, avec une copie
partagée entre les deux établissements. Cela correspond aux **accords** dans
AroundLink.

**À quoi ça sert.** Vous gérez tout le cycle de vie d'un accord — contenu,
conditions de mobilité, contacts, dates de signature — de façon numérique et
partagée avec le partenaire. Fini les versions PDF divergentes échangées par e-mail :
les deux côtés travaillent sur une même référence.

**Pour qui.** <span class="al-audience">gestionnaire RI / établissement partenaire</span>

**Comment ça marche.** Le partenaire peut lister et consulter les accords qu'il
partage avec vous. Chaque établissement approuve la version exacte qu'il a sous les
yeux ; quand les deux ont approuvé, l'accord est en vigueur. Toute modification d'un
côté notifie automatiquement l'autre, qui récupère la version fraîche.

**Cas d'usage.**
> Vous ajustez le nombre de places d'un accord ; le partenaire est notifié, récupère
> la nouvelle version, l'approuve, et l'accord bascule « en vigueur » des deux côtés.

### Notification de changement (CNR) et revue

**À quoi ça sert.** Lorsqu'un partenaire modifie un accord, vous êtes prévenu et
vous décidez champ par champ ce que vous acceptez, plutôt que de subir un écrasement
automatique. C'est le garde-fou qui protège l'intégrité de vos données.

**Pour qui.** <span class="al-audience">gestionnaire RI</span>

**Comment ça marche.** Une notification de changement déclenche la récupération de la
version du partenaire. AroundLink prépare une comparaison côte à côte et met la
proposition en attente de revue (jamais appliquée automatiquement) ; le coordinateur
est averti par e-mail. Il accepte les champs souhaités, l'accord repasse alors en
brouillon pour une nouvelle approbation, ou rejette sans toucher à ses données.

**Cas d'usage.**
> Un partenaire change une langue d'enseignement ; le coordinateur voit la
> différence, accepte cette seule modification et laisse le reste inchangé.


## OLA — contrats pédagogiques (Learning Agreements)

Échange et co-signature numériques des contrats pédagogiques (OLA) des étudiants que
vous envoyez en mobilité. Voir aussi la page [Learning Agreement](../etablissement/documents.md).

**À quoi ça sert.** Vous publiez les contrats pédagogiques de vos étudiants sortants
— cours suivis, cours reconnus au retour, signatures — pour que l'université
d'accueil les relise et les signe en ligne. L'aller-retour de validation se fait sans
papier.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur / établissement partenaire</span>

**Comment ça marche.** L'université d'accueil peut lister et récupérer les contrats
de vos étudiants, puis les approuver ou demander des modifications. À l'approbation,
sa signature est enregistrée ; quand les deux côtés ont signé, le contrat est
validé. Si le partenaire signale un changement de son côté, AroundLink récupère
automatiquement la version à jour.

**Cas d'usage.**
> L'université d'accueil approuve le contrat pédagogique d'un étudiant en ligne ; le
> statut passe à « validé » dans AroundLink et la reconnaissance est enclenchée.


## Transcript (ToR — relevé de notes)

Envoi numérique des relevés de notes des étudiants que vous **accueillez**, vers leur
université d'origine. Voir aussi [Transcript of Records](../etablissement/documents.md).

**À quoi ça sert.** Vous transmettez le relevé officiel (cours, notes, crédits ECTS,
réussite / échec) de vos étudiants entrants, pour que leur établissement d'origine
importe les résultats et accorde la reconnaissance sans relevé papier.

**Pour qui.** <span class="al-audience">coordinateur / établissement partenaire</span>

**Comment ça marche.** L'établissement d'origine peut lister et récupérer les relevés
de ses étudiants qui ont étudié chez vous. Le relevé est transmis dans un format
européen normalisé, prêt à être importé et reconnu automatiquement.

**Cas d'usage.**
> À l'issue des examens, le logiciel du partenaire récupère le relevé de son étudiant
> et reconnaît automatiquement les crédits obtenus.


## Nominations (mobilités sortantes)

Nomination numérique des étudiants que vous envoyez à un partenaire, et réception de
sa décision. Voir aussi [affectation](../etablissement/campagnes.md).

**À quoi ça sert.** Vous transmettez chaque nomination d'étudiant sortant (identité,
domaine d'études, niveau, accord de rattachement) pour que l'université d'accueil
l'accepte ou la refuse numériquement, avec un historique tracé de la décision.

**Pour qui.** <span class="al-audience">gestionnaire RI / établissement partenaire</span>

**Comment ça marche.** L'université d'accueil peut lister et consulter les
nominations que vous lui adressez, puis les approuver ou les rejeter. La décision
revient dans AroundLink et met à jour le statut de l'étudiant, avec la trace du
signataire ou du motif de refus.

**Cas d'usage.**
> Vous nommez une étudiante à Milan ; le bureau milanais approuve via le réseau et le
> statut de l'étudiante passe à « approuvé » dans AroundLink, avec le signataire.


## Fondations techniques

**À quoi ça sert.** Sous chaque échange se trouvent les mécanismes qui garantissent
que les données arrivent au bon partenaire, intactes et de source certifiée. Ils
sont invisibles pour l'utilisateur mais indispensables à la confiance du réseau.

**Pour qui.** <span class="al-audience">admin</span>

**Comment ça marche.** Chaque message échangé est signé et vérifié, de sorte que
chaque établissement sait avec certitude qui lui parle. Un annuaire central du réseau
permet de retrouver l'adresse et l'identité de chaque partenaire avant de lui
transmettre quoi que ce soit.

**Cas d'usage.**
> Avant d'envoyer un accord, AroundLink consulte l'annuaire pour localiser le
> partenaire et signe le message afin qu'il soit accepté comme authentique.

