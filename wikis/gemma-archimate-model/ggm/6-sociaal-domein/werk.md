<!-- gegenereerd door tools/ggm.py; hash: e1d3fdaa801c8b8260e874649176c5580d8edd6dcb73e7e7415e34e2fd009402 -->
# Werk

Taakveld: 6 Sociaal Domein. Alleen objecttypen; letterlijke definities uit het GGM.

## Arbeidsmarktkwalificaties

Een verzameling formele en informele kwalificaties, vaardigheden en eigenschappen die relevant zijn voor de inzetbaarheid van een persoon op de arbeidsmarkt.

Attributen: KlantTypering, Code taalbeheersing mondeling, Code taalbeheersing schriftelijk, Code werk en denkniveau, ToelichtingArbeidsmarktKwalificaties.

GUID: `EAID_E771BA5B_93D4_48a0_A6FC_BEBDD18C8975`

## Arbeidsperiode

Een aaneengesloten periode waarin een persoon arbeid heeft verricht, met begin- en einddatum.

Attributen: Datum aanvang arbeidsperiode, Datum einde arbeidsperiode, Gemiddeld aantal uur per week, Functienaam, Functieomschrijving, Contact persoon, Contact email, Contact telefoon.

GUID: `EAID_E2F30023_4E8C_44fc_8989_1E467EA8618F`

## Arbeidsverhouding

Een relatie waarin sprake is van afspraken tussen een werknemer en een werkgever over het verrichten van arbeid.

Attributen: Datum aanvraag arbeidsverhouding, Datum einde arbeidsverhouding.

GUID: `EAID_BDC8C949_2563_45eb_9E85_866ED51B3AC4`

Relaties:

- → Arbeidsperiode (*Association*, 1..1 → 1..*, `EAID_2B88DC4F_001E_4131_A4B3_98295635D774`)
- → Werkzoekende (*Association*, 0..* → 1..1, `EAID_C1086760_9918_4728_B643_18136C1DDF99`)

## Arbeidsvermogen

Een inschatting van wat iemand op basis van fysieke, mentale en sociale capaciteiten aan arbeid kan verrichten.

Attributen: CodeArbeidsvermogen.

GUID: `EAID_F657BA3E_8B66_4b84_8036_0FA4CCC2D3CE`

## Bemiddelingsactiviteit

Een activiteit in het kader van arbeidstoeleiding waarbij de gemeente of uitvoeringsinstantie gericht handelt om de persoon in contact te brengen met een werkgever of werkplek.

Attributen: DatumBemiddeling, OmschrijvingSoortContactbemiddeling, OmschrijvingSatutsBemiddeling, OmschrijvingResultaatBemiddeling, DatumVerwijzingVacature, IndicatiePlaatsing.

GUID: `EAID_7F16F190_CC44_4550_A677_7BFEC6D34E64`

## Bemiddelingsberoep

Het beoogde beroep waarvoor een persoon wordt begeleid of bemiddeld in een traject.

Attributen: ToelichtingBeroep.

GUID: `EAID_E2147AA5_89F8_4a59_A8F2_558AA872037F`

Relaties:

- → Werkzoekende (*Association*, 0..* → 1..1, `EAID_E3A8C6B1_5785_4483_B1E0_4EFDF1147E26`)

## Bemiddelingstraject

Een traject waarin een persoon begeleid wordt naar passend werk, bijvoorbeeld door een gemeente of uitvoeringsinstantie.

Attributen: DatumBemiddeling, OmschrijvingContactbemiddeling, OmschrijvingStatusbemiddeling, OmschrijvingResultaatbemiddeling, DatumVacature, IndicatiePlaatsing.

GUID: `EAID_1C180C62_5B5E_45b4_BB94_F44454D11BDE`

## BeschikbaarVoorArbeid

Een indicatie of iemand op dit moment inzetbaar is voor arbeid, los van begeleiding of ondersteuning.

Attributen: StartdatumBeschikbaarheid, DagBeschikbaarheid, AantalUrenpwBeschikbaar, Interval opzegtermijn, WaardeOpzegtermijn, StartdagBeschikbaarheid, EinddatumBeschikbaarheid, EindtijdDagBeschikbaarheid, ToelichtingBeschikbaarheid, Indicatie nog werkzaam.

GUID: `EAID_A0F5CBE4_67D2_47bb_9CE9_B104E7093D12`

## BeschikbaarVoorBemiddeling

Een indicatie dat een persoon beschikbaar is voor bemiddeling richting arbeid, waarbij wordt gekeken naar inzetbaarheid, bereidheid en eventuele beperkingen.

Attributen: IndicatieDirectBemiddelbaar, DatumEinde.

GUID: `EAID_1F4F46AC_825C_46c7_A417_BFA6775FF3D9`

## Doelgroep

Een specifieke groep personen met gedeelde kenmerken (zoals afstand tot de arbeidsmarkt) die in aanmerking komt voor bepaalde voorzieningen of aangepaste begeleiding.

Attributen: naam, omschrijving.

GUID: `EAID_FF5A6019_C72C_4bcc_ADDF_84811CBDA79B`

## Doelgroepenregister

Een landelijk register waarin mensen met een afstand tot de arbeidsmarkt worden opgenomen, vaak ten behoeve van loonkostensubsidie of andere voorzieningen.

Attributen: IndicatieDoelgroepenRegister, AdviesUWV, Baanafspraak.

GUID: `EAID_B1CD002A_85A3_41db_A905_D9A7512A7307`

## DoelReintegratievoorziening

Het beoogde effect van een ingezette voorziening, bijvoorbeeld toeleiding naar werk, dagbesteding of maatschappelijke participatie.

Attributen: CodeDoelReintegratievoorziening.

GUID: `EAID_2F1FD6B9_AF03_4864_B40C_027155621707`

## Flexibliteit

De mate waarin een persoon flexibel inzetbaar is qua werktijden, werkplek of werkzaamheden.

Attributen: IngeschrevenbijUitzendbureau, IndicatieBereidBuitenBeroepswens, IndicatieBereidheidZoekenOnderNiveau, IndicatieBereidheidZwaarWerk, IndicatieBereidheidOnregelmatigWerk.

GUID: `EAID_E7BC941E_A54D_49e1_8F77_1D8D7CE8EBD7`

## Loonkostensubsidie

Een tegemoetkoming aan een werkgever voor het in dienst nemen van een werknemer met verminderde loonwaarde.

Attributen: PercentageLoonwaardeWML.

GUID: `EAID_F600A89B_EE8E_4b86_949E_F15E9328EB83`

## Mobiliteit

De bereikbaarheid van werkplekken voor een persoon, afhankelijk van vervoermiddel, rijbewijs en fysieke mogelijkheden.

Attributen: IndicatieBereidheidVerhuizen, MaximaleReistijd, ToelichtingMaximaleReistijd, CodeVervoermiddel, ToelichtingVervoermiddel.

GUID: `EAID_8C8FAE2D_5F4D_4e3b_8EA3_43FF544775F2`

## Ontheffing

Een formele vrijstelling van verplichtingen rond arbeidsparticipatie, zoals beschikbaarheid of tegenprestatie, op basis van persoonlijke of juridische gronden.

Attributen: RedenAanvraag, AanvraagdatumOntheffing, Ontheffingsbesluit, MotivatieOntheffingsbesluit, SoortOntheffing, IngangsdatumOntheffing, EinddatumOntheffing, ResultaatInstrumentbeoordeling, OntheffenVerplichtingen, VersieNummerAanvraag, BijlagenBijAanvraag, BijlagenBijOntheffingsbesluit, HerzieningsdatumOntheffing, MotivatieHerzieningsbesluit, BijlagenBijHerzieningsbesluit.

GUID: `EAID_8EE515EA_11F9_4f56_B9AA_F7B0904B39E7`

## Opleiding

Een formeel of informeel leertraject dat een persoon heeft gevolgd met als doel het verwerven van kennis, vaardigheden of competenties.

Attributen: Opleidingstype, Instituutnaam, DatumAanvang, DatumEinde, CodeStatusOpleiding, IndicatieDiploma, DatumDiploma, CodeNiveauOpleiding, Opleidingsrichting, CodeLeerwegMBO, AantalJarenOpleiding, CodeTijdsBeslagOpleiding, IndicatieDeeltijdopleiding, ToelichtingBeeindigenOpleiding, Indicatiebuitenlandseopleiding, ToelichtingOpleiding.

GUID: `EAID_E250F980_18C3_4666_8022_302ACDC18A56`

Relaties:

- → Opleidingsnaam (*Association*, 1..1 → 1..1, `EAID_961F974A_4FF8_41ce_A573_0ECF65593CED`)

## Opleidingsnaam

De naam waarmee een gevolgde opleiding aangeduid wordt. Dit kan een officiële (gecodeerde) of vrije tekst zijn.

Attributen: naamOpleiding.

GUID: `EAID_DD9C65D4_0B47_4623_9BE4_6CE711DB846E`

## OpleidingsnaamGecodeerd

Een OpleidingsnaamGecodeerd is een versleutelde/coderende aanduiding van de naam van een opleiding zoals vastgelegd in onderwijs-microdata, bedoeld om de opleiding te identificeren zonder de volledige tekstuele naam direct in de dataset op te nemen.

Attributen: CodeOpleidingsnaam, OmschrijvingOpleidingsnaam, CodeSoortOpleidingsnaam, IndicatieOpleidingsnaamActief.

GUID: `EAID_E194EC08_CD47_4429_9598_FDA0AF9E3C2A`

Relaties:

- heeft synoniem → OpleidingsnaamGecodeerd (*Association*, 0..* → 1..1, `EAID_0FE32C76_69E2_4d61_BB8B_92F4DC906BC2`)
- gen → Opleidingsnaam (*Generalization*,  → , `EAID_35F919C6_41A9_4378_BB5F_DE485D97B71D`)

## OpleidingsnaamOngecodeerd

*OpleidingsnaamOngecodeerd* is de tekstuele naam van een opleiding zoals geregistreerd in CBS-onderwijsdata, weergegeven zonder codering om de opleidingsidentificatie leesbaar te maken.

Attributen: naamOpleidingOngecodeerd.

GUID: `EAID_5CA681BF_8AC1_4161_921F_F5F78C9DB65F`

Relaties:

- gen → Opleidingsnaam (*Generalization*,  → , `EAID_F495EEAD_2FEC_4212_9E5E_318C4060C744`)

## Opleidingsniveau

Het abstractieniveau waarop de opleiding is ingeschaald, vaak gebaseerd op landelijke of Europese onderwijsclassificaties.

Attributen: CodeOpleidingsniveauClient.

GUID: `EAID_FBDF2AE8_AC88_4288_9B40_5B26C450FC20`

Relaties:

- → Opleiding (*Association*, 1..1 → 0..*, `EAID_8A0284D9_1A7B_4c83_A1CF_6A8160046C5E`)

## Reintegratievoorziening

Een voorziening of dienst die wordt ingezet om de kansen van een persoon op arbeidsparticipatie te vergroten.

Attributen: RegistratienummerReintegratievoorziening, DatumStartVoorlopigeToekenning, DatumStart, DatumVerwachtEinde, DatumEinde, DatumIngebruikname, DatumInname, DatumEindeVerlengdeBeslistermijn, CodeType, Omschrijving, OmschrijvingType, ToelichtingOmschrijving.

GUID: `EAID_6B1C7773_77F8_47a5_8C4E_E7E129148ADB`

Relaties:

- → Loonkostensubsidie (*Association*, 0..1 → 0..1, `EAID_BA1DAE52_6E3B_4141_9B1C_C8F2356E4FB0`)

## Rijbewijs /Certificaat

Een door een bevoegde instantie afgegeven document dat aangeeft dat een persoon bevoegd is tot het besturen van bepaalde typen voertuigen.

Attributen: CodeSoortRijbewijs, NummerCertificaat, NaamCertificaat, GeldigVanaf, GeldigTot, VerstrekkendePartij, Beschrijving, IndicatieGeldigheidRijbewijs.

GUID: `EAID_40C7DD8D_7F0A_4019_860A_EB59841D1DAF`

## Taalbeheersing

Het Europese of Nederlandse taalniveau (zoals A1 t/m C2) waarop de taalvaardigheid van een persoon is ingeschaald.

Attributen: Taalcode, Taalnaam, Moedertaal, Leesvaardigheid, Schrijfvaardigheid, Spreekvaardigheid.

GUID: `EAID_AFB7351F_6761_4db2_ACC4_537A1B7C0CAA`

## TaalbeheersingNederlands

De mate waarin een persoon de Nederlandse taal beheerst, inclusief mondelinge en schriftelijke vaardigheden.

Attributen: OntheffingTaaleis, SpreeksvaardigheidNederlands, LuistervaardigheidNederlands, LeesvaardigheidNederlands, SchrijfvaardigheidNederlands, GespreksvaardigheidNederlands.

GUID: `EAID_14E98618_2093_4442_9593_1B15890260A8`

## Vaardigheidsvaststelling

Het proces waarin specifieke vaardigheden van een persoon worden beoordeeld of gemeten, vaak ter ondersteuning van een werkprofiel of plaatsingsbeslissing.

Attributen: datumLaatsteVaststelling, Indicatie mate van vaardigheid.

GUID: `EAID_A1912CA8_11EA_4d8a_A5FB_C5F98F521367`

## Voorkeur

Voorkeur is een door de klant geuite wens of voorkeur met betrekking tot werk, opleiding of ondersteuning, waarmee bij de invulling van het re-integratie- of participatietraject rekening kan worden gehouden voor zover dit past binnen de wettelijke kaders en mogelijkheden van de gemeente.

Attributen: BrancheCode, BrancheNaam, SoortBaan, SoortWerk, GegevensWerklocatie, Vervoermiddel, ToelichtingVervoersmiddel, BezitPersoonlijkeOVkaart, NummerOVK, VerloopdatumOVK.

GUID: `EAID_A514BC85_0096_4bbc_B393_DE1784056420`

## VrijstellingArbeidsplicht

Geeft aan of en waarom iemand tijdelijk of structureel is vrijgesteld van de plicht om arbeid te verrichten.

Attributen: IndicatieVrijstelling, CodeVrijstelling, DatumStart, DatumEinde, CodeRedenVrijheidstelling.

GUID: `EAID_5E0C3ED7_DCB9_4fc0_A11C_50F079D74EFD`

## Werkervaring

Eerdere functies of werkzaamheden van een persoon, inclusief sector, duur en aard van de werkzaamheden.

Attributen: Aantal jaren werkzaam in beroep, Toelichting beroep.

GUID: `EAID_48CCBBD0_2327_4620_881C_A39F151BABD6`

## Werkzaamheden als mantelzorger

Activiteiten die een persoon uitvoert in de rol van mantelzorger, buiten een formele arbeidsverhouding, maar met mogelijke invloed op beschikbaarheid voor arbeid.

Attributen: Mantelzorgverkalring verstrekt, Mantelzorgovereenkomst afgesloten, Hulp bij medicatie, Toezicht houden, Verzorgde actviteiten, Vervoer en begeleiding, Andere mantelzorgtaken, Te bespreken mantelzorgtaken, Omschrijving andere mantelzorgtaken.

GUID: `EAID_D985F79E_8616_4144_9071_238FB9240B85`

Relaties:

- → Werkzaamheden anders dan in arbeidsverhouding (*Generalization*,  → , `EAID_86D90F6C_C99A_4252_A06A_DA7740A9DD7E`)

## Werkzaamheden anders dan in arbeidsverhouding

Taken of activiteiten die een persoon verricht zonder dat sprake is van een formele arbeidsovereenkomst, zoals vrijwilligerswerk of mantelzorg.

Attributen: Code maatschappelijke context, Omschrijving werkzaamheden, Datum aanvang werkzaamheden, Datum einde werkzaamheden, Omschrijving reden einde werkzaamheden, aantalUrenGemiddeldWeek, Functienaam, PersoonOrganisatieWaarbij, Bedrag netto inkomsten uit Wadia.

GUID: `EAID_F0C047DA_725B_486b_9FF3_EB60662C1895`

## Werkzoekende

Een generiek werkprofiel van een persoon waarin diens arbeidspositie, bemiddelbaarheid en begeleidingsbehoefte worden vastgelegd, als basis voor begeleiding naar arbeid.

Attributen: DatumAanvangWerkzoekende, DatumEindeWerkzoekende.

GUID: `EAID_24A45AF2_13FF_491d_9E3D_F8D8113F28E1`

Relaties:

- → Arbeidsmarktkwalificaties (*Association*, 1..1 → 1..*, `EAID_AB605CB3_7A9A_4339_8BC6_0FE3057D0A83`)
- → Arbeidsvermogen (*Association*, 1..1 → 1..*, `EAID_DC56CC6E_4531_482d_8657_F32CF341CF3F`)
- → Bemiddelingstraject (*Association*, 1..1 → 0..*, `EAID_C3E34D34_9F52_426f_83AF_C392B07ABFE8`)
- → BeschikbaarVoorArbeid (*Association*, 1..1 → 0..1, `EAID_0E78C397_09BC_42e1_8E57_C3B95AFAA7FC`)
- → BeschikbaarVoorBemiddeling (*Association*, 1..1 → 0..*, `EAID_3A088C24_90A1_4a98_BB67_6DEC41BC8D7B`)
- → Doelgroepenregister (*Association*, 1..1 → 1..*, `EAID_F6952DDC_3D60_4847_930A_E84AB1FABBAA`)
- → DoelReintegratievoorziening (*Association*, 1..1 → 0..1, `EAID_2F385F1E_FAF1_45e4_9632_080E119C8894`)
- → Flexibliteit (*Association*, 1..1 → 0..1, `EAID_2D3D13CF_83DE_4d64_8792_11D476954F4D`)
- → Mobiliteit (*Association*, 1..1 → 0..1, `EAID_C7927091_EE48_4c92_9C92_E904145DCB9D`)
- → Ontheffing (*Association*, 1..1 → 0..1, `EAID_215D9398_9BE9_40b4_88E6_6183BF173600`)
- → Opleidingsniveau (*Association*, 1..1 → 0..1, `EAID_3DDE0EC5_209F_4ffe_A4B5_78A036D86D89`)
- → Reintegratievoorziening (*Association*, 1..1 → 0..*, `EAID_1820B8A7_B5FA_4df2_9310_9A332743E529`)
- → Rijbewijs /Certificaat (*Association*, 1..1 → 0..*, `EAID_F0232FF3_B0A6_4fe2_B1E1_94240BBA4EDE`)
- → Taalbeheersing (*Association*, 1..1 → 1..*, `EAID_8CDF19AE_21FB_4071_873D_C99D3F0B1CEA`)
- → TaalbeheersingNederlands (*Association*, 1..1 → 1..1, `EAID_F3F8C187_FB01_42d0_AAC0_8D92E7D3B6B9`)
- → Voorkeur (*Association*, 1..1 → 0..*, `EAID_E90A8EA3_8DFD_422f_A41E_6454BEBA891C`)
- → VrijstellingArbeidsplicht (*Association*, `1..`1 → 0..1, `EAID_FF67E901_9A5A_42d6_A057_D9C4CCF28661`)
- → Werkervaring (*Association*, 1..1 → 0..*, `EAID_233E4DAA_5F42_4e31_9618_0C8DE4DDA387`)
- → Werkzaamheden anders dan in arbeidsverhouding (*Association*, 1..1 → 0..*, `EAID_B8F143EF_FACE_4bdc_8C94_967CCC0831E3`)
- → ZelfredzaamheidScore (*Association*, `1..`1 → 1..*, `EAID_FE9C4793_57C5_48fe_964E_358BFA3B3EF2`)
- → Client (*Generalization*,  → , `EAID_4458A527_EEE8_48eb_B246_AF004030273D`)

## ZelfredzaamheidScore

Een gekwantificeerde weergave van het niveau van zelfstandigheid van een persoon op meerdere levensgebieden, vaak volgens de methodiek van de ZRM (Zelfredzaamheidsmatrix).

Attributen: Domein van Zelfredzaamheid, ZRM score, DatumBeoordeling, KenmerkBeoordelaar, IndicatieHulpAanwezig, Woongemeente.

GUID: `EAID_609AECDB_CFEA_4316_9541_5239A26CC069`
