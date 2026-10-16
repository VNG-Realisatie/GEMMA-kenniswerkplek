---
id: ggd
type: actor
archimate_type: business-actor
status: review
naam: GGD
onderwerpen:
- lijkbezorging
definitie: Gezondheidsdienst die de colleges van de gemeenten in een regio via een gemeenschappelijke regeling instellen en in stand houden voor de publieke gezondheid.
match:
  gemma: geen
doelgroep: ketenpartners
synoniemen:
- Gemeentelijke gezondheidsdienst (wet)
bronnen:
- 2026-rijk-wet-publieke-gezondheid-wettekst
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
---

# GGD

<!-- Gegenereerd door tools/render.py uit de beoordeling ggd.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Gezondheidsdienst die de colleges van de gemeenten in een regio via een gemeenschappelijke regeling instellen en in stand houden voor de publieke gezondheid.

### Beschrijving

De colleges van burgemeester en wethouders van de gemeenten in een regio stellen de gemeentelijke gezondheidsdienst via een gemeenschappelijke regeling in en houden haar in stand (Wet publieke gezondheid art. 14 lid 1); de regeling stelt een openbaar lichaam in, zodat de GGD eigen rechtspersoonlijkheid heeft (art. 14 lid 2). De gemeenten zijn zo mede-eigenaar en opdrachtgever. De GGD staat onder leiding van een directeur publieke gezondheid (art. 14 lid 3).

### Per onderwerp

#### [Lijkbezorging](../../../onderwerpen/lijkbezorging/begrippen.md)

Een arts meldt een besmet stoffelijk overschot aan de GGD, die de melding doorgeeft aan de burgemeester (Wet publieke gezondheid art. 21 lid 2, 27 lid 3). De GGD adviseert de burgemeester over maatregelen om het gevaar af te wenden (Wet op de lijkbezorging art. 22a).

### Synoniemen

| Synoniem | Context |
|---|---|
| Gemeentelijke gezondheidsdienst | wet |

## Plaats in het model

### Typering

Actor. Uitkomst van de beslistabel: Samenwerkingsverband met eigen rechtspersoon (kern ja).

### Plaats in de indelingen

- **Doelgroep**: ketenpartners.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: samenwerkingsverband. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **los van verantwoordelijkheid**: Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen? | Ja, bestaat los van de adviestaak bij een besmet lijk. [Wet publieke gezondheid](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-publieke-gezondheid-wettekst.md) |
| **eigen rechtspersoon**: Heeft het verband of de organisatie eigen rechtspersoonlijkheid (openbaar lichaam, stichting, vennootschap)? | Ja, openbaar lichaam, ingesteld bij gemeenschappelijke regeling (art. 14 lid 2). [Wet publieke gezondheid](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-publieke-gezondheid-wettekst.md) |
| **vervult een rol**: Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? | Ja, met [Adviseur](../rollen/adviseur.md). |
| **soort partij**: Heeft elke gemeente met deze partij te maken in dezelfde rol, zodat het element voor alle gemeenten geldt? Het criterium sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat. | Ja, elke gemeente is via een gemeenschappelijke regeling aangesloten bij een GGD (Wpg art. 14); een soort partij, geen individuele GGD. [Wet publieke gezondheid](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-publieke-gezondheid-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| GGD | vervult *toewijzing* | [Adviseur](../rollen/adviseur.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Wet publieke gezondheid](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-publieke-gezondheid-wettekst.md) (Wlb art. 22a; Wpg art. 16) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet publieke gezondheid](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-publieke-gezondheid-wettekst.md) | Wet publieke gezondheid (BWBR0024705) |
| [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.

### Besluiten redacteur

- 2026-10-15: Hoofdkenmerk samenwerkingsverband: de GGD is altijd een samenwerkingsverband van gemeenten, met eigen rechtspersoon (Actor); in sommige processen treedt zij op als handelende partij, via de rol die zij vervult (Adviseur). Los van verantwoordelijkheid mag daarom ook bij een samenwerkingsverband. *Zekerheid: kennis.*
