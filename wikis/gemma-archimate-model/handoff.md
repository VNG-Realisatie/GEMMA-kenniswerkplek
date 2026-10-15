# Handoff

Overdracht naar de volgende Sessie (2026-10-15). Wordt bij elke overdracht overschreven.

## Stand van zaken

- Plan goedgekeurd: [plannen/2026-10-15-lichtere-werkwijze.md](plannen/2026-10-15-lichtere-werkwijze.md).
- Stap 1 uitgevoerd (commit "rules: afspraken lichtere werkwijze"): commitprefixen in AGENTS.md met `llmwiki commit-check` (geen hook), F1–F3, D1, G1 en E1 in `references/besluiten.md`, de update-skill en `wiki-curatie-update`, en een besluit zonder tekst (`advies: gevolgd`, schema, render, test).
- Volgende stap: stap 2, `tools/beoordeling.py` met `zoek`, `besluiten`, `toon --oordeel`, `zet`, `relatie`, `besluit`, plus A7 (compacte uitvoer en `.gitattributes`).

## Scope

Stap 2 van het plan, zie de sectie Uitvoering en de rijen A2–A4, A7, C2 en C5 (alleen A7 en C2 nu). Daarna stap 3 en verder, elk in een eigen commit na akkoord.

## Besluiten die gelden

- Geen inhoudelijke wijzigingen in deze klus: de beslistabel, de typen, de uitkomsten en de export blijven gelijk.
- Alleen de kenmerken met ja vastleggen is afgeraden; de nee die de uitkomst bepaalt, blijft als dubbelcheck.
- 2026-10-14: elk levensloopproces met afnemer extern realiseert minstens één UPL-dienst (voor de proef, stap 9).
- 2026-10-14: de plaats van Verzorgen gemeentebegrafenis is geparkeerd; het advies is optie 1 (voor de proef, stap 9).
- 2026-10-15: geen gereedschaps- of harnessspecifieke hooks; controles zijn gewone commando's. De vraag over `.pre-commit-config.yaml` staat in de root-`TODO.md`.
- De wiki-skills staan in `.agents/skills/`; `.claude/skills/` is een gitignored kopie, wijzig alleen `.agents/skills/`.

## Werkwijze

- Per stap: kort voorleggen wat er verandert, dan uitvoeren, dan commit met een prefix en een bericht van één of twee zinnen; controleer met `uv run python -m llmwiki commit-check <bestand>`.
- Voorleggen voor een architect: in gewone taal en analytisch, met de gevolgen voor het model, de bron als link.
- Commit direct op main.

## Modeladvies

Stap 2 is denkniveau middel (scripts schrijven met tests); een snel model of een middelhoge redeneerinspanning volstaat. Stap 3 tot en met 5 vragen denkniveau hoog. Begin een nieuwe Sessie: deze Sessie bevat de stap-1-context niet meer nodig.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en voer stap 2 uit van plannen/2026-10-15-lichtere-werkwijze.md (sectie Uitvoering). Lees uit het plan alleen de rijen A2–A4, A7 en C2 en de sectie Controle. Leg kort voor wat je bouwt, voer uit na mijn akkoord, en commit met een prefix.
```
