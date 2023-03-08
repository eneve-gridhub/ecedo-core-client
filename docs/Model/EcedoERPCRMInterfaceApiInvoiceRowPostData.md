# EcedoERPCRMInterfaceApiInvoiceRowPostData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_component_type** | **string** | Het type prijscomponent. | [optional] 
**custom_price_component_id** | **string** | Het Id van de CustomPriceComponent waarvoor de factuurregel aangemaakt moet worden. Deze &#x60;CustomPriceComponentId&#x60;s kunnen opgevraagd worden via de CustomPriceComponent-API. | [optional] 
**contract_id** | **string** | Het contract waar de factuurregel bij hoort. Voor voorschotfacturen is dit veld verplicht. | [optional] 
**start_date** | [**\DateTime**](\DateTime.md) | De startdatum van de factuurregel. | [optional] 
**end_date** | [**\DateTime**](\DateTime.md) | De einddatum van de factuurregel. | [optional] 
**product_id** | **string** | Het product waar de factuurregel aan toebehoort. | [optional] 
**usage** | **int** | De verbruikseenheid van deze factuurregel. | [optional] 
**price** | **double** | De prijs per eenheid van deze factuurregel. Dit mag bijvoorbeeld 1 zijn als een klant 1 laadpaal heeft gekocht. | [optional] 
**price_unit** | **string** | De eenheid van de prijs. | [optional] 
**amount** | **double** | Het bedrag van deze factuurregel. | [optional] 
**vat_inclusive** | **bool** | Deze variabele geeft aan of het bedrag van de factuurregel inclusief of exclusief btw is. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


