---
id: 2025-vng-upl-producten-en-diensten-extern
type: bronduiding
model: upl
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
relevant: ja
korte_titel: UPL-lijst extern
bijgewerkt: '2026-10-11'
---

# Standaard producten en dienstenlijst extern basis UPL

Bron: [tekst](../../../../../../sources/modellen/2025-vng-upl-producten-en-diensten-extern.md) · [origineel (xlsx)](../../../../../../sources/modellen/2025-vng-upl-producten-en-diensten-extern.xlsx) · [omzetting (json)](../../../../../../sources/modellen/2025-vng-upl-producten-en-diensten-extern.json) · [online](https://www.gemmaonline.nl/images/gemma/f/f9/Standaard_producten_en_dienstenlijst_extern_basis_UPL.zip)

## Samenvatting

De externe producten- en dienstenlijst van de GEMMA-procesarchitectuur is de UPL voor gemeenten, aangevuld door de expertgroep procesarchitectuur van GEMMA (werkblad Bron, regel 7: de lijst is afgeleid van de UPL-query voor gemeenten van Logius). De echte bron is de [UPL van Logius](2026-logius-upl-actueel.md). Deze lijst is de uitzondering op de regel dat inhoud van GEMMA Online geen bron is: ze staat op GEMMA Online, maar is een bron voor de inhoud, met brontype `informatiemodel` (besluit redacteur 2026-10-04).

Wat de aanvulling van GEMMA toevoegt aan de UPL, per product (kolomkop, regel 13): het Iv3-taakveld, het GEMMA-domein (zoals Publieksdiensten, Fysieke leefomgeving, Sociaal domein, Openbare orde en Veiligheid), de soort product, of het specifiek is (van toepassing voor een gemeente) of generiek (voor alle gemeenten vanuit wetgeving), of er een digitaal kanaal is en het bewijs volgens de WMBEV, en tot zes grondslagen met link. Definities of beschrijvingen staan er niet in.

Voor de wiki geeft de lijst bij een dienst uit de UPL het taakveld en het GEMMA-domein: de twee ouders in de Beleidsdomeinindeling en de Functie-indeling. Wijkt de wiki ervan af, dan meldt zij dat terug aan de werkgroep procesarchitectuur (regel Afwijken mits teruggemeld).

Deze bronduiding voegt de duidingen van twee onderwerpen samen, letterlijk, per sectie: eerst Lijkbezorging, dan Burgerzaken. In de tabellen staan de rijen van Lijkbezorging eerst.

### Lijkbezorging

De externe producten- en dienstenlijst van de GEMMA-procesarchitectuur (versie 1.0) is een bewerking van de Uniforme Productenlijst (UPL). Voor dit onderwerp gaat het om 16 producten (afbakening met de redacteur, 2026-10-04): de vijftien producten over begraafplaats, crematorium, asbestemming, vervoer en verlof, en de aangifte van een doodgeboren kind. Die laatste hoort erbij omdat de Wet op de lijkbezorging ook voor een doodgeborene geldt. De geboorteakte van een levenloos kind en de overlijdensuitkering vallen erbuiten.

De lijst bepaalt welke producten een gemeente levert en waarop ze steunen. De betekenis staat er niet in: er is geen definitie of beschrijving. Per product geeft de lijst het Iv3-taakveld, de doelgroep (burger, bedrijf), Dienstenwet en SDG, de grondslag met link, het GEMMA-domein en of er een digitaal kanaal is. Brontype informatiemodel: de lijst hoort bij de GEMMA-architectuur (besluit redacteur 2026-10-04). De gangbare naam en de herkenbare definitie komen uit de beleids- en praktijkbronnen (regel Bronvoorrang). Een productnaam uit de UPL is een synoniem met context "UPL" of de naam van een product.

Wat opvalt:

- **Taakveld:** elf producten staan onder Iv3 7.5 (Begraafplaatsen en crematoria). Verlof tot begraven, overlijdensaangifte, overlijdensakte en doodgeboren kind aangifte staan onder 0.2 (Burgerzaken). Ontleding stoffelijk overschot toestemming heeft geen taakveld.
- **GEMMA-domein:** verwante producten staan in verschillende domeinen. Begraafplaatsregister en bijzondere begraafplaats toestemming staan bij Publieksdiensten, de andere registers en vergunningen bij Fysieke leefomgeving en asverstrooiing bij Openbare orde en Veiligheid.
- **Grondslagen:** zeven producten steunen op de Wet op de lijkbezorging (art. 11, 27, 29, 40–41, 50, 65, 67), drie op Boek 1 BW (art. 19f, 19h, 19i) en grafrechten op Gemeentewet art. 229. Gedenkteken plaatsingsvergunning steunt op art. 19 van de model-beheersverordening (Vergunning grafbedekking; 2010-vng-model-beheersverordening-begraafplaatsen, regel 201) en grafuitgifte op art. 11 (in het model "Indeling graven en asbezorging", regel 143). De uitgifte zelf staat in art. 13 tot 15 van het model. Asverstrooiing steunt op model-APV art. 5:36 en vervoersdocumenten op Besluit op de lijkbezorging art. 11. Grafonderhoud steunt op het begraafplaatsenbeleid van één gemeente (CVDR659831) en niet op art. 20–21 van het model.
- **Digitaal kanaal (J):** asverstrooiing, bijzondere begraafplaats toestemming, gedenkteken plaatsingsvergunning, herbegraven of alsnog cremeren, ontleding, verlof tot begraven en vervoersdocumenten.
- **Registers:** begraafplaats-, bijzettingen- en crematoriumregister zijn producten voor bedrijven onder de Dienstenwet. De afnemer is de houder (van de begraafplaats, plaats van bijzetting of crematorium), niet de nabestaande.

### Burgerzaken

De externe producten- en dienstenlijst van de GEMMA-procesarchitectuur (versie 1.0) is een bewerking van de Uniforme Productenlijst (UPL) met 500 producten. Voor dit onderwerp gaat het om de producten onder Iv3-taakveld 0.2 Burgerzaken: 73 van de 500, waarvan 56 binnen de afbakening staan (BRP, burgerlijke stand, reisdocumenten, kiesrecht, Nederlanderschap). De lijst bepaalt welke producten een gemeente levert en waarop ze steunen; de betekenis staat er niet in, want er zijn geen definities of beschrijvingen. Per product geeft de lijst het Iv3-taakveld, de doelgroep (burger, bedrijf), Dienstenwet en SDG, tot zes grondslagen met link, het GEMMA-domein en of er een digitaal kanaal is. Alle producten hebben soort Primair, specifiek/generiek Generiek en GEMMA-domein Publieksdiensten. Brontype informatiemodel: de lijst hoort bij de GEMMA-architectuur (besluit redacteur 2026-10-04). De gangbare naam en de herkenbare definitie komen uit de beleids- en praktijkbronnen; een productnaam uit de UPL is een synoniem met context UPL.

Wat opvalt:

- **Reisdocumenten:** de UPL kent zeven producten: paspoort (art. 26 Paspoortwet, doelgroep burger en bedrijf), paspoort tweede (art. 30), zakenpaspoort (grondslag Paspoortuitvoeringsregeling Buitenland 2001, niet de Paspoortwet), vluchtelingenpaspoort en vreemdelingenpaspoort (art. 11), identiteitskaart (art. 16a) en reisdocument en reisdocument niet-ingezetene (art. 4.2 Paspoortbesluit). Het product reisdocument heeft geen doelgroep. Een nooddocument en het waarmerken van een kopie van een reisdocument komen niet voor.
- **Naamgeving:** de UPL gebruikt productnamen op het niveau van de gebeurtenis of de akte (geboorteaangifte, geboorteakte, huwelijksaangifte, huwelijk, overlijdensakte), zonder onderscheid tussen product, dienst en bedrijfsobject. Ze mengt dus producten (paspoort), akten en uittreksels (bedrijfsobjecten), registraties (brp-inschrijving) en rollen (ambtenaar burgelijke stand).
- **Digitaal kanaal (J):** achternaamwijziging, briefadres, brp-adoptie-uitschrijving, brp-geheimhoudingsverzoek, brp-wijzigingsverzoek, geboorteaangifte, huwelijksaangifte, trouwlocatie, verhuismelding en verklaring van huwelijksbevoegdheid. Het kanaal In Persoon (kolom bewijs WMBEV) staat bij de aanvragen die een bezoek vereisen.
- **Taakveld:** verlof tot begraven staat in de lijst onder 0.2 maar hoort bij Lijkbezorging.
- **Rijbewijs en VOG:** rijbewijs (nr. 360, art. 26 Reglement rijbewijzen), rijbewijs buitenlands omwisseling (nr. 361, art. 45), rijbewijs gezondheidsverklaring (nr. 362, art. 100), rijbewijs verlengen (nr. 363, art. 35) en verklaring omtrent gedrag (vog) (nr. 434, art. 28 Wet justitiële en strafvorderlijke gegevens) staan onder 0.2 en vallen sinds het besluit van 2026-10-07 binnen de afbakening (zesde plak). De grondslagen staan in de bronnen Reglement rijbewijzen, Wegenverkeerswet 1994 en Wet justitiële en strafvorderlijke gegevens. Bij nr. 362 wijkt de UPL af van de wet: art. 100 legt de aanvraag van de verklaring van geschiktheid bij het CBR, niet bij de gemeente (zie de bronanalyse van het Reglement). Nr. 362 is geen zelfstandige dienst maar een subdienst, een onderdeel van Rijbewijs aanvragen (nr. 360): de gemeente controleert de verklaring van geschiktheid als onderdeel van Behandelen aanvraag rijbewijs (besluit redacteur 2026-10-07; procesarchitectuur-terugmelding 18). Taakveld 0.2 klopt voor deze vijf wel.
- **Kiesrecht:** kiezerspas, stempas en stemrecht staan in de lijst; de organisatie van de verkiezingen valt buiten de afbakening.

Buiten de afbakening bij de 73 producten onder 0.2: verlof tot begraven (Lijkbezorging, in de analyse van dat onderwerp); melding openbare ruimte (vier producten), reclamesticker, contactgegevens aanpassing en overlijdensuitkering (geen burgerzaken); kandidaatstelling verkiezingen, stembiljet, stemmen identificatieplicht en volmachtbewijs verkiezingen (organisatie van de verkiezingen).

## Kernbegrippen

| Begrip | Omschrijving in de bron | Andere termen in deze bron | Vindplaats |
|---|---|---|---|
| asverstrooiing | product, Iv3 7.5, burger en bedrijf, Dienstenwet; grondslag model-APV art. 5:36; Openbare orde en Veiligheid; digitaal | — | regel 46 (nr. 32) |
| begraafplaatsregister | product, Iv3 7.5, bedrijf, Dienstenwet; grondslag Wlb art. 27; Publieksdiensten | — | regel 59 (nr. 45) |
| bijzettingenregister | product, Iv3 7.5, bedrijf, Dienstenwet; grondslag Wlb art. 65; Fysieke leefomgeving | — | regel 84 (nr. 70) |
| bijzondere begraafplaats toestemming | product, Iv3 7.5, burger en bedrijf, Dienstenwet; grondslag Wlb art. 40 en 41; Publieksdiensten; digitaal | — | regel 85 (nr. 71) |
| crematoriumregister | product, Iv3 7.5, bedrijf, Dienstenwet; grondslag Wlb art. 50; Fysieke leefomgeving | — | regel 120 (nr. 106) |
| doodgeboren kind aangifte | product, Iv3 0.2, burger, SDG; grondslag BW 1 art. 19i; Publieksdiensten; bewijs in persoon | — | regel 132 (nr. 118) |
| gedenkteken plaatsingsvergunning | product, Iv3 7.5, burger en bedrijf, Dienstenwet; grondslag model-beheersverordening art. 19; Fysieke leefomgeving; digitaal | model: vergunning grafbedekking | regel 156 (nr. 142) |
| grafonderhoud | product, Iv3 7.5, burger en bedrijf; grondslag Begraafplaatsenbeleid 2020-2030 (CVDR659831); Fysieke leefomgeving | — | regel 177 (nr. 163) |
| grafrechten | product, Iv3 7.5, burger; grondslag Gemeentewet art. 229; Fysieke leefomgeving | — | regel 178 (nr. 164) |
| grafuitgifte | product, Iv3 7.5, burger en bedrijf; grondslag model-beheersverordening art. 11; Fysieke leefomgeving | — | regel 179 (nr. 165) |
| herbegraven of alsnog cremeren | product, Iv3 7.5, burger en bedrijf, Dienstenwet; grondslag Wlb art. 29; Fysieke leefomgeving; digitaal | wet: opgraven | regel 185 (nr. 171) |
| ontleding stoffelijk overschot toestemming | product, geen taakveld, bedrijf; grondslag Wlb art. 67; Fysieke leefomgeving; digitaal | wet: ontleding, lijk | regel 320 (nr. 306) |
| overlijdensaangifte | product, Iv3 0.2, burger en bedrijf, SDG; grondslag BW 1 art. 19h; Publieksdiensten | — | regel 329 (nr. 315) |
| overlijdensakte | product, Iv3 0.2, burger; grondslag BW 1 art. 19f; Publieksdiensten | — | regel 330 (nr. 316) |
| verlof tot begraven | product, Iv3 0.2, burger en bedrijf, Dienstenwet; grondslag Wlb art. 11; Fysieke leefomgeving; digitaal | wet: verlof tot begraving of crematie | regel 452 (nr. 438) |
| vervoersdocumenten stoffelijk overschot | product, Iv3 7.5, burger en bedrijf, Dienstenwet, SDG; grondslag Besluit op de lijkbezorging art. 11; Fysieke leefomgeving; digitaal | besluit: laissez-passer voor lijken | regel 459 (nr. 445) |
| Burger, Bedrijf | doelgroep van een product (kolom met X) | — | regel 13 |
| Iv3 | taakveld van een product | — | regel 13 |
| GEMMA Domeinen | domein van een product | — | regel 13 |
| DigitaalKanaal | of het product digitaal wordt aangeboden (J/N) | — | regel 13 |
| aangifte vertrek buitenland | primair, Iv3 0.2, burger, SDG; grondslag Artikel 2.43 Wet basisregistratie personen; Publieksdiensten; niet digitaal; bewijs in persoon | vergelijk Utrecht: emigratie doorgeven | regel 15 (nr. 1) |
| achternaamwijziging | primair, Iv3 0.2, burger; grondslag Artikel 7 Burgerlijk Wetboek Boek 1; Publieksdiensten; digitaal | vergelijk Utrecht: voornaam of achternaam veranderen | regel 19 (nr. 5) |
| adoptie aangifte | primair, Iv3 0.2, burger; grondslag Artikel 2.38 Wet basisregistratie personen; Publieksdiensten; niet digitaal; bewijs in persoon | vergelijk Utrecht: adoptie kind inschrijven | regel 20 (nr. 6) |
| akte van de burgerlijke stand | primair, Iv3 0.2, burger; grondslag Artikel 23b Burgerlijk Wetboek Boek 1; Publieksdiensten; niet digitaal | — | regel 37 (nr. 23) |
| ambtenaar burgelijke stand | primair, Iv3 0.2, burger; grondslag Artikel 16 Burgerlijk Wetboek Boek 1; Publieksdiensten; niet digitaal | wet: ambtenaar van de burgerlijke stand (de UPL schrijft burgelijke) | regel 42 (nr. 28) |
| bewijs van in leven zijn (attestatie de vita) | primair, Iv3 0.2, burger, SDG; grondslag Artikel 19k Burgerlijk Wetboek Boek 1; Publieksdiensten; niet digitaal; bewijs in persoon | vergelijk Utrecht: bewijs van in leven zijn of attestatie de vita | regel 75 (nr. 61) |
| bewijs van nederlanderschap | primair, Iv3 0.2, burger; grondslag Artikel 2.55 Wet basisregistratie personen; Publieksdiensten; niet digitaal | — | regel 76 (nr. 62) |
| briefadres | primair, Iv3 0.2, burger; grondslag Artikel 2.23 Wet basisregistratie personen; Publieksdiensten; digitaal | — | regel 99 (nr. 85) |
| brp-adoptie-uitschrijving | primair, Iv3 0.2, burger; grondslag Artikel 2.57 Wet basisregistratie personen; Publieksdiensten; digitaal | vergelijk Utrecht: adoptie kind inschrijven | regel 100 (nr. 86) |
| brp-geheimhoudingsverzoek | primair, Iv3 0.2, burger; grondslag Artikel 2.59 Wet basisregistratie personen; Publieksdiensten; digitaal | vergelijk Utrecht: persoonsgegevens geheimhouden | regel 101 (nr. 87) |
| brp-inschrijving | primair, Iv3 0.2, burger, SDG; grondslag Artikel 2.38 Wet basisregistratie personen; Publieksdiensten; niet digitaal; bewijs in persoon | vergelijk Utrecht: inschrijven vanuit het buitenland | regel 102 (nr. 88) |
| brp-inschrijving buitenlandse akte | primair, Iv3 0.2, burger, SDG; grondslag Artikel 2.38 Wet basisregistratie personen; Publieksdiensten; niet digitaal; bewijs in persoon | vergelijk Utrecht: buitenlandse documenten inschrijven | regel 103 (nr. 89) |
| brp-inschrijving niet in leven zijnd kind | primair, Iv3 0.2, burger; grondslag Artikel 2.56a Wet basisregistratie personen; Publieksdiensten; niet digitaal; bewijs in persoon | — | regel 104 (nr. 90) |
| brp-inzagerecht | primair, Iv3 0.2, burger, SDG; grondslag Artikel 2.55 Wet basisregistratie personen; Publieksdiensten; niet digitaal | vergelijk Utrecht: persoonsgegevens BRP bekijken | regel 105 (nr. 91) |
| brp-inzagerecht gegevensverstrekking | primair, Iv3 0.2, burger; grondslag Artikel 3.22 Wet basisregistratie personen; Publieksdiensten; niet digitaal | — | regel 106 (nr. 92) |
| brp-uittreksel | primair, Iv3 0.2, burger; grondslag Artikel 2.55 Wet basisregistratie personen; Publieksdiensten; niet digitaal | vergelijk Utrecht: uittreksel of akte aanvragen | regel 107 (nr. 93) |
| brp-uittreksel met gezag | primair, Iv3 0.2, burger; grondslag Artikel 2.55 Wet basisregistratie personen; Publieksdiensten; niet digitaal | — | regel 108 (nr. 94) |
| brp-wijzigingsverzoek | primair, Iv3 0.2, burger; grondslag Artikel 2.58 Wet basisregistratie personen; Publieksdiensten; digitaal | vergelijk Utrecht: persoonsgegevens opvragen of aanpassen BRP | regel 109 (nr. 95) |
| doodgeboren kind aangifte | primair, Iv3 0.2, burger, SDG; grondslag Artikel 19i Burgerlijk Wetboek Boek 1; Publieksdiensten; niet digitaal; bewijs in persoon | vergelijk Utrecht: levenloos geboren kind of overleden pasgeboren kind aangifte doen | regel 132 (nr. 118) |
| echtscheiding inschrijving | primair, Iv3 0.2, burger, SDG; grondslag Artikel 163 Burgerlijk Wetboek Boek 1; Publieksdiensten; niet digitaal | vergelijk Utrecht: scheiden of geregistreerd partnerschap beëindigen | regel 136 (nr. 122) |
| erkenning kind | primair, Iv3 0.2, burger, SDG; grondslag Artikel 203 Burgerlijk Wetboek Boek 1; Publieksdiensten; niet digitaal; bewijs in persoon | vergelijk Utrecht: kind erkennen | regel 143 (nr. 129) |
| geboorteaangifte | primair, Iv3 0.2, burger, SDG; grondslag Artikel 19e Burgerlijk Wetboek Boek 1; Publieksdiensten; digitaal | vergelijk Utrecht: geboorteaangifte doen | regel 150 (nr. 136) |
| geboorteakte | primair, Iv3 0.2, burger, SDG; grondslag Artikel 19 Burgerlijk Wetboek Boek 1; Publieksdiensten; niet digitaal | — | regel 151 (nr. 137) |
| geboorteakte levenloos kind | primair, Iv3 0.2, burger; grondslag Artikel 19i Burgerlijk Wetboek Boek 1; Publieksdiensten; niet digitaal | — | regel 152 (nr. 138) |
| geregistreerd partnerschap omzetting in huwelijk | primair, Iv3 0.2, burger; grondslag Artikel 80g Burgerlijk Wetboek Boek 1; Publieksdiensten; niet digitaal; bewijs in persoon | — | regel 170 (nr. 156) |
| geregistreerd partnerschap ontbinding | primair, Iv3 0.2, burger, SDG; grondslag Artikel 80c Burgerlijk Wetboek Boek 1; Publieksdiensten; niet digitaal | — | regel 171 (nr. 157) |
| geregistreerd partnerschapaangifte | primair, Iv3 0.2, burger, SDG; grondslag Artikel 80a Burgerlijk Wetboek Boek 1; Publieksdiensten; niet digitaal | vergelijk Utrecht: voorgenomen huwelijk of geregistreerd partnerschap melden | regel 172 (nr. 158) |
| geslachtswijzigingsaangifte | primair, Iv3 0.2, burger, SDG; grondslag Artikel 28 Burgerlijk Wetboek Boek 1; Publieksdiensten; niet digitaal; bewijs in persoon | vergelijk Utrecht: geslacht vermelding aanpassen | regel 173 (nr. 159) |
| huwelijk | primair, Iv3 0.2, burger; grondslag Artikel 30 Burgerlijk Wetboek Boek 1; Publieksdiensten; niet digitaal; bewijs in persoon | — | regel 198 (nr. 184) |
| huwelijksaangifte | primair, Iv3 0.2, burger, SDG; grondslag Artikel 44 Burgerlijk Wetboek Boek 1; Publieksdiensten; digitaal | vergelijk Utrecht: voorgenomen huwelijk of geregistreerd partnerschap melden | regel 199 (nr. 185) |
| identiteitskaart | primair, Iv3 0.2, burger; grondslag Artikel 16a Paspoortwet; Publieksdiensten; niet digitaal; bewijs in persoon | wet: Nederlandse identiteitskaart; Utrecht: ID-kaart | regel 200 (nr. 186) |
| kiezerspas | primair, Iv3 0.2, burger; grondslag Artikel K 1 Kieswet; Publieksdiensten; niet digitaal | wet: kiezerspas | regel 222 (nr. 208) |
| legalisatie handtekening | primair, Iv3 0.2, burger; grondslag Wet griffierechten burgelijke zaken artikel 23; Publieksdiensten; niet digitaal; bewijs in persoon | vergelijk Utrecht: handtekening laten legaliseren | regel 240 (nr. 226) |
| naamgebruik verzoek aanduiding | primair, Iv3 0.2, burger; grondslag Artikel 2.25 Wet basisregistratie personen; Publieksdiensten; niet digitaal | — | regel 271 (nr. 257) |
| naamskeuzeverklaring | primair, Iv3 0.2, burger; grondslag Artikel 5 Burgerlijk Wetboek Boek 1; Publieksdiensten; niet digitaal; bewijs in persoon | vergelijk Utrecht: achternaam kind kiezen | regel 272 (nr. 258) |
| naturalisatieceremonie | primair, Iv3 0.2, burger; grondslag Artikel 60a Besluit verkrijging en verlies Nederlanderschap; Publieksdiensten; niet digitaal | — | regel 275 (nr. 261) |
| naturalisatieoptie | primair, Iv3 0.2, burger; grondslag Artikel 6 Rijkswet op het Nederlanderschap; Publieksdiensten; niet digitaal; bewijs in persoon | vergelijk Utrecht: Nederlander worden door naturalisatie of optie | regel 276 (nr. 262) |
| naturalisatieverzoek | primair, Iv3 0.2, burger, SDG; grondslag Artikel 7 Rijkswet op het Nederlanderschap; Publieksdiensten; niet digitaal; bewijs in persoon | vergelijk Utrecht: Nederlander worden door naturalisatie of optie | regel 277 (nr. 263) |
| overlijdensaangifte | primair, Iv3 0.2, burger en bedrijf, SDG; grondslag Artikel 19h Burgerlijk Wetboek Boek 1; Publieksdiensten; niet digitaal | vergelijk Utrecht: overlijden aangifte doen | regel 329 (nr. 315) |
| overlijdensakte | primair, Iv3 0.2, burger; grondslag Artikel 19f Burgerlijk Wetboek Boek 1; Publieksdiensten; niet digitaal | — | regel 330 (nr. 316) |
| paspoort | primair, Iv3 0.2, burger en bedrijf, SDG; grondslag Artikel 26 Paspoortwet; Publieksdiensten; niet digitaal; bewijs in persoon | wet: nationaal paspoort; Utrecht: paspoort | regel 343 (nr. 329) |
| paspoort tweede | primair, Iv3 0.2, burger, SDG; grondslag Artikel 30 Paspoortwet; Publieksdiensten; niet digitaal; bewijs in persoon | wet: verzoek om houder te blijven van een geldig reisdocument naast het aangevraagde reisdocument; Utrecht: tweede paspoort | regel 344 (nr. 330) |
| persoonsgegevens verklaring onder eed of belofte | primair, Iv3 0.2, burger; grondslag Artikel 2.8 Wet basisregistratie personen; Publieksdiensten; niet digitaal; bewijs in persoon | — | regel 349 (nr. 335) |
| reisdocument | primair, Iv3 0.2, geen doelgroep; grondslag Artikel 4.2 Paspoortbesluit; Publieksdiensten; niet digitaal; bewijs in persoon | wet: reisdocument | regel 370 (nr. 356) |
| reisdocument niet-ingezetene | primair, Iv3 0.2, burger; grondslag Artikel 4.2 Paspoortbesluit; Publieksdiensten; niet digitaal; bewijs in persoon | besluit: aanvragen van niet-ingezetenen bij de burgemeester van een aangewezen gemeente | regel 371 (nr. 357) |
| rni inschrijving | primair, Iv3 0.2, burger, SDG; grondslag Artikel 2.66 Wet basisregistratie personen; Publieksdiensten; niet digitaal; bewijs in persoon | vergelijk Utrecht: registratie niet-ingezetenen (RNI) inschrijven | regel 383 (nr. 369) |
| stempas | primair, Iv3 0.2, burger; grondslag Artikel J 7 Kieswet; Publieksdiensten; niet digitaal | — | regel 411 (nr. 397) |
| stemrecht | primair, Iv3 0.2, burger, SDG; grondslag Artikel B 1 Kieswet; Artikel B 2 Kieswet; Artikel B 2a Kieswet; Artikel B 3 Kieswet; Artikel Y 2 Kieswet; Publieksdiensten; niet digitaal | wet: kiesrecht | regel 412 (nr. 398) |
| trouwlocatie | primair, Iv3 0.2, burger en bedrijf; grondslag Artikel 63 Burgerlijk Wetboek Boek 1; Publieksdiensten; digitaal | vergelijk Utrecht: trouwlocaties in Utrecht | regel 428 (nr. 414) |
| verhuismelding | primair, Iv3 0.2, burger, SDG; grondslag Artikel 2.39 Wet basisregistratie personen; Publieksdiensten; digitaal | vergelijk Utrecht: verhuizing doorgeven | regel 438 (nr. 424) |
| verklaring van afstand nederlandse nationaliteit | primair, Iv3 0.2, burger; grondslag Artikel 15 Rijkswet op het Nederlanderschap; Publieksdiensten; niet digitaal; bewijs in persoon | vergelijk Utrecht: Nederlandse nationaliteit opgeven of verliezen | regel 450 (nr. 436) |
| verklaring van huwelijksbevoegdheid | primair, Iv3 0.2, burger; grondslag Overeenkomst betreffende de afgifte van een verklaring van huwelijksbevoegdheid, München, 05-09-1980; Publieksdiensten; digitaal | — | regel 451 (nr. 437) |
| vluchtelingenpaspoort | primair, Iv3 0.2, burger; grondslag Artikel 11 Paspoortwet; Publieksdiensten; niet digitaal; bewijs in persoon | wet: reisdocument voor vluchtelingen | regel 463 (nr. 449) |
| voornaamwijziging | primair, Iv3 0.2, burger; grondslag Artikel 4 Burgerlijk Wetboek Boek 1; Publieksdiensten; niet digitaal | vergelijk Utrecht: voornaam of achternaam veranderen | regel 474 (nr. 460) |
| vreemdelingenpaspoort | primair, Iv3 0.2, burger; grondslag Artikel 11 Paspoortwet; Publieksdiensten; niet digitaal; bewijs in persoon | wet: reisdocument voor vreemdelingen | regel 476 (nr. 462) |
| zakenpaspoort | primair, Iv3 0.2, burger, SDG; grondslag Artikel 3 Paspoortuitvoeringsregeling Buitenland 2001; Publieksdiensten; niet digitaal; bewijs in persoon | Utrecht: zakenpaspoort; Paspoortwet kent het niet (letter B in het documentnummer volgens de HUP) | regel 508 (nr. 494) |

## Relaties

| Van | Werkwoord | Naar | Vindplaats |
|---|---|---|---|
| burger | is doelgroep van | asverstrooiing, bijzondere begraafplaats toestemming, doodgeboren kind aangifte, gedenkteken plaatsingsvergunning, grafonderhoud, grafrechten, grafuitgifte, herbegraven of alsnog cremeren, overlijdensaangifte, overlijdensakte, verlof tot begraven, vervoersdocumenten stoffelijk overschot | kolom Burger, regels 46–459 |
| bedrijf | is doelgroep van | asverstrooiing, begraafplaatsregister, bijzettingenregister, bijzondere begraafplaats toestemming, crematoriumregister, gedenkteken plaatsingsvergunning, grafonderhoud, grafuitgifte, herbegraven of alsnog cremeren, ontleding stoffelijk overschot toestemming, overlijdensaangifte, verlof tot begraven, vervoersdocumenten stoffelijk overschot | kolom Bedrijf, regels 46–459 |
| verlof tot begraven | heeft grondslag | Wet op de lijkbezorging art. 11 | regel 452 |
| herbegraven of alsnog cremeren | heeft grondslag | Wet op de lijkbezorging art. 29 | regel 185 |
| bijzondere begraafplaats toestemming | heeft grondslag | Wet op de lijkbezorging art. 40 en 41 | regel 85 |
| ontleding stoffelijk overschot toestemming | heeft grondslag | Wet op de lijkbezorging art. 67 | regel 320 |
| begraafplaatsregister, crematoriumregister, bijzettingenregister | heeft grondslag | Wet op de lijkbezorging art. 27, 50, 65 | regels 59, 120, 84 |
| grafrechten | heeft grondslag | Gemeentewet art. 229 | regel 178 |
| grafuitgifte | heeft grondslag | model-beheersverordening art. 11 | regel 179 |
| gedenkteken plaatsingsvergunning | heeft grondslag | model-beheersverordening art. 19 | regel 156 |
| asverstrooiing | heeft grondslag | model-APV art. 5:36 | regel 46 |
| vervoersdocumenten stoffelijk overschot | heeft grondslag | Besluit op de lijkbezorging art. 11 | regel 459 |
| overlijdensaangifte, overlijdensakte, doodgeboren kind aangifte | heeft grondslag | Burgerlijk Wetboek Boek 1 art. 19h, 19f, 19i | regels 329, 330, 132 |
| burger | is doelgroep van | alle producten in de tabel, behalve reisdocument (geen doelgroep) | kolom Burger |
| bedrijf | is doelgroep van | overlijdensaangifte, paspoort, trouwlocatie | kolom Bedrijf, regels 329, 343, 428 |
| paspoort, paspoort tweede, identiteitskaart, vluchtelingenpaspoort, vreemdelingenpaspoort | heeft grondslag | Paspoortwet art. 26, 30, 16a, 11, 11 | regels 343, 344, 200, 463, 476 |
| reisdocument, reisdocument niet-ingezetene | heeft grondslag | Paspoortbesluit art. 4.2 | regels 370, 371 |
| zakenpaspoort | heeft grondslag | Paspoortuitvoeringsregeling Buitenland 2001 art. 3 | regel 508 |
| brp-inschrijving, brp-inschrijving buitenlandse akte, adoptie aangifte, aangifte vertrek buitenland, verhuismelding, briefadres, rni inschrijving, brp-uittreksel, brp-inzagerecht | heeft grondslag | Wet basisregistratie personen art. 2.38, 2.43, 2.39, 2.23, 2.66, 2.55 | regels 102, 103, 20, 15, 438, 99, 383, 107, 105 |
| geboorteaangifte, geboorteakte, doodgeboren kind aangifte, overlijdensaangifte, overlijdensakte | heeft grondslag | Burgerlijk Wetboek Boek 1 art. 19e, 19, 19i, 19h, 19f | regels 150, 151, 132, 329, 330 |
| huwelijk, huwelijksaangifte, geregistreerd partnerschapaangifte, geregistreerd partnerschap ontbinding, echtscheiding inschrijving | heeft grondslag | Burgerlijk Wetboek Boek 1 art. 30, 44, 80a, 80c, 163 | regels 198, 199, 172, 171, 136 |
| stemrecht, stempas, kiezerspas | heeft grondslag | Kieswet art. B 1 tot en met B 3 en Y 2, J 7, K 1 | regels 412, 411, 222 |
| naturalisatieverzoek, naturalisatieoptie, verklaring van afstand nederlandse nationaliteit | heeft grondslag | Rijkswet op het Nederlanderschap art. 7, 6, 15 | regels 277, 276, 450 |
| naturalisatieceremonie | heeft grondslag | Besluit verkrijging en verlies Nederlanderschap art. 60a | regel 275 |
| ambtenaar burgelijke stand | heeft grondslag | Burgerlijk Wetboek Boek 1 art. 16 | regel 42 |

## Relevantie voor de architectuur

### Lijkbezorging

- **Producten en diensten:** de lijst is de referentie voor het kenmerk *levert aanbod* (beslistabel, rij Gedrag). Elk van de 16 is een kandidaat-product of -dienst. Bij het beoordelen moet blijken of het een product is (een bundel met een afspraak, zoals grafuitgifte met het grafrecht) of een dienst (zoals verlof tot begraven of een register raadplegen). De naam van een dienst volgt de regel Naamvorm. De UPL-naam wordt een synoniem.
- **Aansluiting op de wiki:** de producten passen bij begrippen die er al zijn. Grafuitgifte past bij *Verlenen grafrecht* en de dienst *Graf aanvragen*, grafrechten bij *Lijkbezorgingsrechten* en *Heffing*, grafonderhoud bij *Onderhouden graf*, gedenkteken plaatsingsvergunning bij *Vergunning grafbedekking*, herbegraven bij *Opgraven lijk* en *Vergunning tot opgraving*, verlof tot begraven bij *Verlenen verlof tot begraving of crematie*, asverstrooiing bij *Incidentele asverstrooiing*, bijzondere begraafplaats toestemming bij *Verlenen toestemming bijzondere begraafplaats* en ontleding bij *Verlof tot ontleding*. Voor vervoersdocumenten is er nog geen begrip (zie de bronanalyse van het Besluit op de lijkbezorging). De ijking in `analyses/indelingen.md` (§ IJking met de UPL) koppelt elk product aan een deelproces.
- **Burgerzaken:** overlijdensaangifte, overlijdensakte en doodgeboren kind aangifte staan onder 0.2. *Aangifte van overlijden* en *Akte van overlijden* zijn verwijzingen naar het onderwerp burgerlijke stand.
- **Indelingen:** het Iv3-taakveld en het GEMMA-domein per product zijn de twee ouders in de Beleidsdomeinindeling en de Functie-indeling (besluit redacteur 2026-10-04). Waar de lijst afwijkt (verlof tot begraven onder 0.2, domeinen die verschillen), legt de beoordeling dat vast.
- **Rollen:** de doelgroep bedrijf bij de registers en bij ontleding wijst op de houder van de begraafplaats of het crematorium en op een instelling voor ontleding als afnemer.
- **Kanaal:** DigitaalKanaal J of N is input voor de centrale set kanalen (todo).

### Burgerzaken

- **Producten en diensten:** de lijst is de referentie voor het kenmerk levert aanbod. Elk van de 56 in scope is een kandidaat-product of -dienst; bij de beoordeling moet blijken of het een product is (een bundel met een afspraak, bijvoorbeeld paspoort, huwelijk), een dienst (bijvoorbeeld verhuizing doorgeven, uittreksel aanvragen) of geen van beide maar een bedrijfsobject (geboorteakte, overlijdensakte, akte van de burgerlijke stand, stempas, kiezerspas, bewijs van nederlanderschap), een gebeurtenis (huwelijk, geboorteaangifte) of een rol (ambtenaar burgelijke stand). De naam van een dienst volgt de regel Naamvorm; de UPL-naam wordt een synoniem.
- **Reisdocumenten:** de UPL splitst het reisdocument in zeven producten; de Paspoortwet kent drie aanspraken (nationaal paspoort, reisdocument voor vluchtelingen en voor vreemdelingen) plus nooddocument. Het zakenpaspoort steunt op een andere regeling en niet op de Paspoortwet.
- **BRP en burgerlijke stand:** de lijst werkt met aangiften en inschrijvingen als producten (brp-inschrijving, geboorteaangifte). De naamgeving volgt het wetsartikel in plaats van de gemeentelijke praktijk (Utrecht: verhuizing doorgeven, inschrijven vanuit het buitenland).
- **Kiesrecht:** stemrecht, stempas en kiezerspas zijn de producten die binnen de afbakening vallen.
- **Kanaal:** DigitaalKanaal J of N is input voor de centrale set kanalen (todo). De kolom bewijs WMBEV (In Persoon) geeft aan voor welke producten persoonlijk verschijnen nodig is.
- **Indelingen:** de producten staan alle onder Iv3 0.2 en GEMMA-domein Publieksdiensten; een ijking met de beleidsdomeinindeling is daardoor eenvoudig.

## Citaten

### Lijkbezorging

> asverstrooiing | 7.5 | … | Artikel 5:36 Model Algemene plaatselijke verordening (regel 46)

> grafuitgifte | 7.5 | … | Artikel 11 Model Beheersverordening begraafplaatsen (regel 179)

> verlof tot begraven | 0.2 | … | Artikel 11 Wet op de lijkbezorging (regel 452)

> vervoersdocumenten stoffelijk overschot | 7.5 | … | Artikel 11 Besluit op de lijkbezorging (regel 459)

> Specifiek/Generiek: Specifiek/generiek met definitie : van toepassing voor een gemeente/van toepassing voor alle gemeenten vanuit wetgeving (kolomkop, regel 13)

### Burgerzaken

> paspoort | 0.2 | ... | Artikel 26 Paspoortwet (regel 343)

> zakenpaspoort | 0.2 | ... | Artikel 3 Paspoortuitvoeringsregeling Buitenland 2001 (regel 508)

> reisdocument | 0.2 | ... | Artikel 4.2 Paspoortbesluit (regel 370)

> Specifiek/Generiek: Specifiek/generiek met definitie : van toepassing voor een gemeente/van toepassing voor alle gemeenten vanuit wetgeving (kolomkop, regel 13)
