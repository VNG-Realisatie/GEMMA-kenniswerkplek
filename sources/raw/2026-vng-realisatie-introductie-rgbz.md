---
title: "Introductie RGBZ"
source: "https://vng-realisatie.github.io/RGBZ/"
author: "VNG Realisatie"
published:
created: 2026-06-18
description: "Introductiepagina RGBZ: status, totstandkoming, relatie tot RGBZ 2.0, ZGW API's en berichtenarchitectuur (StUF-ZKN, Zaak- en Documentservices)."
tags:
  - "Dienstverlening"
  - "Standaarden"
  - "GEMMA"
---
Het Referentiemodel Gemeentelijke Basisgegevens Zaken (RGBZ) specificeert de gegevens en hun samenhang die gemeenten, daarmee samenwerkende organisaties en hun klanten minimaal nodig hebben om voldoende op de hoogte te zijn van lopende en afgeronde zaken. Het informatiemodel is gericht op:

- het adequaat kunnen informeren van betrokkenen bij, en geïnteresseerden in een zaak. Dit loopt van ex- en interne initiatoren van een zaak via medebehandelaars
- daarvan en belangstellenden in de publicatie van de zaak of het resultaat daarvan tot management dat behoefte heeft aan sturingsinformatie.
- het (ook achteraf) kunnen verantwoorden van de zaak, zowel inhoudelijk (is de zaak goed afgehandeld) als qua proces (is de zaak op de juiste wijze afgehandeld),
- en desgewenst kunnen reconstrueren van de (behandeling van de) zaak.

Het informatiemodel draagt bij aan:

- het verbeteren van de dienstverlening aan de burger,
- het ondersteunen van elektronische dienstverlening,
- het verbeteren van de bedrijfsvoering van de gemeente,
- het adequater beheren van de, steeds meer digitale, documentaire informatievoorziening en archivering.

## Status

De actuele versie van het RGBZ is versie 1.0 (‘in gebruik’). Dat is ook de versie die is geïmplementeerd in [StUF-ZKN 3.10](https://vng-realisatie.github.io/StUF-ZKN/). Het RGBZ is één van de informatiemodellen op het gebied van zaakgericht werken (naast het informatiemodel voor de Zaaktypecatalogus) en één van de standaarden van de Gegevens- en berichtenarchitectuur.

Er bestaat ook een RGBZ versie 2.0, echter deze heeft nooit een officiële status bereikt. Deze concept-versie is ook opgenomen in de [documentatie](https://vng-realisatie.github.io/RGBZ/documentatie). Sommige van de nieuwe concepten die zijn geïntroduceerd in RGBZ 2.0 zijn overgenomen in de ZGW API’s die op hun beurt wel weer een officiële status hebben.

## Totstandkoming RGBZ

In 2004 heeft de Vereniging van Nederlandse Gemeenten (VNG) het Gemeentelijk Functioneel Ontwerp Zaken uitgebracht. Hiermee werd een standaard gezet voor de centrale beschikbaarheid van basis- en kerngegevens over een zaak en het centraal kunnen ontsluiten van een zaak. Vanwege de opkomst van basisregistratie en het uitbrengen, in 2007 door EGEM i-teams, van versie 1.0 van het [Referentiemodel Stelsel van Gemeentelijke Basisgegevens (RSGB)](https://vng-realisatie.github.io/RSGB/), ontstond de behoefte om het GFO Zaken en het RSGB te verbinden. Dit is in de periode december 2007 – maart 2009 gerealiseerd in een werkgroep met gemeentelijke ervaringsdeskundigen onder leiding van EGEM i-teams. Het heeft tevens geleid tot een actualisatie van het GFO Zaken met als belangrijkste toevoeging het ‘document’, Het resultaat is versie 1.0 van het Referentiemodel Gemeentelijke Basisgegevens Zaken, kortweg het RGB Zaken, afgekort: RGBZ, dat het GFO Zaken vervangt. Het is, op voordracht van VNG Realisatie, in september 2010 vastgesteld door de Regiegroep Gegevens- en berichtenstandaarden.

## Berichtenarchitectuur

Het RGBZ beschrijft de structuur en semantiek van (uit te wisselen) gegevens over zaken en documenten. Om deze gegevens daadwerkelijk uit te kunnen wisselen, zijn berichten nodig. Hiertoe is het RGBZ allereerst uitgewerkt in de [berichtenstandaard Sectormodel Zaken (StUF-ZKN 3.10)](https://vng-realisatie.github.io/StUF-ZKN/). Voor specifieke en veelvoorkomende gebeurtenissen binnen het zaakgericht werken en het documentmanagement zijn hiervan specifieke berichten afgeleid onder de noemer [Zaak- en Documentservices](https://vng-realisatie.github.io/Zaak-en-Documentservices/). Zaak- en documentgegevens zijn tevens opgenomen in [andere koppelvlakken](https://vng-realisatie.github.io/Standaarden/Zaken-en-documenten).