# Handoff

Overdracht naar de volgende Sessie (2026-10-15). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits en de todo.

## Stand van zaken

- Plan: [plannen/2026-10-15-lichtere-werkwijze.md](plannen/2026-10-15-lichtere-werkwijze.md), stap 9 (de proef) met het onderwerp Participatie. Fase 1 en fase 2 zijn gecommit; fase 3 (beslissen, voorleggen, akkoord, commit) is de volgende.
- K1 uitgevoerd: bron `2024-vng-model-participatieverordening` (gemeentelijke-regelgeving, bijlage 1 bij VNG-ledenbrief 24/051), bronduiding in `onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/`.
- Fase B gedaan door drie beoordelingsagenten (Participatieplan; Verzoek uitdaagrecht; zonder kernobject). `beslissen.py` geeft geen fouten; lint en pytest slagen. Status: review voor Uitvoeren inwonersparticipatie, Participatieplan, Behandelen verzoek uitdaagrecht, Verzoek uitdaagrecht, Indiener, Inwoner, Maatschappelijke partij, Model Participatieverordening en Gemeentewet; kandidaat voor Eindverslag inwonersparticipatie, Afspraak over uitvoering en Participatieverordening (geen proces bepaalt de levensloop).
- Gebundeld door de hoofdsessie: toewijzing van Beslisser naar beide processen; toegang (raadplegen) van beide processen naar Participatieverordening; Participatieverordening als specialisatie (met element) van Regeling; de zin over burgerzaken in Inwoner herschreven (regel Los van het onderwerp); terugmeldingen procesarchitectuur (UPL-product voor het uitdaagrecht) en GEMMA-team (actor Burger naast Inwoner).
- Overgebleven waarschuwingen zijn toegelicht: 'Registreert' in Uitvoeren inwonersparticipatie (vaste handeling); Gemeentewet en Model Participatieverordening hangen alleen aan processen (geen UPL-product, teruggemeld); de naam Model Participatieverordening volgt het precedent van de Model beheersverordening.

## Voor te leggen in fase 3 (`vragen:` en open redenen)

1. Beleidsdomein voor het hele onderwerp: een gemeentelijk beleidsdomein Participatie onder taakveld 0 (nu bij de twee processen, Participatieplan, Eindverslag, Verzoek uitdaagrecht, Afspraak) of Besluitvorming (nu bij Participatieverordening, Model en Gemeentewet). Eén besluit; daarna gelijktrekken, en bij Participatie de regel in `modellen/gemma/indelingen/beleidsdomeinen.yaml` en een procesarchitectuur-terugmelding (beleidsdomein).
2. Uitvoeren inwonersparticipatie en Behandelen verzoek uitdaagrecht zijn levensloopproces (K4 zei bedrijfsproces): bevestigen.
3. Participatieplan en Eindverslag: grondslag art. 150 lid 1 Gemeentewet, de wet schrijft plan en verslag niet voor (alleen de VNG-modelverordening).
4. Eindverslag inwonersparticipatie: advies geen eigen element (afwijzen); het staat als resultaat in het proces. Bij afwijzen vervalt de relatie vanuit het proces.
5. Afspraak over uitvoering zonder eigen levensloopproces: advies opnemen, levensloop in Behandelen verzoek uitdaagrecht (precedent Urn, 2026-10-08).
6. Verzoek uitdaagrecht geen specialisatie van Aanvraag (Awb), en Indiener geen specialisatie van Belanghebbende: advies nee, want geen bron noemt de reactie een besluit (bevestigen).
7. Participatieverordening: zelfstandige specialisatie van Regeling (advies ja); het signaal over de levensloop laten staan zoals bij Beleidsnota en Regeling.
8. GEMMA-match partieel van Uitvoeren inwonersparticipatie op Generiek deelproces Uitvoeren participatie (K4). Blijft hij, dan een GEMMA-terugmelding (de import geeft dat deelproces een naam, definitie en niveau; controleren in Vaststellen omgevingsplan).
- Niet aangemaakt, advies geen element: reactie op het verzoek, formulier, experimenteerprogramma; participatiejaarverslag is synoniem van Participatieparagraaf (variant 2). Kandidaat-bedrijfsfunctie: GEMMA-bladfunctie Burgerinitiatieven facilitering (id-27250af5-c8bc-4167-a743-9b1c6d6edef6) onder Samenwerking en participatie.
- Rol van het college als centraal loket voor verzoeken: nu alleen in de beschrijving.
- Vermoedelijke verwijsfout in de VNG-modelverordening (var. 2 art. [13] lid 3 onder c: artikel 12 in plaats van [11]); past in geen register.

## Meting fase 2 (transcripten)

| | Hoofdsessie | Ingest | Participatieplan | Verzoek uitdaagrecht | Zonder kernobject | Fase 2 totaal | Fase 1 | Deel 2, heel onderwerp |
|---|---|---|---|---|---|---|---|---|
| Beurten | 30 (tot de meting) | 18 | 44 | 56 | 65 | 213 | 42 | 156 |
| Totale invoer | 2,8 mln | 1,3 mln | 5,1 mln | 7,9 mln | 8,9 mln | 26,0 mln | 5,6 mln | 48 mln |
| Startcontext | 40.300 | 34.000 | 34.400 | 34.500 | 34.600 | — | 40.400 | 43.000 |
| Grootste context | 131.000 | 100.000 | 162.000 | 211.000 | 198.000 | — | 205.000 | 487.000 |
| Gelezen (woorden, eigen opgave) | — | 13.000 | 17.000 | 21.000 | 21.000 | — | — | — |

- Werkpakket per cluster (met `--alles`): Participatieplan 1.423, Verzoek uitdaagrecht 3.486, het hele onderwerp 21.243 woorden (zonder `--alles` 730, 1.209 en 9.879). De agent zonder kernobject las er gefilterd ongeveer 7.500 uit.
- Wat de agenten lazen: regels en skills 6.000 à 7.800 woorden, bronnen ongeveer 4.000, en bestaande beoordelingen en code als precedent 3.500 à 5.000, wat niet in hun opdracht stond. De beurten (44 à 65 per agent) zijn de grootste post: de invoer groeit kwadratisch met de beurten.
- Ingest-subagent: 18 beurten, 1,3 mln; `tools/bronduiding.py citaat` kon de bron niet lezen (zie todo), citaten overgetypt en gecontroleerd. Bronduiding na fase A aangevuld: 0 keer.
- Uitvoer van de subagenten staat niet betrouwbaar in hun transcript (een paar honderd tokens); niet meegeteld.
- E2 (beoordelingsagenten): fase 2 kost met 26 mln meer dan het plan verwachtte (ongeveer neutraal). Drie agenten met elk 34.000 startcontext en 44–65 beurten, voor 12 begrippen. De afweging voor een klein onderwerp: één hoofdsessie (skill, stap 8: "bij een handvol begrippen") is waarschijnlijk goedkoper.

## Modeladvies

Fase 3 vraagt denkniveau hoog (voorleggen in één tabel, oordelen per vraag); stap 13 tot en met 17 laag. Begin een nieuwe Sessie: fase 3 begint met een schone context.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en voer fase 3 uit van skill gemma-archimate-model-update voor het onderwerp Participatie (stap 9, de proef, van plannen/2026-10-15-lichtere-werkwijze.md). Draai beslissen.py, leg de acht punten uit de handoff en de open redenen voor in één tabel zoals voor een architect (references/besluiten.md), verwerk mijn antwoorden per geval en draai opnieuw. Daarna promote plan; ik geef akkoord met AKKOORD; dan afronden.py met een prefix. Meet beurten, totale invoer en grootste context van fase 3, en vat de proef samen tegen de tabel "Totaal per onderwerp" van het plan.
```
