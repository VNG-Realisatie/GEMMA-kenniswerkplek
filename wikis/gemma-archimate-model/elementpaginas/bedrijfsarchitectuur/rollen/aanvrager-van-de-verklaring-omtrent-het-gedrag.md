---
id: aanvrager-van-de-verklaring-omtrent-het-gedrag
type: rol
archimate_type: business-role
status: review
naam: Aanvrager van de verklaring omtrent het gedrag
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Hoedanigheid van degene omtrent wiens gedrag een verklaring omtrent het gedrag wordt gevraagd en die de aanvraag indient.
match:
  gemma: geen
doelgroep: inwoners en ondernemers
synoniemen:
- Aanvrager VOG (beleid)
- Aanvrager verklaring omtrent het gedrag (wet)
bronnen:
- 2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194
- 2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog
---

# Aanvrager van de verklaring omtrent het gedrag

<!-- Gegenereerd door tools/render.py uit de beoordeling aanvrager-van-de-verklaring-omtrent-het-gedrag.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Hoedanigheid van degene omtrent wiens gedrag een verklaring omtrent het gedrag wordt gevraagd en die de aanvraag indient.

### Beschrijving

De wet kent de aanvrager, degene omtrent wiens gedrag de verklaring wordt gevraagd, of een vertegenwoordiger van de rechtspersoon (Wet justitiële en strafvorderlijke gegevens art. 33). De aanvraag bevat de voornamen, de geboortedatum en het doel, en de aanvrager of degene te wiens behoeve de verklaring wordt gevraagd, geeft het risico voor de samenleving op (art. 32). In de praktijk heeft vaak een werkgever of een andere organisatie het aanvraagformulier ingevuld; de aanvrager zelf dient in en betaalt (Utrecht).

### Synoniemen

| Synoniem | Context |
|---|---|
| Aanvrager VOG | beleid |
| Aanvrager verklaring omtrent het gedrag | wet |

### Naamkeuze

Naar het precedent Houder van het reisdocument: de rol heet naar het object, zodat de naam ondubbelzinnig is; de korte term Aanvrager is al synoniem van Houder van het reisdocument. De wet noemt ook de vertegenwoordiger van een rechtspersoon, maar de gemeente behandelt alleen de aanvraag van een natuurlijk persoon.

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (kern ja).

### Plaats in de indelingen

- **Doelgroep**: inwoners en ondernemers.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: hoedanigheid. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Behandelen aanvraag verklaring omtrent het gedrag](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-verklaring-omtrent-het-gedrag.md). |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, per aanvraag één aanvrager (Wet justitiële en strafvorderlijke gegevens art. 33). [Wet justitiële en strafvorderlijke gegevens](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Aanvrager van de verklaring omtrent het gedrag | dient de aanvraag in *toewijzing* | [Behandelen aanvraag verklaring omtrent het gedrag](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-verklaring-omtrent-het-gedrag.md) | [Wet justitiële en strafvorderlijke gegevens](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md), [Utrecht VOG aanvragen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog.md) (art. 30, 33; Utrecht regel 37-53) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet justitiële en strafvorderlijke gegevens](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) | Wet justitiële en strafvorderlijke gegevens |
| [Utrecht VOG aanvragen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog.md) | Gemeente Utrecht: Verklaring omtrent het gedrag (VOG) aanvragen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen rol voor dit begrip; nieuw voor GEMMA.
