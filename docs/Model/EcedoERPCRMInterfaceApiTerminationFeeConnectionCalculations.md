# EcedoERPCRMInterfaceApiTerminationFeeConnectionCalculations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **string** | Het id van de aansluiting. | [optional] 
**termination_fees** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiCalculatedTerminationFee[]**](EcedoERPCRMInterfaceApiCalculatedTerminationFee.md) | Een lijst van alle berekende opzegvergoedingen die bij de aansluiting horen. | [optional] 
**termination_fee_amount** | **double** | Het totaal (de som) van de berekende opzegvergoedingen. Deze som is exclusief btw. | [optional] 
**termination_fee_vat_amount** | **double** | Het totaal (de som) van de berekende BTW van de opzegvergoedingen. | [optional] 
**termination_fee_total_amount** | **double** | Het totaal (de som) van de berekende opzegvergoedingen. Deze som is inclusief btw. | [optional] 
**termination_date** | [**\DateTime**](\DateTime.md) | De opzegdatum die gebruikt is in de berekening. | [optional] 
**has_termination_fee** | **bool** | Of er een opzegvergoeding betaald moet worden. Dus er is ten minste één opzegvergoedingen die groter dan 0 is. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


