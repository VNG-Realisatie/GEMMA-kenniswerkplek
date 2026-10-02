<!-- gegenereerd door tools/ggm.py; hash: 962a84b71451ebb9820774d73261f65343f4ad4160c4b54c791e408df0d527de -->
# Inburgering

Taakveld: 6 Sociaal Domein. Alleen objecttypen; letterlijke definities uit het GGM.

## Aandachtspunt

Een Aandachtspunt is een bijzonder aspect of omstandigheid in de persoonlijke situatie van de inburgeraar, dat extra aandacht vereist bij de begeleiding of dienstverlening in het kader van inburgering.

Attributen: aandachtspuntOmschrijving, StartDatum, EindDatum.

GUID: `EAID_F188F63C_0033_4164_9F73_413AE6943497`

Relaties:

- → Subdoel Aandachtspunt (*Association*, 0..0 → 0..*, `EAID_7BD80251_560B_4bd4_8BAC_7FB003EB04DE`)

## Aanvraag verlenging Inburgeringstermijn

Een Aanvraag verlenging inburgeringstermijn is een verzoek van een inburgeringsplichtige aan het college van burgemeester en wethouders tot verlenging van de inburgeringstermijn op grond van persoonlijke omstandigheden als bedoeld in artikel 7.3, tweede lid, van de Wet inburgering 2021.

Attributen: BeoordelingAanvraagVerlenging, VerlengingsGrond.

GUID: `EAID_63D30089_AD78_4c29_9D17_160FE4A242E8`

Relaties:

- beoordeling Aanvraag → Inburgeringstermijn (*Association*, 1..1 → 1..*, `EAID_4D3479C4_B18A_4a5a_B528_D1A780EC7F4F`)
- → Verlengingsgrond (*Association*, 1 → 1..*, `EAID_C1877738_BECA_476e_8906_4DB092D0D0E1`)

## Asielstatushouder

De Inburgeringsplichtige die rechtmatig verblijf heeft

Attributen: Telefoonnummer verblijf AZC, Emailadres verblijf AZC, DigiD aangevraagd, Rijbewijs, Land Rijbewijs, Is gekoppeld aan.

GUID: `EAID_598F7015_C6B5_4eed_80A6_139B62324678`

Relaties:

- heeft aangevraagd → Diplomawaardering (*Association*, 1 → 0..*, `EAID_EF148167_40EF_4598_A654_94DC90DE7646`)
- heeft gevolgd → Educatie (*Association*, 1 → 0..*, `EAID_8AAE3275_1F11_4b67_BD1E_443971D3DEA3`)
- is gekoppeld aan  → Gemeente (*Association*, 0..* → 0..1, `EAID_5F26AFF9_ADDC_4234_AB26_A3E9201A2CAF`)
- is gekoppeld aan → Gemeente (*Association*, 0..* → 0..1, `EAID_CF75F931_F266_433c_BA48_5ED157516443`)
- bezit → ICT-Vaardigheid (*Association*, 1 → 0..*, `EAID_C166A1FF_871F_4a0c_A556_D64840893524`)
- heeft → Taalvaardigheid (*Association*, 1 → 1, `EAID_743C5835_5DF0_4cb8_A13F_AD396DD4794F`)
- heeft gevolgd → Training (*Association*, 1 → 0..*, `EAID_5C77DF7C_5271_4f51_9995_DAB3D5E7710A`)
- verblijft → Verblijfplaats AZC (*Association*, 0..* → 0..1, `EAID_903DDEF6_9B11_46cf_A9A9_5E1C880CDABB`)
- neemt deel → Voorbereiding op Inburgering (*Association*, 1 → 1, `EAID_2839C308_1490_41f8_9996_CFAC2B7399A3`)
- → Werk (*Association*, 1 → 0..*, `EAID_CA8768E8_ADE1_4199_B1F9_2A97D5273306`)
- → Inburgeraar (*Generalization*,  → , `EAID_E86953B8_2000_47ce_B010_617922D06209`)

## B1-route

De B1-route is één van de drie leerroutes in het inburgeringsstelsel, waarbij de inburgeringsplichtige zich voorbereidt op het afleggen van het inburgeringsexamen op taalniveau B1, gericht op brede participatie in de Nederlandse samenleving en toeleiding naar arbeid.

Attributen: ExamenDatum, Resultaat, RedenGeenResultaat, AantalGratisExamenpogingenTegoed, GevolgdeUrenParticipatieTaalles.

GUID: `EAID_09D462A9_94C8_4803_A0A0_B7DB4363B45D`

Relaties:

- onderdeel van  → Leerroute (*Association*, 0..1 → 1, `EAID_9821848F_48A0_446d_8811_5DC161D2D13A`): Kan ook een generalisatie zijn. Geldt ook voor de overige routes

## Brede Intake

De Brede Intake in het sociaal domein is een gestructureerd proces waarbij een hulpverlener samen met een inwoner diens situatie, behoeften, en problemen in kaart brengt om tot een integraal beeld te komen van wat nodig is om passende ondersteuning te bieden. Hierbij wordt niet alleen gekeken naar specifieke hulpvragen, zoals schulden of werkloosheid, maar ook naar onderliggende factoren, zoals gezondheidsproblemen, woonsituatie, en sociaal netwerk. Het doel is om vanuit een holistisch perspectief samenhangende oplossingen te vinden en de inwoner te ondersteunen bij het versterken van zelfredzaamheid en participatie.

Attributen: GevolgdeUrenKNMenTaalles, UrenGeoorloofdVerzuim, UrenOngeoorloofdVerzuim, DatumTot(Peildatum), AantalUrenAlfabetiseringsOnderwijs, startdatum, einddatum.

GUID: `EAID_8B394DCE_C3C4_4262_9460_8EF130E90D83`

Relaties:

- onderdeel van → Inburgeringstraject (*Association*, 1..1 → 1..1, `EAID_36F38F1C_2F35_4088_A9E7_35BF53C3E709`)
- heeft → Leerroute (*Association*, 0..1 → 1, `EAID_18BB4C56_7880_4b1e_9FE8_1F2DF357CE51`)

## Diplomawaardering

Een Diplomawaardering is de beoordeling van een buitenlands diploma, certificaat of graad door het Informatiecentrum Diplomawaardering (IDW), met als doel het vaststellen van het Nederlandse opleidingsniveau waarmee dit diploma vergelijkbaar is.

Attributen: NiveauCompetentie, WaarderingAangevraagd, DiplomaWaarderingVoor, DiplomaWaarderingNederlandsNiveau, DiplomaWaarderingRichting.

GUID: `EAID_950DD620_01C0_4594_875F_AE23C9154826`

## Educatie

Educatie betreft het formele en non-formele onderwijsaanbod dat gericht is op het vergroten van basisvaardigheden, zoals taalvaardigheid, rekenen en digitale vaardigheden, ter ondersteuning van participatie en zelfredzaamheid van (laagopgeleide) volwassenen, waaronder inburgeringsplichtigen.

Attributen: Opleiding, EducatieVan, EducatieTot, EducatieLand, EducatieDiploma, EducatieInBezit.

GUID: `EAID_8C5FEEDF_1AE5_44a6_8A13_53A70F06DBBC`

## Examen

Een Examen in de context van onderwijs is een formele toetsingsactiviteit waarmee de kennis, vaardigheden en competenties van een leerling of student worden beoordeeld ten opzichte van vooraf vastgestelde leerdoelen of eindtermen. Het examen kan schriftelijk, mondeling, digitaal of praktijkgericht zijn en vormt doorgaans een afsluiting van een cursus, module of opleiding. Het behalen van een examen kan leiden tot het verkrijgen van een diploma, certificaat of overgangsbewijs en is bedoeld om de voortgang en geschiktheid voor verdere studie of beroep te waarborgen.

Attributen: ExamenResultaat.

GUID: `EAID_DCE46ABA_613D_4204_86F4_35F517FF680F`

Relaties:

- Afgerond met → Inburgeringstraject (*Association*, 0..1 → 1, `EAID_61E77119_7B76_4855_9CFE_39C02A9AB2E8`)

## Examenonderdeel

Een Examenonderdeel in de context van onderwijs is een specifieke, afgebakende component van een examen waarin een deelaspect van de leerdoelen of eindtermen wordt getoetst. Het kan betrekking hebben op een specifiek vak, thema of vaardigheid en kan bestaan uit verschillende toetsvormen, zoals meerkeuzevragen, essays, praktijkopdrachten of mondelinge presentaties. Het examenonderdeel draagt bij aan de totaalscore of het eindresultaat van het examen en kan afzonderlijk beoordeeld en gewaardeerd worden.

Attributen: ExamenOnderdeelSpecificatie, Resultaat, Ontheffing, RedenVrijstelling, DatumRegistratieUitslag, BehaaldeScore.

GUID: `EAID_D41DCE2D_4AD5_45b8_9527_EC416F4A4CC7`

Relaties:

- → Examen (*Association*, 0..* → 1, `EAID_07D6B7FF_09FC_4f30_B4CF_85EE247E38B9`)

## Gezinsmigrant en Overige migrant

Object Inburgeraar is gespecialiseerd in Asielstatushouder en Gezinsmigrant en Overige Migrant. Gezinsmigrant en Overige Migrant heeft geen kenmerken en is bedoeld om relaties te leggen met objecten die alleen van toepassing zijn voor Gezinsmigrant en Overige Migrant zoals bijvoorbeeld: object Aanvraag Sociale Lening. Hetzelfde geldt ook voor object Asielstatushouder, deze heeft overigens wel kenmerken.

GUID: `EAID_526489DC_4D57_4e6d_8338_5F7C898162F6`

Relaties:

- → Inburgeraar (*Generalization*,  → , `EAID_BD79AE98_4F00_4a06_9568_5A40F7D55F63`)

## Hoofddoel

Het Hoofddoel is de door de gemeente vastgestelde eindbestemming van het inburgeringstraject, waarin wordt vastgelegd of de inburgeringsplichtige wordt begeleid richting werk, onderwijs of (maatschappelijke) participatie, op basis van de brede intake en het leerrouteadvies.

Attributen: Doel, StartDatum, EindDatum.

GUID: `EAID_CEAAEBFB_9CB8_4c5e_98F7_11791C0A21D2`

## ICT-Vaardigheid

ICT-vaardigheid betreft het vermogen van de inburgeringsplichtige om digitale middelen en toepassingen zelfstandig en doelgericht te gebruiken voor communicatie, informatieverwerking en deelname aan de samenleving.

Attributen: ICTVaardigheid, NiveauICTVaardigheid.

GUID: `EAID_1095BF0E_087F_4341_8B3C_E0DD4C9AF269`

## Inburgeraar

De gemeente gaat inburgeringsplichtige nieuwkomers begeleiden bij hun inburgering. Voor asielstatushouders doen zij dit vanaf het moment van koppeling aan een gemeente

Attributen: Gedetailleerde Doelgroep, Doelgroep.

GUID: `EAID_EE5472C2_193E_4432_B175_78D6DF1D357B`

Relaties:

- heeft → Aandachtspunt (*Association*, 1..1 → 0..*, `EAID_82DF0B8F_A0F0_4ad7_B346_87B8E4BEED4B`)
- heeft → Aanvraag verlenging Inburgeringstermijn (*Association*, 1 → 0..1, `EAID_97F5FC70_3EF7_4e2d_ABB6_6FEDD3E67843`)
- heeft → Hoofddoel (*Association*, 1..1 → 0..*, `EAID_228DEC20_E504_4c49_B1AF_0B4637DCCADB`)
- heeft een → Inburgeringsplicht (*Association*, 1 → 1, `EAID_DD96E8B4_4622_4a34_B2AC_A9C7363709EB`)
- heeft → Ontwikkelwens (*Association*, 1..1 → 0..*, `EAID_A2DD3BA5_80F4_4454_B90B_BDD529FA2949`)
- → Vreemdeling (*Generalization*,  → , `EAID_02A0FDF0_2C0C_4282_B6DE_64C7B857BEBE`)

## InburgeringsAanbod

Het Inburgeringsaanbod is het geheel van activiteiten, voorzieningen en ondersteuning dat door de gemeente wordt aangeboden aan de inburgeringsplichtige om de inburgeringsdoelen te behalen, zoals vastgelegd in het persoonlijk plan inburgering en participatie (PIP).

Attributen: DatumInburgeringsAanbod, DatumAanvangTaalschakelTraject, DatumEindeCursus, CursusInstelling, IndicatorAlfabetisering, TaalschakelTraject, DatumTaalschakelDiploma, ParticipatieDeelname, ContractId.

GUID: `EAID_D9FAEFEC_2B8E_48dc_A1E8_E134754E9943`

Relaties:

- voor → Inburgeraar (*Association*, 1..1 → 1..*, `EAID_40558423_3CC2_455c_A9DD_AC4F8CAA30D3`)

## Inburgeringsplicht

Bevat de uitkomst Leerbaarheidstoets dat een groot deel van de leerroutes bepaalt. Bevat mogelijk ook de Examenresultaten (nog toe te voegen als Ja). Dit zijn DUO berichten (Opvragen en per API beschikbaar stellen aan deze Entiteit/Attributen.

Attributen: IndicatorInburgeringsplicht, UitkomstLeerbaarheidstoets, BeschikkingVoldaanInburgeringsplicht, V-nummer, InburgeraarSpecialisatie, DatumStart, DatumEind, RedenGeenInburgeringsplicht, DatumGewijzigdInburgeringsplicht, WordtBehandelsAls, DatumGewijzigdWordtBehandeldAls.

GUID: `EAID_E2C66E88_930E_460f_93F8_8CD160DCEE15`

Relaties:

- heeft → Inburgeringstermijn (*Association*, 1..1 → 1..*, `EAID_88DB8E16_976E_45bc_A3F9_D17297A9CD71`)
- Ontheffing → Ontheffing (*Association*, 1 → 0..*, `EAID_18274FB3_5BA5_4396_B56C_64F9C715BF62`)
- Vrijstelling → Vrijstelling (*Association*, 1 → 0..*, `EAID_846CC71C_D354_47be_BF3F_0708F44D69B6`)

## Inburgeringstermijn

De Inburgeringstermijn is de wettelijke periode waarbinnen een inburgeringsplichtige moet voldoen aan de inburgeringsplicht, gerekend vanaf de startdatum van de verplichting zoals vastgesteld door DUO of de gemeente.

Attributen: DatumAanvangInburgeringstermijn, DatumEindeInburgeringstermijn, VooraankondigingBoete, BoeteBedrag, DatumBoete.

GUID: `EAID_E07490AD_C5DE_4665_8540_92B19656A027`

## Inburgeringstraject

Een Inburgeringstraject in de context van inburgering bij gemeenten is een persoonlijk begeleidingstraject dat nieuwkomers ondersteunt bij het leren van de Nederlandse taal, het begrijpen van de samenleving, en het ontwikkelen van vaardigheden om zelfstandig te participeren in de Nederlandse maatschappij. Het traject omvat doorgaans onderdelen zoals taallessen (NT2), kennis van de Nederlandse maatschappij (KNM), en participatieactiviteiten, zoals vrijwilligerswerk of een werkstage. Het inburgeringstraject wordt afgestemd op de behoeften, achtergrond en mogelijkheden van de nieuwkomer en heeft als doel hen te begeleiden naar maatschappelijke zelfredzaamheid en een actieve rol in de samenleving.

Attributen: UItkomstLeerbaarheidstoets.

GUID: `EAID_F9B2A863_63C8_4229_906A_D0891BB4F021`

Relaties:

- Heeft → Inburgeringsplicht (*Association*, 1..1 → 1..1, `EAID_E4F555EE_2BD4_4eb0_B42D_366D4B560400`)

## Introductiemodule

De Introductiemodule is een verplicht onderdeel van het inburgeringstraject waarin de inburgeringsplichtige basisinformatie ontvangt over de Nederlandse samenleving, de inburgeringsplicht en het lokale voorzieningenaanbod, direct na de brede intake.

Attributen: ModuleNaam, DeelnameIntroductieModule.

GUID: `EAID_7328FC95_FA03_405d_8EC4_5C4B3D5CF042`

## Leerroute

Een Leerroute is het door de gemeente vastgestelde traject dat een inburgeringsplichtige volgt om te voldoen aan de inburgeringsplicht, bestaande uit taallessen, participatieactiviteiten en aanvullende modules, afgestemd op het leervermogen en het hoofddoel van de inburgeraar.

Attributen: LeerrouteType, Niveau, GeschatteIntensiteitB1Route, IndicatorAlfabetisering, IndicatorToestemmingExamenA2, IndicatorMagOpleidingAfmaken, geenLeerbaarheidstoetsZB, ExamenA2.

GUID: `EAID_51285531_9529_4b2d_9EC6_B6BAEA729D9A`

Relaties:

- afgesproken in → PIP (*Association*, 0..1 → 1, `EAID_8E0A85FD_9A97_40f3_A4FA_96B74FE20774`)

## MAP

De Module Arbeidsmarkt en Participatie (MAP) is een verplicht onderdeel van het inburgeringstraject waarin de inburgeringsplichtige wordt voorbereid op deelname aan de Nederlandse arbeidsmarkt, door middel van voorlichting, oriëntatie en arbeidsmarktgerichte activiteiten.

Attributen: Resultaat, DatumEindgesprekMAP, RedenNietSuccesvolVoltooid, IndicatorVerwijtbaar.

GUID: `EAID_2177E7F0_0F76_41b7_B5CA_5FE182355E94`

Relaties:

- Onderdeel van → Leerroute (*Association*, 0..1 → 1, `EAID_9DE13CC8_C495_4f21_8538_B6967FEEE075`)

## Ontheffing

Een Ontheffing is een formeel besluit van de gemeente of van DUO waarbij een inburgeringsplichtige geheel of gedeeltelijk wordt vrijgesteld van onderdelen van de inburgeringsplicht, op grond van persoonlijke omstandigheden zoals medische beperkingen, psychische problematiek of aantoonbare inspanning.

Attributen: BeslissingOntheffing, DatumOntheffing.

GUID: `EAID_3F5932BD_C721_402d_8154_74A1CE097825`

Relaties:

- ontheffing voor → Examenonderdeel (*Association*, 1 → 0..*, `EAID_5423D12F_B004_4fa9_ABC0_0ABADB27A103`)

## Ontwikkelwens

Een Ontwikkelwens is een door de inburgeringsplichtige geuite persoonlijke ambitie of leerdoel die richting kan geven aan het inburgeringstraject, en wordt meegenomen bij het opstellen van het Persoonlijk Plan Inburgering en Participatie (PIP).

Attributen: ontwikkelwensOmschrijving, StartDatum, EindDatum.

GUID: `EAID_AE33D54A_A105_4fac_B378_D5651B66F0F0`

Relaties:

- → Subdoel Ontwikkelwens (*Association*, 0..0 → 0..*, `EAID_CD062567_4976_488f_A5F3_17E3EDD1B018`)

## PIP

Het Persoonlijk Plan Inburgering en Participatie (PIP) is een individueel plan dat door de gemeente wordt vastgesteld in overleg met de inburgeringsplichtige, waarin het leerrouteadvies, het inburgeringsaanbod, het hoofddoel en de begeleidingsafspraken zijn vastgelegd, met als doel het succesvol afronden van de inburgering binnen de gestelde termijn.

Attributen: DagtekeningInitielePIP, DagtekeningPIP, NaamContactPersoon, EmailContactPersoon, IndicatorMagOpleidingAfmaken.

GUID: `EAID_94EB7844_F863_4330_A15A_06ED4D1401E0`

Relaties:

- bevat → InburgeringsAanbod (*Association*, 1 → 1, `EAID_39B99BE0_69B3_47a0_B6FC_991C56118F85`)

## PVT

Het Participatieverklaringstraject (PVT) is een verplicht onderdeel van het inburgeringstraject waarin de inburgeringsplichtige kennismaakt met de basiswaarden van de Nederlandse samenleving, en deze onderschrijft door het ondertekenen van de participatieverklaring.

Attributen: Resultaat, DatumOndertekening PVT, RedenNietVoldaan, VerwijtbaarNietVoldaan.

GUID: `EAID_783B026E_E993_467c_85E0_E90E9E01BAA0`

Relaties:

- Onderdeel van → Leerroute (*Association*, 0..1 → 1, `EAID_04F5981A_6C61_4431_A2CA_82DCFA1FDD9B`)

## Subdoel Aandachtspunt

Een Subdoel aandachtspunt is een concreet, afgebakend leer- of begeleidingsdoel dat voortvloeit uit een gesignaleerd aandachtspunt in de persoonlijke situatie van de inburgeringsplichtige, en dat bijdraagt aan het wegnemen van belemmeringen voor het volgen van de leerroute of het behalen van het PIP-doel.

Attributen: Subdoel, Startdatum, Einddatum.

GUID: `EAID_0279048D_E742_400c_9D86_03085E5EF917`

## Subdoel Ontwikkelwens

Een Subdoel ontwikkelwens is een concreet, haalbaar leer- of ontwikkeldoel dat is afgeleid van een door de inburgeringsplichtige geuite ontwikkelwens, en dat richting geeft aan de invulling van het inburgeringstraject binnen het PIP.

Attributen: Subdoel, StartDatum, EindDatum.

GUID: `EAID_564CEF80_C5BE_4d74_8BC7_B48BEFDEE655`

## Taalvaardigheid

Taalvaardigheid is het niveau van beheersing van de Nederlandse taal door de inburgeringsplichtige, gemeten op onderdelen zoals luisteren, spreken, lezen en schrijven, overeenkomstig het Europees Referentiekader voor Talen (ERK).

Attributen: ToetsTaalleerbaarheid, Score, ResultaatToetsTaalleerbaarheid, ToetsSpreekvaardigheid, ResultaatToetsSpreekvaardigheid, OpleidingsniveauGeschat, TaallesActiviteit, StartVanTaallesActviteit, EindeVanTaallesActviteit, ResultaatTaalles, PresentieTaalles, TaalvaardigheidOverall, TaalvaardigheidMondeling, TaalvaardigheidSchriftelijk.

GUID: `EAID_0C74C068_BA3A_4394_AA76_16B47FEFC88C`

## Training

Een Training is een gestructureerde leeractiviteit binnen het inburgeringstraject, gericht op het aanleren of versterken van specifieke vaardigheden of kennis ter ondersteuning van taalverwerving, participatie of persoonlijke ontwikkeling.

Attributen: TrainingGevolgd, PeriodeTraining, ResultaatTraining.

GUID: `EAID_88DF555F_9F2F_4274_A1ED_B201EEE0E62E`

## Verblijfplaats AZC

Verblijfplaats AZC is de formele verblijfslocatie van een asielgerechtigde of inburgeringsplichtige binnen een Asielzoekerscentrum (AZC), beheerd door het Centraal Orgaan opvang Asielzoekers (COA), voorafgaand aan of tijdens het inburgeringstraject.

Attributen: Plaats, Straatnummer, Huisnummer.

GUID: `EAID_40C9655E_15CF_4b46_8B59_FD8D4CBC57B5`

## Verlengingsgrond

Een Verlengingsgrond is een wettelijk erkende reden op basis waarvan de gemeente de inburgeringstermijn van een inburgeringsplichtige kan verlengen, zoals vastgelegd in artikel 7.3, tweede lid, van de Wet inburgering 2021.

Attributen: AanwezigheidAanvraagVerlening, VerlengingInWeken, Verlengingsgrondslag, DatumAanvangVerlengingsgrond, DatumEindeVerlengingsgrond, DatumBeoordelingVerlengingsgrond.

GUID: `EAID_951AC549_985D_4bdb_BEE0_65AD3C1ED9E2`

## Voorbereiding op Inburgering

Voorbereiding op inburgering omvat de activiteiten die worden aangeboden aan asielstatushouders vóór de start van de formele inburgeringsplicht, gericht op oriëntatie op de Nederlandse samenleving, taal en het inburgeringsstelsel.

Attributen: InstemmingDeelnameVoorinburgering, DatumInstemming, Reden.

GUID: `EAID_6AEA0314_895B_46be_B525_96F4657E7F0D`

Relaties:

- bestaat uit → Introductiemodule (*Association*, 1 → 1..*, `EAID_7FCA5582_9B35_4ded_A509_EF499639C01A`)

## Vreemdeling

Een Vreemdeling is een Natuurlijk Persoon die de Nederlandse Nationaliteit niet bezit en niet op grond van een wettelijke bepaling als Nederlander wordt behandeld.

Attributen: v-nummer, Sociaal Referent.

GUID: `EAID_3BBDD95F_6586_4591_BBD0_D04D1CF2801E`

Relaties:

- → NatuurlijkPersoon (*Generalization*,  → , `EAID_A2F928D0_04AB_483b_AFA1_045AE421EF32`)

## Vrijstelling

Een Vrijstelling is een formeel besluit waarbij een inburgeringsplichtige geheel of gedeeltelijk wordt ontheven van specifieke onderdelen van de inburgeringsplicht, omdat deze reeds op andere wijze zijn behaald of niet van toepassing zijn, zoals bedoeld in artikel 7.2 van de Wet inburgering 2021.

Attributen: EindoordeelVrijstelling, DatumVrijstelling.

GUID: `EAID_C31D4A7E_1F25_4b85_B49C_AEC45EB3DB54`

Relaties:

- vrijstelling voor → Examenonderdeel (*Association*, 1 → 1, `EAID_4A22D6DF_64B2_464e_9C4D_FED046CC57E0`)

## Werk

Werk betreft het verrichten van betaalde arbeid door een inburgeringsplichtige, als onderdeel van of resultaat uit het inburgeringstraject, en wordt meegenomen in de beoordeling van participatie, uitstroom en leerroutegeschiktheid.

Attributen: CVGemaakt, VrijeTekstBesteding, Ambitie, ContactUAF, Beroep, BeroepVan, BeroepTot, SoortAanstelling, Taak, TaakVan, TaakTot.

GUID: `EAID_45BB12F8_C796_43aa_A4D0_FDC724601EB9`

## Z-route

De *Z-route* (Zelfredzaamheidsroute) is een van de drie leerroutes onder de Nederlandse Wet inburgering 2021 en is bedoeld voor inburgeringsplichtigen met een lage leerbaarheid die moeite hebben met het leren van de Nederlandse taal, gericht op zelfredzaamheid, participatie en taalontwikkeling zonder centrale examenvereisten.

Attributen: Resultaat, ExamenDatum, Onderdeel, Niveau, RedenGeenResultaat, AantalGratisExamenpogingenTegoed, GevolgdeUrenParticipatieActiviteiten.

GUID: `EAID_42CA98D5_0E2F_4110_AED0_6B8ADB955BBF`

Relaties:

- heeft (onderdeel van) → Leerroute (*Association*, 0..1 → 1..1, `EAID_D8950A51_815D_4ddc_A7ED_F99377454BC1`)
