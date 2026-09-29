---
name: gemma-archimate-model-criteria
description: De criteria van deze wiki voor de vraag of een begrip een ArchiMate-element is en van welk type (bedrijfsobject, contract, product, dienst, proces, functie, gebeurtenis, actor, rol). Laad deze skill bij elke beoordeling van een begrip, vóór er een elementpagina wordt voorgesteld.
metadata:
  kind: capability
  scope: wiki
  requires-tools: "python:tools/bepaal_type.py"
  reads: "bronanalyse"
  writes: "beoordeling"
---

# Criteria: is dit begrip een ArchiMate-element, en welk?

Deze skill is de enige plek waar staat wanneer een begrip een element van dit model wordt. Ze beschrijft alleen *wat* het begrip is. Hoe je het daarna vastlegt (GGM-match, naam, definitie, relaties) staat in `gemma-archimate-model-write`.

## Kenmerk en criterium

- Een **kenmerk** is een neutrale eigenschap van het begrip zelf, bijvoorbeeld *onderscheidbare exemplaren*. Je beantwoordt het met ja of nee, met een onderbouwing en de bron-id's waarop die steunt. Een kenmerk oordeelt niet over het type.
- Een **criterium** is een regel in de beslistabel hieronder: welke combinatie van kenmerken tot welk type leidt. De tool `tools/bepaal_type.py` past de criteria toe; jij beoordeelt ze niet los.

Zo beantwoord je alle kenmerken **één keer, tegelijk**. Je kiest dus niet eerst een type om daarna te toetsen of het klopt. Het type is de uitkomst.

## Werkwijze

1. Beantwoord **alle** kenmerken uit de tabel voor het begrip, ook als ze voor de hand liggend lijken. Gebruik de bronnen in de volgorde van de bronvoorrang (wet → informatiemodel → beleid → overig).
2. Vul waar nodig de extra velden in:
   - `genoemd_begrip` bij *slechts eigenschap* of *waarneembare vorm*;
   - `archimate_buiten_model` bij *buiten kernlagen*;
   - `benoemde_partij` (ja/nee) als zowel *handelende partij* als *hoedanigheid* ja is.
3. Leg de beoordeling vast volgens `schemas/beoordeling.schema.json` en draai `uv run python tools/bepaal_type.py evalueer <bestand> --schrijf`. De uitkomst is bindend.
4. Is de uitkomst `conflict` of staat `voorleggen` aan, dan leg je het begrip voor aan de redacteur, met de redenen uit de uitkomst. Pas je antwoorden niet aan om een conflict weg te werken, tenzij een antwoord aantoonbaar fout was.

## ArchiMate-typen in dit model

Definities volgens ArchiMate 3.2 (Engels), met de duiding voor gemeenten. "Herkend" betekent: de tool herkent het type, maar deze wiki heeft er nog geen paginatype voor; het begrip wordt voorgelegd.

| ArchiMate-type | Paginatype | Definitie | Duiding |
|---|---|---|---|
| Business Object | `bedrijfsobject` | A concept used within a particular business domain. | Een ding waar de gemeente mee werkt: het wordt gebruikt, gemaakt of gewijzigd door gemeentelijk gedrag. |
| Contract | `bedrijfsobject` (`archimate_type: contract`) | A formal or informal specification of an agreement between a provider and a consumer that specifies the rights and obligations associated with a product. | Een tweezijdige afspraak (overeenkomst, convenant). Een besluit of verordening is géén contract. |
| Product | `product` | A coherent collection of services and/or passive structure elements, accompanied by a contract/set of agreements, which is offered as a whole to customers. | Wat de gemeente als geheel aanbiedt, met voorwaarden (bijv. uit de productencatalogus). |
| Business Service | `bedrijfsdienst` | Explicitly defined behavior that a business role, actor or collaboration exposes to its environment. | Wat een afnemer van de gemeente kan krijgen, los van hoe het wordt uitgevoerd. |
| Business Process | `bedrijfsproces` | A sequence of business behaviors that achieves a specific result. | Wordt per keer doorlopen en levert een resultaat op (besluit, product). |
| Business Function | `bedrijfsfunctie` | A collection of business behavior based on a chosen set of criteria (typically required business resources and/or competencies). | Doorlopende groepering van gedrag. Niet "wat de gemeente kan": dat is een vermogen (Capability). |
| Business Event | `bedrijfsgebeurtenis` | A business behavior element that denotes an organizational state change. | Ogenblikkelijk voorval dat gedrag start of afsluit (verhuizing, aanvraag ontvangen). |
| Business Actor | `actor` | A business entity that is capable of performing behavior. | Persoon, organisatie of eenheid, ook extern of generiek (inwoner). |
| Business Role | `rol` | The responsibility for performing specific behavior, to which an actor can be assigned, or the part an actor plays in a particular action or event. | Verantwoordelijkheid of hoedanigheid (aanvrager, belastingplichtige, heffingsambtenaar). |
| Business Collaboration | herkend | An aggregate of two or more business internal active structure elements that work together to perform collective behavior. | Samenwerkingsverband. |
| Business Interaction | herkend | A unit of collective business behavior performed by two or more business actors, roles or collaborations. | Gezamenlijk gedrag (keukentafelgesprek, zitting). |
| Business Interface | herkend | A point of access where a business service is made available to the environment. | Loket, website, kanaal. |
| Representation | herkend | A perceptible form of the information carried by a business object. | Document, formulier, bericht (aanslagbiljet). |
| Location | herkend | A conceptual or physical place or position where concepts are located or performed. | Fysieke plaats als zodanig; een gebiedsindeling als gegevensconcept is een bedrijfsobject. |
| Data Object (applicatielaag) | annotatie `data_object` | Data structured for automated processing. | Voorbereiding op `applicatiearchitectuur/`; hier alleen als signaal. |

Buiten dit model vallen de motivatie- en strategielaag (Goal, Outcome, Driver, Principle, Requirement, Constraint, Value, Capability) en Grouping (thema). Dat zijn ArchiMate-elementen, maar deze wiki modelleert ze niet. Een losse norm uit een wet is een Requirement of Constraint; de regeling als geheel is een bedrijfsobject (grondslag governance-object).

<!-- BEGIN gegenereerd door: uv run python tools/bepaal_type.py markdown — niet met de hand bewerken -->
### Kenmerken

**Scope**

| Kenmerk | Vraag | Herkomst | Voorbeeld | Tegenvoorbeeld |
|---|---|---|---|---|
| herkenbaar | Kennen domeinexperts dit als eigen begrip binnen het onderwerp? | ArchiMate (concept in een domein) + GEMMA | Omgevingsvergunning | Technisch volgnummer van een dossierregel |
| gemeentelijk | Ziet, doet of beslist de gemeente hierover, of werkt zij rechtstreeks samen met deze partij? | GEMMA | Parkeervergunning; GGD (directe samenwerking) | Interne werkvoorraad van het UWV |
| buiten kernlagen | Is het een thema, doel, waarde, drijfveer, principe, losse norm of eis, of een vermogen? Noem welk ArchiMate-type | ArchiMate (motivatie-, strategie- en overige lagen) | Armoedebestrijding (doel); leefbaarheid (waarde); 'binnen 8 weken beslissen' (norm) | Bijstandsuitkering |

**Afhankelijkheid**

| Kenmerk | Vraag | Herkomst | Voorbeeld | Tegenvoorbeeld |
|---|---|---|---|---|
| slechts eigenschap | Is het alleen een eigenschap, status, waarde of indeling van één ander begrip? Noem dat begrip | GEMMA | Bouwjaar (van Pand); status van een aanvraag | Pand |

**Aard**

| Kenmerk | Vraag | Herkomst | Voorbeeld | Tegenvoorbeeld |
|---|---|---|---|---|
| gedrag | Beschrijft het iets wat gedaan wordt of gebeurt, en niet een ding, partij of plaats? | ArchiMate (gedragselement) | Aanvraag behandelen; verhuizing | Aanvraag |
| handelende partij | Is het een persoon, organisatie of organisatie-eenheid (ook extern of generiek) die zelf kan handelen? | ArchiMate Business Actor | College van B&W; inwoner; woningcorporatie | Aanvrager |
| hoedanigheid | Is het een verantwoordelijkheid waaraan een partij wordt toegewezen, of de hoedanigheid waarin een partij optreedt in een handeling of gebeurtenis? | ArchiMate Business Role | Aanvrager; belastingplichtige; heffingsambtenaar | Gemeenteraad |
| samenwerkingsverband | Is het een verband van twee of meer partijen dat samen gedrag uitvoert? | ArchiMate Business Collaboration | Zorg- en Veiligheidshuis; samenwerkingsverband passend onderwijs | GGD |
| toegangspunt | Is het een punt waarlangs een dienst beschikbaar komt (loket, website, telefoonnummer, kanaal)? | ArchiMate Business Interface | Publieksbalie; gemeentelijke website | Klantcontact |
| plaats | Is het een fysieke plaats als zodanig, en niet een gebiedsindeling als gegevensconcept? | ArchiMate Location | Stadskantoor als vestigingsplaats | Wijk (gebiedsindeling) |
| aanbod als geheel | Is het een samenhangend pakket van diensten en/of objecten dat met voorwaarden als geheel aan afnemers wordt aangeboden? | ArchiMate Product | Bewonersparkeervergunning zoals aangeboden in de productencatalogus | Parkeren |

**Soort gedrag**

| Kenmerk | Vraag | Herkomst | Voorbeeld | Tegenvoorbeeld |
|---|---|---|---|---|
| per keer doorlopen | Is het een reeks activiteiten die per keer wordt doorlopen en een benoembaar resultaat oplevert? | ArchiMate Business Process | Aanvraag omgevingsvergunning behandelen | Vergunningverlening |
| gegroepeerd gedrag | Is het een doorlopende groepering van gedrag, ingedeeld naar benodigde kennis of middelen, zonder eigen volgorde of doorlooptijd? (Niet: 'wat de gemeente kan'; dat is een vermogen) | ArchiMate Business Function | Vergunningverlening; belastingheffing | Aanslag opleggen |
| toestandsverandering | Is het een ogenblikkelijke toestandsverandering die gedrag start of afsluit, van binnen of buiten de gemeente? | ArchiMate Business Event | Verhuizing; aanvraag ontvangen; beslistermijn verstreken | Verhuizing doorgeven |
| aangeboden gedrag | Is het expliciet beschreven gedrag dat aan de omgeving wordt aangeboden, vanuit de waarde voor de afnemer en los van hoe het wordt uitgevoerd? | ArchiMate Business Service | Melding openbare ruimte doen | Melding afhandelen |
| gezamenlijk gedrag | Is het gedrag dat alleen door twee of meer partijen samen wordt uitgevoerd? | ArchiMate Business Interaction | Keukentafelgesprek; hoorzitting bezwaarcommissie | Beschikking opstellen |

**Passief**

| Kenmerk | Vraag | Herkomst | Voorbeeld | Tegenvoorbeeld |
|---|---|---|---|---|
| eigen identiteit | Bestaat het zelfstandig, niet alleen als onderdeel van één ander ding? | GEMMA | Beschikking | Ondertekening van een besluit |
| onderscheidbare exemplaren | Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | GEMMA | Aanvraag (elke aanvraag apart) | Gemeentefonds (er is er één) |
| levenscyclus | Ontstaan, veranderen en eindigen de exemplaren? | GEMMA | Vergunning (verleend, gewijzigd, ingetrokken) | Kadastrale gemeentecode |
| wordt bewerkt | Wordt het door gemeentelijk gedrag gebruikt, gemaakt of gewijzigd (behandeld, besloten, geleverd)? | ArchiMate (access-relatie) | Aanvraag (ontvangen, beoordeeld) | Begrip dat in geen enkel gemeentelijk gedrag voorkomt |
| afspraak | Is het een tweezijdige afspraak met rechten en plichten, en geen eenzijdig besluit of regeling? | ArchiMate Contract | Subsidieovereenkomst; convenant | Subsidiebeschikking (eenzijdig); verordening |
| waarneembare vorm | Is het de vorm (document, formulier, bericht) waarin informatie van een ander begrip wordt overgebracht? Noem dat begrip | ArchiMate Representation | Aanslagbiljet (vorm van Aanslag); aanvraagformulier | Aanslag |
| geautomatiseerd verwerkt | Is het een gegevensstructuur voor geautomatiseerde verwerking? | ArchiMate Data Object (applicatielaag) | Zaak in het zaaksysteem | Keukentafelgesprek |

### Beslistabel (= de criteria)

Van boven naar beneden; de eerste passende regel beslist. Daarna gelden de aanvullingen.

| Nr | Stap | Als | Dan |
|---|---|---|---|
| 1 | 1 Scope | niet *herkenbaar* of niet *gemeentelijk* | buiten scope, met reden |
| 2 | 1 Scope | *buiten kernlagen* | buiten dit model, met het ArchiMate-type (Goal, Driver, Capability …) |
| 3 | 2 Afhankelijk | *slechts eigenschap* | eigenschap of specialisatie zonder pagina van het genoemde begrip |
| 4 | 3 Aard | *handelende partij* én *hoedanigheid* (verder geen aard) | Actor als het een benoemde persoon/organisatie/eenheid is, anders Rol |
| 5 | 3 Aard | meer dan één aard (behalve actor + rol) | conflict: voorleggen |
| 6 | 3 Aard | *handelende partij* | Business Actor |
| 7 | 3 Aard | *hoedanigheid* | Business Role |
| 8 | 3 Aard | *aanbod als geheel* | Product |
| 9 | 3 Aard | *samenwerkingsverband* | Business Collaboration: herkend, voorleggen |
| 10 | 3 Aard | *toegangspunt* | Business Interface: herkend, voorleggen |
| 11 | 3 Aard | *plaats* | Location: herkend, voorleggen |
| 12 | 4 Gedrag | *gedrag* en precies één van *per keer doorlopen* / *gegroepeerd gedrag* / *toestandsverandering* / *aangeboden gedrag* / *gezamenlijk gedrag* | Business Process / Function / Event / Service / Interaction (Interaction: herkend, voorleggen) |
| 13 | 4 Gedrag | *gedrag*, maar geen of meer dan één soort gedrag | conflict: voorleggen |
| 14 | 5 Passief | geen aard, maar wel een soort gedrag | conflict: voorleggen (tegenstrijdige antwoorden) |
| 15 | 5 Passief | *waarneembare vorm* | Representation van het genoemde begrip: herkend, voorleggen |
| 16 | 5 Passief | *eigen identiteit* + *onderscheidbare exemplaren* + *wordt bewerkt* + *afspraak* | Contract |
| 17 | 5 Passief | *eigen identiteit* + *onderscheidbare exemplaren* + *wordt bewerkt* | Business Object (een wet of verordening als geheel: grondslag governance-object) |
| 18 | 5 Passief | één van *eigen identiteit*, *onderscheidbare exemplaren*, *wordt bewerkt* ontbreekt | geen element; noem het ontbrekende kenmerk |

**Aanvullingen**

| Stap | Als | Dan |
|---|---|---|
| Na regel 16/17 | geen *levenscyclus* | voorleggen |
| 6 Tegenhanger | Actor of Rol met *onderscheidbare exemplaren* + *levenscyclus* + *wordt bewerkt* | ook een bedrijfsobjectpagina (tegenhanger); bij gedrag nooit: het resultaat is dan een apart begrip |
| 7 Annotatie | *geautomatiseerd verwerkt* | `data_object: ja` (voedt het hiaat-signaal richting GGM) |
<!-- EINDE gegenereerd -->

## Scope

- **Gemeentelijk perspectief.** Alleen wat de gemeente ziet, doet of beslist, of een partij waarmee zij rechtstreeks samenwerkt. Een ketenpartner (UWV, IND, COA, GGD …) krijgt een actorpagina als de gemeente er direct mee samenwerkt, opdracht aan geeft of gegevens mee uitwisselt. De interne processen en rollen van die partner blijven buiten scope.
- **Een begrip met uitkomst "geen element"** wordt niet weggelaten: het blijft in de begrippenlijst van het onderwerp staan, met de uitkomst en de reden.

## Anti-patronen

Deze argumenten tellen **nooit** mee, ook niet impliciet of als synoniem:
- registreren of registreerbaar zijn ("wat de gemeente registreert", "registratieobject");
- eigendom ("eigendom ligt bij X"), systeembeheer, "regie, niet registratie", "extern systeem".

Het kenmerk *geautomatiseerd verwerkt* is de enige plek waar gegevensvastlegging meetelt, en alleen als annotatie (`data_object`): het bepaalt nooit of iets een element is.

## Begripstype en entiteitstype

De uitkomst van de beslistabel typeert een **begrip uit een bron** ("wat is het?"). Een GGM-entiteit heeft daarnaast een eigen classificatie (entiteitstype, bij de dekkingsanalyse van het GGM). Die twee zijn niet uitwisselbaar: een GGM-entiteit is geen begrip en wordt pas via een bron beoordeeld.
