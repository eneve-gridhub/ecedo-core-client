# Swagger\Client\SysAnnualStandardUsagesApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysAnnualStandardUsagesDeleteExpectedAnnualStandardUsage**](SysAnnualStandardUsagesApi.md#sysAnnualStandardUsagesDeleteExpectedAnnualStandardUsage) | **DELETE** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/expectedannualstandardusages | Verwijderen verwacht jaarverbruik
[**sysAnnualStandardUsagesPostExpectedAnnualStandardUsage**](SysAnnualStandardUsagesApi.md#sysAnnualStandardUsagesPostExpectedAnnualStandardUsage) | **POST** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/expectedannualstandardusages | Aanpassen verwacht jaarverbruik
[**sysAnnualStandardUsagesSetActiveAnnualStandardUsageType**](SysAnnualStandardUsagesApi.md#sysAnnualStandardUsagesSetActiveAnnualStandardUsageType) | **PUT** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/annualstandardusages/setactiveannualstandardusagetype | Aanpassen actief verbruikstype


# **sysAnnualStandardUsagesDeleteExpectedAnnualStandardUsage**
> sysAnnualStandardUsagesDeleteExpectedAnnualStandardUsage($organization_id, $connection_id)

Verwijderen verwacht jaarverbruik

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysAnnualStandardUsagesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$connection_id = "connection_id_example"; // string | 

try {
    $apiInstance->sysAnnualStandardUsagesDeleteExpectedAnnualStandardUsage($organization_id, $connection_id);
} catch (Exception $e) {
    echo 'Exception when calling SysAnnualStandardUsagesApi->sysAnnualStandardUsagesDeleteExpectedAnnualStandardUsage: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **connection_id** | **string**|  |

### Return type

void (empty response body)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysAnnualStandardUsagesPostExpectedAnnualStandardUsage**
> sysAnnualStandardUsagesPostExpectedAnnualStandardUsage($organization_id, $connection_id, $expected_annual_standard_usage)

Aanpassen verwacht jaarverbruik

ExpectedUsageSource: User, Customer, GridOperator, ExternalApplication

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysAnnualStandardUsagesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$connection_id = "connection_id_example"; // string | 
$expected_annual_standard_usage = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiExpectedAnnualStandardUsagePostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiExpectedAnnualStandardUsagePostData | 

try {
    $apiInstance->sysAnnualStandardUsagesPostExpectedAnnualStandardUsage($organization_id, $connection_id, $expected_annual_standard_usage);
} catch (Exception $e) {
    echo 'Exception when calling SysAnnualStandardUsagesApi->sysAnnualStandardUsagesPostExpectedAnnualStandardUsage: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **connection_id** | **string**|  |
 **expected_annual_standard_usage** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiExpectedAnnualStandardUsagePostData**](../Model/EcedoERPCRMInterfaceApiExpectedAnnualStandardUsagePostData.md)|  |

### Return type

void (empty response body)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysAnnualStandardUsagesSetActiveAnnualStandardUsageType**
> sysAnnualStandardUsagesSetActiveAnnualStandardUsageType($organization_id, $connection_id, $set_annual_standard_usage_type_post_data)

Aanpassen actief verbruikstype

ActiveAnnualStandardUsageTypes: SAU, ExpectedSAU

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysAnnualStandardUsagesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$connection_id = "connection_id_example"; // string | 
$set_annual_standard_usage_type_post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiSetAnnualStandardUsageTypePostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiSetAnnualStandardUsageTypePostData | 

try {
    $apiInstance->sysAnnualStandardUsagesSetActiveAnnualStandardUsageType($organization_id, $connection_id, $set_annual_standard_usage_type_post_data);
} catch (Exception $e) {
    echo 'Exception when calling SysAnnualStandardUsagesApi->sysAnnualStandardUsagesSetActiveAnnualStandardUsageType: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **connection_id** | **string**|  |
 **set_annual_standard_usage_type_post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiSetAnnualStandardUsageTypePostData**](../Model/EcedoERPCRMInterfaceApiSetAnnualStandardUsageTypePostData.md)|  |

### Return type

void (empty response body)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

