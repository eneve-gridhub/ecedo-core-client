# Swagger\Client\SysPersonsApi

All URIs are relative to *https://innova.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysPersonsDeleteFullPerson**](SysPersonsApi.md#sysPersonsDeleteFullPerson) | **DELETE** /sysapi/v1.0/organizations/{organizationId}/persons/{personId} | Verwijdert een contactpersoon.
[**sysPersonsGetFullPerson**](SysPersonsApi.md#sysPersonsGetFullPerson) | **GET** /sysapi/v1.0/organizations/{organizationId}/persons/{personId} | Vraagt een contactpersoon op.
[**sysPersonsGetFullPersons**](SysPersonsApi.md#sysPersonsGetFullPersons) | **GET** /sysapi/v1.0/organizations/{organizationId}/persons | Vraagt alle contactpersonen op die bij een organisatie horen.
[**sysPersonsGetFullPersonsByInvoice**](SysPersonsApi.md#sysPersonsGetFullPersonsByInvoice) | **GET** /sysapi/v1.0/organizations/{organizationId}/persons/byInvoice/{invoiceId} | Vraagt de contactpersonen op die bij een factuur horen.
[**sysPersonsPostFullPerson**](SysPersonsApi.md#sysPersonsPostFullPerson) | **POST** /sysapi/v1.0/organizations/{organizationId}/persons | Voegt een nieuw contactpersoon toe bij een organisatie.
[**sysPersonsUpdateFullPerson**](SysPersonsApi.md#sysPersonsUpdateFullPerson) | **PUT** /sysapi/v1.0/organizations/{organizationId}/persons/{personId} | Wijzigt een bestaande contactpersoon.


# **sysPersonsDeleteFullPerson**
> sysPersonsDeleteFullPerson($organization_id, $person_id)

Verwijdert een contactpersoon.

Deze API verwijdert een contactpersoon die bij de organisatie hoort. Deze API kan __niet__ de default contactpersoon verwijderen.

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

$apiInstance = new Swagger\Client\Api\SysPersonsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Het id van de organisatie bij wie de contactpersoon hoort
$person_id = "person_id_example"; // string | Het id van de contactpersoon

try {
    $apiInstance->sysPersonsDeleteFullPerson($organization_id, $person_id);
} catch (Exception $e) {
    echo 'Exception when calling SysPersonsApi->sysPersonsDeleteFullPerson: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Het id van de organisatie bij wie de contactpersoon hoort |
 **person_id** | **string**| Het id van de contactpersoon |

### Return type

void (empty response body)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysPersonsGetFullPerson**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiFullPerson sysPersonsGetFullPerson($organization_id, $person_id)

Vraagt een contactpersoon op.

Deze API vraagt één contactpersoon op van een organisatie. Deze API kan ook de default contactpersoon returnen.

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

$apiInstance = new Swagger\Client\Api\SysPersonsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Het id van de organisatie bij wie de contactpersoon hoort
$person_id = "person_id_example"; // string | Het id van de contactpersoon

try {
    $result = $apiInstance->sysPersonsGetFullPerson($organization_id, $person_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPersonsApi->sysPersonsGetFullPerson: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Het id van de organisatie bij wie de contactpersoon hoort |
 **person_id** | **string**| Het id van de contactpersoon |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiFullPerson**](../Model/EcedoERPCRMInterfaceApiFullPerson.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysPersonsGetFullPersons**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiFullPerson[] sysPersonsGetFullPersons($organization_id)

Vraagt alle contactpersonen op die bij een organisatie horen.

Deze API vraagt alle contactpersonen op die bij een organisatie horen.  __Let op!__ Deze API returnt niet de default contactpersoon.

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

$apiInstance = new Swagger\Client\Api\SysPersonsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Het id van de organisatie

try {
    $result = $apiInstance->sysPersonsGetFullPersons($organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPersonsApi->sysPersonsGetFullPersons: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Het id van de organisatie |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiFullPerson[]**](../Model/EcedoERPCRMInterfaceApiFullPerson.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysPersonsGetFullPersonsByInvoice**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiFullPerson[] sysPersonsGetFullPersonsByInvoice($organization_id, $invoice_id)

Vraagt de contactpersonen op die bij een factuur horen.

Deze API vraagt de contactpersonen op die bij een (type) factuur horen.

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

$apiInstance = new Swagger\Client\Api\SysPersonsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Het id van de organisatie bij wie de factuur hoort
$invoice_id = "invoice_id_example"; // string | Het id van de factuur van wie de bijbehorende contactpersonen opgevraagd moeten worden

try {
    $result = $apiInstance->sysPersonsGetFullPersonsByInvoice($organization_id, $invoice_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPersonsApi->sysPersonsGetFullPersonsByInvoice: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Het id van de organisatie bij wie de factuur hoort |
 **invoice_id** | **string**| Het id van de factuur van wie de bijbehorende contactpersonen opgevraagd moeten worden |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiFullPerson[]**](../Model/EcedoERPCRMInterfaceApiFullPerson.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysPersonsPostFullPerson**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiFullPersonPostResult sysPersonsPostFullPerson($person, $organization_id)

Voegt een nieuw contactpersoon toe bij een organisatie.

Deze API voegt een nieuw contactpersoon toe bij een organisatie.

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

$apiInstance = new Swagger\Client\Api\SysPersonsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$person = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiFullPersonPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiFullPersonPostData | De data van de contactpersoon die aangemaakt moet worden
$organization_id = "organization_id_example"; // string | Het id van de organisatie bij wie de contactpersoon hoort

try {
    $result = $apiInstance->sysPersonsPostFullPerson($person, $organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPersonsApi->sysPersonsPostFullPerson: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiFullPersonPostData**](../Model/EcedoERPCRMInterfaceApiFullPersonPostData.md)| De data van de contactpersoon die aangemaakt moet worden |
 **organization_id** | **string**| Het id van de organisatie bij wie de contactpersoon hoort |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiFullPersonPostResult**](../Model/EcedoERPCRMInterfaceApiFullPersonPostResult.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysPersonsUpdateFullPerson**
> sysPersonsUpdateFullPerson($person, $organization_id, $person_id)

Wijzigt een bestaande contactpersoon.

Deze API wijzigt een bestaande contactpersoon. Als je bijvoorbeeld de rollen van de persoon wilt updaten, dan zul je alle rollen die de persoon na de update moet hebben moeten meesturen. Alle niet meegestuurde rollen worden verwijderd.  __Let op!__ Deze API kan niet de default contactpersoon verwijderen.

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

$apiInstance = new Swagger\Client\Api\SysPersonsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$person = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiFullPersonPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiFullPersonPostData | De data die geüpdate moet worden van de contactpersoon
$organization_id = "organization_id_example"; // string | Het id van de organisatie bij wie de contactpersoon hoort
$person_id = "person_id_example"; // string | Het id van de persoon die gewijzigd moet worden

try {
    $apiInstance->sysPersonsUpdateFullPerson($person, $organization_id, $person_id);
} catch (Exception $e) {
    echo 'Exception when calling SysPersonsApi->sysPersonsUpdateFullPerson: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiFullPersonPostData**](../Model/EcedoERPCRMInterfaceApiFullPersonPostData.md)| De data die geüpdate moet worden van de contactpersoon |
 **organization_id** | **string**| Het id van de organisatie bij wie de contactpersoon hoort |
 **person_id** | **string**| Het id van de persoon die gewijzigd moet worden |

### Return type

void (empty response body)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

