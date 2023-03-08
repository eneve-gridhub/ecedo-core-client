# Swagger\Client\SysGdprApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysGdprDelete**](SysGdprApi.md#sysGdprDelete) | **DELETE** /sysapi/v1.0/gdpr/organizations/{organizationId} | Verwijder opgeslagen gegevens van een organization
[**sysGdprGet**](SysGdprApi.md#sysGdprGet) | **GET** /sysapi/v1.0/gdpr/organizations/{organizationId} | Zoek opgeslagen gegevens van een organization


# **sysGdprDelete**
> object sysGdprDelete($organization_id)

Verwijder opgeslagen gegevens van een organization

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysGdprApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 

try {
    $result = $apiInstance->sysGdprDelete($organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysGdprApi->sysGdprDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysGdprGet**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiGdprOrganization sysGdprGet($organization_id)

Zoek opgeslagen gegevens van een organization

De resultset van deze call zal nog uitgebreid worden.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysGdprApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 

try {
    $result = $apiInstance->sysGdprGet($organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysGdprApi->sysGdprGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiGdprOrganization**](../Model/EcedoERPCRMInterfaceApiGdprOrganization.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

