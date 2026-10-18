# Plan: afleidbare aggregaties uit de export

Basis: main op 169b22dd. De besluiten van de redacteur staan in hoofdstuk 3 (interview van 2026-10-18).

## 1 Probleem

In Archi hangt elk element met een aggregatie aan de groepering van zijn beleidsdomein, ook als het al via een ander element onder die groepering te vinden is. Begraafplaatsen en crematoria aggregeert de Wet op de lijkbezorging; het Besluit op de lijkbezorging werkt die wet uit, dus de aggregatie van Begraafplaatsen en crematoria naar het Besluit is dubbel. Zulke afleidbare aggregaties wil de redacteur niet in de export.

## 2 De regel

**Afleidbare indeling** — De export laat de aggregatie van een groepering naar een element weg als een ander element onder dezelfde groepering boven dat element staat, met een relatie die het kennismodel als afleidbaar markeert. Wat bovenaan staat, houdt zijn aggregatie (het anker); in een kring blijft er één. Het element staat dan nog in de indeling, via het anker. Het exportrapport noemt per groepering wat wegviel en via welk element.

- *Boven* volgt de betekenis, niet de pijl van ArchiMate: bij *werkt uit* (beleidskader → beleidskader) staat het doel boven, bij *is grondslag voor* (beleidskader → element) de bron.
- Het bovenliggende element hangt onder dezelfde groepering (direct of zelf afleidbaar). Een element waarvan het bovenliggende element onder een andere groepering hangt, houdt zijn aggregatie.
- De markering staat in het kennismodel, per relatietype en vaste naam, met de kant die boven staat; per indeling staat of de regel er geldt.

## 3 Besluiten van de redacteur

| Vraag | Besluit |
|---|---|
| Welke relaties maken afleidbaar | De grondslagketen: *werkt uit* (beleidskader → beleidskader) en *is grondslag voor* (beleidskader → element). Niet *werkt uit voor*, *is model voor*, *verwijst naar*, toegang, realisatie of specialisatie. |
| In welke indelingen | Voor nu de Beleidsdomeinindeling en de Grondslagindeling. |
| Voorwaarde voor het bovenliggende element | Onder dezelfde groepering. |
| Zichtbaarheid | Alleen in het exportrapport. |
| Waar de markering staat | De redacteur wijst de relaties aan in een tussenmodel in Archi, met de eigenschap `wiki-gemma-model maakt indeling afleidbaar` op de relatie in Kennismodel-wiki, waarde `<naam>: <kant>` (bijv. `werkt uit: doel`, `is grondslag voor: bron`); de AI leest dat uit en verwerkt het in `tools/kennismodel.py`. |

## 4 Voorbeelden (export op 169b22dd)

Beleidsdomeinindeling: 97 van de 157 aggregaties vallen weg (Burgerzaken 74 van 91, Begraafplaatsen en crematoria 12 van 27, Besluitvorming 11 van 30); Grondslagindeling: 5 van de 20. Alle 102 zijn nieuw: GEMMA heeft er geen van.

| Groepering | Weg: aggregatie naar | Herleidbaar via |
|---|---|---|
| Begraafplaatsen en crematoria | Besluit op de lijkbezorging | werkt de Wet op de lijkbezorging uit |
| Begraafplaatsen en crematoria | Vervoersdocumenten stoffelijk overschot | het Besluit op de lijkbezorging is grondslag voor (dat via de Wet hangt) |
| Begraafplaatsen en crematoria | Verlof tot begraven, Grafuitgifte, Crematoriumregister, Bijzettingenregister, Begraafplaatsregister, Herbegraven of alsnog cremeren, Bijzondere begraafplaats toestemming, Ontleding stoffelijk overschot toestemming, Uitvaart vervroegen of uitstellen | de Wet op de lijkbezorging is grondslag voor |
| Begraafplaatsen en crematoria | Verzorgen gemeentebegrafenis (bedrijfsproces) | de Wet op de lijkbezorging is grondslag voor |
| Burgerzaken | Paspoortbesluit, Besluit basisregistratie personen, Besluit burgerlijke stand 1994, Besluit verkrijging en verlies Nederlanderschap | werkt de Paspoortwet, de Wet BRP, BW Boek 1 en de Rijkswet op het Nederlanderschap uit |
| Rijksregelgeving | dezelfde vijf besluiten | werken hun wet uit, die ook onder Rijksregelgeving hangt |

Wat blijft onder Begraafplaatsen en crematoria: de Wet op de lijkbezorging, de processen, de objecten (Graf, Begraafplaats, Crematorium, Urn, Stoffelijk overschot, Gemeentebegrafenis), Grafrecht en Bezorgen stoffelijk overschot. De Wet op de Nederlandse identiteitskaart blijft hangen: zij *verwijst naar* de Paspoortwet, en die naam telt niet mee.

## 5 Uitvoering

1. **Vaste naam afdwingen** *(script)*: een relatie van een type met vaste namen (`Relatie.namen`) gebruikt er een van. De filter leunt op de naam; nu controleert alleen het type. Eén afwijking vandaag: *is model voor (algemene plaatselijke verordening)* (Model-APV → Regeling); voorleggen.
2. **Kennismodel** (`tools/kennismodel.py`): een veld `afleidbaar` op `Relatie` (paren naam en kant) en op `Indeling` (de regel geldt), gevuld volgens hoofdstuk 3; de regel in *Voor alle indelingen* van `kennismodel/indelingen.md`, en *Alles ingedeeld* telt een afleidbare plaats mee.
3. **Export** (`tools/archimate_export.py`): de ankers per groepering in `_indelingen`, op de relaties van de beoordelingen die de export meeneemt; `_zonder_plaats` telt een afleidbare plaats mee; het rapport krijgt een sectie *Afleidbare aggregaties weggelaten*. Een aggregatie die GEMMA zelf al heeft, blijft (de import verwijdert niets van GEMMA); het rapport noemt haar. In Kennismodel-wiki de eigenschap `wiki-gemma-model maakt indeling afleidbaar` op elke relatie (leeg of gevuld) en op elke indeling (`ja` of `nee`), zodat de redacteur haar in Archi alleen hoeft in te vullen.
4. **Tussenmodel uitlezen**: `tools/kennismodel.py afleidbaar <bestand.archimate>` leest de eigenschap uit de relaties in Kennismodel-wiki en toont het verschil met `RELATIES`; de AI verwerkt het na het besluit van de redacteur (commit `rules`).
5. **Tests** in `tools/tests/`: anker, kring, andere groepering, een naam die niet meetelt, het tussenmodel.
6. **Documentatie**: de docstring van de export, `ARCHITECTURE.md` (de export), skill gemma-archimate-model-archimate-export (woordbudget 1300: eerst meten).
7. **Export** opnieuw, het rapport nagelopen tegen hoofdstuk 4, commit `export`. Na de import in GEMMA verwijdert het jArchi-script de 102 aggregaties, want ze hebben een oudere exportdatum.
