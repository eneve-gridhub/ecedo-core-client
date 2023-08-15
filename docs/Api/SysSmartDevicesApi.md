# Swagger\Client\SysSmartDevicesApi

All URIs are relative to *https://innova.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysSmartDevicesGetSmartChargingSessions**](SysSmartDevicesApi.md#sysSmartDevicesGetSmartChargingSessions) | **GET** /sysapi/v1.0/organizations/{organizationId}/smartdevices/{deviceId}/smartchargingsessions | Verkrijg slimme laadsessies per apparaat
[**sysSmartDevicesGetSmartDevices**](SysSmartDevicesApi.md#sysSmartDevicesGetSmartDevices) | **GET** /sysapi/v1.0/organizations/{organizationId}/smartdevices | Verkrijg slimme apparaten van organisatie


# **sysSmartDevicesGetSmartChargingSessions**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiSmartChargingSession[] sysSmartDevicesGetSmartChargingSessions($organization_id, $device_id, $start_date, $end_date, $include_already_settled)

Verkrijg slimme laadsessies per apparaat

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: Authorization
$config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');
// Configure API key authorization: Ocp-Apim-Subscription-Key
$config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Ocp-Apim-Subscription-Key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Ocp-Apim-Subscription-Key', 'Bearer');

$apiInstance = new Swagger\Client\Api\SysSmartDevicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$device_id = "device_id_example"; // string | 
$start_date = new \DateTime("2013-10-20"); // \DateTime | 
$end_date = new \DateTime("2013-10-20"); // \DateTime | 
$include_already_settled = true; // bool | 

try {
    $result = $apiInstance->sysSmartDevicesGetSmartChargingSessions($organization_id, $device_id, $start_date, $end_date, $include_already_settled);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysSmartDevicesApi->sysSmartDevicesGetSmartChargingSessions: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **device_id** | **string**|  |
 **start_date** | **\DateTime**|  |
 **end_date** | **\DateTime**|  | [optional]
 **include_already_settled** | **bool**|  | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiSmartChargingSession[]**](../Model/EcedoERPCRMInterfaceApiSmartChargingSession.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysSmartDevicesGetSmartDevices**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiSmartDevice[] sysSmartDevicesGetSmartDevices($organization_id)

Verkrijg slimme apparaten van organisatie

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: Authorization
$config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');
// Configure API key authorization: Ocp-Apim-Subscription-Key
$config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Ocp-Apim-Subscription-Key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Ocp-Apim-Subscription-Key', 'Bearer');

$apiInstance = new Swagger\Client\Api\SysSmartDevicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 

try {
    $result = $apiInstance->sysSmartDevicesGetSmartDevices($organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysSmartDevicesApi->sysSmartDevicesGetSmartDevices: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiSmartDevice[]**](../Model/EcedoERPCRMInterfaceApiSmartDevice.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

