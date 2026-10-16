---
id: toevoegen-latere-vermelding
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Toevoegen latere vermelding
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het toevoegen van een rechterlijke uitspraak of een besluit over de staat van een persoon aan een akte als latere vermelding.
match:
  gemma: geen
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

<!-- Gegenereerd door tools/render.py uit de beoordeling toevoegen-latere-vermelding.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

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

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Ambtenaar van de burgerlijke stand](../../../rollen/ambtenaar-van-de-burgerlijke-stand.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met [Adoptie](../../../gebeurtenissen/adoptie.md), [Naamswijziging](../../../gebeurtenissen/naamswijziging.md), [Ontkenning ouderschap](../../../gebeurtenissen/ontkenning-ouderschap.md), [Vaststelling ouderschap](../../../gebeurtenissen/vaststelling-ouderschap.md). |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een latere vermelding op de akte, maandelijks doorgestuurd naar de centrale bewaarplaats (Besluit burgerlijke stand art. 31). [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, BW 1 art. 20, 20a; Besluit burgerlijke stand art. 15-17, 31, 53, 54. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van de uitspraak of het besluit dat de staat verandert tot de latere vermelding. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md), [HUP BRP: Adoptie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-adoptie.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Achternaamwijziging](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/achternaamwijziging.md), [Voornaamwijziging](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/voornaamwijziging.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Toevoegen latere vermelding | voegt latere vermelding toe aan *toegang (bijwerken)* | [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 20) |
| Toevoegen latere vermelding | realiseert *realisatie* | [Achternaamwijziging](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/achternaamwijziging.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Voornaam of achternaam veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) (UPL nr. 5; Utrecht) |
| Toevoegen latere vermelding | realiseert *realisatie* | [Voornaamwijziging](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/voornaamwijziging.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Voornaam of achternaam veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) (UPL nr. 460; Utrecht) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Adoptie](../../../gebeurtenissen/adoptie.md) | leidt tot *triggering* | Toevoegen latere vermelding | [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md), [HUP BRP: Adoptie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-adoptie.md) (art. 53) |
| [Ambtenaar van de burgerlijke stand](../../../rollen/ambtenaar-van-de-burgerlijke-stand.md) | voegt toe *toewijzing* | Toevoegen latere vermelding | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 20) |
| [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Toevoegen latere vermelding | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 20) |
| [Naamswijziging](../../../gebeurtenissen/naamswijziging.md) | leidt tot *triggering* | Toevoegen latere vermelding | [Utrecht Voornaam of achternaam veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md), [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (Utrecht inleiding; art. 20) |
| [Ontkenning ouderschap](../../../gebeurtenissen/ontkenning-ouderschap.md) | leidt tot *triggering* | Toevoegen latere vermelding | [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md), [HUP BRP: Ontkenning ouderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-ontkenning-ouderschap.md) (art. 49-52) |
| [Vaststelling ouderschap](../../../gebeurtenissen/vaststelling-ouderschap.md) | leidt tot *triggering* | Toevoegen latere vermelding | [HUP BRP: Vaststelling ouderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-vaststelling-ouderschap.md) (inleiding) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP BRP: Vaststelling ouderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-vaststelling-ouderschap.md) | HUP BRP: Vaststelling ouderschap |
| [HUP BRP: Ontkenning ouderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-ontkenning-ouderschap.md) | HUP BRP: Ontkenning ouderschap |
| [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) | Besluit burgerlijke stand 1994 |
| [HUP BRP: Adoptie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-adoptie.md) | HUP BRP: Adoptie |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Voornaam of achternaam veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) | Gemeente Utrecht: Voornaam of achternaam veranderen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
