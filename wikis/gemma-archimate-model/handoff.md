# Handoff

Overdracht naar de volgende Sessie (2026-10-15). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits en de todo.

## Stand van zaken

- Plan: [plannen/2026-10-15-lichtere-werkwijze.md](plannen/2026-10-15-lichtere-werkwijze.md), stap 9 (de proef) met het onderwerp Participatie. Fase 1 (bronnen en fase A) is gecommit; fase 2 (fase B per cluster) is de volgende.
- Fase A staat in `onderwerpen/participatie/beoordelingen/` (28 beoordelingen: 12 naar fase B, 17 vallen af) en in `onderwerpen/bestuur-en-organisatie/beoordelingen/gemeentewet.yaml` (verplaatst uit Lijkbezorging). Belanghebbende, Beslisser, Beleidsnota, Uitvoeren uniforme openbare voorbereidingsprocedure en Zienswijze hebben `participatie` in `onderwerpen`.
- `tools/beslissen.py` meldt 12 fouten: de kenmerken van fase B. Het schrijft pas na fase B; tot dan wijken de pagina's af van de beoordelingen (`render.py --check`). Lint en pytest slagen.

## Besluiten fase 1 (2026-10-15, advies gevolgd)

- K1: de VNG Model Participatieverordening 2024 wordt een eigen bron (brontype gemeentelijke-regelgeving), als eerste stap van fase 2, met skill `gemma-archimate-model-ingest` in een subagent; de implementatiehandleiding (richtlijn) bevat de modeltekst niet. Model Participatieverordening wordt beleidskader (VNG-modelverordening) dat de Gemeentewet uitwerkt.
- K2: Gemeentewet wordt beleidskader met thuis Bestuur en organisatie; in deze ronde alleen de relaties voor Participatie (art. 150). De rest staat in [todo.md](todo.md).
- K3: het verzoekproces heet Behandelen verzoek uitdaagrecht (kernobject Verzoek uitdaagrecht); Overheidsparticipatie is synoniem (variant 2). Het besluit over het uitdaagrecht van 2026-09-30 staat nu letterlijk in die beoordeling.
- K4: Uitvoeren inwonersparticipatie is een eigen bedrijfsproces met kernobject Participatieplan. GEMMA kent alleen het Generiek deelproces Uitvoeren participatie (partieel, voorleggen in fase 3) en de functie Samenwerking en participatie.
- K5: Inspraak is geen element; Uitvoeren inwonersparticipatie krijgt bij inspraak een relatie naar Uitvoeren uniforme openbare voorbereidingsprocedure (Gemeentewet art. 150 lid 2).
- K6: Inspraakverordening is synoniem van Participatieverordening (voorganger).
- Voor fase B: Verzoek uitdaagrecht mogelijk specialisatie van Aanvraag (Awb), Indiener mogelijk specialisatie van Belanghebbende; Inwoner thuis Participatie zolang alleen Participatie haar gebruikt.

## Clusters voor fase B

1. Participatieplan: `uitvoeren-inwonersparticipatie`, `participatieplan`, `eindverslag-inwonersparticipatie`.
2. Verzoek uitdaagrecht: `behandelen-verzoek-uitdaagrecht`, `verzoek-uitdaagrecht`, `afspraak-over-uitvoering`, `indiener`.
3. Zonder kernobject: `model-participatieverordening`, `participatieverordening`, `inwoner`, `maatschappelijke-partij`, `gemeentewet`.

Advies: drie beoordelingsagenten (plan E2), ook al is het onderwerp klein, zodat de proef E2 meet.

## Meting fase 1 (transcript)

| | Fase 1 gemeten | Plan, fase 1 | Deel 2, heel onderwerp |
|---|---|---|---|
| Beurten | 42 (tot de meting; met handoff en commit ongeveer 47) | ongeveer 30 | 156 |
| Totale invoer | 5,6 miljoen | deel van 4 à 5 miljoen | 48 miljoen |
| Startcontext | 40.400 | ongeveer 40.000 | 43.000 |
| Grootste context | 205.000 | ongeveer 80.000 | 487.000 |
| Groei per beurt | ongeveer 3.900 tokens | ongeveer 1.200 | ongeveer 2.800 |
| Uitvoer | 51.000 | — | 189.000 |
| Vragenrondes | 2 (voorstel; één tabel met 6 keuzes) | 2 à 3 per onderwerp | verspreid |
| Nieuwe besluiten | 3 (plus 1 letterlijk verplaatst) | ongeveer 10 per onderwerp | ongeveer 30 |

- Woorden: toolresultaten 31.200 (werkpakket 13.200), toolaanroepen 3.500, chat 1.850; beoordelingen 3.400 woorden voor 28 bestanden (ongeveer 120 per begrip, tegen 980 vóór B1).
- Werkpakket: 13.196 woorden voor het hele onderwerp (40 begrippen; Lijkbezorging 35.000). De passage van Gemeentewet art. 150 staat er vijf keer in (bij elk begrip uit dat artikel): een kandidaat om te ontdubbelen. Een leesopdracht van het werkpakket gaf een te grote uitvoer en werd opnieuw gelezen (plan, A7). Per cluster nog niet gemeten (fase 2).
- Ingest-subagent: niet gebruikt in fase 1 (bronduidingen bestonden, citaten letterlijk); in fase 2 wel (K1), meten. Bronduiding na fase A aangevuld: 0 keer.
- De grootste context komt vooral uit het lezen van de regels en het werkpakket (ongeveer 12.000 + 13.000 woorden) en de beoordelingen schrijven; het kwadratische deel blijft, ook met 42 beurten.

## Modeladvies

Fase 2 vraagt denkniveau hoog (fase B, een sterker model of hoge redeneerinspanning); de ingest-subagent middel. Begin een nieuwe Sessie: fase 2 begint met een schone context.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en voer fase 2 uit van skill gemma-archimate-model-update voor het onderwerp Participatie (stap 9, de proef, van plannen/2026-10-15-lichtere-werkwijze.md). Begin met K1: neem de VNG Model Participatieverordening 2024 op als bron met skill gemma-archimate-model-ingest in een subagent op denkniveau middel. Doe daarna fase B per cluster met drie beoordelingsagenten op denkniveau hoog, en draai beslissen.py. Leg kort voor wat je doet, voer uit na mijn akkoord, en commit met een prefix. Meet beurten, totale invoer, grootste context en woorden van de fase, van de ingest-subagent en van elke beoordelingsagent, en de omvang van het werkpakket per cluster.
```
