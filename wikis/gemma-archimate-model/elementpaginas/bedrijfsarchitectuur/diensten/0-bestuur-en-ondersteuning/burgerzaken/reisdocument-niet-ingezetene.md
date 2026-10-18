---
id: reisdocument-niet-ingezetene
type: dienst
archimate_type: business-service
status: review
naam: Reisdocument niet-ingezetene
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het aanvragen van een paspoort of ander reisdocument door iemand die niet als ingezetene in de BRP staat, bij een daartoe aangewezen gemeente.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- reisdocument (UPL)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rijk-paspoortbesluit-bwbr0044308
- 2026-rijk-paspoortwet-bwbr0005212
---

# Reisdocument niet-ingezetene

<!-- Gegenereerd door tools/render.py uit de beoordeling reisdocument-niet-ingezetene.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het aanvragen van een paspoort of ander reisdocument door iemand die niet als ingezetene in de BRP staat, bij een daartoe aangewezen gemeente.

### Beschrijving

De burgemeester van een bij ministeriële regeling aangewezen gemeente neemt ook aanvragen in ontvangst en verstrekt nationale paspoorten, reisdocumenten voor vluchtelingen en voor vreemdelingen en nooddocumenten voor personen die niet als ingezetene in de basisregistratie personen staan (Paspoortbesluit art. 3.2, 4.2). Het document is hetzelfde reisdocument als voor een ingezetene; bijzonder is de bevoegde gemeente. Grondslag art. 4.2 Paspoortbesluit (UPL nr. 357). De UPL noemt met dezelfde grondslag en zonder doelgroep ook het product reisdocument (nr. 356); dat valt samen met deze dienst.

### Synoniemen

| Synoniem | Context |
|---|---|
| reisdocument | UPL |

### Homoniemen

| Begrip | Betekenis | Naamkeuze |
|---|---|---|
| [Reisdocument](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/reisdocument.md) (wiki, Paspoortwet art. 2) | Het document zelf, het bedrijfsobject Reisdocument | Deze dienst heet Reisdocument niet-ingezetene, de UPL-naam van nr. 357; reisdocument (UPL nr. 356) is een synoniem met context UPL, want het valt samen met deze dienst. Het bedrijfsobject houdt de naam Reisdocument. |

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Officiële documenten verstrekking](../../../bedrijfsfuncties/publieksdiensten/officiele-documenten-verstrekking.md).
- **Afnemer**: extern.
- **Domein**: Publieksdiensten.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md), [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Behandelen aanvraag reisdocument niet-ingezetene](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument-niet-ingezetene.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md), [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md), [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md), [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen aanvraag reisdocument niet-ingezetene](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument-niet-ingezetene.md) | realiseert *realisatie* | Reisdocument niet-ingezetene | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) (UPL nr. 356, 357; Paspoortbesluit art. 3.2, 4.2) |
| [Officiële documenten verstrekking](../../../bedrijfsfuncties/publieksdiensten/officiele-documenten-verstrekking.md) | omvat *aggregatie* | Reisdocument niet-ingezetene | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 357 (GEMMA-domein Publieksdiensten)) |
| [Paspoortbesluit](../../../../motivatie/beleidskaders/rijksregelgeving/paspoortbesluit.md) | is grondslag voor *associatie (gericht)* | Reisdocument niet-ingezetene | [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) (art. 3.2, 4.2) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) | Paspoortbesluit |
| [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 12](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (product, open): **UPL:** de UPL kent onder taakveld 0.2 naast reisdocument niet-ingezetene (nr. 357, doelgroep burger) ook het product reisdocument (nr. 356), met dezelfde grondslag art. 4.2 Paspoortbesluit en zonder doelgroep ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), nr. 356, 357). **Bevinding:** art. 4.2 Paspoortbesluit gaat alleen over de verstrekking aan personen die niet als ingezetene in de BRP staan, door aangewezen gemeenten ([2026-rijk-paspoortbesluit-bwbr0044308](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md), art. 3.2, 4.2). Nr. 356 valt daarmee samen met nr. 357; de reisdocumenten van ingezetenen hebben elk een eigen product. In GEMMA is reisdocument (nr. 356) een synoniem van de dienst Reisdocument niet-ingezetene. **Voorstel:** laat nr. 356 vervallen of voeg het samen met nr. 357.

### Besluiten redacteur

- 2026-10-07: UPL nr. 356 reisdocument is geen eigen dienst maar een synoniem (context UPL) van deze dienst, met procesarchitectuur-terugmelding. De dienst wordt gerealiseerd door het nieuwe deelproces Behandelen aanvraag reisdocument niet-ingezetene. *Zekerheid: logica.*
