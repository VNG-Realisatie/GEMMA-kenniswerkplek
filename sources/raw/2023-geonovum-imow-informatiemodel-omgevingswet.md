---
title: "Informatiemodel Omgevingswet (IMOW) v3.0.1"
source: "https://docs.geostandaarden.nl/ow/def-im-imow-20231227/"
author: "Geonovum (TPOD-team)"
published: 2023-12-27
created: 2026-06-27
description: "Informatiemodel voor aantekeningen bij omgevingsbesluiten in het DSO — objecttypen, attributen en relaties voor Juridische Regel, Activiteit, Gebiedsaanwijzing, Omgevingsnorm, Omgevingswaarde, Locatie"
tags:
  - "Omgevingswet"
---

# Informatiemodel Omgevingswet (IMOW) - Versie 3.0.1

**Versie:** 3.0.1
**Datum:** 27 december 2023
**Redacteur:** TPOD-team (Geonovum)
**Licentie:** Creative Commons Naamsvermelding-GeenAfgeleideWerken 4.0 Internationaal

## Doel en Scope

Het IMOW beschrijft hoe aantekeningen bij omgevingsbesluiten dienen te worden aangeleverd. Dit informatiemodel specificeert de implementatie van concepten uit het CIM-OW (Conceptueel Informatiemodel Omgevingswet) en bepaalt welke objecten aan het Digitaal Stelsel Omgevingswet (DSO) kunnen worden aangeboden.

Het IMOW zorgt ervoor dat omgevingsinformatie "beter verwerkt en op een kaart getoond kan worden in het DSO" door tekstonderdelen van regelingen te voorzien van machine-leesbare aantekeningen.

## Contextuele Standaarden

Het IMOW werkt samen met:

- **STOP** (Standaard Officiële Publicaties): beschrijft documentstructuur en metadata
- **LVBB bronhouderkoppelvlak**: schrijft bestandsstructuur voor aanlevering voor
- **TPOD's** (Toepassingsprofielen omgevingsdocumenten): specifieke regels per documenttype
- **Basisgeometrie**: standaard voor GML/geometrieën (versie 30 september 2020)

## Kernobjecten en Objecttypen

### OW-Object (Supertype)

Alle in het IMOW aangeleverde objecttypen erven af van OWobject. Gemeenschappelijke attributen:

- **identificatie** (verplicht): unieke identificatie volgens NEN3610-standaard
- **status** (optioneel): leeg voor actief; 'B' voor beëindigd
- **procedurestatus** (optioneel): leeg voor vastgesteld; 'ontwerp' voor ontwerpbesluiten

### OP-Object (Subtype van OW-Object)

OW-objecten met directe verwijzing naar STOP-tekstelementen via:
- **wId**: identificatie van artikel/lid/divisie in STOP
- **wIdRegeling**: identificatie van de regeling in STOP

Subtypes: Regeltekst, Divisie, Divisietekst

## Artikelsgewijze Structuur - Objecttypen

### Regeltekst

Vormt de verbinding tussen STOP-artikelen/leden en OW-juridische regels.

**Attributen:**
- wId (verplicht): artikel/lid-identificatie uit STOP
- identificatie (verplicht): NEN3610-identificatie van het Regeltekst-object

### Juridische Regel (Abstract Objecttype)

Drie concrete subtypes om verschillende regelsoorten te duiden:

#### RegelVoorIedereen
Regel die voor alle personen/organisaties geldt.

**Attributen:**
- identificatie (verplicht): NEN3610
- idealisatie (verplicht): uit waardelijst 'idealisatie'
- artikelOfLid (verplicht): referentie naar Regeltekst
- thema (optioneel, meervoudig): waarden uit 'Thema'

**Relaties:**
- locatieaanduiding (verplicht): verwijzing naar Locatie(s)
- gebiedsaanwijzing (optioneel): verwijzing naar Gebiedsaanwijzing(en)
- kaartaanduiding (optioneel): verwijzing naar Kaart(en)
- activiteitaanduiding (optioneel, meervoudig): verwijzing naar Activiteit
- omgevingsnormaanduiding (optioneel, meervoudig): verwijzing naar Omgevingsnorm(en)

Elke activiteitaanduiding bij RegelVoorIedereen moet vergezeld gaan van een **ActiviteitLocatieaanduiding** met:
- identificatie (verplicht): unieke NEN3610-id per activiteit/regel-combinatie
- activiteitregelkwalificatie (verplicht): uit waardelijst
- Locatieaanduiding (verplicht): de gekwalificeerde locatie

#### Instructieregel
Regel gericht op ander bevoegd gezag.

**Attributen:**
- identificatie (verplicht)
- idealisatie (verplicht)
- artikelOfLid (verplicht)
- instructieregelInstrument (optioneel): uit waardelijst 'instrument'
- instructieregelTaakuitoefening (optioneel): uit waardelijst 'adressaat'

Opmerking: instrument en taakuitoefening mogen niet beide in dezelfde regel voorkomen.

**Relaties:**
- locatieaanduiding (verplicht)
- gebiedsaanwijzing (optioneel)
- kaartaanduiding (optioneel)
- omgevingsnormaanduiding (optioneel)

#### Omgevingswaarderegel
Regel van het eigen bevoegd gezag.

**Attributen:**
- identificatie (verplicht)
- idealisatie (verplicht)
- artikelOfLid (verplicht)

**Relaties:**
- locatieaanduiding (verplicht)
- gebiedsaanwijzing (optioneel)
- kaartaanduiding (optioneel)
- omgevingswaardeaanduiding (optioneel): verwijzing naar Omgevingswaarde(n)

### Activiteit

Representeert menselijk handelen/nalaten dat in de regeling wordt gereguleerd en gevolgen heeft voor de fysieke leefomgeving.

**Attributen:**
- identificatie (verplicht): NEN3610
- naam (verplicht): hoe de activiteit heet
- groep (verplicht): uit waardelijst 'Activiteitengroep'

**Relaties:**
- gerelateerdeActiviteit (optioneel): verwijzing naar gerelateerde Activiteiten
- bovenliggendeActiviteit (verplicht): hiërarchische positie in functionele structuur

**Regelgeving voor tophaak-activiteiten:**
Elke regeling (behalve AMvB/ministeriële regeling) met Activiteiten moet een tophaak-activiteit bevatten. Voor omgevingsplan: naam moet zijn "Activiteit gereguleerd in het omgevingsplan gemeente [naam]". Deze tophaak moet verwijzen naar "Activiteit gereguleerd in het omgevingsplan" uit Placeholder-Regeling.

### Gebiedsaanwijzing

Aanwijzing van een specifiek gebied met beleid/bestemming.

**Attributen:**
- identificatie (verplicht): NEN3610
- type (verplicht): uit waardelijst 'TypeGebiedsaanwijzing'
- naam (verplicht): naam van het aangewezen gebied
- groep (verplicht): uit waardelijst 'gebiedsaanwijzinggroep' (afhankelijk van type)

**Relaties:**
- locatieaanduiding (verplicht): verwijzing naar Locatie(s)

### Omgevingsnorm

Vastlegging van normwaarden als referentiepunt voor handelen in de fysieke leefomgeving.

**Attributen:**
- identificatie (verplicht): NEN3610
- naam (verplicht): benaming door bevoegd gezag
- type (verplicht): uit waardelijst 'TypeNorm'
- eenheid (optioneel): uit waardelijst 'Eenheid' (alleen bij kwantitatieve waarden)
- groep (verplicht): uit waardelijst 'Omgevingsnormgroep'

**Normwaarde-element (meervoudig, verplicht):**
- identificatie (verplicht): NEN3610
- kwantitatieveWaarde (optioneel): numerieke waarde
- kwalitatieveWaarde (optioneel): tekstuele waarde
- waardeInRegeltekst (optioneel): indien waarde in artikel/lid staat
- locatieaanduiding (verplicht): verwijzing naar Locatie(s) waar normwaarde geldt

### Omgevingswaarde

Vastlegging van gewenste staat of kwaliteit van de fysieke leefomgeving als beleidsdoel.

**Attributen:**
- identificatie (verplicht): NEN3610
- naam (verplicht)
- type (verplicht): uit waardelijst 'TypeNorm'
- eenheid (optioneel): uit waardelijst 'Eenheid'
- groep (verplicht): uit waardelijst 'Omgevingswaardegroep'

**Normwaarde-element (identiek aan Omgevingsnorm)**

## Vrijetekststructuur - Objecttypen

### Divisie

Koppeling naar divisie-elementen in STOP (hoofdstukken, paragrafen).

**Attributen:**
- wId (verplicht): divisie-identificatie uit STOP
- identificatie (verplicht): NEN3610

### Divisietekst

Koppeling naar divisietekst-elementen in STOP.

**Attributen:**
- wId (verplicht)
- identificatie (verplicht): NEN3610

### Tekstdeel

Container voor aantekeningen op specifieke tekstfragmenten.

**Attributen:**
- identificatie (verplicht): NEN3610
- idealisatie (optioneel): uit waardelijst 'idealisatie'
- thema (optioneel, meervoudig): uit waardelijst 'Thema'

**Relaties:**
- divisieaanduiding (verplicht): verwijzing naar Divisie of Divisietekst
- hoofdlijnaanduiding (optioneel): verwijzing naar Hoofdlijn(en)
- kaartaanduiding (optioneel): verwijzing naar Kaart(en)
- locatieaanduiding (optioneel): verwijzing naar Locatie(s)
- gebiedsaanwijzing (optioneel): verwijzing naar Gebiedsaanwijzing(en)

### Hoofdlijn

Vrij in te vullen object voor beleidsonderdelen in vrijetekststructuur.

**Attributen:**
- identificatie (verplicht): NEN3610
- naam (verplicht): naam gegeven door bevoegd gezag
- soort (verplicht): zelf bepaald type (bijv. "ambitie", "perspectief")

**Relaties:**
- gerelateerdeHoofdlijn (optioneel): verwijzing naar andere Hoofdlijnen

## Locatie-Objecttypen

Locaties modelleren geografische toepassingsgebieden van OW-objecten.

### Groepen (Gebiedengroep, Lijnengroep, Puntengroep)

Collectie van individuele locaties.

**Attributen:**
- identificatie (verplicht): NEN3610
- noemer (optioneel): naam van de groep in regel

**Relaties:**
- groepselement (verplicht): verwijzingen naar Gebied/Lijn/Puntobjecten

### Individuele Locaties (Gebied, Lijn, Punt)

Geometrische locaties op kaart.

**Attributen:**
- identificatie (verplicht): NEN3610
- noemer (optioneel): mensleesbare naamkoppeling aan GIO
- hoogte (optioneel): voor hoogte-gerelateerde informatie

**Relaties:**
- geometrie (verplicht): verwijzing naar Geometrie-object (UUID)

### Ambtsgebied

Bijzondere locatie die samenvalt met ambtsgebied van bevoegd gezag.

**Attributen:**
- identificatie (verplicht): NEN3610
- noemer (optioneel)
- bestuurlijkeGrenzenID (verplicht): verwijzing naar bestuurlijkeGrenzen-voorziening
- Domein (verplicht): altijd 'NL.BI.BestuurlijkGebied'
- geldigOp (verplicht): datum waarop ambtsgebied geldig was

## Geometrie

Verwijzing naar coördinaten in GML-bestand.

**Attributen:**
- id (verplicht): UUID
- geometrie: GML-inhoud (Polygon, LineString, Point of samengesteld)

**Coördinaatsystemen:**
- RD (2D): srsName="urn:ogc:def:crs:EPSG::28992"
- ETRS89 (2D): srsName="urn:ogc:def:crs:EPSG::4258"

## Kaart en Kaartlaag

### Kaart

Object voor definiëren en naamgeven van kaarten.

**Attributen:**
- identificatie (verplicht): NEN3610
- naam (verplicht)
- nummer (optioneel)
- uitsnede/Kaartextent (verplicht): minX, minY, maxX, maxY

**Relaties:**
- kaartlagen (verplicht, meervoudig): Kaartlaag-objecten

### Kaartlaag

Onderdeel van kaart met specifieke inhoud.

**Attributen:**
- identificatie (verplicht): NEN3610
- naam (optioneel)
- niveau (verplicht): stapelvolgorde (1 = onderst)

**Relaties:**
- activiteitlocatieweergave (optioneel): ActiviteitLocatieaanduiding(en)
- normweergave (optioneel): Omgevingsnorm/Omgevingswaarde
- Gebiedsaanwijzingweergave (optioneel): Gebiedsaanwijzing(en)

## Overige Objecttypen

### Pons

Duidde gebied waar bestemmingsplannen niet meer hoeven te worden getoond (alleen omgevingsplan). Maximaal één per regeling; nooit in tijdelijk regelingdeel.

### Regelingsgebied

Het totale werkingsgebied van een regeling.

### SymbolisatieItem

Aangepaste symbolisatie voor kaartweergave.

## Identificatieregels

Alle identificaties volgen NEN3610-standaard met patroon:

```
nl.imow-(gm|pv|ws|mn|mnre)[0-9]{1,6}.(objecttype).[A-Za-z0-9]{1,32}
```

**Voorbeelden:**
- `nl.imow-gm0200.gebied.2019000001`
- `nl.imow-pv27.activiteit.WONEN001`

## Verplichte Attributen per Objecttype

| Objecttype | Verplichte Attributen |
|---|---|
| Regeltekst | wId, identificatie |
| RegelVoorIedereen | identificatie, idealisatie, artikelOfLid, locatieaanduiding |
| Instructieregel | identificatie, idealisatie, artikelOfLid, locatieaanduiding |
| Omgevingswaarderegel | identificatie, idealisatie, artikelOfLid, locatieaanduiding |
| Activiteit | identificatie, naam, groep, bovenliggendeActiviteit |
| Gebiedsaanwijzing | identificatie, type, naam, groep, locatieaanduiding |
| Omgevingsnorm | identificatie, naam, type, groep, normwaarde |
| Omgevingswaarde | identificatie, naam, type, groep, normwaarde |
| Locatie-groepen | identificatie |
| Gebied/Lijn/Punt | identificatie, geometrie |
| Ambtsgebied | identificatie, bestuurlijkeGrenzenID, Domein, geldigOp |
| Kaart | identificatie, naam, uitsnede, kaartlagen |
| Kaartlaag | identificatie, niveau |
| Regelingsgebied | identificatie, locatieaanduiding |

## Sleutelverhoudingen en Restricties

- Geen kruisverwijzingen tussen bevoegde gezagen (behalve tophaak-activiteiten)
- Geen verwijzingen naar beëindigde objecten door actieve objecten
- Status 'B' beëindigt objecten expliciet
- Procedurestatus 'ontwerp' voor ontwerpbesluiten (niet muteren)
- ActiviteitLocatieaanduiding, Normwaarde, Kaartlaag zijn geen zelfstandige objecten (wijzigen via parent)
- Geometrie kan niet zelfstandig gemuteerd worden
