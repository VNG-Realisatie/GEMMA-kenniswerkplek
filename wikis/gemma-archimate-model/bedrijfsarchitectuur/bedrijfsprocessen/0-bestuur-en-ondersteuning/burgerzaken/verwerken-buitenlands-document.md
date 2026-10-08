---
id: verwerken-buitenlands-document
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Verwerken buitenlands document
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het beoordelen van een buitenlands document over een gebeurtenis van de burgerlijke staat en het verwerken daarvan in de basisregistratie personen.
grondslag: bron
match:
  gemma: geen
data_object: nee
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Buitenlandse akte verwerken (HUP)
bronnen:
- 2026-rvig-hup-huwelijkgeregistreerd-partnerschap
- 2026-utrecht-burgerzaken-trouwen-in-het-buitenland
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven
- 2026-rvig-hup-overlijden-buitenland
- 2025-vng-upl-producten-en-diensten-extern
---

# Verwerken buitenlands document

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/verwerken-buitenlands-document.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het beoordelen van een buitenlands document over een gebeurtenis van de burgerlijke staat en het verwerken daarvan in de basisregistratie personen.

### Beschrijving

Het document moet gelegaliseerd en zo nodig vertaald zijn; de gemeente beoordeelt per geval of het volstaat en kan om andere stukken vragen; ontbreekt een akte, dan kan een lager brondocument dienen (Wet BRP art. 2.8, 2.51; HUP Overlijden buitenland; Utrecht). Een huwelijk of echtscheiding in strijd met de Nederlandse openbare orde wordt niet opgenomen (HUP Huwelijk/geregistreerd partnerschap). Een registratie van een in het buitenland gesloten huwelijk is verplicht; bij een vermoeden van een schijnhuwelijk stelt de gemeente onderzoek in (Utrecht Trouwen in het buitenland).

Inschrijving van de buitenlandse akte in de Nederlandse registers is een aparte stap bij de gemeente Den Haag, op verzoek of ambtshalve (BW 1 art. 25).

### Synoniemen

| Synoniem | Context |
|---|---|
| Buitenlandse akte verwerken | HUP |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aanvraag product*. Een verzoek waarop de gemeente beslist en dat zij verwerkt (Utrecht).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 43 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar: buitenlandse documenten inschrijven (Utrecht); de HUP verwerkt buitenlandse akten en lagere brondocumenten (HUP Overlijden buitenland). [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-overlijden-buitenland.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de gemeente van inschrijving verwerkt het document in de BRP (Utrecht). [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-overlijden-buitenland.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-overlijden-buitenland.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gedaan wordt. [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-overlijden-buitenland.md) |
| **per keer doorlopen**: Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? | Ja, wordt per geval van begin tot eind doorlopen. [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-overlijden-buitenland.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, bijhoudingsgemeente en Beslisser (college) (Utrecht; HUP Overlijden buitenland). [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-overlijden-buitenland.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, bijwerkt de gegevens van de ingeschreven persoon op grond van het buitenlandse document (Utrecht). [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, het verzoek van de ingeschrevene met het buitenlandse document (Utrecht), of een melding van een gebeurtenis in het buitenland (HUP Overlijden buitenland). [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-overlijden-buitenland.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de verwerking in de BRP met een bevestiging per brief, of een besluit dat het document niet volstaat (Utrecht; HUP Overlijden buitenland). [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-overlijden-buitenland.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-overlijden-buitenland.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, wet BRP art. 2.8, 2.51 (HUP Overlijden buitenland); BW 1 art. 25 (Utrecht); UPL: art. 2.38 Wet BRP. [HUP BRP: Overlijden buitenland](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-overlijden-buitenland.md), [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [UPL-lijst extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, draagt bij aan Bijhouden persoonsgegevens: één mutatie bij de ingeschreven persoon. [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md) |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van het verzoek of de melding tot de verwerking of het besluit. [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-overlijden-buitenland.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, de gemeente beoordeelt per geval of het document volstaat (Wet BRP art. 2.8, 2.51; HUP Overlijden buitenland). [HUP BRP: Overlijden buitenland](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-overlijden-buitenland.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, realiseert de dienst BRP-inschrijving buitenlandse akte (UPL nr. 89). [UPL-lijst extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip van hetzelfde type in deze wiki. [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-overlijden-buitenland.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verwerken buitenlands document | verwerkt document bij *toegang (bijwerken)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md) (inleiding) |
| Verwerken buitenlands document | realiseert *realisatie* | [BRP-inschrijving buitenlandse akte](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-inschrijving-buitenlandse-akte.md) | [UPL-lijst extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md) (UPL nr. 89) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Verwerken buitenlands document | [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-overlijden-buitenland.md) (Utrecht; HUP art. 2.8, 2.51) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP BRP: Huwelijk en geregistreerd partnerschap](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-huwelijkgeregistreerd-partnerschap.md) | HUP BRP: Huwelijk en geregistreerd partnerschap |
| [Utrecht Trouwen in het buitenland](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-trouwen-in-het-buitenland.md) | Gemeente Utrecht: Trouwen in het buitenland |
| [BW boek 1](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [Utrecht Buitenlandse documenten inschrijven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md) | Gemeente Utrecht: Buitenlandse documenten inschrijven |
| [HUP BRP: Overlijden buitenland](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-overlijden-buitenland.md) | HUP BRP: Overlijden buitenland |
| [UPL-lijst extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../terugmeldingen/procesarchitectuur-terugmeldingen.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../analyses/gemma-kennismodel.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), 2025-vng-upl-producten-en-diensten-intern). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../analyses/proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
