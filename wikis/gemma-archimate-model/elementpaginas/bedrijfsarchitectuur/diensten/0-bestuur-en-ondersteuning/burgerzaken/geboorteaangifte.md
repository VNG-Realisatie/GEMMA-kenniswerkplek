---
id: geboorteaangifte
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Geboorteaangifte
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het doen van aangifte van de geboorte van een kind bij de gemeente waar het is geboren, waarna de gemeente een geboorteakte opmaakt.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Aangifte van geboorte (wet)
- Geboorteaangifte doen (beleid)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-geboorteaangifte-doen
- 2026-rijk-burgerlijk-wetboek-boek-1
---

# Geboorteaangifte

<!-- Gegenereerd door tools/render.py uit de beoordeling geboorteaangifte.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het doen van aangifte van de geboorte van een kind bij de gemeente waar het is geboren, waarna de gemeente een geboorteakte opmaakt.

### Beschrijving

Aangifte binnen drie dagen na de geboortedag (BW 1 art. 19e). Kanalen: online met DigiD voor de moeder of de andere ouder als die al juridisch ouder is, met controle bij ziekenhuis of verloskundige, of aan de balie op afspraak; een afwijkende of dubbele achternaam kan alleen aan de balie met beide ouders (Utrecht). Grondslag art. 19e BW 1; digitaal kanaal (UPL nr. 136).

### Synoniemen

| Synoniem | Context |
|---|---|
| Aangifte van geboorte | wet |
| Geboorteaangifte doen | beleid |

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
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Opmaken geboorteakte](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-geboorteakte.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md), [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md), [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md), [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Burgerlijk Wetboek Boek 1](../../../../motivatie/beleidskaders/rijksregelgeving/burgerlijk-wetboek-boek-1.md) | is grondslag voor *associatie (gericht)* | Geboorteaangifte | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 136, art. 19e) |
| [Burgerlijke stand diensten](../../../bedrijfsfuncties/publieksdiensten/burgerlijke-stand-diensten.md) | omvat *aggregatie* | Geboorteaangifte | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 136 (GEMMA-domein Publieksdiensten)) |
| [Opmaken geboorteakte](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-geboorteakte.md) | realiseert *realisatie* | Geboorteaangifte | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) (UPL nr. 136) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) | Gemeente Utrecht: Geboorteaangifte |
| [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
