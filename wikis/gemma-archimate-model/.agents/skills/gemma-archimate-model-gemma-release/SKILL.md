---
name: gemma-archimate-model-gemma-release
description: Verwerk een nieuwe versie van het GEMMA-architectuurmodel in gemma-archimate-model — het Archi-bestand (.archimate, voorkeur) of de AMEFF-export ophalen of als lokaal bestand opnemen, als bron opnemen, parsen en de beoordelingen opnieuw afleiden, zodat de letterlijke GEMMA-velden en de pagina's meegaan. Gebruik alleen bij een nieuwe GEMMA-modelversie.
metadata:
  kind: capability
  scope: wiki
  requires-skills: "gemma-archimate-model-update"
  requires-tools: "llmwiki python:tools/gemma.py python:tools/afleiden.py"
---

# Nieuwe versie van het GEMMA-model

Het GEMMA-model is een matchdoel (brontype `model`), geen bron voor begrippen. Voorkeur: het Archi-bestand (`.archimate`, het opslagformaat van Archi en van coArchi 2). Alleen dat heeft de id's van mappen en profielen, die de export naar Archi nodig heeft (skill `gemma-archimate-model-archimate-export`). De ArchiMate Open Exchange-export (AMEFF) uit de GEMMA-Archi-repository kan ook, maar dan werkt de export niet. `tools/gemma.py` herkent het formaat zelf.

Zolang de GEMMA-Archi-repository geen `.archimate` publiceert (zie `todo.md`): de redacteur opent het GEMMA-model in Archi (met coArchi), slaat een kopie op via *File › Save As…* als `.archimate` en geeft het pad; neem het op als lokaal bestand.

1. **Bron-id kiezen** met de redacteur, bij voorkeur met de release-datum uit het model, bijv. `2026-vng-gemma-2026-07-01`.
2. **Release draaien:** `uv run python tools/gemma.py release <bestand.archimate> --id <bron-id>` voor een lokaal Archi-bestand. Zonder bestandsnaam haalt de tool de AMEFF op van `wiki.yaml` → `gemma.herkomst`: `VNG-Realisatie/GEMMA-Archi-repository`, branch `master`, bestand `export/GEMMA release.xml`. Met `--ref` of `--pad` kies je een andere versie; een lokaal bestand kan ook: `release <bestand> --id <bron-id>`. De tool neemt het bestand op in `sources/raw/` (met download-URL, GitHub-pagina en de release-datum als versie in de intake), schrijft `gemma/gemma_parsed.json` en `gemma/overzicht.md` (met hash-kop) en zet `gemma.bron` in `wiki.yaml`. Meld formaat, release-datum en aantallen aan de redacteur.
3. **Afleiden:** `uv run python tools/afleiden.py` haalt de letterlijke GEMMA-velden opnieuw op en rendert de pagina's. Een verdwenen GEMMA-id is een fout: zoek met `tools/gemma.py kandidaten` opnieuw op betekenis en leg elk geval apart voor.
4. **Status:** zoals bij de GGM-release: de letterlijke modelvelden horen niet bij het akkoord; een inhoudelijke wijziging in een beoordeling gaat via de gewone workflow naar akkoord.

De branch `master` verandert mee met GEMMA. De release-datum in de intake (`versie`) legt vast welke stand is opgenomen; een nieuwe stand is altijd een nieuwe bron.

## Terugschrijven naar GEMMA

Zie skill `gemma-archimate-model-archimate-export`: een `.archimate` met de id's van GEMMA, import in Archi en een volledige sync met een jArchi-script.
