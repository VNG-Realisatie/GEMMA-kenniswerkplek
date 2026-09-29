---
title: "GEMMA: Bedrijfsobjecten, procesarchitectuur, zaakgericht werken en het GGM"
source: "https://www.gemmaonline.nl/wiki/Bedrijfsobjecten, https://www.gemmaonline.nl/wiki/GEMMA_en_het_Gemeentelijk_Gegevensmodel, https://www.gemmaonline.nl/wiki/Procesarchitectuur_kennismodel, https://www.gemmaonline.nl/wiki/Bedrijfsfuncties, https://www.gemmaonline.nl/wiki/Bedrijfsarchitectuur, https://www.gemmaonline.nl/wiki/Samenhang_PDC,_UPL,_zaaktypen_en_verwerkingsregister, https://www.gemmaonline.nl/wiki/Visie_op_zaakgericht_werken, https://www.gemmaonline.nl/wiki/Procesarchitectuur_Relatie_met_zaakgericht_werken"
author: "VNG Realisatie"
published:
created: 2026-06-18
description: "Geconsolideerde weergave van acht GEMMA-pagina's over bedrijfsobjecten, het GGM, procesarchitectuur, zaakgericht werken en de samenhang van PDC/UPL/ZTC."
tags:
  - "GEMMA"
---

# GEMMA: Bedrijfsobjecten, procesarchitectuur en het GGM

Geconsolideerde weergave van vijf pagina's op gemmaonline.nl, geraadpleegd op 2026-06-18.

---

## 1. Bedrijfsobjecten (gemmaonline.nl/wiki/Bedrijfsobjecten)

Bedrijfsobjecten zijn "concepten die binnen een bepaald domein worden gebruikt en betekenis hebben" (bijvoorbeeld 'paspoort' of 'uitkering'). Het GEMMA-bedrijfsobjectenmodel toont de belangrijkste gemeentelijke bedrijfsobjecten. Omdat data over objecten wordt geregistreerd, wordt het bedrijfsobjectenmodel ook wel een 'conceptueel gegevensmodel' genoemd. Het beschrijft grotere eenheden van gegevens in organisatiebreed herkenbare taal. Het is uitdrukkelijk geen logisch gegevensmodel en bevat geen beschrijving van de gewenste gegevensstructuur.

Bedrijfsobjecten zijn onafhankelijk van organisatorische en IT-inrichting en blijven bruikbaar over langere termijn. Het model wordt onder andere gebruikt voor:
- Organiseren van beheer, gebruik en bescherming van data per bedrijfsobject
- Vaststellen van eindverantwoordelijke voor datakwaliteit
- Identificeren van het "system of record"
- Bepalen van vereiste beschikbaarheid, integriteit en vertrouwelijkheidsniveaus (BBN)

> GEMMA had eerder een globaal bedrijfsobjectenmodel. Op basis van het door gemeenten gemaakte Gemeentelijk Gegevensmodel (GGM) is een nieuw, uitgebreider bedrijfsobjectenmodel gemaakt.

### Bedrijfsobjectmodellen per beleidsdomein

Het GGM maakt per beleidsdomein een of meer informatiemodellen. De beleidsdomeinen zijn gebaseerd op IV3-taakvelden, aangevuld met domeinen voor domeindoorsnijdende gegevensdefinities. GEMMA heeft per beleidsdomein één bedrijfsobjectmodel:

- 0 Bestuur, Politiek en Ondersteuning: Griffie
- 1 Veiligheid en Vergunningen
- 2 Verkeer, Vervoer en Waterstaat: Parkeren, Verkeer
- 3 Economie
- 4 Onderwijs: Leerplicht en Leerlingenvervoer, Onderwijs
- 5 Sport, Cultuur en Recreatie: Erfgoed (Archeologie, Archief, Generieke Entiteiten, Monumenten), Museum, Sport
- 6 Sociaal Domein: Gemeentebegrafenissen, Generiek Jeugd en Wmo, Inburgering (in ontwikkeling), Jeugdbescherming, Participatie, Schuldhulpverlening, Sociaal Domein Generiek (Inkomsten, Vermogen), Sociale Teams
- 7 Volksgezondheid en Milieu: Afval
- 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing: Beheer Openbare Ruimte, Bouwen en Wonen, Omgevingswet
- 9 Interne Organisatie: Financien, HR, ICT, Inkoop, Organisatie, Subsidies, Vastgoed
- 10 Dienstverlening
- 99 Kern: BAG, Dimensies, Generiek, RGBZ Model, RSGB Model, Referentielijsten

---

## 2. GEMMA en het Gemeentelijk Gegevensmodel (gemmaonline.nl/wiki/GEMMA_en_het_Gemeentelijk_Gegevensmodel)

*Laatst bewerkt: 13 december 2024*

VNG Realisatie werkt voor het GEMMA-model van bedrijfsobjecten samen met de gebruikersgroep van het GGM, waarin verschillende gemeenten en andere overheden zijn vertegenwoordigd.

Het GGM is een logisch gegevensmodel dat alle beleidsdomeinen omvat die onder de verantwoordelijkheid van de gemeente vallen. Het maakt het mogelijk om alle gegevens binnen gemeenten op een eenduidige manier te beschrijven. Het GGM is als open source beschikbaar en wordt onder andere gebruikt als datamodel voor het inrichten van datawarehouses.

### Positionering

Het GGM beschrijft, in ArchiMate-termen, **dataobjecten**: "samenhangende sets gegevens die geautomatiseerd kunnen worden verwerkt". De GEMMA beschrijft **bedrijfsobjecten**: "concepten die binnen een bepaald domein worden gebruikt en betekenis hebben". GEMMA's bedrijfsobjecten geven een meer conceptuele weergave (bedrijfsniveau), terwijl GGM's dataobjecten informatie vertalen naar een technischer niveau (applicatieniveau). Dataobjecten zijn te zien als de technische tegenhangers van bedrijfsobjecten.

**Om een consistente relatie tussen beide te borgen, leidt de GEMMA bedrijfsobjecten af van de GGM-dataobjecten.**

Bedrijfsobjecten zijn te relateren aan andere GEMMA-elementen in de bedrijfsarchitectuur:
- **Bedrijfsfuncties**: welke bedrijfsobjecten zijn van belang voor welke functies
- **Bedrijfsprocessen**: welke bedrijfsobjecten spelen een rol binnen welke processen

### Afspraken

- GGM-gebruikersgroep beheert de logische datamodellen (conform MIM)
- VNG Realisatie neemt deel aan de expertgroep GGM
- VNG beheert het GEMMA bedrijfsobjectenmodel
- Gezamenlijk beheer van het koppelvlak: CSV-koppeling (gereed), UML(MIM)–AMEFF (te besluiten)

### Koppeling

- GGM levert objecten en relaties in CSV-formaat (UML-attributen zijn geen onderdeel)
- VNG retourneert GEMMA-bedrijfsobjecten met vastgelegde definities in CSV-formaat
- VNG biedt het GGM ArchiMate-model aan in AMEFF-formaat

### Statistieken

- 507 bedrijfsobjecten (487 met definitie)
- 46 beleidsdomeinen, 40 bedrijfsobjectmodellen
- Indeling conform DCAT-DONL

### Vervolgstappen

- Gemeentelijke ontologie conform SKOS
- Relaties tussen bedrijfsobjecten en andere GEMMA-elementen (bedrijfsfuncties, referentiecomponenten)
- Aandachtspunt: dubbele begrippen in het GGM (bijv. 'Aanbesteding' in Inkoop én in Vastgoed)

---

## 3. Procesarchitectuur kennismodel (gemmaonline.nl/wiki/Procesarchitectuur_kennismodel)

Het kennismodel biedt inzicht in hoe gemeenten producten en diensten realiseren via bedrijfsprocessen en bedrijfsfuncties. Gebaseerd op ArchiMate.

### Uitgangspunten

- Producten en diensten worden gerealiseerd door bedrijfsprocessen
- Processen koppelen beleidsdomeinen aan bedrijfsfuncties en bedrijfsobjecten
- Bedrijfsprocessen zijn organisatie-onafhankelijke beschrijvingen
- Onderscheid: besturende, primaire en ondersteunende processen

### Elementen (24 concepten over twee lagen)

**Motivatielaag:** beleidskaders, visie, strategie, architectuurprincipes, kwaliteitsdoelen, kernwaarden, stakeholders

**Organisatielaag:** bedrijfsprocessen (op meerdere niveaus), functies, diensten, producten, bedrijfsobjecten, actoren, rollen, middelen, capabilities

### Proceshiërarchie

- Handeling: kleinste werkeenheid door één persoon/machine
- Processtap: geordende handelingen binnen één functie
- Deelproces: opeenvolgende stappen binnen organisatie-eenheid
- Bedrijfsproces: complete waardeketen
- Ketenproces: organisatieoverschrijdend

---

## 4. Bedrijfsfuncties (gemmaonline.nl/wiki/Bedrijfsfuncties)

Bedrijfsfuncties zijn "activiteiten die zijn gegroepeerd omdat daarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn." Ze beschrijven wat gemeenten doen, onafhankelijk van hoe het wordt uitgevoerd.

### Drie categorieën

**Besturende functies:** Sturing, Samenwerkingsvorming, Verantwoording, Strategie, Besturing

**Primaire functies:** Klant- en keteninteractie, Contactbeheer, Verstrekking, Ontvangst, Informering, Klantenservice, Samenwerking en participatie, Signaalverwerking, Zelfredzaamheidstimulering, Ontwikkeling, en domeinspecifieke functies (Sociaal, Fysieke leefomgeving, Openbare orde en veiligheid, Publieke dienstverlening)

**Ondersteunende functies:** Automatiseringsmanagement, Projectmanagement, Veiligheidsmanagement, Personeelsmanagement, Informatiseringsmanagement, Communicatiemanagement, Financieel management, en andere

---

## 5. Bedrijfsarchitectuur (gemmaonline.nl/wiki/Bedrijfsarchitectuur)

De GEMMA bedrijfsarchitectuur beschrijft de inrichting van organisatie, producten en processen. Definities:

- **Bedrijfsfunctie**: activiteiten gegroepeerd vanwege vergelijkbare bedrijfsmiddelen, kennis of competenties
- **Bedrijfsobject**: concept dat binnen een bepaald domein wordt gebruikt en betekenis heeft
- **Bedrijfsproces**: reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat

De bedrijfsarchitectuur wordt ondersteund door de informatiearchitectuur (applicaties en data).

---

## 6. Visie op zaakgericht werken (gemmaonline.nl/wiki/Visie_op_zaakgericht_werken)

Zaakgericht werken is "een benadering die zich richt op het gestructureerd en efficiënt afhandelen van processen, met de nadruk op individuele zaken."

### Definitie zaak

Een zaak is "een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden."

### Onderscheid met procesmatig werken

Zaakgericht werken verschilt van algemeen procesmatig werken op vier punten:
1. Elke zaak is een afzonderlijke uitvoering van een bedrijfsproces, standaard afgehandeld
2. Vergelijkbare zaken volgen identieke behandelprocedures
3. Alle informatie wordt gecentraliseerd in een gestandaardiseerd zaakdossier
4. Focus op procesessentiëlen, vereist competentie van medewerkers

### Zaakdossier

Het zaakdossier is een gestandaardiseerd informatieobject voor het vastleggen en ontsluiten van inhoudelijke en procesinformatie.

### Toepasbaarheid

Meest geschikt voor organisaties met een divers dienstenaanbod en gematigde volumes per dienst — eigenschappen die gemeenten typisch bezitten.

---

## 7. Procesarchitectuur: relatie met zaakgericht werken (gemmaonline.nl/wiki/Procesarchitectuur_Relatie_met_zaakgericht_werken)

De zaak is de **informatiecontainer** die de uitvoering van een bedrijfsproces begeleidt. Zaaktypen dienen als templates voor procesuitvoering.

### Vier kernpunten

1. **Procesgericht**: bouwt voort op end-to-end bedrijfsprocessen gericht op klantwaarde, van klantvraag tot dienstverlening
2. **Mijlpaalgestuurd**: stakeholders ontvangen updates bij procesmuslestenen (= zaakstatussen). Individuele processtappen worden niet in het zaaksysteem gedocumenteerd
3. **Gestandaardiseerd informatiebeheer**: alle procesinformatie vastgelegd in gestructureerd zaakdossier
4. **Zaaktypespecificaties**: vergelijkbare zaken volgen gestandaardiseerde zaaktypen met informatiestructuur, statussen, rollen, documentcategorieën en resultaten

### Procesmodel

Bedrijfsprocessen worden opgedeeld in deelprocessen. De afronding van elk deelproces markeert een statusovergang in de bijbehorende zaak. Meerdere zaaktypen kunnen corresponderen met hetzelfde bedrijfsproces — bijv. verschillende vergunningaanvragen volgen hetzelfde generieke behandelproces.

---

## 8. Samenhang PDC, UPL, zaaktypen en verwerkingsregister (gemmaonline.nl/wiki/Samenhang_PDC,_UPL,_zaaktypen_en_verwerkingsregister)

### Componenten

- **PDC (Producten- en Dienstencatalogus)**: publiekrechtelijke producten en diensten voor burgers en bedrijven, gepubliceerd op de gemeentelijke website
- **UPL (Uniforme Productnamenlijst)**: landelijke standaardlijst met namen voor publiekrechtelijke producten, met wettelijke grondslag per product. Beheerd door Logius (KOOP, min. BZK)
- **ZTC (Zaaktypecatalogus)**: bevat zaaktypen conform ImZTC — statussen, doorlooptijden, betrokkenen, dossiersamenstelling, resultaten. VNG Realisatie levert structuur, gemeenten vullen in
- **Verwerkingsregister**: AVG-verplichting, registreert verwerkingen van persoonsgegevens met doel, grondslag, categorieën betrokkenen, bewaartermijnen

### Wettelijke grondslag als verbindend element

De wettelijke grondslag verbindt UPL, verwerkingsregister en administratieve handelingen. Voorbeeld: "Omzetting geregistreerd partnerschap in huwelijk" verschijnt in alle drie op basis van art. 80g BW Boek 1.

### Relatie met GEMMA-procesmodel

Het aggregatieniveau van verwerkingsactiviteiten in het verwerkingsregister is vergelijkbaar met het niveau van deelprocessen in de GEMMA-procesarchitectuur. Gemeenten kunnen verwerkingen koppelen aan deelprocessen.

Proceshiërarchie:

| Niveau | Definitie | Voorbeeld |
|---|---|---|
| Bedrijfsproces | End-to-end, klant tot klant, onder verantwoordelijkheid van één organisatie | Behandel vergunningaanvraag |
| Deelproces | Onder verantwoordelijkheid van één bedrijfsfunctie, levert een deeldienst | Intake vergunningaanvraag |
| Processtap | Onder verantwoordelijkheid van één rol | Verstuur ontvangstbevestiging |
| Handeling | Kleinste werkeenheid, één persoon/machine | Opvragen adres bij basisregistratie |

### Visie ZTC

De ZTC-visie evolueert naar generieke zaaktypen (Aanvragen, Meldingen, Aangiften) in plaats van productspecifieke zaaktypen. Dit zou leiden tot een beperkt aantal standaard zaaktypen in plaats van honderden productgebonden types.

### Verbetervoorstellen (selectie)

- Koppel verwerkingsactiviteiten uit verwerkingsregister aan GEMMA-deelprocessen
- Breid GEMMA-bedrijfsarchitectuur uit waar verwerkingsactiviteiten niet aan processen gekoppeld kunnen worden
- Standaardiseer inhoud verwerkingsregister voor publiekrechtelijke taken
- Gebruik UPL als bron voor publiekrechtelijke verwerkingsactiviteiten
- Stel een informationmodel voor de PDC vast (ImPDC)
