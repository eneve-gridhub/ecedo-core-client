# Swagger\Client\SysGreeningOptionsApi

All URIs are relative to *https://innova-test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysGreeningOptionsGetGreeningOptions**](SysGreeningOptionsApi.md#sysGreeningOptionsGetGreeningOptions) | **GET** /sysapi/v1.0/greeningoptions | Verkrijg de Vergroeningstypes


# **sysGreeningOptionsGetGreeningOptions**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiGreeningOption[] sysGreeningOptionsGetGreeningOptions($market_segment)

Verkrijg de Vergroeningstypes

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

$apiInstance = new Swagger\Client\Api\SysGreeningOptionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$market_segment = "market_segment_example"; // string | 

try {
    $result = $apiInstance->sysGreeningOptionsGetGreeningOptions($market_segment);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysGreeningOptionsApi->sysGreeningOptionsGetGreeningOptions: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_segment** | **string**|  | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiGreeningOption[]**](../Model/EcedoERPCRMInterfaceApiGreeningOption.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

