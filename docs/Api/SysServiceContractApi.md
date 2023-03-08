# Swagger\Client\SysServiceContractApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysServiceContractGetServiceContract**](SysServiceContractApi.md#sysServiceContractGetServiceContract) | **GET** /sysapi/v1.0/organizations/{organizationId}/servicecontracts/{contractId} | 


# **sysServiceContractGetServiceContract**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiEvChargerServiceContractData sysServiceContractGetServiceContract($organization_id, $contract_id)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysServiceContractApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$contract_id = "contract_id_example"; // string | 

try {
    $result = $apiInstance->sysServiceContractGetServiceContract($organization_id, $contract_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysServiceContractApi->sysServiceContractGetServiceContract: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **contract_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiEvChargerServiceContractData**](../Model/EcedoERPCRMInterfaceApiEvChargerServiceContractData.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

