# Swagger\Client\SysPropositionGroupsApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysPropositionGroupsDelete**](SysPropositionGroupsApi.md#sysPropositionGroupsDelete) | **DELETE** /sysapi/v1.0/propositiongroups/{propositionGroupId} | 
[**sysPropositionGroupsGetPropositionGroups**](SysPropositionGroupsApi.md#sysPropositionGroupsGetPropositionGroups) | **GET** /sysapi/v1.0/propositiongroups | Haal alle propositiegroepen op
[**sysPropositionGroupsPost**](SysPropositionGroupsApi.md#sysPropositionGroupsPost) | **POST** /sysapi/v1.0/propositiongroups | Aanmaken van een propositiegroep
[**sysPropositionGroupsPut**](SysPropositionGroupsApi.md#sysPropositionGroupsPut) | **PUT** /sysapi/v1.0/propositiongroups/{propositionGroupId} | 


# **sysPropositionGroupsDelete**
> object sysPropositionGroupsDelete($proposition_group_id)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysPropositionGroupsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$proposition_group_id = "proposition_group_id_example"; // string | 

try {
    $result = $apiInstance->sysPropositionGroupsDelete($proposition_group_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPropositionGroupsApi->sysPropositionGroupsDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposition_group_id** | **string**|  |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysPropositionGroupsGetPropositionGroups**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiPropositionGroup[] sysPropositionGroupsGetPropositionGroups($company_label_id)

Haal alle propositiegroepen op

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysPropositionGroupsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$company_label_id = "company_label_id_example"; // string | Optioneel

try {
    $result = $apiInstance->sysPropositionGroupsGetPropositionGroups($company_label_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPropositionGroupsApi->sysPropositionGroupsGetPropositionGroups: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_label_id** | [**string**](../Model/.md)| Optioneel | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiPropositionGroup[]**](../Model/EcedoERPCRMInterfaceApiPropositionGroup.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysPropositionGroupsPost**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiPropositionGroupPostResult sysPropositionGroupsPost($data)

Aanmaken van een propositiegroep

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysPropositionGroupsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiPropositionGroupPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiPropositionGroupPostData | 

try {
    $result = $apiInstance->sysPropositionGroupsPost($data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPropositionGroupsApi->sysPropositionGroupsPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiPropositionGroupPostData**](../Model/EcedoERPCRMInterfaceApiPropositionGroupPostData.md)|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiPropositionGroupPostResult**](../Model/EcedoERPCRMInterfaceApiPropositionGroupPostResult.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysPropositionGroupsPut**
> object sysPropositionGroupsPut($proposition_group_id, $proposition_group_put_data)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysPropositionGroupsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$proposition_group_id = "proposition_group_id_example"; // string | 
$proposition_group_put_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiPropositionGroupPutData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiPropositionGroupPutData | 

try {
    $result = $apiInstance->sysPropositionGroupsPut($proposition_group_id, $proposition_group_put_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPropositionGroupsApi->sysPropositionGroupsPut: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposition_group_id** | **string**|  |
 **proposition_group_put_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiPropositionGroupPutData**](../Model/EcedoERPCRMInterfaceApiPropositionGroupPutData.md)|  |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

