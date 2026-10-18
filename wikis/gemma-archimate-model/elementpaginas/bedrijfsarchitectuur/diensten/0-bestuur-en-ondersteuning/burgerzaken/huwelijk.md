---
id: huwelijk
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Huwelijk
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het laten voltrekken van een huwelijk door de ambtenaar van de burgerlijke stand, op een gekozen datum en locatie.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Trouwen (beleid)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
---

# Huwelijk

<!-- Gegenereerd door tools/render.py uit de beoordeling huwelijk.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het laten voltrekken van een huwelijk door de ambtenaar van de burgerlijke stand, op een gekozen datum en locatie.

### Beschrijving

Na de melding van het voorgenomen huwelijk legt het paar locatie en datum vast, liefst drie maanden vooraf, met twee tot vier getuigen. Gemeenten bieden varianten met eigen tarieven, zoals gratis trouwen, eenvoudig trouwen, een flitshuwelijk of trouwen op een locatie naar keuze (Utrecht). Een geregistreerd partnerschap gaat op dezelfde manier. Grondslag art. 30 BW 1 (UPL nr. 184).

### Synoniemen

| Synoniem | Context |
|---|---|
| Trouwen | beleid |

### Homoniemen

| Begrip | Betekenis | Naamkeuze |
|---|---|---|
| Huwelijk (de relatie) (BW 1 art. 30; HUP Huwelijk/geregistreerd partnerschap) | De verbintenis tussen twee echtgenoten zelf, in de BRP een gegeven van de persoon (burgerlijke staat) | Deze pagina heet Huwelijk, de UPL-naam van de dienst (regel Naamvorm); de relatie zelf is een eigenschap van Ingeschreven persoon zonder pagina (Burgerlijke staat). |

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
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Voltrekken huwelijk](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/voltrekken-huwelijk.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Burgerlijk Wetboek Boek 1](../../../../motivatie/beleidskaders/rijksregelgeving/burgerlijk-wetboek-boek-1.md) | is grondslag voor *associatie (gericht)* | Huwelijk | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 184, art. 30) |
| [Burgerlijke stand diensten](../../../bedrijfsfuncties/publieksdiensten/burgerlijke-stand-diensten.md) | omvat *aggregatie* | Huwelijk | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 184 (GEMMA-domein Publieksdiensten)) |
| [Voltrekken huwelijk](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/voltrekken-huwelijk.md) | realiseert *realisatie* | Huwelijk | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Trouwen in Utrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-trouwen-in-utrecht.md) (UPL nr. 184) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
