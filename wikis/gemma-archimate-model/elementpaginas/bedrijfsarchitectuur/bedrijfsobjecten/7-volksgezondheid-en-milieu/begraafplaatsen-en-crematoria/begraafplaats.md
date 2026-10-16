---
id: begraafplaats
type: bedrijfsobject
archimate_type: business-object
status: review
naam: Begraafplaats
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Terrein waar stoffelijke overschotten worden begraven en urnen worden bijgezet, aangelegd en in stand gehouden door een houder.
match:
  ggm: geen
  gemma: geen
objectniveau: kernobject
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen
- 2026-vng-wet-op-de-lijkbezorging
---

# Begraafplaats

<!-- Gegenereerd door tools/render.py uit de beoordeling begraafplaats.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Terrein waar stoffelijke overschotten worden begraven en urnen worden bijgezet, aangelegd en in stand gehouden door een houder.

### Beschrijving

Elke gemeente heeft ten minste één gemeentelijke begraafplaats, voor zich of samen met andere gemeenten (art. 33). Daarnaast bestaan bijzondere begraafplaatsen van een kerkgenootschap, rechtspersoon of natuurlijk persoon (art. 24, 37). De gemeente beslist over grond voor en ingebruikname van bijzondere begraafplaatsen en kan begraafplaatsen sluiten (art. 40, 41, 43, 44). Op de begraafplaats liggen graven, urnenmuren en verstrooiingsplaatsen (Groningen art. 1). Een begraafplaats is een fysieke plaats, maar wordt hier als gemeentelijke voorziening beschreven.

## Plaats in het model

### Typering

Bedrijfsobject, niveau kernobject. Uitkomst van de beslistabel: Passief (kern ja, 2/2).

### Plaats in de indelingen

- **Objectniveau**: kernobject.
- **Levensloop bepaald door**: [Beheren begraafplaatsen](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/beheren-begraafplaatsen.md).
- **Mutaties door bedrijfsprocessen**: [Sluiten begraafplaats](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/sluiten-begraafplaats.md), [Verlenen toestemming bijzondere begraafplaats](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlenen-toestemming-bijzondere-begraafplaats.md).
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, passief (Bedrijfsobject, Afspraak, Representatie (geen pagina)). **Hoofdkenmerk**: ding. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, elke begraafplaats apart, met naam (Groningen art. 3 lid 1). [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, aangelegd, in gebruik genomen, gesloten, opgeheven (art. 41, 43, 47). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, met [Beheren begraafplaatsen](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/beheren-begraafplaatsen.md), [Sluiten begraafplaats](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/sluiten-begraafplaats.md), [Uitvoeren lijkbezorging](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvoeren-lijkbezorging.md), [Verlenen toestemming bijzondere begraafplaats](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlenen-toestemming-bijzondere-begraafplaats.md). |

### Specialisaties

- **Gemeentelijke begraafplaats**: Begraafplaats die de gemeente in stand houdt en waarover het college het beheer heeft (art. 33; Groningen art. 3). Geen eigen pagina.
- **Bijzondere begraafplaats**: Begraafplaats van een kerkgenootschap, privaatrechtelijke rechtspersoon of natuurlijk persoon (art. 24, 37, 38). Geen eigen pagina.
- **Joodse begraafplaats**: Deel van een gemeentelijke begraafplaats waarvan het beheer bij de besturen van die gezindte berust (Groningen art. 3 lid 3). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Begraafplaats | bevat *aggregatie* | [Graf](graf.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (Wlb art. 23 lid 1, 2; Groningen art. 1 d, h) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren begraafplaatsen](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/beheren-begraafplaatsen.md) | beheert *toegang (bijwerken)* | Begraafplaats | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 33, 36, 43, 47) |
| [Heffing](../../0-bestuur-en-ondersteuning/belastingen/heffing.md) | voor het gebruik van (lijkbezorgingsrechten) *associatie (gericht)* | Begraafplaats | [VNG Retributies](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-retributies.md) (§ Lijkbezorgingsrechten) |
| [Houder van de begraafplaats](../../../rollen/houder-van-de-begraafplaats.md) | houdt *toegang (houder)* | Begraafplaats | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 8, 23) |
| [Regeling](../../0-bestuur-en-ondersteuning/besluitvorming/regeling.md) | regelt (beheersverordening begraafplaatsen) *associatie (gericht)* | Begraafplaats | [VNG Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-wet-op-de-lijkbezorging.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (VNG inleiding; Groningen) |
| [Sluiten begraafplaats](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/sluiten-begraafplaats.md) | sluit *toegang (beëindigen)* | Begraafplaats | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 43, 44) |
| [Uitvoeren lijkbezorging](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvoeren-lijkbezorging.md) | geschiedt op *toegang (raadplegen)* | Begraafplaats | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 23 lid 1) |
| [Urn](urn.md) | wordt bijgezet op *associatie (gericht)* | Begraafplaats | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 62 lid 1 b) |
| [Verlenen toestemming bijzondere begraafplaats](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlenen-toestemming-bijzondere-begraafplaats.md) | betreft *toegang (bijwerken)* | Begraafplaats | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 40, 41) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) | Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023 |
| [VNG Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-wet-op-de-lijkbezorging.md) | Wet op de lijkbezorging |

### Afstemming met GGM

Geen GGM-entiteit. Het GGM kent geen entiteit voor dit begrip (tools/ggm.py kandidaten: geen naamgenoten of treffers).

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.

### Besluiten redacteur

- 2026-09-30: Kenmerk plaats is nee: beoordeeld als gemeentelijke voorziening, niet als fysieke plaats. *Zekerheid: indruk.*
