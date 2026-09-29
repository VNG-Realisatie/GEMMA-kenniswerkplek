---
name: gemma-archimate-model-gemma-release
description: Verwerk een nieuwe versie van het GEMMA-architectuurmodel (Archi-bronbestand, .archimate) in gemma-archimate-model — als bron opnemen, parsen en de gemma_*-velden van bestaande elementen via een run bijwerken. Gebruik alleen bij een nieuw GEMMA-modelbestand.
metadata:
  kind: capability
  scope: wiki
  requires-skills: "wiki-update"
  requires-tools: "llmwiki python:tools/gemma.py"
---

# Nieuwe versie van het GEMMA-model

Het GEMMA-model is een matchdoel (brontype `model`), geen bron voor begrippen. Gebruik het Archi-bronbestand
(`.archimate`): dat is completer dan een Open Exchange-export (mappen met id's, alle eigenschappen).

1. **Bron-id kiezen** met de redacteur, bijv. `2026-vng-gemma-model`.
2. **Release draaien:** `uv run python tools/gemma.py release <bestand.archimate> --id <bron-id>`. Dit neemt het
   bestand op in `sources/raw/`, schrijft `gemma/gemma_parsed.json` en `gemma/overzicht.md` (met hash-kop) en zet
   `gemma.bron` in `wiki.yaml`.
3. **Verschillen bekijken:** `uv run python tools/gemma.py verrijk`. Afwijkende `gemma_*`-velden of verdwenen
   elementen per stuk voorleggen.
4. **Bijwerken via een run**, zoals bij de GGM-release: WRITE met `uv run python tools/gemma.py verrijk --run <run-id>`,
   daarna VALIDATE en de promotiegate.

## Terugschrijven naar GEMMA (later)

Nog niet gebouwd. Advies: geen Open Exchange-export (die maakt bij importeren nieuwe mappen aan), maar een
deel-`.archimate` dat de id's van bestaande elementen, relaties en mappen uit het bronbestand behoudt; nieuwe
elementen krijgen een nieuw id in een bestaande map. Archi voegt bij "import model" samen op id. Test dit eerst
met een klein deelbestand op een kopie van het model.
