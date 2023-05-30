# EcedoERPCRMInterfaceApiCalculatedTerminationFee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_termination_fee** | **bool** | Of er een opzegvergoeding betaald moet worden. Deze is true als de opzegboete groter dan 0 is. | [optional] 
**termination_fee_amount** | **double** | De opzegvergoeding die berekend is Als de opzegvergoeding kleiner dan 0 is of er is geen opzegvergoeding berekend, dan wordt dit veld op 0 gezet. &lt;br /&gt;   Als de opzegvergoeding groter dan 0 is dan bevat het de berekende opzegvergoeding.  Dit bedrag is exclusief BTW. | [optional] 
**termination_fee_vat_amount** | **double** | De BTW van de opzegvergoeding. | [optional] 
**termination_fee_total_amount** | **double** | Het totale bedrag van de opzegvergoeding. Dus de opzegvergoeding inclusief BTW | [optional] 
**contract_id** | **string** | Het contract waar de opzegvergoeding bij hoort. | [optional] 
**contract_start_date** | [**\DateTime**](\DateTime.md) | De startdatum van het contract. | [optional] 
**contract_end_date** | [**\DateTime**](\DateTime.md) | De (oorspronkelijke) einddatum van het contract. Dus niet de einddatum van de opzegdatum (de termination date). | [optional] 
**contract_termination_date** | [**\DateTime**](\DateTime.md) | De opzegdatum van het contract. | [optional] 
**termination_fee_type** | **string** | Het type van de berekende opzegvergoeding. &lt;br /&gt;   Er zijn 4 mogelijkheden: None, Business, Rover2013 en Rover2023. &lt;br /&gt;   None: Geen, betekent dat er geen opzegvergoeding berekend is. &lt;br /&gt;   Business: Zakelijk, er is een opzegvergoeding berekend, maar dit is een zakelijke opzegvergoeding. &lt;br /&gt;   Rover2013: Het is een rover 2013 opzegvergoeding. &lt;br /&gt;   Rover2023: Het is een rover 2023 opzegvergoeding. (Alleen in het geval van een rover 2023 opzegvergoeding zal er een CalculationData object gevuld zijn) &lt;br /&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


