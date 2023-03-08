# Swagger\Client\SysMeterReadingsApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysMeterReadingsCalculateAnnualStandardUsage**](SysMeterReadingsApi.md#sysMeterReadingsCalculateAnnualStandardUsage) | **POST** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/calculateannualstandardusage | Bereken het standaard jaarverbruik (SJV) / Annual Standard Usage
[**sysMeterReadingsCalculatedMeterReading**](SysMeterReadingsApi.md#sysMeterReadingsCalculatedMeterReading) | **GET** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/calculatedmeterreading | Meterstand berekenen voor een bepaalde datum
[**sysMeterReadingsDeleteUsableMeterReading**](SysMeterReadingsApi.md#sysMeterReadingsDeleteUsableMeterReading) | **DELETE** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/meterreadings/{meterReadingId} | Verwijderen van een meteropname/meterstand behorende bij een aansluiting
[**sysMeterReadingsGetMeterReadingById**](SysMeterReadingsApi.md#sysMeterReadingsGetMeterReadingById) | **GET** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/meterreadings/{meterReadingId} | Meteropname opvragen aan de hand van een meter reading Id.
[**sysMeterReadingsGetUsableMeterReadings**](SysMeterReadingsApi.md#sysMeterReadingsGetUsableMeterReadings) | **GET** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/meterreadings | Meerdere (bruikbare) meteropnames/meterstanden opvragen gerelateerd aan een aansluiting.  De niet bruikbare meteropnames zijn in de GUI zichtbaar als &#39;Niet gebruikt&#39;.
[**sysMeterReadingsPostNewMeterReading**](SysMeterReadingsApi.md#sysMeterReadingsPostNewMeterReading) | **POST** /sysapi/v1.0/meterreadings | Meteropname insturen.


# **sysMeterReadingsCalculateAnnualStandardUsage**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiAnnualStandardUsage sysMeterReadingsCalculateAnnualStandardUsage($organization_id, $connection_id, $data)

Bereken het standaard jaarverbruik (SJV) / Annual Standard Usage

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysMeterReadingsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de organisatie
$connection_id = "connection_id_example"; // string | Guid van de aansluiting
$data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiCalculateAnnualStandardUsagePostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiCalculateAnnualStandardUsagePostData | 

try {
    $result = $apiInstance->sysMeterReadingsCalculateAnnualStandardUsage($organization_id, $connection_id, $data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeterReadingsApi->sysMeterReadingsCalculateAnnualStandardUsage: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de organisatie |
 **connection_id** | **string**| Guid van de aansluiting |
 **data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiCalculateAnnualStandardUsagePostData**](../Model/EcedoERPCRMInterfaceApiCalculateAnnualStandardUsagePostData.md)|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAnnualStandardUsage**](../Model/EcedoERPCRMInterfaceApiAnnualStandardUsage.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysMeterReadingsCalculatedMeterReading**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiCalculatedMeterReading sysMeterReadingsCalculatedMeterReading($organization_id, $connection_id, $reading_date)

Meterstand berekenen voor een bepaalde datum

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysMeterReadingsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de organisatie
$connection_id = "connection_id_example"; // string | Guid van de aansluiting
$reading_date = new \DateTime("2013-10-20"); // \DateTime | Datum waarvoor de meterstand moet worden berekend

try {
    $result = $apiInstance->sysMeterReadingsCalculatedMeterReading($organization_id, $connection_id, $reading_date);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeterReadingsApi->sysMeterReadingsCalculatedMeterReading: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de organisatie |
 **connection_id** | **string**| Guid van de aansluiting |
 **reading_date** | **\DateTime**| Datum waarvoor de meterstand moet worden berekend |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiCalculatedMeterReading**](../Model/EcedoERPCRMInterfaceApiCalculatedMeterReading.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysMeterReadingsDeleteUsableMeterReading**
> object sysMeterReadingsDeleteUsableMeterReading($organization_id, $connection_id, $meter_reading_id)

Verwijderen van een meteropname/meterstand behorende bij een aansluiting

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysMeterReadingsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de organisatie
$connection_id = "connection_id_example"; // string | Guid van de aansluiting
$meter_reading_id = "meter_reading_id_example"; // string | Guid van de meterstand

try {
    $result = $apiInstance->sysMeterReadingsDeleteUsableMeterReading($organization_id, $connection_id, $meter_reading_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeterReadingsApi->sysMeterReadingsDeleteUsableMeterReading: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de organisatie |
 **connection_id** | **string**| Guid van de aansluiting |
 **meter_reading_id** | **string**| Guid van de meterstand |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysMeterReadingsGetMeterReadingById**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiMeterReading sysMeterReadingsGetMeterReadingById($organization_id, $connection_id, $meter_reading_id)

Meteropname opvragen aan de hand van een meter reading Id.

Meteropname opvragen.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysMeterReadingsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de organisatie
$connection_id = "connection_id_example"; // string | Guid van de aansluiting
$meter_reading_id = "meter_reading_id_example"; // string | Guid van de meterstand

try {
    $result = $apiInstance->sysMeterReadingsGetMeterReadingById($organization_id, $connection_id, $meter_reading_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeterReadingsApi->sysMeterReadingsGetMeterReadingById: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de organisatie |
 **connection_id** | **string**| Guid van de aansluiting |
 **meter_reading_id** | **string**| Guid van de meterstand |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeterReading**](../Model/EcedoERPCRMInterfaceApiMeterReading.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysMeterReadingsGetUsableMeterReadings**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiMeterReading[] sysMeterReadingsGetUsableMeterReadings($organization_id, $connection_id, $only_usable)

Meerdere (bruikbare) meteropnames/meterstanden opvragen gerelateerd aan een aansluiting.  De niet bruikbare meteropnames zijn in de GUI zichtbaar als 'Niet gebruikt'.

Meerdere meteropnames opvragen.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysMeterReadingsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de organisatie
$connection_id = "connection_id_example"; // string | Guid van de aansluiting
$only_usable = true; // bool | Met of zonder meteropnames 'Niet gebruikt'. Default true (= 'Zonder')

try {
    $result = $apiInstance->sysMeterReadingsGetUsableMeterReadings($organization_id, $connection_id, $only_usable);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeterReadingsApi->sysMeterReadingsGetUsableMeterReadings: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de organisatie |
 **connection_id** | **string**| Guid van de aansluiting |
 **only_usable** | **bool**| Met of zonder meteropnames &#39;Niet gebruikt&#39;. Default true (&#x3D; &#39;Zonder&#39;) | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeterReading[]**](../Model/EcedoERPCRMInterfaceApiMeterReading.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysMeterReadingsPostNewMeterReading**
> object sysMeterReadingsPostNewMeterReading($meter_reading)

Meteropname insturen.

Met behulp van deze API kunnen meterstanden in Ecedo worden aangemaakt. Dit zijn bijvoorbeeld meterstanden die een klant kan invullen in een klantportaal en waarvoor Ecedo eerder een meterstandenverzoek heeft verstuurd.<br />  __Let op!__ Voordat deze API wordt aangeroepen moet de meterstand gevalideerd worden via de ValudateMeterReading-API.<br /><br />  Zie de developer handleiding <a target=\"_blank\" href=\"https://ecedo1.atlassian.net/wiki/spaces/KNOWLEDGE/pages/440664069/Meterstandverzoeken+afhandelen+in+extern+portaal\">Meterstandverzoeken afhandelen in extern portaal</a> voor het gebruik van deze API in een keten<br /><br />  De API biedt de mogelijkheid om maximaal 4 tellerstanden in te voeren. Welke tellerstanden nodig zijn is afhankelijk van de meter die op de aansluiting aanwezig is.<br />  Voor gas-meters geldt dat de stand ingestuurd moet worden in het veld `LDNT1`<br />

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysMeterReadingsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$meter_reading = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiMeterReadingPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiMeterReadingPostData | 

try {
    $result = $apiInstance->sysMeterReadingsPostNewMeterReading($meter_reading);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeterReadingsApi->sysMeterReadingsPostNewMeterReading: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_reading** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeterReadingPostData**](../Model/EcedoERPCRMInterfaceApiMeterReadingPostData.md)|  |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

