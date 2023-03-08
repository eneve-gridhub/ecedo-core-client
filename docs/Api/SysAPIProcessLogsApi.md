# Swagger\Client\SysAPIProcessLogsApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysAPIProcessLogsPost**](SysAPIProcessLogsApi.md#sysAPIProcessLogsPost) | **POST** /sysapi/v1.0/processlogs | Algemene wijziging insturen


# **sysAPIProcessLogsPost**
> object sysAPIProcessLogsPost($api_process_log)

Algemene wijziging insturen

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysAPIProcessLogsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_process_log = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiAPIProcessLogPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiAPIProcessLogPostData | 

try {
    $result = $apiInstance->sysAPIProcessLogsPost($api_process_log);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysAPIProcessLogsApi->sysAPIProcessLogsPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_process_log** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAPIProcessLogPostData**](../Model/EcedoERPCRMInterfaceApiAPIProcessLogPostData.md)|  |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

