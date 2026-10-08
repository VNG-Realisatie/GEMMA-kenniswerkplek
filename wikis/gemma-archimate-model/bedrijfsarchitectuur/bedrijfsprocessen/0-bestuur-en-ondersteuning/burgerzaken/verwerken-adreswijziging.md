---
id: verwerken-adreswijziging
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Verwerken adreswijziging
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het verwerken van een verhuizing binnen of naar de gemeente in de verblijfplaats van de ingeschreven persoon.
grondslag: bron
match:
  gemma: geen
data_object: nee
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Binnengemeentelijke adreswijziging (HUP)
- Intergemeentelijke adreswijziging (HUP)
bronnen:
- 2026-utrecht-burgerzaken-verhuizing-doorgeven
- 2026-rvig-hup-binnengemeentelijke-adreswijziging
- 2026-rvig-hup-intergemeentelijke-adreswijziging
- 2025-vng-upl-producten-en-diensten-extern
---

# Verwerken adreswijziging

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/verwerken-adreswijziging.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het verwerken van een verhuizing binnen of naar de gemeente in de verblijfplaats van de ingeschreven persoon.

### Beschrijving

Wie binnen of naar de gemeente verhuist, doet aangifte van adreswijziging, vanaf vier weken voor tot de vijfde dag na de verhuizing; alle verhuizende personen ondertekenen, de aangifte kan schriftelijk of digitaal met DigiD en de gemeente kan de betrouwbaarheid controleren (HUP Binnengemeentelijke adreswijziging; Utrecht Verhuizing doorgeven). Bij een verhuizing vanuit een andere gemeente wordt de nieuwe gemeente bijhoudingsgemeente en neemt zij de persoonslijst over, met openstaande onderzoeken (HUP Intergemeentelijke adreswijziging). Wie bij iemand anders gaat wonen, levert een verklaring van inwoning van de hoofdbewoner (Utrecht).

Een infrastructurele wijziging zonder verhuizing (straatnaamwijziging, vernummering, gemeentelijke herindeling) wordt als adreswijziging verwerkt, zonder aangifte (HUP Binnengemeentelijke en Intergemeentelijke adreswijziging).

### Synoniemen

| Synoniem | Context |
|---|---|
| Binnengemeentelijke adreswijziging | HUP |
| Intergemeentelijke adreswijziging | HUP |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Verblijfplaats](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/verblijfplaats.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aangifte of melding*. De verwerking volgt op een aangifte van adreswijziging die de basisregistratie bijwerkt (HUP Binnengemeentelijke adreswijziging).
- **Gestart door gebeurtenis**: [Verhuizing](../../../gebeurtenissen/verhuizing.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 44 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar als verhuizing doorgeven (Utrecht) en adreswijziging (HUP). [Utrecht Verhuizing doorgeven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de gemeente past de gegevens aan en geeft de verhuizing door aan organisaties (Utrecht Verhuizing doorgeven). [Utrecht Verhuizing doorgeven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md), [Utrecht Verhuizing doorgeven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md), [Utrecht Verhuizing doorgeven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gedaan wordt. [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md), [Utrecht Verhuizing doorgeven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md) |
| **per keer doorlopen**: Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? | Ja, wordt per geval van begin tot eind doorlopen. [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md), [Utrecht Verhuizing doorgeven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, bijhoudingsgemeente; de Aangever doet aangifte (HUP Binnengemeentelijke en Intergemeentelijke adreswijziging). [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, legt de nieuwe verblijfplaats vast; bij een verhuizing naar de gemeente neemt zij de persoonslijst over (HUP Intergemeentelijke adreswijziging). [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, aangifte van adreswijziging, of ambtshalve na een onderzoek (HUP Binnengemeentelijke adreswijziging). [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een nieuwe verblijfplaats met datum aanvang adreshouding (HUP Binnengemeentelijke adreswijziging). [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md), [Utrecht Verhuizing doorgeven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, aangifte vanaf vier weken voor tot de vijfde dag na de verhuizing; bij latere aangifte geldt de ontvangstdatum (art. 2.39 Wet BRP; HUP Binnengemeentelijke adreswijziging; UPL nr. 424). [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [UPL-lijst extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, draagt bij aan Bijhouden persoonsgegevens: één mutatie in de verblijfplaats (HUP Binnengemeentelijke adreswijziging). [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van de aangifte, of ambtshalve, tot de nieuwe verblijfplaats. [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, realiseert de dienst Verhuismelding (UPL nr. 424). [UPL-lijst extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder proces in deze wiki. [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verwerken adreswijziging | legt vast *toegang (bijwerken)* | [Verblijfplaats](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/verblijfplaats.md) | [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) (inleiding) |
| Verwerken adreswijziging | realiseert *realisatie* | [Verhuismelding](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/verhuismelding.md) | [UPL-lijst extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Verhuizing doorgeven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md) (UPL nr. 424) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Aangever](../../../rollen/aangever.md) | doet aangifte *toewijzing* | Verwerken adreswijziging | [HUP Verblijfplaats](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Verwerken adreswijziging | [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) (HUP Binnengemeentelijke en Intergemeentelijke adreswijziging) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Verwerken adreswijziging | [HUP BRP Achtergronden en begrippen](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |
| [Verhuizing](../../../gebeurtenissen/verhuizing.md) | leidt tot *triggering* | Verwerken adreswijziging | [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [Utrecht Verhuizing doorgeven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md) (HUP inleiding; Utrecht inleiding) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht Verhuizing doorgeven](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md) | Gemeente Utrecht: Verhuizing doorgeven |
| [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) | HUP BRP: Binnengemeentelijke adreswijziging |
| [HUP Intergemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) | HUP BRP: Intergemeentelijke adreswijziging |
| [UPL-lijst extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../analyses/procesarchitectuur-terugmeldingen.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../analyses/gemma-kennismodel.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), 2025-vng-upl-producten-en-diensten-intern). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../analyses/proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
