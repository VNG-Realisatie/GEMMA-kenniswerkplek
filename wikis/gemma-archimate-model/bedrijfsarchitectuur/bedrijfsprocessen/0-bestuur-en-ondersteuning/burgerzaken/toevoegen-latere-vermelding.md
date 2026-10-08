---
id: toevoegen-latere-vermelding
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Toevoegen latere vermelding
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het toevoegen van een rechterlijke uitspraak of een besluit over de staat van een persoon aan een akte als latere vermelding.
grondslag: bron
match:
  gemma: geen
data_object: nee
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Verwerken rechterlijke uitspraak (beleid)
bronnen:
- 2026-rvig-hup-vaststelling-ouderschap
- 2026-rvig-hup-ontkenning-ouderschap
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493
- 2026-rvig-hup-adoptie
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen
---

# Toevoegen latere vermelding

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/toevoegen-latere-vermelding.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het toevoegen van een rechterlijke uitspraak of een besluit over de staat van een persoon aan een akte als latere vermelding.

### Beschrijving

Een latere vermelding legt een verandering vast die na het opmaken van de akte is ontstaan: een adoptie of herroeping daarvan, een ontkenning of gerechtelijke vaststelling van het ouderschap, een vernietigde erkenning, of een wijziging van de voornaam (rechtbank) of geslachtsnaam (Koning) (BW 1 art. 4, 7, 20; Besluit burgerlijke stand art. 53, 54; HUP Adoptie; HUP Vaststelling ouderschap). De gemeente waar de akte berust, voegt de vermelding toe; de woongemeente verwerkt de wijziging in de BRP.

De gemeente beslist hier niet zelf over de staat van de persoon: de rechtbank of de Koning heeft beslist. Het geslacht (BW 1 art. 28b) en de ontbinding van een huwelijk of partnerschap hebben een eigen bedrijfsproces.

### Synoniemen

| Synoniem | Context |
|---|---|
| Verwerken rechterlijke uitspraak | beleid |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md).
- **Kernobject**: [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md).
- **Gestart door gebeurtenis**: [Adoptie](../../../gebeurtenissen/adoptie.md), [Naamswijziging](../../../gebeurtenissen/naamswijziging.md), [Ontkenning ouderschap](../../../gebeurtenissen/ontkenning-ouderschap.md), [Vaststelling ouderschap](../../../gebeurtenissen/vaststelling-ouderschap.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 44 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, de ambtenaar voegt latere vermeldingen toe aan akten (BW 1 art. 20; Besluit burgerlijke stand art. 15-17, 53). [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, taak van de ambtenaar van de burgerlijke stand van de gemeente waar de akte berust (BW 1 art. 20). [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gedaan wordt. [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **per keer doorlopen**: Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? | Ja, wordt per geval van begin tot eind doorlopen. [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, ambtenaar van de burgerlijke stand (BW 1 art. 20). [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, bijwerkt de akte van de burgerlijke stand met een latere vermelding (BW 1 art. 20). [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, een rechterlijke uitspraak of besluit dat de staat van een persoon verandert: adoptie, ontkenning of vaststelling van ouderschap, wijziging van voornaam of geslachtsnaam, vernietiging van een erkenning (BW 1 art. 20; Besluit burgerlijke stand art. 53; HUP Adoptie). [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md), [HUP BRP: Adoptie](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-adoptie.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een latere vermelding op de akte, maandelijks doorgestuurd naar de centrale bewaarplaats (Besluit burgerlijke stand art. 31). [Besluit burgerlijke stand 1994](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, BW 1 art. 20, 20a; Besluit burgerlijke stand art. 15-17, 31, 53, 54. [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, draagt bij aan Bijhouden burgerlijke stand: één mutatie van een bestaande akte. [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van de uitspraak of het besluit dat de staat verandert tot de latere vermelding. [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md), [HUP BRP: Adoptie](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-adoptie.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, realiseert de diensten waarbij de gemeente een uitspraak of besluit verwerkt, zoals Achternaamwijziging en Voornaamwijziging (UPL nr. 5, 460). [UPL-lijst extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip van hetzelfde type in deze wiki. [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Toevoegen latere vermelding | voegt latere vermelding toe aan *toegang (bijwerken)* | [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md) | [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 20) |
| Toevoegen latere vermelding | realiseert *realisatie* | [Achternaamwijziging](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/achternaamwijziging.md) | [UPL-lijst extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Voornaam of achternaam veranderen](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) (UPL nr. 5; Utrecht) |
| Toevoegen latere vermelding | realiseert *realisatie* | [Voornaamwijziging](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/voornaamwijziging.md) | [UPL-lijst extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Voornaam of achternaam veranderen](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) (UPL nr. 460; Utrecht) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Adoptie](../../../gebeurtenissen/adoptie.md) | leidt tot *triggering* | Toevoegen latere vermelding | [Besluit burgerlijke stand 1994](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md), [HUP BRP: Adoptie](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-adoptie.md) (art. 53) |
| [Ambtenaar van de burgerlijke stand](../../../rollen/ambtenaar-van-de-burgerlijke-stand.md) | voegt toe *toewijzing* | Toevoegen latere vermelding | [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 20) |
| [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Toevoegen latere vermelding | [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 20) |
| [Naamswijziging](../../../gebeurtenissen/naamswijziging.md) | leidt tot *triggering* | Toevoegen latere vermelding | [Utrecht Voornaam of achternaam veranderen](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md), [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (Utrecht inleiding; art. 20) |
| [Ontkenning ouderschap](../../../gebeurtenissen/ontkenning-ouderschap.md) | leidt tot *triggering* | Toevoegen latere vermelding | [Besluit burgerlijke stand 1994](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md), [HUP BRP: Ontkenning ouderschap](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-ontkenning-ouderschap.md) (art. 49-52) |
| [Vaststelling ouderschap](../../../gebeurtenissen/vaststelling-ouderschap.md) | leidt tot *triggering* | Toevoegen latere vermelding | [HUP BRP: Vaststelling ouderschap](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-vaststelling-ouderschap.md) (inleiding) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP BRP: Vaststelling ouderschap](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-vaststelling-ouderschap.md) | HUP BRP: Vaststelling ouderschap |
| [HUP BRP: Ontkenning ouderschap](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-ontkenning-ouderschap.md) | HUP BRP: Ontkenning ouderschap |
| [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [Besluit burgerlijke stand 1994](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) | Besluit burgerlijke stand 1994 |
| [HUP BRP: Adoptie](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-adoptie.md) | HUP BRP: Adoptie |
| [UPL-lijst extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Voornaam of achternaam veranderen](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) | Gemeente Utrecht: Voornaam of achternaam veranderen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../terugmeldingen/procesarchitectuur-terugmeldingen.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../bronanalyses/algemeen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), 2025-vng-upl-producten-en-diensten-intern). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../bronanalyses/algemeen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
