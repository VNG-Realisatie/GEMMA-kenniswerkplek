---
id: heffingsverordening
type: bedrijfsobject
archimate_type: business-object
status: goedgekeurd
naam: Heffingsverordening
onderwerpen:
- algemeen
- lijkbezorging
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Belastingen
definitie: Door de gemeenteraad vastgestelde verordening over de heffing en invordering van gemeentelijke belastingen of rechten.
grondslag: ggm-entiteit
match:
  ggm: exact
  gemma: sterk
data_object: ja
objectniveau: generiek
synoniemen:
- Belastingverordening (wet)
bronnen:
- 2024-rijk-gemeentewet-wettekst
- 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen
- 2026-vng-retributies
ggm_entiteit: Heffingsverordening
ggm_guid: EAID_C29CCD49_04E2_44b4_A6B0_AD8B10552628
ggm_uml_type: Class
ggm_beleidsdomein: 1 Veiligheid en Vergunningen
ggm_taakveld: 1 Veiligheid en Vergunningen
ggm_diagram:
- Diagram Vergunningen en Meldingen
- Verkamering en Woonoverlast
ggm_diagram_ids:
- EAID_BB52C835_0B2D_4164_AC9D_9D6EDBD7E267
- EAID_B039478A_DAF7_458f_A7C7_E4744EC08DBF
ggm_definitie: Een *heffingsverordening* is een door de gemeenteraad vastgestelde verordening die de **heffing en invordering van gemeentelijke belastingen en rechten** regelt, zoals afvalstoffenheffing, precariobelasting of marktgelden.
ggm_toelichting: Gemeenten mogen alleen heffingen vaststellen binnen de kaders die de wet hen geeft. Een heffingsverordening bevat de regels over **welke belastingen of rechten worden geheven, wie belastingplichtig is, wat de maatstaf en tarieven zijn, en hoe invordering plaatsvindt**. Dit is de lokale juridische basis voor het innen van gemeentelijke heffingen waarvoor de gemeenteraad een verordening opstelt.
gemma_id: id-b5f50c54f1cf45b8b7b61a5929035919
gemma_naam: Heffingsverordening
gemma_type: business-object
gemma_definitie: Een vastgestelde regeling waarin de grondslagen, tarieven en voorwaarden voor belastingen en heffingen zijn vastgelegd.
gemma_map: Business / _Sync GEMMA en project / GGM / Bedrijfsobjecten
gemma_eigenschappen:
  GEMMA URL: https://gemmaonline.nl/index.php/GEMMA/id-f94b299a-c9eb-4bdb-82e7-5752360494cd
  GGM-datum-tijd-export: 10122024-112046
  GGM-guid: '{C29CCD49-04E2-44b4-A6B0-AD8B10552628}'
  GGM-uml-type: Class
  Let op: '"ggm-" properties worden beheerd in het GGM informatiemodel'
  Object ID: f94b299a-c9eb-4bdb-82e7-5752360494cd
---

# Heffingsverordening

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/heffingsverordening.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Door de gemeenteraad vastgestelde verordening over de heffing en invordering van gemeentelijke belastingen of rechten.

### Beschrijving

De raad voert een gemeentelijke belasting in, wijzigt of schaft haar af door een belastingverordening vast te stellen (Gemeentewet art. 216). Die vermeldt onder meer de belastingplichtige, het belastbaar feit en het tarief (art. 217).

### Per onderwerp

#### [Lijkbezorging](../../../../begrippen/lijkbezorging.md)

Gemeenten leggen de lijkbezorgingsrechten vast in een heffingsverordening, de verordening op de heffing en invordering van rechten voor het gebruik van de gemeentelijke begraafplaatsen (Groningen art. 1 l; VNG retributies). De beheersverordening verwijst ernaar voor de tarieven (Groningen art. 8, 23, 24).

### Synoniemen

| Synoniem | Context |
|---|---|
| Belastingverordening | wet |

## Plaats in het model

### Typering

Bedrijfsobject, niveau generiek. Uitkomst van de beslistabel: Passief (kern ja, 2/2).

### Plaats in de indelingen

- **Objectniveau**: generiek.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Belastingen.

### Specialisaties per onderwerp

#### Lijkbezorging

- **Verordening lijkbezorgingsrechten**: Specialisatie zonder pagina van Heffingsverordening: verordening die de lijkbezorgingsrechten regelt (VNG retributies; Groningen art. 1 l).

### Kenmerken

Alleen de kenmerken met ja; de overige 50 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, GGM-entiteit; gangbaar (Groningen art. 1 l). [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md), [VNG Retributies](../../../../bronanalyses/lijkbezorging/overig/2026-vng-retributies.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de raad stelt haar vast (Gemeentewet art. 216). [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md), [VNG Retributies](../../../../bronanalyses/lijkbezorging/overig/2026-vng-retributies.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md), [VNG Retributies](../../../../bronanalyses/lijkbezorging/overig/2026-vng-retributies.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij dit onderwerp; geen ander onderwerp beoordeelt het. [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md), [VNG Retributies](../../../../bronanalyses/lijkbezorging/overig/2026-vng-retributies.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, per belasting of recht en per gemeente. [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, vastgesteld, gewijzigd, ingetrokken (Gemeentewet art. 216). [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, geraadpleegd voor de tarieven bij uitgifte en onderhoud (Groningen art. 8, 23, 24). [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **geautomatiseerd verwerkt**: Wordt het als gegevensstructuur geautomatiseerd verwerkt? | Ja, GGM-entiteit. [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, specialisatie van Regeling met eigen gegevens (belastingplichtige, belastbaar feit, tarief, art. 217); het hoogste herkenbare niveau voor de verordening lijkbezorgingsrechten (besluit redacteur 2026-09-30). [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |
| **generiek**: Komt het met dezelfde betekenis in veel onderwerpen voor? | Ja, heffingsverordeningen komen in veel onderwerpen voor (Gemeentewet art. 216, 229). [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |

### Specialisaties

- **Verordening lijkbezorgingsrechten**: Verordening die de retributies en vergoedingen voor begraafplaats en crematorium regelt (VNG retributies). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Heffingsverordening | regelt *associatie (gericht)* | [Heffing](heffing.md) | [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [VNG Retributies](../../../../bronanalyses/lijkbezorging/overig/2026-vng-retributies.md) (Gemeentewet art. 216, 229; § Lijkbezorgingsrechten) |
| Heffingsverordening | is een *specialisatie* | [Regeling](../besluitvorming/regeling.md) | [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) (art. 216) |
| Heffingsverordening | regelt het recht voor *associatie (gericht)* | [Grafonderhoud](../../../diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/grafonderhoud.md) | [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (art. 23, 24) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) | Gemeentewet (BWBR0005416) - geldend per 2024-01-31 |
| [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) | Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023 |
| [VNG Retributies](../../../../bronanalyses/lijkbezorging/overig/2026-vng-retributies.md) | Retributies |

### Afstemming met GGM

Match **exact** met GGM-entiteit *Heffingsverordening* (beleidsdomein 1 Veiligheid en Vergunningen, taakveld 1 Veiligheid en Vergunningen). Zelfde begrip; de GGM-definitie noemt ook rechten.

> Een *heffingsverordening* is een door de gemeenteraad vastgestelde verordening die de **heffing en invordering van gemeentelijke belastingen en rechten** regelt, zoals afvalstoffenheffing, precariobelasting of marktgelden.

### Afstemming met GEMMA

Match **sterk** met GEMMA-element *Heffingsverordening* (business-object). Zelfde begrip; nieuw: een herkenbare definitie.

> Een vastgestelde regeling waarin de grondslagen, tarieven en voorwaarden voor belastingen en heffingen zijn vastgelegd.

### Besluiten redacteur

- 2026-09-30: Het hoogste herkenbare niveau voor de verordening lijkbezorgingsrechten.
