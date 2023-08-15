# Swagger\Client\SysInvoiceDataSetsApi

All URIs are relative to *https://innova.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysInvoiceDataSetsGet**](SysInvoiceDataSetsApi.md#sysInvoiceDataSetsGet) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoicetypes/{invoiceType}/invoicedatasets | Verkrijg een geaggregeerde dataset van facturen over een bepaalde periode
[**sysInvoiceDataSetsGetAnyType**](SysInvoiceDataSetsApi.md#sysInvoiceDataSetsGetAnyType) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoicedatasets/{invoiceId} | Verkrijg alle data van een specifieke factuur
[**sysInvoiceDataSetsGetForAdvancePayment**](SysInvoiceDataSetsApi.md#sysInvoiceDataSetsGetForAdvancePayment) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoicedatasets/forAdvancePayment/{invoiceId} | Verkrijg alle data van een voorschotfactuur
[**sysInvoiceDataSetsGetForChargeSessionCredit**](SysInvoiceDataSetsApi.md#sysInvoiceDataSetsGetForChargeSessionCredit) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoicedatasets/forChargeSession/{invoiceId} | Verkrijg alle data van een laadsessies credit
[**sysInvoiceDataSetsGetForCustom**](SysInvoiceDataSetsApi.md#sysInvoiceDataSetsGetForCustom) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoicedatasets/forCustom/{invoiceId} | Verkrijg alle data van een handmatige factuur
[**sysInvoiceDataSetsGetForEvChargeCard**](SysInvoiceDataSetsApi.md#sysInvoiceDataSetsGetForEvChargeCard) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoicedatasets/forEvChargeCard/{invoiceId} | Verkrijg alle data van een laadpasafrekening
[**sysInvoiceDataSetsGetForEvCharger**](SysInvoiceDataSetsApi.md#sysInvoiceDataSetsGetForEvCharger) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoicedatasets/forEvCharger/{invoiceId} | Verkrijg alle data van een laadpaal reimbursement factuur
[**sysInvoiceDataSetsGetForPurchase**](SysInvoiceDataSetsApi.md#sysInvoiceDataSetsGetForPurchase) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoicedatasets/forPurchase/{invoiceId} | Verkrijg alle data van een aanschaffactuur
[**sysInvoiceDataSetsGetForServiceContract**](SysInvoiceDataSetsApi.md#sysInvoiceDataSetsGetForServiceContract) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoicedatasets/forServiceContract/{invoiceId} | Verkrijg alle data van een servicecontractenfactuur
[**sysInvoiceDataSetsGetForSettlement**](SysInvoiceDataSetsApi.md#sysInvoiceDataSetsGetForSettlement) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoicedatasets/forSettlement/{invoiceId} | Verkrijg alle data van een afrekenfactuur


# **sysInvoiceDataSetsGet**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoicesDataSetSummaryDto sysInvoiceDataSetsGet($organization_id, $invoice_type, $start_date, $end_date, $invoice_sub_type)

Verkrijg een geaggregeerde dataset van facturen over een bepaalde periode

__Let op!__ Deze versie ondersteunt enkel `Purchase`-facturen van de subtypes `EnergyPurchase` en `ProducerSettlement`.<br />  All invoices with the requested type and subtype (mandatory when invoiceType = `Purchase`) with the status `Billed` or `Credited` where the invoice period is within the requested Start end EndDate will be selected.<br />  This means for instance when the Requested StartDate = 03-03-2021 and the requested EndDate = 05-05-2021, an invoice with invoice period 01-03-2021 – 01-04-2021 will not be selected but an invoice with period 01-04-2021 – 01-05-2021 will be selected.<br />

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

$apiInstance = new Swagger\Client\Api\SysInvoiceDataSetsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$invoice_type = "invoice_type_example"; // string | Het factuurtype (zie implementatienotities voor de limiteringen)
$start_date = new \DateTime("2013-10-20"); // \DateTime | Startdatum van de selectieperiode
$end_date = new \DateTime("2013-10-20"); // \DateTime | Einddatum van de selectieperiode
$invoice_sub_type = "invoice_sub_type_example"; // string | Het factuursubtype (zie implementatienotities voor de limiteringen)

try {
    $result = $apiInstance->sysInvoiceDataSetsGet($organization_id, $invoice_type, $start_date, $end_date, $invoice_sub_type);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoiceDataSetsApi->sysInvoiceDataSetsGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **invoice_type** | **string**| Het factuurtype (zie implementatienotities voor de limiteringen) |
 **start_date** | **\DateTime**| Startdatum van de selectieperiode |
 **end_date** | **\DateTime**| Einddatum van de selectieperiode |
 **invoice_sub_type** | **string**| Het factuursubtype (zie implementatienotities voor de limiteringen) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoicesDataSetSummaryDto**](../Model/EcedoERPCRMInterfaceApiInvoicesDataSetSummaryDto.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoiceDataSetsGetAnyType**
> \Swagger\Client\Model\EcedoERPCRMInterfaceReportModelOrganizationDto sysInvoiceDataSetsGetAnyType($organization_id, $invoice_id)

Verkrijg alle data van een specifieke factuur

Deze API geeft alle informatie van een specifieke factuur terug die nodig is om een factuur-pdf te maken.<br />  Creditfacturen bevatten geen factuurregels. Voor een overzicht van gecrediteerde regels moet naar de gecrediteerde factuur verwezen worden.<br /><br />  __Let op!__ De inhoud van de response is afhankelijk van het factuurtype van de opgevraagde factuur. Alleen de base-class is hetzelfde. Zie de API's per factuurtype voor de specifieke response-objecten.<br />

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

$apiInstance = new Swagger\Client\Api\SysInvoiceDataSetsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)

try {
    $result = $apiInstance->sysInvoiceDataSetsGetAnyType($organization_id, $invoice_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoiceDataSetsApi->sysInvoiceDataSetsGetAnyType: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **invoice_id** | **string**| Guid van de factuur (Invoice) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceReportModelOrganizationDto**](../Model/EcedoERPCRMInterfaceReportModelOrganizationDto.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoiceDataSetsGetForAdvancePayment**
> \Swagger\Client\Model\EcedoERPCRMInterfaceReportModelAdvancePaymentInvoiceLetterAdvancePaymentInvoiceLetterEnergyDto sysInvoiceDataSetsGetForAdvancePayment($organization_id, $invoice_id)

Verkrijg alle data van een voorschotfactuur

Deze API geeft alle informatie van een specifieke voorschotfactuur/termijnfactuur terug die nodig is om een factuur-pdf te maken.<br />  Creditfacturen bevatten geen factuurregels. Voor een overzicht van gecrediteerde regels moet naar de gecrediteerde factuur verwezen worden.<br /><br />  Er wordt een foutmelding teruggegeven wanneer deze API wordt aangeroepen met de `InvoiceId` van een factuur die geen voorschotfactuur/termijnfactuur (`AdvancePayment`) is.<br />

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

$apiInstance = new Swagger\Client\Api\SysInvoiceDataSetsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)

try {
    $result = $apiInstance->sysInvoiceDataSetsGetForAdvancePayment($organization_id, $invoice_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoiceDataSetsApi->sysInvoiceDataSetsGetForAdvancePayment: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **invoice_id** | **string**| Guid van de factuur (Invoice) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceReportModelAdvancePaymentInvoiceLetterAdvancePaymentInvoiceLetterEnergyDto**](../Model/EcedoERPCRMInterfaceReportModelAdvancePaymentInvoiceLetterAdvancePaymentInvoiceLetterEnergyDto.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoiceDataSetsGetForChargeSessionCredit**
> \Swagger\Client\Model\EcedoERPCRMInterfaceReportModelChargeSessionInvoiceLetterChargeSessionInvoiceLetterDto sysInvoiceDataSetsGetForChargeSessionCredit($organization_id, $invoice_id)

Verkrijg alle data van een laadsessies credit

Deze API geeft alle informatie van een specifieke laadsessies credit terug die nodig is om een factuur-pdf te maken.<br />  Creditfacturen bevatten geen factuurregels. Voor een overzicht van gecrediteerde regels moet naar de gecrediteerde factuur verwezen worden.<br /><br />  Er wordt een foutmelding teruggegeven wanneer deze API wordt aangeroepen met de `InvoiceId` van een factuur die geen \"afrekening laadsessies\" (`ChargeSession`) is.<br />

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

$apiInstance = new Swagger\Client\Api\SysInvoiceDataSetsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)

try {
    $result = $apiInstance->sysInvoiceDataSetsGetForChargeSessionCredit($organization_id, $invoice_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoiceDataSetsApi->sysInvoiceDataSetsGetForChargeSessionCredit: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **invoice_id** | **string**| Guid van de factuur (Invoice) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceReportModelChargeSessionInvoiceLetterChargeSessionInvoiceLetterDto**](../Model/EcedoERPCRMInterfaceReportModelChargeSessionInvoiceLetterChargeSessionInvoiceLetterDto.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoiceDataSetsGetForCustom**
> \Swagger\Client\Model\EcedoERPCRMInterfaceReportModelPurchaseInvoiceLetterPurchaseInvoiceLetterDto sysInvoiceDataSetsGetForCustom($organization_id, $invoice_id)

Verkrijg alle data van een handmatige factuur

Deze API geeft alle informatie van een specifieke handmatige factuur terug die nodig is om een factuur-pdf te maken.<br />  Creditfacturen bevatten geen factuurregels. Voor een overzicht van gecrediteerde regels moet naar de gecrediteerde factuur verwezen worden.<br /><br />  Er wordt een foutmelding teruggegeven wanneer deze API wordt aangeroepen met de `InvoiceId` van een factuur die geen handmatige factuur (`Custom`) is.<br />

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

$apiInstance = new Swagger\Client\Api\SysInvoiceDataSetsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)

try {
    $result = $apiInstance->sysInvoiceDataSetsGetForCustom($organization_id, $invoice_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoiceDataSetsApi->sysInvoiceDataSetsGetForCustom: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **invoice_id** | **string**| Guid van de factuur (Invoice) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceReportModelPurchaseInvoiceLetterPurchaseInvoiceLetterDto**](../Model/EcedoERPCRMInterfaceReportModelPurchaseInvoiceLetterPurchaseInvoiceLetterDto.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoiceDataSetsGetForEvChargeCard**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiChargeSessionInvoiceLetter sysInvoiceDataSetsGetForEvChargeCard($organization_id, $invoice_id)

Verkrijg alle data van een laadpasafrekening

Deze API geeft alle informatie van een specifieke laadpasafrekening terug die nodig is om een factuur-pdf te maken.<br />  Creditfacturen bevatten geen factuurregels. Voor een overzicht van gecrediteerde regels moet naar de gecrediteerde factuur verwezen worden.<br /><br />  Er wordt een foutmelding teruggegeven wanneer deze API wordt aangeroepen met de `InvoiceId` van een factuur die geen \"afrekening laadsessies\" (`ChargeSession`) is.<br />

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

$apiInstance = new Swagger\Client\Api\SysInvoiceDataSetsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)

try {
    $result = $apiInstance->sysInvoiceDataSetsGetForEvChargeCard($organization_id, $invoice_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoiceDataSetsApi->sysInvoiceDataSetsGetForEvChargeCard: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **invoice_id** | **string**| Guid van de factuur (Invoice) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiChargeSessionInvoiceLetter**](../Model/EcedoERPCRMInterfaceApiChargeSessionInvoiceLetter.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoiceDataSetsGetForEvCharger**
> \Swagger\Client\Model\EcedoERPCRMInterfaceReportModelEvChargerReimbursementLetterEvChargerReimbursementInvoiceLetterDto sysInvoiceDataSetsGetForEvCharger($organization_id, $invoice_id)

Verkrijg alle data van een laadpaal reimbursement factuur

Deze API geeft alle informatie van een specifieke laadpaal reimbursement factuur terug die nodig is om een factuur-pdf te maken.<br />  Creditfacturen bevatten geen factuurregels. Voor een overzicht van gecrediteerde regels moet naar de gecrediteerde factuur verwezen worden.<br /><br />  Er wordt een foutmelding teruggegeven wanneer deze API wordt aangeroepen met de `InvoiceId` van een factuur die geen \"afrekening laadsessies\" (`ChargeSession`) is.<br />

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

$apiInstance = new Swagger\Client\Api\SysInvoiceDataSetsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)

try {
    $result = $apiInstance->sysInvoiceDataSetsGetForEvCharger($organization_id, $invoice_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoiceDataSetsApi->sysInvoiceDataSetsGetForEvCharger: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **invoice_id** | **string**| Guid van de factuur (Invoice) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceReportModelEvChargerReimbursementLetterEvChargerReimbursementInvoiceLetterDto**](../Model/EcedoERPCRMInterfaceReportModelEvChargerReimbursementLetterEvChargerReimbursementInvoiceLetterDto.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoiceDataSetsGetForPurchase**
> \Swagger\Client\Model\EcedoERPCRMInterfaceReportModelPurchaseInvoiceLetterPurchaseInvoiceLetterDto sysInvoiceDataSetsGetForPurchase($organization_id, $invoice_id)

Verkrijg alle data van een aanschaffactuur

Deze API geeft alle informatie van een specifieke aanschaffactuur terug die nodig is om een factuur-pdf te maken.<br />  Creditfacturen bevatten geen factuurregels. Voor een overzicht van gecrediteerde regels moet naar de gecrediteerde factuur verwezen worden.<br /><br />  Er wordt een foutmelding teruggegeven wanneer deze API wordt aangeroepen met de `InvoiceId` van een factuur die geen aanschaffactuur (`Purchase`) is.<br />

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

$apiInstance = new Swagger\Client\Api\SysInvoiceDataSetsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)

try {
    $result = $apiInstance->sysInvoiceDataSetsGetForPurchase($organization_id, $invoice_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoiceDataSetsApi->sysInvoiceDataSetsGetForPurchase: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **invoice_id** | **string**| Guid van de factuur (Invoice) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceReportModelPurchaseInvoiceLetterPurchaseInvoiceLetterDto**](../Model/EcedoERPCRMInterfaceReportModelPurchaseInvoiceLetterPurchaseInvoiceLetterDto.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoiceDataSetsGetForServiceContract**
> \Swagger\Client\Model\EcedoERPCRMInterfaceReportModelPurchaseInvoiceLetterServiceContractInvoiceLetterDto sysInvoiceDataSetsGetForServiceContract($organization_id, $invoice_id)

Verkrijg alle data van een servicecontractenfactuur

Deze API geeft alle informatie van een specifieke servicecontractenfactuur terug die nodig is om een factuur-pdf te maken.<br />  Creditfacturen bevatten geen factuurregels. Voor een overzicht van gecrediteerde regels moet naar de gecrediteerde factuur verwezen worden.<br /><br />  Er wordt een foutmelding teruggegeven wanneer deze API wordt aangeroepen met de `InvoiceId` van een factuur die geen \"aankoop\" (`Purchase`) is.<br />

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

$apiInstance = new Swagger\Client\Api\SysInvoiceDataSetsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)

try {
    $result = $apiInstance->sysInvoiceDataSetsGetForServiceContract($organization_id, $invoice_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoiceDataSetsApi->sysInvoiceDataSetsGetForServiceContract: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **invoice_id** | **string**| Guid van de factuur (Invoice) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceReportModelPurchaseInvoiceLetterServiceContractInvoiceLetterDto**](../Model/EcedoERPCRMInterfaceReportModelPurchaseInvoiceLetterServiceContractInvoiceLetterDto.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoiceDataSetsGetForSettlement**
> \Swagger\Client\Model\EcedoERPCRMInterfaceReportModelSettlementInvoiceLetterSettlementInvoiceLetterEnergyDto sysInvoiceDataSetsGetForSettlement($organization_id, $invoice_id)

Verkrijg alle data van een afrekenfactuur

Deze API geeft alle informatie van een specifieke afrekenfactuur terug die nodig is om een factuur-pdf te maken.<br />  Creditfacturen bevatten geen factuurregels. Voor een overzicht van gecrediteerde regels moet naar de gecrediteerde factuur verwezen worden.<br /><br />  Er wordt een foutmelding teruggegeven wanneer deze API wordt aangeroepen met de `InvoiceId` van een factuur die geen afrekenfactuur (`Settlement`) is.<br />

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

$apiInstance = new Swagger\Client\Api\SysInvoiceDataSetsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)

try {
    $result = $apiInstance->sysInvoiceDataSetsGetForSettlement($organization_id, $invoice_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoiceDataSetsApi->sysInvoiceDataSetsGetForSettlement: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **invoice_id** | **string**| Guid van de factuur (Invoice) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceReportModelSettlementInvoiceLetterSettlementInvoiceLetterEnergyDto**](../Model/EcedoERPCRMInterfaceReportModelSettlementInvoiceLetterSettlementInvoiceLetterEnergyDto.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

