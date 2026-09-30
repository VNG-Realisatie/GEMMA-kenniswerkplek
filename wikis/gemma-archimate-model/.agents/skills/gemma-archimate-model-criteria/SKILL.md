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

1. Beantwoord **alle** kenmerken uit de tabel voor het begrip, ook als ze voor de hand liggend lijken of niet bij het vermoedelijke type horen (een passief begrip krijgt *los van verantwoordelijkheid*: nee). Gebruik de bronnen in de volgorde van de bronvoorrang (wet → informatiemodel → beleid → overig).
2. Let bij de kenmerken die de oude criteria dragen op het volgende:
   - *relaties*: noem in de onderbouwing de concrete relaties uit de `## Relaties` van de bronanalyses (werkwoord en ander begrip). Staat er geen, dan is het antwoord nee, ook als je een relatie vermoedt; vul dan eerst de bronanalyse aan.
   - *zelfstandig beleidsbegrip*: kijk eerst naar boven. Zoek de generalisaties in de wiki, het GGM (`tools/ggm.py generalisaties`, `naamgenoten`) en het GEMMA-model (`tools/gemma.py zoek`) en noteer de keten (bijv. Besluit → Beschikking → Vergunning → Vergunning tot opgraving). Nee als het begrip een variant is van een breder begrip dat domeinexperts herkennen; zie `gemma-archimate-model-assess` §3.
   - *Gedrag* (toegewezen partij, gebruikt objecten, aanleiding, benoembaar resultaat, herhaald uitgevoerd, eigen normering, stabiel over tijd): beantwoord ze bij elk gedragsbegrip met de concrete partij, objecten, aanleiding of regels uit de bronnen; bij een begrip dat geen gedrag is zijn ze nee. Bij proces en functie vervangen *toegewezen partij* en *gebruikt objecten* in de drempel het brede kenmerk *relaties*: een losse associatie volstaat daar niet. Een werkvorm zonder eigen objecten, aanleiding of regels (burgerberaad) haalt de drempel voor een proces dan niet.
   - *los van verantwoordelijkheid*: de vraag van de oude actor- en roltoets "blijft het bestaan als zijn verantwoordelijkheden veranderen, en kan het ook andere rollen vervullen?". Ja maakt een partij tot actor, nee tot rol.
   - De oude rolvraag "kan één actor meerdere van deze rollen vervullen?" is vervallen: ze onderscheidt niet (vrijwel altijd ja).
   - Een doelgroep (minima, jongeren) is geen actor of rol maar een indeling van een actor: *slechts eigenschap* ja, met de actor als `genoemd_begrip`.
3. Vul waar nodig de extra velden in:
   - `genoemd_begrip` bij *slechts eigenschap*, *eigen identiteit* nee (het geheel of het proces waarvan het een deel is), *zelfstandig beleidsbegrip* nee (het bredere begrip) of *waarneembare vorm*;
   - `archimate_buiten_model` bij *buiten kernlagen*.
4. Leg de beoordeling vast volgens `schemas/beoordeling.schema.json` en draai `uv run python tools/bepaal_type.py evalueer <bestand> --schrijf`. De uitkomst is bindend.
5. Is de uitkomst `conflict` of staat `voorleggen` aan, dan leg je het begrip voor aan de redacteur, met de redenen uit de uitkomst. Pas je antwoorden niet aan om een conflict weg te werken, tenzij een antwoord aantoonbaar fout was.

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
| herkenbaar | Kennen domeinexperts dit als eigen begrip? | ArchiMate (concept in een domein) + GEMMA (BO-criterium herkenbaar voor domeinexperts) | Omgevingsvergunning | Technisch volgnummer van een dossierregel |
| gemeentelijk | Ziet, doet of beslist de gemeente hierover? Bij een externe partij: werkt de gemeente er structureel mee samen (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht), en is zij meer dan context? | GEMMA (gemeentelijk perspectief; ketenpartners alleen als context) | Parkeervergunning; GGD (gemeenschappelijke regeling) | Interne werkvoorraad van het UWV; behandelend arts |
| buiten kernlagen | Is het een thema, doel, waarde, drijfveer, principe, losse norm of eis, of een vermogen? Noem welk ArchiMate-type | ArchiMate (motivatie-, strategie- en overige lagen) | Armoedebestrijding (doel); leefbaarheid (waarde); 'binnen 8 weken beslissen' (norm) | Bijstandsuitkering |

**Zelfstandigheid**

| Kenmerk | Vraag | Herkomst | Voorbeeld | Tegenvoorbeeld |
|---|---|---|---|---|
| betekenis in onderwerp | Speelt het in dit onderwerp een eigen rol, en niet alleen als terloopse vermelding of als begrip dat primair bij een ander onderwerp hoort? | GEMMA (BO-criterium betekenis binnen het onderwerp) | Graf (lijkbezorging) | Akte van overlijden (hoort bij de burgerlijke stand) |
| slechts eigenschap | Is het alleen een eigenschap, status, waarde, classificatie of indeling (ook een doelgroep) van één ander begrip? Noem dat begrip | GEMMA (negatieve toets: eigenschap, status, classificatie) | Bouwjaar (van Pand); status van een aanvraag; minima (indeling van Inwoner) | Pand |
| eigen identiteit | Bestaat het zelfstandig, en niet alleen als onderdeel of deelstap van één ander begrip? Noem dat begrip | GEMMA (BO-criterium eigen bestaan; actorvraag eigen identiteit) | Beschikking; uitgifte van een graf | Ondertekening van een besluit (deelstap) |
| relaties | Heeft het in de bronnen aanwijsbare relaties met andere begrippen? Bij een partij: gedrag dat zij uitvoert en objecten die zij houdt of beheert. Noem ze in de onderbouwing | GEMMA (BO-criterium relaties; actor- en rolvragen toewijsbaar aan gedrag, gekoppeld aan taken) | Kerkgenootschap (houdt een bijzondere begraafplaats) | Begrip dat alleen in een opsomming voorkomt |
| zelfstandig beleidsbegrip | Herkent de gemeente dit als apart soort ding naast zijn generalisatie, met eigen gegevens of een eigen behandeling, op het detailniveau van GEMMA? Nee als het een variant is van een breder herkenbaar begrip; noem dat begrip | GEMMA (beslisvraag: zelfstandig ding waar beleid op gemaakt wordt) | Omgevingsvergunning; parkeervergunning | Vergunning tot opgraving (variant van een vergunning) |

**Aard**

| Kenmerk | Vraag | Herkomst | Voorbeeld | Tegenvoorbeeld |
|---|---|---|---|---|
| gedrag | Beschrijft het iets wat gedaan wordt of gebeurt, en niet een ding, partij of plaats? | ArchiMate (gedragselement) | Aanvraag behandelen; verhuizing | Aanvraag |
| handelende partij | Is het een persoon, organisatie of organisatie-eenheid (ook extern of generiek) die zelf kan handelen? | ArchiMate Business Actor (actorvragen zelfstandig gedrag; persoon, organisatie of eenheid) | College van B&W; inwoner; woningcorporatie | Aanvrager |
| hoedanigheid | Is het een verantwoordelijkheid waaraan een partij wordt toegewezen, of de hoedanigheid waarin een partij optreedt in een handeling of gebeurtenis? | ArchiMate Business Role (rolvragen verantwoordelijkheid; actor toewijsbaar) | Aanvrager; belastingplichtige; heffingsambtenaar | Gemeenteraad |
| samenwerkingsverband | Is het een verband van twee of meer partijen dat samen gedrag uitvoert? | ArchiMate Business Collaboration | Zorg- en Veiligheidshuis; samenwerkingsverband passend onderwijs | GGD |
| toegangspunt | Is het een punt waarlangs een dienst beschikbaar komt (loket, website, telefoonnummer, kanaal)? | ArchiMate Business Interface | Publieksbalie; gemeentelijke website | Klantcontact |
| plaats | Is het een fysieke plaats als zodanig, en niet een gebiedsindeling als gegevensconcept? | ArchiMate Location | Stadskantoor als vestigingsplaats | Wijk (gebiedsindeling) |
| aanbod als geheel | Is het een samenhangend pakket van diensten en/of objecten dat met voorwaarden als geheel aan afnemers wordt aangeboden? | ArchiMate Product | Bewonersparkeervergunning zoals aangeboden in de productencatalogus | Parkeren |

**Partij**

| Kenmerk | Vraag | Herkomst | Voorbeeld | Tegenvoorbeeld |
|---|---|---|---|---|
| los van verantwoordelijkheid | Bestaat de partij los van de taak of verantwoordelijkheid die zij hier heeft, zodat zij ook andere rollen kan vervullen? Ja: actor; nee: rol. Nee als het geen partij of verantwoordelijkheid is | ArchiMate Actor/Role (actorvragen meerdere rollen, blijft bestaan als verantwoordelijkheden veranderen; rolvraag geen eigen identiteit) | Kerkgenootschap; burgemeester | Houder van de begraafplaats |
| meerdere vervullers | Kan deze verantwoordelijkheid door verschillende partijen worden vervuld? Nee als het geen verantwoordelijkheid is | ArchiMate Business Role (rolvraag door meerdere actoren vervulbaar) | Houder van de begraafplaats (gemeente of kerkgenootschap) | Burgemeester |

**Soort gedrag**

| Kenmerk | Vraag | Herkomst | Voorbeeld | Tegenvoorbeeld |
|---|---|---|---|---|
| per keer doorlopen | Is het een reeks activiteiten die per keer wordt doorlopen en een benoembaar resultaat oplevert? | ArchiMate Business Process | Aanvraag omgevingsvergunning behandelen | Vergunningverlening |
| gegroepeerd gedrag | Is het een doorlopende groepering van gedrag, ingedeeld naar benodigde kennis of middelen, zonder eigen volgorde of doorlooptijd? (Niet: 'wat de gemeente kan'; dat is een vermogen) | ArchiMate Business Function | Vergunningverlening; belastingheffing | Aanslag opleggen |
| toestandsverandering | Is het een ogenblikkelijke toestandsverandering die gedrag start of afsluit, van binnen of buiten de gemeente? | ArchiMate Business Event | Verhuizing; aanvraag ontvangen; beslistermijn verstreken | Verhuizing doorgeven |
| aangeboden gedrag | Is het expliciet beschreven gedrag dat aan de omgeving wordt aangeboden, vanuit de waarde voor de afnemer en los van hoe het wordt uitgevoerd? | ArchiMate Business Service | Melding openbare ruimte doen | Melding afhandelen |
| gezamenlijk gedrag | Is het gedrag dat alleen door twee of meer partijen samen wordt uitgevoerd? | ArchiMate Business Interaction | Keukentafelgesprek; hoorzitting bezwaarcommissie | Beschikking opstellen |

**Gedrag**

| Kenmerk | Vraag | Herkomst | Voorbeeld | Tegenvoorbeeld |
|---|---|---|---|---|
| toegewezen partij | Is er een actor of rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? Noem die. Nee als het geen gedrag is | ArchiMate (assignment van actor of rol aan gedrag) | Ruiming (houder van de begraafplaats) | Draagvlak creëren (niemand aanwijsbaar) |
| gebruikt objecten | Leest, maakt of wijzigt het gedrag aanwijsbare bedrijfsobjecten? Noem ze. Nee als het geen gedrag is | ArchiMate (access van gedrag naar passief element) | Inspraak (ontwerpbesluit, zienswijze) | Burgerberaad (geen vast object) |
| aanleiding | Start het door een aanwijsbare gebeurtenis, verzoek of termijn? Noem die. Nee als het geen gedrag is | ArchiMate (triggering) + GEMMA (procesarchitectuur: een proces start bij een gebeurtenis) | Overheidsparticipatie (verzoek ingediend) | Kennisdeling |
| benoembaar resultaat | Levert het een concreet, benoembaar resultaat op (besluit, product, verslag, afspraak)? Nee als het geen gedrag is | ArchiMate Business Process (achieves a specific result) + GEMMA (proces levert product of besluit) | Opgraving (opgegraven lijk) | Informeren |
| herhaald uitgevoerd | Wordt het regelmatig en voor verschillende gevallen doorlopen, en is het geen eenmalig project? Nee als het geen gedrag is | GEMMA (proces als herhaalbare werkwijze; tegenhanger van onderscheidbare exemplaren) | Inspraak (per ontwerpbesluit) | Invoeren van de participatieverordening (eenmalig) |
| eigen normering | Gelden er eigen regels, termijnen of bevoegdheden voor, uit wet, verordening of beleidsregel? Noem ze. Nee als het geen gedrag is | GEMMA (proces met eigen spelregels; tegenhanger van levenscyclus) | Inspraak (afdeling 3.4 Awb) | Burgerberaad (vormvrij) |
| stabiel over tijd | Blijft deze groepering van gedrag bestaan als de organisatie-inrichting of werkwijze verandert? Nee als het geen gedrag is | ArchiMate Business Function (stabiel, los van de organisatie) + GEMMA (bedrijfsfunctiemodel) | Participatie; belastingheffing | Projectteam Omgevingswet |

**Passief**

| Kenmerk | Vraag | Herkomst | Voorbeeld | Tegenvoorbeeld |
|---|---|---|---|---|
| onderscheidbare exemplaren | Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | GEMMA (BO-criterium kan in meervoud bestaan) | Aanvraag (elke aanvraag apart) | Gemeentefonds (er is er één) |
| levenscyclus | Ontstaan, veranderen en eindigen de exemplaren? | GEMMA (BO-criterium eigen levenscyclus) | Vergunning (verleend, gewijzigd, ingetrokken) | Kadastrale gemeentecode |
| wordt bewerkt | Wordt het concreet door gemeentelijk gedrag gebruikt, gemaakt of gewijzigd (operationeel, en niet alleen beleidsmatig)? | ArchiMate (access-relatie) + GEMMA (abstractieniveau operationeel) | Aanvraag (ontvangen, beoordeeld) | Preventieakkoord (alleen beleidsmatig) |
| afspraak | Is het een tweezijdige afspraak met rechten en plichten, en geen eenzijdig besluit of regeling? | ArchiMate Contract | Subsidieovereenkomst; convenant | Subsidiebeschikking (eenzijdig); verordening |
| waarneembare vorm | Is het de vorm (document, formulier, bericht) waarin informatie van een ander begrip wordt overgebracht? Noem dat begrip | ArchiMate Representation | Aanslagbiljet (vorm van Aanslag); aanvraagformulier | Aanslag |
| geautomatiseerd verwerkt | Is het een gegevensstructuur voor geautomatiseerde verwerking? | ArchiMate Data Object (applicatielaag) | Zaak in het zaaksysteem | Keukentafelgesprek |

### Beslistabel (= de criteria)

Stap 1–3 van boven naar beneden: de eerste passende regel beslist en levert het einde of een voorlopig type op. Een voorlopig type met een paginatype gaat door naar stap 4 (drempel) en stap 5 (specialisatieniveau). Daarna gelden de aanvullingen.

| Nr | Stap | Als | Dan |
|---|---|---|---|
| 1 | 1 Scope | niet *herkenbaar* of niet *gemeentelijk* | buiten scope, met reden |
| 2 | 1 Scope | *buiten kernlagen* | buiten dit model, met het ArchiMate-type (Goal, Driver, Capability …) |
| 3 | 2 Afhankelijk | *slechts eigenschap* | eigenschap, status of indeling van het genoemde begrip; geen pagina |
| 4 | 2 Afhankelijk | niet *eigen identiteit* | onderdeel of deelstap van het genoemde begrip; geen pagina, relaties opgetild |
| 5 | 3 Aard | *handelende partij* én *hoedanigheid* (verder geen aard) | *los van verantwoordelijkheid* ja → Actor, nee → Rol |
| 6 | 3 Aard | meer dan één aard (behalve actor + rol) | conflict: voorleggen |
| 7 | 3 Aard | *handelende partij* | Actor; conflict als niet *los van verantwoordelijkheid* (mogelijk rol) |
| 8 | 3 Aard | *hoedanigheid* | Rol; conflict als *los van verantwoordelijkheid* (mogelijk actor) |
| 9 | 3 Aard | *aanbod als geheel* | Product |
| 10 | 3 Aard | *samenwerkingsverband* | Business Collaboration: herkend, voorleggen |
| 11 | 3 Aard | *toegangspunt* | Business Interface: herkend, voorleggen |
| 12 | 3 Aard | *plaats* | Location: herkend, voorleggen |
| 13 | 3 Gedrag | *gedrag* en precies één van *per keer doorlopen* / *gegroepeerd gedrag* / *toestandsverandering* / *aangeboden gedrag* / *gezamenlijk gedrag* | Business Process / Function / Event / Service / Interaction (Interaction: herkend, voorleggen) |
| 14 | 3 Gedrag | *gedrag*, maar geen of meer dan één soort gedrag | conflict: voorleggen |
| 15 | 3 Passief | geen aard, maar wel een soort gedrag | conflict: voorleggen (tegenstrijdige antwoorden) |
| 16 | 3 Passief | *waarneembare vorm* | Representation van het genoemde begrip: herkend, voorleggen |
| 17 | 3 Passief | *afspraak* | Contract |
| 18 | 3 Passief | overig passief begrip | Business Object (een wet of verordening als geheel: grondslag governance-object) |

**Stap 4 — Drempel.** Per voorlopig type de getelde criteria; hoogstens 1 nee. *herkenbaar*, *gemeentelijk* en *eigen identiteit* zijn al harde poorten in stap 1 en 2. Meer nee → geen element, voorleggen met de ontbrekende criteria.

| Nr | Type | Getelde criteria |
|---|---|---|
| 19 | Bedrijfsobject, Contract | *betekenis in onderwerp*, *relaties*, *onderscheidbare exemplaren*, *levenscyclus*, *wordt bewerkt* |
| 20 | Product | *betekenis in onderwerp*, *relaties*, *onderscheidbare exemplaren* |
| 21 | Actor | *betekenis in onderwerp*, *relaties* |
| 22 | Rol | *betekenis in onderwerp*, *relaties*, *meerdere vervullers* |
| 23 | Proces | *betekenis in onderwerp*, *toegewezen partij*, *gebruikt objecten*, *aanleiding*, *benoembaar resultaat*, *herhaald uitgevoerd*, *eigen normering* |
| 24 | Functie | *betekenis in onderwerp*, *toegewezen partij*, *gebruikt objecten*, *stabiel over tijd* |
| 25 | Gebeurtenis, Dienst | *betekenis in onderwerp*, *relaties* |

**Stap 5 — Specialisatieniveau** (alle typen met een paginatype)

| Nr | Als | Dan |
|---|---|---|
| 26 | niet *zelfstandig beleidsbegrip*, met `genoemd_begrip` | specialisatie zonder pagina van het genoemde, herkenbare bredere begrip; relaties opgetild |
| 27 | niet *zelfstandig beleidsbegrip*, zonder `genoemd_begrip` | voorleggen: noem het bredere begrip |
| 28 | anders | element van het voorlopige type |

**Aanvullingen**

| Stap | Als | Dan |
|---|---|---|
| Tegenhanger | Actor of Rol met *onderscheidbare exemplaren* + *levenscyclus* + *wordt bewerkt* | ook een bedrijfsobjectpagina (tegenhanger); bij gedrag nooit: het resultaat is dan een apart begrip |
| Annotatie | *geautomatiseerd verwerkt* | `data_object: ja` (voedt het hiaat-signaal richting GGM) |
<!-- EINDE gegenereerd -->

## Scope

- **Gemeentelijk perspectief.** Alleen wat de gemeente ziet, doet of beslist, of een partij waarmee zij structureel samenwerkt. Een ketenpartner (UWV, IND, COA, GGD …) krijgt ALLEEN een actorpagina bij een structurele relatie met de gemeente: opdrachtgever, mede-eigenaar (gemeenschappelijke regeling), prestatieafspraken of een wettelijke overlegplicht. Een partij die alleen als context of afbakening in de bron staat (behandelend arts, gedeputeerde staten), krijgt *gemeentelijk*: nee. De interne processen en rollen van een ketenpartner blijven altijd buiten scope. Precedent: GGD (gemeente is mede-eigenaar en opdrachtgever).
- **Een begrip met uitkomst "geen element"** wordt niet weggelaten: het blijft in de begrippenlijst van het onderwerp staan, met de uitkomst en de reden.

## Anti-patronen

Deze argumenten tellen **nooit** mee, ook niet impliciet of als synoniem:
- registreren of registreerbaar zijn ("wat de gemeente registreert", "registratieobject");
- eigendom ("eigendom ligt bij X"), systeembeheer, "regie, niet registratie", "extern systeem".

Het kenmerk *geautomatiseerd verwerkt* is de enige plek waar gegevensvastlegging meetelt, en alleen als annotatie (`data_object`): het bepaalt nooit of iets een element is.

## Begripstype en entiteitstype

De uitkomst van de beslistabel typeert een **begrip uit een bron** ("wat is het?"). Een GGM-entiteit heeft daarnaast een eigen classificatie (entiteitstype, bij de dekkingsanalyse van het GGM). Die twee zijn niet uitwisselbaar: een GGM-entiteit is geen begrip en wordt pas via een bron beoordeeld.
