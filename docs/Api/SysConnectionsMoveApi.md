# Swagger\Client\SysConnectionsMoveApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysConnectionsMoveMove**](SysConnectionsMoveApi.md#sysConnectionsMoveMove) | **POST** /sysapi/v1.0/organizations/{organizationId}/moveconnections | Verhuisflow starten


# **sysConnectionsMoveMove**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiMoveConnectionsConnectionGroupPostResult sysConnectionsMoveMove($organization_id, $connection_group)

Verhuisflow starten

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysConnectionsMoveApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$connection_group = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiMoveConnectionsConnectionGroupPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiMoveConnectionsConnectionGroupPostData | 

try {
    $result = $apiInstance->sysConnectionsMoveMove($organization_id, $connection_group);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysConnectionsMoveApi->sysConnectionsMoveMove: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **connection_group** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMoveConnectionsConnectionGroupPostData**](../Model/EcedoERPCRMInterfaceApiMoveConnectionsConnectionGroupPostData.md)|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMoveConnectionsConnectionGroupPostResult**](../Model/EcedoERPCRMInterfaceApiMoveConnectionsConnectionGroupPostResult.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

