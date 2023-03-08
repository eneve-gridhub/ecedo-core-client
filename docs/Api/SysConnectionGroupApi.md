# Swagger\Client\SysConnectionGroupApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysConnectionGroupGet**](SysConnectionGroupApi.md#sysConnectionGroupGet) | **GET** /sysapi/v1.0/organizations/{organizationId}/connectiongroups | 
[**sysConnectionGroupPost**](SysConnectionGroupApi.md#sysConnectionGroupPost) | **POST** /sysapi/v1.0/organizations/{organizationId}/connectiongroups | 
[**sysConnectionGroupPutClusterContractChange**](SysConnectionGroupApi.md#sysConnectionGroupPutClusterContractChange) | **POST** /sysapi/v1.0/organizations/{organizationId}/connectiongroups/{clusterReference}/ClusterContractChange | 


# **sysConnectionGroupGet**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionGroup[] sysConnectionGroupGet($organization_id, $connection_group_type)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysConnectionGroupApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$connection_group_type = "connection_group_type_example"; // string | 

try {
    $result = $apiInstance->sysConnectionGroupGet($organization_id, $connection_group_type);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysConnectionGroupApi->sysConnectionGroupGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **connection_group_type** | **string**|  | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionGroup[]**](../Model/EcedoERPCRMInterfaceApiConnectionGroup.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysConnectionGroupPost**
> object sysConnectionGroupPost($organization_id, $connection_group)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysConnectionGroupApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$connection_group = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionGroupPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionGroupPostData | 

try {
    $result = $apiInstance->sysConnectionGroupPost($organization_id, $connection_group);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysConnectionGroupApi->sysConnectionGroupPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **connection_group** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionGroupPostData**](../Model/EcedoERPCRMInterfaceApiConnectionGroupPostData.md)|  |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysConnectionGroupPutClusterContractChange**
> object sysConnectionGroupPutClusterContractChange($organization_id, $cluster_reference, $post_data)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysConnectionGroupApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$cluster_reference = "cluster_reference_example"; // string | 
$post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionGroupContractChangePostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionGroupContractChangePostData | 

try {
    $result = $apiInstance->sysConnectionGroupPutClusterContractChange($organization_id, $cluster_reference, $post_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysConnectionGroupApi->sysConnectionGroupPutClusterContractChange: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **cluster_reference** | **string**|  |
 **post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionGroupContractChangePostData**](../Model/EcedoERPCRMInterfaceApiConnectionGroupContractChangePostData.md)|  |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

