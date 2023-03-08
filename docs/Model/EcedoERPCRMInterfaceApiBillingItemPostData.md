# EcedoERPCRMInterfaceApiBillingItemPostData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_item_group_id** | **string** | Een BillingItem is een instantie van een BillingItemGroup. Dit veld moet de verwijzing bevatten naar de BillingItemGroup waarop dit BillingItem gebaseerd moet worden. De BillingItemGroups zijn op te vragen via een andere API | [optional] 
**external_reference** | **string** | Optionele externe referentie waarin bijvoorbeeld de bron van of aanleiding voor het BillingItem geregistreerd kan worden | [optional] 
**description** | **string** | Optionele omschrijving | [optional] 
**start_date** | [**\DateTime**](\DateTime.md) | Verplichte datum waarmee aangegeven wordt vanaf wanneer het BillingItem gefactureerd mag worden | [optional] 
**end_date** | [**\DateTime**](\DateTime.md) | Optionele datum tot wanneer het BillingItem gefactureerd mag worden | [optional] 
**usage** | **double** | Het verbruik van het factuuritem. Dit kan alleen gebruikt worden wanneer bij de BillingItemGroup is aangegeven dat het een verbruik gerelateerd BillingItem is | [optional] 
**price** | **double** | Met behulp van dit veld kan de prijs van het BillingItem vastgelegd kan worden. Dit is verplicht wanneer bij de BillingItemGroup is vastgelegd dat het een Volume-BillingItem is | [optional] 
**contract_id** | **string** | Met behulp van dit veld kan een referentie naar een contract vastgelegd worden. Dit is verplicht wanneer bij de BillingItemGroup is vastgelegd dat het een Contract-BillingItem is | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


