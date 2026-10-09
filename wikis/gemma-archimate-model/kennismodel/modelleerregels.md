---
id: modelleerregels
type: kennismodel
titel: Modelleerregels
---

# Modelleerregels

De regels die voor alle elementen gelden, met de voorrang. Wat per elementtype geldt (kernrelatie, niveaus, naamvorm, toegestane en weggefilterde relaties), staat in de modelleerafspraken van dat type; het overzicht in het [kennismodel](README.md), de vragen in [kenmerken en beslistabel](kenmerken-en-beslistabel.md). De werkwijze van de AI (navragen, per geval, elke claim een bron) staat in [AGENTS.md](../AGENTS.md); waarom het model zo is, in [ARCHITECTURE.md](../ARCHITECTURE.md). Deze pagina is met de hand geschreven.

Verwijs naar een regel met haar naam, bijvoorbeeld "regel Thuishoren". Achter een regel staat of een script haar controleert: *(schema)* en *(script)* houden een fout tegen, *(signaal)* geeft een waarschuwing die de AI inhoudelijk beoordeelt. Zonder markering is het een regel voor het oordeel van de AI.

## Voorrang

### Bronvoorrang

Voor welke begrippen er zijn en wat ze formeel betekenen, gaat een bron met een hoger brontype voor. Het brontype staat per bron in de intake (`sources/index/`); de volgorde staat in `wiki.yaml` `bronvoorrang` en is, van hoog naar laag:

1. `europese-regelgeving`: regelgeving van de Europese Unie die voor alle gemeenten geldt, zoals verordeningen die rechtstreeks werken (AVG, AI-verordening).
2. `rijksregelgeving`: regelgeving van het Rijk die voor alle gemeenten gelijk is: wetten, algemene maatregelen van bestuur en ministeriële regelingen, en door Nederland goedgekeurde verdragen.
3. `informatiemodel`: RSGB, RGBZ, catalogi van basisregistraties, en architectuurmodellen zoals de UPL-lijsten.
4. `richtlijn`: landelijke uitvoeringsvoorschriften, handleidingen, circulaires en handreikingen van het Rijk, uitvoeringsorganisaties en koepels (HUP van RvIG, NVVB, VNG, Divosa).
5. `gemeentelijke-regelgeving`: verordeningen, nadere regels, beleidsregels en regelingen van gemeenschappelijke regelingen, die elke gemeente zelf vaststelt, en de VNG-modellen daarvan. Omdat de inhoud per gemeente verschilt, staat in het model het VNG-model als gemeenschappelijke vorm; de regeling van één gemeente is een voorbeeld en geen element.
6. `beleid`: intern gericht beleid van een gemeente (beleidsnota's, visies, programma's).
7. `overig`: praktijk, zoals productpagina's, websites en presentaties.

Voorrang bepaalt nooit of iets een element is. De naam en de herkenbare definitie komen uit de gangbare taal van bronnen van `richtlijn`, `beleid` en `overig`; de wetsterm wordt een synoniem met context "wet". Precedent: Urn, niet Asbus. `europese-regelgeving` en `rijksregelgeving` heten samen landelijke regelgeving. Het GGM en het GEMMA-model (brontype `model`) zijn geen bron maar matchdoel en vallen buiten de volgorde; de UPL is bron én matchdoel. *(signaal)*

### Een element modelleren, in deze volgorde

1. Welk begrip? Synoniem of homoniem (stap 0 van de beslistabel).
2. Grondslag: de juiste landelijke wettelijke bron, met het artikel (regel Wettelijke grondslag).
3. Kenmerken → type, via de beslistabel. De uitkomst is bindend (regel Beslistabel beslist).
4. Kernrelaties, uit dezelfde wettekst.
5. Indeling en indelingsrelaties ([indelingen](indelingen.md)).
6. Overige relaties, uit de bronanalyse.
7. Matches.

### Matchen

De AI matcht op betekenis (regel Match op betekenis), met de kandidaten uit `tools/ggm.py` en `tools/gemma.py`; het script haalt daarna alleen de letterlijke velden op.

| Match | Typen | Wat het doet | Zonder match |
|---|---|---|---|
| UPL (ook bron) | product, dienst | een UPL-item valt nooit weg; de naam letterlijk uit de UPL | procesarchitectuur-terugmelding |
| GGM | bedrijfsobject, data-object; beleidsdomein | matchdoel en toets: entiteit, definitie, relaties; per beleidsdomein de dekking | GGM-terugmelding (hiaat) |
| GEMMA-model | alle elementtypen | het id gaat mee in de export en overschrijft naam en definitie; zwak of partieel voorleggen | nieuw element via de export; GEMMA-terugmelding als een GEMMA-element vervalt |
| Generiek GEMMA-element | gebeurtenis, rol, dienst, bedrijfsproces | specialisatie (`gemma_generiek`) | voorstel aan GEMMA |
| GEMMA-kennismodel (Over GEMMA) | elementtypen en relatietypen | namen en definities van de typen | in de export gemarkeerd als niet in Over GEMMA |
| Indelingslijsten | typen met een indeling | Iv3-taakveld, GGM-beleidsdomein, GEMMA-domein, GEMMA-procesarchitectuur (soort werk) | nieuwe groepering in de export; terugmelding |

### Relaties

Ter uitleg als aparte stappen; bij het beoordelen gebeuren ze vaak tegelijk, uit dezelfde wettekst:

1. grondslag (*is grondslag voor* vanuit een beleidskader);
2. kernrelatie van het type;
3. indelingsrelaties (levensloopproces → aggregatie → bedrijfsproces, functieketen, kernobject);
4. overige relaties uit de bronanalyse (per partij wat zij houdt, beheert, uitvoert of vervult; toegang met een handeling of verantwoordelijkheid);
5. de GGM-match van de relatie, alleen bij bedrijfsobjecten, data-objecten en beleidsdomeinen;
6. GEMMA (geen match: de relatie gaat als nieuw mee in de export).

Welke relaties tussen twee typen in het kennismodel staan, en welke weggefilterd zijn met de reden, staat in de modelleerafspraken van het type.

## Oordeel

- **Beslistabel beslist** — Of een begrip een element is en van welk type, volgt alleen uit de kenmerken en de beslistabel ([kenmerken en beslistabel](kenmerken-en-beslistabel.md), skill `gemma-archimate-model-criteria`). Registratie, eigendom, systeembeheer, regie of een extern systeem zijn geen argument, ook niet impliciet of als synoniem ("wat de gemeente registreert", "registratieobject", "eigendom ligt bij X", "regie, niet registratie", "extern systeem"). Het kenmerk *geautomatiseerd verwerkt* is de enige plek waar gegevensvastlegging meetelt, en alleen als annotatie (`data_object`). De uitkomst typeert een begrip uit een bron ("wat is het?"); een GGM-entiteit heeft een eigen classificatie, is geen begrip en wordt pas via een bron beoordeeld. *(script; signaal bij registr*-taal)*
- **Match op betekenis** — Match met GGM en GEMMA op betekenis, niet op naam: herken homoniemen en synoniemen en volg relaties en generalisaties. Lees de modellen alleen via `tools/ggm.py` en `tools/gemma.py`, nooit direct en nooit via kopieën of CSV-exports. *(script: de gekozen match moet bestaan; signaal bij een afwijkende modelnaam)*
- **Zwakke match voorleggen** — Een GEMMA-match met sterkte `zwak` of `partieel` leg je altijd voor aan de redacteur, met wat er in GEMMA verandert: de export naar Archi (skill `gemma-archimate-model-archimate-export`) neemt het GEMMA-id over en overschrijft naam en definitie van dat GEMMA-element. Matchen is de verantwoordelijkheid van de wiki en de redacteur; de export en Archi vertrouwen de match. Past het GEMMA-element niet echt, kies dan `sterkte: geen` en noem het in de onderbouwing.
- **Eén element in het hele model** — Eén betekenis is één element in het hele model, ook als meer onderwerpen het gebruiken; een gelijke naam met een andere betekenis is een homoniem (regel Match op betekenis). Zoek vóór je een begrip beoordeelt in alle beoordelingen, van alle onderwerpen, op naam en synoniemen. Bestaat het al, werk die beoordeling bij: voeg je onderwerp toe aan `onderwerpen` en zet wat alleen in jouw onderwerp geldt onder `per_onderwerp`. Hetzelfde begrip onder een andere naam krijgt `synoniem_van`, een gelijke naam met een andere betekenis staat onder `homoniemen`. *(signaal: dezelfde naam of hetzelfde synoniem in twee beoordelingen zonder `synoniem_van` of `homoniemen`; dezelfde GEMMA- of GGM-match, exact of sterk, bij twee elementen)*
- **Thuishoren** — Elk element heeft één thuisonderwerp, het eerste in `onderwerpen`: dat onderwerp beoordeelt het, ook het kenmerk *betekenis in onderwerp*; de andere onderwerpen gebruiken het met relaties en `per_onderwerp`. Een generiek element (kenmerk *generiek*) en een orgaan of de organisatie van de gemeente horen thuis in het onderwerp Algemeen. Anders beslist de inhoud: het thuisonderwerp is het onderwerp van de taak waarin het element ontstaat of verandert. Voor een bedrijfsobject is dat het onderwerp van het proces dat het maakt, voor een proces, dienst of product het onderwerp van zijn kernobject, voor een gebeurtenis het onderwerp van het object waarvan de toestand verandert, voor een rol of actor het onderwerp van het meeste gedrag dat hij uitvoert. Het aantal relaties is een aanwijzing, geen beslissing; dat een element eerder in een ander onderwerp is beoordeeld of goedgekeurd (de volgorde van inlezen) is geen argument. Volgt het thuisonderwerp eenduidig uit de inhoud, dan verplaatst de AI het zonder voorleggen en noemt het in de lijst ter bevestiging; alleen bij inhoudelijke twijfel voorleggen. Hoort een begrip bij een onderwerp dat nog niet bestaat, dan is de uitkomst een verwijzing en beoordeelt dat onderwerp het later. Verplaatsen gaat per geval (regel Per geval) door de volgorde van `onderwerpen` te wijzigen; het object in Archi blijft, want de export gebruikt de onderwerpen niet. De omschrijving van een onderwerp noemt zijn kernobjecten en wat erbuiten valt, met het onderwerp waar dat thuishoort. *(signaal: kernobject met een ander thuisonderwerp; verwijzing naar een onderwerp dat nu bestaat; element met meer relaties naar één ander onderwerp dan naar het eigen, generieke elementen uitgezonderd)*
- **Relaties tussen onderwerpen** — Een relatie tussen elementen van verschillende onderwerpen is een gewone relatie: leg haar vast waar de bronnen haar noemen, in de beoordeling van het bronelement (`tools/relaties.py voorstel` kijkt over alle onderwerpen). Een onderwerp verwijst zo naar de elementen van een ander onderwerp in plaats van ze te herhalen. Is het bronelement van een ander onderwerp en goedgekeurd, dan gaat het door de relatie opnieuw ter beoordeling. Elk element heeft minstens één relatie met een ander element; de samenhang per onderwerp staat in `voortgang.md`. *(signaal: element zonder relatie)*
- **Gemeentelijk perspectief** — Beschrijf wat de gemeente ziet, doet en beslist. Een externe partij (UWV, IND, COA, GGD …) wordt alleen een element bij een structurele relatie met de gemeente: opdrachtgever, mede-eigenaar (gemeenschappelijke regeling), prestatieafspraken of een wettelijke overlegplicht. Een partij die alleen als context of afbakening in de bron staat, of die alleen per geval en op verzoek beslist (gedeputeerde staten als beroepsinstantie), krijgt *gemeentelijk*: nee en staat in de beschrijving. De interne processen en rollen van een ketenpartner blijven altijd buiten scope. Precedenten: GGD wel (de gemeente is mede-eigenaar en opdrachtgever); Officier van justitie en Arts als behandelende arts (wettelijke meld- en overlegplicht met de gemeentelijke lijkschouwer). Een begrip met uitkomst "geen element" blijft in de begrippenlijst staan, met de uitkomst en de reden.

## Bronnen

- **Tegenspraak** — Spreken bronnen elkaar tegen, leg dan beide vast en markeer de tegenspraak. Wat formeel geldt volgt de regel Bronvoorrang (landelijke regelgeving gaat voor, `overig` komt laatst); de afwijkende bron blijft vermeld als afwijking in de praktijk.
- **Wettelijke grondslag** — Het model geldt voor alle gemeenten; daarom heeft elk element een landelijke wettelijke bron, dat is een bron van brontype `europese-regelgeving` of `rijksregelgeving` (regel Bronvoorrang), genoemd met het artikel. *(script; signaal: een element zonder landelijke wettelijke bron)* Uitgewerkt:
  - Een relatie heeft geen eigen landelijke grondslag nodig: de structuur wordt uit de wet afgeleid, maar per relatie volstaat een bron (regel Elke claim een bron).
  - Bronnen van `richtlijn`, `beleid` en `overig` dienen voor taal, voorbeelden, werkwijze en het vinden van lacunes, niet als onderbouwing; een grondslag uit de UPL geldt pas na controle in de wettekst.
  - Eén uitzondering: een product of dienst uit de UPL blijft altijd, ook zonder landelijke wettelijke grondslag. Heeft het dan een grondslag in een bron van brontype `gemeentelijke-regelgeving` (een VNG-model, niet de verordening van één gemeente), dan wordt die genoemd; heeft het geen grondslag, of noemt de UPL een grondslag die geen taak geeft, dan volgt een procesarchitectuur-terugmelding. Zo'n product wordt niet uitgewerkt in processen, objecten, gebeurtenissen of rollen.
  - Een element zonder landelijke wettelijke bron, en een product of dienst buiten de UPL zonder die bron, blijft niet.
  - Staat de landelijke grondslag eenduidig in de nagelezen wettekst, dan voegt de AI de bron en de relatie *is grondslag voor* toe zonder voorleggen en noemt het geval in de samenvatting ter bevestiging; alleen bij twijfel voorleggen.
  - Een bedrijfsfunctie heeft geen eigen wettelijke bron nodig: zij volgt de grondslag van de diensten en processen die zij omvat, en vervalt alleen als zij niets meer omvat. Een bedrijfsfunctie die alleen UPL-producten of -diensten zonder landelijke grondslag zou omvatten, bedient geen proces en vervalt in de wiki; die producten hangen onder de functie van hun beleidsdomein, met een GEMMA-terugmelding.
  - De grondslag staat als relatie *is grondslag voor* van een beleidskader; een beleidskader in *Gemeentelijke regelgeving* is alleen grondslag voor een UPL-product of -dienst zonder landelijke grondslag, en werkt voor de rest de wet uit (relatie *werkt uit voor*); een beleidskader in *Richtlijn* is geen wettelijke grondslag, zijn relatie heet *geeft richtlijn voor*. De groep volgt de Grondslagindeling ([indelingen](indelingen.md)). *(script: een relatie is grondslag voor vanuit een richtlijn, of vanuit gemeentelijke regelgeving naar iets anders dan een UPL-product zonder landelijke grondslag, en een bedrijfsproces dat een UPL-product zonder landelijke grondslag realiseert)*

## Tekst

- **Begrijpelijk** — Herkenbaar voor domeinexperts; geen jargon tenzij nodig. De definitie is één zin. *(signaal)*
- **Los van het onderwerp** — Definitie en beschrijving gelden in elk onderwerp; toets: past de tekst ongewijzigd in elk ander onderwerp? Wat een element in één onderwerp doet, staat onder `per_onderwerp`. *(signaal)*
- **Naamvorm** — De naam volgt de naamvorm van het type, in zijn modelleerafspraken: een proces een infinitief met object in GEMMA-volgorde ("Behandelen aanvraag"), een functie een zelfstandig naamwoord voor het gebied van gedrag ("Vergunningverlening"), een gebeurtenis een voltooide verandering ("Overlijden"), een dienst geformuleerd vanuit de afnemer ("Melding openbare ruimte doen"). Het zelfstandig naamwoord uit de bron wordt een synoniem met context "beleid". Een product of dienst uit de UPL krijgt de UPL-naam letterlijk ("Verlof tot begraven"), met een synoniem waar dat betekenis toevoegt. *(signaal)*

## Terugmelden en export

- **Afwijken mits teruggemeld** — Het model mag afwijken van de UPL-indeling (taakveld, GEMMA-domein) en van het kennismodel procesarchitectuur, mits de afwijking is teruggemeld in de procesarchitectuur-terugmeldingen; de terugmelding dekt dan het signaal. *(signaal)*
- **Objectbehoud** — Hernoemen, samenvoegen of splitsen van een element leidt niet vanzelf tot een nieuw object in Archi: de redacteur gebruikt de objecten in views, en de export werkt views niet bij. Leg in `beoordelingen/objecten.yaml` vast welk bestaand object het element voortzet. Bij hernoemen altijd; bij samenvoegen vraag je de redacteur of en welk object blijft; bij splitsen of er een object blijft en welk deel het krijgt. *(script: het register klopt; de export weigert een typewijziging van een voortgezet object)*
