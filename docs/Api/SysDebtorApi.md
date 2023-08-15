# Swagger\Client\SysDebtorApi

All URIs are relative to *https://innova.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysDebtorDeleteDebtorProperties**](SysDebtorApi.md#sysDebtorDeleteDebtorProperties) | **DELETE** /sysapi/v1.0/organizations/{organizationId}/debtors/{debtorId}/debtorproperties/{debtorProperty} | Verwijder een debiteur-eigenschap
[**sysDebtorGetDebtorProperties**](SysDebtorApi.md#sysDebtorGetDebtorProperties) | **GET** /sysapi/v1.0/organizations/{organizationId}/debtors/{debtorId}/debtorproperties/{debtorProperty} | Ophalen van debiteur-eigenschappen
[**sysDebtorGetOutstandingDebtorAmount**](SysDebtorApi.md#sysDebtorGetOutstandingDebtorAmount) | **GET** /sysapi/v1.0/organizations/{organizationId}/debtors/{debtorId}/outstandingamount | Ophalen van het debiteursaldo uit het financiële systeem
[**sysDebtorPostDebtorProperties**](SysDebtorApi.md#sysDebtorPostDebtorProperties) | **POST** /sysapi/v1.0/organizations/{organizationId}/debtors/{debtorId}/debtorproperties | Instellen van een debiteur-eigenschap


# **sysDebtorDeleteDebtorProperties**
> object sysDebtorDeleteDebtorProperties($organization_id, $debtor_id, $debtor_property)

Verwijder een debiteur-eigenschap

De volgende propertyTypes worden ondersteund:  * AdvancePaymentSchedule

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

$apiInstance = new Swagger\Client\Api\SysDebtorApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$debtor_id = "debtor_id_example"; // string | Guid van de debiteur (Debtor)
$debtor_property = "debtor_property_example"; // string | Guid van de debiteur-eigenschap (DebtorProperty)

try {
    $result = $apiInstance->sysDebtorDeleteDebtorProperties($organization_id, $debtor_id, $debtor_property);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysDebtorApi->sysDebtorDeleteDebtorProperties: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **debtor_id** | **string**| Guid van de debiteur (Debtor) |
 **debtor_property** | **string**| Guid van de debiteur-eigenschap (DebtorProperty) |

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysDebtorGetDebtorProperties**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiDebtorProperty[] sysDebtorGetDebtorProperties($organization_id, $debtor_id, $debtor_property, $include_default)

Ophalen van debiteur-eigenschappen

De volgende propertyTypes worden ondersteund:  * AdvancePaymentSchedule

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

$apiInstance = new Swagger\Client\Api\SysDebtorApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$debtor_id = "debtor_id_example"; // string | Guid van de debiteur (Debtor)
$debtor_property = "debtor_property_example"; // string | Het type van de debiteur-eigenschap
$include_default = true; // bool | Default 'false'. Als 'true' dan wordt als er geen properties zijn of als de eerste property pas start na het begin het resultaat aangevuld met een property die de default systeemwaarde heeft. Deze property is geen echte property en heeft daarom ook geen DebtorPropertyId.

try {
    $result = $apiInstance->sysDebtorGetDebtorProperties($organization_id, $debtor_id, $debtor_property, $include_default);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysDebtorApi->sysDebtorGetDebtorProperties: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **debtor_id** | **string**| Guid van de debiteur (Debtor) |
 **debtor_property** | **string**| Het type van de debiteur-eigenschap |
 **include_default** | **bool**| Default &#39;false&#39;. Als &#39;true&#39; dan wordt als er geen properties zijn of als de eerste property pas start na het begin het resultaat aangevuld met een property die de default systeemwaarde heeft. Deze property is geen echte property en heeft daarom ook geen DebtorPropertyId. | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiDebtorProperty[]**](../Model/EcedoERPCRMInterfaceApiDebtorProperty.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysDebtorGetOutstandingDebtorAmount**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiOutstandingDebtorAmount sysDebtorGetOutstandingDebtorAmount($organization_id, $debtor_id)

Ophalen van het debiteursaldo uit het financiële systeem

Deze API kan alleen gebruikt worden wanneer het geconfigureerde financiële systeem ondersteuning biedt voor deze functionaliteit. Als dit niet het geval is zal een foutmelding worden teruggegeven.<br />

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

$apiInstance = new Swagger\Client\Api\SysDebtorApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$debtor_id = "debtor_id_example"; // string | Guid van de debiteur (Debtor)

try {
    $result = $apiInstance->sysDebtorGetOutstandingDebtorAmount($organization_id, $debtor_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysDebtorApi->sysDebtorGetOutstandingDebtorAmount: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **debtor_id** | **string**| Guid van de debiteur (Debtor) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiOutstandingDebtorAmount**](../Model/EcedoERPCRMInterfaceApiOutstandingDebtorAmount.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysDebtorPostDebtorProperties**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiDebtorPropertyPostResult sysDebtorPostDebtorProperties($organization_id, $debtor_id, $debtor_property)

Instellen van een debiteur-eigenschap

De StartDate van de property moet op of na de laatste property liggen.  De volgende propertyTypes worden ondersteund:  AdvancePaymentSchedule: InMonth en BeforeMonth of Memorial, Fixed en Flexible

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

$apiInstance = new Swagger\Client\Api\SysDebtorApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$debtor_id = "debtor_id_example"; // string | 
$debtor_property = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiDebtorPropertyPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiDebtorPropertyPostData | 

try {
    $result = $apiInstance->sysDebtorPostDebtorProperties($organization_id, $debtor_id, $debtor_property);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysDebtorApi->sysDebtorPostDebtorProperties: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **debtor_id** | **string**|  |
 **debtor_property** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiDebtorPropertyPostData**](../Model/EcedoERPCRMInterfaceApiDebtorPropertyPostData.md)|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiDebtorPropertyPostResult**](../Model/EcedoERPCRMInterfaceApiDebtorPropertyPostResult.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

