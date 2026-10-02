<!-- gegenereerd door tools/ggm.py; hash: fd3abd91e5f49fa5926f67b09b5b88056dfedb56cf02fbea4e8188f2716f8572 -->
# 1 Veiligheid en Vergunningen

Taakveld: 1 Veiligheid en Vergunningen. Alleen objecttypen; letterlijke definities uit het GGM.

## Activiteit Omgevingswet

Ieder menselijk handelen waarbij, of ieder menselijk nalaten waardoor een verandering of effect in de (fysieke) leefomgeving wordt of kan worden bewerkstelligd.

Attributen: omschrijving.

GUID: `EAID_9547BC67_7488_4d9a_B651_2B69A62D789F`

Relaties:

- heeft → Leges_Grondslag (*Association*, 1 → 1..*, `EAID_2EBFB0E8_1F2A_45fb_A9C2_AAED1EFBA6DB`)
- Heeft → VTHzaak (*Association*, 1..* → 1..*, `EAID_7F7FE836_F4D9_4584_BD7B_F8579984F9F7`)

## AOMStatus

Attributen: datumBeginStatus, datumEindeStatus, status, statusVolgorde, statuscode.

GUID: `EAID_FDEB42B6_5D93_46bf_9B5C_10F42BA4AC26`

## Bevinding

Een *bevinding* is de uitkomst van een waarneming of onderzoek die aangeeft wat is geconstateerd bij beoordeling of inspectie.

Attributen: controleElement, controleniveau, resultaat, risico, diepte, activiteit, fase, datumAanmaak, aangemaaktDoor, datumMutatie, gemuteerdDoor.

GUID: `EAID_ED0D0224_0A30_435b_AB25_87FDA8DF4078`

Relaties:

- → Bevinding (*Association*, 1..1 → 0..*, `EAID_5077B808_045A_4c39_8368_5EF557975018`)
- heeft → Inspectie (*Association*, 0..* → 1.., `EAID_36B85F97_36E8_4031_B65F_8B9943124096`)

## BOA

Een buitengewoon opsporingsambtenaar (boa) is een ambtenaar met een specifieke opsporingsbevoegdheid.

GUID: `EAID_90B2A249_8D88_4a14_979F_672223D98E8C`

Relaties:

- verbalisant → VTH-Melding (*Association*, 1 → 0..*, `EAID_AA01203B_68F8_49c7_93A0_50AF6F0CA78B`)

## Combibon

Een Combibon is een modelformulier dat handhavende ambtenaren gebruiken om geconstateerde overtredingen en de gekozen afdoeningsmodaliteit (bijv. bekeuring of strafbeschikking) vast te leggen.

Attributen: sanctie.

GUID: `EAID_43D57BB8_C2E4_4b5a_A41C_C5CEC9D3877D`

Relaties:

- → VTH-Melding (*Generalization*,  → , `EAID_8CEB0C48_F21B_4f40_8937_DC4D44E8E1E6`)

## Fietsregistratie

Adminstreren van fietsen

Attributen: verwijderd, gelabeld.

GUID: `EAID_FF9A4A36_6674_4590_BC33_7B6DC5256490`

Relaties:

- → VTH-Melding (*Generalization*,  → , `EAID_7D24D0DE_BD63_4306_AB96_5C927A98D923`)

## Grondslag

Een *grondslag* is de juridische of normatieve basis waarop een besluit, handeling of rechtspraak steunt; het is hetgeen zijn **basis vindt in wetgeving of andere geldende rechtsregels**.

Attributen: omschrijving, code.

GUID: `EAID_94E2B19A_6942_4164_8A52_3C0BBDE45808`

Relaties:

- heeft → Leges_Grondslag (*Association*, 1..1 → 1..1, `EAID_116E1177_D516_4939_8514_6C0A46BA1885`)
- Heeft → Zaak (*Association*, 1..* → 1..*, `EAID_54E984A2_35F1_4126_BA3D_0BD84F744E25`)

## Heffinggrondslag

De maatstaf waarop een belasting is gebaseerd, het bedrag op basis waarvan een bepaalde belasting wordt geheven of de premie voor sociale zekerheid wordt vastgesteld.

Attributen: domein, hoofdstuk, paragraaf, omschrijving, bedrag.

GUID: `EAID_3D2D5426_653C_485c_A99C_8AD933E76D78`

Relaties:

- heeft → Activiteit Omgevingswet (*Association*, 1..* → 1.., `EAID_54AE48BD_8390_49e1_8C8C_3EEDFF82D0F0`)

## Heffingsverordening

Een *heffingsverordening* is een door de gemeenteraad vastgestelde verordening die de **heffing en invordering van gemeentelijke belastingen en rechten** regelt, zoals afvalstoffenheffing, precariobelasting of marktgelden.

GUID: `EAID_C29CCD49_04E2_44b4_A6B0_AD8B10552628`

Relaties:

- vermeld in → Heffinggrondslag (*Association*, 1 → 0..*, `EAID_21767452_C186_401e_B6FB_C672ACC15B19`)
- → Document (*Generalization*,  → , `EAID_542C097B_D8CF_4ee5_B454_7F99D9AE078B`)

## Indiener

Persoon die meldiing of aanvraag doet

GUID: `EAID_E9AD325A_49CF_48a6_AA9E_7FB57E03E414`

Relaties:

- → Rechtspersoon (*Generalization*,  → , `EAID_4D77D7A7_D33D_4ed9_B3A5_352278A94E0F`)

## Inspectie

het inwinnen, verwerken en interpreteren van informatie met het doel om de momentane toestand van de boezemkade vast te stellen.

Attributen: datumInspectie, inspectietype, datumGepland, status, kenmerk, omschrijving, opmerkingen, datumAanmaak, aangemaaktDoor, datumMutatie, gemuteerdDoor.

GUID: `EAID_F73901FC_A78E_486f_B6C6_74CFCBE26CAB`

Relaties:

- heeft → VTHzaak (*Association*, 1..* → 1.., `EAID_A8A40307_22D9_4cdb_AD87_E911FEDFEFC5`)

## Kosten

*Kosten* zijn de prijs of uitgaven die men moet betalen voor het gebruik, verkrijgen of verbruiken van een product, dienst of middel, doorgaans uitgedrukt in geld.

Attributen: type, omschrijving, opBasisVanGrondslag, naam, aantal, bedrag, bedragTotaal, vastgesteldBedrag, tarief, eenheid, datumAanmaak, aangemaaktDoor, geaccordeerd, gefactureerdOp, datumMutatie, gemuteerdDoor.

GUID: `EAID_0E4A8F94_ED08_43dc_9F78_C9DD17D34690`

Relaties:

- heeft → VTHzaak (*Association*, 1..* → 1.., `EAID_4BD998AC_402B_4878_A326_37E05F1EC7AB`)

## Leges_Grondslag

*Leges_Grondslag* is de basis of maatstaf waarop de heffing van leges wordt berekend, zoals de omvang van de werkzaamheden, bouwkosten of andere relevante parameters die in de legesverordening zijn vastgelegd.

Attributen: omschrijving, datumAanmaak, legesGrondslag, aantalOpgegeven, aantalVastgesteld, eenheid, automatisch, aangemaaktDoor, datumMutatie, gemuteerdDoor.

GUID: `EAID_7F9392E5_6E43_4880_AF14_819E32A86204`

Relaties:

- is van → VTHzaak (*Association*, 1..* → 1.., `EAID_D5B590DA_28E1_4b12_8C69_F16AF4B9ADD7`)

## Ligplaatsontheffing

Tijdelijke toestemming voor het innemen van een ligplaats op een locatie in een gebied met een verbod op ligplaatsen.

Attributen: stickernummer.

GUID: `EAID_872A0342_EA75_418e_9455_E51875BFD771`

## MORAanvraagOfMelding

*MORAanvraagOfMelding* is een aanvraag of melding die een burger of organisatie doet bij de gemeente om een **situatie in de openbare ruimte te melden of te laten beoordelen**, zoals schade, overlast, gevaarlijke situaties of onderhoudsproblemen.

Attributen: locatie, locatieOmschrijving, meldingOmschrijving, meldingTekst, CROW.

GUID: `EAID_80F23226_8DD8_4926_B8F1_F2A3C01A29BF`

Relaties:

- → AanvraagOfMelding (*Generalization*,  → , `EAID_1D2BDC1C_B6D7_47d0_9B5D_4E6E46B906A6`)

## OpenbareActiviteit

Activiteit in het publieke domein

Attributen: datumStart, datumEinde, evenmentnaam, locatieOmschrijving, status.

GUID: `EAID_B2B423C3_B9C9_4b4f_A47D_85D29417B9B4`

## Precario

Belasting die specifiek wordt geheven voor het plaatsen van voorwerpen onder, op of boven voor de openbare dienst bestemde gemeentegrond.

GUID: `EAID_13BB343D_A595_43c9_8208_9BC5B05B618C`

## Producttype

Een *producttype* is een categorie of variant van producten die dezelfde aard of kenmerken delen, waarmee producten binnen een groep worden ingedeeld op basis van gemeenschappelijke eigenschappen.

Attributen: omschrijving.

GUID: `EAID_03B4B3C0_3616_4ea2_A8B1_3D6754325F02`

Relaties:

- Heeft → VTHzaak (*Association*, 1 → 1, `EAID_04849139_9FA5_4487_B037_ABFDB627C473`)

## SubProducttype

*SubProducttype* is een afgeleide of meer specifieke categorie binnen een *Producttype* die producten verder onderscheidt op basis van gedetailleerde kenmerken.

Attributen: omschrijving, prioriteit.

GUID: `EAID_0DB447E3_B31B_4f07_8E35_7E77D0AAEF80`

Relaties:

- heeft → Producttype (*Association*, -1..* → 1..1, `EAID_F473FC6F_A3A3_4fb0_84E8_46E74F004E84`)
- Heeft → VTHzaak (*Association*, * → 0..*, `EAID_FA102DCE_9AB3_46cb_9715_340B3A43ACDD`)

## Vaartuig

Een zee- of binnenvaartuig, tot de vaart gebruikt of bestemd, daaronder begrepen drijvende werktuigen, zoals baggerwerktuigen, kranen, bokken, elevators, alsmede woonschepen, glijboten en ponten.

Attributen: naamVaartuig, registratienummer, kleur, lengte, breedte, hoogte.

GUID: `EAID_D12123D3_D62D_4978_B7D4_8405F00A0D6A`

## VOMAanvraagOfMelding

VOM staat voor Vergunning, Ontheffing of Melding. Het betreft hier een melding of een aanvraag voor een vergunning of een ontheffing.

Attributen: dossiernummer, intaketype, adres, locatie, kadastraleAanduiding, BAGID, activiteiten, toelichting, locatieOmschrijving, kenmerk, internNummer.

GUID: `EAID_44B26957_BAA4_41c2_ABBF_CC1AC91D30D6`

Relaties:

- → AanvraagOfMelding (*Generalization*,  → , `EAID_ADE64570_57AC_49f0_95C2_75C54F38437A`)

## Vordering

Een *vordering* is een juridisch recht dat een schuldeiser heeft om van een andere partij (schuldenaar) een prestatie te ontvangen, zoals een geldbedrag, levering van goederen of uitvoering van een dienst.

Attributen: vorderingnummer, omschrijving, totaalbedrag, bedragBTW, totaalbedragInclusief, geaccordeerd, geexporteerd, geaccordeerdOp, geaccordeerdDoor, datumAanmaak, aangemaaktDoor, datumMutatie, gemuteerdDoor.

GUID: `EAID_341942C1_0F72_4e13_ADD1_235805BB81C0`

Relaties:

- heeft → Vorderingregel (*Association*, 1.. → 1..*, `EAID_7BBFA897_6852_412c_926B_E156B7A48C23`)
- heeft → VTHzaak (*Association*, 1..* → 1.., `EAID_F9EED8C4_63F8_409b_8B6C_1CD783D7A903`)

## Vorderingregel

Een *vorderingregel* is een afzonderlijke regel of entry in een gegevensset of lijst die een specifieke *vordering* beschrijft, inclusief kenmerken zoals de omvang, datum, type en status van de vordering.

Attributen: Omschrijving, Bedrag_incl_btw, Bedrag_excl_btw, Type, Btwcategorie, Periodiek, Gemuteerd_door, Mutatiedatum, Aangemaakt_door, Aanmaakdatum.

GUID: `EAID_E2B83F97_FDFD_4876_9E66_23D79D4A4C03`

Relaties:

- betreft → Kosten (*Association*, 1.. → 0..1, `EAID_454A71AF_5181_44da_A750_0883C39F734D`)

## VTH-Melding

Melding met betrekking tot Vergunningen, Toezicht en Handhaving

Attributen: referentienummer, soortVTHMelding, locatie, straatnaam, geseponeerd, datumSeponering, datumtijdTot, organisatieonderdeel, status, taaktype, beoordeling, overtredingsgroep, resultaat, activiteit, zaaknummer, overtredingscode.

GUID: `EAID_E9AEF0A9_11BC_4d2a_BC48_FB77F04EF9A6`

Relaties:

- heeft → Foto (*Association*, 0..1 → 0..*, `EAID_564051E6_A5BA_44c2_9AC4_E2E84198168B`)
- betreft → Object (*Association*, 0..* → 0..*, `EAID_E9EAACB4_682A_43eb_8CAA_E7536337D9AE`)
- → AanvraagOfMelding (*Generalization*,  → , `EAID_86C8960F_4162_4dd8_98E7_AD6E526DF2EE`)

## VTHAanvraagOfMelding

VTH staat voor Vergunning, Toezicht en Handhaving. Het betreft hier een melding of een aanvraag voor een vergunning of een melding voor Toezicht en/of Handhaving.

Attributen: omschrijving.

GUID: `EAID_EAC249B9_13F7_472b_A971_05ED32006F04`

Relaties:

- → VOMAanvraagOfMelding (*Generalization*,  → , `EAID_7E1FC35B_0CFF_42a9_9A67_D312692BA0E7`)

## VTHzaak

Een *VTHzaak* is een zaak of dossier binnen de gemeentelijke administratie die betrekking heeft op **vergunningverlening, toezicht en handhaving (VTH)** van regels en voorschriften in de fysieke leefomgeving.

Attributen: verkamering, bevoegdGezag, uitvoerendeInstantie, behandelaar, prioritering, teamBehandelaar.

GUID: `EAID_88AF7A2E_C508_464a_AD22_DD9B156D570D`

Relaties:

- kan leiden tot → Zaak (*Generalization*,  → , `EAID_18115A7E_6613_4d50_B334_53B8AD8659F2`)

## Waarneming

Handhavende taak in het kader van VTH

GUID: `EAID_DDC990BC_C026_4c98_BEE5_6692EA0C2515`

Relaties:

- → VTH-Melding (*Generalization*,  → , `EAID_4323D9C5_F3AB_4acf_902C_45336D4DF3B1`)

## WABOAanvraagOfMelding

Aanvraag of medling in het kader van de Wet algemene bepalingen omgevingsrecht (WABO)

Attributen: bouwkosten, projectkosten, omschrijving, registratienummer, OLONummer.

GUID: `EAID_192EA281_414F_4d8d_85D1_5C1B75224942`

Relaties:

- → VOMAanvraagOfMelding (*Generalization*,  → , `EAID_0145CDE7_919F_46a8_8B31_93091CA9EA58`)

## WoonfraudeAanvraagOfMelding

Melding of aanvraag van woonfraude

Attributen: meldingTekst, meldingOmschrijving, adres, categorie, locatieOmschrijving.

GUID: `EAID_5CE9E5F3_BA9A_47e4_A4C1_DE21E66E9F8E`

Relaties:

- → AanvraagOfMelding (*Generalization*,  → , `EAID_FF5B0203_B376_4d22_9FFD_AD7B52587264`)

## WoonoverlastAanvraagOfMelding

Melding of aanvraag met betrekking tot Woonoverlast

Attributen: locatie, locatieOmschrijving, meldingOmschrijving, meldingTekst.

GUID: `EAID_CB5BCFAA_01F3_468d_A5CE_4E08D3E4FFC2`

Relaties:

- → AanvraagOfMelding (*Generalization*,  → , `EAID_ACEECD8F_8C9D_4d66_9CE7_F396DC55C3F3`)
