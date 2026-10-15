# Handoff

Overdracht naar de volgende Sessie (2026-10-15). Wordt bij elke overdracht overschreven.

## Stand van zaken

- Plan goedgekeurd: [plannen/2026-10-15-lichtere-werkwijze.md](plannen/2026-10-15-lichtere-werkwijze.md). Vastgelegd in de commit "docs: plan lichtere werkwijze", samen met de todo en het verplaatsen van deze handoff.
- Nog niets uitgevoerd. Volgende stap: stap 1 van de sectie Uitvoering.

## Scope

Stap 1 van het plan: de afspraken.

- **G3 commitprefixen:** de prefixen in de root-AGENTS.md (Werkwijze), plus een controle op het commitbericht in de pre-commit (`tools/llmwiki`, commando `precommit`).
- **F1–F3 vragen en besluiten:** vragen opsparen, voorleggen voor een architect en minder besluiten, in `references/besluiten.md` van skill `gemma-archimate-model-beoordelen`.
- **D1 precedent:** een precedent wordt pas een regel na voorleggen.
- **G1 bundelen:** promote, terugmeldingen en AKKOORD per afgerond onderwerp of deel, in de update-skill.
- **E1 een Sessie per fase:** in de update-skill en in skill `wiki-curatie-update` (Een onderwerp in één keer afronden).
- **Besluit zonder tekst:** `tools/beslissen.py` laat dat toe bij advies gevolgd.

Daarna stap 2 en verder, elk in een eigen commit na akkoord.

## Besluiten die gelden

- Geen inhoudelijke wijzigingen in deze klus: de beslistabel, de typen, de uitkomsten en de export blijven gelijk.
- Alleen de kenmerken met ja vastleggen is afgeraden; de nee die de uitkomst bepaalt, blijft als dubbelcheck.
- 2026-10-14: elk levensloopproces met afnemer extern realiseert minstens één UPL-dienst (voor de proef, stap 9).
- 2026-10-14: de plaats van Verzorgen gemeentebegrafenis is geparkeerd; het advies is optie 1 (voor de proef, stap 9).

## Werkwijze

- Per stap: kort voorleggen wat er verandert, dan uitvoeren, dan commit met een prefix (`rules:`, `tools:`, `docs:`, …) en een bericht van één of twee zinnen.
- Voorleggen voor een architect: in gewone taal en analytisch, met de gevolgen voor het model, de bron als link.
- Commit direct op main.

## Modeladvies

Stap 1 is denkniveau middel: afspraken nauwkeurig vastleggen, met weinig afweging. Een snel model of een middelhoge redeneerinspanning volstaat. Stap 3 tot en met 5 vragen denkniveau hoog. Begin een nieuwe Sessie: de Sessie van het plan heeft een grote context.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en voer stap 1 uit van plannen/2026-10-15-lichtere-werkwijze.md (sectie Uitvoering). Lees uit het plan alleen de secties die stap 1 nodig heeft: F3 (Analyse van de besluiten), Prefixen voor commitberichten en de rijen F1–F3, D1, G1, G3 en E1. Leg kort voor wat je wijzigt, voer uit na mijn akkoord, en commit met een prefix.
```
