# Swagger\Client\SysCustomPriceComponentApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysCustomPriceComponentGetCustomPriceComponents**](SysCustomPriceComponentApi.md#sysCustomPriceComponentGetCustomPriceComponents) | **GET** /sysapi/v1.0/custompricecomponents | Opvragen alle custom price componenten


# **sysCustomPriceComponentGetCustomPriceComponents**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiCustomPriceComponent[] sysCustomPriceComponentGetCustomPriceComponents()

Opvragen alle custom price componenten

Opvragen alle custom price componenten.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysCustomPriceComponentApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->sysCustomPriceComponentGetCustomPriceComponents();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysCustomPriceComponentApi->sysCustomPriceComponentGetCustomPriceComponents: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiCustomPriceComponent[]**](../Model/EcedoERPCRMInterfaceApiCustomPriceComponent.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

