# Swagger\Client\SysEntityRevisionApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysEntityRevisionGetEntityRevisions**](SysEntityRevisionApi.md#sysEntityRevisionGetEntityRevisions) | **GET** /sysapi/v1.0/entityrevisions | Verkrijg Entiteiten die gewijzigd zijn na opgegeven datum


# **sysEntityRevisionGetEntityRevisions**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiOutboundEntityRevision[] sysEntityRevisionGetEntityRevisions($updated_since, $only_push_failures)

Verkrijg Entiteiten die gewijzigd zijn na opgegeven datum

Deze API is bedoeld voor synchronisatie doeleinden met externe systemen

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysEntityRevisionApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$updated_since = new \DateTime("2013-10-20"); // \DateTime | 
$only_push_failures = true; // bool | Als 'true' dan worden alleen de entiteiten opgeleverd waarbij de push niet is gelukt

try {
    $result = $apiInstance->sysEntityRevisionGetEntityRevisions($updated_since, $only_push_failures);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysEntityRevisionApi->sysEntityRevisionGetEntityRevisions: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_since** | **\DateTime**|  |
 **only_push_failures** | **bool**| Als &#39;true&#39; dan worden alleen de entiteiten opgeleverd waarbij de push niet is gelukt | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiOutboundEntityRevision[]**](../Model/EcedoERPCRMInterfaceApiOutboundEntityRevision.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

