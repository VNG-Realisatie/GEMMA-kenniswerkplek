---
id: houder-van-het-rijbewijs
type: rol
archimate_type: business-role
status: goedgekeurd
naam: Houder van het rijbewijs
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Hoedanigheid van degene aan wie een rijbewijs is of wordt afgegeven en die het aanvraagt, ophaalt, vermissing meldt en inlevert.
match:
  gemma: geen
doelgroep: inwoners en ondernemers
synoniemen:
- Aanvrager rijbewijs (wet)
- Rijbewijshouder (beleid)
bronnen:
- 2026-rijk-wegenverkeerswet-1994-bwbr0006622
- 2026-rijk-reglement-rijbewijzen-bwbr0008074
- 2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen
- 2026-utrecht-burgerzaken-rijbewijs-buitenland-omwisselen
---

# Houder van het rijbewijs

<!-- Gegenereerd door tools/render.py uit de beoordeling houder-van-het-rijbewijs.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Hoedanigheid van degene aan wie een rijbewijs is of wordt afgegeven en die het aanvraagt, ophaalt, vermissing meldt en inlevert.

### Beschrijving

Het Reglement rijbewijzen spreekt van de aanvrager, de Wegenverkeerswet 1994 van de houder van een rijbewijs. In de gemeentelijke praktijk is het dezelfde persoon in opeenvolgende fasen: hij vraagt aan met een identiteitsbewijs en een pasfoto, haalt het nieuwe rijbewijs persoonlijk op, levert het oude in, geeft een vermissing door en levert een teruggevonden rijbewijs in (Reglement rijbewijzen art. 27, 33; Wegenverkeerswet 1994 art. 111 lid 2, 119 lid 2 en 4; Utrecht).

### Synoniemen

| Synoniem | Context |
|---|---|
| Aanvrager rijbewijs | wet |
| Rijbewijshouder | beleid |

### Naamkeuze

Naar het precedent Houder van het reisdocument: de rol heet naar het object, zodat de naam ondubbelzinnig is. Aanvrager en houder uit de wet zijn één hoedanigheid in opeenvolgende fasen; Aanvrager rijbewijs staat als synoniem, de korte termen Aanvrager en Houder zijn al synoniem van Houder van het reisdocument.

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
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Behandelen aanvraag rijbewijs](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-rijbewijs.md), [Behandelen aanvraag omwisseling buitenlands rijbewijs](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-omwisseling-buitenlands-rijbewijs.md), [Verwerken vermissing rijbewijs](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-rijbewijs.md). |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, per rijbewijs één houder (Wegenverkeerswet 1994 art. 118a, 119). [Wegenverkeerswet 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Houder van het rijbewijs | vraagt aan, haalt op en levert het eerdere rijbewijs in *toewijzing* | [Behandelen aanvraag rijbewijs](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-rijbewijs.md) | [Reglement rijbewijzen](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md), [Wegenverkeerswet 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) (art. 27, 33; Utrecht regel 17, 35; WVW art. 119 lid 2; Utrecht regel 29, 63-67) |
| Houder van het rijbewijs | vraagt aan en levert het buitenlandse rijbewijs in *toewijzing* | [Behandelen aanvraag omwisseling buitenlands rijbewijs](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-omwisseling-buitenlands-rijbewijs.md) | [Reglement rijbewijzen](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md), [Utrecht Rijbewijs buitenland omwisselen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-buitenland-omwisselen.md) (art. 27, 109; Utrecht regel 55) |
| Houder van het rijbewijs | geeft vermissing door *toewijzing* | [Verwerken vermissing rijbewijs](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-rijbewijs.md) | [Utrecht Rijbewijs aanvragen of verlengen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) (Utrecht regel 126-140) |
| Houder van het rijbewijs | is houder van *toegang (houder)* | [Rijbewijs](../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/rijbewijs.md) | [Wegenverkeerswet 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) (art. 119 lid 4) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wegenverkeerswet 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) | Wegenverkeerswet 1994 |
| [Reglement rijbewijzen](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) | Reglement rijbewijzen |
| [Utrecht Rijbewijs aanvragen of verlengen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) | Gemeente Utrecht: Rijbewijs aanvragen of verlengen |
| [Utrecht Rijbewijs buitenland omwisselen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-buitenland-omwisselen.md) | Gemeente Utrecht: Rijbewijs buitenland omwisselen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen rol voor dit begrip; nieuw voor GEMMA.
