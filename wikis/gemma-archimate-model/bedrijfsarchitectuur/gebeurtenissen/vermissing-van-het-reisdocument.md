---
id: vermissing-van-het-reisdocument
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Vermissing van het reisdocument
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het moment waarop de houder niet meer over zijn reisdocument beschikt, doordat het kwijt of gestolen is.
grondslag: bron
match:
  gemma: geen
data_object: nee
synoniemen:
- Vermissing (wet)
- Diefstal (beleid)
bronnen:
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven
- 2026-rvig-hup-inhouding-inlevering-vermissing
---

# Vermissing van het reisdocument

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/vermissing-van-het-reisdocument.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het moment waarop de houder niet meer over zijn reisdocument beschikt, doordat het kwijt of gestolen is.

> ieder geval waarin de houder niet meer de feitelijke beschikking heeft over een op zijn naam gesteld reisdocument, anders dan door of ten behoeve van handelingen van een daartoe bevoegde autoriteit
>
> — [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), art. 1 onder k

### Beschrijving

Diefstal is een vorm van vermissing. Wie een reisdocument van een ander vindt, zorgt dat het bij een tot inhouding bevoegde autoriteit komt (Paspoortwet art. 5). Een ingenomen document is geen vermissing: wie een nieuw document aanvraagt, legt dan een verklaring van de innemende autoriteit over (art. 31 lid 2). Het formele begrip sluit de inname door een bevoegde autoriteit uit; de herkenbare definitie noemt alleen kwijt of gestolen, wat op hetzelfde neerkomt.

### Synoniemen

| Synoniem | Context |
|---|---|
| Vermissing | wet |
| Diefstal | beleid |

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (kern ja, 1/1).

### Plaats in de indelingen

- **Start**: [Verwerken vermissing reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-reisdocument.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 51 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, wetsbegrip vermissing (Paspoortwet art. 1 onder k); gangbaar: paspoort of identiteitskaart kwijt of gestolen (Utrecht). [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Vermissing paspoort of ID-kaart](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de houder meldt de vermissing bij de gemeente, die haar registreert (Utrecht; HUP Inhouding). [Utrecht Vermissing paspoort of ID-kaart](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md), [HUP Inhouding, inlevering of vermissing](../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Vermissing paspoort of ID-kaart](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort bij burgerzaken: de toestand van het reisdocument verandert (regel Thuishoren). [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gebeurt. [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **toestandsverandering**: Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | Ja, het moment waarop de houder niet meer over zijn reisdocument beschikt, anders dan door een bevoegde autoriteit (Paspoortwet art. 1 onder k). [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk reisdocument dat kwijtraakt of wordt gestolen. [Utrecht Vermissing paspoort of ID-kaart](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, start Verwerken vermissing reisdocument: de houder meldt de vermissing zo snel mogelijk (Paspoortwet art. 5a; Utrecht). [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Vermissing paspoort of ID-kaart](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip van hetzelfde type in deze wiki. [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Vermissing van het reisdocument | leidt tot *triggering* | [Verwerken vermissing reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-reisdocument.md) | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Vermissing paspoort of ID-kaart](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) (Paspoortwet art. 5a; Utrecht regel 17-23) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren reisdocumenten](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-reisdocumenten.md) | omvat *aggregatie* | Vermissing van het reisdocument | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) (art. 1 onder k) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [Utrecht Vermissing paspoort of ID-kaart](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) | Gemeente Utrecht: Paspoort of ID-kaart kwijt |
| [HUP Inhouding, inlevering of vermissing](../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md) | HUP BRP: Inhouding inlevering vermissing |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
