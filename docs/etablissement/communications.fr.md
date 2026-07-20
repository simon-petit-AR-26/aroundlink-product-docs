# Communications & notifications

Ce module regroupe tout ce qui touche à la communication du bureau des relations
internationales : diffuser un message à une audience ciblée, notifier en temps
réel, échanger en direct avec un étudiant ou un partenaire, et relancer
automatiquement les documents manquants. L'objectif : remplacer les envois manuels
dispersés par des outils intégrés et suivis.

## Diffusion de messages

**À quoi ça sert.** Vous rédigez un message une seule fois et le diffusez sur
plusieurs canaux — notification dans l'application, e-mail, épinglage au tableau de
bord, message direct — vers des audiences ciblées. Fini le publipostage manuel :
vous ciblez, vous envoyez, et vous gardez une trace.

**Pour qui.** <span class="al-audience">coordinateur / gestionnaire RI</span>

**Comment ça marche.** Le compositeur vous laisse choisir les audiences (étudiants
sortants, étudiants entrants, partenaires) et des filtres optionnels (pays, campus,
statut d'accès de l'étudiant), avec un compteur de destinataires en direct avant
l'envoi. Vous sélectionnez les canaux souhaités, vous pouvez enregistrer un
brouillon, et un message envoyé est verrouillé. À l'envoi, un récapitulatif indique
le nombre de destinataires, d'e-mails partis et de messages épinglés. Un message
épinglé peut ensuite être retiré du tableau de bord.

**Cas d'usage.**
> Un coordinateur envoie « Date limite de nomination reportée au 15 mars » à tous
> les étudiants sortants en Espagne, épinglé sur leur tableau de bord et envoyé
> par e-mail.

??? note "Détails internes (équipe AroundLink)"
    Audiences : `outgoing_students` / `incoming_students` / `partners`. Canaux :
    in_app / email / dashboard_pin / direct_message. La livraison e-mail est
    suivie par destinataire (statut file d'attente / envoyé / ouvert / cliqué /
    rejeté). Le compositeur avertit avant de remplacer un épinglage existant.
    Propriété vérifiée avant édition / suppression / désépinglage ; un message
    envoyé n'est plus modifiable. Contrôleur : `CommunicationController`,
    entités `Communication` / `CommunicationEmailLog`. AROUNDLINK-509.

## Notifications dans l'application

**À quoi ça sert.** Chaque utilisateur dispose d'un fil de notifications avec un
compteur de non-lus en direct dans la barre supérieure. Coordinateurs, partenaires
et étudiants restent informés des nouveaux messages et événements sans dépendre de
l'e-mail.

**Pour qui.** <span class="al-audience">coordinateur / partenaire / étudiant</span>

**Comment ça marche.** La cloche affiche le nombre de notifications non lues ;
ouvrir une notification la marque comme lue, et un bouton permet de tout marquer
lu d'un coup. Une notification peut renvoyer vers le message d'origine.

**Cas d'usage.**
> Un étudiant voit un « 3 » sur la cloche, l'ouvre et découvre que son Learning
> Agreement vient d'être approuvé.

??? note "Détails internes (équipe AroundLink)"
    Fil d'historique + endpoint de comptage interrogé par la cloche + lecture à
    l'ouverture + « tout marquer lu ». L'entité `Notification` peut être liée à une
    `Communication`. Contrôleurs : `NotificationController` (mobilité) et
    `StudentNotificationController` (étudiant). AROUNDLINK-509 / -511.

## Messagerie directe

**À quoi ça sert.** Une messagerie privée en fil de discussion entre les trois
types d'acteurs — équipe RI, étudiants, équipe AroundLink. Les questions se
règlent dans la plateforme plutôt que par e-mails éparpillés.

**Pour qui.** <span class="al-audience">coordinateur / étudiant / partenaire</span>

**Comment ça marche.** Chaque profil a sa propre boîte de réception : liste des
conversations, fil un-à-un avec lecture à l'ouverture, réponse, et un sélecteur
« nouveau message » pour démarrer un échange. Un compteur de non-lus s'affiche dans
la barre supérieure.

**Cas d'usage.**
> Un étudiant entrant écrit au bureau d'accueil pour poser une question sur le
> logement ; le coordinateur répond dans le fil.

??? note "Détails internes (équipe AroundLink)"
    Entités partagées `Conversation` / `Message` et mêmes gabarits entre les trois
    contrôleurs (`MessageController` côté mobilité, admin et étudiant). Identifiants
    de fil au format UUID. AROUNDLINK-147.

## Campagnes de relance de documents

**À quoi ça sert.** Des campagnes d'e-mails de relance automatisées et suivies
poussent les étudiants à déposer leurs documents manquants, avec des statistiques
d'ouverture, de clic et de rejet par campagne. La chasse aux documents devient une
opération mesurable en un clic.

**Pour qui.** <span class="al-audience">coordinateur / gestionnaire RI</span>

**Comment ça marche.** Une campagne cible les étudiants par type de document,
niveau d'études et campagnes associées. La liste des campagnes et une fenêtre de
statistiques affichent le nombre d'envois, le taux d'ouverture, le taux de clic et
le taux de délivrabilité. Les e-mails partent ensuite automatiquement en tâche de
fond.

**Cas d'usage.**
> Un coordinateur lance une relance pour tous les étudiants de Master à qui il
> manque le Learning Agreement, puis vérifie un taux d'ouverture de 62 % dans la
> fenêtre de statistiques.

!!! tip "Depuis les campagnes"
    Les relances se déclenchent aussi depuis le suivi des documents d'une
    [campagne](../etablissement/campagnes.md) : c'est la même mécanique de relance
    documentée ici.

??? note "Détails internes (équipe AroundLink)"
    Une `ReminderLine` par étudiant trace envoi / ouverture / clic / rejet. Envoi
    asynchrone via la commande `reminder-campaigns:send-pending-emails` (traite les
    lignes dont `sentAt IS NULL`). Suivi d'ouverture/clic/rejet mis à jour côté
    fournisseur d'e-mail. Contrôleur : `ReminderCampaignController` ; création via
    `CreateReminderCampaign` depuis le suivi des documents étudiants.
