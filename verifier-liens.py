#!/usr/bin/env python3
"""Chasse aux liens morts dans le site CONSTRUIT — pages, ancres, images.

    ./.venv/bin/mkdocs build -q -d /tmp/site && ./.venv/bin/python verifier-liens.py /tmp/site
    ./.venv/bin/python verifier-liens.py /tmp/site --externes   # interroge aussi le web

Pourquoi sur le site construit et pas sur les sources : c'est le HTML que lit le
client. Un lien juste dans le markdown peut casser à la construction — une ancre
générée autrement que prévu, un repli de langue qui pointe ailleurs, un `site_url`
absent qui envoie le sélecteur de langue à la racine du domaine (le bug du 05/11).

Avec `--externes`, chaque lien http(s) écrit DANS le contenu est aussi interrogé : la
documentation de l'API « démo » a répondu 404 pendant des semaines sans que rien ne le
signale. 401, 403 et 405 comptent pour vivants — la page existe, elle est protégée.

Rend zéro écart avant toute publication.
"""
from __future__ import annotations
import html
import pathlib
import re
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import unquote, urlsplit

ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
EXTERNES = "--externes" in sys.argv
SITE = pathlib.Path(ARGS[0] if ARGS else "/tmp/site").resolve()
# La page existe, elle demande seulement d'être connecté ou refuse la méthode.
VIVANTS = {401, 403, 405}
# Le préfixe sous lequel GitHub Pages sert le site : un lien absolu commençant par lui
# vise une page du site, pas la racine du domaine.
PREFIXE = "/aroundlink-product-docs/"

ids_cache: dict[pathlib.Path, set[str]] = {}


def ids_de(fichier: pathlib.Path) -> set[str]:
    if fichier not in ids_cache:
        t = fichier.read_text(encoding="utf-8", errors="replace")
        ids_cache[fichier] = set(re.findall(r'\sid="([^"]+)"', t))
    return ids_cache[fichier]


def cible(depuis: pathlib.Path, chemin: str) -> pathlib.Path | None:
    """Le fichier que sert ce lien, ou None s'il n'existe pas."""
    if chemin.startswith(PREFIXE):
        base = SITE / chemin[len(PREFIXE):]
    elif chemin.startswith("/"):
        return None  # racine du domaine : hors du site, c'est précisément le bug
    else:
        base = (depuis.parent / chemin)
    base = pathlib.Path(str(base))
    for essai in (base, base / "index.html"):
        try:
            r = essai.resolve()
        except OSError:
            continue
        if r.is_file():
            return r
    return None


def contenu(t: str) -> str:
    """Le corps de l'article seul : les liens du thème (polices, dépôt) ne sont pas les nôtres."""
    m = re.search(r'<article class="md-content__inner.*?</article>', t, re.S)
    return m.group(0) if m else ""


def statut(url: str) -> str | None:
    """None si le lien répond, sinon ce qui ne va pas."""
    for methode in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=methode, headers={"User-Agent": "verifier-liens/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=15):
                return None
        except urllib.error.HTTPError as e:
            if e.code in VIVANTS:
                return None
            if methode == "HEAD" and e.code in (400, 404, 501):
                continue  # certains serveurs refusent HEAD : on redemande en GET
            return f"HTTP {e.code}"
        except Exception as e:  # DNS, délai, certificat
            return type(e).__name__
    return "HTTP 404"


def main() -> int:
    ecarts = defaultdict(list)
    pages = sorted(SITE.rglob("*.html"))
    # Les copies figées d'exemple et les pages de redirection ne sont pas de la doc.
    pages = [p for p in pages if "/assets/exemples/" not in str(p)]
    externes: dict[str, set[str]] = defaultdict(set)
    for page in pages:
        t = page.read_text(encoding="utf-8", errors="replace")
        # On ne contrôle que le CONTENU et le sélecteur de langue — la navigation et le
        # pied de page sont générés par le thème et se vérifient d'eux-mêmes.
        if EXTERNES:
            for val in re.findall(r'\shref="(https?://[^"#]+)', contenu(t)):
                externes[html.unescape(val)].add(str(page.relative_to(SITE)))
        for attr, val in re.findall(r'\s(href|src)="([^"]+)"', t):
            val = html.unescape(val)
            if re.match(r"^(https?:|mailto:|tel:|javascript:|data:)", val):
                continue
            parts = urlsplit(val)
            chemin, ancre = unquote(parts.path), parts.fragment
            rel = page.relative_to(SITE)
            if chemin == "":
                f = page
            else:
                f = cible(page, chemin)
                if f is None:
                    ecarts["lien mort"].append(f"{rel}  →  {val}")
                    continue
            if ancre and f.suffix == ".html" and ancre not in ids_de(f):
                ecarts["ancre absente"].append(f"{rel}  →  {val}")
    if externes:
        with ThreadPoolExecutor(8) as pool:
            for url, err in zip(externes, pool.map(statut, externes)):
                if err:
                    pages_url = sorted(externes[url])
                    ecarts["lien externe mort"].append(
                        f"{url}  ({err}) — {pages_url[0]}" + (f" et {len(pages_url) - 1} autres" if len(pages_url) > 1 else ""))
        print(f"{len(externes)} liens externes interrogés")
    total = 0
    for nature, lignes in ecarts.items():
        uniques = sorted(set(lignes))
        total += len(uniques)
        print(f"\n=== {nature} : {len(uniques)} ===")
        for l in uniques[:60]:
            print("  " + l)
        if len(uniques) > 60:
            print(f"  … et {len(uniques) - 60} autres")
    print(f"\n{len(pages)} pages contrôlées · {total} écarts")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
