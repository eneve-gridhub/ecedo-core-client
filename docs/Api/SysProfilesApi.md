# Swagger\Client\SysProfilesApi

All URIs are relative to *https://innova-test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysProfilesAddRowsToCustomProfile**](SysProfilesApi.md#sysProfilesAddRowsToCustomProfile) | **POST** /sysapi/v1.0/customprofiles/{profileId}/rows | Voeg profielfracties toe aan een bestaand maatwerkprofiel
[**sysProfilesCreateCustomProfile**](SysProfilesApi.md#sysProfilesCreateCustomProfile) | **POST** /sysapi/v1.0/customprofiles | Aanmaken van een nieuw maatwerkprofiel
[**sysProfilesGetActiveProfiles**](SysProfilesApi.md#sysProfilesGetActiveProfiles) | **GET** /sysapi/v1.0/customprofiles | Haal alle actieve maatwerkprofielen op
[**sysProfilesGetCustomProfile**](SysProfilesApi.md#sysProfilesGetCustomProfile) | **GET** /sysapi/v1.0/customprofiles/{profileId} | Haal een maatwerkprofiel op op basis van een id


# **sysProfilesAddRowsToCustomProfile**
> object sysProfilesAddRowsToCustomProfile($profile_id, $rows)

Voeg profielfracties toe aan een bestaand maatwerkprofiel

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

$apiInstance = new Swagger\Client\Api\SysProfilesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$profile_id = "profile_id_example"; // string | 
$rows = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiCustomProfileRowsPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiCustomProfileRowsPostData | 

try {
    $result = $apiInstance->sysProfilesAddRowsToCustomProfile($profile_id, $rows);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysProfilesApi->sysProfilesAddRowsToCustomProfile: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **string**|  |
 **rows** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiCustomProfileRowsPostData**](../Model/EcedoERPCRMInterfaceApiCustomProfileRowsPostData.md)|  |

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysProfilesCreateCustomProfile**
> string sysProfilesCreateCustomProfile($profile)

Aanmaken van een nieuw maatwerkprofiel

Bij het aanmaken van een prijscurve profiel wordt het eventuele bestaande profiel voor die periode afgesloten.

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

$apiInstance = new Swagger\Client\Api\SysProfilesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$profile = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiCustomProfilePostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiCustomProfilePostData | 

try {
    $result = $apiInstance->sysProfilesCreateCustomProfile($profile);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysProfilesApi->sysProfilesCreateCustomProfile: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiCustomProfilePostData**](../Model/EcedoERPCRMInterfaceApiCustomProfilePostData.md)|  |

### Return type

**string**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysProfilesGetActiveProfiles**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiCustomProfile[] sysProfilesGetActiveProfiles()

Haal alle actieve maatwerkprofielen op

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

$apiInstance = new Swagger\Client\Api\SysProfilesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->sysProfilesGetActiveProfiles();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysProfilesApi->sysProfilesGetActiveProfiles: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiCustomProfile[]**](../Model/EcedoERPCRMInterfaceApiCustomProfile.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysProfilesGetCustomProfile**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiCustomProfile sysProfilesGetCustomProfile($profile_id, $include_rows)

Haal een maatwerkprofiel op op basis van een id

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

$apiInstance = new Swagger\Client\Api\SysProfilesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$profile_id = "profile_id_example"; // string | 
$include_rows = true; // bool | 

try {
    $result = $apiInstance->sysProfilesGetCustomProfile($profile_id, $include_rows);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysProfilesApi->sysProfilesGetCustomProfile: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **string**|  |
 **include_rows** | **bool**|  | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiCustomProfile**](../Model/EcedoERPCRMInterfaceApiCustomProfile.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

