# EcedoERPCRMInterfaceApiExpectedAnnualStandardUsage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **string** | Optioneel veld waarin vastgelegd kan worden waarom een VJV is aangemaakt. Bijvoorbeeld omdat de klant zonnepanelen heeft laten installeren. | [optional] 
**valid_until** | [**\DateTime**](\DateTime.md) |  | [optional] 
**single_usage** | **int** | Indien een aansluiting enkel-verbuik heeft wordt de Standaard Jaar Afname (SJA) in dit veld weergegeven.  Wanneer de aansluiting normaal- en dal-verbruik heeft is dit veld null  Wanneer de aansluiting een gas aansluiting betreft, is dit veld verplicht en moeten de anderen null zijn | [optional] 
**peak_usage** | **int** | Indien een aansluiting enkel-verbuik heeft is dit veld null.  Wanneer de aansluiting normaal- en dal-verbruik heeft wordt in dit veld het normaal-verbruik van de Standaard Jaar Afname (SJA) weergegeven. | [optional] 
**off_peak_usage** | **int** | Indien een aansluiting enkel-verbuik heeft is dit veld null.  Wanneer de aansluiting normaal- en dal-verbruik heeft wordt in dit veld het dal-verbruik van de Standaard Jaar Afname (SJA) weergegeven. | [optional] 
**single_usage_odn** | **int** | Indien een aansluiting enkel-verbruik (en dus ook teruglevering) heeft wordt de Standaard Jaar Invoeding (SJI) in dit veld weergegeven. Wanneer de aansluiting geen teruglevering heeft wordt hier een 0 teruggegeven.  Wanneer de aansluiting normaal- en dal-verbruik (en dus ook teruglevering) heeft is dit veld null. | [optional] 
**peak_usage_odn** | **int** | Indien een aansluiting enkel-verbuik (en dus ook teruglevering) heeft is dit veld null.  Wanneer de aansluiting normaal- en dal-verbruik (en dus ook teruglevering) heeft wordt in dit veld de normaal-teruglevering van de Standaard Jaar Invoeding (SJI) weergegeven. Wanneer de aansluiting geen teruglevering heeft wordt hier een 0 teruggegeven. | [optional] 
**off_peak_usage_odn** | **int** | Indien een aansluiting enkel-verbuik (en dus ook teruglevering) heeft is dit veld null.  Wanneer de aansluiting normaal- en dal-verbruik (en dus ook teruglevering) heeft wordt in dit veld de dal-teruglevering van de Standaard Jaar Invoeding (SJI) weergegeven. Wanneer de aansluiting geen teruglevering heeft wordt hier een 0 teruggegeven. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


