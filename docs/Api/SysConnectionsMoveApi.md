# Swagger\Client\SysConnectionsMoveApi

All URIs are relative to *https://innova-test.ecedo.com*

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

// Configure API key authorization: Authorization
$config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');
// Configure API key authorization: Ocp-Apim-Subscription-Key
$config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Ocp-Apim-Subscription-Key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Ocp-Apim-Subscription-Key', 'Bearer');

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

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

