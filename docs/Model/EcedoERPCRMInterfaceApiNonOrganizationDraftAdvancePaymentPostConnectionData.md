# EcedoERPCRMInterfaceApiNonOrganizationDraftAdvancePaymentPostConnectionData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_segment** | **string** | Het marktsegment (ook wel productsoort genoemd) van de aansluiting. Dit is in alle gevallen een verplicht veld. | [optional] 
**ean** | **string** | De EAN code van de aansluiting. Dit is in alle gevallen een verplicht veld. | [optional] 
**agreement_date** | [**\DateTime**](\DateTime.md) | De tekendatum van het contract. Deze tekendatum wordt gebruikt om te valideren of de propositie(s) geldig waren op het moment van tekenen. Dit is een verplicht veld wanneer de &#x60;AgreementDate&#x60; in het bovenliggende object niet gebruikt wordt. | [optional] 
**proposition_reference** | **string** | De referentie van de energielevering-propositie. Deze wordt alleen gebruikt en is verplicht wanneer &#x60;PropositionId&#x60; niet wordt gebruikt. | [optional] 
**proposition_id** | **string** | Het unieke Id van de energielevering-propositie. Dit veld is verplicht wanneer &#x60;PropositionReference&#x60; niet wordt gebruikt. | [optional] 
**meelift_proposition_reference** | **string** | De referentie van de meelift-propositie. Of dit veld gebruikt moet worden is afhankelijk van de configuratie van de omgeving. Deze waarde wordt alleen gebruikt en is verplicht wanneer &#x60;MeeliftPropositionId&#x60; niet wordt gebruikt. | [optional] 
**meelift_proposition_id** | **string** | Het unieke Id van de meelift-propositie. Of dit veld gebruikt moet worden is afhankelijk van de configuratie van de omgeving. Dit veld is verplicht wanneer &#x60;MeeliftPropositionReference&#x60; niet wordt gebruikt. | [optional] 
**annual_standard_usage** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAnnualStandardUsage**](EcedoERPCRMInterfaceApiAnnualStandardUsage.md) | Het verbruik van de aansluiting. Zie de objectspecificatie voor meer informatie. Dit is in alle gevallen een verplicht veld. | [optional] 
**billing_items** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiDraftBillingItem[]**](EcedoERPCRMInterfaceApiDraftBillingItem.md) | Optionele lijst van factuuritems. Zie de groep \&quot;SysBillingItems\&quot; in de Swagger specificatie voor meer informatie. | [optional] 
**contract_prices** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiPriceGroupPostData[]**](EcedoERPCRMInterfaceApiPriceGroupPostData.md) | Een optionele lijst van contractprijzen waarmee de propositieprijzen aangevuld of overschreven kunnen worden. | [optional] 
**is_residential** | **bool** | Geeft aan of de aansluiting een verblijfsfunctie heeft. Dit is een verplicht veld bij elektriciteit-aansluitingen. | [optional] 
**usage_type** | **string** | Het verbruikstype (ook wel Verbruikssegment genoemd) van de aansluiting, waarmee wordt aangegeven of de aansluiting in het grootverbruik- of kleinverbruiksegment valt. Deze waarde wordt automatisch opgevraagd uit het C-AR en hoeft doordoor vrijwel nooit expliciet meegegeven te worden. Als deze waarde wordt meegegeven wordt de waarde uit het C-AR overschreven. | [optional] 
**profile** | **string** | Het profiel van de aansluiting, bijvoorbeeld &#x60;E2B&#x60; of &#x60;G1A&#x60;. Bij elektriciteit-aansluitingen is het van belang dat het profiel overeenkomst met het verbruik (&#x60;AnnualStandardUsage&#x60;). Door de uitschakeling van het TF-signaal converteert Ecedo automatisch dubbele SJV&#39;s naar een enkele SJV&#39;s als dat nodig is voor het profiel dat wordt ingestuurd. A-profielen (bijv. E1A) hebben enkel verbruik, B- en C-Profielen hebben dubbel verbruik. | [optional] 
**cap_tar_code** | **string** | Volledige EAN code voor het capaciteitstarief. Bijvoorbeeld &#x60;8742010102115&#x60; of &#x60;8742090202118&#x60;. Dit is een veld voor kleinverbruikaansluitingen wanneer &#x60;CapTarCodeShort&#x60; niet wordt gebruikt. | [optional] 
**cap_tar_code_short** | **string** | Korte versie van de code voor het capaciteitstarief zodat het niet langer nodig is om een geldige EAN te gebruiken. Bijvoorbeeld &#x60;E10211&#x60; of &#x60;G20211&#x60;. Dit is een veld voor kleinverbruikaansluitingen wanneer &#x60;CapTarCode&#x60; niet wordt gebruikt. | [optional] 
**supplier_ean** | **string** | Optioneel veld waarmee aangegeven kan worden namens welke marktpartij EAN de callbacks naar EDSN (het C-AR) uitgevoerd moeten worden. Dit is alleen van toepassing op omgevingen waarbij meerdere marktpartij EANs geconfigureerd zijn. | [optional] 
**location_type** | **string** | Optioneel locatietype van de aansluiting. Locatietypes kunnen invloed hebben op de energiebelasting die in rekening gebracht wordt. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


