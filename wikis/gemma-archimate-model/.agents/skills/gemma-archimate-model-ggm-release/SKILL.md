---
name: gemma-archimate-model-ggm-release
description: Verwerk een nieuwe GGM-release (XMI) in gemma-archimate-model — XMI als bron opnemen, parsen, leesbare GGM-pagina's genereren en de ggm_*-velden van bestaande elementen via een run bijwerken. Gebruik alleen bij een nieuw GGM-XMI-bestand.
metadata:
  kind: capability
  scope: wiki
  requires-skills: "wiki-update"
  requires-tools: "llmwiki python:tools/ggm.py"
---

# Nieuwe GGM-release

Het XMI is de bron van waarheid voor het GGM. Het model leest het nooit direct; alleen via `tools/ggm.py`.

1. **Bron-id kiezen** met de redacteur, bijv. `2026-vng-ggm-2-5-1`. Een nieuwe release is altijd een nieuwe bron.
2. **Release draaien:** `uv run python tools/ggm.py release --id <bron-id> --titel "<titel>"`. Zonder bestandsnaam haalt de tool het XMI op van de GGM-repository op GitHub, zoals vastgelegd in `wiki.yaml` onder `ggm.herkomst` (`Gemeente-Delft/Gemeentelijk-Gegevensmodel`, branch `Voorbereidingen-Release-v2.5.1`, bestand `v2.5.1/Gemeentelijk Gegevensmodel XMI2.1.xml`). Voor een andere release: `--ref <branch of tag>` en zo nodig `--pad <pad>`, of pas `ggm.herkomst` aan in overleg met de redacteur. Een lokaal bestand kan ook: `release <xmi> --id <bron-id>`. De tool neemt het XMI op in `sources/raw/` (met de download-URL en de GitHub-pagina in de intake en een gegenereerd structuuroverzicht als Markdown-versie), schrijft `ggm/ggm_parsed.json` en de leesbare pagina's in `ggm/<taakveld>/<beleidsdomein>.md` (met hash-kop), en zet `ggm.bron` in `wiki.yaml`. Meld de aantallen (entiteiten, relaties, pagina's) aan de redacteur. Geteld worden alleen objecttypen; enumeraties en diagramcontainers niet.
3. **Verschillen bekijken:** `uv run python tools/ggm.py verrijk`. Toon welke elementen afwijkende `ggm_*`-velden krijgen. Een gewijzigde GUID of een verdwenen entiteit kan wijzen op een homoniem of een verplaatste entiteit: leg die gevallen per stuk voor, nooit blind toepassen.
4. **Bijwerken via een run:** start `uv run python -m llmwiki run start --workflow gemma-archimate-model-ggm-release`, doorloop INGEST en ASSESS kort (bron = de release; voorstellen = de afwijkende elementen) en stage in WRITE met `uv run python tools/ggm.py verrijk --run <run-id>`. Goedgekeurde pagina's gaan daarbij terug naar `review`. Rond af via VALIDATE (`tools/check_elementen.py`) en de promotiegate, zoals in `wiki-update`.
5. `ggm/` nooit met de hand bewerken; bij twijfel opnieuw genereren met stap 2.
