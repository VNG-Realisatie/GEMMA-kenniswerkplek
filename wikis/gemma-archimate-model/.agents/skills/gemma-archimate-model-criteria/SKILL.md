---
name: gemma-archimate-model-criteria
description: Fase A van de beoordeling in gemma-archimate-model — valt een begrip af (alleen een poortafwijking), en zo niet, in welk vak van de ArchiMate-matrix valt het, met welk hoofdkenmerk en welke soort gedrag — met de vragen uit tools/bepaal_type.py vragen. Gebruik in fase 1 van gemma-archimate-model-update, voor elk nieuw begrip; fase B (de kenmerken van het type) staat in gemma-archimate-model-beoordelen.
metadata:
  kind: capability
  scope: wiki
  requires-tools: "python:tools/bepaal_type.py python:tools/beoordeling.py python:tools/werkpakket.py"
  reads: "bronduiding"
  writes: "beoordeling"
---

# Criteria: fase A

Het type is de uitkomst van de beslistabel (`tools/bepaal_type.py`), geen keuze vooraf (regel Beslistabel beslist). Fase A (deze skill) kiest drie velden: het **vak** in de ArchiMate-matrix (`vak`: laag, aspect, intern of extern), het **hoofdkenmerk** als het vak er meer heeft (`hoofdkenmerk`, alleen bij `bedrijf/actief-intern`), en bij gedrag intern de **soort gedrag** (`soort_gedrag`). Daarna de kenmerken van de groep van het hoofdkenmerk. De poort schrijf je alleen bij een afwijking: zonder antwoord is zij doorlopen en steunt zij op de bronnen van de beoordeling (`bronnen`). Fase B (skill `gemma-archimate-model-beoordelen`) vraagt alleen de kenmerken van het type. Een kenmerk buiten het pad laat je weg: het script leidt de standaardwaarde af. De matrix, de vragen per vak en de stappentabel staan in [kenmerken en beslistabel](../../../kennismodel/kenmerken-en-beslistabel.md); lees die alleen bij twijfel.

## Stappen

1. **Begrippen verzamelen.** De begrippen van het onderwerp staan in het werkpakket (sectie Begrippen): de kernbegrippen uit de bronduidingen en de beoordelingen die het onderwerp al kent. Kijk per partij ook naar kanalen, beleidskaders en samenwerkingen. Het GGM is matchdoel, geen bron: een GGM-entiteit wordt geen begrip omdat het GGM haar kent, en een begrip uit de bronnen sla je niet over omdat het GGM het al kent. Een GGM-entiteit van het beleidsdomein die de bronnen niet noemen, noem je in de tabel; zoek een bron als ze ertoe doet.
2. **Welk begrip? (stap 0)** Een ander woord voor een element dat bestaat of nu wordt beoordeeld: `synoniem_van`, met de context van het woord. Dezelfde naam voor een ander begrip, in de wiki, het GGM, het GEMMA-model of een bron (de naamgenoten '=' in het werkpakket): `homoniem_van`, en de naamkeuze gaat in de tabel. Een actor of rol en een bedrijfsobject met dezelfde naam zijn een tegenhanger, geen homoniem. Staat een begrip niet in het werkpakket: `uv run python tools/beoordeling.py zoek <naam> [<synoniem> …]`.
3. **Naam en thuisonderwerp.** De naam is de gangbare term uit beleid en praktijk; de wetsterm wordt een synoniem met context "wet" (regel Bronvoorrang). Het id is de naam in kleine letters met koppeltekens. Het thuisonderwerp volgt uit de inhoud (regel Thuishoren) en staat als eerste in `onderwerpen`; de beoordeling staat in `onderwerpen/<thuisonderwerp>/beoordelingen/<id>.yaml`. Hoort het begrip bij een onderwerp dat nog niet bestaat, dan is *betekenis in onderwerp* nee (een verwijzing).
4. **De vragen.** `uv run python tools/bepaal_type.py vragen` geeft de vragen van fase A met voorbeelden; één keer per Sessie.
5. **Schrijven.** De velden bovenaan, de bronnen van de beoordeling, en alleen een afwijking van de poort:

   ```yaml
   begrip: Ruimen graf
   vak: bedrijf/gedrag-intern
   soort_gedrag: per_keer_doorlopen
   onderwerpen: [lijkbezorging]
   bronnen: [2026-rijk-wet-op-de-lijkbezorging-wettekst]
   kenmerken: {}
   ```

   Een afwijking van de poort of een kenmerk van de groep schrijf je als één regel onder `kenmerken:`: `eigen_identiteit: nee — Een deelstap van de uitgifte (art. 28).`; een ja met de bron-id's tussen haken. Zet de tekst tussen aanhalingstekens als hij `: ` of ` #` bevat. Bij "Noem …" hoort bij ja een concreet begrip, artikel of relatie uit de bronnen; staat die niet in de bronduiding, vul dan eerst de bronduiding aan. Valt het begrip af, stop dan bij dat kenmerk, met `genoemd_begrip` (bij *slechts eigenschap* en bij *eigen identiteit* nee) of `archimate_buiten_model` (bij *buiten dit model*), en een `toelichting` van één zin voor de begrippenlijst. Bij *waarneembare vorm* ja is `genoemd_begrip` het object. Een begrip dat afvalt, blijft in de begrippenlijst staan. Ken je het kernobject van een proces, dienst of gebeurtenis al, zet dan ook `kernobject: <id>`.
6. **Normaliseren.** `uv run python tools/beoordeling.py normaliseer <id> …` maakt van de regels de opgeslagen vorm, laat een nee buiten het pad weg en noemt wat op het pad nog open staat. Een fout los je op in de regel; lees het bestand niet terug. De eerste regel van `uv run python tools/bepaal_type.py vragen <id>` noemt het type voor fase B ("Fase B, Bedrijfsproces"). `tools/beslissen.py` draai je pas in fase B.

## Let op

- Een eigenschap of waarde van een ander begrip (`uv run python tools/ggm.py attribuut <term>`) is *slechts eigenschap* ja, met dat begrip als `genoemd_begrip`. Een doelgroep (minima, jongeren) is geen actor of rol maar een indeling van een actor: *slechts eigenschap* ja, met de actor als `genoemd_begrip`.
- In `bedrijf/actief-intern` leiden *handelende partij*, *hoedanigheid* en *samenwerkingsverband* naar actor, rol en bedrijfssamenwerking; *los van verantwoordelijkheid* en *eigen rechtspersoon* beslissen ertussen. Een samenwerkingsverband met eigen rechtspersoon (GGD) blijft *samenwerkingsverband*, ook waar het als partij optreedt.
- Een concreet benoemde regeling als geheel is *regeling als geheel*; een los artikel is *buiten dit model*; een soort regeling is een ding (Regeling); een richtlijn blijft bron (modelleerafspraken van [Beleidskader](../../../kennismodel/motivatie/beleidskader-modelleerafspraken.md)). Een wet die de UPL als grondslag van een UPL-item noemt, haal je op als bron; zij wordt alleen een beleidskader als ze de gemeente een taak of bevoegdheid geeft. Een wet met alleen een tarief of een regel buiten de gemeentelijke taak (Wet griffierechten burgerlijke zaken, art. 23) blijft bron; zoek dan de bevoegdheidsgrondslag. Een verdrag blijft bron zolang de criteria geen regelgever verdrag kennen.
- Bij gedrag kiest het vak tussen intern en extern (een dienst); intern kiest *soort gedrag* tussen proces, procesgroep, functie, gebeurtenis en bedrijfsinteractie. Het procesniveau (levensloopproces, bedrijfsproces, deelproces) volgt in fase B; voor de tabel noem je het verwachte niveau.
- Een vermogen (wat de gemeente moet kunnen, gerealiseerd door ten minste twee functies) is `vak: strategie/gedrag`, zonder hoofdkenmerk. Je leidt haar af uit de functies en diensten van een onderwerp: skill `gemma-archimate-model-beoordelen`, `references/capability.md`.
