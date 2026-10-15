# Handoff

Overdracht naar de volgende Sessie (2026-10-15). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits en de todo.

## Stand van zaken

- Plan: [plannen/2026-10-15-lichtere-werkwijze.md](plannen/2026-10-15-lichtere-werkwijze.md), stap 1 tot en met 8 uitgevoerd (`git log` op de prefixen `rules:` en `tools:` sinds "rules: afspraken lichtere werkwijze").
- Stap 8: workspace-check herstelt bruggen van verdwenen skills (G5); woordbudget in `llmwiki lint` via `lint.woordbudget` in `wiki.yaml` (G4); export alleen op verzoek, `afronden.py --export` (G2); de todo is gesplitst in [todo.md](todo.md) (actief) en [todo-later.md](todo-later.md) (E4).
- Controle: pytest (416) en lint zonder fouten; `render.py --check` en `archimate_export.py --check` slagen.
- De 11 niet-letterlijke citaten zijn per geval met de redacteur hersteld; een citaat dat niet letterlijk in de bron staat is nu een fout in `beslissen.py`.
- Nog niet gedaan: compacte uitvoer van `llmwiki promote plan`.

## Scope

Stap 9, de proef: "Levensloopproces realiseert altijd een dienst" en "Verzorgen gemeentebegrafenis" (todo.md, Proef), in een Sessie per fase (skill `gemma-archimate-model-update`). Meet beurten, totale invoer, vragen en besluiten uit het transcript en vergelijk ze met de tabel "Totaal per onderwerp" in het plan; meet ook de ingest-subagent en het aanvullen van bronduidingen na fase A (plan, Afwijking bij stap 7).

## Besluiten die gelden

- Geen inhoudelijke wijzigingen in de beslistabel, de typen en de uitkomsten.
- 2026-10-14: elk levensloopproces met afnemer extern realiseert minstens één UPL-dienst; de plaats van Verzorgen gemeentebegrafenis is geparkeerd, het advies is optie 1.
- 2026-10-15: export alleen op verzoek van de redacteur, per afronding `--check`; een nieuwe regel die het woordbudget overschrijdt gaat eerst naar de redacteur.
- 2026-10-15: geen gereedschaps- of harnessspecifieke hooks.

## Modeladvies

De proef vraagt denkniveau hoog (een sterker model of hoge redeneerinspanning), in een nieuwe Sessie per fase. Begin een nieuwe Sessie.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en voer stap 9 (de proef) uit van plannen/2026-10-15-lichtere-werkwijze.md: begin met fase 1 van skill gemma-archimate-model-update voor "Levensloopproces realiseert altijd een dienst". Leg kort voor wat je doet, voer uit na mijn akkoord, en commit met een prefix. Houd bij hoeveel beurten en woorden elke fase kost.
```
