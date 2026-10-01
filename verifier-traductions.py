#!/usr/bin/env python3
"""Contrôle mécanique des traductions — ce qu'on peut vérifier sans parler la langue.

    ./.venv/bin/python verifier-traductions.py

Une traduction peut être belle et fausse. Ce script ne juge pas le style : il vérifie
que chaque version dit la MÊME CHOSE au même endroit — mêmes sections, mêmes tableaux,
mêmes encadrés, mêmes images, mêmes liens, mêmes chiffres. C'est là que se logent les
erreurs qui comptent : un encadré d'avertissement oublié, un lien qui ne pointe plus au
bon endroit, un « 24 heures » devenu « 48 ».
"""

import re
import sys
from pathlib import Path

DOCS = Path(__file__).parent / "docs"
LANGUES = ["en", "es", "it", "de"]


def empreinte(texte: str) -> dict:
    """Ce qui doit se retrouver à l'identique d'une langue à l'autre."""
    return {
        "sections": len(re.findall(r"^## ", texte, re.M)),
        "sous-sections": len(re.findall(r"^### ", texte, re.M)),
        "tableaux": len(re.findall(r"^\|", texte, re.M)),
        "encadrés": len(re.findall(r"^!!!|^\?\?\?", texte, re.M)),
        "images": sorted(re.findall(r"!\[[^\]]*\]\(([^)]+)\)", texte)),
        "liens internes": sorted(set(re.findall(r"\]\((?!https?:)([^)#]+\.md)", texte))),
        "liens externes": sorted(set(re.findall(r"\]\((https?://[^)]+)\)", texte))),
        # Les séparateurs de milliers changent selon la langue (12 000 / 12,000 /
        # 12.000) : on les retire pour ne comparer que les valeurs elles-mêmes.
        "nombres": sorted({re.sub(r"[\s\u202f,.]", "", n)
                           for n in re.findall(r"\d[\d\s\u202f,.]*\d|\d", texte)}),
    }


def main() -> int:
    pages = sorted(DOCS.rglob("*.fr.md"))
    soucis = manquantes = 0

    for fr in pages:
        base = str(fr)[: -len(".fr.md")]
        ref = empreinte(fr.read_text(encoding="utf-8"))
        for lang in LANGUES:
            autre = Path(f"{base}.{lang}.md")
            if not autre.exists():
                manquantes += 1
                continue
            got = empreinte(autre.read_text(encoding="utf-8"))
            ecarts = [
                f"{clef} : fr={ref[clef]} {lang}={got[clef]}"
                for clef in ref
                if ref[clef] != got[clef]
            ]
            if ecarts:
                soucis += 1
                print(f"\n{autre.relative_to(DOCS)}")
                for e in ecarts:
                    print(f"    {e}")

    print(f"\n{len(pages)} pages × {len(LANGUES)} langues")
    print(f"{manquantes} traductions manquantes · {soucis} pages avec un écart de structure")
    return 1 if soucis else 0


if __name__ == "__main__":
    sys.exit(main())
