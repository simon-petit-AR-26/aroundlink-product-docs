#!/usr/bin/env python3
"""Relecture MÉCANIQUE des pages françaises — ce qui se repère sans lire le code.

    ./.venv/bin/python relire.py

Ne remplace pas la relecture contre le produit : elle débusque les défauts qui
reviennent, pour que la lecture humaine se concentre sur le fond.

Chaque règle est née d'un défaut réel trouvé dans cette doc.
"""
from __future__ import annotations

import pathlib
import re
import sys
from collections import defaultdict

DOCS = pathlib.Path(__file__).parent / "docs"

REGLES = {
    # Simon, 2026 : « fais pas le détail entre ce qui est payant et gratuit ».
    "gratuit / payant": r"\b(plans? (de mobilité )?payants?|plans? gratuits?|offres? (payante|gratuite)s?"
                        r"|comptes? (gratuit|payant)s?|établissements? (payant|gratuit)s?|Mobility (Paid|Free)"
                        r"|réservée?s? aux (plans|offres|comptes|établissements))\b",
    # Un seul document public : aucun nom de classe, de table, de route ni de ticket.
    "jargon interne": r"\b(AROUNDLINK-\d+|[A-Z][a-z]+(?:[A-Z][a-z]+){2,}(?:Controller|Service|Repository|Enum|Entity)?"
                      r"|[a-z]+_[a-z]+_[a-z_]+|/api/[a-z]|Twig|Doctrine|Symfony|PostgreSQL|back-office)\b",
    # Une doc qui promet le futur ment le jour où le futur arrive autrement.
    "promesse datée": r"\b(bientôt|prochainement|à venir|dans une prochaine version|en cours de développement"
                      r"|sera disponible|feuille de route)\b",
    # Formulations du premier jet, avant la refonte de ton du 31/08.
    "ton de notice": r"\b(Ce module permet|Le module \w+ permet|Cette fonctionnalité permet|Page centrale listant"
                     r"|permet de gérer|Cette vue permet)\b",
    # Faits connus pour avoir changé — à relire contre le code à chaque passage.
    "fait daté": r"(le lendemain (de son|du) dernier jour|clôt d'elle-même|neuf types|séquences? d'onboarding"
                 r"|case « Active »|Google Workspace.{0,20}feuille)",
}

# Exceptions VOULUES : un faux positif qu'on laisse revenir finit par faire ignorer le rapport.
# - « cadenas » a été retiré des règles : il désigne aussi le verrou de synchronisation EWP et
#   les villes cloisonnées d'un partenaire, sans rapport avec une offre.
# - La page Architecture s'adresse aux DSI : nommer ses technologies est son objet.
# - « à venir » est aussi un libellé de l'agenda (« en retard / à venir / passé »).
IGNORER = {
    ("jargon interne", "plateforme/architecture.fr.md"),
    # La seule feuille de route assumée : SAML / Shibboleth, sans date. Les DSI la demandent.
    ("promesse datée", "plateforme/sso.fr.md"),
}
IGNORER_MOTIF = {
    "promesse datée": r"\*\*à venir\*\*|en retard, à venir|Shibboleth|eduGAIN|SAML",
}

# La terminologie doit être UNE : le même objet sous trois noms fait croire à trois objets.
SYNONYMES = {
    "contrat d'études / contrat pédagogique / Learning Agreement": [
        r"contrats? d'études", r"contrats? pédagogiques?", r"Learning Agreements?"],
    "relevé de notes / Transcript of Records": [r"relevés? de notes", r"Transcript of Records"],
    "établissement d'accueil / partenaire d'accueil": [r"établissements? d'accueil", r"partenaires? d'accueil"],
}


def main() -> int:
    pages = sorted(DOCS.rglob("*.fr.md"))
    trouves = defaultdict(list)
    for p in pages:
        rel = p.relative_to(DOCS)
        for n, ligne in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if ligne.startswith(("![", "    ```")):
                continue
            for regle, motif in REGLES.items():
                if (regle, str(rel)) in IGNORER:
                    continue
                if regle in IGNORER_MOTIF and re.search(IGNORER_MOTIF[regle], ligne):
                    continue
                for m in re.finditer(motif, ligne, re.I if regle != "jargon interne" else 0):
                    extrait = ligne[max(0, m.start() - 35): m.end() + 35].strip()
                    trouves[regle].append(f"{rel}:{n}  …{extrait}…")
    total = 0
    for regle, lignes in trouves.items():
        total += len(lignes)
        print(f"\n=== {regle} : {len(lignes)} ===")
        for l in lignes[:40]:
            print("  " + l)
        if len(lignes) > 40:
            print(f"  … et {len(lignes) - 40} autres")
    print("\n=== TERMINOLOGIE (occurrences par forme) ===")
    corpus = "\n".join(p.read_text(encoding="utf-8") for p in pages)
    for objet, formes in SYNONYMES.items():
        compte = {f: len(re.findall(f, corpus, re.I)) for f in formes}
        print(f"  {objet} :", " · ".join(f"{re.sub(r'[^a-zA-Zéè ]', '', f)} {c}" for f, c in compte.items()))
    print(f"\n{len(pages)} pages · {total} points à relire")
    return 0


if __name__ == "__main__":
    sys.exit(main())
