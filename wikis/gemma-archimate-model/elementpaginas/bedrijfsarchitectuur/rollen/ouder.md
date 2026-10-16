---
id: ouder
type: rol
archimate_type: business-role
status: review
naam: Ouder
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Hoedanigheid van wie juridisch moeder of andere ouder van een kind is, door geboorte, huwelijk, erkenning, vaststelling of adoptie.
match:
  gemma: geen
doelgroep: inwoners en ondernemers
synoniemen:
- Moeder (wet)
- Vader (wet)
- Duomoeder (beleid)
- Erkenner (wet)
bronnen:
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-rvig-hup-geboorte
- 2026-utrecht-burgerzaken-geboorteaangifte-doen
- 2026-rijk-wet-brp-bwbr0033715
- 2026-utrecht-burgerzaken-kind-erkennen
- 2026-utrecht-burgerzaken-levenloos-geboren-kind-of-overleden-pasgeboren-kind-aangifte-doen
- 2026-utrecht-burgerzaken-achternaam-kind-kiezen
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen
- 2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven
---

# Ouder

<!-- Gegenereerd door tools/render.py uit de beoordeling ouder.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Hoedanigheid van wie juridisch moeder of andere ouder van een kind is, door geboorte, huwelijk, erkenning, vaststelling of adoptie.

### Beschrijving

Een kind heeft juridisch altijd een moeder, de vrouw uit wie het is geboren of de adoptiefmoeder, en hoogstens één andere ouder: de echtgenoot of partner van de moeder, de erkenner, de ouder van wie het ouderschap is vastgesteld of de adoptiefouder (BW 1 art. 198, 199; HUP Geboorte). In de gemeentelijke praktijk heet de vrouwelijke andere ouder duomoeder (Utrecht). De ouder doet aangifte van geboorte, erkent het kind, kiest samen met de andere ouder de achternaam en heeft gezag over een minderjarig kind (BW 1 art. 5, 19e, 203, 247).

Voor een reisdocument van een minderjarige geeft iedere ouder met gezag toestemming, online of op een formulier; een ouder meldt de vermissing van het reisdocument van een kind tot en met elf jaar (Paspoortwet art. 34; Utrecht).

### Synoniemen

| Synoniem | Context |
|---|---|
| Moeder | wet |
| Vader | wet |
| Duomoeder | beleid |
| Erkenner | wet |

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
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Opmaken geboorteakte](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-geboorteakte.md), [Opmaken akte van erkenning](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-erkenning.md), [Inschrijven levenloos geboren kind](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-levenloos-geboren-kind.md), [Opmaken akte van naamskeuze](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-naamskeuze.md), [Behandelen aanvraag reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument.md), [Verwerken vermissing reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-reisdocument.md). |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, elke ouder is een te onderscheiden persoon. [HUP BRP: Geboorte](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geboorte.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Ouder | doet aangifte *toewijzing* | [Opmaken geboorteakte](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-geboorteakte.md) | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) (art. 19e) |
| Ouder | erkent of stemt toe *toewijzing* | [Opmaken akte van erkenning](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-erkenning.md) | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Kind erkennen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-kind-erkennen.md) (art. 203, 204) |
| Ouder | verzoekt *toewijzing* | [Inschrijven levenloos geboren kind](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-levenloos-geboren-kind.md) | [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [Utrecht Levenloos geboren kind, aangifte doen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-levenloos-geboren-kind-of-overleden-pasgeboren-kind-aangifte-doen.md) (art. 2.56a) |
| Ouder | verklaart naamskeuze *toewijzing* | [Opmaken akte van naamskeuze](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-naamskeuze.md) | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Achternaam kind kiezen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaam-kind-kiezen.md) (art. 5 lid 4) |
| Ouder | geeft toestemming voor een minderjarige *toewijzing* | [Behandelen aanvraag reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument.md) | [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Paspoort of identiteitskaart aanvragen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) (art. 34; Utrecht regel 131-185) |
| Ouder | meldt vermissing voor een kind *toewijzing* | [Verwerken vermissing reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-reisdocument.md) | [Utrecht Vermissing paspoort of ID-kaart](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) (regel 35-37) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [HUP BRP: Geboorte](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geboorte.md) | HUP BRP: Geboorte |
| [Utrecht Geboorteaangifte doen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) | Gemeente Utrecht: Geboorteaangifte |
| [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |
| [Utrecht Kind erkennen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-kind-erkennen.md) | Gemeente Utrecht: Kind erkennen |
| [Utrecht Levenloos geboren kind, aangifte doen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-levenloos-geboren-kind-of-overleden-pasgeboren-kind-aangifte-doen.md) | Gemeente Utrecht: Levenloos geboren kind |
| [Utrecht Achternaam kind kiezen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaam-kind-kiezen.md) | Gemeente Utrecht: Achternaam kind |
| [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [Utrecht Paspoort of identiteitskaart aanvragen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) | Gemeente Utrecht: Paspoort of ID-kaart aanvragen |
| [Utrecht Vermissing paspoort of ID-kaart](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) | Gemeente Utrecht: Paspoort of ID-kaart kwijt |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen rol Ouder; nieuw voor GEMMA.
