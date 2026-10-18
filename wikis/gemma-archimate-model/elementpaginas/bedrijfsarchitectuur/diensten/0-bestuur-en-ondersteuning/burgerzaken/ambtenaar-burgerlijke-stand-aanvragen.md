---
id: ambtenaar-burgerlijke-stand-aanvragen
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Ambtenaar burgerlijke stand aanvragen
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het laten aanwijzen van een eigen trouwambtenaar voor één dag, voor de voltrekking van het eigen huwelijk of partnerschap.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Ambtenaar burgelijke stand (UPL)
- Trouwambtenaar voor één dag (beleid)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
---

# Ambtenaar burgerlijke stand aanvragen

<!-- Gegenereerd door tools/render.py uit de beoordeling ambtenaar-burgerlijke-stand-aanvragen.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het laten aanwijzen van een eigen trouwambtenaar voor één dag, voor de voltrekking van het eigen huwelijk of partnerschap.

### Beschrijving

Utrecht: € 313,45 in 2026. Grondslag art. 16 BW 1 (UPL nr. 28).

### Synoniemen

| Synoniem | Context |
|---|---|
| Ambtenaar burgelijke stand | UPL |
| Trouwambtenaar voor één dag | beleid |

### Homoniemen

| Begrip | Betekenis | Naamkeuze |
|---|---|---|
| [Ambtenaar van de burgerlijke stand](../../../rollen/ambtenaar-van-de-burgerlijke-stand.md) (wiki, BW 1 art. 16) | De rol: de ambtenaar die bevoegd is akten op te maken | Deze pagina heet Ambtenaar burgerlijke stand aanvragen, de dienst; de UPL-naam is een synoniem, omdat de rol die naam draagt (precedent Briefadres aanvragen). |

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
| [Burgerlijk Wetboek Boek 1](../../../../motivatie/beleidskaders/rijksregelgeving/burgerlijk-wetboek-boek-1.md) | is grondslag voor *associatie (gericht)* | Ambtenaar burgerlijke stand aanvragen | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 28, art. 16) |
| [Burgerlijke stand diensten](../../../bedrijfsfuncties/publieksdiensten/burgerlijke-stand-diensten.md) | omvat *aggregatie* | Ambtenaar burgerlijke stand aanvragen | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 28 (GEMMA-domein Publieksdiensten)) |
| [Voltrekken huwelijk](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/voltrekken-huwelijk.md) | realiseert *realisatie* | Ambtenaar burgerlijke stand aanvragen | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Trouwen in Utrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-trouwen-in-utrecht.md) (UPL nr. 28; Utrecht trouwambtenaar voor één dag) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
