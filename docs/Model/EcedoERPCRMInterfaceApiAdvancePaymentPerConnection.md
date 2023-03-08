# EcedoERPCRMInterfaceApiAdvancePaymentPerConnection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **string** |  | [optional] 
**market_segment** | **string** | Electricity / Gas. Dit veld is alleen gevuld wanneer de API is aangeroepen met query parameter includeConnectionDetails | [optional] 
**amount** | **double** | Het voorschotbedrag van deze aansluiting in euro&#39;s, inclusief btw | [optional] 
**calculated_amount** | **double** | Het berekende voorschotbedrag van deze aansluiting in euro&#39;s inclusief btw. Dit kan afwijken van het Amount als het voorschot met een AgreedAmount of TargetAmount is berekend | [optional] 
**agreed_amount** | **double** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


