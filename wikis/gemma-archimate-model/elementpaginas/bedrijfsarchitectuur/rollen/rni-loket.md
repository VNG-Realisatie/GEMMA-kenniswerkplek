---
id: rni-loket
type: rol
archimate_type: business-role
status: goedgekeurd
naam: RNI-loket
onderwerpen:
- burgerzaken
definitie: Verantwoordelijkheid van een daartoe aangewezen gemeente om personen in de registratie niet-ingezetenen in te schrijven en hun gegevens te verstrekken.
match:
  gemma: geen
data_object: nee
doelgroep: gemeente
bronnen:
- 2026-rvig-hup-achtergronden-en-begrippen
- 2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven
- 2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp
- 2026-rijk-wet-brp-bwbr0033715
- 2026-rijk-besluit-brp-bwbr0034306
- 2026-nederlandwereldwijd-rni-hoe-kan-ik-mij-inschrijven
---

# RNI-loket

<!-- Gegenereerd door tools/render.py uit de beoordeling rni-loket.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Verantwoordelijkheid van een daartoe aangewezen gemeente om personen in de registratie niet-ingezetenen in te schrijven en hun gegevens te verstrekken.

### Beschrijving

Niet elke gemeente is RNI-loket; wie niet bij een loket terecht kan, gaat naar een ander loket (Utrecht RNI). Het college van het RNI-loket is bevoegd schriftelijk gegevens over niet-ingezetenen te verstrekken; andere gemeenten sturen zulke verzoeken door (NVVB Schema). De minister van BZK is verantwoordelijk voor de RNI (HUP Achtergronden). Het RNI-loket is een verantwoordelijkheid, geen kanaal.

De RNI is een taak van de minister: hij schrijft in en houdt daarvoor inschrijfvoorzieningen in stand, waar de persoon in persoon verschijnt (Wet BRP art. 2.64, 2.66, 2.67 lid 3). Een RNI-loket is de gemeente waar zo'n inschrijfvoorziening is ondergebracht (Besluit BRP art. 36); welke gemeenten dat zijn, regelt de wet niet. In 2026 zijn het er 19: Alkmaar, Almelo, Amsterdam, Breda, Den Haag, Doetinchem, Eindhoven, Goes, Groningen, Heerlen, Leeuwarden, Leiden, Nijmegen, Rotterdam, Terneuzen, Utrecht, Venlo, Westland en Zwolle; wie geen Nederlandse of EU/EER- of Zwitserse nationaliteit heeft, kan alleen in Breda en Venlo terecht (Nederland Wereldwijd RNI). Daarnaast schrijven aangewezen bestuursorganen zoals de Belastingdienst, de SVB en DUO in (Wet BRP art. 2.68; Nederland Wereldwijd RNI).

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
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Inschrijven niet-ingezetene](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-niet-ingezetene.md), [Verstrekken persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-persoonsgegevens.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| RNI-loket | schrijft in *toewijzing* | [Inschrijven niet-ingezetene](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-niet-ingezetene.md) | [Utrecht RNI inschrijven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (Inschrijven RNI; Wet BRP art. 2.66, 2.67 lid 3) |
| RNI-loket | verstrekt gegevens over niet-ingezetenen *toewijzing* | [Verstrekken persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-persoonsgegevens.md) | [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (Niet-ingezetenen; Wet BRP art. 2.79, 3.19 lid 2) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Besluit basisregistratie personen](../../motivatie/beleidskaders/rijksregelgeving/besluit-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | RNI-loket | [Besluit BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) (art. 36 (de gemeente waar de inschrijfvoorziening is ondergebracht)) |
| [Gemeente](../actoren/gemeente.md) | vervult *toewijzing* | RNI-loket | [Utrecht RNI inschrijven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven.md) (Inschrijven RNI) |
| [Wet basisregistratie personen](../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | RNI-loket | [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 2.64, 2.67 lid 3, 2.79) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md) | HUP BRP: Achtergronden en begrippen |
| [Utrecht RNI inschrijven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven.md) | Gemeente Utrecht: Registratie niet-ingezetenen (RNI) |
| [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md) | Schema verzoeken om schriftelijke gegevensverstrekking uit de BRP |
| [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |
| [Besluit BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) | Besluit basisregistratie personen |
| [Nederland Wereldwijd RNI inschrijven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-nederlandwereldwijd-rni-hoe-kan-ik-mij-inschrijven.md) | Hoe kan ik mij inschrijven in de RNI? |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen rol voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 23](../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (grondslag, open): **UPL:** de UPL noemt RNI-inschrijving als product van de gemeente, met grondslag art. 2.66 Wet BRP ([2025-vng-upl-producten-en-diensten-extern](../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), nr. 369). **Bevinding:** de inschrijving in de RNI is een taak van de minister van BZK. De persoon verschijnt bij een inschrijfvoorziening van de minister ([2026-rijk-wet-brp-bwbr0033715](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), art. 2.64, 2.66, 2.67 lid 3); het Besluit BRP spreekt van de gemeente waar de inschrijfvoorziening is ondergebracht ([2026-rijk-besluit-brp-bwbr0034306](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md), art. 36). Welke gemeenten dat zijn, staat niet in de wet, het besluit of de regeling. Alleen een informatiepagina noemt de 19 gemeenten ([2026-nederlandwereldwijd-rni-hoe-kan-ik-mij-inschrijven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-nederlandwereldwijd-rni-hoe-kan-ik-mij-inschrijven.md)). Het product geldt dus niet voor alle gemeenten. GEMMA modelleert het als de rol RNI-loket met het proces Inschrijven niet-ingezetene, net als de reisdocumenten voor niet-ingezetenen bij aangewezen gemeenten. **Voorstel:** vermeld bij het UPL-product dat alleen gemeenten met een RNI-loket het leveren, en verwijs naar de grondslag van de loketten (de afspraak of aanwijzing door de minister), zodat gemeenten zonder loket het product niet hoeven aan te bieden.
