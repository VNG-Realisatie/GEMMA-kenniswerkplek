<!-- gegenereerd door tools/ggm.py; hash: 42a29cb34ffb8491273ec45da4aba738f17d85db99531362c77d7b4750415c06 -->
# Vroegsignalering

Taakveld: Schulden. Alleen objecttypen; letterlijke definities uit het GGM.

## AanleverendeOrganisatie

Organisatie de data aanlevert aan het CBS. Het kan hier gaan om de gemeente zelf, of een partij die namens de gemeente uitvoering geeft aan de afhandeling van vroegsignalen.

Attributen: naam, kvk-nummer.

GUID: `EAID_3109FEF3_A1CB_4f50_800B_376A18465F9F`

Relaties:

- contactpersonen → Contactpersoon (*Association*, 1..1 → 1..*, `EAID_98E54A02_6094_44ba_927B_2F06691C90BD`)

## Contactpersoon

Contactpersoon bij de aanleverende organisatie.

Attributen: naam, telefoonnummer, email, functietitel.

GUID: `EAID_A629ED5F_E919_6316_A279_92891F2325BB`

## Contactpoging

Een Contactpoging is de actie die de gemeente onderneemt om in contact te treden met de inwoner naar aanleiding van een vroegsignaal. Een contactpoging maakt onderdeel uit van de vroegsignaalzaak en kan verschillende vormen aannemen, zoals een telefoongesprek, huisbezoek, brief of digitaal bericht. Van elke contactpoging wordt vastgelegd wanneer deze is gedaan, op welke wijze, met welk doel en wat het resultaat was (bijvoorbeeld: geen gehoor, gesprek gevoerd, brief retour ontvangen).

Attributen: soort, bereikt, datum, dagdeel.

GUID: `EAID_C7000EFD_826C_4e47_BD80_075A6EF4E558`

## Signaalpartner

Een signaalpartner is een organisatie die op grond van artikel 2.2.1 van de Wet gemeentelijke schuldhulpverlening (Wgs) bevoegd is om signalen van betalingsachterstanden door te geven aan de gemeente met het doel vroegtijdige hulpverlening bij schulden mogelijk te maken. Signaalpartners zijn dienstverleners met een maatschappelijk belang, zoals zorgverzekeraars, energieleveranciers, drinkwaterbedrijven en woningverhuurders. Een signaalpartner verstrekt een vroegsignaal aan de gemeente wanneer bij een klant of huurder sprake is van een betalingsachterstand die voldoet aan de wettelijke en/of contractuele criteria voor signalering.

Attributen: type.

GUID: `EAID_3643CF44_EFAA_4939_9AEB_ACA8D8EE11F9`

Relaties:

- → Rechtspersoon (*Generalization*,  → , `EAID_9769C85C_A134_467c_90A1_8131814AB300`)

## Vroegsignaal

Een Vroegsignaal is een bericht dat door een signaalpartner (zoals een zorgverzekeraar, energieleverancier of verhuurder) aan de gemeente wordt verstrekt, met als doel de gemeente te informeren over een mogelijk beginnende schuldsituatie van een inwoner. Het vroegsignaal vormt het startpunt van het gemeentelijk proces van vroegsignalering van schulden. De juridische grondslag voor het ontvangen en verwerken van vroegsignalen is vastgelegd in artikel 2.2.1 van de Wet gemeentelijke schuldhulpverlening (Wgs). Deze wet verplicht gemeenten om vroegtijdig signalen van betalingsachterstanden te ontvangen en op basis daarvan inwoners passende hulp aan te bieden.

Attributen: crisissignaal, warmeOverdracht, bedrag, ontstaansdatum, signaaldatum, status.

GUID: `EAID_C6DA2586_C0E3_4868_93E8_64AF6D118092`

Relaties:

- betreft → Client (*Association*, 0..* → 1, `EAID_E8182EBD_8772_4d5f_96BF_423FD95F7F36`)
- verzondenDoor → Signaalpartner (*Association*, 0..* → 1, `EAID_5CCE8C02_FBA7_405f_A9F1_4DF3182B7437`)
- opgepaktIn → Vroegsignaalzaak (*Association*, 1..* → 0..1, `EAID_992CBE57_218F_42d1_8495_76BC51827E3A`)

## Vroegsignaalzaak

Een Vroegsignaalzaak is procesmatige eenheid binnen de gemeentelijke organisatie waarin de behandeling van één of meerdere vroegsigna(a)len is/zijn ondergebracht. De vroegsignaalzaak omvat alle handelingen die de gemeente verricht naar aanleiding van het ontvangen vroegsignaal, zoals het vastleggen van het signaal, het uitvoeren van een eerste beoordeling, het leggen van contact met de inwoner, het registreren van contactpogingen en -resultaten, en het eventueel toeleiden naar schuldhulpverlening of andere passende ondersteuning.

Attributen: resultaat, matchingsdatum, startdatum_matchtingperiode, datum_opgepakt, einddatum_matchingperiode.

GUID: `EAID_1AA67F0D_3B94_48a3_A037_A2ACC6D61CF0`

Relaties:

- heeft → Contactpoging (*Association*, 1 → 0..*, `EAID_614E37B8_40E2_4a6d_B8B9_1A4939BAE27E`)
- opgepaktNamens → Gemeente (*Association*, 0..* → 1, `EAID_3A702009_0E61_4756_AD68_959F192FA31A`)
- opgepaktDoor → NietNatuurlijkPersoon (*Association*, 0..* → 1, `EAID_EB0C17C7_84CB_4130_93A0_B58E06C70982`)
- → Zaak (*Generalization*,  → , `EAID_DAB43642_F4F5_4206_8968_5FA75E058FA8`)
