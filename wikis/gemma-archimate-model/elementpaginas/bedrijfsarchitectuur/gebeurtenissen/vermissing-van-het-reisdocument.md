---
id: vermissing-van-het-reisdocument
type: gebeurtenis
archimate_type: business-event
status: review
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

**Status: review.** Wacht op het akkoord van de redacteur.

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

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (2 toetskenmerken ja).

### Plaats in de indelingen

- **Start**: [Verwerken vermissing reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-reisdocument.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Vermissing paspoort of ID-kaart](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md), [HUP Inhouding, inlevering of vermissing](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-inhouding-inlevering-vermissing.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Verwerken vermissing reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-reisdocument.md). [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Vermissing paspoort of ID-kaart](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md), [HUP Inhouding, inlevering of vermissing](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-inhouding-inlevering-vermissing.md) |
| **komt herhaald voor**: Gebeurt het regelmatig en voor verschillende gevallen, en is het geen eenmalig voorval? | Ja, standaard. [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Vermissing paspoort of ID-kaart](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md), [HUP Inhouding, inlevering of vermissing](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-inhouding-inlevering-vermissing.md) |

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
