# EcedoERPCRMInterfaceApiDebtorPostData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **string** | De betaalmethode waar de klant gebruik van maakt | [optional] 
**payment_term** | **int** | Optionele betaaltermijn in dagen. Dit is een verplicht veld wanneer er meerdere betaaltermijnen geconfigureerd zijn voor de gekozen &#x60;PaymentMethod&#x60; | [optional] 
**debtor_name** | **string** | Optioneel veld waarmee een afwijkende tenaamstelling van de bankrekening vastgelegd kan worden. Als dit veld niet wordt meegestuurd genereert Ecedo een tenaamstelling op basis van de klant-naam | [optional] 
**bank_account_type** | **string** | Type bankrekeningnummer. Let op! Alleen &#x60;IBAN&#x60; wordt actief ondersteund. | [optional] 
**bank_account_number** | **string** | Optioneel bankrekeningnummer. Dit is een verplicht veld wanneer &#x60;BankAccountType&#x60; is ingevuld of wanneer gebruik wordt gemaakt van de &#x60;PaymentMethod&#x60; &#x60;AutomaticCollection&#x60; | [optional] 
**mandate_date** | [**\DateTime**](\DateTime.md) | Datum waarop de klant het mandaat voor de automatische incasso heeft afgegeven | [optional] 
**mandate_reference** | **string** | Referentie die verwijst naar het automatische-incasso-mandaat dat de klant heeft afgegeven | [optional] 
**bic** | **string** |  | [optional] 
**print_advance_payment_invoice** | **bool** |  | [optional] 
**preferred_automatic_collection_day** | **int** |  | [optional] 
**payment_reference** | **string** |  | [optional] 
**preferred_invoice_day** | **int** |  | [optional] 
**preferred_advance_payment_invoice_contact_method** | **string** |  | [optional] 
**preferred_settlement_invoice_contact_method** | **string** |  | [optional] 
**advance_payment_schedule_type** | **string** |  | [optional] 
**mandate_type** | **string** |  | [optional] 
**generate_e_invoice** | **bool** |  | [optional] 
**client_reference** | **string** | Optionele externe referentie vanuit een ander systeem | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


