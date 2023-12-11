# Swagger\Client\SysPeriodicCostEventLogsApi

All URIs are relative to *https://innova-test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysPeriodicCostEventLogsGet**](SysPeriodicCostEventLogsApi.md#sysPeriodicCostEventLogsGet) | **GET** /sysapi/v1.0/organizations/{organizationId}/periodiccosteventlogs | 


# **sysPeriodicCostEventLogsGet**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiPeriodicCostEventLog[] sysPeriodicCostEventLogsGet($organization_id, $event_end_date, $cluster_reference, $include_last_year)



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

$apiInstance = new Swagger\Client\Api\SysPeriodicCostEventLogsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$event_end_date = new \DateTime("2013-10-20"); // \DateTime | 
$cluster_reference = "cluster_reference_example"; // string | 
$include_last_year = true; // bool | 

try {
    $result = $apiInstance->sysPeriodicCostEventLogsGet($organization_id, $event_end_date, $cluster_reference, $include_last_year);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPeriodicCostEventLogsApi->sysPeriodicCostEventLogsGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **event_end_date** | **\DateTime**|  | [optional]
 **cluster_reference** | **string**|  | [optional]
 **include_last_year** | **bool**|  | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiPeriodicCostEventLog[]**](../Model/EcedoERPCRMInterfaceApiPeriodicCostEventLog.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

