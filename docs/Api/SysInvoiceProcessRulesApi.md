# Swagger\Client\SysInvoiceProcessRulesApi

All URIs are relative to *https://innova-test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysInvoiceProcessRulesDeleteInvoiceProcessRule**](SysInvoiceProcessRulesApi.md#sysInvoiceProcessRulesDeleteInvoiceProcessRule) | **DELETE** /sysapi/v1.0/organizations/{organizationId}/invoiceprocessrules/{invoiceProcessRuleId} | Verwijdert een factuurblokkade.
[**sysInvoiceProcessRulesGetInvoiceProcessRules**](SysInvoiceProcessRulesApi.md#sysInvoiceProcessRulesGetInvoiceProcessRules) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoiceprocessrules | Vraagt alle factuurblokkades op die bij een organisatie horen.
[**sysInvoiceProcessRulesGetInvoiceProcessRulesVersionOneDotOne**](SysInvoiceProcessRulesApi.md#sysInvoiceProcessRulesGetInvoiceProcessRulesVersionOneDotOne) | **GET** /sysapi/v1.1/organizations/{organizationId}/invoiceprocessrules | Vraagt alle factuurblokkades op die bij een organisatie horen.
[**sysInvoiceProcessRulesPostInvoiceProcessRule**](SysInvoiceProcessRulesApi.md#sysInvoiceProcessRulesPostInvoiceProcessRule) | **POST** /sysapi/v1.0/organizations/{organizationId}/invoiceprocessrules | Voegt een nieuwe factuurblokkade toe bij een organisatie.
[**sysInvoiceProcessRulesPostInvoiceProcessRuleVersionOneDotOne**](SysInvoiceProcessRulesApi.md#sysInvoiceProcessRulesPostInvoiceProcessRuleVersionOneDotOne) | **POST** /sysapi/v1.1/organizations/{organizationId}/invoiceprocessrules | Voegt een nieuwe factuurblokkade toe bij een organisatie.


# **sysInvoiceProcessRulesDeleteInvoiceProcessRule**
> sysInvoiceProcessRulesDeleteInvoiceProcessRule($organization_id, $invoice_process_rule_id)

Verwijdert een factuurblokkade.

Deze API verwijdert een factuurblokkade die bij de organisatie hoort. <br />  Facturen die al zijn uitgevallen vanwege de verwijderde blokkade zullen niet automatisch verder gaan. Deze validatieuitval moet eerst goedgekeurd worden door een gebruiker.<br />

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

$apiInstance = new Swagger\Client\Api\SysInvoiceProcessRulesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$invoice_process_rule_id = "invoice_process_rule_id_example"; // string | Guid van de factuurblokkade (InvoiceProcessRule)

try {
    $apiInstance->sysInvoiceProcessRulesDeleteInvoiceProcessRule($organization_id, $invoice_process_rule_id);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoiceProcessRulesApi->sysInvoiceProcessRulesDeleteInvoiceProcessRule: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **invoice_process_rule_id** | **string**| Guid van de factuurblokkade (InvoiceProcessRule) |

### Return type

void (empty response body)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoiceProcessRulesGetInvoiceProcessRules**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceProcessRule[] sysInvoiceProcessRulesGetInvoiceProcessRules($organization_id, $invoice_type, $invoice_sub_type, $cluster_reference, $company_label_id)

Vraagt alle factuurblokkades op die bij een organisatie horen.

Deze API vraagt alle factuurblokkades op die bij een organisatie horen.    Hierbij wordt gefiltered op enkel 'Valideer factuur' blokkeertype. Gebruik V1.1 om expliciet te kunnen filteren op het blokkeertype.

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

$apiInstance = new Swagger\Client\Api\SysInvoiceProcessRulesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Het id van de organisatie
$invoice_type = "invoice_type_example"; // string | Optionele invoice type
$invoice_sub_type = "invoice_sub_type_example"; // string | Optionele invoice sub type
$cluster_reference = "cluster_reference_example"; // string | Optionele cluster referentie
$company_label_id = "company_label_id_example"; // string | Optionele company label

try {
    $result = $apiInstance->sysInvoiceProcessRulesGetInvoiceProcessRules($organization_id, $invoice_type, $invoice_sub_type, $cluster_reference, $company_label_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoiceProcessRulesApi->sysInvoiceProcessRulesGetInvoiceProcessRules: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Het id van de organisatie |
 **invoice_type** | **string**| Optionele invoice type | [optional]
 **invoice_sub_type** | **string**| Optionele invoice sub type | [optional]
 **cluster_reference** | **string**| Optionele cluster referentie | [optional]
 **company_label_id** | [**string**](../Model/.md)| Optionele company label | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceProcessRule[]**](../Model/EcedoERPCRMInterfaceApiInvoiceProcessRule.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoiceProcessRulesGetInvoiceProcessRulesVersionOneDotOne**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceProcessRule[] sysInvoiceProcessRulesGetInvoiceProcessRulesVersionOneDotOne($organization_id, $invoice_type, $invoice_sub_type, $cluster_reference, $company_label_id, $block_type)

Vraagt alle factuurblokkades op die bij een organisatie horen.

Deze API vraagt alle factuurblokkades op die bij een organisatie horen.

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

$apiInstance = new Swagger\Client\Api\SysInvoiceProcessRulesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Het id van de organisatie
$invoice_type = "invoice_type_example"; // string | Optionele invoice type
$invoice_sub_type = "invoice_sub_type_example"; // string | Optionele invoice sub type
$cluster_reference = "cluster_reference_example"; // string | Optionele cluster referentie
$company_label_id = "company_label_id_example"; // string | Optionele company label
$block_type = "block_type_example"; // string | Optionele block type

try {
    $result = $apiInstance->sysInvoiceProcessRulesGetInvoiceProcessRulesVersionOneDotOne($organization_id, $invoice_type, $invoice_sub_type, $cluster_reference, $company_label_id, $block_type);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoiceProcessRulesApi->sysInvoiceProcessRulesGetInvoiceProcessRulesVersionOneDotOne: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Het id van de organisatie |
 **invoice_type** | **string**| Optionele invoice type | [optional]
 **invoice_sub_type** | **string**| Optionele invoice sub type | [optional]
 **cluster_reference** | **string**| Optionele cluster referentie | [optional]
 **company_label_id** | [**string**](../Model/.md)| Optionele company label | [optional]
 **block_type** | **string**| Optionele block type | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceProcessRule[]**](../Model/EcedoERPCRMInterfaceApiInvoiceProcessRule.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoiceProcessRulesPostInvoiceProcessRule**
> object sysInvoiceProcessRulesPostInvoiceProcessRule($process_rule, $organization_id)

Voegt een nieuwe factuurblokkade toe bij een organisatie.

Deze API voegt een nieuw factuurblokkade toe bij een organisatie.    Niet alle combinaties van `InvoiceType` en `InvoiceSubType` zijn mogelijk. Dit is afhankelijk van de productgroepen behorende bij een klant.  Verder moet een `BlockReason` uniek zijn per `InvoiceType` en `ClusterReference`     De `BlockType` wordt standaard gezet op 'Validation' indien er geen expliciete waarde meegegeven wordt.

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

$apiInstance = new Swagger\Client\Api\SysInvoiceProcessRulesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$process_rule = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceProcessRulePostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceProcessRulePostData | 
$organization_id = "organization_id_example"; // string | Het id van de organisatie bij wie de factuurblokkade hoort

try {
    $result = $apiInstance->sysInvoiceProcessRulesPostInvoiceProcessRule($process_rule, $organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoiceProcessRulesApi->sysInvoiceProcessRulesPostInvoiceProcessRule: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_rule** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceProcessRulePostData**](../Model/EcedoERPCRMInterfaceApiInvoiceProcessRulePostData.md)|  |
 **organization_id** | **string**| Het id van de organisatie bij wie de factuurblokkade hoort |

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoiceProcessRulesPostInvoiceProcessRuleVersionOneDotOne**
> object sysInvoiceProcessRulesPostInvoiceProcessRuleVersionOneDotOne($process_rule, $organization_id)

Voegt een nieuwe factuurblokkade toe bij een organisatie.

Deze API voegt een nieuw factuurblokkade toe bij een organisatie.    Niet alle combinaties van `InvoiceType` en `InvoiceSubType` zijn mogelijk. Dit is afhankelijk van de productgroepen behorende bij een klant.  Verder moet een `BlockReason` uniek zijn per `InvoiceType` en `ClusterReference`. Ook is het verplicht een blockType mee te geven.

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

$apiInstance = new Swagger\Client\Api\SysInvoiceProcessRulesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$process_rule = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceProcessRulePostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceProcessRulePostData | 
$organization_id = "organization_id_example"; // string | Het id van de organisatie bij wie de factuurblokkade hoort

try {
    $result = $apiInstance->sysInvoiceProcessRulesPostInvoiceProcessRuleVersionOneDotOne($process_rule, $organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoiceProcessRulesApi->sysInvoiceProcessRulesPostInvoiceProcessRuleVersionOneDotOne: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_rule** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceProcessRulePostData**](../Model/EcedoERPCRMInterfaceApiInvoiceProcessRulePostData.md)|  |
 **organization_id** | **string**| Het id van de organisatie bij wie de factuurblokkade hoort |

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

