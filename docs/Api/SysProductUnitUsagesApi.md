# Swagger\Client\SysProductUnitUsagesApi

All URIs are relative to *https://innova-test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysProductUnitUsagesDeleteProductUnitUsages**](SysProductUnitUsagesApi.md#sysProductUnitUsagesDeleteProductUnitUsages) | **DELETE** /sysapi/v1.0/productunits/{productUnitId}/usages/startdate/{startDate}/enddate/{endDate} | Verwijderen verbruik/opwek voor productunit
[**sysProductUnitUsagesGetProductUnitUsages**](SysProductUnitUsagesApi.md#sysProductUnitUsagesGetProductUnitUsages) | **GET** /sysapi/v1.0/productunits/{productUnitId}/usages/startdate/{startDate}/enddate/{endDate} | Opvragen verbruik/opwek voor productunit
[**sysProductUnitUsagesPost**](SysProductUnitUsagesApi.md#sysProductUnitUsagesPost) | **POST** /sysapi/v1.0/organizations/{organizationId}/productunits/{productUnitId}/usages | Verbruik van verbruiksproduct insturen


# **sysProductUnitUsagesDeleteProductUnitUsages**
> object sysProductUnitUsagesDeleteProductUnitUsages($product_unit_id, $start_date, $end_date)

Verwijderen verbruik/opwek voor productunit

Verwijderen verbruiksregels

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

$apiInstance = new Swagger\Client\Api\SysProductUnitUsagesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$product_unit_id = "product_unit_id_example"; // string | Guid van de productUnit
$start_date = new \DateTime("2013-10-20"); // \DateTime | begin datum periode in formaat yyyy-mm-dd
$end_date = new \DateTime("2013-10-20"); // \DateTime | einddatum (tot) periode in formaat yyyy-mm-dd

try {
    $result = $apiInstance->sysProductUnitUsagesDeleteProductUnitUsages($product_unit_id, $start_date, $end_date);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysProductUnitUsagesApi->sysProductUnitUsagesDeleteProductUnitUsages: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_unit_id** | **string**| Guid van de productUnit |
 **start_date** | **\DateTime**| begin datum periode in formaat yyyy-mm-dd |
 **end_date** | **\DateTime**| einddatum (tot) periode in formaat yyyy-mm-dd |

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysProductUnitUsagesGetProductUnitUsages**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnitUsageGetData[] sysProductUnitUsagesGetProductUnitUsages($product_unit_id, $start_date, $end_date)

Opvragen verbruik/opwek voor productunit

Opvragen verbruiksregels

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

$apiInstance = new Swagger\Client\Api\SysProductUnitUsagesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$product_unit_id = "product_unit_id_example"; // string | Guid van de productUnit
$start_date = new \DateTime("2013-10-20"); // \DateTime | begin datum opvraag periode in formaat yyyy-mm-dd
$end_date = new \DateTime("2013-10-20"); // \DateTime | einddatum (tot) opvraag periode in formaat yyyy-mm-dd

try {
    $result = $apiInstance->sysProductUnitUsagesGetProductUnitUsages($product_unit_id, $start_date, $end_date);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysProductUnitUsagesApi->sysProductUnitUsagesGetProductUnitUsages: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_unit_id** | **string**| Guid van de productUnit |
 **start_date** | **\DateTime**| begin datum opvraag periode in formaat yyyy-mm-dd |
 **end_date** | **\DateTime**| einddatum (tot) opvraag periode in formaat yyyy-mm-dd |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnitUsageGetData[]**](../Model/EcedoERPCRMInterfaceApiProductUnitUsageGetData.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysProductUnitUsagesPost**
> object sysProductUnitUsagesPost($organization_id, $product_unit_id, $readings)

Verbruik van verbruiksproduct insturen



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

$apiInstance = new Swagger\Client\Api\SysProductUnitUsagesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de organisatie behorend bij de productunit
$product_unit_id = "product_unit_id_example"; // string | Guid van de productunit
$readings = array(new \Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnitUsagePostData()); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnitUsagePostData[] | verbruikdata

try {
    $result = $apiInstance->sysProductUnitUsagesPost($organization_id, $product_unit_id, $readings);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysProductUnitUsagesApi->sysProductUnitUsagesPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de organisatie behorend bij de productunit |
 **product_unit_id** | **string**| Guid van de productunit |
 **readings** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnitUsagePostData[]**](../Model/EcedoERPCRMInterfaceApiProductUnitUsagePostData.md)| verbruikdata |

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

