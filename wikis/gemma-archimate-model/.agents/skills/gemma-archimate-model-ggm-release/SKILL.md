---
name: gemma-archimate-model-ggm-release
description: Verwerk een nieuwe GGM-release (XMI) in gemma-archimate-model — XMI als bron opnemen, parsen, leesbare GGM-pagina's genereren en de beoordelingen opnieuw laten beslissen, zodat de letterlijke GGM-velden en de pagina's meegaan. Gebruik alleen bij een nieuw GGM-XMI-bestand.
metadata:
  kind: capability
  scope: wiki
  requires-skills: "gemma-archimate-model-update"
  requires-tools: "llmwiki python:tools/ggm.py python:tools/beslissen.py"
---

# Nieuwe GGM-release

Het XMI is de bron van waarheid voor het GGM. Het model leest het nooit direct; alleen via `tools/ggm.py`.

1. **Bron-id kiezen** met de redacteur, bijv. `2026-vng-ggm-2-5-1`. Een nieuwe release is altijd een nieuwe bron.
2. **Release draaien:** `uv run python tools/ggm.py release --id <bron-id> --titel "<titel>"`. Zonder bestandsnaam haalt de tool het XMI op van de GGM-repository op GitHub, zoals vastgelegd in `wiki.yaml` onder `ggm.herkomst` (`Gemeente-Delft/Gemeentelijk-Gegevensmodel`, branch `Voorbereidingen-Release-v2.5.1`, bestand `v2.5.1/Gemeentelijk Gegevensmodel XMI2.1.xml`). Voor een andere release: `--ref <branch of tag>` en zo nodig `--pad <pad>`, of pas `ggm.herkomst` aan in overleg met de redacteur. Een lokaal bestand kan ook: `release <xmi> --id <bron-id>`. De tool neemt het XMI op in `sources/raw/` (met de download-URL en de GitHub-pagina in de intake en een gegenereerd structuuroverzicht als Markdown-versie), schrijft `ggm/ggm_parsed.json` en de leesbare pagina's in `ggm/<taakveld>/<beleidsdomein>.md` (met hash-kop), en zet `ggm.bron` in `wiki.yaml`. Meld de aantallen (entiteiten, relaties, pagina's) aan de redacteur. Geteld worden alleen objecttypen; enumeraties en diagramcontainers niet.
3. **Beslissen:** `uv run python tools/beslissen.py`. Het script haalt de letterlijke GGM-velden van elke gekozen match opnieuw op en rendert de pagina's; de wijzigingen staan daarna in Source Control. Een verdwenen GUID is een fout: zoek met `tools/ggm.py kandidaten` de entiteit op betekenis opnieuw op en leg elk geval apart voor (een verplaatste entiteit of een homoniem), nooit blind vervangen.
4. **Status:** de letterlijke modelvelden horen niet bij het akkoord; goedgekeurde elementen blijven goedgekeurd zolang hun beoordeling niet verandert. Leidt de release tot een inhoudelijke wijziging (een andere match, een nieuwe terugmelding), dan pas je de beoordeling aan en gaat het element via de gewone workflow (`gemma-archimate-model-update`, stap 4 tot 9) naar akkoord.
5. `ggm/` nooit met de hand bewerken; bij twijfel opnieuw genereren met stap 2.
