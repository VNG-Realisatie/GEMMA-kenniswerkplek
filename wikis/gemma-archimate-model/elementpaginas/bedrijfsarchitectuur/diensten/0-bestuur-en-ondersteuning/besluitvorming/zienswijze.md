---
id: zienswijze
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Zienswijze
onderwerpen:
- besluitvorming
- participatie
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: Het schriftelijk of mondeling naar voren brengen van een mening over een ontwerpbesluit dat ter inzage ligt.
match:
  gemma: geen
afnemer: extern
domein: Bestuur
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
---

# Zienswijze

<!-- Gegenereerd door tools/render.py uit de beoordeling zienswijze.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het schriftelijk of mondeling naar voren brengen van een mening over een ontwerpbesluit dat ter inzage ligt.

### Beschrijving

Als een besluit wordt voorbereid met de uniforme openbare voorbereidingsprocedure, kunnen belanghebbenden bij het bestuursorgaan naar keuze schriftelijk of mondeling hun zienswijze over het ontwerp naar voren brengen; een wettelijk voorschrift of het bestuursorgaan kan bepalen dat ook anderen dat mogen (Awb art. 3:15). De termijn is zes weken vanaf de terinzagelegging (art. 3:16); van een mondelinge zienswijze wordt een verslag gemaakt (art. 3:17). De UPL noemt de dienst voor burgers en bedrijven (nr. 497).

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Afnemer**: extern.
- **Domein**: Bestuur.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Uitvoeren uniforme openbare voorbereidingsprocedure](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/uitvoeren-uniforme-openbare-voorbereidingsprocedure.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Algemene wet bestuursrecht](../../../../motivatie/beleidskaders/rijksregelgeving/algemene-wet-bestuursrecht.md) | is grondslag voor *associatie (gericht)* | Zienswijze | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 3:15) |
| [Uitvoeren uniforme openbare voorbereidingsprocedure](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/uitvoeren-uniforme-openbare-voorbereidingsprocedure.md) | realiseert *realisatie* | Zienswijze | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. 3:15; UPL nr. 497) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst Zienswijze; de Deelservice Inspraakprocedure (Vaststellen omgevingsplan) is een interne deeldienst voor het omgevingsplan. Nieuw voor GEMMA.
