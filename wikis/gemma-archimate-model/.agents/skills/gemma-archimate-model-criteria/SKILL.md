---
name: gemma-archimate-model-criteria
description: Afbakenen en Typeren in de beoordeling van gemma-archimate-model — wordt een begrip een eigen element (scope en afhankelijkheid), en zo ja, in welk vak van de ArchiMate-matrix valt het, met welk hoofdkenmerk, welke soort gedrag en welk niveau — met de vragen uit tools/bepaal_type.py vragen. Gebruik in Sessie 1 van gemma-archimate-model-update, voor elk nieuw begrip; Onderbouwen (de toetskenmerken van het type) staat in gemma-archimate-model-beoordelen.
metadata:
  kind: capability
  scope: wiki
  requires-tools: "python:tools/bepaal_type.py python:tools/beoordeling.py python:tools/werkpakket.py"
  reads: "bronduiding"
  writes: "beoordeling"
---

# Criteria: Afbakenen en Typeren

Het type is de uitkomst van de beslistabel (`tools/bepaal_type.py`), geen keuze vooraf (regel Beslistabel beslist). Afbakenen beantwoordt de vraag of het begrip een eigen element wordt: stap 0 (welk begrip), stap 1 (scope: alleen een afwijking) en stap 2 (*afhankelijkheid*). Typeren kiest het type en het niveau (stap 3): het **vak** (`vak`), het **hoofdkenmerk** als het vak er meer heeft (`hoofdkenmerk`: bij `bedrijf/actief-intern` een partij, bij `bedrijf/passief` object, afspraak of representatie), de **soort gedrag** (`soort_gedrag`), de kenmerken van het hoofdkenmerk (*eigen rechtspersoon*, *soort partij*, *landelijk*), het **procesniveau** bij een proces en de **interactievorm** bij een bedrijfsinteractie. Stap 4, de grondslag, doet het script. Een kenmerk buiten het pad laat je weg: het script leidt het standaardantwoord af, en een antwoord zonder eigen bron steunt op `bronnen` van de beoordeling, de hoofdbron eerst. Onderbouwen (skill `gemma-archimate-model-beoordelen`) vraagt alleen de toetskenmerken van het type. Matrix, waarden en stappentabel: [kenmerken en beslistabel](../../../kennismodel/kenmerken-en-beslistabel.md), alleen bij twijfel.

## Stappen

1. **Begrippen verzamelen.** De begrippen van het onderwerp staan in het werkpakket (sectie Begrippen): de kernbegrippen uit de bronduidingen en de beoordelingen die het onderwerp al kent. Kijk per partij ook naar kanalen, beleidskaders en samenwerkingen. Het GGM is matchdoel, geen bron: een GGM-entiteit wordt geen begrip omdat het GGM haar kent, en een begrip uit de bronnen sla je niet over omdat het GGM het kent. Noem een GGM-entiteit van het beleidsdomein die de bronnen niet noemen in de tabel.
2. **Welk begrip? (stap 0)** Een ander woord voor een element dat bestaat of nu wordt beoordeeld: `synoniem_van`, met de context van het woord. Dezelfde naam voor een ander begrip, in de wiki, het GGM, het GEMMA-model of een bron (de naamgenoten '=' in het werkpakket): `homoniem_van`, en de naamkeuze gaat in de tabel. Een actor of rol en een bedrijfsobject met dezelfde naam zijn een tegenhanger (veld `tegenhanger`), geen homoniem. Niet in het werkpakket: `uv run python tools/beoordeling.py zoek <naam> [<synoniem> …]`.
3. **Naam en thuisonderwerp.** De naam is de gangbare term uit beleid en praktijk; de wetsterm wordt een synoniem met context "wet" (regel Bronvoorrang). Het id is de naam in kleine letters met koppeltekens. Het thuisonderwerp volgt uit de inhoud (regel Thuishoren) en staat als eerste in `onderwerpen`; de beoordeling staat in `onderwerpen/<thuisonderwerp>/beoordelingen/<id>.yaml`. Hoort het begrip bij een onderwerp dat nog niet bestaat, dan is *betekenis in onderwerp* nee (een verwijzing).
4. **De vragen.** `uv run python tools/bepaal_type.py vragen` geeft de vragen met voorbeelden; één keer per Sessie.
5. **Schrijven.** De keuzevelden bovenaan, de bronnen van de beoordeling, en alleen een afwijking:

   ```yaml
   begrip: Verlenen grafrecht
   vak: bedrijf/gedrag-intern
   soort_gedrag: per_keer_doorlopen
   onderwerpen: [lijkbezorging]
   bronnen: [2026-rijk-wet-op-de-lijkbezorging-wettekst]
   kernobject: grafrecht
   kenmerken:
     procesniveau: bedrijfsproces — Een mutatie in de levensloop van het grafrecht (art. 28).
   ```

   Een keuzekenmerk of een kenmerk van het hoofdkenmerk schrijf je als één regel onder `kenmerken:`: de waarde (ja, nee of de keuze), een onderbouwing met de vindplaats, en de bron-id's tussen haken als de bron niet die van de beoordeling is. Bij "Noem …" hoort bij ja een concreet begrip, artikel of relatie uit de bronnen; ontbreekt die in de bronduiding, vul die dan aan. Valt het begrip af, stop dan bij die afwijking, met `genoemd_begrip` (bij *afhankelijkheid* of representatie) of `archimate_buiten_model` (bij *buiten dit model*), en een `toelichting` van één zin voor de begrippenlijst. Een begrip dat afvalt, blijft in de begrippenlijst staan.
6. **Normaliseren.** `uv run python tools/beoordeling.py normaliseer <id> …` maakt van de regels de opgeslagen vorm, laat een kenmerk met het standaardantwoord weg en noemt wat op het pad nog open staat. Een fout los je op in de regel. De eerste regel van `uv run python tools/bepaal_type.py vragen <id>` noemt het type voor Onderbouwen. `tools/beslissen.py` draai je pas in Sessie 2.

## Let op

- *Afhankelijkheid* is één keuze met het begrip waarvan het afhangt in `genoemd_begrip`: een eigenschap of waarde (`tools/ggm.py attribuut <term>`; ook een doelgroep), een onderdeel, een deelproces (geen klant tot klant), een variant (geen eigen gegevens, regels of werkwijze) of invoer van een ander. Bij een variant kijk je eerst naar boven: de generalisaties in de wiki, het GGM (`tools/ggm.py generalisaties`) en GEMMA (`tools/gemma.py zoek`); kies het hoogste niveau dat domeinexperts herkennen, zonder kunstmatige verzamelnaam (`references/hierarchie.md`). Het type van een variant volgt uit dat begrip.
- Een proces kiest het *procesniveau* (levensloopproces, bedrijfsproces of cluster naar soort werk) met het kernobject; het script toetst de samenhang. Een bedrijfsinteractie kiest de *interactievorm*: estafette of orkestratie.
- In `bedrijf/actief-intern` leiden *handelende partij*, *hoedanigheid* en *samenwerkingsverband* naar actor, rol en bedrijfssamenwerking; *eigen rechtspersoon* beslist bij een verband, en *los van verantwoordelijkheid* volgt uit het hoofdkenmerk (alleen een afwijking). Een samenwerkingsverband met eigen rechtspersoon (GGD) blijft *samenwerkingsverband*.
- Een concreet benoemde regeling als geheel is *regeling als geheel*; een los artikel is *buiten dit model*; een soort regeling is een ding (Regeling); een richtlijn blijft bron (modelleerafspraken van [Beleidskader](../../../kennismodel/motivatie/beleidskader-modelleerafspraken.md)). Een wet die de UPL als grondslag noemt, haal je op als bron; zij wordt alleen een beleidskader als ze de gemeente een taak of bevoegdheid geeft. Een wet met alleen een tarief of een regel buiten de gemeentelijke taak blijft bron; zoek dan de bevoegdheidsgrondslag. Een verdrag blijft bron.
- Een vermogen (wat de gemeente moet kunnen, gerealiseerd door ten minste twee functies) is `vak: strategie/gedrag`, zonder hoofdkenmerk. Je leidt haar af uit de functies en diensten van een onderwerp: skill `gemma-archimate-model-beoordelen`, `references/capability.md`.
