---
id: identiteitskaart
type: dienst
archimate_type: business-service
status: review
naam: Identiteitskaart
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het aanvragen en ophalen van een Nederlandse identiteitskaart, waarmee een Nederlander zich identificeert en naar een deel van de landen kan reizen.
match:
  gemma: geen
data_object: nee
afnemer: extern
domein: Publieksdiensten
synoniemen:
- ID-kaart (beleid)
- Nederlandse identiteitskaart (wet)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen
---

# Identiteitskaart

<!-- Gegenereerd door tools/render.py uit de beoordeling identiteitskaart.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het aanvragen en ophalen van een Nederlandse identiteitskaart, waarmee een Nederlander zich identificeert en naar een deel van de landen kan reizen.

### Beschrijving

Een ID-kaart is goedkoper dan een paspoort, maar niet voor alle landen geldig; ze kan naast een paspoort bestaan. Een kind jonger dan twaalf jaar heeft toestemming van de ouders of gezaghebbers nodig (Utrecht; Wet op de Nederlandse identiteitskaart art. 22). Sinds 2026-10-01 regelt de Wet op de Nederlandse identiteitskaart de aanvraag, verstrekking, uitreiking, weigering, het verval en de inhouding van de kaart (art. 11, 15-39); de Paspoortwet levert de registers van de minister (Paspoortwet art. 1 onder u, 4a, 25). De UPL noemt als grondslag art. 16a Paspoortwet (UPL nr. 186); die paragraaf is per 2026-10-01 vervallen, zie de terugmelding over de grondslag.

### Synoniemen

| Synoniem | Context |
|---|---|
| ID-kaart | beleid |
| Nederlandse identiteitskaart | wet |

### Homoniemen

| Begrip | Betekenis | Naamkeuze |
|---|---|---|
| [Nederlandse identiteitskaart](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/reisdocument.md) (wiki, Paspoortwet art. 1 onder u) | Het document zelf, een specialisatie zonder pagina van Reisdocument | Deze pagina heet Identiteitskaart, de UPL-naam van de dienst (regel Naamvorm); het document zelf heet met de wetsterm Nederlandse identiteitskaart. |

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (kern ja, 2/2).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Officiële documenten verstrekking](../../../bedrijfsfuncties/publieksdiensten/officiele-documenten-verstrekking.md).
- **Afnemer**: extern.
- **Domein**: Publieksdiensten.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de aanvrager krijgt het reisdocument uitgereikt. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke aanvraag. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, de aanvrager, een inwoner (UPL: doelgroep burger). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert? | Ja, met [Behandelen aanvraag reisdocument](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument.md). |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, de UPL noemt het als eigen product. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen aanvraag reisdocument](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument.md) | realiseert *realisatie* | Identiteitskaart | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) (UPL nr. 186) |
| [Officiële documenten verstrekking](../../../bedrijfsfuncties/publieksdiensten/officiele-documenten-verstrekking.md) | omvat *aggregatie* | Identiteitskaart | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 186 (GEMMA-domein Publieksdiensten)) |
| [Wet op de Nederlandse identiteitskaart](../../../../motivatie/beleidskaders/rijksregelgeving/wet-op-de-nederlandse-identiteitskaart.md) | is grondslag voor *associatie (gericht)* | Identiteitskaart | [Wet op de Nederlandse identiteitskaart](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-nederlandse-identiteitskaart-bwbr0052951.md) (art. 11, 15, 25) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) | Gemeente Utrecht: Paspoort of ID-kaart aanvragen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 9](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (grondslag, open): **UPL:** identiteitskaart heeft als grondslag art. 16a Paspoortwet ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), nr. 186). **Bevinding:** paragraaf 3A van de Paspoortwet, met art. 16a en 17 over de Nederlandse identiteitskaart, is per 2026-10-01 vervallen. De kaart heeft een eigen wet, de Wet op de Nederlandse identiteitskaart, waarnaar de Paspoortwet verwijst ([2026-rijk-paspoortwet-bwbr0005212](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), art. 1 onder u, § 3A). GEMMA gebruikt die wet als grondslag ([2026-rijk-wet-op-de-nederlandse-identiteitskaart-bwbr0052951](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-nederlandse-identiteitskaart-bwbr0052951.md), art. 11, 15, 25). **Voorstel:** vervang in de UPL de grondslag door art. 11, 15 en 25 Wet op de Nederlandse identiteitskaart.
