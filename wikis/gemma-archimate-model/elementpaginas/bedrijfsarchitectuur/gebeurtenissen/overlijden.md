---
id: overlijden
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Overlijden
onderwerpen:
- burgerzaken
- lijkbezorging
definitie: Het sterven van een persoon.
match:
  gemma: geen
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2026-rvo-aangifte-en-akte-van-overlijden
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-rvig-hup-overlijden-nederland
- 2026-utrecht-burgerzaken-overlijden-aangifte-doen
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-rvig-hup-van-rechtswege-vervallen-reisdocument
---

# Overlijden

<!-- Gegenereerd door tools/render.py uit de beoordeling overlijden.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het sterven van een persoon.

### Beschrijving

Het overlijden van een persoon wordt aangegeven bij de gemeente waar de persoon is overleden; voor de aangifte is een verklaring van overlijden nodig (Ondernemersplein).

### Per onderwerp

#### [Lijkbezorging](../../../onderwerpen/lijkbezorging/begrippen.md)

Het overlijden start de schouwing van het stoffelijk overschot (Wet op de lijkbezorging art. 3) en de termijn waarbinnen de lijkbezorging moet plaatsvinden: niet eerder dan 36 uur en uiterlijk op de zesde werkdag (art. 16).

#### [Burgerzaken](../../../onderwerpen/burgerzaken/begrippen.md)

Het overlijden wordt aangegeven bij de ambtenaar van de burgerlijke stand van de gemeente van overlijden, die de akte van overlijden opmaakt (BW 1 art. 19f, 19h). De woongemeente verwerkt het in de BRP: de bijhouding van de persoonslijst wordt opgeschort, en bij een echtgenoot of geregistreerd partner wordt de ontbinding door overlijden verwerkt (HUP Overlijden in Nederland).

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (2 toetskenmerken ja).

### Plaats in de indelingen

- **Start**: [Bezorgen stoffelijk overschot](../bedrijfsinteracties/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bezorgen-stoffelijk-overschot.md), [Opmaken akte van overlijden](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-overlijden.md), [Schouwen stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/schouwen-stoffelijk-overschot.md), [Toestaan lijkbezorging](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/toestaan-lijkbezorging.md), [Uitvoeren lijkbezorging](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvoeren-lijkbezorging.md), [Verval van het reisdocument](verval-van-het-reisdocument.md).

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md), [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Overlijden nederland](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-nederland.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Schouwen stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/schouwen-stoffelijk-overschot.md), [Uitvoeren lijkbezorging](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvoeren-lijkbezorging.md), [Bezorgen stoffelijk overschot](../bedrijfsinteracties/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bezorgen-stoffelijk-overschot.md), [Opmaken akte van overlijden](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-overlijden.md). [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md), [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Overlijden nederland](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-nederland.md) |
| **komt herhaald voor**: Gebeurt het regelmatig en voor verschillende gevallen, en is het geen eenmalig voorval? | Ja, standaard. [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md), [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Overlijden nederland](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-nederland.md) |

### Specialisaties

- **Lijkvinding**: Het vinden van een stoffelijk overschot van een onbekende of niet aangegeven overledene; de hulpofficier van justitie doet aangifte en datum en plaats van de vinding gelden als die van het overlijden (Besluit burgerlijke stand art. 62; HUP Lijkvinding). Geen eigen pagina.
- **Rechtsvermoeden van overlijden**: Een uitspraak van de rechtbank dat een vermiste wordt vermoed te zijn overleden, ingeschreven in de registers (HUP Rechtsvermoeden van overlijden). Geen eigen pagina.
- **Overlijden in het buitenland**: Verwerkt op een buitenlandse, consulaire of Haagse akte (HUP Overlijden buitenland). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Overlijden | leidt tot *triggering* | [Schouwen stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/schouwen-stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3) |
| Overlijden | leidt tot *triggering* | [Uitvoeren lijkbezorging](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvoeren-lijkbezorging.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 16) |
| Overlijden | start *triggering* | [Bezorgen stoffelijk overschot](../bedrijfsinteracties/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bezorgen-stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3, 16) |
| Overlijden | leidt tot *triggering* | [Opmaken akte van overlijden](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-overlijden.md) | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Overlijden, aangifte doen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-overlijden-aangifte-doen.md) (art. 19f, 19h; Utrecht inleiding) |
| Overlijden | doet het reisdocument vervallen *triggering* | [Verval van het reisdocument](verval-van-het-reisdocument.md) | [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) (Paspoortwet art. 47 lid 1 onder f; HUP Van rechtswege vervallen) |
| Overlijden | start *triggering* | [Toestaan lijkbezorging](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/toestaan-lijkbezorging.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3, 11, 18) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden burgerlijke stand](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Overlijden | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19f, 19h) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [Ondernemersplein Aangifte overlijden](../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) | Aangifte en akte van overlijden (Ondernemersplein) |
| [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [HUP BRP: Overlijden nederland](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-nederland.md) | HUP BRP: Overlijden nederland |
| [Utrecht Overlijden, aangifte doen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-overlijden-aangifte-doen.md) | Gemeente Utrecht: Overlijden |
| [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [HUP Van rechtswege vervallen reisdocument](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) | HUP BRP: Van rechtswege vervallen reisdocument |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.

### Besluiten redacteur

- 2026-10-04: Niet generiek: Overlijden is een specifieke gebeurtenis, geen specialisatie van een generieke GEMMA-gebeurtenis; geen voorstel aan GEMMA. *Zekerheid: logica.*
- 2026-10-08: Overlijden leidt tot de akte (Opmaken akte van overlijden, daarna Verlenen verlof) en tot het begraven of cremeren (Uitvoeren lijkbezorging). Bijzetten of verstrooien van de as wordt een deelproces van Uitvoeren lijkbezorging. Schouwen stoffelijk overschot blijft een eigen bedrijfsproces (de schouw gebeurt vóór de aangifte en de aanvraag van het verlof, door een andere rol); de verklaring van overlijden gaat als stroom naar Verlenen verlof (Wlb art. 12). Afgewezen: Schouwen als deelproces van Verlenen verlof. *Zekerheid: logica.*
