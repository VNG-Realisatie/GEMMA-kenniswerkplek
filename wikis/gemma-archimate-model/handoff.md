# Handoff

Overdracht naar de volgende Sessie (2026-10-18). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits, het plan en de todo.

## Stand van zaken

- Plan [plannen/2026-10-15-archimate-indeling.md](plannen/2026-10-15-archimate-indeling.md) is uitgevoerd (Uitkomst stap 14).
- Gedaan in deze Sessie: `beslist` staat niet meer in de beoordeling maar in `onderwerpen/<onderwerp>/beslist.yaml` (gegenereerd door `tools/beslissen.py`, `curation.beslist` in wiki.yaml). `llmwiki.beoordeling.alle()` voegt het blok samen, zodat render, export, relaties en werkpakket ongewijzigd lezen; `schrijf(pad, data, wiki_yaml)` laat het weg. De migratie liet de 484 akkoord-hashes, de pagina's en de export ongewijzigd (geen nieuw AKKOORD).
- Een agent die een beoordeling als precedent leest, krijgt nu 22.000 woorden minder; `beslist.yaml` leest alleen wie het nodig heeft.

## Volgende klus

Kies uit [todo.md](todo.md), sectie ArchiMate-indeling en Herbeoordeling:

1. **Potentiële relaties vastleggen** (inhoud, middel): 239 relationele kenmerken ja zonder relatie.
2. **Participatie herbeoordelen** met de lichtere werkwijze (inhoud, hoog voor de beoordeling).
3. **GEMMA-functies onder *Ontvangst*** terugmelden (inhoud, middel), of **GGM-match voor rollen, actoren en gebeurtenissen**.

## Modeladvies

Optie 1 is inhoudelijk werk met een bekende werkwijze (middel). Optie 2 vraagt oordelen en afwegen (hoog): een sterker model of hogere redeneerinspanning. Begin een nieuwe Sessie: de context van dit scriptwerk helpt niet bij de inhoud. Meet bij de volgende beoordeling met agenten of het lezen van precedenten (zonder `beslist`) is afgenomen.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en todo.md. Voer het todo-punt "Potentiële relaties vastleggen" uit voor één onderwerp: stel eerst voor welk onderwerp en hoe je de tegenpartij in `naar` bepaalt, en leg dat voor vóór je schrijft. Houd je aan de woordbudgetten in wiki.yaml.
```
