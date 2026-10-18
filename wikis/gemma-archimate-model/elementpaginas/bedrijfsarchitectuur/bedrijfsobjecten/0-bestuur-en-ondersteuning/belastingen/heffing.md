---
id: heffing
type: bedrijfsobject
archimate_type: business-object
status: review
naam: Heffing
onderwerpen:
- heffingen-en-betalingen
- lijkbezorging
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Belastingen
definitie: Een door de overheid opgelegde verplichting tot betaling.
match:
  ggm: exact
  gemma: exact
data_objecten:
- Heffing-data
objectniveau: generiek
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

<!-- Gegenereerd door tools/render.py uit de beoordeling heffing.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Een door de overheid opgelegde verplichting tot betaling.

### Beschrijving

Een heffing is een door de overheid opgelegde verplichting tot betaling. De gemeente heft alleen de belastingen die de wet toestaat, waaronder rechten voor het gebruik van gemeentebezittingen en het genot van gemeentelijke diensten (Gemeentewet art. 229); de tarieven gaan niet boven de kosten uit (art. 229b).

### Per onderwerp

#### [Lijkbezorging](../../../../../onderwerpen/lijkbezorging/begrippen.md)

De gemeente heft lijkbezorgingsrechten, ook begraafplaatsrechten genoemd: retributies voor het gebruik van de gemeentelijke begraafplaats of het crematorium, voor de uitgifte en het onderhoud van graven en urnen, en voor gemeentelijke diensten (VNG retributies; Groningen art. 8, 23).

#### [Burgerzaken](../../../../../onderwerpen/burgerzaken/begrippen.md)

De gemeente heft rechten voor de handelingen van de burgemeester ten behoeve van de aanvraag van een reisdocument; ze gelden als gemeentelijke belasting en worden bij de indiening voldaan (Paspoortwet art. 7 lid 2 en 4, 33).

## Plaats in het model

### Typering

Bedrijfsobject, niveau generiek. Uitkomst van de beslistabel: Passief, object (3 toetskenmerken ja).

### Plaats in de indelingen

- **Objectniveau**: generiek.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Belastingen.

### Specialisaties per onderwerp

#### Burgerzaken

- **Leges reisdocumenten**: Specialisatie zonder pagina van Heffing: de rechten voor de aanvraag van een reisdocument, gemeentelijke belasting en bij de indiening te voldoen (Paspoortwet art. 7, 33). Het tarief en de bezorgkosten zijn lokale gegevens (Utrecht).

#### Lijkbezorging

- **Grafrechten**: Specialisatie zonder pagina van Heffing: in de UPL het product grafrechten (nr. 164, Gemeentewet art. 229), de lijkbezorgingsrechten voor de uitgifte van een graf; het tarief van de dienst Grafuitgifte. Niet te verwarren met Grafrecht, het recht op het graf zelf.
- **Lijkbezorgingsrechten**: Specialisatie zonder pagina van Heffing: retributies voor het gebruik van begraafplaats of crematorium (VNG retributies). Genoemd door [Gemeentewet](../../../../motivatie/beleidskaders/rijksregelgeving/gemeentewet.md).
- **Retributie**: Specialisatie zonder pagina van Heffing: heffing voor het gebruik van gemeentebezittingen of het genot van gemeentelijke diensten (Gemeentewet art. 229; VNG retributies).

### Kenmerken

**Vak**: bedrijfslaag, passief (Bedrijfsobject, Afspraak, Representatie (geen pagina)). **Hoofdkenmerk**: object.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Gemeentewet](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [VNG Retributies](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-retributies.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, met Onderhouden graf, [Verlenen grafrecht](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlenen-grafrecht.md). [Gemeentewet](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [VNG Retributies](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-retributies.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, standaard. [Gemeentewet](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [VNG Retributies](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-retributies.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, standaard. [Gemeentewet](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [VNG Retributies](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-retributies.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |

### Specialisaties

- **Lijkbezorgingsrechten**: Retributies voor het gebruik van de gemeentelijke begraafplaats of het crematorium (VNG retributies). Geen eigen pagina.
- **Retributie**: Heffing voor het gebruik van gemeentebezittingen of het genot van gemeentelijke diensten (Gemeentewet art. 229; VNG retributies). Geen eigen pagina.
- **Grafrechten**: De lijkbezorgingsrechten voor de uitgifte van een graf, in de UPL een eigen product (UPL nr. 164; Gemeentewet art. 229). Geen eigen pagina.
- **Leges reisdocumenten**: Rechten voor de aanvraag van een reisdocument, gemeentelijke belasting (Paspoortwet art. 7, 33; voor de identiteitskaart Wet op de Nederlandse identiteitskaart art. 9). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Heffing | voor het gebruik van (lijkbezorgingsrechten) *associatie (gericht)* | [Begraafplaats](../../7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/begraafplaats.md) | [VNG Retributies](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-retributies.md) (§ Lijkbezorgingsrechten) |
| Heffing | voor het gebruik van (lijkbezorgingsrechten) *associatie (gericht)* | [Crematorium](../../7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/crematorium.md) | [VNG Retributies](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-retributies.md) (§ Lijkbezorgingsrechten) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Gemeentewet](../../../../motivatie/beleidskaders/rijksregelgeving/gemeentewet.md) | is grondslag voor *associatie (gericht)* | Heffing | [Gemeentewet](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) (art. 229 lid 1, 229b lid 1) |
| [Heffingsverordening](heffingsverordening.md) | regelt *associatie (gericht)* | Heffing | [Gemeentewet](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [VNG Retributies](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-retributies.md) (Gemeentewet art. 216, 229; § Lijkbezorgingsrechten) |
| [Verlenen grafrecht](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlenen-grafrecht.md) | leidt tot (lijkbezorgingsrechten) *toegang (registreren)* | Heffing | [Gemeentewet](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [VNG Retributies](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-retributies.md) (Gemeentewet art. 229 lid 1 onder a, b; VNG § Lijkbezorgingsrechten) |

### Data-objecten

- [Heffing-data](../../../../applicatiearchitectuur/data-objecten/heffing-data.md) *realisatie*: GGM-entiteit *Heffing*, match exact.

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Gemeentewet](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) | Gemeentewet (BWBR0005416) - geldend per 2024-01-31 |
| [VNG Retributies](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-retributies.md) | Retributies |
| [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) | Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023 |

### Afstemming met GGM

Match **exact** met GGM-entiteit *Heffing* (beleidsdomein RGBZPlus, taakveld 99 Kern). Zelfde begrip en definitie.

> Een door de overheid opgelegde verplichting tot betaling

### Afstemming met GEMMA

Match **exact** met GEMMA-element *Heffing* (business-object). Zelfde begrip.

> Een door de overheid opgelegde verplichting tot betaling
