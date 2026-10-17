---
id: asverstrooiing
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Asverstrooiing
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Toestemming van de gemeente om as te verstrooien op een plek waar dat zonder toestemming niet mag.
match:
  gemma: geen
afnemer: extern
domein: Fysieke leefomgeving
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2025-groningen-algemene-plaatselijke-verordening
- 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen
- 2023-vng-model-apv
---

# Asverstrooiing

<!-- Gegenereerd door tools/render.py uit de beoordeling asverstrooiing.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

**Zonder landelijke wettelijke grondslag.** Een UPL-dienst die geen wettelijke taak is: ze wordt beschreven voor zover mogelijk, zonder processen, objecten, gebeurtenissen of rollen, is teruggemeld aan de procesarchitectuur ([nr. 24](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md)) en gaat niet naar het GEMMA-model ([lijst](../../../../overig/zonder-grondslag.md)).

## Betekenis

### Definitie

Toestemming van de gemeente om as te verstrooien op een plek waar dat zonder toestemming niet mag.

### Beschrijving

Buiten de begraafplaats is asverstrooiing vrij, behalve op de plaatsen die de APV verbiedt en bij hinder of overlast; het college kan op verzoek van de nabestaande die zorgdraagt voor de asbus bij bijzondere omstandigheden ontheffing verlenen, behalve voor begraafplaatsen, crematoriumterreinen, schoolpleinen en kinderspeelplaatsen (APV Groningen art. 5:27, 5:28). Op de gemeentelijke begraafplaats is verstrooien verboden zonder toestemming van het college, op een aangewezen plek en onder toezicht van een medewerker van de begraafplaats (Groningen art. 21).

De UPL geeft als grondslag art. 5:36 van de model-APV en rekent het product tot het GEMMA-domein Openbare orde en veiligheid (UPL).

Tegenspraak: de APV definieert incidentele asverstrooiing als verstrooien op een plek die de overledene of nabestaande kiest, buiten een permanent daartoe bestemd terrein (APV Groningen art. 5:26); de beheersverordening als verstrooien op een plek die de gemeente aanwijst, op of buiten de begraafplaats (Groningen art. 1). Beide vallen onder deze dienst.

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (kern ja, 2/2).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Exploiteren van begraafplaatsen](../../../bedrijfsfuncties/fysieke-leefomgeving/exploiteren-van-begraafplaatsen.md).
- **Afnemer**: extern.
- **Domein**: Fysieke leefomgeving.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een ontheffing van het verbod of een toestemming om op een aangewezen plek te verstrooien (APV Groningen art. 5:27 lid 3; Groningen art. 21 lid 2). [APV Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2025-groningen-algemene-plaatselijke-verordening.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, burger en bedrijf (UPL); de nabestaande die zorgdraagt voor de asbus vraagt de ontheffing aan (APV Groningen art. 5:27 lid 3). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [APV Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2025-groningen-algemene-plaatselijke-verordening.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Exploiteren van begraafplaatsen](../../../bedrijfsfuncties/fysieke-leefomgeving/exploiteren-van-begraafplaatsen.md), Verlenen toestemming asverstrooiing. |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Asverstrooiing | bedient *bediening* | [Nabestaande](../../../rollen/nabestaande.md) | [Model-APV](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-vng-model-apv.md), [APV Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2025-groningen-algemene-plaatselijke-verordening.md) (Model-APV art. 5:36 lid 3; Groningen art. 5:27 lid 3) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Exploiteren van begraafplaatsen](../../../bedrijfsfuncties/fysieke-leefomgeving/exploiteren-van-begraafplaatsen.md) | omvat *aggregatie* | Asverstrooiing | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Model-APV](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-vng-model-apv.md) (UPL nr. 32; Model-APV art. 5:36) |
| [Exploiteren van begraafplaatsen](../../../bedrijfsfuncties/fysieke-leefomgeving/exploiteren-van-begraafplaatsen.md) | realiseert *realisatie* | Asverstrooiing | [Model-APV](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-vng-model-apv.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (Model-APV art. 5:36; UPL nr. 32) |
| [Model-APV](../../../../motivatie/beleidskaders/gemeentelijke-regelgeving/model-apv.md) | werkt uit voor *associatie (gericht)* | Asverstrooiing | [Model-APV](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-vng-model-apv.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. 5:36 lid 3; UPL nr. 32) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [APV Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2025-groningen-algemene-plaatselijke-verordening.md) | Algemene Plaatselijke Verordening Groningen 2021 |
| [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) | Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023 |
| [Model-APV](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-vng-model-apv.md) | Model Algemene plaatselijke verordening per 1 januari 2024 (VNG, november 2023) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 24](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (grondslag, open): **UPL:** asverstrooiing heeft als grondslag art. 5:36 van de Model-APV ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), nr. 32). **Bevinding:** de Model-APV is een model dat gemeenten invullen en waarvan ze bepalingen mogen weglaten; het is geen landelijke wettelijke grondslag ([2023-vng-model-apv](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-vng-model-apv.md)). De Wet op de lijkbezorging staat het verstrooien door de nabestaande die de zorg voor de asbus heeft toe zonder toestemming van de gemeente, en geeft burgemeester en wethouders alleen een vergunning voor een terrein om permanent as op te verstrooien ([2026-rijk-wet-op-de-lijkbezorging-wettekst](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), art. 66a lid 2, 66b). De ontheffing of toestemming voor incidentele asverstrooiing regelt de gemeente zelf, in haar APV en beheersverordening ([2025-groningen-algemene-plaatselijke-verordening](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2025-groningen-algemene-plaatselijke-verordening.md), art. 5:27; [2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md), art. 21). Het is daarmee geen wettelijke taak. GEMMA beschrijft de dienst, maar neemt haar niet op in het GEMMA-model. **Voorstel:** vermeld bij het UPL-product dat er geen landelijke wettelijke grondslag is en dat het een taak is die de gemeente zelf op zich neemt (Gemeentewet art. 108 lid 1), en noem art. 5:36 van de Model-APV als uitwerking, niet als grondslag.

GEMMA-terugmeldingen:

- [Nummer 1](../../../../../modellen/gemma/terugmeldingen/gemma-team.md) (element, open): **GEMMA:** de functies Producten- en dienstenrealisatie veiligheidsdomein en Uitvoering openbare orde en veiligheid omvatten onder meer Vergunningenbeheer evenementen en Horeca vergunningverlening ([2026-vng-gemma-2026-10-02](../../../../../modellen/gemma/bronduidingen/model/2026-vng-gemma-2026-10-02.md)). De UPL zet asverstrooiing onder Openbare orde en veiligheid ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), nr. 32). **Bevinding:** asverstrooiing is alleen in de Model-APV geregeld, en gemeenten mogen die bepaling weglaten ([2023-vng-model-apv](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-vng-model-apv.md)). In de wiki bleef daardoor niets over wat deze twee functies bedienen, dus vervallen ze en staat asverstrooiing bij de andere producten van de lijkbezorging. De import verwijdert niets, dus in GEMMA blijft staan wat de wiki laat vervallen. Ook de andere producten onder deze functies (zoals de evenementenvergunning) berusten deels alleen op de APV. **Voorstel:** verwijder asverstrooiing ook uit GEMMA, samen met de twee functies die alleen daarvoor in de wiki stonden. Beoordeel bij een onderwerp Openbare orde en veiligheid per overig product of het een landelijke wettelijke basis heeft, en laat de producten zonder die basis ook vervallen.
