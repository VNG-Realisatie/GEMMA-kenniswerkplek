---
id: verwerken-emigratie
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Verwerken emigratie
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het verwerken van het vertrek van een ingezetene naar het buitenland, waarna hij als niet-ingezetene in de RNI staat.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Uitschrijving (dagelijks gebruik)
bronnen:
- 2026-utrecht-burgerzaken-emigratie-doorgeven
- 2026-rvig-hup-emigratie
- 2026-rijk-besluit-brp-bwbr0034306
- 2025-rvig-logisch-ontwerp-brp-2025q1
- 2025-vng-upl-producten-en-diensten-extern
---

# Verwerken emigratie

<!-- Gegenereerd door tools/render.py uit de beoordeling verwerken-emigratie.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het verwerken van het vertrek van een ingezetene naar het buitenland, waarna hij als niet-ingezetene in de RNI staat.

### Beschrijving

Wie ten minste twee derde van een jaar in het buitenland gaat wonen, doet aangifte van vertrek, vanaf vijf dagen voor het vertrek; ook een verhuizing naar het Caribisch deel van het Koninkrijk is een emigratie, waarbij de persoon kosteloos een verhuisbericht krijgt (HUP Emigratie; Regeling BRP bijlage 9). Na verwerking verhuist de persoonslijst naar de RNI en blijft de laatste bijhoudingsgemeente verantwoordelijk voor rechtsfeiten van voor de emigratie (HUP Emigratie). Is de persoon niet te bereiken, dan neemt de gemeente het vertrek ambtshalve op na een adresonderzoek (HUP Emigratie; Circulaire adresonderzoek 4.8).

### Synoniemen

| Synoniem | Context |
|---|---|
| Uitschrijving | dagelijks gebruik |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aangifte of melding*. De verwerking volgt op een aangifte van vertrek die de basisregistratie bijwerkt (HUP Emigratie).
- **Gestart door gebeurtenis**: [Emigratie](../../../gebeurtenissen/emigratie.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Aangever](../../../rollen/aangever.md), [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met [Emigratie](../../../gebeurtenissen/emigratie.md). |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de persoon is niet-ingezetene en staat in de RNI (Utrecht Emigratie doorgeven). [Utrecht Emigratie doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [HUP Emigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md), [Utrecht Emigratie doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, verplicht bij een verblijf van ten minste twee derde van een jaar buiten Nederland (art. 2.43 Wet BRP; HUP Emigratie); aangifte in persoon of schriftelijk (Besluit BRP art. 29). [HUP Emigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md), [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van de aangifte van vertrek tot de inschrijving in de RNI. [HUP Emigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md), [Utrecht Emigratie doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Aangifte vertrek buitenland](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/aangifte-vertrek-buitenland.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verwerken emigratie | schrijft uit naar de RNI *toegang (bijwerken)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [HUP Emigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md) (inleiding) |
| Verwerken emigratie | realiseert *realisatie* | [Aangifte vertrek buitenland](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/aangifte-vertrek-buitenland.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Emigratie doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md) (UPL nr. 1) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Aangever](../../../rollen/aangever.md) | doet aangifte *toewijzing* | Verwerken emigratie | [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| [Besluit basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/besluit-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Verwerken emigratie | [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) (art. 29) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Verwerken emigratie | [HUP Emigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md) (inleiding) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Verwerken emigratie | [HUP BRP Achtergronden en begrippen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 1.4 lid 1, 2.43) |
| [Emigratie](../../../gebeurtenissen/emigratie.md) | leidt tot *triggering* | Verwerken emigratie | [HUP Emigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md), [Utrecht Emigratie doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (inleiding; Wet BRP art. 2.43 lid 1) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht Emigratie doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md) | Gemeente Utrecht: Emigratie doorgeven |
| [HUP Emigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md) | HUP BRP: Emigratie |
| [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) | Besluit basisregistratie personen |
| [Logisch Ontwerp BRP 2025.Q1](../../../../../onderwerpen/burgerzaken/bronduidingen/informatiemodel/2025-rvig-logisch-ontwerp-brp-2025q1.md) | Logisch Ontwerp BRP Versie 2025.Q1 |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
