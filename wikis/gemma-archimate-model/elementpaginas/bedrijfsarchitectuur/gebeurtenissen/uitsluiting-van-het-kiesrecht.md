---
id: uitsluiting-van-het-kiesrecht
type: gebeurtenis
archimate_type: business-event
status: review
naam: Uitsluiting van het kiesrecht
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het moment waarop een persoon bij onherroepelijke rechterlijke uitspraak van het kiesrecht is uitgesloten.
match:
  gemma: geen
synoniemen:
- Ontzetting uit het kiesrecht (wet)
bronnen:
- 2026-rijk-kieswet-bwbr0004627
- 2026-rvig-hup-nederlands-kiesrecht
---

# Uitsluiting van het kiesrecht

<!-- Gegenereerd door tools/render.py uit de beoordeling uitsluiting-van-het-kiesrecht.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het moment waarop een persoon bij onherroepelijke rechterlijke uitspraak van het kiesrecht is uitgesloten.

### Beschrijving

Een uitsluiting van het kiesrecht volgt altijd uit een onherroepelijke rechterlijke uitspraak, geldt voor bepaalde of onbepaalde tijd en voor alle verkiezingen, en kan Nederlanders en vreemdelingen treffen; ze wordt beoordeeld naar de toestand op de dag van de kandidaatstelling (Kieswet art. B 5 lid 1; HUP Nederlands kiesrecht). De minister van Justitie en Veiligheid doet mededeling aan de burgemeester van de woongemeente, die de persoon in kennis stelt (art. B 5 lid 2-3). Ook de lidstaat van nationaliteit kan een EU-onderdaan van het Europees kiesrecht uitsluiten (HUP Europees kiesrecht). De uitsluiting eindigt na een nieuwe mededeling of op de einddatum (HUP Nederlands kiesrecht).

### Synoniemen

| Synoniem | Context |
|---|---|
| Ontzetting uit het kiesrecht | wet |

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (kern ja, 1/1).

### Plaats in de indelingen

- **Start**: [Registreren kiesgerechtigdheid](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/registreren-kiesgerechtigdheid.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke uitspraak tot ontzetting. [HUP Nederlands kiesrecht](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nederlands-kiesrecht.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Registreren kiesgerechtigdheid](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/registreren-kiesgerechtigdheid.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Uitsluiting van het kiesrecht | leidt tot *triggering* | [Registreren kiesgerechtigdheid](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/registreren-kiesgerechtigdheid.md) | [Kieswet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [HUP Nederlands kiesrecht](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nederlands-kiesrecht.md) (Kieswet art. B 5 lid 3; HUP Nederlands kiesrecht) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Uitsluiting van het kiesrecht | [HUP Nederlands kiesrecht](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nederlands-kiesrecht.md) (HUP Nederlands kiesrecht) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Kieswet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) | Kieswet |
| [HUP Nederlands kiesrecht](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nederlands-kiesrecht.md) | HUP BRP: Nederlands kiesrecht |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
