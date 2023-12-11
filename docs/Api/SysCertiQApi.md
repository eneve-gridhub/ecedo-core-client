# Swagger\Client\SysCertiQApi

All URIs are relative to *https://innova-test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysCertiQGetCurrentCertiQReport**](SysCertiQApi.md#sysCertiQGetCurrentCertiQReport) | **GET** /sysapi/v1.0/certiq/report | Geeft het actuele CertiQ rapport
[**sysCertiQGetMeansOfProductionCertiqDashboardData**](SysCertiQApi.md#sysCertiQGetMeansOfProductionCertiqDashboardData) | **GET** /sysapi/v1.0/organizations/{organizationId}/certiqstatistics | Verkrijg certificaat statistieken
[**sysCertiQGetMeansOfProductionCertiqTransactions**](SysCertiQApi.md#sysCertiQGetMeansOfProductionCertiqTransactions) | **GET** /sysapi/v1.0/organizations/{organizationId}/meansofproductions/{meansOfProductionId}/certiqtransactions | Verkrijg transacties per periode en CertiqEAN


# **sysCertiQGetCurrentCertiQReport**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiCertiQReport[] sysCertiQGetCurrentCertiQReport()

Geeft het actuele CertiQ rapport

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

$apiInstance = new Swagger\Client\Api\SysCertiQApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->sysCertiQGetCurrentCertiQReport();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysCertiQApi->sysCertiQGetCurrentCertiQReport: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiCertiQReport[]**](../Model/EcedoERPCRMInterfaceApiCertiQReport.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysCertiQGetMeansOfProductionCertiqDashboardData**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiMeansOfProductionCertiqDashboardData[] sysCertiQGetMeansOfProductionCertiqDashboardData($organization_id)

Verkrijg certificaat statistieken

Verkrijg certificaat statistieken van CertiqData voor alle productiemiddelen behorend bij een organisatie  Certiq CSV moet geimporteerd zijn

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

$apiInstance = new Swagger\Client\Api\SysCertiQApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 

try {
    $result = $apiInstance->sysCertiQGetMeansOfProductionCertiqDashboardData($organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysCertiQApi->sysCertiQGetMeansOfProductionCertiqDashboardData: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeansOfProductionCertiqDashboardData[]**](../Model/EcedoERPCRMInterfaceApiMeansOfProductionCertiqDashboardData.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysCertiQGetMeansOfProductionCertiqTransactions**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiMeansOfProductionCertiqTransactions sysCertiQGetMeansOfProductionCertiqTransactions($organization_id, $means_of_production_id)

Verkrijg transacties per periode en CertiqEAN



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

$apiInstance = new Swagger\Client\Api\SysCertiQApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$means_of_production_id = "means_of_production_id_example"; // string | 

try {
    $result = $apiInstance->sysCertiQGetMeansOfProductionCertiqTransactions($organization_id, $means_of_production_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysCertiQApi->sysCertiQGetMeansOfProductionCertiqTransactions: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **means_of_production_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeansOfProductionCertiqTransactions**](../Model/EcedoERPCRMInterfaceApiMeansOfProductionCertiqTransactions.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

