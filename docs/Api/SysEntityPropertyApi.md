# Swagger\Client\SysEntityPropertyApi

All URIs are relative to *https://innova-test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysEntityPropertyGetEntityPropertyDefinitions**](SysEntityPropertyApi.md#sysEntityPropertyGetEntityPropertyDefinitions) | **GET** /sysapi/v1.0/entitypropertydefinitions | Opvragen Entity Property Definitions


# **sysEntityPropertyGetEntityPropertyDefinitions**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiEntityPropertyDefinition[] sysEntityPropertyGetEntityPropertyDefinitions($entity_type)

Opvragen Entity Property Definitions

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

$apiInstance = new Swagger\Client\Api\SysEntityPropertyApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$entity_type = "entity_type_example"; // string | Filter voor EntityTypes (optioneel)

try {
    $result = $apiInstance->sysEntityPropertyGetEntityPropertyDefinitions($entity_type);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysEntityPropertyApi->sysEntityPropertyGetEntityPropertyDefinitions: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **string**| Filter voor EntityTypes (optioneel) | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiEntityPropertyDefinition[]**](../Model/EcedoERPCRMInterfaceApiEntityPropertyDefinition.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

