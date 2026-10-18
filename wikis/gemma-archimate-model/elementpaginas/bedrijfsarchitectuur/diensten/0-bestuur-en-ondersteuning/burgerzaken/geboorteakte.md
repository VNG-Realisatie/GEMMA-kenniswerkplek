---
id: geboorteakte
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Geboorteakte
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het verkrijgen van een uittreksel of afschrift van een geboorteakte.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-geboorteaangifte-doen
- 2026-rijk-burgerlijk-wetboek-boek-1
---

# Geboorteakte

<!-- Gegenereerd door tools/render.py uit de beoordeling geboorteakte.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het verkrijgen van een uittreksel of afschrift van een geboorteakte.

### Beschrijving

De UPL noemt als grondslag art. 19 BW 1, het opmaken van de akte van geboorte; de afnemer krijgt een uittreksel of afschrift. De akte zelf is een specialisatie van Akte van de burgerlijke stand.

### Homoniemen

| Begrip | Betekenis | Naamkeuze |
|---|---|---|
| Akte van geboorte (wiki, BW 1 art. 19) | De akte zelf, een specialisatie zonder pagina van Akte van de burgerlijke stand; gangbaar ook geboorteakte | Deze pagina heet Geboorteakte, de UPL-naam van de dienst (regel Naamvorm); de akte zelf heet met de wetsterm Akte van geboorte. |

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Burgerlijke stand diensten](../../../bedrijfsfuncties/publieksdiensten/burgerlijke-stand-diensten.md).
- **Afnemer**: extern.
- **Domein**: Publieksdiensten.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md), [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Verstrekken uittreksels en verklaringen burgerlijke stand](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-uittreksels-en-verklaringen-burgerlijke-stand.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md), [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md), [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md), [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Burgerlijk Wetboek Boek 1](../../../../motivatie/beleidskaders/rijksregelgeving/burgerlijk-wetboek-boek-1.md) | is grondslag voor *associatie (gericht)* | Geboorteakte | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 137, art. 19) |
| [Burgerlijke stand diensten](../../../bedrijfsfuncties/publieksdiensten/burgerlijke-stand-diensten.md) | omvat *aggregatie* | Geboorteakte | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 137 (GEMMA-domein Publieksdiensten)) |
| [Verstrekken uittreksels en verklaringen burgerlijke stand](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-uittreksels-en-verklaringen-burgerlijke-stand.md) | realiseert *realisatie* | Geboorteakte | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 137) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) | Gemeente Utrecht: Geboorteaangifte |
| [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
