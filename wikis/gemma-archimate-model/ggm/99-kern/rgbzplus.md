<!-- gegenereerd door tools/ggm.py; hash: 9242d4da7c35f21046a0856076aafd2e24b8ec7d6c44c20793abf7e505d69728 -->
# RGBZPlus

Taakveld: 99 Kern. Alleen objecttypen; letterlijke definities uit het GGM.

## AfwijkendBuitenlandsCorrespondentieadresRol

De gegevens van het adres in het buitenland waarop BETROKKENE in zijn/haar ROL in de ZAAK in de regel schriftelijk bereikbaar is indien dat afwijkt van het reguliere buitenlandse correspondentieadres van BETROKKENE

Attributen: adresBuitenland1, adresBuitenland2, adresBuitenland3, landPostadres.

GUID: `EAID_6F75D9F8_50B8_4d89_9798_26B7FD9A6DA2`

## AfwijkendCorrespondentiePostadresRol

De gegevens die tezamen een postbusadres of antwoordnummeradres vormen waarvan BETROKKENE, geen ORGANISATORISCHE EENHEID en MEDEWERKER ziinde, heeft aangegeven schriftelijk bereikbaar te zijn in verband met zijn/haar ROL in de ZAAK en dat afwijkt van de reguliere correspondentiegegevens van BETROKKENE.

Attributen: postcodePostadres, postadresType, postbusOfAntwoordnummer.

GUID: `EAID_8F133649_AE11_491c_998B_6288B7FC8FE4`

## AnderZaakobjectZaak

Aanduiding van het object (of de objecten) waarop de ZAAK betrekking heeft indien dat object (of die objecten) niet aangeduid kan worden met de relatie "heeft betrekking op ZAAKOBJECT".

Attributen: anderZaakobjectRegistratie, anderZaakobjectOmschrijving, anderZaakobjectAanduiding, anderZaakobjectLocatie.

GUID: `EAID_ABF8E616_8600_49e8_BD38_52F7C9FB70CA`

## Bedrijfsproces

Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een product of product of dienst.

Attributen: Omschrijving, Datum_start, Datum_eind, Afgerond, Naam.

GUID: `EAID_EDB5D3CD_CE4D_4317_81C6_C01CC7325148`

Relaties:

- is van → Bedrijfsprocestype (*Association*, 1..* → 1.., `EAID_E2A9D50C_A97B_4a16_B459_6AF2C5E70523`)
- uitgevoerd binnen → Zaak (*Association*, 1..* → 1..*, `EAID_096328B5_7E92_42a3_B30A_572EA01B47A4`)

## Bedrijfsprocestype

soort Bedrijfsproces met bepaalde kenmerken

Attributen: Omschrijving.

GUID: `EAID_14E4AF23_21E9_412a_B78D_C208EE9F419D`

Relaties:

- is onderdeel van → Bedrijfsprocestype (*Association*, 0..* → 0..*, `EAID_F7C59B99_448C_42c0_ACEC_9D497D3E0D5B`)
- heeft → Producttype (*Association*, 1 → 1..*, `EAID_3D1EFD60_73B1_4a17_81AE_DDD33A2EB868`)
- heeft → Zaaktype (*Association*, 1 → 1..*, `EAID_9807C834_5480_4fa2_A27B_C379E2437C85`)

## Besluit

Een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval.

Attributen: besluitidentificatie, datumBesluit, besluittoelichting, datumStart, datumVerval, redenVerval, datumPublicatie, datumVerzending, datumUiterlijkeReactie, omschrijving.

GUID: `EAID_AFB100D2_8C68_4488_8949_13E945D15920`

Relaties:

- is van → Besluittype (*Association*, 0..* → 1, `EAID_90835500_2830_4eb0_812A_4088C8C3F672`): Aanduiding van de aard van het BESLUIT.
- kan vastgelegd zijn als → Document (*Association*, 0..* → 0..*, `EAID_12F1389D_562F_4850_BA96_74239D26E835`): Aanduiding van het (de) DOCUMENT(en) waarin het BESLUIT beschreven is.
- is vastgelegd in → Document (*Association*, 0..1 → 0..1, `EAID_1832A896_B756_4337_9A4B_3A2C5C3E2624`)
- is uitkomst van → Zaak (*Association*, 0..* → 1, `EAID_520BC9F9_923B_4ed1_B58C_4940D065F52E`): Aanduiding van de ZAAK waarbinnen het BESLUIT genomen is.

## Besluittype

Generieke aanduiding van de aard van een besluit

Attributen: besluittypeOmschrijving, besluittypeOmschrijvingGeneriek, besluitcategorie, reactietermijn, indicatiePublicatie, publicatietekst, publicatietermijn, datumBeginGeldigheidBesluittype, datumEindeGeldigheidBesluittype.

GUID: `EAID_922D3938_A0EA_42bf_9EFC_23A6A236AF9B`

## Betaling

het onderhandigen of overboeken van geld in ruil voor goed of dienst

Attributen: bedrag, datumtijd, valuta, omschrijving.

GUID: `EAID_FC488929_8721_402f_A073_1DFDB76A816E`

Relaties:

- komt voor op → Bankafschriftregel (*Association*, 0..* → 0..1, `EAID_C80A3916_7A36_4443_B0C8_A936E6C9DAED`)

## Betrokkene

Een SUBJECT, zijnde een NATUURLIJK PERSOON, NIET-NATUURLIJK PERSOON of VESTIGING, ORGANISATORISCHE EENHEID (binnen een vestiging van de zaak-behandelende niet-natuurlijk persoon), of MEDEWERKER (van die organisatorische eenheid) die een rol kan spelen bij een ZAAK.

Attributen: naam, identificatie, adresBinnenland, adresBuitenland, rol, rol.

GUID: `EAID_16FB8171_A9ED_4027_A663_C035509501C8`

Relaties:

- doet → Klantbeoordeling (*Association*, 1 → 0..*, `EAID_8B6E4D35_622B_47e1_B648_7960E48898CC`)
- is → Medewerker (*Association*, 0..1 → 1, `EAID_F096C1D1_2139_414d_AF41_CDC5AB0453EE`): Een MEDEWERKER als specialisatie van BETROKKENE.
- is → NatuurlijkPersoon (*Association*, 0..1 → 1, `EAID_19608E86_9614_4a15_A3CE_8FC5D0508750`): Een NATUURLIJK PERSOON als specialisatie van BETROKKENE.
- is → NietNatuurlijkPersoon (*Association*, 0..1 → 1, `EAID_90A5DA8A_9CBA_444a_93C8_9665C5DF1A99`): Een VESTIGING is een specialisatie van BETROKKENE.
- is → OrganisatorischeEenheid (*Association*, 0..1 → 1, `EAID_6B62BEFD_0485_4a41_9C55_A1480F0DF153`): Een ORGANISATORISCHE EENHEID als specialisatie van BETROKKENE
- oefent uit → Zaak (*Association*, 1..* → 1..*, `EAID_066348C0_B9D0_49ba_A200_75D0213B2FB4`): De ROLlen die BETROKKENE heeft in de zaken waarin BETROKKENE een ROL speelt.
- → Rechtspersoon (*Generalization*,  → , `EAID_FFF5C3F6_C827_46ea_9711_B46836F57745`)

## Brondocumenten

Indicatie of bij een opname, mutatie of verwijdering van de relatie het brondocument aangeduid wordt op basis waarvan de verandering van de relatie heeft plaatsgevonden en zo ja, de specificatie van de metagegevens waarmee het brondcument aangeduid wordt, zijnde één of meer van de volgende metagegevens: Documentidentificatie, Documentdatum, Documentcode, Documentomschrijving, Document- soort, Documenthouder.

Attributen: documentGemeente, akteGemeente, documentOmschrijving, datumDocument, documentIdentificatie.

GUID: `EAID_C8CE34A2_362A_4c99_A934_C66A2E6A0793`

## ContactpersoonRol

De gegevens van de persoon die anderen desgevraagd in contact brengt met medewerkers van de BETROKKENE, een NIET-NATUURLIJK PERSOON of VESTIGING zijnde, of met BETROKKENE zelf, een NATUURLIJK PERSOON zijnde, vanuit het belang van BETROKKENE in haar ROL bij een ZAAK,.

Attributen: Contactpersoonnaam, contactpersoonFunctie, contactpersoonTelefoonnummer, contactpersoonEmailadres.

GUID: `EAID_22A29BB4_15B8_43bb_ACF5_2EAF09ABFFFB`

## Deelproces

Een geordende reeks van processtappen die binnen één organisatorische eenheid binnen een organisatie wordt uitgevoerd met als doel een specifieke bijdrage (prestatie) te leveren aan een dienst die uiteindelijke zal worden geleverd aan een burger, een bedrijf of een andere organisatie. Voorheen 'werkproces' genoemd.

Attributen: Datum_gepland, Datum_afgehandeld.

GUID: `EAID_1B65D674_DC17_40e8_B663_85DA82FD7E94`

Relaties:

- is deel van → Bedrijfsproces (*Association*, 1.. → 1, `EAID_E3A29593_7D11_45b6_8760_C93326BC40D1`)
- is van → Deelprocestype (*Association*, 1 → 1, `EAID_5943359E_DF81_47ae_A92E_10B7337A0102`)

## Deelprocestype

soort Deelproces met bepaalde kenmerken

Attributen: Omschrijving.

GUID: `EAID_710A1D2B_3C7B_41cf_A947_727186C40A98`

Relaties:

- is deel van → Bedrijfsprocestype (*Association*, 1 → 1, `EAID_6632E190_6345_4e95_BD10_E4F8D912E404`)

## Document

Geheel van gegevens met een eigen identiteit ongeacht zijn vorm, met de bijbehorende metadata ontvangen of opgemaakt door een natuurlijke en/of rechtspersoon bij de uitvoering van taken, zijnde een ENKELVOUDIG DOCUMENT of een SAMENGESTELD DOCUMENT.

Attributen: documentIdentificatie, datumCreatieDocument, datumOntvangstdocument, documentTitel, cocumentBeschrijving, datumVerzendingDocument, vertrouwelijkAanduiding, documentAuteur.

GUID: `EAID_5641C50A_C0FA_4e71_B07B_26C7B1CE94ED`

Relaties:

- is van → Documenttype (*Association*, 0..* → 1, `EAID_CFC59C3B_CE93_4428_B10D_BE49A6FCD782`): Aanduiding van de aard van het DOCUMENT.
- heeft kenmerk → Identificatiekenmerk (*Association*, 0..* → 1..1, `EAID_9A5D63E3_15C9_4ebe_9333_27D3BECE7E0D`)

## Documenttype

Aanduiding van de aard van een DOCUMENT zoals gehanteerd door de zaakbehandelende organisatie

Attributen: documenttypeOmschrijving, documenttypeOmschrijvingGeneriek, documentCategorie, documenttypeTrefwoord, datumBeginGeldigheidDocumenttype, datumEindeGeldigheidDocumenttype.

GUID: `EAID_77C7D6B6_44DE_44c0_A662_8E1A0A226EA8`

## EnkelvoudigDocument

Een DOCUMENT waarvan aard, omvang en/of vorm aanleiding geven het als één geheel te behandelen en te beheren.

Attributen: documentFormaat, documentTaal, documentVersie, documentStatus, documentInhoud, documentLink, bestandsnaam.

GUID: `EAID_547FD48D_F885_4816_BCFA_4048995C8D83`

Relaties:

- is specialisatie van → Document (*Generalization*,  → , `EAID_125BDD18_1CDE_4dcc_B15F_97BCAE63CAEA`)

## FormeleHistorie

Indicatie of de formele historie van de attribuutsoort te bevragen is. Formele historie geeft aan wanneer in de administratie een verandering is verwerkt van de attribuutwaarde (wanneer was de verandering bekend en is deze verwerkt)

Attributen: tijdstipRegistratieGegevens.

GUID: `EAID_BB4E5922_F0E8_40bb_8BB6_9B0DC648DD85`

## Heffing

Een door de overheid opgelegde verplichting tot betaling

Attributen: bedrag, code, inrekening, gefactureerd, runnummer, datumIndiening, nummer.

GUID: `EAID_B3371695_97AD_49d2_9AF1_15591B422007`

Relaties:

- heeft grondslag → Heffinggrondslag (*Association*, 0..* → 1, `EAID_4D45461F_C60E_41dc_8E1B_A4A741A90FC3`)
- soort → Heffingsoort (*Association*, 0..* → 1, `EAID_266F9975_CC9F_4d21_BDDF_20EC737CF568`)
- betreft → Vorderingregel (*Association*, 0..1 → 1.., `EAID_DE71ABE2_98B3_4ed8_9C03_D54816E84F9A`)

## Identificatiekenmerk

Nodig voor archivering om verschillende typen identificatie te kunnen onderscheiden:

Attributen: kenmerk.

GUID: `EAID_D73AFAEC_3BF1_4309_93FE_5354EF26DA51`

## InOnderzoek

De indicatie of te bevragen is dat er twijfel is of is geweest aan de juistheid van de attribuutwaarde en dat een onderzoek wordt of is uitgevoerd naar de juistheid van de attribuutwaarde.

Attributen: aanduidingGegevensInOnderzoek.

GUID: `EAID_E4DA500D_AB53_4e8a_B1A5_411F354F4AD2`

## KenmerkenZaak

Identificatie-gegevens over de zaak in andere administraties

Attributen: kenmerkBron, kenmerk.

GUID: `EAID_9E261D63_5143_4aa8_A1DA_554AB3D27025`

## Klantcontact

Klantcontacten zijn contactmomenten die werkelijk hebben plaatsgevonden, terwijl Balieafspraken afspraken zijn voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden. Hetzelfde geldt voor de telefoontjes, de klantcontacten komen uit levelOneData, dat zijn alle telefoontjes die werkelijk met een medewerker (of een gedelegeerde) hebben plaatsgevonden (soms zelfs meerdere binnen 1 telefoontje).

Attributen: eindtijd, starttijd, tijdsduur, wachttijdTotaal, kanaal, toelichting, notitie.

GUID: `EAID_A3DAD553_0E55_4256_824B_CDB5E12CB545`

Relaties:

- kan leiden tot → AanvraagOfMelding (*Association*, 0..1 → 0..*, `EAID_34EC7FEA_4CA2_4ef7_8B64_2CA8A801BE8B`)
- heeft klantcontacten → Betrokkene (*Association*, 0..* → 0..1, `EAID_4F9D5F50_DE94_480e_BE89_958A1FFF824B`)
- is gevoerd door → Medewerker (*Association*, 0..* → 0..1, `EAID_7DE2D62B_838D_4d12_A5B1_4C6DB9A475E3`)
- betreft → ProductOfDienst (*Association*, 0..* → 0..*, `EAID_4721A97B_B196_4494_B145_8AB2BCA38305`)
- is van soort → Soorten Klantcontact (*Association*, 1 → 0..*, `EAID_3F138B95_B799_496c_8B92_7BAD804EBAAC`)
- locatie → VestigingVanZaakbehandelendeOrganisatie (*Association*, 0..* → 0..1, `EAID_EA77B4A5_CA76_44c6_9EC8_F01ABEEF768B`)
- heeft betrekking op → Zaak (*Association*, 0..* → 0..1, `EAID_3DEF8FFF_14B3_4877_8B09_89A1FB3FF2E9`)

## MaterieleHistorie

Indicatie of de materiële historie van de attribuutsoort te bevragen is. Materiële historie geeft aan wanneer een verandering is opgetreden in de werkelijkheid die heeft geleid tot veranderjng van de attribuutwaarde.

Attributen: datumEindeGeldigheidGegevens, datumBeginGeldigheidGegevens.

GUID: `EAID_3D63DBCE_3FD5_4988_81D5_93A2D01A9D99`

## Medewerker

Een medewerker van de organisatie die zaken behandelt uit hoofde van zijn of haar functie binnen een ORGANISATORISCHE EENHEID.

Attributen: medewerkerIdentificatie, achternaam, datumUitDienst, emailadres, functie, geslachtsaanduiding, medewerkerToelichting, roepnaam, telefoonnummer, voorletters, voorvoegselAchternaam, extern, datumInDienst.

GUID: `EAID_16EB3936_03CB_4854_9CD8_9F0911EEA51B`

Relaties:

- vraagt aan → Aanvraag Inkooporder (*Association*, 1 → 0..*, `EAID_7CD3D99F_7481_4f29_A83F_B4BBCA24C6C0`)
- geleverd via → Leverancier (*Association*, 0..* → 0..1, `EAID_2D7DFEB4_3B70_4079_A901_DC9F424EF009`)
- is contactpersoon voor → OrganisatorischeEenheid (*Association*, 0..1 → 0..1, `EAID_7FBB7F66_64B4_40dd_9628_02202FF00FB1`): De MEDEWERKER die anderen desgevraagd in contact brengt met (andere) medewerkers van deze ORGANISATORISCHE EENHEID.
- hoort bij → OrganisatorischeEenheid (*Association*, 0..* → 0..*, `EAID_CF008EC2_F42E_4e6b_8000_E9A81F3A2ECA`): De ORGANISATORISCHE EENHEID waarvan de MEDEWERKER deel uitmaakt of deel heeft uitgemaakt.
- is verantwoordelijk voor → OrganisatorischeEenheid (*Association*, 0..1 → 0..1, `EAID_F5450BE9_CD9C_4fc5_A2E6_A569D5CE87AE`): De ORGANISATORISCHE EENHEID waarvoor de MEDEWERKER uit hoofde van zijn of haar functie zorgt (of zorgde) dat deze goed functioneert en daar rekenschap van geeft.
- verleent → Proces-verbaal-MOOR-melding (*Association*, 1 → 0..*, `EAID_9B0E9554_A8CB_482f_9F02_89D4F65902BF`)
- voert uit → Schouwronde (*Association*, 1..1 → 0..*, `EAID_4C32F102_6FF6_4f9a_A48F_9336CD363A79`)
- dient in → StartformulierAanbesteden (*Association*, 1 → 0..*, `EAID_4FE9452E_CB92_4bce_AC0F_D2555EEE49EA`)
- ingevoerd door → Stremming (*Association*, 1..1 → 0..*, `EAID_BB0E15C3_7C28_4167_A47C_C8EC2B734D21`)
- gewijzigd door → Stremming (*Association*, 0..1 → 0..*, `EAID_CD55CE9B_6C1C_4e74_BD88_3187ADD85856`)
- aanvrager → Subsidie (*Association*, 0..1 → 0..*, `EAID_AF1FA711_126D_491b_A50B_0A3FD50E6EC0`)
- werkt bij → Uitvoerende instantie (*Association*, 0..* → 1, `EAID_DBA162E4_7D2A_4e48_A76A_C23731E1E35E`)
- is verantwoordelijke voor → Zaaktype (*Association*, 0..1 → 0..*, `EAID_DE49408A_E6E8_44c9_B127_6365ABD57598`): De MEDEWERKER die verantwoordelijk is voor ZAAKen van het ZAAKTYPE.

## Object

Het OBJECT waarop een ZAAK betrekking kan hebben zijnde één of meer voorkomens van de in het RSGB en het RGBZ onderscheiden objecttypen.

Attributen: identificatie, objecttype, naam, adresBinnenland, adresBuitenland, kadastraleAanduiding, geometrie, toelichting, domein, indicatieRisico.

GUID: `EAID_91F9D39E_0322_42c6_AE7F_5027B36F3EC3`

Relaties:

- is → Besluit (*Association*, 0..1 → 1.., `EAID_DACA45FB_FC4C_4e34_AC69_09811CE65CDF`): Een BESLUIT als specialisatie van OBJECT.
- is → Buurt (*Association*, 0..1 → 0..*, `EAID_4104376C_1AD6_4103_A360_B0C6C7B11452`)
- is → Buurt (*Association*, 0..1 → 0..*, `EAID_E5B87DF0_8E09_4275_A6F3_BCE04E6877B4`)
- is → Huishouden (*Association*, 0..1 → 1, `EAID_2CA9E920_CD4C_432e_9A5E_44F84F706FAE`): Een HUISHOUDEN als specialisatie van OBJECT.
- Is → Ingezetene (*Association*, 0..1 → 1, `EAID_93320AED_D823_4ac6_BD19_2C55AFE2D453`): Een INGEZETENE is een specialisatie van OBJECT.
- is → Inrichtingselement (*Association*, 0..1 → 0..*, `EAID_139BE972_6A22_49c6_898D_188BA2505570`)
- is → KadastraalPerceel (*Association*, 0..1 → 0..*, `EAID_9142C2DC_9D2F_41b8_AD21_7C22ADF570E1`)
- is → KadastraleOnroerendeZaak (*Association*, 0..1 → 0..*, `EAID_A0CCD38F_E4E7_4044_A32A_DF84CA8A7DA6`)
- is → Kunstwerkdeel (*Association*, 0..1 → 0..*, `EAID_B905E456_B624_4d2d_B5F3_413FC8BF08D6`)
- is → Ligplaats (*Association*, 0..1 → 0..*, `EAID_37EA10C7_3C72_4026_8302_6BBD81BE0200`)
- is → Ligplaats (*Association*, 0..1 → 0..*, `EAID_ACC89638_0162_4bf4_856A_F48A6CDBFA48`)
- is → MaatschappelijkeActiviteit (*Association*, 0..1 → 0..*, `EAID_012E0E79_E6CE_4524_8869_650547508733`)
- is → NatuurlijkPersoon (*Association*, 0..1 → 0..*, `EAID_E9AA24B1_EE12_49cc_8CA9_7930E154DD9D`)
- is → NietNatuurlijkPersoon (*Association*, 0..1 → 0..*, `EAID_0830350C_FF0C_43d0_8A9A_842171749C87`)
- is → OpenbareRuimte (*Association*, 0..1 → 0..*, `EAID_BC791907_D562_40fe_9F9E_81FEF5482049`)
- is → OpenbareRuimte (*Association*, 0..1 → 0..*, `EAID_C8CB03FB_9768_4e98_9EFE_8A07021867E7`)
- is → Pand (*Association*, 0..1 → 0..*, `EAID_425C5C44_916C_47bd_ACE2_73CB085EC80D`)
- is → Pand (*Association*, 0..1 → 0..*, `EAID_E471E71D_D793_403d_BDE8_69BF54783133`)
- is → Standplaats (*Association*, 0..1 → 0..*, `EAID_90E45AEB_98D7_490a_B3F7_AD23213A3565`)
- is → Standplaats (*Association*, 0..1 → 0..*, `EAID_98745F83_6621_4255_BA46_4A280FE34F0D`)
- is → Vaartuig (*Association*, 0..1 → 0..1, `EAID_92A22D30_408A_441f_81CD_1C5F1024FA59`)
- is → Voertuig (*Association*, 0..1 → 0..1, `EAID_B5707E27_09A9_44de_933A_FAF7D8613113`)
- is → Waterdeel (*Association*, 0..1 → 0..*, `EAID_4F678BE2_85AA_4354_A4AF_24D9D5F779C3`)
- betreft → Zaak (*Association*, 0..1 → 1, `EAID_3891E5AC_DA6D_445c_BC0A_D70AE3450F0E`): De ZAAKen die betrekking hebben op het OBJECT

## Offerte

Aanbod, aanbieding of voorstel van goederen of diensten waarin opgave is gedaan van de prijs.

GUID: `EAID_B259BE5F_AC3A_4e0f_A149_D1F165277CC2`

## OpschortingZaak

Gegevens omtrent het tijdelijk opschorten van de behandeling van de ZAAK

Attributen: indicatieOpschorting, redenOpschorting.

GUID: `EAID_8EF0E043_5575_42fe_B2E7_81D8F12ADC77`

## OrganisatorischeEenheid

Het deel van een functioneel afgebakend onderdeel binnen de organisatie dat haar activiteiten uitvoert binnen een VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE en die verantwoordelijk is voor de behandeling van zaken.

Attributen: organisatieIdentificatie, datumOntstaan, datumOpheffing, emailadres, faxnummer, naam, naamVerkort, omschrijving, telefoonnummer, toelichting, Formatie.

GUID: `EAID_936A4E8B_3E5A_44b6_8A5D_EFB39F83FB6D`

Relaties:

- heeft → Klantbeoordeling (*Association*, 1..* → 0..*, `EAID_0684D5EF_2ED0_4667_91FB_BA90F35EE98E`)
- heeft → Kostenplaats (*Association*, 0..1 → 1, `EAID_2B472ADB_4268_4c90_85C2_436E804F561A`)
- Is deel van → OrganisatorischeEenheid (*Association*, 1 → 0..1, `EAID_D2770201_1CC5_47bd_90F4_EC39317F189B`)
- is gehuisvest in → VestigingVanZaakbehandelendeOrganisatie (*Association*, 1..* → 1, `EAID_689523F1_DB08_428a_B016_53B63C975012`): De VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE waar de ORGANISATORISCHE EENHEID haar activiteiten uitvoert.
- is verantwoordelijke voor → Zaaktype (*Association*, 0..1 → 0..*, `EAID_B26014D0_A1AF_4738_9D86_FF18128429F5`): De ORGANISATORISCHE EENHEID die verantwoordelijk is voor ZAAKen van het ZAAKTYPE.

## SamengesteldDocument

Een DOCUMENT waarbinnen twee of meer ENKELVOUDIGe DOCUMENTen onderscheiden worden die vanwege gezamenlijke vervaardiging en/of ontvangst en/of vanwege aard en/of omvang als één geheel beschouwd moeten worden dan wel behandeld worden.,

GUID: `EAID_47DA1FC8_F181_41bc_B16A_CE80D2CA13B1`

Relaties:

- omvat → EnkelvoudigDocument (*Association*, 0..1 → 2..*, `EAID_98544267_83F6_43ed_A9B5_5775C5462D91`): De ENKELVOUDIGe DOCUMENTen die deel uit maken van het SAMENGESTELD DOCUMENT.
- is specialisatie van → Document (*Generalization*,  → , `EAID_FA6AA954_4369_49a3_938D_A26469440859`)

## Status

Een aanduiding van de stand van zaken van een zaak op basis van betekenisvol behaald resultaat voor de initiator van de zaak.

Attributen: datumStatusGezet, statustoelichting, indicatieIaatstGezetteStatus.

GUID: `EAID_7C975D37_670B_405e_B825_924BCAFA74C7`

Relaties:

- is van → Statustype (*Association*, 0..* → 1, `EAID_B632C4ED_D11A_49a2_9AE8_70F6799F2EB1`): Aanduiding van de aard van de STATUS.

## Statustype

Generieke aanduiding van de aard van een STATUS

Attributen: statustypeOmschrijving, statustypeVolgnummer, doorlooptijdStatus, statustypeOmschrijvingGeneriek, datumBeginGeldigheidStatustype, datumEindeGeldigheidStatustype.

GUID: `EAID_AA496B7B_913C_40fd_943E_52F1A6E89440`

## StrijdigheidOfNietigheid

De aanduiding of te bevragen is dat de attribuutwaarde strijdig met de openbare orde dan wel nietig is.

Attributen: aanduidingStrijdigheidNietigheid.

GUID: `EAID_85741CBC_594C_43f9_A2B5_C50166F1A461`

## VerlengingZaak

Gegevens omtrent het verlengen van de doorlooptijd van de behandeling van de ZAAK

Attributen: redenVerlenging, duurVerlenging.

GUID: `EAID_7014565C_F8AF_459a_A2FD_30E8D7F9F0CC`

## VestigingVanZaakbehandelendeOrganisatie

Een VESTIGING van een onderneming of rechtspersoon zijnde de zaakbehandelende organisatie.

GUID: `EAID_D8142B98_64CB_408e_9941_92423543F08A`

## Zaak

Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden.

Attributen: zaakidentificatie, datumEinde, datumEindeGepland, omschrijving, omschrijvingResultaat, toelichtingResultaat, datumStart, toelichting, datumEindeUiterlijkeAfdoening, zaakniveau, indicatieDeelzaken, datumRegistratie, datumPublicatie, archiefnominatie, datumVernietigingDossier, indicatieBetaling, datumLaatsteBetaling, indicatieOpschorting, duurVerlenging, redenOpschorting, redenVerlenging, vertrouwelijkheid, leges, document, document.

GUID: `EAID_649EFD86_ED52_4293_8577_DBE5445845BF`

Relaties:

- heeft betaling → Betaling (*Association*, 0..1 → 0..*, `EAID_4792EF86_3EA9_4e05_A5CC_0EA419541F79`)
- kent → Document (*Association*, 0..* → 1..*, `EAID_B89D9C03_1963_4320_9F82_3ED1E30C2895`)
- heeft → Heffing (*Association*, 1 → 0..1, `EAID_EE334186_2640_4708_BB09_B028A5434439`)
- heeft kenmerken → KenmerkenZaak (*Association*, 1..1 → 0..*, `EAID_F19D0464_AAC3_42d0_96FA_4B7027AD4905`)
- heeft → Klantbeoordeling (*Association*, 1 → 0..1, `EAID_38EA370E_4A5A_42fc_9CFC_4D0E53E8A0CC`)
- afhandelend medewerker → Medewerker (*Association*, 0..* → 0..*, `EAID_5118E6F9_F965_4953_8F8D_5F9F1D0A2121`)
- heeft product → Producttype (*Association*, 1 → 1, `EAID_56AD30A7_9970_419a_875D_F3EFAC07B608`)
- betreft → Project (*Association*, 0..* → 0..1, `EAID_8E2A02C8_9992_4342_B3C1_3B34ABAA88D5`)
- heeft → Status (*Association*, 1 → 0..*, `EAID_FA90DE4F_C686_4701_A3A0_5A67856C004D`): De STATUSsen die bereikt zijn gedurende de behandeling van de ZAAK.
- is deelzaak van → Zaak (*Association*, 1 → 0..1, `EAID_0B81CD99_DB7F_40a0_BD64_26FCBC96420A`): De verwijzing naar de ZAAK, waarom verzocht is door de initiator daarvan, die door de zaakbehandelende organisatie is opgedeeld in twee of meer separaat te behandelen zaken waarvan de onderhavige zaak er één is.
- heeft betrekking op andere → Zaak (*Association*, 1 → 0..*, `EAID_87D7E92A_583F_4b4a_AA34_019ABCFBD939`): De andere ZAAKen die het onderwerp zijn van de ZAAK.
- is van → Zaaktype (*Association*, 0..* → 1, `EAID_213C1581_1B5D_467e_B825_25738FF800C9`): Aanduiding van de aard van de ZAAK.

## ZAAK - Origineel

Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden.

Attributen: zaakidentificatie, datumEinde, datumEindeGepland, omschrijving, kenmerk, omschrijvingResultaat, toelichtingResultaat, datumStart, toelichting, datumEindeUiterlijkeAfdoening, zaakniveau, indicatieDeelzaken, datumRegistratie, datumPublicatie, archiefnominatie, datumVernietigingDossier, indicatieBetaling, datumLaatsteBetaling, opschorting, verlenging, anderZaakobject.

GUID: `EAID_766265DF_56DD_4560_A55C_FF82E3B9751A`

Relaties:

- heeft betrekking op andere → ZAAK - Origineel (*Association*,  → 0..*, `EAID_5535E8EB_1CF8_4c21_BD0E_B3786D318FB2`): De andere ZAAKen die het onderwerp zijn van de ZAAK.
- is deelzaak van → ZAAK - Origineel (*Association*,  → 0..1, `EAID_F95B6C11_B53E_4135_A96C_77C2F49379A9`): De verwijzing naar de ZAAK, waarom verzocht is door de initiator daarvan, die door de zaakbehandelende organisatie is opgedeeld in twee of meer separaat te behandelen zaken waarvan de onderhavige zaak er één is.

## Zaaktype

Generieke aanduiding van de aard van een zaak

Attributen: zaaktypeOmschrijving, zaaktypeOmschrijvingGeneriek, trefwoord, doorlooptijdBehandeling, servicenormBehandeling, archiefcode, vertrouwelijkAanduiding, indicatiePublicatie, zaakcategorie, publicatietekst, datumBeginGeldigheidZaaktype, datumEindeGeldigheidZaaktype.

GUID: `EAID_7210A379_17EE_4143_A106_ECD9414B2A0D`

Relaties:

- heeft → Heffinggrondslag (*Association*, 1 → 0..*, `EAID_39319771_8062_415c_B199_3696EE6A91A5`)
- heeft → Producttype (*Association*, 1..1 → 1..1, `EAID_86265665_697C_4a7e_B3D4_EA2DCDD7E379`)
- heeft → Statustype (*Association*, 1 → 1..*, `EAID_EF19B3B9_08AC_4c8c_B785_4571F6FA8DDF`): De STATUSTYPEn die bereikt kunnen worden bij behandeling van ZAAKen van het ZAAKTYPE.
