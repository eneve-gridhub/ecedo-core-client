# Swagger\Client\SysRepresentativeApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysRepresentativeDelete**](SysRepresentativeApi.md#sysRepresentativeDelete) | **DELETE** /sysapi/v1.0/representatives/{representativeId} | Verwijderen van een verkoper
[**sysRepresentativeGet**](SysRepresentativeApi.md#sysRepresentativeGet) | **GET** /sysapi/v1.0/representatives | Opvragen verkopers
[**sysRepresentativePost**](SysRepresentativeApi.md#sysRepresentativePost) | **POST** /sysapi/v1.0/representatives | Aanmaken van een verkoper
[**sysRepresentativePut**](SysRepresentativeApi.md#sysRepresentativePut) | **PUT** /sysapi/v1.0/representatives/{representativeId} | Wijzigen van een verkoper


# **sysRepresentativeDelete**
> object sysRepresentativeDelete($representative_id)

Verwijderen van een verkoper

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysRepresentativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$representative_id = "representative_id_example"; // string | 

try {
    $result = $apiInstance->sysRepresentativeDelete($representative_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysRepresentativeApi->sysRepresentativeDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **representative_id** | **string**|  |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysRepresentativeGet**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiRepresentative[] sysRepresentativeGet()

Opvragen verkopers

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysRepresentativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->sysRepresentativeGet();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysRepresentativeApi->sysRepresentativeGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiRepresentative[]**](../Model/EcedoERPCRMInterfaceApiRepresentative.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysRepresentativePost**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiRepresentativePostResult sysRepresentativePost($representative)

Aanmaken van een verkoper

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysRepresentativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$representative = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiRepresentativePostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiRepresentativePostData | 

try {
    $result = $apiInstance->sysRepresentativePost($representative);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysRepresentativeApi->sysRepresentativePost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **representative** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiRepresentativePostData**](../Model/EcedoERPCRMInterfaceApiRepresentativePostData.md)|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiRepresentativePostResult**](../Model/EcedoERPCRMInterfaceApiRepresentativePostResult.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysRepresentativePut**
> object sysRepresentativePut($representative_id, $representative)

Wijzigen van een verkoper

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysRepresentativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$representative_id = "representative_id_example"; // string | 
$representative = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiRepresentativePutData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiRepresentativePutData | 

try {
    $result = $apiInstance->sysRepresentativePut($representative_id, $representative);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysRepresentativeApi->sysRepresentativePut: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **representative_id** | **string**|  |
 **representative** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiRepresentativePutData**](../Model/EcedoERPCRMInterfaceApiRepresentativePutData.md)|  |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

