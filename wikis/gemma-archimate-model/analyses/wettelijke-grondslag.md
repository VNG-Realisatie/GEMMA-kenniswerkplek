---
id: wettelijke-grondslag
type: analyse
titel: Wettelijke grondslag
bijgewerkt: '2026-10-08'
bronnen:
- 2026-rijk-wet-brp-bwbr0033715
- 2026-rijk-wegenverkeerswet-1994-bwbr0006622
- 2026-rijk-reglement-rijbewijzen-bwbr0008074
- 2026-rijk-wet-griffierechten-burgerlijke-zaken-bwbr0028899
- 2026-rijk-gemeentewet-wettekst
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2010-vng-model-beheersverordening-begraafplaatsen
- 2023-vng-model-apv
- 2025-vng-upl-producten-en-diensten-extern
- 2023-rvig-circulaire-adresonderzoek-brp
---

# Wettelijke grondslag

Aanleiding: in burgerzaken staan vier diensten zonder wettelijke grondslag, waaronder Gewaarmerkte kopie reisdocument aanvragen, die alleen op de productpagina van Utrecht steunt. De redacteur stelt op 2026-10-08 de regel Wettelijke grondslag vast (`AGENTS.md`). Deze analyse meet welke elementen geen landelijke wettelijke bron hebben, zoekt die bron alsnog op en geeft per geval een advies. De beoordelingen zijn nog niet aangepast: dat gaat per geval na een besluit van de redacteur (regel Per geval).

## Groepen in de Regelgevingindeling

Een beleidskader staat naast de Beleidsdomeinindeling in de Regelgevingindeling, onder het brontype van zijn regeling, afgeleid uit het veld `regelgever` (export: map `Other / wiki-gemma-model / Regelgevingindeling`, aggregatie vanuit de groep).

| Groep en map | Brontype | Regelgever |
|---|---|---|
| Europese regelgeving | `europese-regelgeving` | EU |
| Rijksregelgeving | `rijksregelgeving` | rijk |
| Richtlijn | `richtlijn` | landelijke organisatie |
| Gemeentelijke regelgeving | `gemeentelijke-regelgeving` | VNG-model |

De omschrijving van elke groep is die van het brontype in de regel Bronvoorrang (`AGENTS.md`); de export neemt haar als documentatie van de groep over.

Nu in het model: 15 beleidskaders in Rijksregelgeving en 2 in Gemeentelijke regelgeving (Model beheersverordening begraafplaatsen, Model-APV); Europese regelgeving is nog leeg en wordt dus niet geëxporteerd. Een beleidskader in Gemeentelijke regelgeving is alleen grondslag voor een UPL-product of -dienst, niet voor een proces of object.

### Wat valt onder gemeentelijke regelgeving

| Soort | Vastgesteld door | Grondslag in de wet | Telt als grondslag van een UPL-product? |
|---|---|---|---|
| Autonome verordening, waaronder de APV | raad | Gemeentewet art. 108 lid 1, 147, 149 | ja, via het VNG-model (Model-APV) |
| Verordening in medebewind (Wmo, Participatiewet, Jeugdwet) | raad | de bijzondere wet die de verordening opdraagt | de bijzondere wet is zelf landelijke grondslag |
| Belasting- en legesverordening | raad | Gemeentewet art. 216, 219 e.v., 229 | alleen voor het tarief, niet voor de dienst zelf |
| Omgevingsplan | raad | Omgevingswet art. 2.4 | ja, via de VNG-staalkaarten |
| Nadere regels | college of burgemeester, gedelegeerd in een verordening | de verordening | als deel van die verordening |
| Regeling van een gemeenschappelijke regeling | bestuur van de GR | Wet gemeenschappelijke regelingen | alleen als VNG-model; anders bron |
| Beleidsregel | bestuursorgaan | Awb art. 4:81 | nee: niet algemeen verbindend, alleen beleid |

Provinciale en waterschapsverordeningen binden de gemeente ook, maar verschillen per provincie of waterschap; ze vallen buiten beide groepen.

## Telling

Maat: het element noemt een landelijke wettelijke bron (toen brontype `wet`, nu `europese-regelgeving` of `rijksregelgeving`) bij een kenmerk of relatie, of het heeft een inkomende relatie *is grondslag voor* van een beleidskader in Europese regelgeving of Rijksregelgeving. Beleidskaders zelf tellen niet mee.

| Type | Met landelijke wettelijke bron | Zonder |
|---|---|---|
| Actor | 10 | 0 |
| Bedrijfsfunctie | 11 | 3 |
| Bedrijfsinteractie | 1 | 0 |
| Bedrijfsobject | 20 | 3 |
| Bedrijfsproces | 68 | 9 |
| Dienst | 70 | 7 |
| Gebeurtenis | 17 | 3 |
| Product | 0 | 1 |
| Rol | 20 | 5 |
| **Totaal** | **217** | **31** |

De meeste van de 31 hebben wel een wet, maar noemen die niet: ze steunen op de HUP van RvIG, het GGM, de UPL of een gemeentelijke bron. Daarnaast hebben 16 diensten en producten wel een wettelijke bron in hun kenmerken, maar geen relatie *is grondslag voor* (onder D).

## A. Wet bestaat, alleen niet genoemd: behouden en de bron toevoegen

Alle artikelen hieronder zijn in de wettekst nagelezen, behalve waar "artikel te bepalen" staat.

| Element | Type | Landelijke grondslag |
|---|---|---|
| Briefadres | bedrijfsobject | [Wet BRP](../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) art. 2.23, 2.40 |
| Inschrijven op briefadres | bedrijfsproces | Wet BRP art. 2.23, 2.40 |
| Briefadresgever | rol | Wet BRP, artikel te bepalen |
| Verblijfplaats | bedrijfsobject | Wet BRP art. 2.20, 2.39 |
| Verwerken adreswijziging | bedrijfsproces | Wet BRP art. 2.20, 2.39 |
| Verhuizing | gebeurtenis | Wet BRP art. 2.39 |
| Emigratie | gebeurtenis | Wet BRP art. 2.43 |
| Vestiging vanuit het buitenland | gebeurtenis | Wet BRP art. 2.38 |
| Inschrijven niet-ingezetene | bedrijfsproces | Wet BRP art. 2.66, 2.67 |
| RNI-loket | rol | Wet BRP art. 2.67 (inschrijfvoorziening); aanwijzing van de gemeenten artikel te bepalen |
| Behandelen verzoek om correctie | bedrijfsproces | Wet BRP art. 2.58 |
| Behandelen verzoek om geheimhouding | bedrijfsproces | Wet BRP art. 2.59 |
| Behandelen verzoek om verwijdering van gegevens | bedrijfsproces | Wet BRP art. 2.57 |
| Wijzigen naamgebruik | bedrijfsproces | Wet BRP art. 2.25 |
| Onjuiste inschrijving op adres melden | dienst | Wet BRP art. 2.20 lid 2, 2.22, 2.26; de melding door een burger zelf staat niet in de wet ([Circulaire adresonderzoek](../bronanalyses/burgerzaken/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) blijft bron voor de werkwijze) |
| Ingeschreven persoon | bedrijfsobject | Wet BRP, artikel te bepalen |
| Bijhoudingsgemeente | rol | Wet BRP, artikel te bepalen |
| Toezichthouder BRP | rol | Wet BRP, artikel te bepalen |
| Bevolkingsadministratie bijhouding | bedrijfsfunctie | Wet BRP (de functie omvat de BRP-diensten) |
| Beheerder van de begraafplaats | rol | [Wet op de lijkbezorging](../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) art. 23 lid 2, 28 (de houder van de begraafplaats) |
| Graf aanvragen | dienst | Wlb art. 23 lid 2, 28, 33 |
| Grafuitgifte | product | Wlb art. 23 lid 2 (particulier graf met uitsluitend recht), 28 (vestiging en termijn), 33 (gemeentelijke begraafplaats) |

## B. UPL-product zonder landelijke grondslag: product behouden, uitwerking vervalt

| Product of dienst | UPL | Gemeentelijke grondslag | Vervalt |
|---|---|---|---|
| [Gedenkteken plaatsingsvergunning](../bedrijfsarchitectuur/diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/gedenkteken-plaatsingsvergunning.md) | nr. 142 | [Model beheersverordening begraafplaatsen](../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md) art. 19 | proces Verlenen vergunning grafbedekking, met zijn relaties |
| [Grafonderhoud](../bedrijfsarchitectuur/diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/grafonderhoud.md) | nr. 163 (grondslag in de UPL: een begraafplaatsenbeleid) | Model beheersverordening art. 20 (onderhoud door de gemeente) | proces Onderhouden graf, met zijn relaties. Wlb art. 28 lid 4 gaat over de onderhoudsplicht van de rechthebbende, niet over de dienst van de gemeente |
| [Asverstrooiing](../bedrijfsarchitectuur/diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/asverstrooiing.md) | nr. 32 | [Model-APV](../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-vng-model-apv.md) art. 5:36 | proces Verlenen toestemming asverstrooiing. De Wlb staat verstrooien toe (art. 66a lid 2 onder b); het verbod en de toestemming voor een plek komen uit de APV. Wlb art. 66b (vergunning voor een terrein om permanent as te verstrooien, voor de houder) is een andere, landelijke taak |
| [Legalisatie handtekening](../bedrijfsarchitectuur/diensten/0-bestuur-en-ondersteuning/burgerzaken/legalisatie-handtekening.md) | nr. 226 (grondslag in de UPL: [Wet griffierechten](../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-griffierechten-burgerlijke-zaken-bwbr0028899.md) art. 23, alleen een tarief) | geen gevonden; de tarieventabel van een legesverordening geeft alleen een tarief | geen uitwerking aanwezig. De dienst blijft (UPL); [procesarchitectuur-terugmelding 21](../terugmeldingen/procesarchitectuur-terugmeldingen.md) vraagt de werkgroep de bevoegdheidsgrondslag uit te zoeken |

Bij elk vervallen proces: nagaan of de objecten, gebeurtenissen en rollen die alleen voor dat proces bestaan ook vervallen (bijvoorbeeld een toegang tot Grafbedekking of Vergunning), en of de relaties naar de bedrijfsfunctie blijven.

## C. Geen UPL en geen landelijke grondslag: vervalt

| Element | Toelichting |
|---|---|
| [Gewaarmerkte kopie reisdocument aanvragen](../bedrijfsarchitectuur/diensten/0-bestuur-en-ondersteuning/burgerzaken/gewaarmerkte-kopie-reisdocument-aanvragen.md) | Niet in de Paspoortwet, het Paspoortbesluit of de Wet op de Nederlandse identiteitskaart (gezocht op kopie, afschrift, waarmerk), niet in de UPL. Gemeenten verschillen ook in wat ze waarmerken (alleen reisdocumenten, ook het rijbewijs, ook andere documenten). Procesarchitectuur-terugmelding 11 en de representatie Gewaarmerkte kopie (geen pagina) gaan mee. |

## D. Wettelijke bron aanwezig, relatie *is grondslag voor* ontbreekt

- **Lijkbezorging**: Begraafplaatsregister, Bijzettingenregister, Crematoriumregister, Bijzondere begraafplaats toestemming, Herbegraven of alsnog cremeren, Ontleding stoffelijk overschot toestemming, Uitvaart vervroegen of uitstellen, Verlof tot begraven, Vervoersdocumenten stoffelijk overschot. De Wet of het Besluit op de lijkbezorging staat al met artikel in de kenmerken; de relatie van het beleidskader ontbreekt.
- **Burgerzaken**: [Vermissing of diefstal rijbewijs doorgeven](../bedrijfsarchitectuur/diensten/0-bestuur-en-ondersteuning/burgerzaken/vermissing-of-diefstal-rijbewijs-doorgeven.md): [Wegenverkeerswet 1994](../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) art. 123 lid 1 onder h (het rijbewijs verliest zijn geldigheid door aangifte van vermissing) en [Reglement rijbewijzen](../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) art. 39 lid 1 (proces-verbaal van vermissing bij de aanvraag van een vervangend rijbewijs); beide zijn al beleidskader.

## Bedrijfsfuncties uit GEMMA

Producten- en dienstenrealisatie veiligheidsdomein en Uitvoering openbare orde en veiligheid zijn GEMMA-functies (Functie-indeling naar domein) zonder wettelijke bron. Een functie is een indeling van gedrag, geen taak uit één wet; ze blijven, met de grondslag van de diensten en processen die zij omvat (besluit 5).

## Bevindingen

- **Brontypen heringedeeld (besluit 6).** 15 gemeentelijke verordeningen, beleidsregels en regelingen van gemeenschappelijke regelingen gingen van `wet` naar `gemeentelijke-regelgeving`; van `beleid` gingen 127 bronnen naar `richtlijn` (RvIG, NVVB, VNG, Divosa, BZK en andere landelijke uitvoerders en koepels) en 3 naar `gemeentelijke-regelgeving` (Model beheersverordening begraafplaatsen, Model subsidieregeling politieke partijen, NVVB-modelbeleidsregel briefadres). `overig` is niet heringedeeld. Daarna (besluit 8) is `wet` gesplitst: 3 bronnen naar `europese-regelgeving` (AVG, twee keer, en AI-verordening), 47 naar `rijksregelgeving`. Twijfelgeval: de memorie van toelichting bij de Archiefwet 1995 is wetsgeschiedenis, geen regelgeving, en staat nu als `rijksregelgeving`.
- **De UPL is geen wettelijke bron.** Haar grondslaglabel wijst meestal naar een wetsartikel, maar soms naar een tarief (legalisatie), een modelverordening (gedenkteken, asverstrooiing) of een beleidsstuk (grafonderhoud). Voor de BRP-diensten zijn de artikelen nagelezen: art. 2.8, 2.23, 2.25, 2.38, 2.39, 2.43, 2.55, 2.57, 2.58, 2.59, 2.66 en 3.22 Wet BRP bestaan en gaan over de dienst. De UPL-kolom Specifiek/Generiek helpt niet bij variatie: zij noemt de parkeervergunning, het grafonderhoud en de legalisatie generiek.

## Terugmeldingen

Alle open procesarchitectuur-terugmeldingen zijn op 2026-10-08 herschreven naar de opbouw van de GGM-terugmeldingen: wat de UPL of het kennismodel zegt, **Bevinding:** en **Voorstel:**. `tools/afleiden.py` houdt een open melding zonder die twee alinea's tegen. Nieuw: nr. 21, de grondslag van Legalisatie handtekening. Nr. 7, 8 en 11 noemen nu ook de landelijke grondslag of het ontbreken ervan.

## Uitwerking

- **A (2026-10-08).** Alle elementen hebben nu een relatie *is grondslag voor* van de Wet BRP of de Wet op de lijkbezorging, en hun eigen relaties de wet als bron. De open artikelen zijn bepaald: Ingeschreven persoon art. 1.1 onder e en f, 2.2, 2.7; Bijhoudingsgemeente art. 1.1 onder h, 1.4 lid 1; Toezichthouder BRP art. 4.2; Briefadresgever art. 1.1, 2.42, 2.45. RNI-loket: Wet BRP art. 2.64, 2.67 lid 3, 2.79 en Besluit BRP art. 36; de wet zegt niet welke gemeenten loket zijn, de beschrijving noemt ze (Nederland Wereldwijd) en een procesarchitectuur-terugmelding vraagt de grondslag. Onjuiste inschrijving op adres melden blijft met Wet BRP art. 2.20 lid 2, 2.22, 2.26; ze staat niet in de UPL, en een terugmelding stelt voor haar op te nemen. Beheerder van de begraafplaats vervalt: de Wlb kent alleen de houder, en de beheerder is nu synoniem van Houder van de begraafplaats. Bevolkingsadministratie bijhouding is een bedrijfsfunctie en krijgt geen eigen grondslag (besluit 5).
- **B (2026-10-08).** De Model-APV is bron (VNG, november 2023; openbare kopie bij een raadsvoorstel van Opmeer, opgenomen met de VNG als eigenaar) en beleidskader in Gemeentelijke regelgeving, thuis in Algemeen (generiek), taakveld 0, beleidsdomein Besluitvorming; zij is grondslag voor Asverstrooiing (art. 5:36 lid 3). De Model beheersverordening is grondslag voor Gedenkteken plaatsingsvergunning (art. 19) en Grafonderhoud (art. 20); haar relaties naar elementen met een grondslag in de Wet op de lijkbezorging heten nu *werkt uit voor* (besluit 13). De UPL is bron van Grafonderhoud. De processen Verlenen vergunning grafbedekking, Onderhouden graf en Verlenen toestemming asverstrooiing vervallen, met hun relaties. De drie diensten worden gerealiseerd door de functie Exploiteren van begraafplaatsen, zonder eigen proces, zoals Legalisatie handtekening door Producten- en dienstenrealisatie publieksdiensten. Wat alleen voor de processen bestond: Grafbedekking wordt onderdeel van Graf, zonder pagina, en de relatie *betreft (vergunning grafbedekking)* van Vergunning vervalt. Urn blijft: de urn is de houder van de as en geen deel van het stoffelijk overschot (Wlb art. 58, 59, 65, 66), met een besluit omdat geen proces haar levensloop bepaalt. De functies Producten- en dienstenrealisatie veiligheidsdomein en Uitvoering openbare orde en veiligheid vervallen in de wiki (besluit 12); Asverstrooiing staat nu onder Exploiteren van begraafplaatsen, met [GEMMA-terugmelding 1](../terugmeldingen/gemma-terugmeldingen.md) en een aanvulling op procesarchitectuur-terugmelding 1. Het signaal voor een proces dat een UPL-product zonder landelijke grondslag realiseert, is nu een fout (besluit 14).
- **C (2026-10-08).** Gewaarmerkte kopie reisdocument aanvragen vervalt, met de relaties vanuit Producten- en dienstenrealisatie publieksdiensten; de representatie Gewaarmerkte kopie blijft een begrip zonder pagina. Procesarchitectuur-terugmelding 11 noemt de dienst niet meer als element en zegt dat GEMMA het waarmerken niet opneemt.
- **D (2026-10-08).** De relatie *is grondslag voor* staat nu bij de negen diensten in lijkbezorging (Wlb of Besluit op de lijkbezorging) en bij Vermissing of diefstal rijbewijs doorgeven (Wegenverkeerswet 1994 art. 123 lid 1 onder h, Reglement rijbewijzen art. 39 lid 1).

## Besluiten van de redacteur (2026-10-08)

1. Voor elementen en structuur bestaat een wettelijke grondslag. Wettelijke bronnen worden genoemd en waar nodig gebruikt als onderbouwing. Gemeentelijke beleidsdocumenten dienen voor taal, voor het vinden van lacunes en dergelijke, maar niet als onderbouwing. *Stand: regel Wettelijke grondslag; voor relaties aangevuld door besluit 16.*
2. Het GEMMA-model geldt voor alle gemeenten; producten en diensten met grote variatie tussen gemeenten zijn ongewenst (voorbeeld: de parkeervergunning, die veel gemeenten kennen maar een kleine landelijke gemeente niet). Landelijke en gemeentelijke regelgeving worden expliciet onderscheiden: in ArchiMate staat elk beleidskader in een van twee groepen. *Stand: regel Wettelijke grondslag.*
3. Alleen een product of dienst uit de UPL zonder landelijke wettelijke grondslag, maar met een gemeentelijke, blijft. Zo'n product wordt niet uitgewerkt in processen, objecten en dergelijke. Processen, bedrijfsobjecten en andere elementen zonder wettelijke bron blijven niet. *Stand: regel Wettelijke grondslag.*
4. Een UPL-product vervalt nooit, ook niet zonder enige grondslag; dan volgt een terugmelding aan de werkgroep procesarchitectuur. Terugmeldingen bevatten, net als de GGM-terugmeldingen, een voorstel en zijn goed leesbaar. *Stand: regel Wettelijke grondslag; skill beoordelen §7.*
5. Een bedrijfsfunctie heeft geen eigen wettelijke bron nodig: zij volgt de grondslag van de diensten en processen die zij omvat, en vervalt alleen als zij niets meer omvat. *Stand: regel Wettelijke grondslag; aangevuld door besluit 12.*
6. De brontypen worden fijnmaziger: `wet` (landelijke en EU-regelgeving en verdragen), `informatiemodel`, `richtlijn` (landelijke uitvoeringsvoorschriften en handreikingen), `gemeentelijke-regelgeving` (verordeningen, nadere regels, beleidsregels, regelingen van gemeenschappelijke regelingen en VNG-modellen daarvan), `beleid` (intern gericht gemeentelijk beleid) en `overig`, in die volgorde van voorrang. Dezelfde indeling bepaalt de map en de groep van een beleidskader, in de wiki en in Archi; een groep zonder beleidskaders wordt niet geëxporteerd. *Stand: herzien door besluit 8 (wet gesplitst in europese- en rijksregelgeving).*
7. Europese regelgeving en rijksregelgeving zijn aparte groepen naast Gemeentelijke regelgeving, zodat projecten EU-kaders als de AVG en de AI-verordening direct herkennen; samen zijn ze de landelijke regelgeving. Een groep wordt alleen gemaakt als er een beleidskader in valt. *Stand: regel Bronvoorrang; regel Wettelijke grondslag (Regelgevingindeling).*
8. Eén naamgeving voor één indeling: het brontype is de indeling, en de groep in Archi en de map in de wiki en in Archi heten als het brontype. Daarom is `wet` gesplitst in `europese-regelgeving` en `rijksregelgeving`; samen heten ze landelijke regelgeving. Het veld regelgever (EU, rijk, VNG-model) blijft als eigenschap: wie de regeling vaststelt. *Stand: regels Bronvoorrang en Eén naamgeving.*
9. Ook een landelijke richtlijn als geheel kan een beleidskader zijn (regelgever *landelijke organisatie*, groep en map *Richtlijn*), zoals de definitie van Beleidskader in GEMMA toelaat. Zij is geen wettelijke grondslag: haar relatie heet *geeft richtlijn voor*. De bronanalyses staan per onderwerp in een map per brontype: `bronanalyses/<onderwerp>/<brontype>/`. *Stand: regel Wettelijke grondslag; skill criteria (regeling).*
10. `tools/afleiden.py` controleert de regel: een fout bij een relatie *is grondslag voor* vanuit een richtlijn, een signaal bij een element zonder landelijke wettelijke bron (UPL-producten en -diensten, bedrijfsfuncties en beleidskaders uitgezonderd) en bij een bedrijfsproces dat een UPL-product zonder landelijke grondslag realiseert. Dat laatste wordt een fout zodra groep B is afgerond, zodat het per geval laten vervallen van die processen niet wordt tegengehouden. *Stand: tools/afleiden.py en tools/signalen.py.*
11. Bij groep A en D wordt een geval zonder twijfel (de grondslag staat eenduidig in de nagelezen wettekst) niet meer apart voorgelegd: de AI voegt de bron en de relatie toe en noemt het geval in de samenvatting ter bevestiging. Een geval met twijfel wordt wel voorgelegd. *Stand: regel Wettelijke grondslag (aangevuld 2026-10-08).*

Aanvullingen bij de uitwerking van groep B (2026-10-08):

12. Bij besluit 5: een bedrijfsfunctie die alleen UPL-producten of -diensten zonder landelijke grondslag zou omvatten, bedient geen proces (besluit 3) en vervalt in de wiki; die producten hangen onder de functie van hun beleidsdomein, met een GEMMA-terugmelding. Besluit 5 blijft verder gelden. *Stand: regel Wettelijke grondslag.*
13. Een beleidskader in Gemeentelijke regelgeving is alleen grondslag (*is grondslag voor*) voor een UPL-product of -dienst zonder landelijke grondslag; waar de wet de grondslag is en het VNG-model de uitvoering regelt, heet de relatie *werkt uit voor*. `tools/signalen.py` houdt een afwijking tegen. *Stand: regel Wettelijke grondslag; references/relaties.md.*
14. Een bedrijfsproces dat een UPL-product zonder landelijke grondslag realiseert, is een fout (besluit 10, na groep B). *Stand: tools/afleiden.py; regel Wettelijke grondslag.*
15. Voorstellen aan het GEMMA-team over het GEMMA-model zelf staan in een eigen register, `beoordelingen/terugmeldingen/gemma.yaml`, met dezelfde opbouw als de GGM- en procesarchitectuur-terugmeldingen (GEMMA, Bevinding, Voorstel); de lijst staat in [GEMMA-terugmeldingen](../terugmeldingen/gemma-terugmeldingen.md). *Stand: skill beoordelen §7.*

Aanvulling bij het nalopen van de relaties (2026-10-08):

16. Bij besluit 1: relaties hebben geen eigen landelijke grondslag nodig, want dat is te gedetailleerd. Elementen en structuur worden afgeleid uit wettelijke bronnen, maar dat hoeft per relatie niet als grondslag te worden vastgelegd; een relatie heeft een bron zoals elke claim. Voor elementen blijft de regel gelden. Het nalopen van de relaties zonder landelijke bron vervalt daarmee, en er komt geen signaal voor. In lijkbezorging hadden 37 relaties geen landelijke bron, in burgerzaken 160 en in Algemeen 27. Zeven relaties in lijkbezorging, die alleen op de verordening van Groningen of op een VNG-pagina steunden, hebben de wet als bron gekregen: Wlb art. 23 lid 1 en 2 (Begraafplaats bevat Graf), art. 23 lid 2 en 28 lid 1 (Verlenen grafrecht geeft uit Graf en realiseert Graf aanvragen), art. 28 lid 6 en 7 (Beheren grafrechten omvat Verval van het grafrecht), art. 23 lid 2 (Rechthebbende op het graf machtigt tot begraving), art. 11 en 18 lid 1 (Verlof tot begraven bedient Degene die in de lijkbezorging voorziet) en Gemeentewet art. 229 lid 1 onder a en b (Verlenen grafrecht leidt tot Heffing). Bij Gedenkteken plaatsingsvergunning (art. 19 lid 2) en Asverstrooiing (Model-APV art. 5:36 lid 3) staat naast Groningen nu het VNG-model als bron. *Stand: regel Wettelijke grondslag.*

Uitwerking in de regel: een grondslag in gemeentelijke regelgeving is een VNG-modelverordening, niet de verordening van één gemeente. Zo raken verordeningen die elkaar tegenspreken het model niet: de verordening van een gemeente blijft bron voor taal, voorbeelden en lacunes, en een afwijking ervan is een afwijking in de praktijk (regel Tegenspraak).

## Vragen aan de redacteur

Geen open vragen meer; de uitwerking per geval staat in `todo.md`.
