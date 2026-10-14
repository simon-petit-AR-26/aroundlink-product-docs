# Emails &amp; connecteurs

Les échanges avec vos partenaires vivent dans votre messagerie, et le dossier de l'étudiant
vit dans AroundLink. Les **emails classés** rapprochent les deux : un message échangé avec un
contact se retrouve sur sa fiche, sans que personne n'ait à le recopier.

!!! info "Où ça se passe"
    **Paramètres ▸ Connectors** rassemble les trois branchements : **Email**, **Calendar** et
    **API**. Les messages classés se lisent ensuite sur les fiches — partenaire, contact,
    étudiant.

## Classer ses emails sans quitter Outlook

**À quoi ça sert.** Retrouver, six mois plus tard, ce qui a été dit à un partenaire — sans
chercher dans la boîte d'un collègue parti en vacances.

**Pour qui.** <span class="al-audience">toute l'équipe mobilité</span>

**Comment ça marche.** Un **add-in Outlook** classe les emails que vous échangez avec vos
contacts sur la bonne fiche, depuis votre messagerie. Un message n'est classé que s'il est
**authentifié** et s'il concerne un **contact déjà présent dans AroundLink** ; tout le reste
est lu puis oublié.

L'installation se fait en six étapes, données directement sur la page — Microsoft ne permet
l'ajout d'un add-in que depuis une page enfouie de son propre site, et la seconde moitié du
guide (où cliquer dans Outlook une fois l'add-in posé) ne figure dans aucune documentation
Microsoft. Chaque étape délicate porte sa capture d'écran.

1. télécharger le fichier de l'add-in — un seul fichier, à garder jusqu'à l'étape 3 ;
2. ouvrir ses add-ins Outlook, colonne de gauche, **My add-ins** ;
3. dans **Custom add-ins**, **Add a custom add-in**, puis **Add from file** ;
4. ouvrir un email, puis le bouton **Apps** de la barre du message ;
5. choisir **AroundLink for Outlook** dans la liste ;
6. épingler le volet, pour qu'il reste ouvert d'un message au suivant.

!!! tip "Sans l'add-in : l'adresse en copie"
    Si l'add-in n'est pas une option, mettez l'**adresse de votre établissement** en copie
    quand vous écrivez à un contact : le message atterrit sur sa fiche. Elle se copie d'un
    bouton depuis la page Connectors. C'est un repli, pas la solution : il faut y penser à
    chaque message, et c'est exactement la raison d'être de l'add-in.

## Lire les échanges sur une fiche

**À quoi ça sert.** Voir l'historique d'une relation à l'endroit où l'on travaille.

**Comment ça marche.** Les messages classés apparaissent **à l'identique sur trois écrans** :
la fiche d'un partenaire (l'agrégat des emails de ses contacts), la fiche d'un contact, et la
fiche d'un étudiant.

- une **carte par message**, une seule ouverte à la fois ;
- le sens de l'échange est marqué — reçu ou envoyé ;
- les **noms sont des liens** quand la personne est répertoriée chez vous ; une adresse
  inconnue reste du texte, ce qui est la vérité ;
- les pièces jointes se téléchargent depuis la carte ;
- **Reply** et **Forward** ouvrent votre messagerie avec le message cité.

Sur la fiche d'un étudiant, les emails sont rapprochés de ses adresses — celle de l'école et
la personnelle. La liste y est **en lecture seule** : un message se gère depuis la fiche du
contact qui le porte.

Dans les grilles de contacts, une colonne **Last contact** donne la date du dernier échange.

!!! warning "Rien ne s'y supprime"
    Les écrans d'emails ne portent aucun geste destructeur. Un message classé par erreur se
    traite côté administration, pas depuis une fiche — un historique de relation qu'un clic
    pourrait vider ne serait pas un historique.

## Le calendrier et l'API

**Comment ça marche.** Les deux autres branchements vivent au même endroit.

- **Calendar** — lire votre [agenda](agenda.md) AroundLink depuis Outlook, Google Agenda ou
  Apple Calendrier. Le lien porte tout votre agenda et ne va **que dans un sens** : votre
  calendrier vient lire, il ne modifie rien.
- **API** — laisser vos propres systèmes lire et écrire des données AroundLink. Ce
  branchement est destiné à la DSI de votre établissement. **La clé est personnelle, pas
  celle de l'établissement** : chacun a la sienne, et la régénérer laisse celle d'un collègue
  fonctionner.

**Cas d'usage.**
> La responsable écrit à son homologue de Bologne pour caler les dates du semestre. Le volet
> AroundLink est épinglé dans son Outlook : le message se classe sur la fiche du contact. Trois
> mois plus tard, sa collègue ouvre la fiche du partenaire, lit l'échange, et répond depuis la
> carte sans chercher dans sa propre boîte.
