---
id: inlevering-van-het-reisdocument
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Inlevering van het reisdocument
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het moment waarop een reisdocument bij een tot inhouding bevoegde autoriteit komt, doordat de houder het inlevert of het aan de balie wordt ingenomen.
match:
  gemma: geen
synoniemen:
- Inleveren (wet)
bronnen:
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-rvig-hup-inhouding-inlevering-vermissing
---

# Inlevering van het reisdocument

<!-- Gegenereerd door tools/render.py uit de beoordeling inlevering-van-het-reisdocument.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het moment waarop een reisdocument bij een tot inhouding bevoegde autoriteit komt, doordat de houder het inlevert of het aan de balie wordt ingenomen.

### Beschrijving

De houder levert zijn oude Nederlandse reisdocumenten in bij de uitreiking van een nieuw document (Paspoortwet art. 32), en een vervallen of teruggevonden vermist document zo spoedig mogelijk bij een tot inhouding bevoegde autoriteit, of op haar verzoek (art. 56; HUP Inhouding). Een document wordt ook ingenomen als het aan de balie beschadigd, onbevoegd gewijzigd of foutief blijkt (art. 54 lid 1).

Inlevering gebeurt op initiatief van de houder, inhouding door een bevoegde autoriteit; een teruggevonden vermist document wordt niet meer teruggegeven (HUP Inhouding). De gemeente registreert de inlevering in de basisregistratie personen.

### Synoniemen

| Synoniem | Context |
|---|---|
| Inleveren | wet |

### Naamkeuze

Voltooide verandering in de vorm van Vermissing van het reisdocument, met de wetsterm inleveren (Paspoortwet art. 56). Was een processtap zonder pagina: Processtap zonder pagina: de houder levert zijn oude Nederlandse reisdocumenten in bij de uitreiking (Paspoortwet art. 32) en een vervallen of teruggevonden document bij een tot inhouding bevoegde autoriteit (art. 56; HUP Inhouding). Vermeld bij Uitreiken reisdocument en Inhouden reisdocument; de gemeente registreert de inlevering in de BRP.

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (2 toetskenmerken ja).

### Plaats in de indelingen

- **Start**: [Inhouden reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inhouden-reisdocument.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Inhouden reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inhouden-reisdocument.md). [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **komt herhaald voor**: Gebeurt het regelmatig en voor verschillende gevallen, en is het geen eenmalig voorval? | Ja, standaard. [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Inlevering van het reisdocument | leidt tot *triggering* | [Inhouden reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inhouden-reisdocument.md) | [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Inhouding, inlevering of vermissing](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-inhouding-inlevering-vermissing.md) (Paspoortwet art. 54, 56; HUP Inhouding) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren reisdocumenten](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-reisdocumenten.md) | omvat *aggregatie* | Inlevering van het reisdocument | [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (art. 56) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [HUP Inhouding, inlevering of vermissing](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-inhouding-inlevering-vermissing.md) | HUP BRP: Inhouding inlevering vermissing |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
