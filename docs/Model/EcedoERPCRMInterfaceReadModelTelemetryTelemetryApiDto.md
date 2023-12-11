# EcedoERPCRMInterfaceReadModelTelemetryTelemetryApiDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **double** | Tot 01-04-2023 werden verbruiken voor elektriciteit-aansluitingen gesaldeerd in alle marktprocessen. Er waren geen losse waarden voor LDN en ODN, maar alleen deze Value. Om backwards compatible te blijven is dit value-veld behouden en bevat deze een on-the-fly gesaldeerd volume van ValueLDN en ValueODN. Deze waarde is negatief bij teruglevering (ODN) en positief bij verbruik (LDN). | [optional] 
**value_ldn** | **double** | Het volume dat geleverd is door de netbeheerder (dus verbruik vanuit het perspectief van een aansluiting). Deze is 0 wanneer er geen verbruik is bij zowel gas- als elektriciteit-aansluitingen | [optional] 
**value_odn** | **double** | Het volume dat ontvangen is door de netbeheerder (dus teruglevering vanuit het perspectief van een aansluiting). Deze is 0 wanneer er geen teruglevering is bij een elektriciteit-aansluiting en &#x60;null&#x60; bij gas-aansluitingen. | [optional] 
**telemetry_id** | **string** |  | [optional] 
**connection_id** | **string** |  | [optional] 
**ean** | **string** |  | [optional] 
**start_date** | [**\DateTime**](\DateTime.md) |  | [optional] 
**end_date** | [**\DateTime**](\DateTime.md) |  | [optional] 
**unit** | **string** |  | [optional] 
**unit_localized** | **string** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


