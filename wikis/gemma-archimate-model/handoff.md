# Handoff

Overdracht naar de volgende Sessie (2026-10-15). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits en de todo.

## Stand van zaken

- Plan: [plannen/2026-10-15-lichtere-werkwijze.md](plannen/2026-10-15-lichtere-werkwijze.md), stap 9 (de proef, onderwerp Participatie): fase 1, 2 en 3 zijn gecommit; 16 elementen goedgekeurd (AKKOORD 2026-10-15), Eindverslag inwonersparticipatie afgewezen.
- Besluiten in fase 3: beleidsdomein Participatie onder taakveld 0 (niet Sociaal domein), met register en procesarchitectuur-terugmelding 30; Uitvoeren inwonersparticipatie hernoemd tot Betrekken inwoners bij beleid, zonder GEMMA-match met het Generiek deelproces Uitvoeren participatie (Omgevingswet); K4 heroverwogen (levensloopproces); Afspraak over uitvoering en Participatieverordening opgenomen; Verzoek uitdaagrecht en Indiener zonder specialisatie naar Aanvraag en Belanghebbende.
- Nieuw werkwijzebesluit: zekerheid van besluiten (`kennis`, `logica`, `indruk`), in [todo.md](todo.md); tot de uitvoering staat de zekerheid in de besluittekst. Dit is de volgende klus, in een eigen commit `rules:`.

## Meting fase 3 (transcript, tot de commit)

| | Fase 1 | Fase 2 | Fase 3 | Proef totaal | Plan "Straks" | Deel 2 (nu) |
|---|---|---|---|---|---|---|
| Beurten | 42 | 213 | 44 | ongeveer 300 | ongeveer 80 | 156 |
| Totale invoer | 5,6 mln | 26,0 mln | 3,8 mln | ongeveer 35 mln | 4 à 5 mln | 48 mln |
| Startcontext | 40.400 | 34.000 à 40.300 | 40.600 | — | ongeveer 40.000 | 43.000 |
| Grootste context | 205.000 | 211.000 | 127.000 | 211.000 | ongeveer 80.000 | 487.000 |
| Vragenrondes | 1 tabel | 0 | 1 tabel en 3 vervolgrondes | 2 tabellen, 3 vervolg | 2 à 3 tabellen | verspreid |
| Nieuwe besluiten | 6 | 0 | 8 | 14 | ongeveer 10 | ongeveer 30 |

## Samenvatting van de proef

- **Totale invoer −26%** ten opzichte van deel 2 (35 tegen 48 mln), maar zeven keer de schatting van het plan. Fase 1 en 3 samen (9,4 mln, 86 beurten) zitten dicht bij het plan; het verschil zit in fase 2: drie beoordelingsagenten met 44–65 beurten voor 12 begrippen (26 mln).
- **Grootste context** bleef ruim onder deel 2 (211.000 tegen 487.000), boven de 80.000 van het plan: elke agent groeide tot 160.000–210.000.
- **Voorleggen in één tabel werkt**, maar vroeg in fase 3 drie vervolgrondes: twee begrippen (K4, levensloopproces) waren onduidelijk, en een besluit uit fase 1 bleek op een verkeerd beeld te rusten. Dat leidde tot het werkwijzebesluit over zekerheid.
- **Nieuwe besluiten** 14 tegen ongeveer 30, iets boven de schatting.
- Advies voor het plan: bij een klein onderwerp (tot ongeveer 15 begrippen voor fase B) fase B in de hoofdsessie doen in plaats van agenten (skill, stap 8); en de bevindingen van fase 2 in todo.md (werkpakket `--alles`, `--ids`, `bronduiding.py citaat`, agenten die precedenten lezen) oppakken. Leg dit voor bij de volgende Sessie, samen met het afsluiten van stap 9 in het plan.

## Modeladvies

De volgende klus (zekerheid van besluiten: regels, `beoordeling.py`, `werkpakket.py`, schema) vraagt denkniveau middel voor de code en hoog voor de regelteksten en de omgang met bestaande besluiten. Begin een nieuwe Sessie: de context is gevuld met Participatie.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en todo.md. Voer de todo "Zekerheid van besluiten" uit (besluit redacteur 2026-10-15): het veld zekerheid (kennis, logica, indruk) in het schema, tools/beoordeling.py (--zekerheid), tools/werkpakket.py (niveau tonen; agenten volgen alleen kennis als regel), de regel Navragen in de wiki-AGENTS.md, references/besluiten.md en de precedentregel van skill gemma-archimate-model-beoordelen, en de kolom Eerder besluit (zekerheid) in fase 3 van skill gemma-archimate-model-update. Bestaande besluiten zonder veld tellen als logica; zet de zekerheid van de Participatie-besluiten van 2026-10-15 uit hun tekst in het veld. Controleer eerst het woordbudget. Daarna pytest en lint, en een commit met prefix rules. Leg daarna de samenvatting van de proef (handoff) voor en sluit stap 9 van het plan af.
```
