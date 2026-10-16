---
id: uitvaartondernemer
type: actor
archimate_type: business-actor
status: goedgekeurd
naam: Uitvaartondernemer
onderwerpen:
- lijkbezorging
- burgerzaken
definitie: Onderneming die in opdracht van nabestaanden de uitvaart verzorgt.
match:
  gemma: geen
data_object: nee
doelgroep: inwoners en ondernemers
synoniemen:
- Uitvaartonderneming (beleid)
bronnen:
- 2010-vng-model-beheersverordening-begraafplaatsen
- 2026-rvo-aangifte-en-akte-van-overlijden
- 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen
- 2026-utrecht-burgerzaken-overlijden-aangifte-doen
- 2026-rijk-burgerlijk-wetboek-boek-1
---

# Uitvaartondernemer

<!-- Gegenereerd door tools/render.py uit de beoordeling uitvaartondernemer.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Onderneming die in opdracht van nabestaanden de uitvaart verzorgt.

### Beschrijving

De uitvaartondernemer doet voor de nabestaanden aangifte van overlijden bij de gemeente waar de persoon is overleden, en krijgt van de gemeente de akte van overlijden en het verlof tot begraven of cremeren; voor het vervroegen of uitstellen van de uitvaart vraagt hij een vergunning aan (Ondernemersplein). De beheerder bepaalt tijd en plaats van een begraving in overleg met de uitvaartondernemer; personeel van uitvaartondernemingen volgt op de begraafplaats de aanwijzingen van de beheerder (Groningen art. 5, 7; VNG-modelverordening art. 4).

### Per onderwerp

#### [Burgerzaken](../../../onderwerpen/burgerzaken/begrippen.md)

De uitvaartondernemer doet meestal de aangifte van overlijden, als gemachtigde van degene die in de lijkbezorging voorziet, online met eHerkenning of aan de balie (BW 1 art. 19h lid 2; Utrecht Overlijden, aangifte doen).

### Synoniemen

| Synoniem | Context |
|---|---|
| Uitvaartonderneming | beleid |

## Plaats in het model

### Typering

Actor. Uitkomst van de beslistabel: Handelende partij (kern ja).

### Plaats in de indelingen

- **Doelgroep**: inwoners en ondernemers.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: handelende partij. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **los van verantwoordelijkheid**: Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen? | Ja, bestaat los van de afzonderlijke uitvaart; handelt voor steeds andere nabestaanden. [Ondernemersplein Aangifte overlijden](../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **vervult een rol**: Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? | Ja, met [Degene die in de lijkbezorging voorziet](../rollen/degene-die-in-de-lijkbezorging-voorziet.md), [Aangever](../rollen/aangever.md). |
| **soort partij**: Heeft elke gemeente met deze partij te maken in dezelfde rol, zodat het element voor alle gemeenten geldt? Het criterium sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat. | Ja, een soort partij die bij elke uitvaart in elke gemeente optreedt (RVO); geen individuele onderneming. [Ondernemersplein Aangifte overlijden](../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Uitvaartondernemer | vervult namens de nabestaanden *toewijzing* | [Degene die in de lijkbezorging voorziet](../rollen/degene-die-in-de-lijkbezorging-voorziet.md) | [Ondernemersplein Aangifte overlijden](../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) (inleiding, § Aangifte doen van overlijden) |
| Uitvaartondernemer | doet aangifte van overlijden als *toewijzing* | [Aangever](../rollen/aangever.md) | [Utrecht Overlijden, aangifte doen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-overlijden-aangifte-doen.md), [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (Utrecht inleiding; BW 1 art. 19h lid 2) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [VNG Model-beheersverordening begraafplaatsen](../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md) | Model-beheersverordening begraafplaatsen 2010 (VNG), met toelichting |
| [Ondernemersplein Aangifte overlijden](../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) | Aangifte en akte van overlijden (Ondernemersplein) |
| [Beheersverordening begraafplaatsen Groningen](../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) | Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023 |
| [Utrecht Overlijden, aangifte doen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-overlijden-aangifte-doen.md) | Gemeente Utrecht: Overlijden |
| [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.
