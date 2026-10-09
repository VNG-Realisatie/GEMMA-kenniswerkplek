---
id: gemma-kennismodel
type: doc
titel: Elementtypen, kenmerken en het GEMMA-kennismodel
bijgewerkt: '2026-10-08'
bronnen:
- 2026-vng-over-gemma
---

# Elementtypen, kenmerken en het GEMMA-kennismodel

Bron: [Over GEMMA (kennismodel en modelleerafspraken)](../bronanalyses/algemeen/overig/2026-vng-over-gemma.md)

Welke elementtypen en kenmerken heeft het model, en waarom wijken ze af van of volgen ze het GEMMA-kennismodel? Deze analyse vergelijkt de elementtypen van deze wiki, hun kenmerken en de beslistabel met het GEMMA-kennismodel uit Over GEMMA. Ze legt de besluiten van de redacteur vast. Regelnummers verwijzen naar de tekst van Over GEMMA; wat de bron zegt, staat in haar bronanalyse. De besloten opzet van 2026-10-01 is doorgevoerd; de geldende beslistabel staat in [Kenmerken en beslistabel](../kennismodel/kenmerken-en-beslistabel.md).

## Het GEMMA-kennismodel

Wat Over GEMMA over de elementtypen zegt, met per paginatype van deze wiki de GEMMA-naam, de definitie en het verschil, staat in de [bronanalyse van Over GEMMA](../bronanalyses/algemeen/overig/2026-vng-over-gemma.md) (verplaatst 2026-10-08).

## Kenmerkenmatrix: huidige situatie

Rijen zijn de kenmerken, kolommen de elementtypen met hun GEMMA-naam. De laatste vijf typen herkent de beslistabel wel, maar ze hebben geen paginatype: zo'n begrip wordt altijd voorgelegd.

Legenda: **T** bepaalt het type · **K** kernrelatie, moet ja zijn · **D** telt in de drempel · **P** poort voor alle typen · **S** specialisatieniveau · **A** aanvulling (tegenhanger of annotatie) · **x** moet nee zijn voor dit type · **E** vaste uitkomst zonder pagina.

| Kenmerk | Bedrijfsobject | Afspraak | Product | Dienst | Bedrijfsproces | Bedrijfsfunctie | Gebeurtenis | Actor | Rol | Bedrijfssamenwerking | Kanaal | Interactie | Representatie | Locatie |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Scope** | | | | | | | | | | | | | | |
| herkenbaar | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| gemeentelijk | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| buiten kernlagen (moet nee) | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| **Zelfstandigheid** | | | | | | | | | | | | | | |
| betekenis in onderwerp | D | D | D | D | D | D | D | D | D |  |  |  |  |  |
| slechts eigenschap (moet nee) | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| eigen identiteit | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| relaties | D | D | D | D |  |  | D | D | D |  |  |  |  |  |
| zelfstandig beleidsbegrip | S | S | S | S | S | S | S | S | S |  |  |  |  |  |
| **Aard** | | | | | | | | | | | | | | |
| gedrag |  |  |  | T | T | T | T |  |  |  |  | T |  |  |
| handelende partij |  |  |  |  |  |  |  | T |  |  |  |  |  |  |
| hoedanigheid |  |  |  |  |  |  |  |  | T |  |  |  |  |  |
| samenwerkingsverband |  |  |  |  |  |  |  |  |  | T |  |  |  |  |
| toegangspunt |  |  |  |  |  |  |  |  |  |  | T |  |  |  |
| plaats |  |  |  |  |  |  |  |  |  |  |  |  |  | T |
| aanbod als geheel |  |  | T |  |  |  |  |  |  |  |  |  |  |  |
| **Partij** | | | | | | | | | | | | | | |
| los van verantwoordelijkheid |  |  |  |  |  |  |  | T | T |  |  |  |  |  |
| meerdere vervullers |  |  |  |  |  |  |  |  | D |  |  |  |  |  |
| **Soort gedrag** | | | | | | | | | | | | | | |
| per keer doorlopen |  |  |  |  | T |  |  |  |  |  |  |  |  |  |
| gegroepeerd gedrag |  |  |  |  |  | T |  |  |  |  |  |  |  |  |
| toestandsverandering |  |  |  |  |  |  | T |  |  |  |  |  |  |  |
| aangeboden gedrag |  |  |  | T |  |  |  |  |  |  |  |  |  |  |
| gezamenlijk gedrag |  |  |  |  |  |  |  |  |  |  |  | T |  |  |
| **Gedrag** | | | | | | | | | | | | | | |
| toegewezen partij |  |  |  |  | D | D |  |  |  |  |  |  |  |  |
| gebruikt objecten |  |  |  |  | D | D |  |  |  |  |  |  |  |  |
| aanleiding |  |  |  |  | D |  |  |  |  |  |  |  |  |  |
| benoembaar resultaat |  |  |  |  | D |  |  |  |  |  |  |  |  |  |
| herhaald uitgevoerd |  |  |  |  | D |  |  |  |  |  |  |  |  |  |
| eigen normering |  |  |  |  | D |  |  |  |  |  |  |  |  |  |
| stabiel over tijd |  |  |  |  |  | D |  |  |  |  |  |  |  |  |
| **Passief** | | | | | | | | | | | | | | |
| onderscheidbare exemplaren | D | D | D |  |  |  |  | A | A |  |  |  |  |  |
| levenscyclus | D | D |  |  |  |  |  | A | A |  |  |  |  |  |
| wordt bewerkt | D | D |  |  |  |  |  | A | A |  |  |  |  |  |
| afspraak | x | T |  |  |  |  |  |  |  |  |  |  |  |  |
| waarneembare vorm | x | x |  |  |  |  |  |  |  |  |  |  | T |  |
| geautomatiseerd verwerkt | A | A | A | A | A | A | A | A | A |  |  |  |  |  |

Aantal getelde drempelcriteria per type, en hoeveel daarvan ja moeten zijn:

| | Bedrijfsobject | Afspraak | Product | Dienst | Bedrijfsproces | Bedrijfsfunctie | Gebeurtenis | Actor | Rol |
|---|---|---|---|---|---|---|---|---|---|
| criteria in de drempel | 5 | 5 | 3 | 2 | 7 | 4 | 2 | 2 | 3 |
| minimaal ja | 4 | 4 | 2 | 1 | 6 | 3 | 1 | 1 | 2 |

## Bevindingen

- **Ongelijke drempel.** Dienst, gebeurtenis en actor tellen twee criteria, waarvan er één nee mag zijn. Een proces moet er zes van zeven halen.
- **Overlap tussen kenmerken.** *Relaties* telt bij het bedrijfsobject naast *wordt bewerkt*, dat dezelfde toegangsrelatie meet. *Per keer doorlopen* vraagt al naar een resultaat, dat daarna nog eens telt als *benoembaar resultaat*. *Meerdere vervullers* is vrijwel altijd ja; het onderscheid tussen actor en rol maakt *los van verantwoordelijkheid* al.
- **Overlap tussen typen.** Bedrijfsobject en afspraak verschillen alleen op *afspraak*, actor en rol alleen op *los van verantwoordelijkheid*; dat klopt met ArchiMate. Dienst, gebeurtenis en actor hebben dezelfde drempel, en daarin staat niets wat typisch is voor een dienst of gebeurtenis.
- **Ontbrekende kenmerken.** Bij een dienst wordt niet gevraagd naar de afnemer en niet naar het gedrag dat de dienst realiseert. Bij een gebeurtenis wordt niet gevraagd welk gedrag zij start. Bij een product wordt niet gevraagd waaruit het bestaat.
- **Eenzijdige conflictcontrole.** De beslistabel ziet "geen gedrag, wel een soort gedrag" als conflict, maar niet het omgekeerde: een gedragsbegrip met *afspraak* ja wordt zonder melding een proces.
- **Representatie wordt elke keer voorgelegd**, terwijl de redacteur al besliste hoe het moet: vermelden bij het object, geen pagina (Register van begraven lijken, 30 september 2026).

## Relaties: kennismodel en wiki

Het kennismodel legt per typepaar vast welke relatie GEMMA gebruikt. Deze wiki staat de volledige ArchiMate-set toe. Het aantal is het aantal relatierijen op de elementpagina's op 1 oktober 2026.

| Relatie in deze wiki | Aantal | In het kennismodel | Regel |
|---|---|---|---|
| bedrijfsproces → toegang → bedrijfsobject | 18 | ja | 927 |
| bedrijfsobject → associatie of specialisatie → bedrijfsobject | 13 | ja | 905-906 |
| gebeurtenis → triggering → bedrijfsproces | 3 | ja | 915 |
| actor → toewijzing → rol | 2 | ja | 914 |
| bedrijfsproces → specialisatie → bedrijfsproces | 1 | ja | 922 |
| rol → toewijzing → bedrijfsproces | 7 | ja, op het niveau van deelproces; besloten op 1 oktober | 599 |
| rol → associatie → bedrijfsobject | 20 | anders: rol → toegang → bedrijfsobject ("heeft toegang tot") | 916 |
| actor → associatie → bedrijfsobject | 17 | nee: alleen via de rol | 914, 916 |
| actor → toewijzing → bedrijfsproces | 6 | nee: actor → toewijzing → rol | 914 |
| actor → toewijzing → gebeurtenis | 1 | nee | — |
| bedrijfsfunctie → aggregatie → bedrijfsproces | 8 | nee: functie en proces bedienen elkaar | 920, 926 |
| dienst → toegang → bedrijfsobject | 2 | nee | — |
| rol → toewijzing → dienst | 1 | nee: kanaal → toewijzing → dienst | 910 |
| bedrijfsobject → aggregatie → bedrijfsobject | 1 | nee | — |
| bedrijfsproces of bedrijfsfunctie → realisatie → dienst | 0 | ja | 925, 921 |
| dienst → bediening → bedrijfsproces | 0 | ja | 912 |
| bedrijfsproces → triggering → gebeurtenis | 0 | ja | 924 |
| kanaal → toewijzing → dienst; kanaal → bediening → rol | 0 | ja | 910-911 |
| bedrijfssamenwerking → aggregatie → rol | 0 | ja | 913 |
| data-object → realisatie → bedrijfsobject | 0 | ja | 971 |

## Inhoudelijke gevolgen

Deze gevolgen leidden tot de besluiten van 1 oktober 2026 onderaan de pagina.

- **Rol aan proces.** Het besluit van 1 oktober bevestigt wat de wiki al doet: zeven toewijzingen van een rol aan een proces blijven staan. *Toegewezen partij* blijft de kernrelatie van een proces.
- **Actor via de rol.** In GEMMA wordt een actor alleen aan een rol toegewezen (regel 914). In deze wiki staan zes actoren direct aan een proces en één aan een gebeurtenis, en zeventien actoren met een associatie naar een object. Volgt de wiki GEMMA, dan komt er steeds een rol tussen. Dan wordt de kernrelatie van een actor *vervult een rol*.
- **Rol en object.** GEMMA gebruikt "heeft toegang tot", met als betekenissen verantwoordelijk voor, eigenaar van, beheerder van en raadpleger van (regel 916). De twintig associaties van rol naar object passen daar grotendeels in.
- **Functie en proces.** GEMMA laat functie en proces elkaar bedienen (regel 920, 926) en groepeert processen in een procescluster (regel 419). De acht aggregaties van functie naar proces wijken daarvan af. Lijkbezorging en Participatie gedragen zich hier als procescluster.
- **Procesniveau.** (Stand 2026-10-01; uitgewerkt op 2026-10-08 in [Proceshiërarchie](proceshierarchie.md).) GEMMA onderscheidt procescluster, ketenproces, bedrijfsproces, deelproces, processtap en handeling (regel 409-421, 564). Een deelproces wordt binnen één organisatorische eenheid uitgevoerd en levert een bijdrage aan een dienst (regel 388); een processtap ligt binnen één bedrijfsfunctie (regel 387). De beslistabel vraagt nu niet op welk niveau een proces ligt. Schouwen lijk, Opgraven lijk en Ruimen graf kunnen daardoor deelprocessen zijn in GEMMA-termen.
- **Product.** Een product bundelt in GEMMA diensten en afspraken (regel 257) en bedient de klant (regel 596). Het nieuwe kenmerk heet daarom *omvat diensten en afspraken*, niet meer *omvat aanbod* met objecten.
- **Afspraak.** Contract heet in GEMMA Afspraak. De twee elementen van dit type, Uitvoeringsovereenkomst en Grafrecht, blijven inhoudelijk gelijk.
- **Wetgeving.** Het GEMMA-kennismodel noemt wetten en regelgeving als beleidskader in de motivatielaag (regel 448). Het GEMMA-architectuurmodel heeft daarnaast een bedrijfsobject Regeling, overgenomen uit het GGM, waaraan het element Regeling van deze wiki gekoppeld is. GEMMA gebruikt dus beide: het beleidskader als motivatie, de regeling als object dat de gemeente vaststelt, wijzigt en bekendmaakt. De motivatielaag van het GEMMA-model bevat nog geen beleidskaders, alleen kernwaarden.
- **Namen.** De paginatypen bedrijfsdienst, bedrijfsgebeurtenis en contract heten in GEMMA Dienst, Gebeurtenis en Afspraak. In de criteria van deze wiki staan nu de GEMMA-namen en -definities. De technische namen van paginatypen en mappen zijn nog niet aangepast.

## Besluiten van de redacteur

| Datum | Besluit | Stand |
|---|---|---|
| 2026-09-30 | Drempel: per type één kernrelatie die ja moet zijn, plus hoogstens één nee op de overige drempelcriteria. | beslistabel (stap 5, drempel) |
| 2026-09-30 | Nieuwe kenmerken *voert gedrag uit*, *afnemer*, *gerealiseerd door*, *leidt tot gedrag* en *omvat aanbod*; *relaties* en *meerdere vervullers* vervallen. | beslistabel (kenmerken) |
| 2026-09-30 | *Betekenis in onderwerp* wordt een poort: een begrip dat bij een ander onderwerp hoort, krijgt hier een verwijzing en wordt daar beoordeeld. | regel Thuishoren; beslistabel |
| 2026-09-30 | Bedrijfssamenwerking en kanaal worden paginatype. Kanalen vormen één centrale set; een onderwerp koppelt alleen een dienst aan een bestaand kanaal. | skill criteria; wiki.yaml (paginatypen) |
| 2026-09-30 | Product blijft paginatype. Business Interaction blijft herkend en wordt per geval voorgelegd. Representatie en locatie worden een vaste uitkomst zonder pagina. | deels herzien door 2026-10-08 (bedrijfsinteractie wordt paginatype); de rest in skill criteria |
| 2026-10-01 | Over GEMMA is bron. Deze wiki volgt de namen en definities van het GEMMA-kennismodel waar die passen. | skill criteria (ArchiMate-typen) |
| 2026-10-01 | Een rol mag ook aan een bedrijfsproces worden toegewezen, niet alleen aan een bedrijfsfunctie. GEMMA doet dat zelf op het niveau van het deelproces (regel 599); de procesarchitectuur van GEMMA is abstract uitgewerkt, en er is geen andere reden om de relatie weg te laten. | references/relaties.md (toewijzing) |
| 2026-10-01 | Een actor wordt alleen via een rol aan gedrag en objecten gekoppeld, zoals in GEMMA (regel 914). De kernrelatie van een actor wordt *vervult een rol*. | references/relaties.md; beslistabel (vervult een rol) |
| 2026-10-01 | Een relatie van rol naar object wordt gesplitst: wat de rol met het object ís, wordt toegang met een getypeerde naam (raadpleger, beheerder, eigenaar, verantwoordelijke; de lijst volgt de indeling uit de Wet basisregistraties en wordt nog vastgesteld). Een handeling, zoals aanvragen of afgeven, wordt een toewijzing van de rol aan een proces dat het object gebruikt of maakt. | references/relaties.md; uitgewerkt in Toegang tot een bedrijfsobject |
| 2026-10-01 | Een bedrijfsfunctie bedient een bedrijfsproces, zoals in GEMMA (regel 920); de aggregatie van functie naar proces vervalt. Een proces mag meerdere functies gebruiken. | references/relaties.md (bediening) |
| 2026-10-01 | Een bedrijfsproces krijgt het veld *procesniveau* (bedrijfsproces of deelproces). Een deelproces krijgt een pagina als het de procesdrempel haalt, en hangt met een aggregatie onder een bedrijfsproces ("is opgebouwd uit", regel 396). Processtap en handeling worden nooit een pagina. | herzien door 2026-10-08 (procesniveaus volgens de GEMMA-ladder; een deelproces krijgt geen pagina) |
| 2026-10-01 | Een concrete wet of verordening wordt een beleidskader (Driver, regel 448) in een nieuwe map `motivatie/` naast `bedrijfsarchitectuur/`, met "geeft grondslag aan" naar GEMMA-kwaliteitsdoelen waar dat aanwijsbaar is (regel 458). Alleen beleidskaders; andere motivatietypen blijven buiten dit model. Het generieke bedrijfsobject Regeling blijft voor het vaststellen, wijzigen en bekendmaken, met een associatie naar het beleidskader. | skill criteria (regeling); wiki.yaml (motivatie/beleidskaders); de relatie heet nu *is grondslag voor* (regel Wettelijke grondslag) |
| 2026-10-01 | De paginatypen bedrijfsdienst en bedrijfsgebeurtenis en hun mappen worden hernoemd naar dienst en gebeurtenis; de nieuwe typen heten bedrijfssamenwerking en kanaal. Engelse ArchiMate-sleutels blijven. Dit gaat mee met de herziening van de beslistabel. | uitgevoerd (wiki.yaml) |
| 2026-10-01 | Na de herziening worden alle bestaande elementen opnieuw beoordeeld, met een run per onderwerp. Elke wijziging van type, relatie of status wordt apart voorgelegd; een element waarvan alleen een kenmerk is aangevuld, houdt zijn status. | uitgevoerd voor lijkbezorging; participatie volgt (todo.md) |
| 2026-10-01 | Een beleidskader is rijks- of EU-regelgeving of een VNG-modelverordening die een taak, bevoegdheid of plicht van de gemeente regelt. Kernrelatie: een associatie "is grondslag voor" naar minstens één proces, dienst of product. Lokale verordeningen en beleidsnota's blijven bron; een wet die alleen een definitie levert ook; een losse norm uit een artikel blijft buiten het model. Kenmerken voor de beslistabel: herkenbaar, gemeentelijk, in werking, regelt een taak, bevoegdheid of plicht van de gemeente. | regel Wettelijke grondslag; skill criteria (regeling) |
| 2026-10-08 | Ook een landelijke richtlijn als geheel (uitvoeringsvoorschrift, handleiding of circulaire van een landelijke organisatie, zoals de HUP of de Circulaire adresonderzoek BRP) kan een beleidskader zijn, met regelgever *landelijke organisatie* en groep Richtlijn. Het is geen wettelijke grondslag: de relatie heet "geeft richtlijn voor". Past bij de definitie van Beleidskader in GEMMA: gebaseerd op bestaand overheidsbeleid en de instrumenten die in het kader daarvan zijn ontwikkeld. | regel Wettelijke grondslag; skill criteria (regeling) |
| 2026-10-08 | Een Business Interaction wordt paginatype *bedrijfsinteractie*, met een kernobject; een ketensamenwerking is een bedrijfsinteractie, bediend door de bedrijfsprocessen van de partijen (GEMMA Online, Proceshiërarchie). Elke nieuwe interactie wordt voorgelegd. Herziet het besluit van 2026-09-30. De procesniveaus zijn levensloopproces, bedrijfsproces en cluster naar soort werk; deelproces en processtap krijgen meestal geen pagina. Herziet het besluit van 2026-10-01 over het veld *procesniveau*. Zie [Proceshiërarchie](proceshierarchie.md) en [Indelingen](indelingen.md). | skill criteria (Ketensamenwerking); wiki.yaml |

## Open vragen

Geen. De vragen van 1 oktober 2026 zijn beantwoord; zie de besluiten hierboven. De namen voor de toegang tot een object (verantwoordelijkheden van een rol en handelingen van een functie of proces) zijn uitgewerkt en besloten in [Toegang tot een bedrijfsobject](gegevensrollen.md).
