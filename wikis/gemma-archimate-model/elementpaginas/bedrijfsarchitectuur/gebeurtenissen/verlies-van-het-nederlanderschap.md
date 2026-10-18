---
id: verlies-van-het-nederlanderschap
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Verlies van het Nederlanderschap
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het moment waarop een persoon het Nederlanderschap verliest, door afstand, een andere nationaliteit, verblijf in het buitenland of intrekking.
match:
  gemma: geen
synoniemen:
- Verlies Nederlanderschap (informatiemodel)
bronnen:
- 2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738
- 2026-utrecht-burgerzaken-nederlandse-nationaliteit-opgeven-of-verliezen
- 2026-rvig-hup-nederlandse-nationaliteit
- 2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605
- 2026-rvig-hup-nationaliteit
- 2026-rijk-paspoortwet-bwbr0005212
---

# Verlies van het Nederlanderschap

<!-- Gegenereerd door tools/render.py uit de beoordeling verlies-van-het-nederlanderschap.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het moment waarop een persoon het Nederlanderschap verliest, door afstand, een andere nationaliteit, verblijf in het buitenland of intrekking.

### Beschrijving

Het Nederlanderschap gaat voor een meerderjarige verloren door het vrijwillig verkrijgen van een andere nationaliteit, door een verklaring van afstand, door dertien jaar hoofdverblijf buiten het Koninkrijk en de EU met ook een vreemde nationaliteit, of door intrekking door de minister; een minderjarige verliest het onder meer met zijn ouder (Rijkswet op het Nederlanderschap art. 14-16). Utrecht onderscheidt het opgeven, door een verklaring van afstand, van het verliezen zonder bewuste keuze.

In de basisregistratie personen wordt de Nederlandse nationaliteit beëindigd en worden vreemde of onbekende nationaliteiten weer opgenomen; een Nederlands reisdocument vervalt van rechtswege en de burgemeester bevordert dat het wordt ingenomen (HUP Nederlandse nationaliteit; Paspoortwet art. 47 lid 1 onder a; Besluit verkrijging en verlies Nederlanderschap art. 64 lid 3).

### Synoniemen

| Synoniem | Context |
|---|---|
| Verlies Nederlanderschap | informatiemodel |

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (2 toetskenmerken ja).

### Plaats in de indelingen

- **Start**: [Bijhouden persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md), [Verval van het reisdocument](verval-van-het-reisdocument.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Rijkswet op het Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md), [Utrecht nationaliteit opgeven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlandse-nationaliteit-opgeven-of-verliezen.md), [HUP Nederlandse nationaliteit](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nederlandse-nationaliteit.md), [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [HUP Nationaliteit](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nationaliteit.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Bijhouden persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md). [Rijkswet op het Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md), [Utrecht nationaliteit opgeven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlandse-nationaliteit-opgeven-of-verliezen.md), [HUP Nederlandse nationaliteit](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nederlandse-nationaliteit.md), [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [HUP Nationaliteit](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nationaliteit.md) |
| **komt herhaald voor**: Gebeurt het regelmatig en voor verschillende gevallen, en is het geen eenmalig voorval? | Ja, standaard. [Rijkswet op het Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md), [Utrecht nationaliteit opgeven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlandse-nationaliteit-opgeven-of-verliezen.md), [HUP Nederlandse nationaliteit](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nederlandse-nationaliteit.md), [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [HUP Nationaliteit](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nationaliteit.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verlies van het Nederlanderschap | leidt tot beëindiging van de Nederlandse nationaliteit *triggering* | [Bijhouden persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md) | [HUP Nederlandse nationaliteit](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nederlandse-nationaliteit.md) (HUP Nederlandse nationaliteit, kop Verlies) |
| Verlies van het Nederlanderschap | doet een Nederlands reisdocument vervallen *triggering* | [Verval van het reisdocument](verval-van-het-reisdocument.md) | [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Nationaliteit](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nationaliteit.md) (Paspoortwet art. 47 lid 1 onder a; HUP Nationaliteit) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen verklaring van afstand](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verklaring-van-afstand.md) | leidt tot *triggering* | Verlies van het Nederlanderschap | [Rijkswet op het Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) (art. 15 lid 1 onder b) |
| [Beheren Nederlanderschap](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-nederlanderschap.md) | omvat *aggregatie* | Verlies van het Nederlanderschap | [Rijkswet op het Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) (art. 15) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Rijkswet op het Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) | Rijkswet op het Nederlanderschap |
| [Utrecht nationaliteit opgeven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlandse-nationaliteit-opgeven-of-verliezen.md) | Gemeente Utrecht: Nederlandse nationaliteit opgeven of verliezen |
| [HUP Nederlandse nationaliteit](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nederlandse-nationaliteit.md) | HUP BRP: Nederlandse nationaliteit |
| [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) | Besluit verkrijging en verlies Nederlanderschap |
| [HUP Nationaliteit](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nationaliteit.md) | HUP BRP: Nationaliteit |
| [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
