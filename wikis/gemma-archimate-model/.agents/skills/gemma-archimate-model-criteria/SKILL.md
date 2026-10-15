---
name: gemma-archimate-model-criteria
description: Fase A van de beoordeling in gemma-archimate-model — valt een begrip af, en zo niet, welke aard heeft het (gedrag, partij, rol, samenwerking, kanaal, plaats, aanbod, regeling of een ding) — met de vragen uit tools/bepaal_type.py vragen, in de schrijfvorm van één regel. Gebruik in fase 1 van gemma-archimate-model-update, voor elk nieuw begrip; fase B (de kenmerken van het type) staat in gemma-archimate-model-beoordelen.
metadata:
  kind: capability
  scope: wiki
  requires-tools: "python:tools/bepaal_type.py python:tools/beoordeling.py python:tools/werkpakket.py"
  reads: "bronduiding"
  writes: "beoordeling"
---

# Criteria: fase A

Het type is de uitkomst van de beslistabel (`tools/bepaal_type.py`), geen keuze vooraf (regel Beslistabel beslist). Jij beantwoordt kenmerken: neutrale eigenschappen van het begrip, elk met ja of nee, een onderbouwing en de bron-id's. De beslistabel loop je af in twee fasen. Fase A (deze skill) is de poort, met een stop als het begrip afvalt, de aard en de groep van die aard. Fase B (skill `gemma-archimate-model-beoordelen`) vraagt alleen de kenmerken van het type. Een kenmerk buiten het pad laat je weg: het script leidt nee af. De volledige vragenlijst met voorbeelden en herkomst, en de stappentabel, staan in [kenmerken en beslistabel](../../../kennismodel/kenmerken-en-beslistabel.md); lees die alleen bij twijfel over een kenmerk.

## Stappen

1. **Begrippen verzamelen.** De begrippen van het onderwerp staan in het werkpakket (sectie Begrippen): de kernbegrippen uit de bronduidingen en de beoordelingen die het onderwerp al kent. Kijk per partij ook naar kanalen, beleidskaders en samenwerkingen. Het GGM is matchdoel, geen bron: een GGM-entiteit wordt geen begrip omdat het GGM haar kent, en een begrip uit de bronnen sla je niet over omdat het GGM het al kent. Een GGM-entiteit van het beleidsdomein die de bronnen niet noemen, noem je in de tabel; zoek een bron als ze ertoe doet.
2. **Welk begrip? (stap 0)** Een ander woord voor een element dat bestaat of nu wordt beoordeeld: `synoniem_van`, met de context van het woord. Dezelfde naam voor een ander begrip, in de wiki, het GGM, het GEMMA-model of een bron (de naamgenoten '=' in het werkpakket): `homoniem_van`, en de naamkeuze gaat in de tabel. Een actor of rol en een bedrijfsobject met dezelfde naam zijn een tegenhanger, geen homoniem. Staat een begrip niet in het werkpakket: `uv run python tools/beoordeling.py zoek <naam> [<synoniem> …]`.
3. **Naam en thuisonderwerp.** De naam is de gangbare term uit beleid en praktijk; de wetsterm wordt een synoniem met context "wet" (regel Bronvoorrang). Het id is de naam in kleine letters met koppeltekens. Het thuisonderwerp volgt uit de inhoud (regel Thuishoren) en staat als eerste in `onderwerpen`; de beoordeling staat in `onderwerpen/<thuisonderwerp>/beoordelingen/<id>.yaml`. Hoort het begrip bij een onderwerp dat nog niet bestaat, dan is *betekenis in onderwerp* nee (een verwijzing).
4. **De vragen.** `uv run python tools/bepaal_type.py vragen` geeft de vragen van fase A met voorbeelden; één keer per Sessie.
5. **Schrijven.** Per kenmerk één regel onder `kenmerken:`, in de volgorde van de vragen:

   ```yaml
   begrip: Ruimen graf
   onderwerpen: [lijkbezorging]
   kenmerken:
     herkenbaar: ja — De wet regelt het ruimen van graven (art. 31). [2026-rijk-wet-op-de-lijkbezorging-wettekst]
     buiten_dit_model: nee — Gedrag, geen doel of norm.
     handelende_partij: nee
   ```

   Een ja heeft de bron-id's tussen haken; een plek in een GEMMA-indeling het id van de GEMMA-relatie (`[id-…]`). Een nee in de poort heeft een onderbouwing; in Aard en Soort gedrag is een kale nee genoeg. Zet de tekst tussen aanhalingstekens als hij `: ` of ` #` bevat. Bij "Noem …" hoort bij ja een concreet begrip, artikel of relatie uit de bronnen; staat die niet in de bronduiding, vul dan eerst de bronduiding aan. Valt het begrip af, stop dan bij dat kenmerk, met `genoemd_begrip` (bij *slechts eigenschap* en bij *eigen identiteit* nee) of `archimate_buiten_model` (bij *buiten dit model*), en een `toelichting` van één zin voor de begrippenlijst. Bij *waarneembare vorm* ja is `genoemd_begrip` het object. Een begrip dat afvalt, blijft in de begrippenlijst staan. Ken je het kernobject van een proces, dienst of gebeurtenis al, zet dan ook `kernobject: <id>`.
6. **Normaliseren.** `uv run python tools/beoordeling.py normaliseer <id> …` maakt van de regels de opgeslagen vorm, laat een nee buiten het pad weg en noemt wat op het pad nog open staat. Een fout los je op in de regel; lees het bestand niet terug. De eerste regel van `uv run python tools/bepaal_type.py vragen <id>` noemt het type voor fase B ("Fase B, Bedrijfsproces"). `tools/beslissen.py` draai je pas in fase B.

## Let op

- Een eigenschap of waarde van een ander begrip (`uv run python tools/ggm.py attribuut <term>`) is *slechts eigenschap* ja, met dat begrip als `genoemd_begrip`. Een doelgroep (minima, jongeren) is geen actor of rol maar een indeling van een actor: *slechts eigenschap* ja, met de actor als `genoemd_begrip`.
- *Handelende partij*, *hoedanigheid* en *samenwerkingsverband* leiden naar actor, rol en bedrijfssamenwerking; in fase B beslissen *los van verantwoordelijkheid* en *eigen rechtspersoon* ertussen.
- Een concreet benoemde regeling als geheel is *regeling als geheel*; een los artikel is *buiten dit model*; een soort regeling is een ding (Regeling); een richtlijn blijft bron (modelleerafspraken van [Beleidskader](../../../kennismodel/motivatie/beleidskader-modelleerafspraken.md)). Een wet die de UPL als grondslag van een UPL-item noemt, haal je op als bron; zij wordt alleen een beleidskader als ze de gemeente een taak of bevoegdheid geeft. Een wet met alleen een tarief of een regel buiten de gemeentelijke taak (Wet griffierechten burgerlijke zaken, art. 23) blijft bron; zoek dan de bevoegdheidsgrondslag. Een verdrag blijft bron zolang de criteria geen regelgever verdrag kennen.
- Bij gedrag kiest *soort gedrag* tussen proces, procesgroep, functie, gebeurtenis, dienst en bedrijfsinteractie. Het procesniveau (levensloopproces, bedrijfsproces, deelproces) volgt in fase B; voor de tabel noem je het verwachte niveau.
