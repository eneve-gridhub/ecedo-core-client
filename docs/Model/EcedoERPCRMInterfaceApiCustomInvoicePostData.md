# EcedoERPCRMInterfaceApiCustomInvoicePostData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debtor_id** | **string** | Optionele Guid waarmee gespecificeerd kan worden voor welke (contract)debiteur deze factuur moet worden aangemaakt. Als deze variabele niet wordt meegegeven wordt de hoofddebiteur van de klant gebruikt. | [optional] 
**financial_description** | **string** | De financiële omschrijving van de factuur. Dit is o.a. zichtbaar in de omschrijving van een automatische incasso. | [optional] 
**invoice_date** | [**\DateTime**](\DateTime.md) | Optionele factuurdatum. Als deze datum niet wordt meegegeven wordt automatisch vandaag gebruikt. | [optional] 
**payment_due_date** | [**\DateTime**](\DateTime.md) | Optionele vervaldatum van de factuur. Als deze niet wordt meegegeven wordt deze automatisch gebaseerd op de factuurdatum en de betaaltermijn van de klant. | [optional] 
**payment_method** | **string** | Optionele betaalmethode voor deze factuur. Als deze variabele niet wordt meegegeven wordt automatisch de betaalmethode van de debiteur geselecteerd. | [optional] 
**invoice_rows** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiCustomInvoiceRowPostData[]**](EcedoERPCRMInterfaceApiCustomInvoiceRowPostData.md) | Een lijst van factuurregels. Zie de specificatie van het het object voor meer informatie. | [optional] 
**invoice_sub_type** | **string** | Optioneel factuur-subtype. Als deze niet wordt meegegeven wordt de waarde &#x60;InvoiceSubTypes.Custom_General&#x60; gebruikt. Door een specifiek subtype te gebruiken kan afgeweken worden in bijvoorbeeld de factuur-opmaak. Alleen InvoiceSubTypes met prefix &#39;Custom_&#39; zijn toegestaan. | [optional] 
**client_reference** | **string** | Optioneel Eigen referentie naar deze factuur | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


