# Swagger\Client\SysMeansOfProductionExpectedYieldApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysMeansOfProductionExpectedYieldGet**](SysMeansOfProductionExpectedYieldApi.md#sysMeansOfProductionExpectedYieldGet) | **GET** /sysapi/v1.0/meansofproductionexpectedyield/{meansOfProductionId} | Verkrijg verwacht af te rekenen verbruik en aantal contracten op basis van MeansOfProductionId


# **sysMeansOfProductionExpectedYieldGet**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiExpectedYield[] sysMeansOfProductionExpectedYieldGet($means_of_production_id)

Verkrijg verwacht af te rekenen verbruik en aantal contracten op basis van MeansOfProductionId

Het verbruik wordt bepaald op basis van het voorschot van klanten die een meeliftpropositie hebben voor betreffend productiemiddel  Het aantal aantal dat geretourneerd wordt betreft het aantal geldige contracten voor betreffende productiemiddel  Als peil datum wordt de huidige datum gebruikt

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysMeansOfProductionExpectedYieldApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$means_of_production_id = "means_of_production_id_example"; // string | 

try {
    $result = $apiInstance->sysMeansOfProductionExpectedYieldGet($means_of_production_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeansOfProductionExpectedYieldApi->sysMeansOfProductionExpectedYieldGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **means_of_production_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiExpectedYield[]**](../Model/EcedoERPCRMInterfaceApiExpectedYield.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

