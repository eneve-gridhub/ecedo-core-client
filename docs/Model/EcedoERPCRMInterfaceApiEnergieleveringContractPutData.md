# EcedoERPCRMInterfaceApiEnergieleveringContractPutData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meelift_proposition_reference** | **string** | Optionele parameter (default null). Hiermee kan de meeliftpropositie van een contract worden aangepast. Gebruik dit alleen in zeer specifieke gevallen. | [optional] 
**original_end_date** | [**\DateTime**](\DateTime.md) | Optionele parameter (default null). Hiermee kan de originele einddatum van een contract worden aangepast. Gebruik dit alleen in zeer specifieke gevallen. | [optional] 
**start_reason** | **string** | Optionele parameter (default null). Hiermee kan de startreden van een contract worden aangepast. Gebruik dit alleen in zeer specifieke gevallen. | [optional] 
**end_reason** | **string** | Optionele parameter (default null). Hiermee kan de eindreden van een contract worden aangepast. Gebruik dit alleen in zeer specifieke gevallen. | [optional] 
**previous_contract_id** | **string** | Optionele parameter (default null). Hiermee kan het huidige contract aan een voorgaand contract worden gekoppeld of kan de koppeling worden verbroken. Gebruik dit alleen in zeer specifieke gevallen. | [optional] 
**channel** | **string** | Optionele parameter (default null). Dit is een verouderde parameter. Gebruik de ContractProperties-array in plaats van dit directe veld. De bestaande waarde wordt alleen bijgewerkt wanneer de nieuwe waarde niet null is. Geef een lege string mee om de bestaande waarde weg te halen. Dit veld mag niet gebruikt worden wanneer er ContractProperties worden meegestuurd. | [optional] 
**sales_reference** | **string** | Optionele parameter (default null). Dit is een verouderde parameter. Gebruik de ContractProperties-array in plaats van dit directe veld. De bestaande waarde wordt alleen bijgewerkt wanneer de nieuwe waarde niet null is. Geef een lege string mee om de bestaande waarde weg te halen. Dit veld mag niet gebruikt worden wanneer er ContractProperties worden meegestuurd. | [optional] 
**status** | **string** | Optionele parameter (default null). Deze parameter kan alleen gebruikt worden bij energieleveringcontracten. Daarnaast is het alleen mogelijk om de status van een actief contract aan te passen naar geannuleerd en de status van een geannuleerd contract aan te passen naar actief. Andere transities zijn niet toegestaan. Bij het aanpassen van de status wordt automatisch de eindreden van het contract ingesteld. | [optional] 
**cancellation_reason** | **string** | Optionele parameter (default null). Deze parameter kan alleen gebruikt worden om de reden van opzegging bij te werken. | [optional] 
**contract_properties** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiContractPropertyPostData[]**](EcedoERPCRMInterfaceApiContractPropertyPostData.md) | Optionele parameter (default null). Deze lijst kan gebruikt worden om de waarden van contractafspraken aan te passen of om bestaande contractafspraken weg te halen. | [optional] 
**start_date** | [**\DateTime**](\DateTime.md) | Optionele parameter (default null). Hiermee kan de startdatum van een contract worden aangepast. Gebruik dit alleen in zeer specifieke gevallen. | [optional] 
**end_date** | [**\DateTime**](\DateTime.md) | Optionele parameter (default null). Hiermee kan de einddatum van een contract worden aangepast. Gebruik dit alleen in zeer specifieke gevallen. | [optional] 
**agreement_date** | [**\DateTime**](\DateTime.md) | Optionele parameter (default null). Hiermee kan de tekendatum van een contract worden aangepast. Gebruik dit alleen in zeer specifieke gevallen. | [optional] 
**proposition_reference** | **string** | Optionele parameter (default null). Hiermee kan de propositie van een contract worden aangepast. Gebruik dit alleen in zeer specifieke gevallen. | [optional] 
**comment** | **string** | Optionele parameter (default null). De bestaande waarde wordt alleen bijgewerkt wanneer de nieuwe waarde niet null is. Geef een lege string mee om de bestaande waarde weg te halen. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


