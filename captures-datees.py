#!/usr/bin/env python3
"""L'âge de chaque capture d'écran publiée — Simon, 05/11 : « il faut que tu aies la date des
screens ». Une capture périmée montre un écran qui n'existe plus : le lecteur le cherche en vain.

    ./.venv/bin/python captures-datees.py [jours]      # 60 par défaut

La date est celle du dernier remplacement de l'image dans le dépôt. Le script informe et ne
bloque pas la publication : refaire une capture demande l'écran, pas le code.
"""
from __future__ import annotations

import datetime as dt
import pathlib
import re
import subprocess
import sys

RACINE = pathlib.Path(__file__).parent
DOCS = RACINE / "docs"
IMAGES = DOCS / "assets/screenshots"


def main() -> int:
    seuil = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    usage: dict[str, list[str]] = {}
    for p in sorted(DOCS.rglob("*.fr.md")):
        for nom in re.findall(r"assets/screenshots/([\w.-]+\.png)", p.read_text(encoding="utf-8")):
            usage.setdefault(nom, []).append(str(p.relative_to(DOCS)).removesuffix(".fr.md"))
    aujourdhui = dt.date.today()
    lignes = []
    for img in sorted(IMAGES.glob("*.png")):
        date = subprocess.run(
            ["git", "log", "-1", "--format=%as", "--", str(img)], cwd=RACINE, capture_output=True, text=True
        ).stdout.strip()
        jour = dt.date.fromisoformat(date) if date else aujourdhui
        lignes.append(((aujourdhui - jour).days, jour, img.name, usage.get(img.name)))
    perimees = [l for l in lignes if l[3] and l[0] > seuil]
    print(f"=== captures publiées de plus de {seuil} jours : {len(perimees)} ===")
    for age, jour, nom, pages in sorted(perimees, reverse=True):
        print(f"  {jour:%d/%m/%Y}  ({age} j)  {nom}  → {', '.join(pages)}")
    inutiles = [l for l in lignes if not l[3]]
    if inutiles:
        print(f"\n=== images que plus aucune page n'affiche : {len(inutiles)} ===")
        for _, jour, nom, _ in inutiles:
            print(f"  {jour:%d/%m/%Y}  {nom}")
    print(f"\n{sum(1 for l in lignes if l[3])} captures publiées · {len(perimees)} à refaire")
    return 0


if __name__ == "__main__":
    sys.exit(main())
