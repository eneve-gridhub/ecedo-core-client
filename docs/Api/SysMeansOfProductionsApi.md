# Swagger\Client\SysMeansOfProductionsApi

All URIs are relative to *https://innova-test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysMeansOfProductionsGetAll**](SysMeansOfProductionsApi.md#sysMeansOfProductionsGetAll) | **GET** /sysapi/v1.0/meansofproductions | Opvragen productiemiddelen.
[**sysMeansOfProductionsGetByMeansOfProductionConnectionId**](SysMeansOfProductionsApi.md#sysMeansOfProductionsGetByMeansOfProductionConnectionId) | **GET** /sysapi/v1.0/meansofproductions/{meansOfProductionId}/connections/{meansOfProductionConnectionId} | Opvragen van een productiemiddelaansluiting voor een productiemiddel aan de hand van een productiemiddelaansluiting id
[**sysMeansOfProductionsGetByOrganizationId**](SysMeansOfProductionsApi.md#sysMeansOfProductionsGetByOrganizationId) | **GET** /sysapi/v1.0/organizations/{organizationId}/meansofproductions | Opvragen productiemiddelen van een klant
[**sysMeansOfProductionsGetContractPropsal**](SysMeansOfProductionsApi.md#sysMeansOfProductionsGetContractPropsal) | **GET** /sysapi/v1.0/meansofproductions/{meansOfProductionId}/contractproposal | Genereer een contract voorstel voor een productiemiddel
[**sysMeansOfProductionsGetMeansOfProduction**](SysMeansOfProductionsApi.md#sysMeansOfProductionsGetMeansOfProduction) | **GET** /sysapi/v1.0/organizations/{organizationId}/meansofproductions/{meansOfProductionId} | Opvragen van een productiemiddel aan de hand van het productiemiddel id
[**sysMeansOfProductionsGetMeansOfProductionConnection**](SysMeansOfProductionsApi.md#sysMeansOfProductionsGetMeansOfProductionConnection) | **GET** /sysapi/v1.0/meansofproductionconnections/{meansOfProductionConnectionId} | Opvragen van een productiemiddelaansluiting aan de hand van een productiemiddelaansluiting id
[**sysMeansOfProductionsGetMeansOfProductionConnections**](SysMeansOfProductionsApi.md#sysMeansOfProductionsGetMeansOfProductionConnections) | **GET** /sysapi/v1.0/meansofproductions/{meansOfProductionId}/connections | Opvragen productiemiddelaansluitingen van een klant


# **sysMeansOfProductionsGetAll**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiMeansOfProduction[] sysMeansOfProductionsGetAll()

Opvragen productiemiddelen.

GET https://server/sysapi/v1.0/meansofproductions

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

$apiInstance = new Swagger\Client\Api\SysMeansOfProductionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->sysMeansOfProductionsGetAll();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeansOfProductionsApi->sysMeansOfProductionsGetAll: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeansOfProduction[]**](../Model/EcedoERPCRMInterfaceApiMeansOfProduction.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysMeansOfProductionsGetByMeansOfProductionConnectionId**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiMeansOfProductionConnection sysMeansOfProductionsGetByMeansOfProductionConnectionId($means_of_production_id, $means_of_production_connection_id)

Opvragen van een productiemiddelaansluiting voor een productiemiddel aan de hand van een productiemiddelaansluiting id

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

$apiInstance = new Swagger\Client\Api\SysMeansOfProductionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$means_of_production_id = "means_of_production_id_example"; // string | 
$means_of_production_connection_id = "means_of_production_connection_id_example"; // string | 

try {
    $result = $apiInstance->sysMeansOfProductionsGetByMeansOfProductionConnectionId($means_of_production_id, $means_of_production_connection_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeansOfProductionsApi->sysMeansOfProductionsGetByMeansOfProductionConnectionId: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **means_of_production_id** | **string**|  |
 **means_of_production_connection_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeansOfProductionConnection**](../Model/EcedoERPCRMInterfaceApiMeansOfProductionConnection.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysMeansOfProductionsGetByOrganizationId**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiMeansOfProduction[] sysMeansOfProductionsGetByOrganizationId($organization_id)

Opvragen productiemiddelen van een klant

GET https://server/sysapi/v1.0/meansofproductions

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

$apiInstance = new Swagger\Client\Api\SysMeansOfProductionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 

try {
    $result = $apiInstance->sysMeansOfProductionsGetByOrganizationId($organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeansOfProductionsApi->sysMeansOfProductionsGetByOrganizationId: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeansOfProduction[]**](../Model/EcedoERPCRMInterfaceApiMeansOfProduction.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysMeansOfProductionsGetContractPropsal**
> object sysMeansOfProductionsGetContractPropsal($means_of_production_id)

Genereer een contract voorstel voor een productiemiddel

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

$apiInstance = new Swagger\Client\Api\SysMeansOfProductionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$means_of_production_id = "means_of_production_id_example"; // string | 

try {
    $result = $apiInstance->sysMeansOfProductionsGetContractPropsal($means_of_production_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeansOfProductionsApi->sysMeansOfProductionsGetContractPropsal: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **means_of_production_id** | **string**|  |

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysMeansOfProductionsGetMeansOfProduction**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiMeansOfProduction sysMeansOfProductionsGetMeansOfProduction($organization_id, $means_of_production_id)

Opvragen van een productiemiddel aan de hand van het productiemiddel id

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

$apiInstance = new Swagger\Client\Api\SysMeansOfProductionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$means_of_production_id = "means_of_production_id_example"; // string | 

try {
    $result = $apiInstance->sysMeansOfProductionsGetMeansOfProduction($organization_id, $means_of_production_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeansOfProductionsApi->sysMeansOfProductionsGetMeansOfProduction: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **means_of_production_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeansOfProduction**](../Model/EcedoERPCRMInterfaceApiMeansOfProduction.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysMeansOfProductionsGetMeansOfProductionConnection**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiMeansOfProductionConnection sysMeansOfProductionsGetMeansOfProductionConnection($means_of_production_connection_id)

Opvragen van een productiemiddelaansluiting aan de hand van een productiemiddelaansluiting id

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

$apiInstance = new Swagger\Client\Api\SysMeansOfProductionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$means_of_production_connection_id = "means_of_production_connection_id_example"; // string | 

try {
    $result = $apiInstance->sysMeansOfProductionsGetMeansOfProductionConnection($means_of_production_connection_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeansOfProductionsApi->sysMeansOfProductionsGetMeansOfProductionConnection: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **means_of_production_connection_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeansOfProductionConnection**](../Model/EcedoERPCRMInterfaceApiMeansOfProductionConnection.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysMeansOfProductionsGetMeansOfProductionConnections**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiMeansOfProductionConnection[] sysMeansOfProductionsGetMeansOfProductionConnections($means_of_production_id)

Opvragen productiemiddelaansluitingen van een klant

GET https://server/sysapi/v1.0/meansofproductionconnections

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

$apiInstance = new Swagger\Client\Api\SysMeansOfProductionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$means_of_production_id = "means_of_production_id_example"; // string | 

try {
    $result = $apiInstance->sysMeansOfProductionsGetMeansOfProductionConnections($means_of_production_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeansOfProductionsApi->sysMeansOfProductionsGetMeansOfProductionConnections: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **means_of_production_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeansOfProductionConnection[]**](../Model/EcedoERPCRMInterfaceApiMeansOfProductionConnection.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

