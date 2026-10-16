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
match:
  gemma: geen
synoniemen:
- Vermissing (wet)
- Diefstal (beleid)
bronnen:
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven
- 2026-rvig-hup-inhouding-inlevering-vermissing
---

# Vermissing van het reisdocument

<!-- Gegenereerd door tools/render.py uit de beoordeling vermissing-van-het-reisdocument.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het moment waarop de houder niet meer over zijn reisdocument beschikt, doordat het kwijt of gestolen is.

> ieder geval waarin de houder niet meer de feitelijke beschikking heeft over een op zijn naam gesteld reisdocument, anders dan door of ten behoeve van handelingen van een daartoe bevoegde autoriteit
>
> — [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), art. 1 onder k

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

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk reisdocument dat kwijtraakt of wordt gestolen. [Utrecht Vermissing paspoort of ID-kaart](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Verwerken vermissing reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-reisdocument.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Vermissing van het reisdocument | leidt tot *triggering* | [Verwerken vermissing reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-reisdocument.md) | [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Vermissing paspoort of ID-kaart](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) (Paspoortwet art. 5a; Utrecht regel 17-23) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren reisdocumenten](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-reisdocumenten.md) | omvat *aggregatie* | Vermissing van het reisdocument | [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (art. 1 onder k) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [Utrecht Vermissing paspoort of ID-kaart](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) | Gemeente Utrecht: Paspoort of ID-kaart kwijt |
| [HUP Inhouding, inlevering of vermissing](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-inhouding-inlevering-vermissing.md) | HUP BRP: Inhouding inlevering vermissing |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
