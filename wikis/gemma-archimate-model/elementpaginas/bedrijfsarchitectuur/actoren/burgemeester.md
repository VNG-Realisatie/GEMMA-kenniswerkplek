---
id: burgemeester
type: actor
archimate_type: business-actor
status: review
naam: Burgemeester
onderwerpen:
- bestuur-en-organisatie
- lijkbezorging
- burgerzaken
definitie: Bestuursorgaan van de gemeente, voorzitter van gemeenteraad en college, benoemd bij koninklijk besluit.
match:
  gemma: geen
data_object: nee
doelgroep: gemeente
bronnen:
- 2024-rijk-gemeentewet-wettekst
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-rijk-wegenverkeerswet-1994-bwbr0006622
- 2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194
---

# Burgemeester

<!-- Gegenereerd door tools/render.py uit de beoordeling burgemeester.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Bestuursorgaan van de gemeente, voorzitter van gemeenteraad en college, benoemd bij koninklijk besluit.

### Beschrijving

De burgemeester wordt bij koninklijk besluit benoemd voor zes jaar (Gemeentewet art. 61) en is voorzitter van de raad en van het college (art. 9, 34). De burgemeester vertegenwoordigt de gemeente in en buiten rechte (art. 171).

### Per onderwerp

#### [Lijkbezorging](../../../onderwerpen/lijkbezorging/begrippen.md)

De burgemeester draagt zorg voor de lijkbezorging als niemand daarin voorziet, verleent vergunning tot opgraving en verlof tot ontleding, stelt een andere termijn en treft maatregelen bij een besmet stoffelijk overschot (Wet op de lijkbezorging art. 17, 21, 22a, 29, 68).

#### [Burgerzaken](../../../onderwerpen/burgerzaken/begrippen.md)

De burgemeester neemt aanvragen voor reisdocumenten in ontvangst van ingezetenen met een adres in zijn gemeente, verstrekt, reikt uit, wijzigt, weigert, verklaart vervallen en houdt in (Paspoortwet art. 26, 40, 42, 43, 44, 50b). Hij besluit tot afgifte van rijbewijzen en reikt ze uit (Wegenverkeerswet 1994 art. 116, 118a, 120a) en ontvangt de aanvraag voor een verklaring omtrent het gedrag, die hij doorzendt aan de minister (Wet justitiële en strafvorderlijke gegevens art. 30).

## Plaats in het model

### Typering

Actor. Uitkomst van de beslistabel: Handelende partij (kern ja).

### Plaats in de indelingen

- **Doelgroep**: gemeente.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: handelende partij. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **los van verantwoordelijkheid**: Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen? | Ja, bestaat los van elke afzonderlijke bevoegdheid; vervult ook andere rollen (voorzitter van raad en college, art. 9, 34). [Gemeentewet](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |
| **vervult een rol**: Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? | Ja, met [Beslisser](../rollen/beslisser.md). |
| **soort partij**: Heeft elke gemeente met deze partij te maken in dezelfde rol, zodat het element voor alle gemeenten geldt? Het criterium sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat. | Ja, elke gemeente heeft een raad, een college van burgemeester en wethouders en een burgemeester (Gemeentewet art. 6). [Gemeentewet](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |
| **generiek**: Komt het met dezelfde betekenis in veel onderwerpen voor? | Ja, komt in elk onderwerp voor als bestuursorgaan (Gemeentewet art. 6). [Gemeentewet](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Burgemeester | vervult *toewijzing* | [Beslisser](../rollen/beslisser.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Wegenverkeerswet 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Wet justitiële en strafvorderlijke gegevens](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) (Wet op de lijkbezorging art. 17, 21, 22a, 29, 68; Paspoortwet art. 40, 44; Wegenverkeerswet 1994 art. 116, 118a) |
| Burgemeester | is voorzitter van *associatie (gericht)* | [Gemeenteraad](gemeenteraad.md) | [Gemeentewet](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) (art. 9) |
| Burgemeester | is voorzitter van *associatie (gericht)* | [College van B&W](college-van-b-w.md) | [Gemeentewet](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) (art. 34 lid 2) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Gemeente](gemeente.md) | omvat *aggregatie* | Burgemeester | [Gemeentewet](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) (art. 6) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Gemeentewet](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) | Gemeentewet (BWBR0005416) - geldend per 2024-01-31 |
| [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [Wegenverkeerswet 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) | Wegenverkeerswet 1994 |
| [Wet justitiële en strafvorderlijke gegevens](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) | Wet justitiële en strafvorderlijke gegevens |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen actor Burgemeester (tools/gemma.py kandidaten: geen naamgenoot); nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 6](../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, open): **Kennismodel:** het kennismodel procesarchitectuur kent geen relaties tussen actoren; een actor wordt alleen aan een rol toegewezen ([2026-vng-over-gemma](../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 602). **Bevinding:** tussen actoren bestaan structurele relaties die de gemeente nodig heeft om haar organisatie te beschrijven. De Gemeente omvat de Gemeenteraad, het College van B&W en de Burgemeester, en de Burgemeester is voorzitter van de raad en van het college ([2024-rijk-gemeentewet-wettekst](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), art. 6, 9, 34). Het model gebruikt tussen actoren alleen deze structurele relaties; een handeling tussen partijen loopt via rollen en processen of een gebeurtenis. **Voorstel:** neem in het kennismodel structurele relaties tussen actoren op (deel van, lid van, voorzitter van), als aggregatie of associatie; handelingen tussen partijen blijven lopen via rollen.
