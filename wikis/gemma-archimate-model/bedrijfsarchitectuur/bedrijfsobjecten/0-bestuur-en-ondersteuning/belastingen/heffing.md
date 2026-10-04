---
id: heffing
type: bedrijfsobject
archimate_type: business-object
status: kandidaat
naam: Heffing
onderwerpen:
- lijkbezorging
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Belastingen
definitie: Een door de overheid opgelegde verplichting tot betaling.
grondslag: ggm-entiteit
match:
  ggm: exact
  gemma: exact
data_object: ja
bronnen:
- 2024-rijk-gemeentewet-wettekst
- 2026-vng-retributies
- 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen
ggm_entiteit: Heffing
ggm_guid: EAID_B3371695_97AD_49d2_9AF1_15591B422007
ggm_uml_type: Class
ggm_beleidsdomein: RGBZPlus
ggm_taakveld: 99 Kern
ggm_diagram:
- Diagram Vergunningen en Meldingen
- Verkamering en Woonoverlast
- Entiteiten Dienstverlening
ggm_diagram_ids:
- EAID_BB52C835_0B2D_4164_AC9D_9D6EDBD7E267
- EAID_B039478A_DAF7_458f_A7C7_E4744EC08DBF
- EAID_48B6C3F9_CCF1_4794_8252_FC6543409B78
ggm_definitie: Een door de overheid opgelegde verplichting tot betaling
gemma_id: id-68bccce27b314b94a022ddd81d517d82
gemma_naam: Heffing
gemma_type: business-object
gemma_definitie: Een door de overheid opgelegde verplichting tot betaling
gemma_map: Business / _Sync GEMMA en project / GGM / Bedrijfsobjecten
gemma_eigenschappen:
  GEMMA URL: https://gemmaonline.nl/index.php/GEMMA/id-ff9366e3-dd65-48ce-9051-9d6b01b2c6db
  GGM-datum-tijd-export: 10122024-112046
  GGM-guid: '{B3371695-97AD-49d2-9AF1-15591B422007}'
  GGM-uml-type: Class
  Let op: '"ggm-" properties worden beheerd in het GGM informatiemodel'
  Object ID: ff9366e3-dd65-48ce-9051-9d6b01b2c6db
---

# Heffing

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/heffing.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: kandidaat.** Er staat een vraag open voor de redacteur (zie *Ter discussie*).

## Ter discussie

- geen proces bepaalt de levensloop van dit object (kernobject), en het is geen deel van een object of generiek

## Betekenis

### Definitie

Een door de overheid opgelegde verplichting tot betaling.

### Beschrijving

Een heffing is een door de overheid opgelegde verplichting tot betaling. De gemeente heft alleen de belastingen die de wet toestaat, waaronder rechten voor het gebruik van gemeentebezittingen en het genot van gemeentelijke diensten (Gemeentewet art. 229); de tarieven gaan niet boven de kosten uit (art. 229b).

### Per onderwerp

#### [Lijkbezorging](../../../../begrippen/lijkbezorging.md)

De gemeente heft lijkbezorgingsrechten, ook begraafplaatsrechten genoemd: retributies voor het gebruik van de gemeentelijke begraafplaats of het crematorium, voor de uitgifte en het onderhoud van graven en urnen, en voor gemeentelijke diensten (VNG retributies; Groningen art. 8, 23).

## Plaats in het model

### Typering

Bedrijfsobject. Uitkomst van de beslistabel: Passief (kern ja, 2/2).

### Plaats in de indelingen

- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Belastingen.

### Kenmerken

Alleen de kenmerken met ja; de overige 51 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, GGM-entiteit; gangbaar (lijkbezorgingsrechten, retributie). [Gemeentewet](../../../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md), [VNG Retributies](../../../../bronanalyses/lijkbezorging/2026-vng-retributies.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de gemeente heft (Gemeentewet art. 229). [Gemeentewet](../../../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md), [VNG Retributies](../../../../bronanalyses/lijkbezorging/2026-vng-retributies.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Gemeentewet](../../../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md), [VNG Retributies](../../../../bronanalyses/lijkbezorging/2026-vng-retributies.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, en niet bij een ander onderwerp waar het wordt beoordeeld? | Ja, hoort primair bij dit onderwerp; geen ander onderwerp beoordeelt het. [Gemeentewet](../../../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md), [VNG Retributies](../../../../bronanalyses/lijkbezorging/2026-vng-retributies.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, per belastingplichtige en belastbaar feit. [Gemeentewet](../../../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, opgelegd, betaald, ingevorderd (Gemeentewet hfst. XV). [Gemeentewet](../../../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, vastgelegd bij de uitgifte van een graf en het onderhoud ervan (VNG retributies; Groningen art. 23). [VNG Retributies](../../../../bronanalyses/lijkbezorging/2026-vng-retributies.md), [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **geautomatiseerd verwerkt**: Wordt het als gegevensstructuur geautomatiseerd verwerkt? | Ja, GGM-entiteit. [Gemeentewet](../../../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, het hoogste herkenbare niveau voor lijkbezorgingsrechten en retributie (besluit redacteur 2026-09-30). [VNG Retributies](../../../../bronanalyses/lijkbezorging/2026-vng-retributies.md) |

### Specialisaties

- **Lijkbezorgingsrechten**: Retributies voor het gebruik van de gemeentelijke begraafplaats of het crematorium (VNG retributies). Geen eigen pagina.
- **Retributie**: Heffing voor het gebruik van gemeentebezittingen of het genot van gemeentelijke diensten (Gemeentewet art. 229; VNG retributies). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Heffing | voor het gebruik van (lijkbezorgingsrechten) *associatie (gericht)* | [Begraafplaats](../../7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/begraafplaats.md) | [VNG Retributies](../../../../bronanalyses/lijkbezorging/2026-vng-retributies.md) (§ Lijkbezorgingsrechten) |
| Heffing | voor het gebruik van (lijkbezorgingsrechten) *associatie (gericht)* | [Crematorium](../../7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/crematorium.md) | [VNG Retributies](../../../../bronanalyses/lijkbezorging/2026-vng-retributies.md) (§ Lijkbezorgingsrechten) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Heffingsverordening](heffingsverordening.md) | regelt *associatie (gericht)* | Heffing | [Gemeentewet](../../../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md), [VNG Retributies](../../../../bronanalyses/lijkbezorging/2026-vng-retributies.md) (Gemeentewet art. 216, 229; § Lijkbezorgingsrechten) |
| [Onderhouden graf](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/onderhouden-graf.md) | leidt tot (recht voor onderhoud) *toegang (registreren)* | Heffing | [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md), [VNG Retributies](../../../../bronanalyses/lijkbezorging/2026-vng-retributies.md) (Groningen art. 23 lid 2; § Lijkbezorgingsrechten) |
| [Verlenen grafrecht](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlenen-grafrecht.md) | leidt tot (lijkbezorgingsrechten) *toegang (registreren)* | Heffing | [VNG Retributies](../../../../bronanalyses/lijkbezorging/2026-vng-retributies.md) (§ Lijkbezorgingsrechten) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Gemeentewet](../../../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md) | Gemeentewet (BWBR0005416) - geldend per 2024-01-31 |
| [VNG Retributies](../../../../bronanalyses/lijkbezorging/2026-vng-retributies.md) | Retributies |
| [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) | Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023 |

### Afstemming met GGM

Match **exact** met GGM-entiteit *Heffing* (beleidsdomein RGBZPlus, taakveld 99 Kern). Zelfde begrip en definitie.

> Een door de overheid opgelegde verplichting tot betaling

### Afstemming met GEMMA

Match **exact** met GEMMA-element *Heffing* (business-object). Zelfde begrip.

> Een door de overheid opgelegde verplichting tot betaling

### Besluiten redacteur

- 2026-09-30: Het hoogste herkenbare niveau voor lijkbezorgingsrechten en retributie.
