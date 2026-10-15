---
id: ambtenaar-van-de-burgerlijke-stand
type: rol
archimate_type: business-role
status: review
naam: Ambtenaar van de burgerlijke stand
onderwerpen:
- burgerzaken
- lijkbezorging
definitie: Ambtenaar die bevoegd is akten van de burgerlijke stand op te maken.
match:
  gemma: geen
data_object: nee
doelgroep: gemeente
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2026-rvo-aangifte-en-akte-van-overlijden
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493
---

# Ambtenaar van de burgerlijke stand

<!-- Gegenereerd door tools/render.py uit de beoordeling ambtenaar-van-de-burgerlijke-stand.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Ambtenaar die bevoegd is akten van de burgerlijke stand op te maken.

### Beschrijving

De ambtenaar van de burgerlijke stand maakt de akten van de burgerlijke stand op, waaronder de akte van overlijden na aangifte bij de gemeente waar iemand is overleden (Wet op de lijkbezorging art. 13, 14; Ondernemersplein).

### Per onderwerp

#### [Lijkbezorging](../../../onderwerpen/lijkbezorging/begrippen.md)

De ambtenaar van de burgerlijke stand geeft kosteloos het schriftelijk verlof tot begraving of crematie af, op grond van een verklaring van overlijden of een verklaring van geen bezwaar, en bewaart die stukken (Wet op de lijkbezorging art. 11–13).

#### [Burgerzaken](../../../onderwerpen/burgerzaken/begrippen.md)

Burgemeester en wethouders wijzen de ambtenaren aan; een van hen heeft de leiding van de dienst (BW 1 art. 16; Besluit burgerlijke stand art. 2). De ambtenaar neemt de akten en latere vermeldingen op in de registers van geboorten, huwelijken, geregistreerde partnerschappen en overlijden, houdt de registers bij en geeft afschriften en uittreksels af; hij voltrekt huwelijken, registreert partnerschappen, neemt erkenningen en naamskeuzes op en weigert een akte bij ongenoegzame bescheiden of strijd met de openbare orde (BW 1 art. 16a, 18c, 23, 63, 80a, 203; Besluit burgerlijke stand art. 5).

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (kern ja).

### Plaats in de indelingen

- **Doelgroep**: gemeente.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: hoedanigheid. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Verlenen verlof tot begraving of crematie](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlenen-verlof-tot-begraving-of-crematie.md), [Bijhouden burgerlijke stand](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-burgerlijke-stand.md), [Opmaken akte van overlijden](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-overlijden.md), [Verstrekken uittreksels en verklaringen burgerlijke stand](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-uittreksels-en-verklaringen-burgerlijke-stand.md), [Opmaken geboorteakte](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-geboorteakte.md), [Opmaken akte levenloos geboren kind](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-levenloos-geboren-kind.md), [Opmaken akte van erkenning](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-erkenning.md), [Toevoegen latere vermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/toevoegen-latere-vermelding.md), [Opmaken akte van naamskeuze](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-naamskeuze.md), [Wijzigen geslachtsvermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/wijzigen-geslachtsvermelding.md), [Voltrekken huwelijk](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/voltrekken-huwelijk.md), [Registreren partnerschap](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/registreren-partnerschap.md), [Inschrijven ontbinding huwelijk of partnerschap](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ontbinding-huwelijk-of-partnerschap.md). |

### Specialisaties

- **Buitengewoon ambtenaar van de burgerlijke stand**: Ambtenaar met een beperkter takenpakket, zoals het voltrekken van huwelijken en registreren van partnerschappen; ook voor één dag aangewezen op verzoek van het bruidspaar (BW 1 art. 16, 16a lid 2). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Ambtenaar van de burgerlijke stand | verleent *toewijzing* | [Verlenen verlof tot begraving of crematie](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlenen-verlof-tot-begraving-of-crematie.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 11) |
| Ambtenaar van de burgerlijke stand | houdt de registers bij *toewijzing* | [Bijhouden burgerlijke stand](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-burgerlijke-stand.md) | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) (BW 1 art. 16a; Besluit art. 5) |
| Ambtenaar van de burgerlijke stand | maakt akte op *toewijzing* | [Opmaken akte van overlijden](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-overlijden.md) | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19f) |
| Ambtenaar van de burgerlijke stand | geeft af *toewijzing* | [Verstrekken uittreksels en verklaringen burgerlijke stand](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-uittreksels-en-verklaringen-burgerlijke-stand.md) | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) (BW 1 art. 19k, 23; Besluit art. 26) |
| Ambtenaar van de burgerlijke stand | maakt akte op *toewijzing* | [Opmaken geboorteakte](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-geboorteakte.md) | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19) |
| Ambtenaar van de burgerlijke stand | maakt akte op *toewijzing* | [Opmaken akte levenloos geboren kind](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-levenloos-geboren-kind.md) | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19i) |
| Ambtenaar van de burgerlijke stand | maakt akte op *toewijzing* | [Opmaken akte van erkenning](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-erkenning.md) | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 203) |
| Ambtenaar van de burgerlijke stand | voegt toe *toewijzing* | [Toevoegen latere vermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/toevoegen-latere-vermelding.md) | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 20) |
| Ambtenaar van de burgerlijke stand | maakt akte op *toewijzing* | [Opmaken akte van naamskeuze](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-naamskeuze.md) | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 5) |
| Ambtenaar van de burgerlijke stand | voegt latere vermelding toe *toewijzing* | [Wijzigen geslachtsvermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/wijzigen-geslachtsvermelding.md) | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 28b) |
| Ambtenaar van de burgerlijke stand | voltrekt, ontvangt kennisgeving *toewijzing* | [Voltrekken huwelijk](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/voltrekken-huwelijk.md) | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 63; art. 44) |
| Ambtenaar van de burgerlijke stand | maakt akte op, ontvangt kennisgeving *toewijzing* | [Registreren partnerschap](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/registreren-partnerschap.md) | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 80a lid 3, 80g; art. 44) |
| Ambtenaar van de burgerlijke stand | schrijft in *toewijzing* | [Inschrijven ontbinding huwelijk of partnerschap](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ontbinding-huwelijk-of-partnerschap.md) | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 80c lid 2, 163) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [Ondernemersplein Aangifte overlijden](../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) | Aangifte en akte van overlijden (Ondernemersplein) |
| [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [Besluit burgerlijke stand 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) | Besluit burgerlijke stand 1994 |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.
