# EcedoERPCRMInterfaceApiProposalMeteringPoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | **string** | Profiel van de aansluiting | [optional] 
**cap_tar_code** | **string** | Capaciteitstariefcode (CapTar) van de aansluiting | [optional] 
**cap_tar_day_tariff** | **double** | Netbeheerkosten (per dag, excl. btw) dat door de netbeheerder in rekening wordt gebracht voor de aansluiting | [optional] 
**first_allowed_switch_date** | [**\DateTime**](\DateTime.md) | Wordt alleen gevuld wanneer de query paramater \&quot;includeCER\&quot; op \&quot;true\&quot; staat.  Aangezien het Contract Einde Register (CER) is tot onbekende datum offline is zal deze datum geen rekening houden met het huidige contract van de klant.  Geeft aan wat de eerstevolgende switchdatum is (rekening houdend met afkoelperiode, EDSN werkdagen, etc.). | [optional] 
**first_allowed_switch_date_message** | **string** | Wordt alleen gevuld wanneer de query paramater \&quot;includeCER\&quot; op \&quot;true\&quot; staat.  Uitleg van de berekening van de FirstAllowedSwitchDate. | [optional] 
**cer_notice_period** | **int** | Wordt alleen gevuld wanneer de query paramater \&quot;includeCER\&quot; op \&quot;true\&quot; staat.  Aangezien het Contract Einde Register (CER) is tot onbekende datum offline is zal dit veld altijd null zijn.  Opzegtermijn van het huidige contract van de klant. | [optional] 
**cer_end_date_contract** | [**\DateTime**](\DateTime.md) | Wordt alleen gevuld wanneer de query paramater \&quot;includeCER\&quot; op \&quot;true\&quot; staat.  Aangezien het Contract Einde Register (CER) is tot onbekende datum offline is zal dit veld altijd null zijn.  Einddatum van het huidige contract van de klant. | [optional] 
**physical_status** | **string** | Fysieke status van de aansluiting | [optional] 
**physical_status_localized** | **string** | Nederlandse vertaling van de fysieke status van de aansluiting | [optional] 
**pap_ean** | **string** | Indien aanwezig de EAN van het primaire allocatiepunt | [optional] 
**sap_eans** | **string** | Indien aanwezig een kommagescheiden lijst van secundaire allocatiepunt EANs | [optional] 
**annual_standard_usage** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAnnualStandardUsage**](EcedoERPCRMInterfaceApiAnnualStandardUsage.md) | Standaard Jaar Invoer (SJI) en Standaard Jaar Afname (SJA) van de aansluiting (zie het object-model voor meer informatie) | [optional] 
**meter** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeter**](EcedoERPCRMInterfaceApiMeter.md) | De gegevens van de meter van de aansluiting | [optional] 
**ean** | **string** | EAN van de aansluiting | [optional] 
**market_segment** | **string** | Het marktsegment (ook wel verbruikssegment genoemd) van de aansluiting | [optional] 
**market_segment_localized** | **string** | Nederlandse vertaling van het marktsegment | [optional] 
**usage_type** | **string** | Verbruikstype van de aansluiting | [optional] 
**usage_type_localized** | **string** | Nederlandse vertaling van het verbruikstype | [optional] 
**type_of_supply** | **string** | Leveringsrichting van de aansluiting | [optional] 
**type_of_supply_localized** | **string** | Nederlandse vertaling van de leveringsrichting | [optional] 
**grid_operator_ean** | **string** | EAN code van de netbeheerder die de aansluiting beheert | [optional] 
**grid_operator_localized** | **string** | De naam van de netbeheerder die de aansluiting beheert | [optional] 
**grid_area** | **string** | Het netgebied waarin de aansluiting zich bevindt (alleen gevuld bij elektriciteit-aansluitingen) | [optional] 
**gos** | **string** | De EAN van het Gas Ontvangst Station (GOS) (alleen gevuld bij gas-aansluitingen) | [optional] 
**gos_tariff** | **double** | Dit veld is niet langer van toepassingen sinds de komst van het postzegeltarief (NC-TAR) | [optional] 
**gos_region** | **int** | Dit veld is niet langer van toepassingen sinds de komst van het postzegeltarief (NC-TAR) | [optional] 
**gos_region_localized** | **string** | Dit veld is niet langer van toepassingen sinds de komst van het postzegeltarief (NC-TAR) | [optional] 
**address** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAddress**](EcedoERPCRMInterfaceApiAddress.md) | Het adres van de aansluiting (zie het object-model voor meer informatie) | [optional] 
**is_secondary_allocation_point** | **bool** | Geeft aan of de aansluiting een primair aansluitpunt heeft en daarmee dus zelf een secundair aansluitpunt is | [optional] 
**primary_allocation_point_ean** | **string** | De EAN van het eventueel aanwezige primaire aansluitpunt | [optional] 
**location_description** | **string** | Een optionele locatieomschrijving die de netbeheerder bij een aansluiting kan registreren | [optional] 
**is_art** | **bool** | Geeft aan of de aansluiting het marktsegment (UsageType) \&quot;Artikel 1 lid 2 of 3\&quot; heeft. Dit zijn kleinverbruikaansluitingen die behandeld moeten worden als grootverbruikaansluitingen.  Bij deze aansluitingen geeft Ecedo UsageType \&quot;LargeConsumer\&quot; terug en wordt deze boolean op \&quot;true\&quot; gezet om aan te geven dat het om een ART-aansluiting gaat. | [optional] 
**bag** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeteringPointBAG**](EcedoERPCRMInterfaceApiMeteringPointBAG.md) | Het object dat het BagId (een string) bevat. | [optional] 
**meter_number_tail** | **string** | De laatste 4 getallen van het meternummer. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


