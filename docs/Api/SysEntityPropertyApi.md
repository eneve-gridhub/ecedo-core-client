# Swagger\Client\SysEntityPropertyApi

All URIs are relative to *https://test.ecedo.com*

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

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


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

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

