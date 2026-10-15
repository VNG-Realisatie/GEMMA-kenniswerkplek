---
id: briefadres-aanvragen
type: dienst
archimate_type: business-service
status: review
naam: Briefadres aanvragen
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het aanvragen van een inschrijving op een briefadres door iemand die geen woonadres heeft.
match:
  gemma: geen
data_object: nee
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Briefadres (UPL)
- Aanvraag briefadres (beleid)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-nvvb-beleidsregel-briefadres
- 2026-rvig-hup-verblijfplaats
---

# Briefadres aanvragen

<!-- Gegenereerd door tools/render.py uit de beoordeling briefadres-aanvragen.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het aanvragen van een inschrijving op een briefadres door iemand die geen woonadres heeft.

### Beschrijving

Wie geen woonadres heeft, vraagt een briefadres aan; daarvoor is een briefadresgever nodig die schriftelijk instemt (HUP Verblijfplaats). De NVVB-modelregeling kent een vragenformulier voor de aanvraag en een verklaring van toestemming (NVVB Beleidsregel briefadres). Grondslag is art. 2.23 Wet BRP; de aanvraag kan digitaal (UPL nr. 85).

### Synoniemen

| Synoniem | Context |
|---|---|
| Briefadres | UPL |
| Aanvraag briefadres | beleid |

### Homoniemen

| Begrip | Betekenis | Naamkeuze |
|---|---|---|
| [Briefadres](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/briefadres.md) (wiki, GGM en GEMMA (bedrijfsobject Briefadres)) | Het adres zelf waar post voor iemand zonder woonadres in ontvangst wordt genomen | Deze pagina heet Briefadres aanvragen, de dienst; de UPL-naam briefadres is een synoniem, omdat het bedrijfsobject Briefadres die naam draagt. |

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (kern ja, 2/2).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Bevolkingsadministratie bijhouding](../../../bedrijfsfuncties/publieksdiensten/bevolkingsadministratie-bijhouding.md).
- **Afnemer**: extern.
- **Domein**: Publieksdiensten.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een inschrijving op een briefadres (HUP Verblijfplaats). [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke afnemer die erom vraagt. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [NVVB Beleidsregel briefadres](../../../../../onderwerpen/burgerzaken/bronduidingen/gemeentelijke-regelgeving/2026-nvvb-beleidsregel-briefadres.md), [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, burger (UPL nr. 85): wie geen woonadres heeft. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert? | Ja, met [Inschrijven op briefadres](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-op-briefadres.md). |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, een eigen product in de UPL (UPL nr. 85); geen bredere dienst in deze wiki. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Briefadres aanvragen | bedient *bediening* | [Aangever](../../../rollen/aangever.md) | [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bevolkingsadministratie bijhouding](../../../bedrijfsfuncties/publieksdiensten/bevolkingsadministratie-bijhouding.md) | omvat *aggregatie* | Briefadres aanvragen | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 85 (GEMMA-domein Publieksdiensten)) |
| [Inschrijven op briefadres](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-op-briefadres.md) | realiseert *realisatie* | Briefadres aanvragen | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [NVVB Beleidsregel briefadres](../../../../../onderwerpen/burgerzaken/bronduidingen/gemeentelijke-regelgeving/2026-nvvb-beleidsregel-briefadres.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (UPL nr. 85; Wet BRP art. 2.23 lid 1) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Briefadres aanvragen | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 85, art. 2.23) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [NVVB Beleidsregel briefadres](../../../../../onderwerpen/burgerzaken/bronduidingen/gemeentelijke-regelgeving/2026-nvvb-beleidsregel-briefadres.md) | NVVB: Beleidsregel briefadres |
| [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) | HUP BRP: Verblijfplaats |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.

### Besluiten redacteur

- 2026-10-07: De dienst heet Briefadres aanvragen, met briefadres (UPL nr. 85) als synoniem; homoniem van het bedrijfsobject Briefadres (precedent Uitvaart vervroegen of uitstellen). *Zekerheid: logica.*
