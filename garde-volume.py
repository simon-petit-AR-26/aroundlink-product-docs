#!/usr/bin/env python3
"""Garde-fou : aucune page ne perd en silence une part de son texte.

    ./.venv/bin/python garde-volume.py            # contre origin/main
    ./.venv/bin/python garde-volume.py <réf-git>

Né du 05/11 : une expression régulière qui devait retirer un encadré de trois lignes a
emporté tout ce qui le suivait — huit sections de la Bourse, quatre des Partenaires — et
les autres contrôles sont restés verts, puisqu'un texte absent n'a ni lien mort ni jargon.

Une page qui perd plus de 10 % de ses mots (et au moins 150) est signalée. Si la coupe est voulue (une
page scindée en deux), le rapport le montre aussi : on le lit, on ne le fait pas taire.
"""
from __future__ import annotations

import pathlib
import subprocess
import sys

REF = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
# 10 % et 150 mots : la coupe des Partenaires faisait 16 % — un seuil au quart la laissait passer.
SEUIL, PLANCHER = 0.10, 150
DOCS = pathlib.Path(__file__).parent / "docs"


def mots(texte: str) -> int:
    return len(texte.split())


def main() -> int:
    liste = subprocess.run(["git", "ls-tree", "-r", "--name-only", REF, "docs"],
                           capture_output=True, text=True, check=True).stdout.split()
    alertes = []
    for chemin in (c for c in liste if c.endswith(".md")):
        avant = mots(subprocess.run(["git", "show", f"{REF}:{chemin}"],
                                    capture_output=True, text=True).stdout)
        fichier = DOCS.parent / chemin
        apres = mots(fichier.read_text(encoding="utf-8")) if fichier.exists() else 0
        if avant - apres >= PLANCHER and apres < avant * (1 - SEUIL):
            alertes.append(f"  {chemin} : {avant} → {apres} mots ({100 * (avant - apres) // avant} % perdus)")
    print(f"=== pages amputées depuis {REF} : {len(alertes)} ===")
    print("\n".join(alertes))
    return 1 if alertes else 0


if __name__ == "__main__":
    sys.exit(main())
