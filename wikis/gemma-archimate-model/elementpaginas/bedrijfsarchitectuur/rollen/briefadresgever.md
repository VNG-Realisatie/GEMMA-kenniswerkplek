---
id: briefadresgever
type: rol
archimate_type: business-role
status: review
naam: Briefadresgever
onderwerpen:
- burgerzaken
definitie: Verantwoordelijkheid van een persoon of aangewezen rechtspersoon om post voor de houder van een briefadres in ontvangst te nemen en door te geven.
match:
  gemma: geen
doelgroep: inwoners en ondernemers
bronnen:
- 2026-rvig-hup-verblijfplaats
- 2026-rijk-wet-brp-bwbr0033715
---

# Briefadresgever

<!-- Gegenereerd door tools/render.py uit de beoordeling briefadresgever.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Verantwoordelijkheid van een persoon of aangewezen rechtspersoon om post voor de houder van een briefadres in ontvangst te nemen en door te geven.

### Beschrijving

De briefadresgever is een natuurlijk persoon of een door het college aangewezen rechtspersoon; hij stemt schriftelijk in, zorgt dat geschriften voor de houder worden doorgegeven en verstrekt het college inlichtingen (HUP Verblijfplaats). Zonder briefadresgever registreert de gemeente een adres van de gemeente zelf (HUP Verblijfplaats).

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (1 toetskenmerken ja).

### Plaats in de indelingen

- **Doelgroep**: inwoners en ondernemers.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: hoedanigheid.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [HUP Verblijfplaats](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) |
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Inschrijven op briefadres](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-op-briefadres.md). [HUP Verblijfplaats](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Briefadresgever | stemt in met *toewijzing* | [Inschrijven op briefadres](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-op-briefadres.md) | [HUP Verblijfplaats](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (Briefadres; Wet BRP art. 2.23 lid 3, 2.45 lid 2) |
| Briefadresgever | geeft post door *toegang (beheerder)* | [Briefadres](../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/briefadres.md) | [HUP Verblijfplaats](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (Briefadres; Wet BRP art. 2.45 lid 3) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Wet basisregistratie personen](../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Briefadresgever | [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 1.1, 2.42, 2.45) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP Verblijfplaats](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) | HUP BRP: Verblijfplaats |
| [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen rol voor dit begrip; nieuw voor GEMMA.
