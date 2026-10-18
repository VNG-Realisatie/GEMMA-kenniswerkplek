---
id: inwoner
type: actor
archimate_type: business-actor
status: review
naam: Inwoner
onderwerpen:
- participatie
definitie: Persoon die ingezetene is van de gemeente.
match:
  gemma: geen
doelgroep: inwoners en ondernemers
synoniemen:
- Ingezetene (wet)
bronnen:
- 2026-rijk-gemeentewet-wettekst
- 2024-vng-implementatiehandleiding-model-participatieverordening
- 2024-vng-model-participatieverordening
---

# Inwoner

<!-- Gegenereerd door tools/render.py uit de beoordeling inwoner.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Persoon die ingezetene is van de gemeente.

### Beschrijving

De Model Participatieverordening definieert inwoners als ingezetenen als bedoeld in artikel 2 van de Gemeentewet; een gemeente kan daar ondernemers aan toevoegen ([2024-vng-model-participatieverordening](../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md), var. 1 art. 1). De wet spreekt van ingezetenen ([2026-rijk-gemeentewet-wettekst](../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-gemeentewet-wettekst.md), art. 150).

De gegevens van de ingezetene staan in het bedrijfsobject Ingeschreven persoon, met de specialisatie Ingezetene.

### Per onderwerp

#### [Participatie](../../../onderwerpen/participatie/begrippen.md)

De gemeente betrekt inwoners bij de voorbereiding, uitvoering en evaluatie van haar beleid, en inwoners kunnen bij het college een verzoek indienen om de feitelijke uitvoering van een gemeentelijke taak over te nemen, het uitdaagrecht ([2026-rijk-gemeentewet-wettekst](../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-gemeentewet-wettekst.md), art. 150 lid 1 en 3; [2024-vng-model-participatieverordening](../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md), var. 1 art. 6 lid 1).

### Synoniemen

| Synoniem | Context |
|---|---|
| Ingezetene | wet |

## Plaats in het model

### Typering

Actor. Uitkomst van de beslistabel: Handelende partij (1 toetskenmerken ja).

### Plaats in de indelingen

- **Doelgroep**: inwoners en ondernemers.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: handelende partij.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Gemeentewet](../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-gemeentewet-wettekst.md), [VNG Implementatiehandleiding participatieverordening](../../../onderwerpen/participatie/bronduidingen/richtlijn/2024-vng-implementatiehandleiding-model-participatieverordening.md) |
| **soort partij**: Heeft elke gemeente met deze partij te maken in dezelfde rol, zodat het element voor alle gemeenten geldt? Het criterium sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat. | Ja, elke gemeente betrekt haar ingezetenen bij beleid en stelt voorwaarden voor de uitvoering van taken door hen (art. 150 lid 1 en 3). [Gemeentewet](../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-gemeentewet-wettekst.md) |
| **vervult een rol**: Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? | Ja, met [Indiener](../rollen/indiener.md). [Gemeentewet](../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-gemeentewet-wettekst.md), [VNG Implementatiehandleiding participatieverordening](../../../onderwerpen/participatie/bronduidingen/richtlijn/2024-vng-implementatiehandleiding-model-participatieverordening.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Inwoner | dient een verzoek in als *toewijzing* | [Indiener](../rollen/indiener.md) | [VNG Model Participatieverordening](../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) (var. 1 art. 6 lid 1, var. 2 art. [11] lid 1) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Gemeentewet](../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-gemeentewet-wettekst.md) | Gemeentewet (BWBR0005416) |
| [VNG Implementatiehandleiding participatieverordening](../../../onderwerpen/participatie/bronduidingen/richtlijn/2024-vng-implementatiehandleiding-model-participatieverordening.md) | Implementatiehandleiding VNG Model Participatieverordening 2024 |
| [VNG Model Participatieverordening](../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) | VNG Model Participatieverordening 2024 |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent de actor Burger (procesarchitectuur, Actoren en rollen) zonder definitie en zonder relaties; een burger is niet altijd ingezetene van de gemeente, dus geen match op betekenis. Ingezetene (RSGB) is een bedrijfsobject, de registratie van de persoon, geen partij. Nieuw voor GEMMA.

GEMMA-terugmeldingen:

- [Nummer 8](../../../modellen/gemma/terugmeldingen/gemma-team.md) (element, open): **GEMMA:** de actor Burger staat in de procesarchitectuur (Actoren en rollen), zonder definitie en zonder relaties ([2026-vng-gemma-2026-10-02](../../../modellen/gemma/bronduidingen/model/2026-vng-gemma-2026-10-02.md)). **Bevinding:** de import voegt de actor Inwoner toe: een ingezetene van de gemeente, die bij het beleid wordt betrokken en een verzoek kan indienen om een gemeentelijke taak over te nemen ([2026-rijk-gemeentewet-wettekst](../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-gemeentewet-wettekst.md), art. 150; [2024-vng-model-participatieverordening](../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md), art. 1). De wiki koppelt Inwoner niet aan Burger, omdat Burger geen definitie heeft en een burger niet altijd ingezetene van de gemeente is. **Voorstel:** geef Burger een definitie en beslis of Burger een generalisatie van Inwoner wordt, of vervalt ten gunste van Inwoner.
