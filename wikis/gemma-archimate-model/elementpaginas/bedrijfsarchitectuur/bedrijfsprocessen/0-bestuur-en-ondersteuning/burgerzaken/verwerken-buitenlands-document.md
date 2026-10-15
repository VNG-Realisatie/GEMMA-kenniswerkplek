---
id: verwerken-buitenlands-document
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Verwerken buitenlands document
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het beoordelen van een buitenlands document over een gebeurtenis van de burgerlijke staat en het verwerken daarvan in de basisregistratie personen.
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

<!-- Gegenereerd door tools/render.py uit de beoordeling verwerken-buitenlands-document.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

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

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, het verzoek van de ingeschrevene met het buitenlandse document (Utrecht), of een melding van een gebeurtenis in het buitenland (HUP Overlijden buitenland). [Utrecht Buitenlandse documenten inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-buitenland.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de verwerking in de BRP met een bevestiging per brief, of een besluit dat het document niet volstaat (Utrecht; HUP Overlijden buitenland). [Utrecht Buitenlandse documenten inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-buitenland.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [Utrecht Buitenlandse documenten inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-buitenland.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, wet BRP art. 2.8, 2.51 (HUP Overlijden buitenland); BW 1 art. 25 (Utrecht); UPL: art. 2.38 Wet BRP. [HUP BRP: Overlijden buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-buitenland.md), [Utrecht Buitenlandse documenten inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van het verzoek of de melding tot de verwerking of het besluit. [Utrecht Buitenlandse documenten inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-buitenland.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, de gemeente beoordeelt per geval of het document volstaat (Wet BRP art. 2.8, 2.51; HUP Overlijden buitenland). [HUP BRP: Overlijden buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-buitenland.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [BRP-inschrijving buitenlandse akte](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-inschrijving-buitenlandse-akte.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verwerken buitenlands document | verwerkt document bij *toegang (bijwerken)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [Utrecht Buitenlandse documenten inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md) (inleiding) |
| Verwerken buitenlands document | realiseert *realisatie* | [BRP-inschrijving buitenlandse akte](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-inschrijving-buitenlandse-akte.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Buitenlandse documenten inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md) (UPL nr. 89) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beslisser](../../../rollen/beslisser.md) | beslist over *toewijzing* | Verwerken buitenlands document | [Utrecht Buitenlandse documenten inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-buitenland.md) (Utrecht: Na uw afspraak; HUP regel 33) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Verwerken buitenlands document | [Utrecht Buitenlandse documenten inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-buitenland.md) (Utrecht; HUP art. 2.8, 2.51) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Verwerken buitenlands document | [Utrecht Buitenlandse documenten inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-buitenland.md) (Utrecht: Voorwaarden, Na uw afspraak; HUP regel 33) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP BRP: Huwelijk en geregistreerd partnerschap](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-huwelijkgeregistreerd-partnerschap.md) | HUP BRP: Huwelijk en geregistreerd partnerschap |
| [Utrecht Trouwen in het buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-trouwen-in-het-buitenland.md) | Gemeente Utrecht: Trouwen in het buitenland |
| [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [Utrecht Buitenlandse documenten inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md) | Gemeente Utrecht: Buitenlandse documenten inschrijven |
| [HUP BRP: Overlijden buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-buitenland.md) | HUP BRP: Overlijden buitenland |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
