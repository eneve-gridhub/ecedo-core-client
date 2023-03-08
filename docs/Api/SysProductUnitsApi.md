# Swagger\Client\SysProductUnitsApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysProductUnitsGetByOrganizationId**](SysProductUnitsApi.md#sysProductUnitsGetByOrganizationId) | **GET** /sysapi/v1.0/organizations/{organizationId}/productunits | 
[**sysProductUnitsGetByProductUnitId**](SysProductUnitsApi.md#sysProductUnitsGetByProductUnitId) | **GET** /sysapi/v1.0/organizations/{organizationId}/productunits/{productUnitId} | 
[**sysProductUnitsPost**](SysProductUnitsApi.md#sysProductUnitsPost) | **POST** /sysapi/v1.0/organizations/{organizationId}/productunits | Aanmaken van een productUnit voor een specifieke organisatie en product
[**sysProductUnitsPostOrder**](SysProductUnitsApi.md#sysProductUnitsPostOrder) | **POST** /sysapi/v1.0/organizations/{organizationId}/productunits/Order | 
[**sysProductUnitsPostOrderNew**](SysProductUnitsApi.md#sysProductUnitsPostOrderNew) | **POST** /sysapi/v1.0/organizations/{organizationId}/productunits/orderproductunits | 


# **sysProductUnitsGetByOrganizationId**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnit[] sysProductUnitsGetByOrganizationId($organization_id, $cluster_reference, $product_id)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysProductUnitsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$cluster_reference = "cluster_reference_example"; // string | 
$product_id = "product_id_example"; // string | 

try {
    $result = $apiInstance->sysProductUnitsGetByOrganizationId($organization_id, $cluster_reference, $product_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysProductUnitsApi->sysProductUnitsGetByOrganizationId: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **cluster_reference** | **string**|  | [optional]
 **product_id** | [**string**](../Model/.md)|  | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnit[]**](../Model/EcedoERPCRMInterfaceApiProductUnit.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysProductUnitsGetByProductUnitId**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnit sysProductUnitsGetByProductUnitId($organization_id, $product_unit_id)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysProductUnitsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$product_unit_id = "product_unit_id_example"; // string | 

try {
    $result = $apiInstance->sysProductUnitsGetByProductUnitId($organization_id, $product_unit_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysProductUnitsApi->sysProductUnitsGetByProductUnitId: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **product_unit_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnit**](../Model/EcedoERPCRMInterfaceApiProductUnit.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysProductUnitsPost**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnitPostResult sysProductUnitsPost($organization_id, $product_unit_post_data)

Aanmaken van een productUnit voor een specifieke organisatie en product

Wanneer het contract element wordt meegestuurd dan wordt dit contract gekoppeld aan de product unit  Het veld NoOfItems is van toepassing bij een contract waar iets wordt aangeschaft

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysProductUnitsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$product_unit_post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnitPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnitPostData | 

try {
    $result = $apiInstance->sysProductUnitsPost($organization_id, $product_unit_post_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysProductUnitsApi->sysProductUnitsPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **product_unit_post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnitPostData**](../Model/EcedoERPCRMInterfaceApiProductUnitPostData.md)|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnitPostResult**](../Model/EcedoERPCRMInterfaceApiProductUnitPostResult.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysProductUnitsPostOrder**
> object sysProductUnitsPostOrder($organization_id, $product_unit_post_data_list)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysProductUnitsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$product_unit_post_data_list = array(new \Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnitPostData()); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnitPostData[] | 

try {
    $result = $apiInstance->sysProductUnitsPostOrder($organization_id, $product_unit_post_data_list);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysProductUnitsApi->sysProductUnitsPostOrder: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **product_unit_post_data_list** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnitPostData[]**](../Model/EcedoERPCRMInterfaceApiProductUnitPostData.md)|  |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysProductUnitsPostOrderNew**
> object sysProductUnitsPostOrderNew($organization_id, $order)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysProductUnitsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$order = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnitOrderPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnitOrderPostData | 

try {
    $result = $apiInstance->sysProductUnitsPostOrderNew($organization_id, $order);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysProductUnitsApi->sysProductUnitsPostOrderNew: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **order** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiProductUnitOrderPostData**](../Model/EcedoERPCRMInterfaceApiProductUnitOrderPostData.md)|  |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

