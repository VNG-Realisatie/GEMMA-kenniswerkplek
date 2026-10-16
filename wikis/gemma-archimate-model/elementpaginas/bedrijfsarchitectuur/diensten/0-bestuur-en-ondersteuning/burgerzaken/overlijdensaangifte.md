---
id: overlijdensaangifte
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Overlijdensaangifte
onderwerpen:
- burgerzaken
- lijkbezorging
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het doen van aangifte van een overlijden bij de gemeente waar iemand is overleden, waarna de gemeente een akte van overlijden opmaakt.
match:
  gemma: geen
data_object: nee
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Aangifte van overlijden (wet)
- Overlijden, aangifte doen (beleid)
bronnen:
- 2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493
- 2026-rvo-aangifte-en-akte-van-overlijden
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-overlijden-aangifte-doen
- 2026-rijk-burgerlijk-wetboek-boek-1
---

# Overlijdensaangifte

<!-- Gegenereerd door tools/render.py uit de beoordeling overlijdensaangifte.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het doen van aangifte van een overlijden bij de gemeente waar iemand is overleden, waarna de gemeente een akte van overlijden opmaakt.

### Beschrijving

Aangifte doet wie het overlijden uit eigen wetenschap kent; degene die de lijkbezorging regelt kan een gemachtigde aanwijzen, meestal de uitvaartondernemer, ook elektronisch (BW 1 art. 19h). Voor de aangifte is een verklaring van overlijden van de behandelend arts of de gemeentelijke lijkschouwer nodig (Utrecht; RVO). De aangifte is gratis (Utrecht).

Kanalen: online voor uitvaartondernemers met eHerkenning, met het burgerservicenummer van de overledene (Besluit burgerlijke stand art. 67a; Utrecht; RVO), of aan de balie op afspraak voor uitvaartondernemers en nabestaanden (Utrecht). Bij een lijkvinding doet de hulpofficier van justitie schriftelijk aangifte (BW 1 art. 19h lid 6; Besluit burgerlijke stand art. 62).

### Per onderwerp

#### [Lijkbezorging](../../../../../onderwerpen/lijkbezorging/begrippen.md)

Na de aangifte krijgt de aangever het verlof tot begraving of crematie en zo nodig het laissez-passer voor vervoer naar het buitenland (RVO; Utrecht).

### Synoniemen

| Synoniem | Context |
|---|---|
| Aangifte van overlijden | wet |
| Overlijden, aangifte doen | beleid |

### Naamkeuze

De UPL-naam letterlijk (regel Naamvorm); de wetsterm aangifte van overlijden (BW 1 art. 19h), tot 2026-10-07 de naam van deze beoordeling, is een synoniem.

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (kern ja, 2/2).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Burgerlijke stand diensten](../../../bedrijfsfuncties/publieksdiensten/burgerlijke-stand-diensten.md).
- **Afnemer**: extern.
- **Domein**: Publieksdiensten.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de akte van overlijden; daarna het verlof tot begraving of crematie (Utrecht inleiding; RVO). [Utrecht Overlijden, aangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-overlijden-aangifte-doen.md), [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke afnemer die erom vraagt. [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Overlijden, aangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-overlijden-aangifte-doen.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, burger en bedrijf (UPL nr. 315): nabestaanden en de uitvaartondernemer (Utrecht inleiding). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Overlijden, aangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-overlijden-aangifte-doen.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert? | Ja, met [Opmaken akte van overlijden](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-overlijden.md). |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, een eigen product in de UPL (nr. 315); geen bredere dienst in deze wiki. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Burgerlijk Wetboek Boek 1](../../../../motivatie/beleidskaders/rijksregelgeving/burgerlijk-wetboek-boek-1.md) | is grondslag voor *associatie (gericht)* | Overlijdensaangifte | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 315, art. 19h) |
| [Burgerlijke stand diensten](../../../bedrijfsfuncties/publieksdiensten/burgerlijke-stand-diensten.md) | omvat *aggregatie* | Overlijdensaangifte | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 315 (GEMMA-domein Publieksdiensten)) |
| [Opmaken akte van overlijden](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-overlijden.md) | realiseert *realisatie* | Overlijdensaangifte | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (UPL nr. 315; art. 19h) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) | Besluit burgerlijke stand 1994 |
| [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) | Aangifte en akte van overlijden (Ondernemersplein) |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Overlijden, aangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-overlijden-aangifte-doen.md) | Gemeente Utrecht: Overlijden |
| [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor de aangifte van overlijden; nieuw voor GEMMA.
