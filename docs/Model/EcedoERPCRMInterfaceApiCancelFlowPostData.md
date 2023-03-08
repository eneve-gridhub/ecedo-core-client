# EcedoERPCRMInterfaceApiCancelFlowPostData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remove_connections** | **bool** | Optionele parameter (default false). Als deze parameter true is wordt een poging gedaan om de aansluitingen van de aanmeldflow te verwijderen. Dit is alleen mogelijk als CancelContracts ook true is. | [optional] 
**termination_fee_not_applicable** | **bool** | Optionele parameter (default false). Als deze parameter true is wordt er geen opzegvergoeding in rekening gebracht. Als deze parameter false is wordt er gekeken of er een opzegvergoeding in rekening gebracht moet worden. | [optional] 
**cancel_contracts** | **bool** | Optionele parameter (default true). Als deze parameter true is worden de statussen van de aansluitingen op \&quot;Aanmelding afgebroken\&quot; gezet, als dat niet het geval is krijgen de aansluitingen de status \&quot;Aangemaakt\&quot;. Daarnaast worden contracten van de aansluitingen van de aanmeldflow geannuleerd. Doordat de contracten geannuleerd worden, worden eventuele contract-factuuritems (ContractBillingItems) ook geannuleerd en worden er ContractCancelled-triggers verstuurd. | [optional] 
**customer_cancellation_date** | [**\DateTime**](\DateTime.md) | Optionele parameter (default &#39;vandaag&#39;). Als de parameter TerminationFeeNotApplicable false is wordt gekeken of er een opzegvergoeding in rekening gebracht moet worden. Daarvoor wordt onder andere gekeken wanneer de klant het contract heeft opgezegd. Met behulp van deze parameter kan aangegeven worden op welke datum dat was. | [optional] 
**contract_cancellation_reason** | **string** | Optioneel veld (default null). Als CancelContracts true is kan met behulp van deze variabele een reden voor de opzegging worden meegegeven. Deze reden wordt ter registratie gebruikt. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


