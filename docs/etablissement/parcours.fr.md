# Parcours de mobilité

Un **parcours** est la liste de ce qu'un étudiant doit faire pendant sa mobilité. Vous le
composez une fois, puis vous l'appliquez à un groupe d'étudiants : chacun le suit à son
rythme, et vous voyez où en est tout le monde.

Il remplace la notion de séquence d'onboarding : un même atelier sert désormais aux
étudiants que vous envoyez **et** à ceux que vous accueillez.

!!! info "Où ça se passe"
    **Paramètres ▸ Workflows** pour fabriquer un parcours. On le **branche** ailleurs : sur
    une campagne pour les sortants, sur une session d'accueil pour les entrants. Un parcours
    qui n'est branché nulle part ne fait rien.

## Un parcours par sens de mobilité

**À quoi ça sert.** Partir et accueillir ne demandent pas les mêmes pièces. Le sens est
choisi à la création et ne change plus : il décide des endroits où le parcours pourra
servir.

**Pour qui.** <span class="al-audience">gestionnaire RI / coordinateur</span>

**Comment ça marche.**

| Sens | Pour qui | Ce qu'on y met d'habitude |
|---|---|---|
| **Outgoing** | les étudiants que vous envoyez | du oui du partenaire au retour : pièce d'identité, assurance, contrat d'études, attestations d'arrivée et de départ, relevé de notes |
| **Incoming** | les étudiants que vous accueillez | de l'arrivée au relevé : vérification des informations, pièces, charte, choix du campus et des cours, avis |

Deux mécaniques ne valent que pour un sens, et l'écran le dit avant que vous ne l'appreniez
en vous faisant refuser l'étape :

- **Choisir son campus** n'existe qu'en accueil — c'est l'établissement d'accueil qui a
  plusieurs sites ;
- **Choisir ses cours** aussi — il lit le catalogue de l'hôte et alimente le relevé de
  l'entrant. Pour un étudiant que vous envoyez, l'équivalent est le contrat d'études, qui
  vit dans son propre module.

!!! tip "Partez d'un parcours existant"
    L'icône de copie sur chaque ligne duplique un parcours sous un nouveau nom. C'est plus
    rapide que la page blanche, et deux parcours proches restent comparables.

## Brancher le parcours

**À quoi ça sert.** Un parcours seul ne démarre rien. Il se met en route quand vous
l'attachez à un groupe.

**Comment ça marche.**

- **Sortants** — ouvrez une campagne, **Edit**, onglet des réglages, champ **Mobility
  workflow**. Chaque étudiant accepté par un partenaire reçoit alors le parcours
  automatiquement. Le champ est facultatif : vous pouvez brancher plus tard depuis l'onglet
  **Mobility** de la campagne.
- **Entrants** — sous **Onboarding**, créez une **session d'accueil**, nommez-la, choisissez
  son parcours. Quand vous acceptez une nomination, vous désignez la session que l'étudiant
  rejoint.

Un même parcours peut servir plusieurs campagnes ou sessions. La colonne **Used by** de la
liste dit combien.

!!! warning "Modifier une étape atteint ceux qui sont déjà en route"
    Un parcours en service n'est pas figé : un changement d'étape rejoint tous les étudiants
    qui le suivent déjà. Regardez la colonne **Used by** avant de toucher à une étape, et la
    colonne **Students** pour savoir combien de dossiers sont concernés.

!!! note "Changer le parcours d'une campagne se confirme"
    Le remplacement se fait depuis l'écran qu'il gouverne, et demande une confirmation : les
    étudiants en cours basculent sur le nouveau parcours.

## Ce qu'une étape peut demander

**À quoi ça sert.** Chaque étape porte **un type d'action**, qui décide qui agit et ce qui
fait passer l'étudiant à la suite.

**Comment ça marche.** Le catalogue est **fermé**, et c'est voulu : chaque type branche une
fonction qui existe déjà dans l'outil — un type de document, un modèle, le catalogue de
cours, la file de validation. Une étape n'est donc jamais un champ de texte libre : le
parcours **ordonne des fonctions existantes** et les rend obligatoires au bon moment.

| Type d'étape | Disponible pour | Qui agit | Ce qui fait avancer |
|---|---|---|---|
| **Complete profile** | les deux sens | l'étudiant | il a rempli les champs que vous avez désignés, vérifié le reste et confirmé que ses informations sont exactes |
| **Deposit documents** | les deux sens | l'étudiant | toutes les pièces demandées sont déposées |
| **Request a language test** | les deux sens | l'étudiant | le test demandé est fourni, certificat **et** scores |
| **Generate a document** | les deux sens | personne — automatique | la plateforme produit le document ; l'étudiant confirme l'avoir lu et téléchargé |
| **Generate, then collect signed** | les deux sens | l'étudiant | il rend signé le document émis par la plateforme |
| **Choose campus** | accueil seulement | l'étudiant | il a choisi l'un de vos campus |
| **Read and accept** | les deux sens | l'étudiant | il coche avoir lu et accepté — le texte accepté est conservé **tel qu'il était ce jour-là** |
| **Choose courses** | accueil seulement | l'étudiant | il a rendu sa sélection de cours |
| **Give feedback** | les deux sens | l'étudiant | il écrit son avis, vous le modérez dans la file de validation : accepté sur tous les thèmes demandés, l'étape se ferme ; refusé, elle repart en réécriture |
| **Mirror something done elsewhere** | les deux sens | personne — reflet | voir ci-dessous |

!!! note "Un test de langue n'est pas un document comme un autre"
    Vous listez les tests acceptés — IELTS, TOEFL iBT, Duolingo — et **l'un d'eux suffit**.
    Ce qui est attendu n'est pas seulement un PDF scanné, mais le résultat structuré : type
    de test, score global, les quatre compétences, le niveau européen. C'est ce qui vous
    permet de décider.

!!! tip "La date cible ne bloque rien"
    Chaque étape peut porter une date indicative. Elle guide l'étudiant, rien de plus :
    rendre après ne bloque pas l'étape. Laissez-la vide si vous n'en voulez pas.

## Les étapes qui se cochent toutes seules

**À quoi ça sert.** La plupart des étapes d'un parcours ne sont pas des choses que l'on fait
*dans* le parcours. Elles **surveillent un objet qui existe déjà ailleurs** dans AroundLink
— un contrat d'études signé, un document validé, un versement de bourse — et se cochent
d'elles-mêmes quand il change. Elles se décochent aussi, si l'objet revient en arrière.

**Comment ça marche.** C'est pour cela qu'on ne peut pas les cocher à la main, et qu'elles
n'apparaissent pas dans la liste des types quand vous ajoutez une étape : **c'est la
plateforme qui les pose**, avec l'objet qu'elles observent. Les parcours livrés avec
AroundLink en contiennent déjà — « contrat d'études signé par les trois parties »,
« confirmation d'arrivée », « relevé validé ».

!!! info "Un reflet ne recopie rien"
    L'étape ne duplique pas la donnée : elle lit l'objet d'origine. Il n'y a donc jamais deux
    versions d'un même fait, et une signature retirée fait repasser l'étape en attente.

## Ordonner, replier, archiver

**Comment ça marche.** Les étapes se réorganisent **en les glissant** d'un encart à l'autre,
et chaque étape déclare la **phase** à laquelle elle appartient — avant, pendant ou après la
mobilité. C'est cette phase qui alimente le [suivi des mobilités](suivi-mobilites.md).

La liste des parcours se trie et se filtre. Sa colonne **State** parle : *With steps*, *With
students*, *Not in use*, *Inactive*. Un parcours dont vous ne voulez plus se range dans les
archives — **Archive**, puis **View archived workflows** pour le retrouver et le restaurer.

**Cas d'usage.**
> L'école compose deux parcours : un sortant en neuf étapes, un entrant en sept. Le sortant
> est branché sur la campagne de l'année ; l'entrant sur la session « Autumn 2026 intake ».
> Les quatre étapes de contrat d'études et de relevé sont des reflets : personne ne les
> coche, elles suivent les documents. La coordinatrice ne surveille donc que les cinq étapes
> qui demandent vraiment quelque chose.
