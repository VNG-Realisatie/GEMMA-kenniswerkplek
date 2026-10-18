---
id: stemrecht
type: dienst
archimate_type: business-service
status: review
naam: Stemrecht
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het registreren als kiezer van wie kiesgerechtigd is, en op verzoek meedelen of iemand als kiezer is geregistreerd.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rijk-kieswet-bwbr0004627
---

# Stemrecht

<!-- Gegenereerd door tools/render.py uit de beoordeling stemrecht.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het registreren als kiezer van wie kiesgerechtigd is, en op verzoek meedelen of iemand als kiezer is geregistreerd.

### Beschrijving

Kiesgerechtigd voor de gemeenteraad zijn ingezetenen van achttien jaar en ouder, ook niet-Nederlanders met verblijfsrecht na vijf jaar verblijf; een EU-onderdaan kan zich registreren voor de verkiezing van het Europees Parlement (Kieswet art. B 1-B 3; HUP Europees kiesrecht). De gemeente registreert de kiesgerechtigdheid en deelt op verzoek mee of iemand als kiezer is geregistreerd (art. D 1, D 5). Grondslag art. B 1, B 2, B 2a, B 3 en Y 2 Kieswet; doelgroep burger, SDG; niet digitaal (UPL nr. 398). De UPL-naam noemt het recht; de dienst is de registratie en de mededeling (procesarchitectuur-terugmelding).

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Verkiezingen gerelateerde diensten](../../../bedrijfsfuncties/publieksdiensten/verkiezingen-gerelateerde-diensten.md).
- **Afnemer**: extern.
- **Domein**: Publieksdiensten.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Registreren kiesgerechtigdheid](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/registreren-kiesgerechtigdheid.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Stemrecht | bedient *bediening* | [Kiezer](../../../rollen/kiezer.md) | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. D 5) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Kieswet](../../../../motivatie/beleidskaders/rijksregelgeving/kieswet.md) | is grondslag voor *associatie (gericht)* | Stemrecht | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. B 1-B 3; UPL nr. 398) |
| [Registreren kiesgerechtigdheid](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/registreren-kiesgerechtigdheid.md) | realiseert *realisatie* | Stemrecht | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (UPL nr. 398) |
| [Verkiezingen gerelateerde diensten](../../../bedrijfsfuncties/publieksdiensten/verkiezingen-gerelateerde-diensten.md) | omvat *aggregatie* | Stemrecht | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 398 (GEMMA-domein Publieksdiensten)) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) | Kieswet |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 14](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (product, open): **UPL:** het product stemrecht heeft als grondslag art. B 1-B 3 en Y 2 Kieswet ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), nr. 398). **Bevinding:** het kiesrecht is een recht van de persoon, geen prestatie van de gemeente. Wat de gemeente levert, is de registratie van de kiesgerechtigdheid en de mededeling op verzoek of iemand als kiezer is geregistreerd ([2026-rijk-kieswet-bwbr0004627](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), art. D 1, D 5). In GEMMA is Stemrecht de dienst die het bedrijfsproces Registreren kiesgerechtigdheid realiseert. **Voorstel:** voeg in de UPL art. D 1 en D 5 Kieswet toe als grondslag, en beschrijf het product als de registratie van en de mededeling over de kiesgerechtigdheid.
