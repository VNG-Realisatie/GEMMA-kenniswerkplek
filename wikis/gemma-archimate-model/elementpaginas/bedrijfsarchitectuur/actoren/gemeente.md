---
id: gemeente
type: actor
archimate_type: business-actor
status: goedgekeurd
naam: Gemeente
onderwerpen:
- bestuur-en-organisatie
- lijkbezorging
- burgerzaken
definitie: Een gemeente als rechtspersoon, met een raad, een college van burgemeester en wethouders en een burgemeester.
match:
  gemma: geen
doelgroep: gemeente
bronnen:
- 2024-rijk-gemeentewet-wettekst
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2026-rijk-bw2-rechtspersonen
- 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen
- 2026-rvig-hup-achtergronden-en-begrippen
- 2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven
---

# Gemeente

<!-- Gegenereerd door tools/render.py uit de beoordeling gemeente.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Een gemeente als rechtspersoon, met een raad, een college van burgemeester en wethouders en een burgemeester.

### Beschrijving

De actor Gemeente staat voor een gemeente als rechtspersoon (BW Boek 2 art. 1), met een raad, een college van burgemeester en wethouders en een burgemeester als organen (Gemeentewet art. 6). Het is een soort partij: elke gemeente, niet een afzonderlijke gemeente zoals Amsterdam of Utrecht.

Wat een gemeente moet of mag doen, zijn verantwoordelijkheden. Die staan in het model als rollen die de gemeente vervult, zoals houder van een begraafplaats of kostendrager; de actor is de partij die ze vervult. Het GGM en GEMMA kennen daarnaast het bedrijfsobject Gemeente als gedeelte van het grondgebied; dat is een ander begrip.

### Per onderwerp

#### [Lijkbezorging](../../../onderwerpen/lijkbezorging/begrippen.md)

De gemeente vervult de rollen Houder van de begraafplaats, Houder van het crematorium, Houder van een plaats van bijzetting en Kostendrager. Als houder van de gemeentelijke begraafplaats geeft zij graven uit en onderhoudt zij ze tegen betaling; als kostendrager betaalt zij de lijkbezorging als niemand anders erin voorziet en verhaalt zij de kosten (Wet op de lijkbezorging art. 22, 33, 39 lid 2; Groningen art. 3, 23).

#### [Burgerzaken](../../../onderwerpen/burgerzaken/begrippen.md)

De gemeente vervult de rol Bijhoudingsgemeente: het college van de gemeente waar een ingezetene zijn adres heeft, houdt zijn gegevens in de basisregistratie personen bij (HUP Achtergronden). Een daartoe aangewezen gemeente is ook RNI-loket (Utrecht RNI).

### Homoniemen

| Begrip | Betekenis | Naamkeuze |
|---|---|---|
| Gemeente (GEMMA-rol, doelgroep in de Applicatieservice-indeling) | De verantwoordelijkheid die gemeenten hebben; in GEMMA de doelgroep die de applicatieservices voor de medewerkers van de gemeente ordent | Deze pagina heet Gemeente: de gemeente als rechtspersoon. De GEMMA-rol wordt niet gekoppeld; de verantwoordelijkheden van de gemeente zijn in de wiki eigen rollen. |

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
| **los van verantwoordelijkheid**: Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen? | Ja, blijft bestaan als een rol wegvalt en vervult meer rollen: houder van de begraafplaats, het crematorium en een plaats van bijzetting, en kostendrager (art. 22, 33). [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **eigen rechtspersoon**: Heeft het verband of de organisatie eigen rechtspersoonlijkheid (openbaar lichaam, stichting, vennootschap)? | Ja, gemeenten bezitten rechtspersoonlijkheid (BW 2 art. 1). [BW Boek 2](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-bw2-rechtspersonen.md) |
| **vervult een rol**: Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? | Ja, met [Houder van de begraafplaats](../rollen/houder-van-de-begraafplaats.md), [Houder van het crematorium](../rollen/houder-van-het-crematorium.md), [Houder van een plaats van bijzetting](../rollen/houder-van-een-plaats-van-bijzetting.md), [Kostendrager](../rollen/kostendrager.md), [Bijhoudingsgemeente](../rollen/bijhoudingsgemeente.md), [RNI-loket](../rollen/rni-loket.md). |
| **soort partij**: Heeft elke gemeente met deze partij te maken in dezelfde rol, zodat het element voor alle gemeenten geldt? Het criterium sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat. | Ja, elke gemeente; een soort partij, geen individuele gemeente. [Gemeentewet](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |
| **generiek**: Komt het met dezelfde betekenis in veel onderwerpen voor? | Ja, komt in elk onderwerp voor: de gemeente als partij (Gemeentewet art. 6). [Gemeentewet](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Gemeente | vervult *toewijzing* | [Houder van de begraafplaats](../rollen/houder-van-de-begraafplaats.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 33, 39 lid 2) |
| Gemeente | vervult *toewijzing* | [Houder van het crematorium](../rollen/houder-van-het-crematorium.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 51) |
| Gemeente | vervult *toewijzing* | [Houder van een plaats van bijzetting](../rollen/houder-van-een-plaats-van-bijzetting.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 62 lid 1) |
| Gemeente | vervult *toewijzing* | [Kostendrager](../rollen/kostendrager.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 22) |
| Gemeente | omvat *aggregatie* | [Gemeenteraad](gemeenteraad.md) | [Gemeentewet](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) (art. 6) |
| Gemeente | omvat *aggregatie* | [College van B&W](college-van-b-w.md) | [Gemeentewet](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) (art. 6) |
| Gemeente | omvat *aggregatie* | [Burgemeester](burgemeester.md) | [Gemeentewet](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) (art. 6) |
| Gemeente | vervult *toewijzing* | [Bijhoudingsgemeente](../rollen/bijhoudingsgemeente.md) | [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |
| Gemeente | vervult *toewijzing* | [RNI-loket](../rollen/rni-loket.md) | [Utrecht RNI inschrijven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven.md) (Inschrijven RNI) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Gemeentewet](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) | Gemeentewet (BWBR0005416) - geldend per 2024-01-31 |
| [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [BW Boek 2](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-bw2-rechtspersonen.md) | Burgerlijk Wetboek Boek 2 Rechtspersonen (BWBR0003045) |
| [Beheersverordening begraafplaatsen Groningen](../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) | Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023 |
| [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md) | HUP BRP: Achtergronden en begrippen |
| [Utrecht RNI inschrijven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven.md) | Gemeente Utrecht: Registratie niet-ingezetenen (RNI) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. De GEMMA-rol Gemeente staat voor de verantwoordelijkheid die gemeenten hebben, en ordent als doelgroep de applicatieservices voor de medewerkers van de gemeente. Dit element is de gemeente als rechtspersoon, een actor: een ander begrip en een ander type, dus geen koppeling.

Procesarchitectuur-terugmeldingen:

- [Nummer 6](../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, open): **Kennismodel:** het kennismodel procesarchitectuur kent geen relaties tussen actoren; een actor wordt alleen aan een rol toegewezen ([2026-vng-over-gemma](../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 602). **Bevinding:** tussen actoren bestaan structurele relaties die de gemeente nodig heeft om haar organisatie te beschrijven. De Gemeente omvat de Gemeenteraad, het College van B&W en de Burgemeester, en de Burgemeester is voorzitter van de raad en van het college ([2024-rijk-gemeentewet-wettekst](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), art. 6, 9, 34). Het model gebruikt tussen actoren alleen deze structurele relaties; een handeling tussen partijen loopt via rollen en processen of een gebeurtenis. **Voorstel:** neem in het kennismodel structurele relaties tussen actoren op (deel van, lid van, voorzitter van), als aggregatie of associatie; handelingen tussen partijen blijven lopen via rollen.

### Besluiten redacteur

- 2026-10-04: Actor als soort partij (elke gemeente), geen rol: de afzonderlijke gemeenten zijn geen eigen element. *Zekerheid: logica.*
- 2026-10-04: Geen GEMMA-match: de actor Gemeente is een gemeente als rechtspersoon, de GEMMA-rol Gemeente is de verantwoordelijkheid die gemeenten hebben (doelgroep van applicatieservices). Het onderscheid staat in definitie, beschrijving en homoniemen. *Zekerheid: logica.*
