# Swagger\Client\SysMeansOfProductionReservationsApi

All URIs are relative to *https://innova.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysMeansOfProductionReservationsGet**](SysMeansOfProductionReservationsApi.md#sysMeansOfProductionReservationsGet) | **GET** /sysapi/v1.0/meansofproductions/{meansOfProductionId}/reservations | Haal reservations op op basis van MeansOfProductionId


# **sysMeansOfProductionReservationsGet**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiReservation[] sysMeansOfProductionReservationsGet($means_of_production_id, $only_active)

Haal reservations op op basis van MeansOfProductionId

Je kan filteren op de actieve contracten

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

$apiInstance = new Swagger\Client\Api\SysMeansOfProductionReservationsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$means_of_production_id = "means_of_production_id_example"; // string | 
$only_active = true; // bool | 

try {
    $result = $apiInstance->sysMeansOfProductionReservationsGet($means_of_production_id, $only_active);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeansOfProductionReservationsApi->sysMeansOfProductionReservationsGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **means_of_production_id** | **string**|  |
 **only_active** | **bool**|  | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiReservation[]**](../Model/EcedoERPCRMInterfaceApiReservation.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

