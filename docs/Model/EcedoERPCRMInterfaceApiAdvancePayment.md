# EcedoERPCRMInterfaceApiAdvancePayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advance_payment_id** | **string** |  | [optional] 
**modified_by_user_name** | **string** |  | [optional] 
**connection_amounts** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAdvancePaymentPerConnection[]**](EcedoERPCRMInterfaceApiAdvancePaymentPerConnection.md) |  | [optional] 
**is_proposed** | **bool** | Geeft aan of het voorschot wacht op bevestiging van de klant | [optional] 
**calculation_reason** | **string** | De reden waarom dit voorschot berekend is: New, ContractRenewal, Settlement, Customer, ContractTypeChange, EnergyTax, Networkcosts, AnnualStandardUsage, MasterData, Cluster, PhysicalStatus, MonthClosed, Move | [optional] 
**calculation_reason_localized** | **string** | Nederlandse vertaling van CalculationReason | [optional] 
**advance_payment_scheme** | **string** |  | [optional] 
**advance_payment_scheme_localized** | **string** |  | [optional] 
**cluster_id** | **string** |  | [optional] 
**cluster_reference** | **string** | De technische referentie van het cluster waarvoor het voorschot is aangemaakt | [optional] 
**has_advance_payment** | **bool** | Wanneer een cluster geen voorschot moet ontvangen, wordt een nee-voorschot aangemaakt, waardoor er dus een AdvancePayment-object dat aangeeft dat er geen voorschot verstuurd moet worden. Als deze variabele de waarde false heeft is er geen voorschot. | [optional] 
**amount** | **double** | Het totale voorschotbedrag in euro&#39;s, inclusief btw | [optional] 
**agreed_amount** | **double** |  | [optional] 
**calculated_amount** | **double** | Het berekende voorschotbedrag in euro&#39;s inclusief btw. Dit kan afwijken van het Amount als het voorschot met een AgreedAmount of TargetAmount is berekend | [optional] 
**start_date** | [**\DateTime**](\DateTime.md) | Eerste dag van de maand vanaf wanneer het voorschot geldig is | [optional] 
**end_date** | [**\DateTime**](\DateTime.md) | Optionele eerste dag van de maand tot wanneer het voorschot geldig is (als het voorschot tot en met februari 2021 geldig is, zal dit veld de waarde \&quot;2021-03-01T00:00:00\&quot; bevatten. Als het voorschot geen einddatum heeft zal dit veld null zijn. | [optional] 
**comment** | **string** |  | [optional] 
**advance_payment_rows** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAdvancePaymentRow[]**](EcedoERPCRMInterfaceApiAdvancePaymentRow.md) | Niet samengevoegde voorschotregels (zie uitleg over doCombineRows) | [optional] 
**combined_advance_payment_rows** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAdvancePaymentRow[]**](EcedoERPCRMInterfaceApiAdvancePaymentRow.md) | Wel samengevoegde voorschotregels (zie uitleg over doCombineRows) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


