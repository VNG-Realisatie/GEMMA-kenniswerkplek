---
id: crematorium
type: bedrijfsobject
archimate_type: business-object
status: goedgekeurd
naam: Crematorium
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Inrichting waar stoffelijke overschotten worden gecremeerd en de as wordt geborgen.
grondslag: bron
match:
  ggm: geen
  gemma: geen
data_object: nee
objectniveau: kernobject
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
---

# Crematorium

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/crematorium.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Inrichting waar stoffelijke overschotten worden gecremeerd en de as wordt geborgen.

### Beschrijving

Crematoria zijn gemeentelijk of bijzonder (art. 51). Een bijzonder crematorium wordt gevestigd door een kerkgenootschap, rechtspersoon of natuurlijk persoon, met een vergunning van burgemeester en wethouders (art. 52, 53). De houder bergt de as, zorgt voor de bestemming ervan en houdt een openbaar register (art. 50, 58, 59).

## Plaats in het model

### Typering

Bedrijfsobject, niveau kernobject. Uitkomst van de beslistabel: Passief (kern ja, 2/2).

### Plaats in de indelingen

- **Objectniveau**: kernobject.
- **Levensloop bepaald door**: [Beheren crematoria](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/beheren-crematoria.md).
- **Mutaties door bedrijfsprocessen**: [Verlenen vergunning bijzonder crematorium](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlenen-vergunning-bijzonder-crematorium.md).
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

Alleen de kenmerken met ja; de overige 52 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, kernbegrip (art. 49). [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de gemeente kan een gemeentelijk crematorium hebben en vergunt bijzondere crematoria (art. 51, 53). [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij dit onderwerp; geen ander onderwerp beoordeelt het. [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, elk crematorium apart, gemeentelijk of bijzonder (art. 51). [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, gevestigd, uitgebreid, gewijzigd, opgeheven (art. 50 lid 3, 53). [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, de gemeente vergunt vestiging, uitbreiding en wijziging van een bijzonder crematorium en besluit over een gemeentelijk crematorium (art. 53, 54). [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip in deze wiki. [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |

### Specialisaties

- **Gemeentelijk crematorium**: Crematorium van de gemeente; vestiging na openbare kennisgeving (art. 51, 54, 56). Geen eigen pagina.
- **Bijzonder crematorium**: Crematorium van een kerkgenootschap, rechtspersoon of natuurlijk persoon (art. 51, 52). Geen eigen pagina.

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren crematoria](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/beheren-crematoria.md) | beheert *toegang (bijwerken)* | Crematorium | [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 50, 51, 54) |
| [Heffing](../../0-bestuur-en-ondersteuning/belastingen/heffing.md) | voor het gebruik van (lijkbezorgingsrechten) *associatie (gericht)* | Crematorium | [VNG Retributies](../../../../bronanalyses/lijkbezorging/2026-vng-retributies.md) (§ Lijkbezorgingsrechten) |
| [Houder van het crematorium](../../../rollen/houder-van-het-crematorium.md) | houdt *toegang (houder)* | Crematorium | [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 50) |
| [Uitvoeren lijkbezorging](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvoeren-lijkbezorging.md) | geschiedt in *toegang (raadplegen)* | Crematorium | [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 49) |
| [Urn](urn.md) | wordt bijgezet in *associatie (gericht)* | Crematorium | [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 62 lid 1 a) |
| [Verlenen vergunning bijzonder crematorium](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlenen-vergunning-bijzonder-crematorium.md) | betreft *toegang (bijwerken)* | Crematorium | [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 53) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GGM

Geen GGM-entiteit. Het GGM kent geen entiteit voor dit begrip (tools/ggm.py kandidaten: geen naamgenoten of treffers).

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.

### Besluiten redacteur

- 2026-09-30: Kenmerk plaats is nee: beoordeeld als gemeentelijke voorziening, niet als fysieke plaats.
- 2026-10-05: Stoffelijk overschot in lopende tekst: lijken wordt stoffelijke overschotten in de definitie.
