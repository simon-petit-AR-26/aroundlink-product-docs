"""Un index de recherche PAR LANGUE — sinon le français trouve de l'allemand.

LE BUG (relevé par Simon le 05/11). `mkdocs-static-i18n` empile volontairement les
pages des cinq langues dans UN SEUL `search/search_index.json` — 871 entrées dont 329
françaises. Material le charge depuis la racine du site quelle que soit la page : un
lecteur français qui tape « daten » voit « Sicherheit und Daten » en premier.

LE CORRECTIF, EN DEUX MORCEAUX :
1. ICI, après la construction : on découpe l'index par préfixe de langue. La racine ne
   garde que le français ; chaque autre langue reçoit le sien sous `<lang>/search/`.
   Les `location` restent relatives à la racine du site — c'est ainsi que Material
   construit les liens des résultats, quelle que soit la page.
2. Dans `overrides/main.html` : la page d'une langue redirige sa requête d'index vers
   le fichier de sa langue.

⚠️ L'ORDRE EST TOUT. i18n reconstruit les autres langues DEPUIS son propre
`on_post_build` (priorité -100), puis empile les cinq index en un seul. Avec la priorité
par défaut, ce hook passait AVANT et découpait l'index du seul français — ou, pendant les
constructions imbriquées, celui d'une seule langue, chaque passe écrasant la précédente.
D'où la priorité -200 : on passe après l'empilement. Et on ne découpe que si l'index
contient plusieurs langues — c'est le signe qu'il est complet.
"""
from __future__ import annotations

import json
import logging
import pathlib

from mkdocs.plugins import event_priority

log = logging.getLogger("mkdocs.hooks.search_par_langue")

# Les langues servies sous un préfixe. Le français est à la racine.
PREFIXEES = ("en", "es", "it", "de")


@event_priority(-200)
def on_post_build(config, **kwargs):
    site = pathlib.Path(config["site_dir"])
    racine = site / "search" / "search_index.json"
    if not racine.is_file():
        log.warning("Pas d'index de recherche à découper : %s", racine)
        return

    index = json.loads(racine.read_text(encoding="utf-8"))
    par_langue: dict[str, list] = {"fr": [], **{l: [] for l in PREFIXEES}}
    for doc in index.get("docs", []):
        tete = doc.get("location", "").split("/", 1)[0]
        par_langue[tete if tete in PREFIXEES else "fr"].append(doc)

    # Pendant les constructions imbriquées de i18n, l'index ne porte qu'une langue : il
    # n'est pas encore complet, on ne touche à rien.
    if sum(1 for docs in par_langue.values() if docs) < 2:
        return

    for langue, docs in par_langue.items():
        dest = racine if langue == "fr" else site / langue / "search" / "search_index.json"
        dest.parent.mkdir(parents=True, exist_ok=True)
        # Un seul racinisateur par index : la recherche allemande coupe les mots en
        # allemand, la française en français.
        config_index = {**index.get("config", {}), "lang": [langue]}
        dest.write_text(
            json.dumps({**index, "config": config_index, "docs": docs}, ensure_ascii=False),
            encoding="utf-8",
        )
        log.info("Index de recherche %s : %d entrées", langue, len(docs))
