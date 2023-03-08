# EcedoERPCRMInterfaceApiAdvancePaymentPostData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_reference** | **string** |  | [optional] 
**start_date** | [**\DateTime**](\DateTime.md) |  | [optional] 
**end_date** | [**\DateTime**](\DateTime.md) |  | [optional] 
**has_advance_payment** | **bool** |  | [optional] 
**connection_amounts** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAdvanceAgreedPaymentPerConnection[]**](EcedoERPCRMInterfaceApiAdvanceAgreedPaymentPerConnection.md) |  | [optional] 
**inform_customer** | **bool** |  | [optional] 
**delete_future_unused_advance_payments** | **bool** |  | [optional] 
**calculation_reason** | **string** |  | [optional] 
**do_combine_rows** | **bool** |  | [optional] 
**amount** | **double** | Obsolete: Dit veld is vervangen door AgreedAmount, zodat het verschil met TargetAmount duidelijk zichtbaar is | [optional] 
**agreed_amount** | **double** |  | [optional] 
**target_amount** | **double** |  | [optional] 
**comment** | **string** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


