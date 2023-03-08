# EcedoERPCRMInterfaceApiTelemetryData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | [**\DateTime**](\DateTime.md) | Startdatum met tijd van de meetperiode. | [optional] 
**end_date** | [**\DateTime**](\DateTime.md) | Einddatum met tijd van de meetperiode. Dit is de tot-tijd. | [optional] 
**reading_date** | [**\DateTime**](\DateTime.md) | Datum met tijd waarop de meetdata is vastgesteld. | [optional] 
**usage_ldn** | **double** | Het verbruik in de aangegeven periode. | [optional] 
**usage_odn** | **double** | De teruglevering in de aangegeven periode. | [optional] 
**measure_unit** | **string** | De eenheid van het verbruik en de teruglevering. Voor elektriciteit wordt alleen &#x60;KWH&#x60; ondersteund en voor gas alleen &#x60;MQT&#x60;. | [optional] 
**version** | **int** | De versie van de meetdata. Bij gas-aansluitingen kan dit gebruikt worden om de BALL-versie vast te leggen. Als er al meetdata bestaat met deze versie dan wordt het revisie-veld opgehoogd zodat zichtbaar is wat de meest recente versie van de data is. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


