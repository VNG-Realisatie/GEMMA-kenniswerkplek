---
id: gemeenteraad
type: actor
archimate_type: business-actor
status: goedgekeurd
naam: Gemeenteraad
onderwerpen:
- algemeen
- lijkbezorging
definitie: Bestuursorgaan van de gemeente dat de gehele bevolking vertegenwoordigt en de gemeentelijke verordeningen vaststelt.
grondslag: bron
match:
  gemma: exact
data_object: nee
doelgroep: gemeente
synoniemen:
- Raad (wet)
bronnen:
- 2024-rijk-gemeentewet-wettekst
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
gemma_id: id-b69cb101-8708-47de-9ac1-e138f205a49f
gemma_naam: Gemeenteraad
gemma_type: business-actor
gemma_map: Business / Procesarchitectuur / Actoren en rollen
gemma_eigenschappen:
  Object ID: b69cb101-8708-47de-9ac1-e138f205a49f
---

# Gemeenteraad

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/gemeenteraad.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Bestuursorgaan van de gemeente dat de gehele bevolking vertegenwoordigt en de gemeentelijke verordeningen vaststelt.

### Beschrijving

De raad vertegenwoordigt de gehele bevolking van de gemeente (Gemeentewet art. 7). Hij stelt de gemeentelijke verordeningen vast, voor zover die bevoegdheid niet bij het college of de burgemeester ligt (art. 147, 149), en benoemt de wethouders (art. 35). De burgemeester is voorzitter van de raad (art. 9).

### Per onderwerp

#### [Lijkbezorging](../../begrippen/lijkbezorging.md)

De raad stelt de beheersverordening begraafplaatsen en de verordening lijkbezorgingsrechten vast, wijst grond aan voor bijzondere begraafplaatsen en kan een kerkgenootschap meer begraafplaatsen toestaan (Wet op de lijkbezorging art. 35, 38, 40).

### Synoniemen

| Synoniem | Context |
|---|---|
| Raad | wet |

## Plaats in het model

### Typering

Actor. Uitkomst van de beslistabel: Handelende partij (kern ja).

### Plaats in de indelingen

- **Doelgroep**: gemeente.

### Kenmerken

Alleen de kenmerken met ja; de overige 50 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar; wettelijk 'raad' (Gemeentewet art. 6, 7; titel hoofdstuk II). [Gemeentewet](../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, bestuursorgaan van de gemeente. [Gemeentewet](../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Gemeentewet](../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij dit onderwerp; geen ander onderwerp beoordeelt het. [Gemeentewet](../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **handelende partij**: Is het een organisatie, afdeling of persoon die activiteiten kan uitvoeren? | Ja, bestuursorgaan dat de bevolking vertegenwoordigt en verordeningen vaststelt. [Gemeentewet](../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |
| **los van verantwoordelijkheid**: Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen? | Ja, bestaat los van elke afzonderlijke bevoegdheid. [Gemeentewet](../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |
| **vervult een rol**: Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? | Ja, vervult de rol Beslisser: stelt de verordeningen vast, wijst grond aan voor een bijzondere begraafplaats en staat een kerkgenootschap meer begraafplaatsen toe (Gemeentewet art. 147, 149; Wlb art. 38, 40). [Gemeentewet](../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **soort partij**: Heeft elke gemeente met deze partij te maken in dezelfde rol, zodat het element voor alle gemeenten geldt? Het criterium sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat. | Ja, elke gemeente heeft een raad, een college van burgemeester en wethouders en een burgemeester (Gemeentewet art. 6). [Gemeentewet](../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder element in deze wiki. [Gemeentewet](../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |
| **generiek**: Komt het met dezelfde betekenis in veel onderwerpen voor? | Ja, komt in elk onderwerp voor als bestuursorgaan (Gemeentewet art. 6). [Gemeentewet](../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Gemeenteraad | vervult *toewijzing* | [Beslisser](../rollen/beslisser.md) | [Gemeentewet](../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (Gemeentewet art. 147; Wlb art. 38, 40) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Burgemeester](burgemeester.md) | is voorzitter van *associatie (gericht)* | Gemeenteraad | [Gemeentewet](../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) (art. 9) |
| [Gemeente](gemeente.md) | omvat *aggregatie* | Gemeenteraad | [Gemeentewet](../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) (art. 6) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Gemeentewet](../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) | Gemeentewet (BWBR0005416) - geldend per 2024-01-31 |
| [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GEMMA

Match **exact** met GEMMA-element *Gemeenteraad* (business-actor). Zelfde begrip.
