#!/usr/bin/env python3
"""Uso: python3 definir_dominio.py https://meusite.com   (sem barra no fim)"""
import sys, pathlib
if len(sys.argv) != 2 or not sys.argv[1].startswith("http"):
    sys.exit("Uso: python3 definir_dominio.py https://meusite.com")
base = sys.argv[1].rstrip("/")
host = base.split("://", 1)[1]
n = 0
for f in ["index.html", "robots.txt", "sitemap.xml"]:
    p = pathlib.Path(f); t = p.read_text(encoding="utf-8")
    if "SEU-DOMINIO" in t:
        p.write_text(t.replace("https://SEU-DOMINIO", base).replace("SEU-DOMINIO", host), encoding="utf-8"); n += 1
print(f"Pronto: domínio definido como {base} em {n} ficheiro(s).")
