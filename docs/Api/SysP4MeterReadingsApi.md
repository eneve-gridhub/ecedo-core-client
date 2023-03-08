# Swagger\Client\SysP4MeterReadingsApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysP4MeterReadingsGetByConnectionId**](SysP4MeterReadingsApi.md#sysP4MeterReadingsGetByConnectionId) | **GET** /sysapi/v1.0/P4MeterReadings/{connectionId} | Get readings voor connectieId, type en periode.
[**sysP4MeterReadingsGetByEan**](SysP4MeterReadingsApi.md#sysP4MeterReadingsGetByEan) | **GET** /sysapi/v1.0/P4MeterReadings | Get readings voor ean, type en periode.
[**sysP4MeterReadingsGetByReadingIds**](SysP4MeterReadingsApi.md#sysP4MeterReadingsGetByReadingIds) | **GET** /sysapi/v1.0/P4MeterReadings/readingIds/{type} | Get readings op basis van p4readingIds.
[**sysP4MeterReadingsGetHistoricalDayP4MeterReadingsFromEdsn**](SysP4MeterReadingsApi.md#sysP4MeterReadingsGetHistoricalDayP4MeterReadingsFromEdsn) | **GET** /sysapi/v1.0/HistoricalDayReadings/{connectionId} | Verkrijg historische dagstanden van EDSN. De klant moet toestemming hebben gegeven om dit op te mogen vragen


# **sysP4MeterReadingsGetByConnectionId**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiP4MeterReadings sysP4MeterReadingsGetByConnectionId($connection_id, $type, $start_date, $end_date)

Get readings voor connectieId, type en periode.

De ODN en LDN velden bevatten standen, geen verbruiken    Het response-voorbeeld geeft dagstanden (`type = DAY`) weer. Zie \"GET /sysapi/v1.0/P4MeterReadings\" voor een voorbeeld voor intervalstanden (`type = INT`).

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysP4MeterReadingsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$connection_id = "connection_id_example"; // string | 
$type = "type_example"; // string | 
$start_date = new \DateTime("2013-10-20"); // \DateTime | startdatum voor opvragen periode
$end_date = new \DateTime("2013-10-20"); // \DateTime | einddatum voor opvragen periode. Indien niet gevuld worden alleen readings op startdatum teruggegeven. Periode is gemaximaliseerd op 31 dagen voor intervalstanden. Bij dagstanden geldt een maximale periode van 366 dagen.

try {
    $result = $apiInstance->sysP4MeterReadingsGetByConnectionId($connection_id, $type, $start_date, $end_date);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysP4MeterReadingsApi->sysP4MeterReadingsGetByConnectionId: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **string**|  |
 **type** | **string**|  |
 **start_date** | **\DateTime**| startdatum voor opvragen periode |
 **end_date** | **\DateTime**| einddatum voor opvragen periode. Indien niet gevuld worden alleen readings op startdatum teruggegeven. Periode is gemaximaliseerd op 31 dagen voor intervalstanden. Bij dagstanden geldt een maximale periode van 366 dagen. | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiP4MeterReadings**](../Model/EcedoERPCRMInterfaceApiP4MeterReadings.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysP4MeterReadingsGetByEan**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiP4MeterReadings sysP4MeterReadingsGetByEan($ean, $type, $start_date, $end_date)

Get readings voor ean, type en periode.

De ODN en LDN velden bevatten standen, geen verbruiken    Het response-voorbeeld geeft intervalstanden (`type = INT`) weer. Zie \"GET /sysapi/v1.0/P4MeterReadings/{connectionId}\" voor een voorbeeld voor dagstanden (`type = DAY`).    Let op: bij een meterwissel kan het voorkomen dat er om middernacht 2 readings beschikbaar zijn: een eindstand voor de oude meter en een beginstand voor de nieuwe meter. Via het MeterNumber veld kan onderscheid gemaakt worden tussen die twee standen.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysP4MeterReadingsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ean = "ean_example"; // string | 
$type = "type_example"; // string | 
$start_date = new \DateTime("2013-10-20"); // \DateTime | startdatum voor opvragen periode
$end_date = new \DateTime("2013-10-20"); // \DateTime | einddatum voor opvragen periode. Indien niet gevuld worden alleen readings op startdatum teruggegeven. Periode is gemaximaliseerd op 31 dagen voor intervalstanden. Bij dagstanden geldt een maximale periode van 366 dagen.

try {
    $result = $apiInstance->sysP4MeterReadingsGetByEan($ean, $type, $start_date, $end_date);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysP4MeterReadingsApi->sysP4MeterReadingsGetByEan: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **string**|  |
 **type** | **string**|  |
 **start_date** | **\DateTime**| startdatum voor opvragen periode |
 **end_date** | **\DateTime**| einddatum voor opvragen periode. Indien niet gevuld worden alleen readings op startdatum teruggegeven. Periode is gemaximaliseerd op 31 dagen voor intervalstanden. Bij dagstanden geldt een maximale periode van 366 dagen. | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiP4MeterReadings**](../Model/EcedoERPCRMInterfaceApiP4MeterReadings.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysP4MeterReadingsGetByReadingIds**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiP4MeterReadings sysP4MeterReadingsGetByReadingIds($reading_ids, $type)

Get readings op basis van p4readingIds.

De ODN en LDN velden bevatten standen, geen verbruiken    Het response-voorbeeld geeft intervalstanden (`type = INT`) weer. Zie \"GET /sysapi/v1.0/P4MeterReadings/{connectionId}\" voor een voorbeeld voor dagstanden (`type = DAY`).

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysP4MeterReadingsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$reading_ids = array("reading_ids_example"); // string[] | P4ReadingIds
$type = "type_example"; // string | 

try {
    $result = $apiInstance->sysP4MeterReadingsGetByReadingIds($reading_ids, $type);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysP4MeterReadingsApi->sysP4MeterReadingsGetByReadingIds: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reading_ids** | [**string[]**](../Model/string.md)| P4ReadingIds |
 **type** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiP4MeterReadings**](../Model/EcedoERPCRMInterfaceApiP4MeterReadings.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysP4MeterReadingsGetHistoricalDayP4MeterReadingsFromEdsn**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiDayP4MeterReadings sysP4MeterReadingsGetHistoricalDayP4MeterReadingsFromEdsn($connection_id, $start_date, $end_date)

Verkrijg historische dagstanden van EDSN. De klant moet toestemming hebben gegeven om dit op te mogen vragen

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysP4MeterReadingsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$connection_id = "connection_id_example"; // string | 
$start_date = new \DateTime("2013-10-20"); // \DateTime | 
$end_date = new \DateTime("2013-10-20"); // \DateTime | wanneer niet wordt meegegeven dan wordt de huidige datum genomen

try {
    $result = $apiInstance->sysP4MeterReadingsGetHistoricalDayP4MeterReadingsFromEdsn($connection_id, $start_date, $end_date);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysP4MeterReadingsApi->sysP4MeterReadingsGetHistoricalDayP4MeterReadingsFromEdsn: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **string**|  |
 **start_date** | **\DateTime**|  |
 **end_date** | **\DateTime**| wanneer niet wordt meegegeven dan wordt de huidige datum genomen | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiDayP4MeterReadings**](../Model/EcedoERPCRMInterfaceApiDayP4MeterReadings.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

