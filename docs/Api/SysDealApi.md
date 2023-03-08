# Swagger\Client\SysDealApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysDealGet**](SysDealApi.md#sysDealGet) | **GET** /sysapi/v1.0/deals/meansofproductionconnections/{meansOfProductionConnectionId} | Opvragen deals voor meansofproduction aansluitingen


# **sysDealGet**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiDeal[] sysDealGet($means_of_production_connection_id)

Opvragen deals voor meansofproduction aansluitingen

GET https://server/sysapi/v1.0/deals/meansofproductionconnections

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysDealApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$means_of_production_connection_id = "means_of_production_connection_id_example"; // string | 

try {
    $result = $apiInstance->sysDealGet($means_of_production_connection_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysDealApi->sysDealGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **means_of_production_connection_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiDeal[]**](../Model/EcedoERPCRMInterfaceApiDeal.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

