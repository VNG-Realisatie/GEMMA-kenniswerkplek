---
id: gedenkteken-plaatsingsvergunning
type: dienst
archimate_type: business-service
status: review
naam: Gedenkteken plaatsingsvergunning
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Vergunning van de gemeente voor het plaatsen en hebben van een gedenkteken of andere grafbedekking op een graf.
match:
  gemma: geen
afnemer: extern
domein: Fysieke leefomgeving
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2010-vng-model-beheersverordening-begraafplaatsen
- 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen
---

# Gedenkteken plaatsingsvergunning

<!-- Gegenereerd door tools/render.py uit de beoordeling gedenkteken-plaatsingsvergunning.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

**Zonder landelijke wettelijke grondslag.** Een UPL-dienst die geen wettelijke taak is: ze wordt beschreven voor zover mogelijk, zonder processen, objecten, gebeurtenissen of rollen, is teruggemeld aan de procesarchitectuur ([nr. 25](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md)) en gaat niet naar het GEMMA-model ([lijst](../../../../overig/zonder-grondslag.md)).

## Betekenis

### Definitie

Vergunning van de gemeente voor het plaatsen en hebben van een gedenkteken of andere grafbedekking op een graf.

### Beschrijving

Voor het hebben van een grafbedekking is een schriftelijke vergunning van het college nodig; de rechthebbende van een particulier graf vraagt haar aan (VNG-modelverordening art. 19 lid 1–2; Groningen art. 22 lid 1–2). Het college kan nadere regels stellen over de aanvraag, de aard en de afmetingen van de grafbedekking en kan de vergunning weigeren (Groningen art. 22 lid 3–4). De beheersverordeningen spreken van vergunning grafbedekking; de UPL van gedenkteken plaatsingsvergunning (UPL).

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Exploiteren van begraafplaatsen](../../../bedrijfsfuncties/fysieke-leefomgeving/exploiteren-van-begraafplaatsen.md).
- **Afnemer**: extern.
- **Domein**: Fysieke leefomgeving.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [VNG Model-beheersverordening begraafplaatsen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Exploiteren van begraafplaatsen](../../../bedrijfsfuncties/fysieke-leefomgeving/exploiteren-van-begraafplaatsen.md), Verlenen vergunning grafbedekking. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [VNG Model-beheersverordening begraafplaatsen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [VNG Model-beheersverordening begraafplaatsen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [VNG Model-beheersverordening begraafplaatsen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Gedenkteken plaatsingsvergunning | bedient *bediening* | [Rechthebbende op het graf](../../../rollen/rechthebbende-op-het-graf.md) | [VNG Model-beheersverordening begraafplaatsen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (VNG-modelverordening art. 19 lid 2; Groningen art. 22 lid 2) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Exploiteren van begraafplaatsen](../../../bedrijfsfuncties/fysieke-leefomgeving/exploiteren-van-begraafplaatsen.md) | omvat *aggregatie* | Gedenkteken plaatsingsvergunning | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 142; GEMMA-toelichting (vergunningen voor plaatsen van grafstenen)) |
| [Exploiteren van begraafplaatsen](../../../bedrijfsfuncties/fysieke-leefomgeving/exploiteren-van-begraafplaatsen.md) | realiseert *realisatie* | Gedenkteken plaatsingsvergunning | [VNG Model-beheersverordening begraafplaatsen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (VNG-modelverordening art. 19; UPL nr. 142) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [VNG Model-beheersverordening begraafplaatsen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md) | Model-beheersverordening begraafplaatsen 2010 (VNG), met toelichting |
| [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) | Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023 |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 25](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (grondslag, open): **UPL:** gedenkteken plaatsingsvergunning heeft als grondslag art. 19 van de Model beheersverordening begraafplaatsen ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), nr. 142). **Bevinding:** de vergunning voor een grafbedekking staat alleen in de beheersverordening van de gemeente, die de VNG-modelverordening uitwerkt ([2010-vng-model-beheersverordening-begraafplaatsen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md), art. 19; [2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md), art. 22). Een VNG-modelverordening is geen landelijke wettelijke grondslag, en de Wet op de lijkbezorging regelt de grafbedekking niet ([2026-rijk-wet-op-de-lijkbezorging-wettekst](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md)). Het is daarmee geen wettelijke taak. GEMMA beschrijft de dienst, maar neemt haar niet op in het GEMMA-model. **Voorstel:** vermeld bij het UPL-product dat er geen landelijke wettelijke grondslag is en dat het een taak is die de gemeente zelf op zich neemt (Gemeentewet art. 108 lid 1), en noem art. 19 van de Model beheersverordening begraafplaatsen als uitwerking, niet als grondslag.
