# Swagger\Client\SysOrganizationEventApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysOrganizationEventGetFirstPossibleEventDate**](SysOrganizationEventApi.md#sysOrganizationEventGetFirstPossibleEventDate) | **GET** /sysapi/v1.0/events/minimumeventdate | Bepaal eerst mogelijke eventdatum op basis van een gewenste eventdatum
[**sysOrganizationEventGetMeterReadingCollectionEvents**](SysOrganizationEventApi.md#sysOrganizationEventGetMeterReadingCollectionEvents) | **GET** /sysapi/v1.0/organizations/{organizationId}/meterreadingcollectionevents | Opvragen van Meteropname opvraag events voor een klant
[**sysOrganizationEventGetOrganizationEventData**](SysOrganizationEventApi.md#sysOrganizationEventGetOrganizationEventData) | **GET** /sysapi/v1.0/organizations/{organizationId}/events | Opvragen van actieve events voor een klant
[**sysOrganizationEventGetSettlementEvents**](SysOrganizationEventApi.md#sysOrganizationEventGetSettlementEvents) | **GET** /sysapi/v1.0/organizations/{organizationId}/settlementevents | Opvragen van Energie Afrekening events voor een klant
[**sysOrganizationEventGetSwitchEvents**](SysOrganizationEventApi.md#sysOrganizationEventGetSwitchEvents) | **GET** /sysapi/v1.0/organizations/{organizationId}/switchevents | Opvragen van Switch (ChangeOfSupplier en MoveIn) events voor een klant


# **sysOrganizationEventGetFirstPossibleEventDate**
> \DateTime sysOrganizationEventGetFirstPossibleEventDate($desired_event_date, $event_type, $usage_type, $include_cooling_down_period, $treat_as_consumer)

Bepaal eerst mogelijke eventdatum op basis van een gewenste eventdatum

Deze API geeft aan wat de eerst mogelijke datum is waarop een bepaald event (`OrganizationEventType`) uitgevoerd kan worden.<br />  Via de parameter `desiredEventDate` kan aangegeven worden op welke moment een event idealiter uitgevoerd zou moeten worden. De API geeft in de response vervolgens terug op welke datum dat daadwerkelijk mogelijk is. Dat kan dezelfde datum als de `desiredEventDate` zijn.<br /><br />  __Belangrijk!__ Deze API geeft de eerst mogelijke datum terug die in theorie mogelijk is. Hier wordt geen rekening gehouden met de tijd die bijvoorbeeld de aanmeldflow nodig heeft om een welkomstbrief te versturen of de mogelijke reactietijd van een backoffice team als een voorschotcalculatie uitvalt. Ons advies is om een aantal dagen buffer toe te voegen om te voorkomen dat de switch-window vervalt terwijl de klant nog in de afkoelperiode zit.<br /><br />  De volgende `eventTypes` kunnen worden gebruikt: `ChangeOfSupplier`, `MoveIn`, `MoveOut`, `PVSwitch`, `EndOfSupply`<br /><br />  De response bevat een losse datum-string, bijvoorbeeld `\"2021-12-31T00:00:00\"`. Het tijd-component uit deze response mag genegeerd worden omdat deze geen waarde heeft.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysOrganizationEventApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$desired_event_date = new \DateTime("2013-10-20"); // \DateTime | Gewenste eventdatum (verplicht veld)
$event_type = "event_type_example"; // string | Type event (verplicht veld). Deze API ondersteunt niet alle `OrganizationEventTypes` die in de specificatie zichtbaar zijn. Zie de API omschrijving voor meer informatie
$usage_type = "usage_type_example"; // string | Verbruikstype van de aansluiting (verplicht veld)
$include_cooling_down_period = true; // bool | Optionele parameter (default false) die aangeeft of de afkoelperiode worden meegenomen in de berekening. Dit is alleen mogelijk bij eventTypes 'ChangeOfSupplier' en 'MoveIn'
$treat_as_consumer = true; // bool | Optionele parameter (default true) die aangeeft of de datum bepaald moet worden voor een klant die als consument behandeld moet worden. Afhankelijk van de systeeminstellingen hebben klanten die niet als consument behandeld moeten worden geen recht op een afkoelperiode. Alleen van toepassing bij eventTypes 'ChangeOfSupplier' en 'MoveIn'

try {
    $result = $apiInstance->sysOrganizationEventGetFirstPossibleEventDate($desired_event_date, $event_type, $usage_type, $include_cooling_down_period, $treat_as_consumer);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysOrganizationEventApi->sysOrganizationEventGetFirstPossibleEventDate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **desired_event_date** | **\DateTime**| Gewenste eventdatum (verplicht veld) |
 **event_type** | **string**| Type event (verplicht veld). Deze API ondersteunt niet alle &#x60;OrganizationEventTypes&#x60; die in de specificatie zichtbaar zijn. Zie de API omschrijving voor meer informatie |
 **usage_type** | **string**| Verbruikstype van de aansluiting (verplicht veld) |
 **include_cooling_down_period** | **bool**| Optionele parameter (default false) die aangeeft of de afkoelperiode worden meegenomen in de berekening. Dit is alleen mogelijk bij eventTypes &#39;ChangeOfSupplier&#39; en &#39;MoveIn&#39; | [optional]
 **treat_as_consumer** | **bool**| Optionele parameter (default true) die aangeeft of de datum bepaald moet worden voor een klant die als consument behandeld moet worden. Afhankelijk van de systeeminstellingen hebben klanten die niet als consument behandeld moeten worden geen recht op een afkoelperiode. Alleen van toepassing bij eventTypes &#39;ChangeOfSupplier&#39; en &#39;MoveIn&#39; | [optional]

### Return type

[**\DateTime**](../Model/\DateTime.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysOrganizationEventGetMeterReadingCollectionEvents**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiMeterReadingCollectionEvent[] sysOrganizationEventGetMeterReadingCollectionEvents($organization_id, $cluster_reference, $only_active)

Opvragen van Meteropname opvraag events voor een klant

Via 'onlyActive = false' kunnen ook afgeronde meteropname opvraag events worden opgehaald

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysOrganizationEventApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant
$cluster_reference = "cluster_reference_example"; // string | Optioneel filter om alleen de events van dit cluster op te vragen
$only_active = true; // bool | Boolean (default true) waarmee aangegeven kan worden dat alleen actieve verzoeken teruggegeven moeten worden

try {
    $result = $apiInstance->sysOrganizationEventGetMeterReadingCollectionEvents($organization_id, $cluster_reference, $only_active);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysOrganizationEventApi->sysOrganizationEventGetMeterReadingCollectionEvents: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant |
 **cluster_reference** | **string**| Optioneel filter om alleen de events van dit cluster op te vragen | [optional]
 **only_active** | **bool**| Boolean (default true) waarmee aangegeven kan worden dat alleen actieve verzoeken teruggegeven moeten worden | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeterReadingCollectionEvent[]**](../Model/EcedoERPCRMInterfaceApiMeterReadingCollectionEvent.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysOrganizationEventGetOrganizationEventData**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganizationEventWithWorkflowData[] sysOrganizationEventGetOrganizationEventData($organization_id, $cluster_reference)

Opvragen van actieve events voor een klant

Opvragen van actieve events voor een klant. Het resultaat geeft ook de workflowstappen die zijn afgerond.<br />  Voor de details van de verschillende steptypes kan gekeken worden naar de specifieke API's voor de specifieke events.<br />  Alleen de events van types waarvoor ook een specifieke API is worden ondersteund / geretourneerd.<br />

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysOrganizationEventApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant
$cluster_reference = "cluster_reference_example"; // string | Optioneel filter om alleen de events van dit cluster op te vragen

try {
    $result = $apiInstance->sysOrganizationEventGetOrganizationEventData($organization_id, $cluster_reference);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysOrganizationEventApi->sysOrganizationEventGetOrganizationEventData: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant |
 **cluster_reference** | **string**| Optioneel filter om alleen de events van dit cluster op te vragen | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganizationEventWithWorkflowData[]**](../Model/EcedoERPCRMInterfaceApiOrganizationEventWithWorkflowData.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysOrganizationEventGetSettlementEvents**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiSettlementEvent[] sysOrganizationEventGetSettlementEvents($organization_id, $cluster_reference, $only_active)

Opvragen van Energie Afrekening events voor een klant

Via 'onlyActive = false' kunnen ook afgeronde events worden opgehaald

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysOrganizationEventApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant
$cluster_reference = "cluster_reference_example"; // string | Optioneel filter om alleen de events van dit cluster op te vragen
$only_active = true; // bool | Boolean (default true) waarmee aangegeven kan worden dat alleen actieve events teruggegeven moeten worden

try {
    $result = $apiInstance->sysOrganizationEventGetSettlementEvents($organization_id, $cluster_reference, $only_active);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysOrganizationEventApi->sysOrganizationEventGetSettlementEvents: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant |
 **cluster_reference** | **string**| Optioneel filter om alleen de events van dit cluster op te vragen | [optional]
 **only_active** | **bool**| Boolean (default true) waarmee aangegeven kan worden dat alleen actieve events teruggegeven moeten worden | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiSettlementEvent[]**](../Model/EcedoERPCRMInterfaceApiSettlementEvent.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysOrganizationEventGetSwitchEvents**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiSwitchEvent[] sysOrganizationEventGetSwitchEvents($organization_id, $cluster_reference, $only_active)

Opvragen van Switch (ChangeOfSupplier en MoveIn) events voor een klant

Via 'onlyActive = false' kunnen ook afgeronde events worden opgehaald

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysOrganizationEventApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant
$cluster_reference = "cluster_reference_example"; // string | Optioneel filter om alleen de events van dit cluster op te vragen
$only_active = true; // bool | Boolean (default true) waarmee aangegeven kan worden dat alleen actieve events teruggegeven moeten worden

try {
    $result = $apiInstance->sysOrganizationEventGetSwitchEvents($organization_id, $cluster_reference, $only_active);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysOrganizationEventApi->sysOrganizationEventGetSwitchEvents: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant |
 **cluster_reference** | **string**| Optioneel filter om alleen de events van dit cluster op te vragen | [optional]
 **only_active** | **bool**| Boolean (default true) waarmee aangegeven kan worden dat alleen actieve events teruggegeven moeten worden | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiSwitchEvent[]**](../Model/EcedoERPCRMInterfaceApiSwitchEvent.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

