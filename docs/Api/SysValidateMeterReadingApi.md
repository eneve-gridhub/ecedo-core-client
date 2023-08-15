# Swagger\Client\SysValidateMeterReadingApi

All URIs are relative to *https://innova.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysValidateMeterReadingPost**](SysValidateMeterReadingApi.md#sysValidateMeterReadingPost) | **POST** /sysapi/v1.0/validatemeterreading | 


# **sysValidateMeterReadingPost**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiValidateMeterReadingPostResult sysValidateMeterReadingPost($meter_reading)



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

$apiInstance = new Swagger\Client\Api\SysValidateMeterReadingApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$meter_reading = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiValidateMeterReadingPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiValidateMeterReadingPostData | 

try {
    $result = $apiInstance->sysValidateMeterReadingPost($meter_reading);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysValidateMeterReadingApi->sysValidateMeterReadingPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_reading** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiValidateMeterReadingPostData**](../Model/EcedoERPCRMInterfaceApiValidateMeterReadingPostData.md)|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiValidateMeterReadingPostResult**](../Model/EcedoERPCRMInterfaceApiValidateMeterReadingPostResult.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

