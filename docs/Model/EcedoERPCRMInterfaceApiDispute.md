# EcedoERPCRMInterfaceApiDispute

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disputed_meter_reading** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeterReading**](EcedoERPCRMInterfaceApiMeterReading.md) | De meterstanden waarover het dispuut gaat | [optional] 
**organization_event_id** | **string** | Het ID van de organisatie event | [optional] 
**proposed_meter_reading** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeterReading**](EcedoERPCRMInterfaceApiMeterReading.md) | De meterstanden die het volgens de aanvrager zouden moeten zijn | [optional] 
**organization_id** | **string** | Het unieke ID van deze klant | [optional] 
**connection_id** | **string** | Het unieke ID van de aansluiting | [optional] 
**dossier_id** | **string** | Het unieke ID van het dossier | [optional] 
**initiator_ean** | **string** | De EAN code van de partij die het dispuut heeft opgestart | [optional] 
**receiver_ean** | **string** | De EAN van de partij die het dispuut ontvangt | [optional] 
**result** | **string** | Geeft het resultaat aan van het dispuut | [optional] 
**result_localized** | **string** | Nederlandse vertaling van het resultaat | [optional] 
**dispute_date** | [**\DateTime**](\DateTime.md) | De datum van het dispuut | [optional] 
**request_comment** | **string** | De opmerking van de aanvrager van het dispuut | [optional] 
**response_comment** | **string** | De opmerking van het antwoord op het dispuut | [optional] 
**dispute_status_type** | **string** | Geeft de status aan van het dispuut | [optional] 
**dispute_status_type_localized** | **string** | Nederlandse vertaling van de status van het dispuut | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


