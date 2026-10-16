---
id: vreemdelingenpaspoort
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Vreemdelingenpaspoort
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het aanvragen en ophalen van een reisdocument voor vreemdelingen, voor wie in Nederland verblijft en geen eigen nationaal paspoort kan krijgen.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Reisdocument voor vreemdelingen aanvragen (wet)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen
---

# Vreemdelingenpaspoort

<!-- Gegenereerd door tools/render.py uit de beoordeling vreemdelingenpaspoort.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het aanvragen en ophalen van een reisdocument voor vreemdelingen, voor wie in Nederland verblijft en geen eigen nationaal paspoort kan krijgen.

### Beschrijving

Voor wie een geldig verblijfsdocument regulier heeft, geen eigen nationaal paspoort heeft en het niet bij de eigen autoriteiten kan aanvragen; de aanvraag wordt voorgelegd aan de IND en het ministerie van Buitenlandse Zaken (Utrecht). De verstrekking volgt pas als de minister van Justitie en Veiligheid heeft vastgesteld dat aan de voorwaarden is voldaan (Paspoortwet art. 12 tot en met 15, 40 lid 4). De UPL noemt als grondslag art. 11 Paspoortwet (UPL nr. 462).

### Synoniemen

| Synoniem | Context |
|---|---|
| Reisdocument voor vreemdelingen aanvragen | wet |

### Homoniemen

| Begrip | Betekenis | Naamkeuze |
|---|---|---|
| [Reisdocument voor vreemdelingen](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/reisdocument.md) (wiki, Paspoortwet art. 2, 12-15) | Het document zelf, een specialisatie zonder pagina van Reisdocument | Deze pagina heet Vreemdelingenpaspoort, de UPL-naam van de dienst (regel Naamvorm); het document zelf heet met de wetsterm Reisdocument voor vreemdelingen. |

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
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, de aanvrager, een in Nederland verblijvende vreemdeling (UPL: doelgroep burger). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert? | Ja, met [Behandelen aanvraag reisdocument](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument.md). |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, de UPL noemt het als eigen product. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen aanvraag reisdocument](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument.md) | realiseert *realisatie* | Vreemdelingenpaspoort | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) (UPL nr. 462) |
| [Officiële documenten verstrekking](../../../bedrijfsfuncties/publieksdiensten/officiele-documenten-verstrekking.md) | omvat *aggregatie* | Vreemdelingenpaspoort | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 462 (GEMMA-domein Publieksdiensten)) |
| [Paspoortwet](../../../../motivatie/beleidskaders/rijksregelgeving/paspoortwet.md) | is grondslag voor *associatie (gericht)* | Vreemdelingenpaspoort | [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (art. 12-15, 40 lid 4) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) | Gemeente Utrecht: Paspoort of ID-kaart aanvragen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
