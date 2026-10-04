---
id: ketenpartner
type: rol
archimate_type: business-role
status: goedgekeurd
naam: Ketenpartner
onderwerpen:
- lijkbezorging
definitie: Verantwoordelijkheid van een andere organisatie voor haar deel van een ketenproces dat zij met de gemeente uitvoert.
grondslag: bron
match:
  gemma: exact
data_object: nee
doelgroep: ketenpartners
bronnen:
- 2026-vng-gemma-2026-10-02
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
gemma_id: id-e03a0402-1890-4a21-8143-c44a8ba53ea4
gemma_naam: Ketenpartner
gemma_type: business-role
gemma_map: Business / Procesarchitectuur / Actoren en rollen
gemma_eigenschappen:
  Object ID: e03a0402-1890-4a21-8143-c44a8ba53ea4
---

# Ketenpartner

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/ketenpartner.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Verantwoordelijkheid van een andere organisatie voor haar deel van een ketenproces dat zij met de gemeente uitvoert.

### Beschrijving

Een ketenpartner is een andere organisatie die een eigen deel van een ketenproces uitvoert, vanuit een eigen wettelijke taak, en niet als klant of alleen als adviseur. GEMMA kent de rol Ketenpartner in de procesarchitectuur en de doelgroep Ketenpartners.

### Per onderwerp

#### [Lijkbezorging](../../begrippen/lijkbezorging.md)

De officier van justitie is ketenpartner in Bezorgen lijken: hij ontvangt bij een niet-natuurlijke dood het verslag van de lijkschouwer, geeft de verklaring van geen bezwaar af en stemt in met een vervroegde uitvaart (Wet op de lijkbezorging art. 10, 12, 17).

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (kern ja).

### Plaats in de indelingen

- **Doelgroep**: ketenpartners.

### Kenmerken

Alleen de kenmerken met ja; de overige 53 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, GEMMA kent de rol Ketenpartner en de doelgroep Ketenpartners; de officier van justitie is ketenpartner in de lijkbezorging (art. 10, 12). [GEMMA](../../../../sources/raw/2026-vng-gemma-2026-10-02.md), [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, structurele, wettelijke rol in een gemeentelijk ketenproces (art. 10, 12, 17). [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, een eigen verantwoordelijkheid in een ketenproces. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, en niet bij een ander onderwerp waar het wordt beoordeeld? | Ja, geen ander onderwerp beoordeelt het. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **hoedanigheid**: Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de hoedanigheid waarin een partij optreedt? | Ja, de verantwoordelijkheid van een andere organisatie voor haar deel van een ketenproces. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, bezorgen lijken: de officier van justitie geeft de verklaring van geen bezwaar af en stemt in met een vervroegde uitvaart (art. 12, 17). [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen bredere rol in deze wiki. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Ketenpartner | voert zijn deel uit van *toewijzing* | [Bezorgen lijken](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bezorgen-lijken.md) | [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 10, 12, 17) |
| Ketenpartner | stemt in met vervroegen bij *toewijzing* | [Stellen andere termijn](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stellen-andere-termijn.md) | [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 17 lid 1) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Officier van justitie](../actoren/officier-van-justitie.md) | vervult *toewijzing* | Ketenpartner | [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 10, 12, 17) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [GEMMA](../../../../sources/raw/2026-vng-gemma-2026-10-02.md) | GEMMA-architectuurmodel |
| [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GEMMA

Match **exact** met GEMMA-element *Ketenpartner* (business-role). GEMMA-rol Ketenpartner (procesarchitectuur, actoren en rollen); zelfde begrip, in GEMMA zonder definitie. Nieuw: een definitie.

### Besluiten redacteur

- 2026-10-04: Nieuwe rol Ketenpartner met exacte GEMMA-match; vervuld door de Officier van justitie, toegewezen aan Bezorgen lijken en Stellen andere termijn.
