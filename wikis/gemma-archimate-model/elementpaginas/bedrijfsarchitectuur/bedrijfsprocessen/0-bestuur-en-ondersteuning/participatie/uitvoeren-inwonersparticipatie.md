---
id: uitvoeren-inwonersparticipatie
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Uitvoeren inwonersparticipatie
onderwerpen:
- participatie
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Participatie
definitie: Het op initiatief van de gemeente betrekken van inwoners en maatschappelijke partijen bij de voorbereiding, uitvoering of evaluatie van beleid.
match:
  gemma: partieel
data_object: nee
procesniveau: levensloopproces
afnemer: extern
synoniemen:
- Inwonersparticipatie (beleid)
- Generiek deelproces Uitvoeren participatie (GEMMA)
bronnen:
- 2024-vng-implementatiehandleiding-model-participatieverordening
- 2026-rijk-gemeentewet-wettekst
- 2024-vng-model-participatieverordening
gemma_id: id-fcd03bc4-cf22-493d-ad97-fba88be7b13a
gemma_naam: Generiek deelproces Uitvoeren participatie
gemma_type: business-process
gemma_map: Business / Procesarchitectuur / Vaststellen omgevingsplan
gemma_eigenschappen:
  Object ID: fcd03bc4-cf22-493d-ad97-fba88be7b13a
---

# Uitvoeren inwonersparticipatie

<!-- Gegenereerd door tools/render.py uit de beoordeling uitvoeren-inwonersparticipatie.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Ter discussie

- Beleidsdomein: het GGM kent onder taakveld 0 alleen Griffie, en de wiki gebruikt Besluitvorming voor de algemene bestuursrechtelijke procedures. Participatie past in geen van beide: het is een eigen taak uit art. 150 Gemeentewet met eigen kernobjecten (Participatieplan, Verzoek uitdaagrecht). Advies: een gemeentelijk beleidsdomein Participatie onder 0 Bestuur en Ondersteuning (zo ingevuld bij dit proces, Participatieplan en Eindverslag inwonersparticipatie), met een beschrijving in het register van beleidsdomeinen en een GGM-terugmelding (hiaat). Alternatief: Besluitvorming, maar dat is een thematisch onderwerp en geen eigen taak.
- Procesniveau: dit proces omvat de hele levensloop van één participatieplan, van opstellen tot het eindverslag, en is daarom een levensloopproces (bedrijfsproces in ArchiMate) met kernobject Participatieplan; besluit K4 noemt het een eigen bedrijfsproces. Er is geen ander proces op het participatieplan, dus geen bedrijfsproces eronder. Advies: levensloopproces bevestigen; de deelprocessen (plan, betrekken, eindverslag) staan in deelprocessen.

## Betekenis

### Definitie

Het op initiatief van de gemeente betrekken van inwoners en maatschappelijke partijen bij de voorbereiding, uitvoering of evaluatie van beleid.

### Beschrijving

De raad regelt in een verordening hoe ingezetenen en belanghebbenden bij de voorbereiding, uitvoering en evaluatie van gemeentelijk beleid worden betrokken ([2026-rijk-gemeentewet-wettekst](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-gemeentewet-wettekst.md), art. 150 lid 1). Elk bestuursorgaan (raad, college of burgemeester) besluit over zijn eigen beleid of inwonersparticipatie plaatsvindt ([2024-vng-model-participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md), var. 1 art. 2 lid 1).

Vooraf stelt het bestuursorgaan een participatieplan op en maakt het openbaar; daarna betrekt het inwoners en maatschappelijke partijen in de gekozen vorm, van informeren tot beslissen; na afloop stelt het een eindverslag op en maakt het openbaar ([2024-vng-model-participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md), var. 1 art. 3–5; var. 2 art. [7], [10]). Bereidt het college een besluit van de raad voor, dan stelt het college plan en eindverslag op en informeert het de raad (var. 1 art. 3 lid 3, 5 lid 3).

Kiest het bestuursorgaan voor inspraak, of is inspraak wettelijk verplicht, dan verloopt de inspraak via de uniforme openbare voorbereidingsprocedure van afdeling 3.4 Awb, tenzij de verordening of het bestuursorgaan een ander proces vaststelt ([2026-rijk-gemeentewet-wettekst](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-gemeentewet-wettekst.md), art. 150 lid 2; [2024-vng-model-participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md), var. 1 art. 4, var. 2 art. [8]).

De VNG-modelverordening sluit inwonersparticipatie facultatief uit, onder meer bij spoed, bij uitvoering van hogere regelgeving zonder beleidsvrijheid, bij interne aangelegenheden en bij begroting, tarieven en belastingen; haar termijnen zijn voorbeeldwaarden die de gemeente zelf invult ([2024-vng-model-participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md), var. 1 art. 2 lid 3, 3 lid 1, 5 lid 1).

### Deelprocessen

1. **Opstellen participatieplan**: Het bestuursorgaan stelt vóór de voorbereiding, uitvoering of evaluatie van het beleid een plan op met het beleid, het doel, het proces en de planning van de participatie, en maakt het openbaar; bij een besluit van de raad doet het college dat en informeert het de raad. [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) (var. 1 art. 3; var. 2 art. [7])
2. **Betrekken inwoners en maatschappelijke partijen**: Het bestuursorgaan betrekt inwoners en maatschappelijke partijen in de vorm uit het plan; bij inspraak volgt het de uniforme openbare voorbereidingsprocedure, tenzij het een ander proces vaststelt. Het college zorgt voor laagdrempelige ondersteuning van deelnemers. [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) (var. 1 art. 4; var. 2 art. [8], [9])
3. **Opstellen eindverslag**: Na afloop stelt het bestuursorgaan een eindverslag op met het gevolgde proces, de uitkomsten, een onderbouwde reactie daarop en een evaluatie, en maakt het openbaar. [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) (var. 1 art. 5; var. 2 art. [10])

### Synoniemen

| Synoniem | Context |
|---|---|
| Inwonersparticipatie | beleid |
| Generiek deelproces Uitvoeren participatie | GEMMA |

## Plaats in het model

### Typering

Bedrijfsproces, niveau levensloopproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: levensloopproces.
- **Beleidsdomeinindeling**: beleidsdomein Participatie, taakveld 0 Bestuur en Ondersteuning (van het kernobject).
- **Kernobject**: [Participatieplan](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/participatie/participatieplan.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Participatie.

### Kenmerken

Alleen de kenmerken met ja; de overige 45 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, inwonersparticipatie: het op initiatief van de gemeente betrekken van inwoners bij voorbereiding, uitvoering of evaluatie van beleid (bijlage 1; art. 150 lid 1). [VNG Implementatiehandleiding participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/richtlijn/2024-vng-implementatiehandleiding-model-participatieverordening.md), [Gemeentewet](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-gemeentewet-wettekst.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, het bestuursorgaan beslist of participatie plaatsvindt, stelt het plan op en maakt het eindverslag openbaar (var. 1 art. 2, 3, 5). [VNG Implementatiehandleiding participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/richtlijn/2024-vng-implementatiehandleiding-model-participatieverordening.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, een eigen traject met plan vooraf en eindverslag achteraf, niet een stap van één ander proces. [VNG Implementatiehandleiding participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/richtlijn/2024-vng-implementatiehandleiding-model-participatieverordening.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort bij participatie. [Gemeentewet](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-gemeentewet-wettekst.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, het betrekken van inwoners bij beleid. [VNG Implementatiehandleiding participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/richtlijn/2024-vng-implementatiehandleiding-model-participatieverordening.md) |
| **per keer doorlopen**: Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? | Ja, per beleidsvoornemen van besluit tot participatie, via het plan, tot het eindverslag (var. 1 art. 2–5). [VNG Implementatiehandleiding participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/richtlijn/2024-vng-implementatiehandleiding-model-participatieverordening.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, beslisser: het bevoegde bestuursorgaan (raad, college of burgemeester) besluit over zijn eigen beleid of inwonersparticipatie plaatsvindt, stelt plan en eindverslag op; het college bij voorbereiding van een raadsbesluit (var. 1 art. 2 lid 1, 3 lid 3, 5 lid 3). [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, registreert het participatieplan en het eindverslag en maakt ze openbaar (var. 1 art. 3 lid 1, 5 lid 1). [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, het besluit van het bestuursorgaan dat over zijn beleid inwonersparticipatie plaatsvindt, voorafgaand aan de voorbereiding, uitvoering of evaluatie van dat beleid (var. 1 art. 2 lid 1, 3 lid 1). [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, het openbare eindverslag met proces, uitkomsten, een onderbouwde reactie en een evaluatie (var. 1 art. 5; var. 2 art. [10]). [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elk beleid waarover een bestuursorgaan inwonersparticipatie laat plaatsvinden (var. 1 art. 2 lid 1). [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, art. 150 lid 1 en 2 (verordening, inspraak via afdeling 3.4 Awb); in de VNG-modelverordening plan, inspraak en eindverslag met termijnen (var. 1 art. 3–5; var. 2 art. [7]–[10]). [Gemeentewet](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-gemeentewet-wettekst.md), [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, van het besluit dat inwonersparticipatie plaatsvindt tot het openbare eindverslag (var. 1 art. 2 lid 1, 5 lid 1). [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) |
| **omvat levensloop**: Omvat het het gedrag over de hele levensloop van één exemplaar van een bedrijfsobject, van ontstaan tot einde, of, binnen een ketensamenwerking, het deel van die levensloop dat één partij uitvoert? | Ja, omvat de hele levensloop van één participatieplan, van opstellen en openbaar maken vóór de participatie tot het eindverslag na afloop (var. 1 art. 3, 5; var. 2 art. [7], [10]). [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder proces in de wiki; Participatie (var. 2 art. 1) is het onderwerp zelf en geen element. [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Uitvoeren inwonersparticipatie | stelt op en maakt openbaar *toegang (registreren)* | [Participatieplan](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/participatie/participatieplan.md) | [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) (var. 1 art. 3 lid 1, 3; var. 2 art. [7] lid 1, 3) |
| Uitvoeren inwonersparticipatie | stelt op en maakt openbaar *toegang (registreren)* | [Eindverslag inwonersparticipatie](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/participatie/eindverslag-inwonersparticipatie.md) | [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) (var. 1 art. 5 lid 1, 3; var. 2 art. [10] lid 1, 3) |
| Uitvoeren inwonersparticipatie | leidt tot (bij inspraak) *triggering* | [Uitvoeren uniforme openbare voorbereidingsprocedure](../besluitvorming/uitvoeren-uniforme-openbare-voorbereidingsprocedure.md) | [Gemeentewet](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-gemeentewet-wettekst.md), [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) (Gemeentewet art. 150 lid 2; var. 1 art. 4; var. 2 art. [8]) |
| Uitvoeren inwonersparticipatie | stelt het plan op aan de hand van (participatiebeleid) *toegang (raadplegen)* | [Beleidsnota](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beleidsnota.md) | [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) (var. 1 art. 3 lid 1; var. 2 art. [7] lid 1) |
| Uitvoeren inwonersparticipatie | volgt de regels van *toegang (raadplegen)* | [Participatieverordening](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/participatieverordening.md) | [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) (var. 1 art. 2–5; var. 2 art. [3]–[10]) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beslisser](../../../rollen/beslisser.md) | besluit over inwonersparticipatie en stelt plan en eindverslag op *toewijzing* | Uitvoeren inwonersparticipatie | [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) (var. 1 art. 2 lid 1, 3 lid 1, 5 lid 1; var. 2 art. [3], [7], [10]) |
| [Gemeentewet](../../../../motivatie/beleidskaders/rijksregelgeving/gemeentewet.md) | is grondslag voor *associatie (gericht)* | Uitvoeren inwonersparticipatie | [Gemeentewet](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-gemeentewet-wettekst.md) (art. 150 lid 1 en 2) |
| [Model Participatieverordening](../../../../motivatie/beleidskaders/gemeentelijke-regelgeving/model-participatieverordening.md) | werkt uit voor *associatie (gericht)* | Uitvoeren inwonersparticipatie | [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) (var. 1 art. 2–5, var. 2 art. [3], [7]–[10]) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [VNG Implementatiehandleiding participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/richtlijn/2024-vng-implementatiehandleiding-model-participatieverordening.md) | Implementatiehandleiding VNG Model Participatieverordening 2024 |
| [Gemeentewet](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-gemeentewet-wettekst.md) | Gemeentewet (BWBR0005416) |
| [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) | VNG Model Participatieverordening 2024 |

### Afstemming met GEMMA

Match **partieel** met GEMMA-element *Generiek deelproces Uitvoeren participatie* (business-process). GEMMA kent het Generiek deelproces Uitvoeren participatie, zonder definitie, in de procesarchitectuur van Vaststellen omgevingsplan, waar het de Deelservice Participatie realiseert. Dit element is breder en van een ander niveau, een eigen proces van plan tot eindverslag voor beleid in elk domein; de export geeft het GEMMA-element deze naam en definitie (besluit K4, voorleggen in fase 3).

### Besluiten redacteur

- 2026-10-15: Eigen bedrijfsproces met Participatieplan als kernobject, geen deelproces van het vaststellen van beleid en geen bedrijfsinteractie: eigen aanleiding, plan en eindverslag van het bestuursorgaan.
