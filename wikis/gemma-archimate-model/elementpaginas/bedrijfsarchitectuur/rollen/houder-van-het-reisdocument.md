---
id: houder-van-het-reisdocument
type: rol
archimate_type: business-role
status: goedgekeurd
naam: Houder van het reisdocument
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Hoedanigheid van degene op wiens naam een reisdocument is of wordt gesteld en die het aanvraagt, ophaalt, vermissing meldt en inlevert.
match:
  gemma: geen
doelgroep: inwoners en ondernemers
synoniemen:
- Aanvrager (wet)
- Houder (wet)
bronnen:
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-rvig-hup-inhouding-inlevering-vermissing
- 2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen
- 2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven
- 2026-rijk-paspoortbesluit-bwbr0044308
---

# Houder van het reisdocument

<!-- Gegenereerd door tools/render.py uit de beoordeling houder-van-het-reisdocument.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Hoedanigheid van degene op wiens naam een reisdocument is of wordt gesteld en die het aanvraagt, ophaalt, vermissing meldt en inlevert.

### Beschrijving

De wet onderscheidt de aanvrager, die een aanvraag indient of op wie zij betrekking heeft, en de houder, op wiens naam het reisdocument is gesteld en voor wie het is uitgereikt (Paspoortwet art. 1 onder b en f). In de gemeentelijke praktijk is het dezelfde persoon in opeenvolgende fasen: hij verschijnt persoonlijk bij de aanvraag, legt al zijn reisdocumenten over, haalt het nieuwe document op en levert de oude in, meldt een vermissing en levert een vervallen of teruggevonden document in (art. 28, 29, 32, 56; Utrecht). Voor een minderjarige vraagt de ouder of voogd aan en geeft de toestemming (art. 34).

### Synoniemen

| Synoniem | Context |
|---|---|
| Aanvrager | wet |
| Houder | wet |

### Naamkeuze

Naar het precedent Rechthebbende op het graf: de rol heet naar het object, zodat de naam ondubbelzinnig is. Houder en aanvrager uit de wet zijn één hoedanigheid in opeenvolgende fasen en staan als synoniemen.

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (1 toetskenmerken ja).

### Plaats in de indelingen

- **Doelgroep**: inwoners en ondernemers.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: hoedanigheid.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Inhouding, inlevering of vermissing](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-inhouding-inlevering-vermissing.md) |
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Behandelen aanvraag reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument.md), [Verwerken vermissing reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-reisdocument.md), [Inhouden reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inhouden-reisdocument.md), [Behandelen aanvraag reisdocument niet-ingezetene](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument-niet-ingezetene.md). [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Inhouding, inlevering of vermissing](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-inhouding-inlevering-vermissing.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Houder van het reisdocument | vraagt aan, haalt op en levert oude documenten in *toewijzing* | [Behandelen aanvraag reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument.md) | [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Paspoort of identiteitskaart aanvragen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) (art. 1 onder b, 28, 29; art. 32, 42) |
| Houder van het reisdocument | meldt vermissing *toewijzing* | [Verwerken vermissing reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-reisdocument.md) | [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Vermissing paspoort of ID-kaart](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) (art. 5a; Utrecht regel 33-37) |
| Houder van het reisdocument | levert in *toewijzing* | [Inhouden reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inhouden-reisdocument.md) | [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Inhouding, inlevering of vermissing](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-inhouding-inlevering-vermissing.md) (art. 56; HUP Inhouding) |
| Houder van het reisdocument | is houder van *toegang (houder)* | [Reisdocument](../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/reisdocument.md) | [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (art. 1 onder f) |
| Houder van het reisdocument | vraagt aan *toewijzing* | [Behandelen aanvraag reisdocument niet-ingezetene](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument-niet-ingezetene.md) | [Paspoortbesluit](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) (art. 3.2) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [HUP Inhouding, inlevering of vermissing](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-inhouding-inlevering-vermissing.md) | HUP BRP: Inhouding inlevering vermissing |
| [Utrecht Paspoort of identiteitskaart aanvragen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) | Gemeente Utrecht: Paspoort of ID-kaart aanvragen |
| [Utrecht Vermissing paspoort of ID-kaart](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) | Gemeente Utrecht: Paspoort of ID-kaart kwijt |
| [Paspoortbesluit](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) | Paspoortbesluit |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen rol voor dit begrip; nieuw voor GEMMA.
