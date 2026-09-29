---
name: gemma-archimate-model-gemma-release
description: Verwerk een nieuwe versie van het GEMMA-architectuurmodel in gemma-archimate-model — de AMEFF-export ophalen (of een lokaal .archimate-bestand gebruiken), als bron opnemen, parsen en de gemma_*-velden van bestaande elementen via een run bijwerken. Gebruik alleen bij een nieuwe GEMMA-modelversie.
metadata:
  kind: capability
  scope: wiki
  requires-skills: "wiki-update"
  requires-tools: "llmwiki python:tools/gemma.py"
---

# Nieuwe versie van het GEMMA-model

Het GEMMA-model is een matchdoel (brontype `model`), geen bron voor begrippen. Standaard gebruiken we de ArchiMate Open Exchange-export (AMEFF) uit de GEMMA-Archi-repository; een Archi-bronbestand (`.archimate`) kan ook, als lokaal bestand. `tools/gemma.py` herkent het formaat zelf.

1. **Bron-id kiezen** met de redacteur, bij voorkeur met de release-datum uit het model, bijv. `2026-vng-gemma-2026-07-01`.
2. **Release draaien:** `uv run python tools/gemma.py release --id <bron-id>`. Zonder bestandsnaam haalt de tool de AMEFF op van `wiki.yaml` → `gemma.herkomst`: `VNG-Realisatie/GEMMA-Archi-repository`, branch `master`, bestand `export/GEMMA release.xml`. Met `--ref` of `--pad` kies je een andere versie; een lokaal bestand kan ook: `release <bestand> --id <bron-id>`. De tool neemt het bestand op in `sources/raw/` (met download-URL, GitHub-pagina en de release-datum als versie in de intake), schrijft `gemma/gemma_parsed.json` en `gemma/overzicht.md` (met hash-kop) en zet `gemma.bron` in `wiki.yaml`. Meld formaat, release-datum en aantallen aan de redacteur.
3. **Verschillen bekijken:** `uv run python tools/gemma.py verrijk`. Afwijkende `gemma_*`-velden of verdwenen elementen per stuk voorleggen.
4. **Bijwerken via een run**, zoals bij de GGM-release: WRITE met `uv run python tools/gemma.py verrijk --run <run-id>`, daarna VALIDATE en de promotiegate.

De branch `master` verandert mee met GEMMA. De release-datum in de intake (`versie`) legt vast welke stand is opgenomen; een nieuwe stand is altijd een nieuwe bron.

## Terugschrijven naar GEMMA (later)

Nog niet gebouwd. Advies: geen AMEFF-import (die maakt in Archi nieuwe mappen aan), maar een deel-`.archimate` dat de id's van bestaande elementen, relaties en mappen uit het Archi-bronbestand behoudt; nieuwe elementen krijgen een nieuw id in een bestaande map. Archi voegt bij "import model" samen op id. Test dit eerst met een klein deelbestand op een kopie van het model.
