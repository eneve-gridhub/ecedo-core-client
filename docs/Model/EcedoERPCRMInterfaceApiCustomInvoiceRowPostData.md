# EcedoERPCRMInterfaceApiCustomInvoiceRowPostData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_price_component_id** | **string** | Het Id van de CustomPriceComponent waarvoor de factuurregel aangemaakt moet worden. Deze &#x60;CustomPriceComponentId&#x60; kunnen opgevraagd worden uit de CustomPriceComponent-API. | [optional] 
**custom_price_component_invoice_row_description** | **string** | Met dit optionele veld kan de standaard omschrijving vastgelegd bij het handmatige prijscomponent overruled worden. De omschrijving wordt de omschrijving van de factuurregel op de factuur.  Het veld mag geen lege string bevatten. | [optional] 
**factor** | **double** | Een optionele factor (percentage) voor de factuurregel | [optional] 
**start_date** | [**\DateTime**](\DateTime.md) | De startdatum (vanaf-datum) voor de periode waarop de factuurregel van toepassing is | [optional] 
**end_date** | [**\DateTime**](\DateTime.md) | De einddatum (tot-datum) voor de periode waarop de factuurregel van toepassing is | [optional] 
**product_id** | **string** | Het product waar de factuurregel aan toebehoort. | [optional] 
**usage** | **int** | De verbruikseenheid van deze factuurregel. | [optional] 
**price** | **double** | De prijs per eenheid van deze factuurregel. Dit mag bijvoorbeeld 1 zijn als een klant 1 laadpaal heeft gekocht. | [optional] 
**price_unit** | **string** | De eenheid van de prijs. | [optional] 
**amount** | **double** | Het bedrag van deze factuurregel. | [optional] 
**vat_inclusive** | **bool** | Deze variabele geeft aan of het bedrag van de factuurregel inclusief of exclusief btw is. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


