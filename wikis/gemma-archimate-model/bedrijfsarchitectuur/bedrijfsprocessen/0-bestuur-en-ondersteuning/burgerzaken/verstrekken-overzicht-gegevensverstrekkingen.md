---
id: verstrekken-overzicht-gegevensverstrekkingen
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Verstrekken overzicht gegevensverstrekkingen
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het op verzoek leveren van een overzicht aan een ingeschrevene van welke gegevens over hem aan wie zijn verstrekt.
grondslag: bron
match:
  gemma: geen
data_object: nee
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen
- 2025-vng-upl-producten-en-diensten-extern
- 2025-rvig-logisch-ontwerp-brp-2025q1
- 2026-rijk-besluit-brp-bwbr0034306
---

# Verstrekken overzicht gegevensverstrekkingen

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/verstrekken-overzicht-gegevensverstrekkingen.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het op verzoek leveren van een overzicht aan een ingeschrevene van welke gegevens over hem aan wie zijn verstrekt.

### Beschrijving

Wie in de gemeente staat ingeschreven, kan een overzicht vragen van de persoonsgegevens die uit de BRP zijn verstrekt en wanneer; het Ministerie van BZK levert de gegevens (vanaf 6 januari 2013), de gemeente stuurt het overzicht met een begeleidende brief per beveiligde e-mail of aangetekende post (Utrecht Persoonsgegevens bekijken). Het overzicht wordt gemaakt met de ProtocolleringsOverzichtModule (LO BRP 1.5.2).

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 44 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar: Overzicht gegevensverstrekkingen BRP (Utrecht; UPL nr. 92). [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md), [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de gemeente stuurt het overzicht met een begeleidende brief (Utrecht Persoonsgegevens bekijken). [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md), [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md), [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gedaan wordt. [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md), [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) |
| **per keer doorlopen**: Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? | Ja, wordt per geval van begin tot eind doorlopen. [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md), [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, bijhoudingsgemeente (Utrecht: alleen voor wie in de gemeente staat ingeschreven). [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, raadpleegt de vastgelegde verstrekkingen over de ingeschreven persoon (Utrecht; LO BRP 1.5.2: POM). [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md), [Logisch Ontwerp BRP 2025.Q1](../../../../bronanalyses/burgerzaken/2025-rvig-logisch-ontwerp-brp-2025q1.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, verzoek van de ingeschrevene (Utrecht). [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een overzicht van de verstrekte gegevens sinds 6 januari 2013 (Utrecht). [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md), [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, wet BRP art. 3.22 (UPL nr. 92); Besluit BRP art. 46 (uitzonderingen op de inzage). [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md), [Besluit BRP](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-brp-bwbr0034306.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, draagt bij aan Bijhouden persoonsgegevens: de burger inzicht geven in de verstrekking van zijn gegevens (Utrecht). [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md) |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van het verzoek tot het overzicht. [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, realiseert de dienst BRP-inzagerecht gegevensverstrekking (UPL nr. 92). [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder proces in deze wiki. [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verstrekken overzicht gegevensverstrekkingen | geeft overzicht over *toegang (raadplegen)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md) (Aanvragen overzicht) |
| Verstrekken overzicht gegevensverstrekkingen | realiseert *realisatie* | [BRP-inzagerecht gegevensverstrekking](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-inzagerecht-gegevensverstrekking.md) | [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md) (UPL nr. 92) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Verstrekken overzicht gegevensverstrekkingen | [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md), [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) (Utrecht Aanvragen overzicht; UPL nr. 92) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Verstrekken overzicht gegevensverstrekkingen | [HUP BRP Achtergronden en begrippen](../../../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht BRP bekijken en overzicht aanvragen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md) | Gemeente Utrecht: Persoonsgegevens bekijken of aanvragen |
| [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Logisch Ontwerp BRP 2025.Q1](../../../../bronanalyses/burgerzaken/2025-rvig-logisch-ontwerp-brp-2025q1.md) | Logisch Ontwerp BRP Versie 2025.Q1 |
| [Besluit BRP](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-brp-bwbr0034306.md) | Besluit basisregistratie personen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../analyses/procesarchitectuur-terugmeldingen.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../analyses/gemma-kennismodel.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md), 2025-vng-upl-producten-en-diensten-intern). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../analyses/proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
