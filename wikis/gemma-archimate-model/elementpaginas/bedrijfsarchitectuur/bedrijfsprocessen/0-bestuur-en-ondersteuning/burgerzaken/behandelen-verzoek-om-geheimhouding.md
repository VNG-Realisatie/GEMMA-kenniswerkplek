---
id: behandelen-verzoek-om-geheimhouding
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Behandelen verzoek om geheimhouding
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het verwerken van een verzoek om persoonsgegevens niet aan bepaalde derden te verstrekken, of om die geheimhouding te beëindigen.
match:
  gemma: geen
data_object: nee
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-utrecht-burgerzaken-persoonsgegevens-geheimhouden
- 2026-rvig-hup-verstrekkingsbeperking
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rijk-wet-brp-bwbr0033715
---

# Behandelen verzoek om geheimhouding

<!-- Gegenereerd door tools/render.py uit de beoordeling behandelen-verzoek-om-geheimhouding.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het verwerken van een verzoek om persoonsgegevens niet aan bepaalde derden te verstrekken, of om die geheimhouding te beëindigen.

### Beschrijving

De burger kan verstrekking aan overheidsorganen op grond van een autorisatiebesluit niet tegenhouden, maar wel schriftelijk verzoeken geen gegevens te verstrekken aan bepaalde derden (HUP Verstrekkingsbeperking). Het verzoek is vormvrij en hoeft niet te worden gemotiveerd; de gemeente stelt de identiteit vast, verwerkt het binnen vier weken, bevestigt het schriftelijk en weigert het niet als de juiste persoon het doet (HUP Verstrekkingsbeperking). Online kan het met DigiD binnen vijf werkdagen; de geheimhouding verhuist mee naar een nieuwe gemeente (Utrecht Persoonsgegevens geheimhouden).

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aanvraag product*. Een verzoek om een product dat de gemeente toekent als de juiste persoon het doet (HUP Verstrekkingsbeperking).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, schriftelijk verzoek van de ingeschrevene van 16 jaar of ouder, of van ouder, voogd of curator (HUP Verstrekkingsbeperking). [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een aantekening van geheimhouding op de persoonslijst en een schriftelijke bevestiging (HUP Verstrekkingsbeperking). [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md), [Utrecht Persoonsgegevens geheimhouden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-geheimhouden.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, wet BRP art. 2.59, 2.60 en 3.21: kosteloos, binnen vier weken, met mededeling van de regels (HUP Verstrekkingsbeperking; UPL nr. 87). [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van het verzoek tot de aantekening en de bevestiging. [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, een beslissing om geen gevolg te geven aan het verzoek is een besluit in de zin van de Awb (art. 2.60 Wet BRP; HUP Verstrekkingsbeperking). [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [BRP-geheimhoudingsverzoek](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-geheimhoudingsverzoek.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Behandelen verzoek om geheimhouding | tekent geheimhouding aan *toegang (bijwerken)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (inleiding; Wet BRP art. 2.59 lid 1) |
| Behandelen verzoek om geheimhouding | realiseert *realisatie* | [BRP-geheimhoudingsverzoek](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-geheimhoudingsverzoek.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Persoonsgegevens geheimhouden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-geheimhouden.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (UPL nr. 87; Wet BRP art. 2.59) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beslisser](../../../rollen/beslisser.md) | beslist over *toewijzing* | Behandelen verzoek om geheimhouding | [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md) (art. 2.60 Wet BRP) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Behandelen verzoek om geheimhouding | [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md) (inleiding) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Behandelen verzoek om geheimhouding | [HUP BRP Achtergronden en begrippen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 2.59) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Behandelen verzoek om geheimhouding | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 2.59) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht Persoonsgegevens geheimhouden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-geheimhouden.md) | Gemeente Utrecht: Persoonsgegevens geheimhouden |
| [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md) | HUP BRP: Verstrekkingsbeperking |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
