---
id: naturalisatieceremonie
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Naturalisatieceremonie
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het bijwonen van de ceremonie waarin een nieuwe Nederlander de verklaring van verbondenheid aflegt en de bevestiging of het besluit ontvangt.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie
- 2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605
---

# Naturalisatieceremonie

<!-- Gegenereerd door tools/render.py uit de beoordeling naturalisatieceremonie.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het bijwonen van de ceremonie waarin een nieuwe Nederlander de verklaring van verbondenheid aflegt en de bevestiging of het besluit ontvangt.

### Beschrijving

Na goedkeuring van de naturalisatie of optie nodigt de gemeente uit voor een naturalisatieceremonie; men wordt pas Nederlander als men daar de verklaring van verbondenheid heeft afgelegd (Utrecht; Besluit verkrijging en verlies Nederlanderschap art. 60a, 60b). Grondslag art. 60a Besluit; doelgroep burger; niet digitaal (UPL nr. 261).

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Nederlanderschap diensten](../../../bedrijfsfuncties/publieksdiensten/nederlanderschap-diensten.md).
- **Afnemer**: extern.
- **Domein**: Publieksdiensten.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Nederlander worden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Behandelen naturalisatieverzoek](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-naturalisatieverzoek.md), [Behandelen optieverklaring](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-optieverklaring.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Nederlander worden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Nederlander worden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Nederlander worden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Naturalisatieceremonie | bedient *bediening* | [Optant](../../../rollen/optant.md) | [Besluit verkrijging en verlies Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Utrecht Nederlander worden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) (art. 60a; Utrecht) |
| Naturalisatieceremonie | bedient *bediening* | [Verzoeker om naturalisatie](../../../rollen/verzoeker-om-naturalisatie.md) | [Besluit verkrijging en verlies Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Utrecht Nederlander worden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) (art. 60b; Utrecht) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen naturalisatieverzoek](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-naturalisatieverzoek.md) | realiseert *realisatie* | Naturalisatieceremonie | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Nederlander worden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) (UPL nr. 261) |
| [Behandelen optieverklaring](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-optieverklaring.md) | realiseert *realisatie* | Naturalisatieceremonie | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Nederlander worden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) (UPL nr. 261) |
| [Besluit verkrijging en verlies Nederlanderschap](../../../../motivatie/beleidskaders/rijksregelgeving/besluit-verkrijging-en-verlies-nederlanderschap.md) | is grondslag voor *associatie (gericht)* | Naturalisatieceremonie | [Besluit verkrijging en verlies Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. 60a; UPL nr. 261) |
| [Nederlanderschap diensten](../../../bedrijfsfuncties/publieksdiensten/nederlanderschap-diensten.md) | omvat *aggregatie* | Naturalisatieceremonie | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 261 (GEMMA-domein Publieksdiensten)) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Nederlander worden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) | Gemeente Utrecht: Nederlander worden door naturalisatie of optie |
| [Besluit verkrijging en verlies Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) | Besluit verkrijging en verlies Nederlanderschap |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
