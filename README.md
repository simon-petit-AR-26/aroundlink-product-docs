# Documentation produit AroundLink — guide de maintenance

Ce dossier contient la **documentation produit** d'AroundLink : une fiche par
fonctionnalité, orientée valeur métier, en **français et anglais**. Elle est
construite avec [MkDocs](https://www.mkdocs.org/) + le thème
[Material](https://squidfunk.github.io/mkdocs-material/) et publiée sur GitHub
Pages.

> ⚠️ **Le site est public.** Ne jamais écrire de secret (identifiants, clés, mots
> de passe), ni de bug/roadmap confidentiel, même dans les blocs « Détails
> internes ».

## 1. Modifier le contenu (sans coder)

Tout le contenu vit dans des fichiers texte `.md` (Markdown), un fichier **par
module**, rangés dans `docs/`. Pour chaque page, il y a deux fichiers :

- `nom-de-page.fr.md` → version française
- `nom-de-page.en.md` → version anglaise

Exemple : la page « Bourse de mobilité » = `docs/etablissement/bourse.fr.md` et
`docs/etablissement/bourse.en.md`.

**Pour corriger un texte** : ouvrez le fichier `.md` concerné, modifiez la phrase,
enregistrez. C'est tout. (Pensez à répercuter la correction dans la version de
l'autre langue.)

### Le format d'une fiche

Chaque fonctionnalité suit toujours le même gabarit :

```markdown
## Nom de la fonctionnalité

**À quoi ça sert.** Ce que ça apporte, en langage client (2–3 phrases).

**Pour qui.** gestionnaire RI · étudiant …{ .al-audience }

**Comment ça marche.** Le fonctionnement au niveau produit (2–4 phrases).

**Cas d'usage.**
> Un exemple concret et parlant.

??? note "Détails internes (équipe AroundLink)"
    Notes pour l'équipe (non sensibles). Repliées par défaut.
```

Pour **ajouter une fonctionnalité**, copiez ce bloc dans la bonne page et
remplissez-le. Pour **ajouter une page entière**, créez `docs/…/ma-page.fr.md` (+
`.en.md`) puis ajoutez-la à la navigation dans `mkdocs.yml` (section `nav:`).

Le fil `{ .al-audience }` après « Pour qui » n'est pas obligatoire — il affiche
juste le rôle sous forme d'étiquette. Les titres du menu en anglais se règlent dans
`mkdocs.yml` (bloc `nav_translations`).

## 2. Prévisualiser en local

Une fois (première installation) :

```bash
cd product-docs
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Ensuite, à chaque fois que vous voulez voir le rendu :

```bash
cd product-docs
source .venv/bin/activate
mkdocs serve
```

Ouvrez ensuite <http://127.0.0.1:8000> dans un navigateur. La page se recharge
automatiquement à chaque enregistrement d'un fichier `.md`.

## 3. Republier le site en ligne

Après vos modifications, une seule commande met à jour le site public :

```bash
cd product-docs
source .venv/bin/activate
mkdocs gh-deploy --force
```

Cela reconstruit le site et le pousse sur la branche `gh-pages` du dépôt. GitHub
Pages met le site à jour en 1–2 minutes.

## Structure du dossier

```
product-docs/
├── mkdocs.yml           ← configuration + navigation (menu)
├── requirements.txt     ← dépendances (mkdocs-material, i18n)
├── README.md            ← ce guide
└── docs/
    ├── index.fr.md / index.en.md      ← page d'accueil
    ├── assets/                         ← logo, feuille de style (couleurs)
    ├── etablissement/  ← espace gestionnaire RI (9 pages)
    ├── etudiant/       ← espace étudiant (2 pages)
    ├── atlas/          ← annuaire mondial
    ├── ewp/            ← réseau EWP
    ├── plateforme/     ← plateforme & sécurité
    └── annexes/        ← glossaire
```

> Note : `A-CONFIRMER.md` (à la racine de `product-docs/`) liste les points à
> clarifier avec l'équipe produit. Il n'est **pas** publié sur le site.
