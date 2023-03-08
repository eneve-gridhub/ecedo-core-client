# EcedoERPCRMInterfaceApiPreNotifyContractProcessSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **string** | Wanneer UpdateConnection de waarde \&quot;true\&quot; heeft moet deze parameter gevuld zijn met het OrganizationId van de klant van de aansluiting | [optional] 
**connection_id** | **string** | Wanneer UpdateConnection de waarde \&quot;true\&quot; heeft moet deze parameter gevuld zijn met het ConnectionId van de aansluiting | [optional] 
**use_cer_lookup** | **bool** | Met behulp van deze parameter kan het Contract Einde Register (CER) bevraagd worden om de gegevens van het huidige contract op te vragen. Wanneer deze variabele \&quot;true\&quot; is wordt het CERLookupData-object in de response gevuld | [optional] 
**update_connection** | **bool** | Het het aanmelden van het contract in het CER kan een bestaande aansluiting automatisch bijgewerkt worden met de gegevens die nu uit het C-AR op te vragen zijn. Dat wordt alleen gedaan wanneer deze variabele \&quot;true\&quot; is | [optional] 
**switch_supplier_ean** | **string** | Indien er in een omgeving meerdere leverancier-EANs geconfigureerd zijn kan met behulp van deze parameter aangegeven worden welke leverancier-EAN gebruikt moet worden om de aanmelding van het contract mee te doen. Standaard wordt de hoofd-EAN gebruikt. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


