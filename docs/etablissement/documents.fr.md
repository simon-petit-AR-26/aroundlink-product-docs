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

![Hub de validation](../assets/screenshots/validations-hub.png)

*Tout ce qui attend votre décision, avec le nombre d'éléments en retard et les filtres par nature de pièce.*

![Choix des types de documents demandés](../assets/screenshots/parametres-types-documents.png)

*Les pièces que votre établissement demande, par famille. Désactiver un type le retire du profil de l'étudiant sans supprimer ce qui a déjà été déposé.*

![Modèles de documents](../assets/screenshots/parametres-modeles-documents.png)

*Vos modèles de documents générés — lettre d'acceptation, attestation de scolarité, contrat pédagogique, relevé — dans lesquels les informations de l'étudiant viennent se substituer aux variables.*

**Cas d'usage.**
> Le coordinateur relit l'OLA de départ de Marie (3 cours, 18 ECTS), lui demande de
> remplacer un cours, puis signe au nom de l'établissement d'envoi ; dès que le
> partenaire signe à son tour, l'OLA passe « Validé ».


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

