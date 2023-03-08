# Swagger\Client\SysContractPricesApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysContractPricesGet**](SysContractPricesApi.md#sysContractPricesGet) | **GET** /sysapi/v1.0/organizations/{organizationId}/contracts/{contractId}/prices | Opvragen contract prijzen
[**sysContractPricesPost**](SysContractPricesApi.md#sysContractPricesPost) | **POST** /sysapi/v1.0/organizations/{organizationId}/contracts/{contractId}/prices | Toevoegen contract prijzen


# **sysContractPricesGet**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionContractPrices[] sysContractPricesGet($organization_id, $contract_id)

Opvragen contract prijzen

Enkel voor Energiecontracten en Laadpaalcontracten

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractPricesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$contract_id = "contract_id_example"; // string | 

try {
    $result = $apiInstance->sysContractPricesGet($organization_id, $contract_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractPricesApi->sysContractPricesGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **contract_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionContractPrices[]**](../Model/EcedoERPCRMInterfaceApiConnectionContractPrices.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractPricesPost**
> object sysContractPricesPost($organization_id, $contract_id, $prices_post_data)

Toevoegen contract prijzen

Prijzen zijn in EUR  Prijzen standaard excl. BTW tenzij anders aangegeven  Voor elektricteit is de unit kWh; voor Gas prijzen is de unit m3

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractPricesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$contract_id = "contract_id_example"; // string | 
$prices_post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiPricesPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiPricesPostData | 

try {
    $result = $apiInstance->sysContractPricesPost($organization_id, $contract_id, $prices_post_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractPricesApi->sysContractPricesPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **contract_id** | **string**|  |
 **prices_post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiPricesPostData**](../Model/EcedoERPCRMInterfaceApiPricesPostData.md)|  |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

