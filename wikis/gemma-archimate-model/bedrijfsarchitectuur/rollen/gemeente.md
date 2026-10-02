---
id: gemeente
type: rol
archimate_type: business-role
status: goedgekeurd
naam: Gemeente
onderwerpen:
- lijkbezorging
definitie: Hoedanigheid van het openbaar lichaam met rechtspersoonlijkheid dat het lokale bestuur vormt, met een raad, een college en een burgemeester.
grondslag: bron
match:
  gemma: zwak
data_object: nee
bronnen:
- 2024-rijk-gemeentewet-wettekst
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2026-rijk-bw2-rechtspersonen
- 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen
gemma_id: id-17a7441705094ba9b385c25497844778
gemma_naam: Gemeente
gemma_type: business-role
gemma_definitie: Groepering van applicatieservices ten behoeve van de (medewerkers) van de gemeente
gemma_map: Business / Bedrijfsrollen
gemma_eigenschappen:
  GEMMA subtype: Doelgroep
  GEMMA type: Groep
  Object ID: ff2d196f-11e0-4328-b78a-0714eb1c4e92
---

# Gemeente

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/gemeente.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Hoedanigheid van het openbaar lichaam met rechtspersoonlijkheid dat het lokale bestuur vormt, met een raad, een college en een burgemeester.

### Beschrijving

Gemeente is de hoedanigheid waarin een afzonderlijke gemeente, zoals Amsterdam of Utrecht, optreedt. Die afzonderlijke gemeenten zijn de actoren: rechtspersonen (BW Boek 2 art. 1) met een raad, een college en een burgemeester (Gemeentewet art. 6). Het GGM en GEMMA kennen daarnaast het bedrijfsobject Gemeente als gedeelte van het grondgebied; dat is een ander begrip.

### Per onderwerp

#### [Lijkbezorging](../../begrippen/lijkbezorging.md)

De gemeente heeft ten minste één gemeentelijke begraafplaats en is daarvan houder; zij draagt de kosten van de gemeentebegrafenis, verhaalt die, en onderhoudt graven tegen betaling (Wet op de lijkbezorging art. 22, 33, 39 lid 2; Groningen art. 3, 23).

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (kern ja).

### Kenmerken

Alleen de kenmerken met ja; de overige 39 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar; de wet spreekt van 'de gemeente' (Wlb art. 22, 33). [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [BW Boek 2](../../bronanalyses/lijkbezorging/2026-rijk-bw2-rechtspersonen.md), [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de gemeente zelf. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [BW Boek 2](../../bronanalyses/lijkbezorging/2026-rijk-bw2-rechtspersonen.md), [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [BW Boek 2](../../bronanalyses/lijkbezorging/2026-rijk-bw2-rechtspersonen.md), [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, en niet bij een ander onderwerp waar het wordt beoordeeld? | Ja, hoort primair bij dit onderwerp; geen ander onderwerp beoordeelt het. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [BW Boek 2](../../bronanalyses/lijkbezorging/2026-rijk-bw2-rechtspersonen.md), [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **hoedanigheid**: Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de hoedanigheid waarin een partij optreedt? | Ja, de hoedanigheid waarin een afzonderlijke gemeente, als rechtspersoon (BW Boek 2 art. 1), optreedt. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [BW Boek 2](../../bronanalyses/lijkbezorging/2026-rijk-bw2-rechtspersonen.md), [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, toegewezen aan de functie Lijkbezorging en aan Verzorgen gemeentebegrafenis (kosten en verhaal, art. 22) en Onderhouden graf (Groningen art. 23). [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [BW Boek 2](../../bronanalyses/lijkbezorging/2026-rijk-bw2-rechtspersonen.md), [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder element in deze wiki. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [BW Boek 2](../../bronanalyses/lijkbezorging/2026-rijk-bw2-rechtspersonen.md), [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Gemeente | voert uit *toewijzing* | [Lijkbezorging](../bedrijfsfuncties/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/lijkbezorging.md) | [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 4, 21, 33) |
| Gemeente | draagt de kosten van *toewijzing* | [Verzorgen gemeentebegrafenis](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verzorgen-gemeentebegrafenis.md) | [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 22) |
| Gemeente | voert uit *toewijzing* | [Onderhouden graf](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/onderhouden-graf.md) | [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (art. 23) |
| Gemeente | heeft *toegang (houder)* | [Begraafplaats](../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/begraafplaats.md) | [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (Wlb art. 33; Groningen art. 3) |
| Gemeente | heeft het uitsluitend recht tot begraven in (algemeen graf) *toegang (houder)* | [Graf](../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/graf.md) | [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (art. 13 lid 1) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Gemeentewet](../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md) | Gemeentewet (BWBR0005416) - geldend per 2024-01-31 |
| [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [BW Boek 2](../../bronanalyses/lijkbezorging/2026-rijk-bw2-rechtspersonen.md) | Burgerlijk Wetboek Boek 2 Rechtspersonen (BWBR0003045) |
| [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) | Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023 |

### Afstemming met GEMMA

Match **zwak** met GEMMA-element *Gemeente* (business-role). GEMMA-rol Gemeente is een doelgroep, een groepering van applicatieservices voor de medewerkers van de gemeente. Zelfde naam en type, ander gebruik; nieuw: een definitie van de rol zelf.

> Groepering van applicatieservices ten behoeve van de (medewerkers) van de gemeente

### Besluiten redacteur

- 2026-09-30: Rol, geen actor: Gemeente is de hoedanigheid; de afzonderlijke gemeenten zijn de actoren.
