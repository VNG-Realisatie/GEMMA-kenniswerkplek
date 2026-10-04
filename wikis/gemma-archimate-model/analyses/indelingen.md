---
id: indelingen
type: analyse
titel: Indelingen van de bedrijfsarchitectuur
bijgewerkt: '2026-10-04'
bronnen:
- 2026-vng-over-gemma
- 2026-vng-gemma-2026-10-02
---

# Indelingen van de bedrijfsarchitectuur

Bronnen: Over GEMMA [tekst](../../../sources/raw/2026-vng-over-gemma.md) (regelnummers verwijzen hiernaar) · GEMMA-architectuurmodel [origineel](../../../sources/raw/2026-vng-gemma-2026-10-02.archimate), gelezen via `tools/gemma.py` · [Producten en diensten procesarchitectuur](https://www.gemmaonline.nl/wiki/Producten_en_diensten_procesarchitectuur) op GEMMA Online, met de externe UPL-lijst (506 regels) en de interne lijst (587 regels). De UPL-lijsten zijn hier analysemateriaal en nog geen bron van de wiki (todo).

Hoe het model wordt ingedeeld in de hele breedte van de bedrijfsarchitectuur: welke indelingen GEMMA heeft, welke erbij komen, welk elementtype waar valt, en welke kenmerken en regels daarvoor nodig zijn. Aanleiding: lijkbezorging was plat en fijnmazig (één functie voor negen processen, vijftien bedrijfsobjecten naast elkaar). Doel: een compleet GEMMA-model op het juiste abstractieniveau, met een indeling die ook in Archi zichtbaar is. De besluiten staan onderaan; de omzetting in de beslistabel volgt.

## Begrippen

### Indeling en view

- **Indeling**: een ordening naar één criterium, met benoemde niveaus. Gebruikt een tweede elementtype hetzelfde criterium, dan wordt het in de bestaande indeling ingedeeld; er komt geen nieuwe.
- **View**: een weergave van één indeling voor één of meer elementtypen, bijvoorbeeld *Bedrijfsobjecten per beleidsdomein*.
- **Specialisatie of aggregatie**: specialisatie koppelt aan een GEMMA-indeling (wat voor soort is het?), aggregatie aan een eigen indeling (waar hoort het bij?).

### Procesniveaus

- **Taak**: een procescluster voor een gemeentelijke taak als geheel (*Verzorgen lijkbezorging*). Een procescluster wordt niet per geval doorlopen (regel 409, 419-420); in ArchiMate een business-process.
- **Bedrijfsproces**: per kernobject het gedrag over de levensloop van één exemplaar, onder verantwoordelijkheid van één organisatie (*Beheren grafrechten*: van uitgifte tot verval). Dit volgt de GEMMA-definitie (regel 573).
- **Ketenproces**: hetzelfde, maar uitgevoerd door meer organisaties (regel 564), zoals *Bezorgen lijken*.
- **Deelproces (werkproces)**: één mutatie, besluit, product of dienst binnen het proces van een kernobject (*Verlenen grafrecht*), in principe binnen één organisatorische eenheid (regel 571). Deelprocessen leveren de producten en diensten.
- **Cluster naar soort werk**: de deelprocessen van één soort binnen een taak, als specialisatie van een generiek GEMMA-bedrijfsproces. Alleen bij minstens twee deelprocessen; anders specialiseert het deelproces zelf.
- **Processtap**, **handeling**: geen pagina (regel 560, 563).

### Objectniveaus

- **Kernobject**: het bedrijfsobject waarvan één bedrijfsproces of ketenproces de hele levensloop omvat.
- **Subobject**: een deel van een kernobject, met een eigen proces.
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
| Procesindeling naar soort werk | GEMMA, per taak uitgebreid | deelprocessen; via generieke GEMMA-elementen ook gebeurtenissen, diensten en rollen | generiek GEMMA-proces → cluster naar soort werk → deelproces | specialisatie naar het GEMMA-element (exacte match); aggregatie |
| Procesindeling naar taak | nieuw | bedrijfs-, keten- en deelprocessen, gebeurtenissen | taak → bedrijfs- of ketenproces per kernobject → deelproces | aggregatie; map `wiki-gemma-model / Procesindeling naar taak` |
| Functie-indeling naar domein | GEMMA | functies, producten, diensten | domein → functie → product of dienst | aggregatie; functie bedient proces |
| Beleidsdomeinindeling | GEMMA | objecten, afspraken, producten, diensten, beleidskaders, taken | taakveld → beleidsdomein → element | aggregatie vanuit de groepering |
| Doelgroepindeling | GEMMA, uitgebreid | rollen, actoren, samenwerkingen, kanalen | gemeente (bestuursorgaan, ambtelijk), inwoners en ondernemers, ketenpartners → element | aggregatie vanuit de doelgroeprol |

Een deelproces heeft twee ouders: het proces van zijn kernobject en zijn cluster naar soort werk. Een deelproces uit een andere taak mag ook in een ketenproces hangen; dat geeft een signaal.

#### Hergebruik

Een product- en dienstindeling, beleidskaderindeling en kanaalindeling zijn geen eigen indelingen:
- producten en diensten vallen in de Beleidsdomeinindeling en de Functie-indeling (twee ouders; de UPL draagt beide als kolom);
- beleidskaders vallen in de Beleidsdomeinindeling, met de regelgever als eigenschap;
- een taak valt in de Beleidsdomeinindeling, omdat er in de Procesindeling naar taak niets boven haar staat;
- kanalen vallen in de Doelgroepindeling, met fysiek of digitaal als eigenschap.

Verder:
- de Applicatieservice-indeling combineert domein en doelgroep;
- een cluster naar soort werk breidt het processenlandschap uit zonder GEMMA-elementen te wijzigen.

#### Taak en beleidsdomein

De taak is geen hergebruik van het beleidsdomein:
- GEMMA kent geen beleidsdomein *Begraafplaatsen en crematoria*; onder taakveld 7 staat alleen *Afval*, en *Gemeentebegrafenissen* valt onder 6;
- de UPL zet het verlof tot begraven onder 0.2 (Burgerzaken), de rest onder 7.5.

De taak blijft dus een eigen niveau, met een hoofdbeleidsdomein als eigenschap.

#### Views

| Indeling | Views |
|---|---|
| Procesindeling naar soort werk | Deelprocessen per cluster en generiek GEMMA-proces |
| Procesindeling naar taak | Per taak: processen per kernobject, deelprocessen met producten en diensten, gebeurtenissen; per ketenproces de deelprocessen in volgorde met de organisaties |
| Functie-indeling naar domein | Functies die processen bedienen; Producten en diensten per functie |
| Beleidsdomeinindeling | Bedrijfsobjecten (kern- en subobjecten), Producten en diensten, Beleidskaders per beleidsdomein |
| Doelgroepindeling | Actoren en rollen per doelgroep; Kanalen per doelgroep |

## Processtructuur

### Eén bedrijfsproces per kernobject

Een gemeente levert meer dan 500 externe en 587 interne producten en diensten; GEMMA dekt ze met zo'n 50 generieke bedrijfsprocessen. Eén bedrijfsproces per product maakt het model plat. Eén per kernobject zit daartussen: herkenbaar per taak, en het aantal groeit met het aantal kernobjecten, niet met het aantal producten. Deelprocessen leveren de producten. Het cluster naar soort werk houdt de aansluiting op het processenlandschap. GEMMA kent ook processen die een levensloop omvatten (*Onderhouden*, *Heffen en innen*).

### Toets aan het Kennismodel procesarchitectuur

Het kennismodel (regel 544-606) is work in progress.

| Kennismodel (regel) | Wiki | Oordeel |
|---|---|---|
| Actor → toewijzing → Rol (602) | actor alleen via een rol | volgt |
| Rol → toewijzing → Deelproces (599) | rol aan deelproces; aan bedrijfsproces mag | volgt |
| Product → bediening → Klant (596) | *afnemer* noemt een specialisatie van Klant; het product bedient die rol | volgt (toegevoegd) |
| Product → associatie → Beleidskader (595) | *is grondslag voor* bij voorkeur van een product, tijdelijk van proces of dienst | volgt, met overgang |
| Product → aggregatie → Dienst (593) | *omvat diensten en afspraken* | volgt |
| Bedrijfsfunctie ↔ bediening ↔ Bedrijfsproces (597, 604) | *bedient gedrag* | volgt |
| Bedrijfsproces → aggregatie → Deelproces → Processtap → Handeling (605, 601, 589) | procesniveaus | volgt |
| Bedrijfsproces → toegang → Bedrijfsobject (606) | kernobject via toegang | volgt |
| Procescluster → aggregatie → Bedrijfsproces, Procescluster (419-420) | taak en cluster naar soort werk | volgt |
| Deelproces → realisatie → Deelservice (398) | een deelproces levert een dienst | afwijking, signaal |
| Ketenproces → aggregatie → Bedrijfsproces (590) | een ketenproces aggregeert deelprocessen, ook uit andere taken | afwijking, signaal |
| Relaties tussen actoren: niet in het kennismodel | alleen structurele relaties | aanvulling |
| Gebeurtenis: niet in deze view | uit het uitgebreide kennismodel (regel 915, 924) | aanvulling |

De afwijkingen en aanvullingen gaan als voorstel naar het GEMMA-team (todo).

## Kenmerken en beslistabel

### Per elementtype

Een **vet** woord is nieuw of gewijzigd ten opzichte van de beslistabel van 2026-10-01.

| Type | Bepaald door | Kernrelatie | Drempel | Eigen pagina | Indeling |
|---|---|---|---|---|---|
| Bedrijfsobject, afspraak | geen aard; *afspraak* | *wordt bewerkt* | *onderscheidbare exemplaren*, *levenscyclus* | **objectniveau**; *zelfstandige specialisatie* | Beleidsdomein |
| Product | *aanbod als geheel* | *omvat diensten en afspraken* | *afnemer* (**klantrol, met bediening**), *benoembaar resultaat* | **zelfstandig aanbod** | Beleidsdomein en Functie |
| Dienst | *aangeboden gedrag* | *gerealiseerd door* (**deel-, bedrijfs- of ketenproces, of functie**) | *afnemer*, *benoembaar resultaat* | **generiek** → specialisatie | Beleidsdomein en Functie |
| Taak | **groepeert processen** | **omvat processen** (minstens 2 per kernobject) | *toegewezen partij* | — | Naar taak |
| Cluster naar soort werk | **groepeert processen** | **omvat processen** (minstens 2 deelprocessen) en specialisatie naar GEMMA | — | anders specialiseert het deelproces | Naar soort werk |
| Bedrijfsproces, ketenproces | *per keer doorlopen* en **omvat levensloop**; keten: **meer organisaties** | *toegewezen partij* | *aanleiding*, *benoembaar resultaat* | **procesniveau** | Naar taak |
| Deelproces | *per keer doorlopen* en *bijdrage aan groter proces* | *toegewezen partij* | pagina bij *eigen besluit*, *eigen normering* of **levert aanbod** | **procesniveau** | Naar taak en naar soort werk |
| Bedrijfsfunctie | *gegroepeerd gedrag* | **bedient gedrag** | *toegewezen partij*, *gebruikt objecten*, *stabiel over tijd* | **in functie-indeling** | Functie |
| Gebeurtenis | *toestandsverandering* | *leidt tot gedrag* | *komt herhaald voor* | **generiek** → specialisatie | Naar taak |
| Actor, bedrijfssamenwerking | partij of verband | *vervult een rol*, *voert gedrag uit* | — | **soort partij** | Doelgroep |
| Rol | *hoedanigheid* | *voert gedrag uit* | — | *zelfstandige specialisatie*; **generiek** → specialisatie | Doelgroep |
| Kanaal | *toegangspunt* | *ontsluit een dienst* | — | centrale set | Doelgroep |
| Beleidskader | *regeling als geheel*, *landelijk* | *is grondslag voor* (**bij voorkeur van een product**) | *in werking* | regeling als geheel | Beleidsdomein |
| Interaction | *gezamenlijk gedrag* | — | — | herkend, voorleggen | als deelproces |
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
| Soort gedrag | *groepeert processen* | Is het een groepering van processen rond één taak of één soort werk, die niet per geval wordt doorlopen? |
| Gedrag | *omvat processen* | Omvat het minstens twee processen? Noem ze. |
| Gedrag | *omvat levensloop* | Omvat het het gedrag over de hele levensloop van één exemplaar van een bedrijfsobject? Noem het object. |
| Gedrag | *meer organisaties* | Voeren twee of meer organisaties het samen uit, elk vanuit een eigen rol, niet als klant of alleen als adviseur? Noem ze. |
| Gedrag | *eigen besluit* | Eindigt het in een besluit van een bevoegd orgaan of mandataris? Noem orgaan en artikel. |
| Gedrag | *levert aanbod* | Realiseert het een dienst of levert het een product aan een afnemer? Noem het (referentie: de UPL). |
| Gedrag | *bedient gedrag* | Ondersteunt de functie aanwijsbaar een proces? Noem het. |
| Gedrag | *in functie-indeling* | Past de functie als onderwerp onder een soort werk in de Functie-indeling naar domein? Noem de bovenliggende functie. |
| Gedrag | *leidt tot gebeurtenis* | Eindigt het in een benoemde toestandsverandering, of in een die een ander proces start? Noem die. |
| Partij | *soort partij* | Komt deze partij met dezelfde rol bij elke gemeente voor, en is het geen individuele organisatie? |
| Passief | *deel van object* | Is het een onderdeel van één ander object, dat ermee ontstaat en eindigt? Noem dat object. |
| Passief | *invoer van een ander* | Maakt en beheert een andere partij het, terwijl de gemeente het alleen ontvangt of raadpleegt? Noem de maker. |
| Passief | *zelfstandig aanbod* | Wordt het onder eigen naam aangeboden, en niet als variant of tarief? |
| Specialisatie | *generiek* | Komt het met dezelfde betekenis in veel onderwerpen voor? |

Hergebruikt worden: *per keer doorlopen*, *aanleiding*, *afnemer*, *benoembaar resultaat*, *eigen normering*, *bijdrage aan groter proces* (nu: één mutatie binnen het proces van een kernobject), *zelfstandige specialisatie* en *leidt tot gedrag*.

**Indelingsvelden**, verplicht per type: `taakveld` en `beleidsdomein` (bestaan), `domein` (functie, product, dienst), `doelgroep` (actor, rol, samenwerking, kanaal), `regelgever` (beleidskader), `kernobject` (bedrijfs- en ketenproces), `afnemer` (processen, product, dienst).

### Stap 7: indeling

Een nieuwe stap na stap 6, met de context van alle uitkomsten.

#### Proces

- Taak bij *groepeert processen* zonder specialisatie naar GEMMA; minstens twee processen per kernobject, anders voorleggen.
- Cluster naar soort werk bij *groepeert processen* met een specialisatie naar GEMMA; minstens twee deelprocessen.
- Ketenproces bij *omvat levensloop* en *meer organisaties*; bedrijfsproces bij *omvat levensloop* zonder *meer organisaties*.
- Deelproces bij *bijdrage aan groter proces* met *eigen besluit*, *eigen normering* of *levert aanbod*. Wie een product of dienst levert, is nooit een processtap.
- Anders processtap: geen pagina; de tekst gaat naar het deelproces.

#### Object

- *generiek* → generiek.
- `kernobject` van een proces → kernobject (per kernobject precies één proces).
- *deel van object* met een eigen deelproces → subobject; zonder → onderdeel, geen pagina.
- *invoer van een ander* → geen pagina; vermeld bij het proces.
- Anders voorleggen.

Bij gebeurtenis, rol en dienst geeft *generiek* een specialisatie van een GEMMA-element met exacte match. Ontbreekt dat element, dan voorleggen als voorstel aan GEMMA.

#### Controles

- Elk element staat in zijn verplichte indeling. Meer ouders geeft een signaal, behalve de twee ouders van een deelproces.
- Een functie onder domeinniveau wordt geaggregeerd door één bovenliggende GEMMA-functie in hetzelfde domein, volgens de GEMMA-functieketen; een functie op domeinniveau hangt via `domein` aan de domeingroepering. Een product of dienst wordt geaggregeerd door één functie in hetzelfde domein.
- Specialisatie en bediening naar GEMMA lopen alleen via een exacte match.
- *leidt tot gebeurtenis* vraagt een triggering.
- `via` wijst naar een specialisatie van het doel.
- Signalen bij:
  - een actorrelatie met een werkwoord van gedrag;
  - een beleidskader zonder product;
  - een deelproces dat een dienst levert;
  - een ketenproces met deelprocessen uit een andere taak.

## Lijkbezorging

### IJking met de UPL

De externe UPL-lijst over lijkbezorging, met het proces dat elk product levert:

| UPL-product (Iv3, grondslag) | Levert | Stap 7 |
|---|---|---|
| grafuitgifte (7.5, model-beheersverordening art. 11) | Verlenen grafrecht | deelproces van *Beheren grafrechten* |
| grafrechten (7.5, Gemeentewet art. 229) | generiek *Heffen en innen* | geen domeinproces |
| grafonderhoud (7.5) | Onderhouden graf | deelproces van *Beheren graven* |
| gedenkteken plaatsingsvergunning (7.5, art. 19) | nog geen proces | gat: deelproces van *Beheren graven*; Grafbedekking wordt subobject |
| herbegraven of alsnog cremeren (7.5, Wlb art. 29) | Opgraven lijk | deelproces van *Bezorgen lijken* |
| verlof tot begraven (0.2, Wlb art. 11) | Verlenen verlof tot begraving of crematie | deelproces van *Bezorgen lijken* |
| asverstrooiing (7.5, model-APV art. 5:36) | nog geen proces | gat: de APV is geen bron |
| bijzondere begraafplaats toestemming (7.5, Wlb art. 40-41) | nog geen proces | gat: proces rond Begraafplaats |
| ontleding stoffelijk overschot toestemming (Wlb art. 67) | nog geen proces | gat: deelproces van *Bezorgen lijken* |
| vervoersdocumenten stoffelijk overschot (7.5, Besluit op de lijkbezorging art. 11) | nog geen proces | gat: het besluit is geen bron |
| begraafplaats-, bijzettingen-, crematoriumregister (7.5, Wlb art. 27, 65, 50) | representatie bij Graf | dienst (raadplegen) |
| overlijdensaangifte, overlijdensakte (0.2, BW 1 art. 19h, 19f) | onderwerp Burgerzaken | ook in *Bezorgen lijken* |

Uitkomst:
- Elk product komt uit bij een deelproces of bij het generieke proces; geen product wordt een eigen bedrijfsproces.
- De ijking vindt vier ontbrekende deelprocessen, plus asverstrooiing. De UPL-grondslagen wijzen de bronnen aan (todo).
- Begraafplaats is mogelijk een kernobject met een proces *Beheren begraafplaatsen*.

### Inschatting

Ter toetsing in de herbeoordeling. Elk verlies van een pagina en elke nieuwe GEMMA-koppeling wordt apart voorgelegd.

#### Procesindeling naar taak

```
Verzorgen lijkbezorging                         taak
├─ Bezorgen lijken                              ketenproces, kernobject Lijk
│   ├─ Schouwen lijk                            deelproces
│   ├─ Verlenen verlof tot begraving of crematie deelproces → verlof tot begraven
│   ├─ Uitvoeren lijkbezorging                  deelproces
│   ├─ Opgraven lijk                            deelproces → herbegraven of alsnog cremeren
│   ├─ Verzorgen gemeentebegrafenis             deelproces
│   └─ Treffen maatregel bij besmet lijk        deelproces
├─ Beheren grafrechten                          bedrijfsproces, kernobject Grafrecht
│   ├─ Verlenen grafrecht                       deelproces → grafuitgifte
│   └─ Vervallen verklaren grafrecht            deelproces
└─ Beheren graven                               bedrijfsproces, kernobject Graf
    ├─ Ruimen graf                              deelproces
    └─ Onderhouden graf                         deelproces → grafonderhoud
```

#### Procesindeling naar soort werk

| Cluster naar soort werk | Generiek GEMMA-proces | Deelprocessen |
|---|---|---|
| Behandelen vergunningaanvragen lijkbezorging | Behandelen aanvraag vergunning of ontheffing | Verlenen verlof, Opgraven lijk |
| Behandelen meldingen lijkbezorging | Behandelen melding | Treffen maatregel bij besmet lijk, Verzorgen gemeentebegrafenis |
| Uitbaten begraafplaatsen en crematoria | Uitbaten gemeentelijke voorzieningen | Uitvoeren lijkbezorging, Ruimen graf |
| — (deelproces specialiseert zelf) | Behandelen aanvraag product; Onderhouden; Opleggen sanctie; nog te bepalen | Verlenen grafrecht; Onderhouden graf; Vervallen verklaren grafrecht; Schouwen lijk |

#### Overige elementen

- **Functies**: *Exploiteren van begraafplaatsen*, *Burgerlijke stand diensten* en waar nodig *Handhaving*, met exacte match.
- **Gebeurtenissen**: Overlijden (start *Bezorgen lijken*), Verval van het grafrecht (start Ruimen graf), Besmet lijk gemeld.
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

Besluiten over de werkwijze en de criteria. Besluiten over afzonderlijke begrippen uit deze analyse staan in [Besluiten van de redacteur](besluiten-redacteur.md): Gemeente, Verzorgen lijkbezorging, Verlenen verlof tot begraving of crematie, Officier van justitie, en het beleidsdomein Begraafplaatsen en crematoria.

| Datum | Besluit |
|---|---|
| 2026-10-04 | De GEMMA-indelingen blijven ongewijzigd en worden gevolgd. Een nieuwe indeling komt er alleen waar GEMMA er geen heeft. Bij voorkeur hiërarchisch; anders mag een element meer ouders hebben. |
| 2026-10-04 | Een indeling heeft een naam die zegt wat wordt ingedeeld en waarnaar: *Procesindeling naar soort werk*, *Functie-indeling naar domein*, *Procesindeling naar taak*. |
| 2026-10-04 | Processtructuur: taak → één bedrijfs- of ketenproces per kernobject → deelprocessen, die de producten en diensten leveren. Daarnaast clusters naar soort werk binnen de taak, als specialisatie van het generieke GEMMA-proces. |
| 2026-10-04 | Een product of dienst valt nooit weg. Wie er een levert, is minstens een deelproces, nooit een processtap. |
| 2026-10-04 | Gebeurtenissen komen in beide procesindelingen: onder het proces van het kernobject waarvan de toestand verandert, en als specialisatie van een generieke gebeurtenis. |
| 2026-10-04 | Bedienende GEMMA-functies worden element met een exacte match; een proces mag door meer functies worden bediend. |
| 2026-10-04 | Een subobject krijgt alleen een pagina als een eigen proces zijn levensloop bepaalt. |
| 2026-10-04 | Generieke objecten krijgen nu een kenmerk en verhuizen later naar een algemeen onderwerp; hun domeinspecialisaties krijgen geen pagina en worden genoemd met `via`. |
| 2026-10-04 | Tussen actoren alleen structurele relaties (deel van, lid van, voorzitter van); een handeling loopt via rollen en processen of een gebeurtenis. Een actor is een soort partij, nooit een individuele organisatie. |
| 2026-10-04 | Producten en diensten vallen in de Beleidsdomeinindeling en de Functie-indeling naar domein; interne producten fijner onder bedrijfsfuncties. |
| 2026-10-04 | Een taak valt in de Beleidsdomeinindeling, onder haar beleidsdomein, zodat ook de bovenste knoop van de Procesindeling naar taak een plaats heeft. Alleen de taak, niet de bedrijfs-, keten- en deelprocessen daaronder. |
| 2026-10-04 | Een beleidskader hangt bij voorkeur aan een product (regel 595); aan een proces of dienst alleen zolang er geen product is. |
| 2026-10-04 | Alles wordt ingedeeld, geen wezen: elk element staat in minstens één indeling, ook in de export naar Archi. Een functie zonder GEMMA-match breidt de GEMMA-functieketen uit: ze wordt geaggregeerd door een bestaande GEMMA-functie. |
| 2026-10-04 | De Functie-indeling naar domein is een relatie, geen eigenschap: de bovenliggende functie wordt een element, onderbouwd uit de bronnen, en aggregeert de functie eronder, zoals in GEMMA (*Exploitatie fysieke leefomgeving* aggregeert *Exploiteren van begraafplaatsen*). De keten wordt element tot en met de functie op domeinniveau (GEMMA type *Bedrijfsfunctie domein*); alleen die hangt via `domein` aan de domeingroepering. Bij meer GEMMA-ouders de ouder in de keten van het eigen domein. Een nieuwe aggregatie in Archi alleen voorleggen bij twijfel. |
| 2026-10-04 | Een functiepagina staat in een map per domein (`bedrijfsfuncties/<domein>/`), niet per taakveld en beleidsdomein: een functie valt alleen in de Functie-indeling naar domein, en een functie op domeinniveau omvat meer taakvelden. |
| 2026-10-04 | De wiki genereert views per indeling en elementtype. De export blijft zonder views (besluit 2026-10-02); Archi-views staan op de todo. |
