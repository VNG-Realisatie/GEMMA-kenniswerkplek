---
id: zakenpaspoort
type: dienst
archimate_type: business-service
status: review
naam: Zakenpaspoort
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het aanvragen en ophalen van een nationaal paspoort met 66 in plaats van 34 bladzijden.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen
- 2026-rvig-hup-uitreiking-registreren-van-een-reisdocument
- 2026-rijk-paspoortwet-bwbr0005212
---

# Zakenpaspoort

<!-- Gegenereerd door tools/render.py uit de beoordeling zakenpaspoort.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het aanvragen en ophalen van een nationaal paspoort met 66 in plaats van 34 bladzijden.

### Beschrijving

Een zakenpaspoort is een gewoon paspoort met extra bladzijden; het kan niet naast een normaal paspoort worden aangevraagd en kost hetzelfde (Utrecht). De Paspoortwet kent het niet als eigen soort; in het documentnummer heeft het de letter B (HUP Uitreiking). De UPL noemt als grondslag art. 3 Paspoortuitvoeringsregeling Buitenland 2001 (UPL nr. 494); zie de terugmelding over de grondslag.

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
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md), [HUP Uitreiking reisdocument](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-uitreiking-registreren-van-een-reisdocument.md), [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Behandelen aanvraag reisdocument](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md), [HUP Uitreiking reisdocument](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-uitreiking-registreren-van-een-reisdocument.md), [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md), [HUP Uitreiking reisdocument](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-uitreiking-registreren-van-een-reisdocument.md), [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md), [HUP Uitreiking reisdocument](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-uitreiking-registreren-van-een-reisdocument.md), [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen aanvraag reisdocument](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument.md) | realiseert *realisatie* | Zakenpaspoort | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) (UPL nr. 494) |
| [Officiële documenten verstrekking](../../../bedrijfsfuncties/publieksdiensten/officiele-documenten-verstrekking.md) | omvat *aggregatie* | Zakenpaspoort | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 494 (GEMMA-domein Publieksdiensten)) |
| [Paspoortwet](../../../../motivatie/beleidskaders/rijksregelgeving/paspoortwet.md) | is grondslag voor *associatie (gericht)* | Zakenpaspoort | [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) (art. 9, 26, 40 (nationaal paspoort); Utrecht regel 229) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) | Gemeente Utrecht: Paspoort of ID-kaart aanvragen |
| [HUP Uitreiking reisdocument](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-uitreiking-registreren-van-een-reisdocument.md) | HUP BRP: Uitreiking registreren van een reisdocument |
| [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 10](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (grondslag, open): **UPL:** zakenpaspoort heeft als grondslag art. 3 Paspoortuitvoeringsregeling Buitenland 2001 ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), nr. 494). **Bevinding:** die regeling gaat over aanvragen in het buitenland en is geen grondslag voor de gemeentelijke dienst. De gemeente verstrekt het zakenpaspoort als gewoon paspoort met 66 in plaats van 34 bladzijden ([2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md)); de Paspoortwet kent het niet als eigen soort, en de HUP geeft het de letter B in het documentnummer ([2026-rvig-hup-uitreiking-registreren-van-een-reisdocument](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-uitreiking-registreren-van-een-reisdocument.md)). GEMMA modelleert het als aanvraag van een nationaal paspoort, met de Paspoortwet als grondslag (art. 26, 40). **Voorstel:** vervang in de UPL de grondslag door art. 26 en 40 Paspoortwet.
