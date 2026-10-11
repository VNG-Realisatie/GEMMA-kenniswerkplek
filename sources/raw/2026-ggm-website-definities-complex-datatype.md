Complex datatype - Gemeentelijk Gegevensmodel (GGM)

Ga naar inhoud

# Complex datatype

## Inleiding

Definitie Complex datatype:

Geen definitie

Kenmerken Model Complex datatype

Kenmerk
Waarde

name
Complex datatype

toelichting

synoniemen

uri

bron

author
debat_e

version
1.0

created
2015-12-01 07:52:09

modified
2018-09-10 15:42:51

id
EAPK_EF3887BA_3215_4cd3_A6E0_18B0C850D4BE

Het model 'Complex datatype' kent de volgende objecttypen:

- BAGObjectnummering:

- CompositeID:

- TypeBedrag:

- TypeBreuk:

- TypeKadastraleAanduiding:

- TypeKoopsom:

- TypeLabel:

- TypeLabelpositie:

- TypeLandinrichtingsrente:

## Objecttypen Complex datatype

### BAGObjectnummering

Definitie BAGObjectnummering:

Geen Definitie

Kenmerken Model BAGObjectnummering

Eigenschap
Waarde

name
BAGObjectnummering

toelichting

synoniemen

uri

bron

author

version

created

modified

id
EAID_AB8B30D0_FD1F_4c44_9396_BB05389EA20B

domein_iv3

domein_dcat

gemma_naam

gemma_type

gemma_url

gemma_definitie

gemma_toelichting

Attributen van objecttype BAGObjectnummering

Attribute
Datatype
Description

gemeentecode
AN4
de (viercijferig) 'gemeentecode'

objecttypecode
typeObjectcode
Een code waarmee het objecttype van een object wordt
aangegeven.

objectvolgnummer
AN10
Een uniek volgnummer waarmee een object van een bepaald
objecttype binnen een gemeente kan worden aangeduid.

### CompositeID

Definitie CompositeID:

Geen Definitie

Kenmerken Model CompositeID

Eigenschap
Waarde

name
CompositeID

toelichting

synoniemen

uri

bron

author

version

created

modified

id
EAID_D0110970_3A90_451c_9EF3_ABD4AD5AA82A

domein_iv3

domein_dcat

gemma_naam

gemma_type

gemma_url

gemma_definitie

gemma_toelichting

Attributen van objecttype CompositeID

Attribute
Datatype
Description

Namspace
AN
Unieke verwijzing naar een domein binnen de Kadaster registratie van objecten

Lokaal id
AN
unieke identificatiecode binnen kadaster registratie

Versie
AN
Versie-aanduiding van een object.

### TypeBedrag

Definitie TypeBedrag:

Geen Definitie

Kenmerken Model TypeBedrag

Eigenschap
Waarde

name
TypeBedrag

toelichting

synoniemen

uri

bron

author

version

created

modified

id
EAID_510A0B01_75F9_430e_9FF1_99911FAA614E

domein_iv3

domein_dcat

gemma_naam

gemma_type

gemma_url

gemma_definitie

gemma_toelichting

Attributen van objecttype TypeBedrag

Attribute
Datatype
Description

som
2
Een hoeveelheid

valutasoort
Valutasoort
Aanduiding van de valutasoort.

### TypeBreuk

Definitie TypeBreuk:

Geen Definitie

Kenmerken Model TypeBreuk

Eigenschap
Waarde

name
TypeBreuk

toelichting

synoniemen

uri

bron

author

version

created

modified

id
EAID_02C9FDB1_0F08_4cd9_80FE_319F83C26757

domein_iv3

domein_dcat

gemma_naam

gemma_type

gemma_url

gemma_definitie

gemma_toelichting

Attributen van objecttype TypeBreuk

Attribute
Datatype
Description

teller
N8
Het aantal delen.

noemer
N8
De noemer van het deel

### TypeKadastraleAanduiding

Definitie TypeKadastraleAanduiding:

Geen Definitie

Kenmerken Model TypeKadastraleAanduiding

Eigenschap
Waarde

name
TypeKadastraleAanduiding

toelichting

synoniemen

uri

bron

author

version

created

modified

id
EAID_DB619B91_E690_49c0_88C0_733F37C0357B

domein_iv3

domein_dcat

gemma_naam

gemma_type

gemma_url

gemma_definitie

gemma_toelichting

Attributen van objecttype TypeKadastraleAanduiding

Attribute
Datatype
Description

kadastraleGemeentecode
AkrKadastraleGemeentecode
AKR code voor de kadastrale gemeente.

perceelnummer
N5
Het perceelnummer dat een geheel perceel of een complex uniek identificeert binnen de sectie.

sectie
AN2
De sectie die de sectie binnen de kadastrale gemeente uniek identificeert.

appartementsrechtvolgnummer
N4
Nummer dat het kadastraal object uniek identificeert als een appartementsrecht binnen het complex.

### TypeKoopsom

Definitie TypeKoopsom:

Geen Definitie

Kenmerken Model TypeKoopsom

Eigenschap
Waarde

name
TypeKoopsom

toelichting

synoniemen

uri

bron

author

version

created

modified

id
EAID_72D99BCE_F52F_4a19_90A6_5813DB40066B

domein_iv3

domein_dcat

gemma_naam

gemma_type

gemma_url

gemma_definitie

gemma_toelichting

Attributen van objecttype TypeKoopsom

Attribute
Datatype
Description

bedrag
TypeBedrag

koopjaar
JAAR
Het jaar waarin het belangrijkste recht van het kadastraal object is verkregen.

meerOnroerendGoed
INDIC
Indicatie of de koopsom betrekking heeft op meer dan 1 kadastraal object.

### TypeLabel

Definitie TypeLabel:

Geen Definitie

Kenmerken Model TypeLabel

Eigenschap
Waarde

name
TypeLabel

toelichting

synoniemen

uri

bron

author

version

created

modified

id
EAID_C74E1553_32AE_4fd8_9796_00C6E1C51A11

domein_iv3

domein_dcat

gemma_naam

gemma_type

gemma_url

gemma_definitie

gemma_toelichting

Attributen van objecttype TypeLabel

Attribute
Datatype
Description

labelTekst
AN
De tekst van het label zoals getoond op de kaart.

labelPositie
TypeLabelpositie
De locatie op de kaart waar het label moet worden getoond, samengesteld uit plaatsingspunt en rotatiehoek

### TypeLabelpositie

Definitie TypeLabelpositie:

Geen Definitie

Kenmerken Model TypeLabelpositie

Eigenschap
Waarde

name
TypeLabelpositie

toelichting

synoniemen

uri

bron

author

version

created

modified

id
EAID_5EEC2C27_B576_4f86_9768_5E785592FA4F

domein_iv3

domein_dcat

gemma_naam

gemma_type

gemma_url

gemma_definitie

gemma_toelichting

Attributen van objecttype TypeLabelpositie

Attribute
Datatype
Description

plaatsingspunt
Point
Coördinaten voor de locatie waar het label moet worden getoond.

hoek
1
De rotatie van het label bij visualisatie, met de klok mee ten opzichte
van de normale tekstrichting.

### TypeLandinrichtingsrente

Definitie TypeLandinrichtingsrente:

Geen Definitie

Kenmerken Model TypeLandinrichtingsrente

Eigenschap
Waarde

name
TypeLandinrichtingsrente

toelichting

synoniemen

uri

bron

author

version

created

modified

id
EAID_46A510E7_E757_4ad6_B697_DF79FE87F4F2

domein_iv3

domein_dcat

gemma_naam

gemma_type

gemma_url

gemma_definitie

gemma_toelichting

Attributen van objecttype TypeLandinrichtingsrente

Attribute
Datatype
Description

bedrag
TypeBedrag
Het bedrag waarmee de Onroerende zaak is belast in het kader van de landinrichtingswet.

eindjaar
JAAR

## Enumeraties Complex datatype

### typeObjectcode

Geen Definitie

Het enumeratie typeObjectcode kent de volgende waarden:

- verblijfsobject:

- ligplaats:

- standplaats:

- pand:

- nummeraanduiding:

- openbare ruimte:

- overig adreseerbaar object aanduiding:

- overig gebouwd object:

- overig benoemd terrein:

De enumeratie typeObjectcode heeft de volgende kenmerken:

Kenmerken Model typeObjectcode

Kenmerk
Waarde

name
typeObjectcode

toelichting

synoniemen

uri

bron

author

version
1.10.0

created
2025-03-26 11:13:41

modified
2025-12-16 10:28:45

id
EAID_e5611508_83dc_4fd6_8868_89303096e6be

domein_iv3

domein_dcat

gemma_naam

gemma_type

gemma_url

gemma_definitie

gemma_toelichting
