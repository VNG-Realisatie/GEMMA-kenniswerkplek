---
id: indelingen
type: doc
titel: Indelingen van de bedrijfsarchitectuur
bijgewerkt: '2026-10-08'
bronnen:
- 2026-vng-over-gemma
- 2026-vng-gemma-2026-10-02
- 2026-vng-gemma-proceshierarchie
---

# Indelingen van de bedrijfsarchitectuur

Bronnen: Over GEMMA [bronanalyse](../bronanalyses/algemeen/overig/2026-vng-over-gemma.md) (regelnummers verwijzen naar de tekst van de bron) · GEMMA-architectuurmodel [origineel](../../../sources/raw/2026-vng-gemma-2026-10-02.archimate), gelezen via `tools/gemma.py` · [Producten en diensten procesarchitectuur](https://www.gemmaonline.nl/wiki/Producten_en_diensten_procesarchitectuur) op GEMMA Online, met de externe UPL-lijst [tekst](../../../sources/raw/2025-vng-upl-producten-en-diensten-extern.md) (500 producten; voor lijkbezorging [bronanalyse](../bronanalyses/lijkbezorging/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md)) en de interne lijst [tekst](../../../sources/raw/2025-vng-upl-producten-en-diensten-intern.md) (215 producten).

Waar staat elk element in de indelingen van het model? Hoe het model wordt ingedeeld in de hele breedte van de bedrijfsarchitectuur: welke indelingen GEMMA heeft, welke erbij komen, welk elementtype waar valt, en welke kenmerken en regels daarvoor nodig zijn. Aanleiding: lijkbezorging was plat en fijnmazig (één functie voor negen processen, vijftien bedrijfsobjecten naast elkaar). Doel: een compleet GEMMA-model op het juiste abstractieniveau, met een indeling die ook in Archi zichtbaar is. De besluiten staan onderaan; de omzetting in de beslistabel volgt.

## Begrippen

### Indeling en view

- **Indeling**: een ordening naar één criterium, met benoemde niveaus. Gebruikt een tweede elementtype hetzelfde criterium, dan wordt het in de bestaande indeling ingedeeld; er komt geen nieuwe.
- **View**: een weergave van één indeling voor één of meer elementtypen, bijvoorbeeld *Bedrijfsobjecten per beleidsdomein*.
- **Specialisatie of aggregatie**: specialisatie koppelt aan een GEMMA-indeling (wat voor soort is het?), aggregatie aan een eigen indeling (waar hoort het bij?).

### Procesniveaus

De procesniveaus, de processtructuur (één levensloopproces per kernobject) en de toets aan het Kennismodel procesarchitectuur staan in [Processen: niveaus, klant-tot-klant en ketensamenwerking](proceshierarchie.md).

### Objectniveaus

- **Kernobject**: het bedrijfsobject waarvan één levensloopproces de hele levensloop omvat.
- **Subobject**: een deel van een kernobject, met een eigen bedrijfsproces.
- **Generiek object**: dezelfde betekenis in veel onderwerpen. Blijft voorlopig element in het onderwerp en verhuist later naar een algemeen onderwerp. Domeinspecialisaties krijgen geen pagina en worden in relaties genoemd met **`via`** (Vergunning via *vergunning tot opgraving*).
- Een onderdeel zonder eigen proces, en invoer die een andere partij maakt, krijgen geen pagina.

### Afnemer

**Afnemer extern of intern**: voor wie een proces, product of dienst is. Dit is een eigenschap, geen indeling. Ze volgt de bovenste laag van het processenlandschap (uitvoerend tegenover sturend en ondersteunend), de rol *Klant (intern of extern)* (regel 567) en de externe en interne UPL-lijst.

## Indelingen

### In GEMMA

Stand van het GEMMA-model van 2026-10-02.

| Indeling | Deelt in | Niveaus | Vorm |
|---|---|---|---|
| Procesindeling naar soort werk (processenlandschap) | bedrijfsprocessen | sturend, uitvoerend of ondersteunend → procescluster → generiek bedrijfsproces → deelproces → processtap → handeling; een domeinproces via specialisatie (*Behandelen omgevingsvergunningaanvraag* → *Behandelen vergunningaanvraag*) | aggregatie (102×), compositie (31×) |
| Functie-indeling naar domein | bedrijfsfuncties | soort sturing → domein → soort werk → onderwerp (*Uitvoering › Fysieke leefomgeving › Exploitatie › Exploiteren van begraafplaatsen*); 7 van de 289 functies hebben meer ouders | aggregatie (302×); groepering *GEMMA domeinen* |
| Beleidsdomeinindeling | bedrijfsobjecten | taakveld Iv3 → beleidsdomein (GGM) → object | groepering (507×) |
| Doelgroepindeling | rollen | *Gemeente*, *Inwoners en ondernemers*, *Ketenpartners*, *Generiek* → rol | rol met *GEMMA type* `Groep` in `Business / Bedrijfsrollen` (regel 214), bediend door de groeperingen *Domein en doelgroep* |
| Applicatieservice-indeling naar domein | applicatieservices | domein × doelgroep → service | groepering (regel 208, 221-227); alleen gedocumenteerd |

- **Twee rode draden**: het GEMMA-domein (functies, applicatieservices, UPL) en het taakveld Iv3 met beleidsdomein (objecten, UPL).
- **Niet ingedeeld**: gebeurtenissen (1 element), diensten, producten (6, technische architectuur), actoren en kanalen.
- **Applicatielaag**: wordt later deel van de wiki. Referentiecomponenten zijn niet direct aan functies gekoppeld (76 van 256 in een groepering). Advies aan het GEMMA-team: laat ze aggregeren door een hogere bedrijfsfunctie (todo).

### In de wiki

| Indeling | Van | Deelt in | Niveaus | Relatie in Archi |
|---|---|---|---|---|
| Procesindeling naar soort werk | GEMMA, uitgebreid | bedrijfsprocessen; via generieke GEMMA-elementen ook gebeurtenissen, diensten en rollen | generiek GEMMA-proces → cluster naar soort werk → bedrijfsproces | specialisatie naar het GEMMA-element (exacte match); aggregatie |
| Procesindeling naar kernobject | nieuw | levensloopprocessen, bedrijfsprocessen, gebeurtenissen, bedrijfsinteracties | levensloopproces per kernobject → bedrijfsproces; een bedrijfsinteractie bij haar kernobject | aggregatie; map `wiki-gemma-model / Procesindeling naar kernobject`, een bedrijfsinteractie in `wiki-gemma-model / Ketensamenwerking` |
| Functie-indeling naar domein | GEMMA | functies, producten, diensten | domein → functie → dienst; domein → product | aggregatie; functie bedient proces |
| Beleidsdomeinindeling | GEMMA | objecten, afspraken, producten, diensten, beleidskaders, levensloopprocessen, bedrijfsinteracties | taakveld → beleidsdomein → element | aggregatie vanuit de groepering |
| Doelgroepindeling | GEMMA, uitgebreid | rollen, actoren, samenwerkingen, kanalen | gemeente (bestuursorgaan, ambtelijk), inwoners en ondernemers, ketenpartners → element | aggregatie vanuit de doelgroeprol |
| Grondslagindeling | nieuw | beleidskaders | brontype van de regeling (regel Bronvoorrang), afgeleid uit de regelgever: *Europese regelgeving* (`europese-regelgeving`), *Rijksregelgeving* (`rijksregelgeving`), *Richtlijn* (`richtlijn`), *Gemeentelijke regelgeving* (`gemeentelijke-regelgeving`) → beleidskader; dezelfde naam voor de groep in Archi en de map in de wiki en in Archi; alleen gevulde groepen | aggregatie vanuit de groep (besluiten redacteur 2026-10-08) |

Een bedrijfsproces heeft hoogstens twee ouders: het levensloopproces van zijn kernobject en zijn cluster naar soort werk. De procesindeling naar kernobject is strikt hiërarchisch: een levensloopproces aggregeert geen levensloopproces, en een bedrijfsproces hangt onder één levensloopproces; anders is het een fout.

#### Hergebruik

Een product- en dienstindeling, beleidskaderindeling en kanaalindeling zijn geen eigen indelingen:
- producten en diensten vallen in de Beleidsdomeinindeling en de Functie-indeling (twee ouders; de UPL draagt beide als kolom);
- beleidskaders vallen in de Beleidsdomeinindeling, met de regelgever als eigenschap, en in de Grondslagindeling onder het brontype van hun regeling: *Europese regelgeving*, *Rijksregelgeving*, *Richtlijn* of *Gemeentelijke regelgeving*, als groep en als map (besluiten redacteur 2026-10-08; zie [Wettelijke grondslag](wettelijke-grondslag.md));
- een levensloopproces en een bedrijfsinteractie vallen in de Beleidsdomeinindeling, onder het beleidsdomein van hun kernobject, omdat er in de Procesindeling naar kernobject niets boven hen staat;
- kanalen vallen in de Doelgroepindeling, met fysiek of digitaal als eigenschap.

Verder:
- de Applicatieservice-indeling combineert domein en doelgroep;
- een cluster naar soort werk breidt het processenlandschap uit zonder GEMMA-elementen te wijzigen.

#### Taak en beleidsdomein

Tot 2026-10-08 was de taak een eigen niveau, met een hoofdbeleidsdomein als eigenschap, omdat GEMMA geen beleidsdomein *Begraafplaatsen en crematoria* kent en de UPL het verlof tot begraven onder 0.2 zet. In de praktijk viel elke taak samen met het beleidsdomein van haar kernobjecten (*Verzorgen burgerzaken* met Burgerzaken, *Verzorgen lijkbezorging* met Begraafplaatsen en crematoria). De taak vervalt daarom (besluit 2026-10-08): een beleidsdomein dat GEMMA niet kent, wordt een gemeentelijk beleidsdomein met een terugmelding, en een product dat de UPL onder een ander taakveld zet, heeft al een procesarchitectuur-terugmelding. Zie [Proceshiërarchie](proceshierarchie.md).

#### Views

| Indeling | Views |
|---|---|
| Procesindeling naar soort werk | Bedrijfsprocessen per cluster en generiek GEMMA-proces |
| Procesindeling naar kernobject | Per beleidsdomein: levensloopprocessen per kernobject, bedrijfsprocessen met producten en diensten, gebeurtenissen; per ketensamenwerking de bedrijfsprocessen die haar bedienen |
| Functie-indeling naar domein | Functies die processen bedienen; Producten en diensten per functie |
| Beleidsdomeinindeling | Bedrijfsobjecten (kern- en subobjecten), Producten en diensten, Beleidskaders per beleidsdomein |
| Doelgroepindeling | Actoren en rollen per doelgroep; Kanalen per doelgroep |

## Kenmerken en beslistabel

Dit is het ontwerp van de criteria voor de indelingen (2026-10-04, bijgewerkt 2026-10-08). De werkinstructie staat in skill gemma-archimate-model-criteria (stap 7) en in [Kenmerken en beslistabel](../kennismodel/kenmerken-en-beslistabel.md); de controles zitten in `tools/bepaal_type.py` en `tools/afleiden.py`.

### Per elementtype

Een **vet** woord is nieuw of gewijzigd ten opzichte van de beslistabel van 2026-10-01. Bijgewerkt naar de procesniveaus van 2026-10-08: de taak en het kenmerk *meer organisaties* vervallen, de bedrijfsinteractie krijgt een pagina.

| Type | Bepaald door | Kernrelatie | Drempel | Eigen pagina | Indeling |
|---|---|---|---|---|---|
| Bedrijfsobject, afspraak | geen aard; *afspraak* | *wordt bewerkt* | *onderscheidbare exemplaren*, *levenscyclus* | **objectniveau**; *zelfstandige specialisatie* | Beleidsdomein |
| Product | *aanbod als geheel* | *omvat diensten en afspraken* | *afnemer* (**klantrol, met bediening**), *benoembaar resultaat* | **zelfstandig aanbod** | Beleidsdomein en Functie |
| Dienst | *aangeboden gedrag* | *gerealiseerd door* (**bedrijfsproces of functie**) | *afnemer*, *benoembaar resultaat* | **generiek** → specialisatie | Beleidsdomein en Functie |
| Cluster naar soort werk | **groepeert processen** | **omvat processen** (minstens 2 bedrijfsprocessen) en specialisatie naar GEMMA | — | anders specialiseert het bedrijfsproces | Naar soort werk |
| Levensloopproces | *per keer doorlopen* en **omvat levensloop** | *toegewezen partij* | *aanleiding*, *benoembaar resultaat* | **procesniveau** | Naar kernobject en Beleidsdomein |
| Bedrijfsproces | *per keer doorlopen* en *bijdrage aan groter proces* | *toegewezen partij* | pagina bij **klant tot klant**; een deelproces staat in `deelprocessen` van zijn bedrijfsproces | **procesniveau** | Naar kernobject en naar soort werk |
| Bedrijfsfunctie | *gegroepeerd gedrag* | **bedient gedrag** | *toegewezen partij*, *gebruikt objecten*, *stabiel over tijd* | **in functie-indeling** | Functie |
| Gebeurtenis | *toestandsverandering* | *leidt tot gedrag* | *komt herhaald voor* | **generiek** → specialisatie | Naar kernobject |
| Actor, bedrijfssamenwerking | partij of verband | *vervult een rol*, *voert gedrag uit* | — | **soort partij** | Doelgroep |
| Rol | *hoedanigheid* | *voert gedrag uit* | — | *zelfstandige specialisatie*; **generiek** → specialisatie | Doelgroep |
| Kanaal | *toegangspunt* | *ontsluit een dienst* | — | centrale set | Doelgroep |
| Beleidskader | *regeling als geheel*, *landelijk* | *is grondslag voor* (**bij voorkeur van een product**) | *in werking* | regeling als geheel | Beleidsdomein |
| Bedrijfsinteractie | *gezamenlijk gedrag* | *toegewezen partij* | *aanleiding*, *benoembaar resultaat* | pagina met kernobject; voorleggen | Naar kernobject en Beleidsdomein |
| Representatie, locatie | — | — | — | geen pagina | — |

Gaten die hiermee dicht gaan:
- **Proces**: er was geen niveau boven het product; 500 producten zouden 500 bedrijfsprocessen geven.
- **Product**: er was geen abstractieregel; de UPL benoemt aanbod per naam, niet per variant.
- **Dienst**: een dienst per processtap was mogelijk.
- **Functie**: de kernrelatie volgde niet het kennismodel, en er was geen toets op de plaats in de functie-indeling.
- **Gebeurtenis**: generieke ontvangstgebeurtenissen konden per proces een pagina krijgen.
- **Actor**: er was geen onderscheid tussen soort en exemplaar.

### Nieuwe kenmerken

| Groep | Kenmerk | Vraag |
|---|---|---|
| Soort gedrag | *groepeert processen* | Is het een groepering van bedrijfsprocessen van één soort werk, die niet per geval wordt doorlopen? (tot 2026-10-08 ook rond één taak) |
| Gedrag | *omvat processen* | Omvat het minstens twee processen? Noem ze. |
| Gedrag | *omvat levensloop* | Omvat het het gedrag over de hele levensloop van één exemplaar van een bedrijfsobject? Noem het object. |
| Gedrag | *meer organisaties* (vervallen op 2026-10-08) | Voeren twee of meer organisaties het samen uit, elk vanuit een eigen rol, niet als klant of alleen als adviseur? Noem ze. |
| Gedrag | *eigen besluit* | Eindigt het in een besluit van een bevoegd orgaan of mandataris? Noem orgaan en artikel. |
| Gedrag | *levert aanbod* | Realiseert het een dienst of levert het een product aan een afnemer? Noem het (referentie: de UPL). |
| Gedrag | *bedient gedrag* | Ondersteunt de functie aanwijsbaar een proces? Noem het. |
| Gedrag | *in functie-indeling* | Past de functie als onderwerp onder een soort werk in de Functie-indeling naar domein? Noem de bovenliggende functie. |
| Gedrag | *leidt tot gebeurtenis* | Eindigt het in een benoemde toestandsverandering, of in een die een ander proces start? Noem die. |
| Partij | *soort partij* | Heeft elke gemeente met deze partij te maken in dezelfde rol, zodat het element voor alle gemeenten geldt? Het criterium sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat. |
| Passief | *deel van object* | Is het een onderdeel van één ander object, dat ermee ontstaat en eindigt? Noem dat object. |
| Passief | *invoer van een ander* | Maakt en beheert een andere partij het, terwijl de gemeente het alleen ontvangt of raadpleegt? Noem de maker. |
| Passief | *zelfstandig aanbod* | Wordt het onder eigen naam aangeboden, en niet als variant of tarief? |
| Specialisatie | *generiek* | Komt het met dezelfde betekenis in veel onderwerpen voor? |

Hergebruikt worden: *per keer doorlopen*, *aanleiding*, *afnemer*, *benoembaar resultaat*, *eigen normering*, *bijdrage aan groter proces* (nu: één mutatie binnen het levensloopproces van een kernobject), *zelfstandige specialisatie*, *leidt tot gedrag* en *gezamenlijk gedrag* (nu ook: de ketensamenwerking).

**Indelingsvelden**, verplicht per type: `taakveld` en `beleidsdomein` (bestaan), `domein` (functie, product, dienst), `doelgroep` (actor, rol, samenwerking, kanaal), `regelgever` (beleidskader), `kernobject` (levensloopproces, bedrijfsproces, bedrijfsinteractie), `afnemer` (levensloopproces, bedrijfsproces, product, dienst).

### Stap 7: indeling

Een nieuwe stap na stap 6, met de context van alle uitkomsten.

#### Proces

- Cluster naar soort werk bij *groepeert processen* met een specialisatie naar GEMMA; minstens twee bedrijfsprocessen. Zonder specialisatie voorleggen: een taak is geen procesniveau.
- Levensloopproces bij *omvat levensloop*.
- Bedrijfsproces bij *bijdrage aan groter proces* met *klant tot klant* (besluit redacteur 2026-10-08, zie [Klant tot klant](proceshierarchie.md#bedrijfsproces-of-deelproces-de-toets-klant-tot-klant)); zonder is het een deelproces of processtap zonder pagina, beschreven in `deelprocessen` van het bedrijfsproces. *Eigen besluit* en *eigen normering* bepalen het niveau niet; een deelproces dat een dienst levert, wordt voorgelegd.
- Anders deelproces of processtap: geen pagina; de tekst gaat naar het bedrijfsproces.
- Bedrijfsinteractie bij *gezamenlijk gedrag*, met een kernobject; altijd voorleggen (estafette of orkestratie).

#### Object

- *generiek* → generiek.
- `kernobject` van een levensloopproces → kernobject (per kernobject precies één levensloopproces).
- *deel van object* met een eigen bedrijfsproces → subobject; zonder → onderdeel, geen pagina.
- *invoer van een ander* → geen pagina; vermeld bij het proces.
- Anders voorleggen.

Bij gebeurtenis, rol en dienst geeft *generiek* een specialisatie van een GEMMA-element met exacte match. Ontbreekt dat element, dan voorleggen als voorstel aan GEMMA.

#### Controles

- Elk element staat in zijn verplichte indeling. Meer ouders geeft een signaal, behalve de twee ouders van een bedrijfsproces (levensloopproces en cluster naar soort werk).
- Strikt hiërarchisch (fout): per kernobject één levensloopproces, of één per partij als ze samen een bedrijfsinteractie met dat kernobject bedienen; een levensloopproces aggregeert geen levensloopproces; een bedrijfsproces hangt onder hoogstens één levensloopproces; het taakveld en beleidsdomein van een levensloopproces en een bedrijfsinteractie zijn die van hun kernobject.
- Een functie onder domeinniveau wordt geaggregeerd door één bovenliggende GEMMA-functie in hetzelfde domein, volgens de GEMMA-functieketen; een functie op domeinniveau hangt via `domein` aan de domeingroepering. Een dienst wordt geaggregeerd door één functie in hetzelfde domein. Een product hangt via `domein` direct aan de domeingroepering: ArchiMate laat een functie geen product aggregeren (besluit 2026-10-05).
- In GEMMA aggregeert een domein de beleidsdomeinen. Het domein van een product of dienst moet passen bij de GEMMA-domeinen van zijn beleidsdomein (soms meer dan één, zoals bij Erfgoed). Een beleidsdomein dat GEMMA niet kent, geeft een signaal als zijn producten en diensten in meer domeinen vallen (besluit 2026-10-05). Het model mag afwijken van de UPL-indeling, mits de afwijking is teruggemeld in de [procesarchitectuur-terugmeldingen](../terugmeldingen/procesarchitectuur-terugmeldingen.md); de terugmelding dekt het signaal.
- Specialisatie en bediening naar GEMMA lopen alleen via een exacte match.
- *leidt tot gebeurtenis* vraagt een triggering.
- `via` wijst naar een specialisatie van het doel.
- Signalen bij:
  - een actorrelatie met een werkwoord van gedrag;
  - een beleidskader zonder product;
  - een bedrijfsproces onder geen levensloopproces;
  - een bedrijfsinteractie die geen bedrijfsproces bedient.

## Lijkbezorging

### IJking met de UPL

De externe UPL-lijst over lijkbezorging, met het proces dat elk product levert:

| UPL-product (Iv3, grondslag) | Levert | Stap 7 |
|---|---|---|
| grafuitgifte (7.5, model-beheersverordening art. 11) | Verlenen grafrecht | bedrijfsproces onder *Beheren grafrechten* |
| grafrechten (7.5, Gemeentewet art. 229) | generiek *Heffen en innen* | geen domeinproces |
| grafonderhoud (7.5) | Onderhouden graf | bedrijfsproces onder *Beheren graven* |
| gedenkteken plaatsingsvergunning (7.5, art. 19) | nog geen proces | gat: bedrijfsproces onder *Beheren graven*; Grafbedekking wordt subobject |
| herbegraven of alsnog cremeren (7.5, Wlb art. 29) | Opgraven lijk | bedrijfsproces onder *Bezorgen lijken* |
| verlof tot begraven (0.2, Wlb art. 11) | Verlenen verlof tot begraving of crematie | bedrijfsproces onder *Bezorgen lijken* |
| asverstrooiing (7.5, model-APV art. 5:36) | nog geen proces | gat: de APV is geen bron |
| bijzondere begraafplaats toestemming (7.5, Wlb art. 40-41) | nog geen proces | gat: proces rond Begraafplaats |
| ontleding stoffelijk overschot toestemming (Wlb art. 67) | nog geen proces | gat: bedrijfsproces onder *Bezorgen lijken* |
| vervoersdocumenten stoffelijk overschot (7.5, Besluit op de lijkbezorging art. 11) | nog geen proces | gat: het besluit is geen bron |
| begraafplaats-, bijzettingen-, crematoriumregister (7.5, Wlb art. 27, 65, 50) | representatie bij Graf | dienst (raadplegen) |
| overlijdensaangifte, overlijdensakte (0.2, BW 1 art. 19h, 19f) | onderwerp Burgerzaken | ook in *Bezorgen lijken* |

Uitkomst:
- Elk product komt uit bij een bedrijfsproces (in 2026-10-04: deelproces) of bij het generieke proces; geen product wordt een eigen levensloopproces.
- De ijking vond vier ontbrekende processen, plus asverstrooiing. De UPL-grondslagen wijzen de bronnen aan.
- Begraafplaats is mogelijk een kernobject met een levensloopproces *Beheren begraafplaatsen*.

### Inschatting

De inschatting van 2026-10-04, ter toetsing in de herbeoordeling, in de niveaus van 2026-10-08 (levensloopproces → bedrijfsproces; de taak is het beleidsdomein en het ketenproces een ketensamenwerking). Elk verlies van een pagina en elke nieuwe GEMMA-koppeling wordt apart voorgelegd. De procesindeling hieronder is de uitkomst; de tabel naar soort werk en de overige elementen zijn de inschatting.

#### Procesindeling naar kernobject

De uitkomst van de herbeoordeling van 2026-10-08 (besluiten redacteur), met de huidige namen; de afbeelding volgt het overzicht van het onderwerp.

```
Begraafplaatsen en crematoria                       beleidsdomein (taakveld 7)
├─ Toestaan lijkbezorging                           levensloopproces, kernobject Stoffelijk overschot (gemeente als overheid)
│   ├─ Schouwen stoffelijk overschot                bedrijfsproces
│   ├─ Verlenen verlof tot begraving of crematie    bedrijfsproces → verlof tot begraven
│   ├─ Opgraven stoffelijk overschot                bedrijfsproces → herbegraven of alsnog cremeren
│   ├─ Treffen maatregel bij besmet stoffelijk overschot  bedrijfsproces
│   └─ … (andere termijn, laissez-passer, ontleding, asverstrooiing)
├─ Begraven en cremeren stoffelijk overschot        levensloopproces, kernobject Stoffelijk overschot (houder)
│   ├─ Uitvoeren lijkbezorging                      bedrijfsproces
│   └─ Bijzetten of verstrooien van de as           bedrijfsproces
├─ Verzorgen gemeentebegrafenis                     levensloopproces, kernobject Gemeentebegrafenis
├─ Beheren grafrechten                              levensloopproces, kernobject Grafrecht
│   ├─ Verlenen grafrecht                           bedrijfsproces → grafuitgifte
│   └─ Vervallen verklaren grafrecht                bedrijfsproces
├─ Beheren graven                                   levensloopproces, kernobject Graf
│   ├─ Ruimen graf                                  bedrijfsproces
│   ├─ Onderhouden graf                             bedrijfsproces → grafonderhoud
│   └─ Verlenen vergunning grafbedekking            bedrijfsproces → gedenkteken plaatsingsvergunning
├─ Beheren begraafplaatsen                          levensloopproces, kernobject Begraafplaats
└─ Beheren crematoria                               levensloopproces, kernobject Crematorium

Bezorgen stoffelijk overschot   bedrijfsinteractie (estafette), kernobject Stoffelijk overschot,
                                bediend door Toestaan lijkbezorging, Begraven en cremeren stoffelijk overschot en
                                Verzorgen gemeentebegrafenis; uitgevoerd door onder meer de Ketenpartner (officier van justitie)
```

#### Procesindeling naar soort werk

| Cluster naar soort werk | Generiek GEMMA-proces | Bedrijfsprocessen |
|---|---|---|
| Behandelen vergunningaanvragen lijkbezorging | Behandelen aanvraag vergunning of ontheffing | Verlenen verlof, Opgraven lijk |
| Behandelen meldingen lijkbezorging | Behandelen melding | Treffen maatregel bij besmet lijk, Verzorgen gemeentebegrafenis |
| Uitbaten begraafplaatsen en crematoria | Uitbaten gemeentelijke voorzieningen | Uitvoeren lijkbezorging, Ruimen graf |
| — (bedrijfsproces specialiseert zelf) | Behandelen aanvraag product; Onderhouden; Opleggen sanctie; nog te bepalen | Verlenen grafrecht; Onderhouden graf; Vervallen verklaren grafrecht; Schouwen lijk |

#### Overige elementen

- **Functies**: *Exploiteren van begraafplaatsen*, *Burgerlijke stand diensten* en waar nodig *Handhaving*, met exacte match.
- **Gebeurtenissen**: Overlijden (start *Bezorgen lijken*), Verval van het grafrecht (start Ruimen graf), Besmet lijk gemeld. Een gebeurtenis hangt onder het levensloopproces van het object waarvan de toestand verandert, en triggert de bedrijfsprocessen die ze start.
- **Objecten**:
  - kernobject: Lijk, Graf, Grafrecht (of een specialisatie: voorleggen), mogelijk Begraafplaats;
  - subobject of onderdeel: Grafbedekking, Plaats van bijzetting, Urn;
  - invoer: Verklaring van overlijden;
  - generiek: Besluit, Beschikking, Vergunning, Heffing, Heffingsverordening, Regeling.
- **Doelgroepen**:
  - gemeente: Gemeente (actor) met Gemeenteraad, College van B&W en Burgemeester; Ambtenaar van de burgerlijke stand en Beheerder;
  - inwoners en ondernemers: Nabestaande, Rechthebbende op het graf, Uitvaartondernemer;
  - ketenpartners: GGD, Kerkgenootschap, Officier van justitie.
- **Actorrelaties**: *Burgemeester is voorzitter van* blijft. *GGD geeft melding door* en *College benoemt lijkschouwer* gaan via rollen en processen of een gebeurtenis.

## Besluiten van de redacteur

Besluiten over de werkwijze en de criteria. Besluiten over afzonderlijke begrippen uit deze analyse staan in [Besluiten van de redacteur](../besluiten/per-begrip.md): Gemeente, Verzorgen lijkbezorging, Verlenen verlof tot begraving of crematie, Officier van justitie, en het beleidsdomein Begraafplaatsen en crematoria.

| Datum | Besluit | Stand |
|---|---|---|
| 2026-10-04 | De GEMMA-indelingen blijven ongewijzigd en worden gevolgd. Een nieuwe indeling komt er alleen waar GEMMA er geen heeft. Bij voorkeur hiërarchisch; anders mag een element meer ouders hebben. | skill criteria (stap 7) |
| 2026-10-04 | Een indeling heeft een naam die zegt wat wordt ingedeeld en waarnaar: *Procesindeling naar soort werk*, *Functie-indeling naar domein*, *Procesindeling naar taak*. | deels herzien door 2026-10-08 (Procesindeling naar kernobject) |
| 2026-10-04 | Processtructuur: taak → één bedrijfs- of ketenproces per kernobject → deelprocessen, die de producten en diensten leveren. Daarnaast clusters naar soort werk binnen de taak, als specialisatie van het generieke GEMMA-proces. | herzien door 2026-10-08 (procesniveaus; de taak vervalt) |
| 2026-10-04 | Een product of dienst valt nooit weg. Wie er een levert, is minstens een deelproces, nooit een processtap. | skill criteria (Procesniveau) en regel Wettelijke grondslag; 'minstens een deelproces' herzien door 2026-10-08 (een bedrijfsproces levert het product of de dienst) |
| 2026-10-04 | Gebeurtenissen komen in beide procesindelingen: onder het proces van het kernobject waarvan de toestand verandert, en als specialisatie van een generieke gebeurtenis. | render (overzichten) en export |
| 2026-10-04 | Bedienende GEMMA-functies worden element met een exacte match; een proces mag door meer functies worden bediend. | geldt (precedent Exploiteren van begraafplaatsen) |
| 2026-10-04 | Een subobject krijgt alleen een pagina als een eigen proces zijn levensloop bepaalt. | skill criteria (Objectniveau) |
| 2026-10-04 | Generieke objecten krijgen nu een kenmerk en verhuizen later naar een algemeen onderwerp; hun domeinspecialisaties krijgen geen pagina en worden genoemd met `via`. | skill criteria (Objectniveau, `via`); verhuizing uitgevoerd 2026-10-06 (onderwerp Algemeen) |
| 2026-10-04 | Tussen actoren alleen structurele relaties (deel van, lid van, voorzitter van); een handeling loopt via rollen en processen of een gebeurtenis. Een actor is een soort partij, nooit een individuele organisatie. | references/relaties.md; skill criteria (soort partij); procesarchitectuur-terugmelding 6 |
| 2026-10-04 | Producten en diensten vallen in de Beleidsdomeinindeling en de Functie-indeling naar domein; interne producten fijner onder bedrijfsfuncties. | skill criteria (indelingsvelden); export |
| 2026-10-04 | Een taak valt in de Beleidsdomeinindeling, onder haar beleidsdomein, zodat ook de bovenste knoop van de Procesindeling naar taak een plaats heeft. Alleen de taak, niet de bedrijfs-, keten- en deelprocessen daaronder. | herzien door 2026-10-08 (de taak vervalt) |
| 2026-10-04 | Een beleidskader hangt bij voorkeur aan een product (regel 595); aan een proces of dienst alleen zolang er geen product is. | references/relaties.md (aangevuld 2026-10-08) |
| 2026-10-04 | Alles wordt ingedeeld, geen wezen: elk element staat in minstens één indeling, ook in de export naar Archi. Een functie zonder GEMMA-match breidt de GEMMA-functieketen uit: ze wordt geaggregeerd door een bestaande GEMMA-functie. | export (rapport: zonder plaats) |
| 2026-10-04 | De Functie-indeling naar domein is een relatie, geen eigenschap: de bovenliggende functie wordt een element, onderbouwd uit de bronnen, en aggregeert de functie eronder, zoals in GEMMA (*Exploitatie fysieke leefomgeving* aggregeert *Exploiteren van begraafplaatsen*). De keten wordt element tot en met de functie op domeinniveau (GEMMA type *Bedrijfsfunctie domein*); alleen die hangt via `domein` aan de domeingroepering. Bij meer GEMMA-ouders de ouder in de keten van het eigen domein. Een nieuwe aggregatie in Archi alleen voorleggen bij twijfel. | export (functieketen) |
| 2026-10-04 | Een functiepagina staat in een map per domein (`bedrijfsfuncties/<domein>/`), niet per taakveld en beleidsdomein: een functie valt alleen in de Functie-indeling naar domein, en een functie op domeinniveau omvat meer taakvelden. | wiki.yaml (bedrijfsfunctie: submap domein) |
| 2026-10-04 | De wiki genereert views per indeling en elementtype. De export blijft zonder views (besluit 2026-10-02); Archi-views staan op de todo. | render (overzichten); Archi-views op todo.md |
| 2026-10-05 | Een product hangt in de Functie-indeling naar domein via `domein` direct aan de domeingroepering, niet onder een functie: ArchiMate laat een functie geen product aggregeren. Het product valt ook in de Beleidsdomeinindeling. De diensten die het omvat hangen onder hun functie. | export |
| 2026-10-05 | Controle op de samenhang tussen de Beleidsdomeinindeling en de Functie-indeling naar domein: het domein van een product of dienst moet passen bij de GEMMA-domeinen die zijn beleidsdomein aggregeren; bij een beleidsdomein dat GEMMA niet kent een signaal als zijn producten en diensten in meer domeinen vallen. | tools/signalen.py |
| 2026-10-05 | Het model mag afwijken van de UPL-indeling (taakveld, GEMMA-domein, beleidsdomein in een GEMMA-domein), mits teruggemeld in de procesarchitectuur-terugmeldingen (`beoordelingen/terugmeldingen/procesarchitectuur.yaml`). | skill beoordelen §7 |
| 2026-10-07 | *Soort partij* betekent: elke gemeente heeft met de partij te maken in dezelfde rol, zodat het element voor alle gemeenten geldt. Het criterium sluit uit wat bij één of enkele gemeenten hoort (gemeente Utrecht, provincie Utrecht), niet een partij die landelijk maar één keer bestaat. Rijk, Provincie en Waterschap zijn een soort partij (de bestuurslaag als geheel); een afzonderlijk ministerie of rijksdienst (minister van BZK, IND) staat in de beschrijving van Rijk. Verduidelijkt het besluit van 2026-10-04 ("nooit een individuele organisatie"). | skill criteria (soort partij) |
| 2026-10-08 | De procesniveaus volgen de GEMMA-ladder: levensloopproces (per kernobject, GEMMA type *Bedrijfsproces (cluster)*) → bedrijfsproces (klant-tot-klant, levert product of dienst) → deelproces (binnen één bedrijfsfunctie). De taak vervalt: boven het levensloopproces staan beleidsdomein en taakveld uit de Beleidsdomeinindeling, afgeleid uit het kernobject. Ketensamenwerking is een bedrijfsinteractie, geen procesniveau. De procesindeling naar soort werk blijft. Herziet de besluiten van 2026-10-04 over de processtructuur en over de taak in de Beleidsdomeinindeling. Zie [Proceshiërarchie](proceshierarchie.md). | skill criteria (Procesniveau) |
| 2026-10-08 | De *Procesindeling naar taak* heet *Procesindeling naar kernobject*: zij deelt de processen in naar hun kernobject. Het niveau heet *levensloopproces*. Afgewezen: *Procesindeling naar levensloop* (zegt minder concreet waarnaar wordt ingedeeld) en *Procesindeling naar beleidsdomein* (het beleidsdomein hoort bij de Beleidsdomeinindeling). Herziet de naam uit het besluit van 2026-10-04. | skill criteria (stap 7); export |
| 2026-10-08 | Een bedrijfsinteractie krijgt een eigen paginatype (*bedrijfsinteractie*), met een kernobject: het object dat door de keten gaat. Ze staat in de Procesindeling naar kernobject bij dat object en, via het beleidsdomein van het kernobject, in de Beleidsdomeinindeling; in Archi in de map *Ketensamenwerking*, zoals in GEMMA. Kernrelatie *toegewezen partij*; elke nieuwe interactie wordt voorgelegd (estafette of orkestratie). Het kenmerk *meer organisaties* vervalt; een keten volgt uit *gezamenlijk gedrag*. Herziet het besluit van 2026-09-30 (Business Interaction herkend). Afgewezen: een paginatype zonder indeling (wijkt af van "geen wezen", 2026-10-04) en herkend laten (de keten zou geen element in Archi zijn). | skill criteria (Ketensamenwerking); wiki.yaml |
| 2026-10-08 | Per kernobject één levensloopproces, of één per partij als ze samen een bedrijfsinteractie met dat kernobject bedienen (Toestaan lijkbezorging en Begraven en cremeren stoffelijk overschot in de ketensamenwerking Bezorgen stoffelijk overschot). Een estafette wordt een bedrijfsinteractie; bij orkestratie is er geen interactie, en het deel dat de gemeente voor een ander uitvoert, specialiseert *Leveren dienst aan derden* (VOG, naturalisatie). Een beleidsdomein krijgt zijn beschrijving in het register `beoordelingen/beleidsdomeinen.yaml`. Zie [Besluiten van de redacteur](../besluiten/per-begrip.md). | skill criteria (Procesniveau); tools/bepaal_type.py |
