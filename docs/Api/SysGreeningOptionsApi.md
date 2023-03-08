# Swagger\Client\SysGreeningOptionsApi

All URIs are relative to *https://test.ecedo.com*

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

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


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

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

