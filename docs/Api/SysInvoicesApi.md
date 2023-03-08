# Swagger\Client\SysInvoicesApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysInvoicesAddInvoiceRows**](SysInvoicesApi.md#sysInvoicesAddInvoiceRows) | **POST** /sysapi/v1.0/organizations/{organizationId}/invoices/{invoiceId}/invoicerows | Toevoegen factuurregels aan een factuur
[**sysInvoicesByNumber**](SysInvoicesApi.md#sysInvoicesByNumber) | **GET** /sysapi/v1.0/invoices/bynumber/{invoiceNumber} | Haal een specifieke factuur op (op basis van factuurnummer)
[**sysInvoicesCalculateExpectedSettlementInvoice**](SysInvoicesApi.md#sysInvoicesCalculateExpectedSettlementInvoice) | **POST** /sysapi/v1.0/organizations/{organizationId}/invoices/calculateexpectedsettlement | Berekend en haalt de verwachte jaarafrekening voor een specifiek cluster op
[**sysInvoicesCredit**](SysInvoicesApi.md#sysInvoicesCredit) | **POST** /sysapi/v1.0/organizations/{organizationId}/invoices/{invoiceId}/credit | Voorschot-, borg- of afrekenfactuur crediteren
[**sysInvoicesDownloadRemitReport**](SysInvoicesApi.md#sysInvoicesDownloadRemitReport) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoices/{invoiceId}/downloadremitreport | Download Remit Report voor een factuur
[**sysInvoicesDownloadSingleInvoice**](SysInvoicesApi.md#sysInvoicesDownloadSingleInvoice) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoices/{invoiceId}/download | Download factuurdocument van een specifieke factuur
[**sysInvoicesGet**](SysInvoicesApi.md#sysInvoicesGet) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoices | Haal facturen van een specifieke klant op (op basis van InvoiceId)
[**sysInvoicesGetInvoice**](SysInvoicesApi.md#sysInvoicesGetInvoice) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoices/{invoiceId} | Haal een specifieke factuur op
[**sysInvoicesGetInvoiceReason**](SysInvoicesApi.md#sysInvoicesGetInvoiceReason) | **GET** /sysapi/v1.0/invoices/{invoiceId}/invoicereason | Vraag de reden op waarom de factuur is aangemaakt
[**sysInvoicesGetInvoicesByCompany**](SysInvoicesApi.md#sysInvoicesGetInvoicesByCompany) | **GET** /sysapi/v1.0/invoices/afternumber/{invoiceNumber} | Haal facturen van een een specifieke label op, met factuurnummers hoger dan het meegegeven factuurnummer&lt;br&gt;&lt;/br&gt;  Fetch invoices with invoice number greater than \&quot;invoiceNumber\&quot; for a company label: \&quot;companyLabelId\&quot;&lt;br&gt;&lt;/br&gt;      Maximum of 1000 records are returned. Additional calls are needed if more than 1000 records are returned
[**sysInvoicesGetInvoicesWithPrettySmaUsages**](SysInvoicesApi.md#sysInvoicesGetInvoicesWithPrettySmaUsages) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoices/{invoiceId}/prettyinvoiceusages | Haal verbruiksregels van een factuur op
[**sysInvoicesGetInvoicesWithSmaUsages**](SysInvoicesApi.md#sysInvoicesGetInvoicesWithSmaUsages) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoices/{invoiceId}/invoiceusages | Haal verbruiksregels van een factuur op
[**sysInvoicesGetInvoicesWithSmaUsagesV11**](SysInvoicesApi.md#sysInvoicesGetInvoicesWithSmaUsagesV11) | **GET** /sysapi/v1.1/organizations/{organizationId}/invoices/{invoiceId}/invoiceusages | Haal verbruiksregels van een factuur op


# **sysInvoicesAddInvoiceRows**
> sysInvoicesAddInvoiceRows($organization_id, $invoice_id, $post_data)

Toevoegen factuurregels aan een factuur

Ondersteunde producten:  * ElektriciteitMeelift: 10E8EF99-2EA1-4F20-B256-A2D300E260E5  * GasMeelift: 3E6CB93A-6650-4B13-B863-C8DC871C7260  * ElektriciteitKleinverbruik: 962d8c69-7403-494e-b772-a0ac011a9d00  * GasKleinverbruik: 60bc826c-aa9a-4279-b6ac-a0ac011ab7d0  * ElektriciteitGrootverbruik: 5CA64903-8345-4DBF-8E88-A1BD013E690A  * GasGrootverbruik: 55B3FB1C-DD2D-4AED-A536-FBEBF9B08381  * ExterneOpwekWind: B156E122-CA1A-4FA7-AAC9-A3FE0114A7BB  * ExterneOpwekZon: 78B56301-D77C-4BAA-AED4-A4A400DC6DBC  * ElektriciteitTankKaart: 6B1B6762-5F28-4EC1-841D-A5E500C89D6B    Let op! Combinatie van CustomPriceComponentId en PriceComponentType in een regel niet toegestaan. 1 van beide moet worden ingestuurd.    Let op! Niet alle PriceComponentTypes kunnen worden toegevoegd.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysInvoicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)
$post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceRowsPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceRowsPostData | 

try {
    $apiInstance->sysInvoicesAddInvoiceRows($organization_id, $invoice_id, $post_data);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoicesApi->sysInvoicesAddInvoiceRows: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **invoice_id** | **string**| Guid van de factuur (Invoice) |
 **post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceRowsPostData**](../Model/EcedoERPCRMInterfaceApiInvoiceRowsPostData.md)|  |

### Return type

void (empty response body)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoicesByNumber**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoice sysInvoicesByNumber($invoice_number, $include_documents, $include_child_invoice_ids, $include_corrected_invoice_ids, $company_label_id)

Haal een specifieke factuur op (op basis van factuurnummer)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysInvoicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$invoice_number = "invoice_number_example"; // string | Het factuurnummer
$include_documents = true; // bool | Optionele parameter (default false) waardoor het response-object voorzien kan worden van `InvoiceDocuments`
$include_child_invoice_ids = true; // bool | Optionele parameter (default false) waardoor het response-object van verzamelfacturen voorzien kan worden van `ChildInvoiceIds`
$include_corrected_invoice_ids = true; // bool | Optionele parameter (default false) waardoor het response-object voorzien kan worden van `CorrectedInvoiceIds`
$company_label_id = "company_label_id_example"; // string | Optionele parameter (default null) waarmee de factuur horende bij een specifieke Label opgehaald kan worden

try {
    $result = $apiInstance->sysInvoicesByNumber($invoice_number, $include_documents, $include_child_invoice_ids, $include_corrected_invoice_ids, $company_label_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoicesApi->sysInvoicesByNumber: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_number** | **string**| Het factuurnummer |
 **include_documents** | **bool**| Optionele parameter (default false) waardoor het response-object voorzien kan worden van &#x60;InvoiceDocuments&#x60; | [optional]
 **include_child_invoice_ids** | **bool**| Optionele parameter (default false) waardoor het response-object van verzamelfacturen voorzien kan worden van &#x60;ChildInvoiceIds&#x60; | [optional]
 **include_corrected_invoice_ids** | **bool**| Optionele parameter (default false) waardoor het response-object voorzien kan worden van &#x60;CorrectedInvoiceIds&#x60; | [optional]
 **company_label_id** | [**string**](../Model/.md)| Optionele parameter (default null) waarmee de factuur horende bij een specifieke Label opgehaald kan worden | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoice**](../Model/EcedoERPCRMInterfaceApiInvoice.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoicesCalculateExpectedSettlementInvoice**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiExpectedSettlementInvoiceResult sysInvoicesCalculateExpectedSettlementInvoice($organization_id, $expected_invoice_post_data)

Berekend en haalt de verwachte jaarafrekening voor een specifiek cluster op

Voor alle aansluitingen in het cluster moeten er SJV gegevens worden meegestuurd  Voor Gas aansluitingen wordt het veld SingleUsage gebruikt en bij Elektriciteit aansluitingen zijn dit de velden PeakUsage, OffPeakUsage, PeakUsageODN en OffPeakUsageODN

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysInvoicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$expected_invoice_post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiExpectedSettlementInvoicePostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiExpectedSettlementInvoicePostData | 

try {
    $result = $apiInstance->sysInvoicesCalculateExpectedSettlementInvoice($organization_id, $expected_invoice_post_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoicesApi->sysInvoicesCalculateExpectedSettlementInvoice: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **expected_invoice_post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiExpectedSettlementInvoicePostData**](../Model/EcedoERPCRMInterfaceApiExpectedSettlementInvoicePostData.md)|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiExpectedSettlementInvoiceResult**](../Model/EcedoERPCRMInterfaceApiExpectedSettlementInvoiceResult.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoicesCredit**
> object sysInvoicesCredit($invoice_id, $organization_id, $invoice_post_data)

Voorschot-, borg- of afrekenfactuur crediteren

Crediteer voorschot-, afreken- of borgfactuur. De velden 'DoComplete', 'CreateNewAdvancePayment' en 'NewAdvancePayment' zijn alleen van toepassing bij het crediteren van een voorschotfactuur

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysInvoicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$invoice_post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiCreditInvoicePostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiCreditInvoicePostData | De request-body, zie het object-model voor meer informatie

try {
    $result = $apiInstance->sysInvoicesCredit($invoice_id, $organization_id, $invoice_post_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoicesApi->sysInvoicesCredit: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **string**| Guid van de factuur (Invoice) |
 **organization_id** | **string**| Guid van de klant (Organization) |
 **invoice_post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiCreditInvoicePostData**](../Model/EcedoERPCRMInterfaceApiCreditInvoicePostData.md)| De request-body, zie het object-model voor meer informatie |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoicesDownloadRemitReport**
> object sysInvoicesDownloadRemitReport($organization_id, $invoice_id)

Download Remit Report voor een factuur

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysInvoicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)

try {
    $result = $apiInstance->sysInvoicesDownloadRemitReport($organization_id, $invoice_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoicesApi->sysInvoicesDownloadRemitReport: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **invoice_id** | **string**| Guid van de factuur (Invoice) |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoicesDownloadSingleInvoice**
> object sysInvoicesDownloadSingleInvoice($invoice_id, $organization_id, $document_type)

Download factuurdocument van een specifieke factuur

Met behulp van deze API kunnen factuurdocumenten van een factuur gedownload worden.<br />  Reguliere facturen hebben één document, waardoor het niet verplicht is om de query parameter `documentType` in te vullen. Als een factuur één document heeft zal dat document teruggegeven worden.<br />  Sommige facturen (op moment van schrijven alleen verzamelfacturen) bevatten echter meerdere documenten. In dat geval zal de API een foutmelding teruggeven omdat niet bekend is welke van deze documenten teruggegeven moet worden.<br />

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysInvoicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$document_type = "document_type_example"; // string | Optioneel documenttype (default leeg) waarmee geforceerd kan worden welk document wordt teruggegeven

try {
    $result = $apiInstance->sysInvoicesDownloadSingleInvoice($invoice_id, $organization_id, $document_type);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoicesApi->sysInvoicesDownloadSingleInvoice: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **string**| Guid van de factuur (Invoice) |
 **organization_id** | **string**| Guid van de klant (Organization) |
 **document_type** | **string**| Optioneel documenttype (default leeg) waarmee geforceerd kan worden welk document wordt teruggegeven | [optional]

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoicesGet**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoice[] sysInvoicesGet($organization_id, $only_complete, $include_documents)

Haal facturen van een specifieke klant op (op basis van InvoiceId)

Opvragen facturen van een klant. De velden \"IsOLEV\", \"SettlementInvoiceFrequency\" en \"SettlementInvoiceFrequencyLocalized\" worden alleen gevuld voor afrekenfacturen energielevering.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysInvoicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$only_complete = true; // bool | Optionele parameter (default true) waarmee woorkomen kan worden dat facturen die nog in een workflow zitten worden geretourneerd
$include_documents = true; // bool | Optionele parameter (default false) waardoor het response-object voorzien kan worden `InvoiceDocuments`

try {
    $result = $apiInstance->sysInvoicesGet($organization_id, $only_complete, $include_documents);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoicesApi->sysInvoicesGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **only_complete** | **bool**| Optionele parameter (default true) waarmee woorkomen kan worden dat facturen die nog in een workflow zitten worden geretourneerd | [optional]
 **include_documents** | **bool**| Optionele parameter (default false) waardoor het response-object voorzien kan worden &#x60;InvoiceDocuments&#x60; | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoice[]**](../Model/EcedoERPCRMInterfaceApiInvoice.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoicesGetInvoice**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoice sysInvoicesGetInvoice($invoice_id, $organization_id, $include_documents, $include_child_invoice_ids, $include_corrected_invoice_ids)

Haal een specifieke factuur op

Opvragen factuurdetails. De velden \"IsOLEV\", \"SettlementInvoiceFrequency\" en \"SettlementInvoiceFrequencyLocalized\" worden alleen gevuld voor afrekenfacturen energielevering.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysInvoicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$include_documents = true; // bool | Optionele parameter (default false) waardoor het response-object voorzien kan worden van `InvoiceDocuments`
$include_child_invoice_ids = true; // bool | Optionele parameter (default false) waardoor het response-object van verzamelfacturen voorzien kan worden van `ChildInvoiceIds`
$include_corrected_invoice_ids = true; // bool | Optionele parameter (default false) waardoor het response-object voorzien kan worden van `CorrectedInvoiceIds`

try {
    $result = $apiInstance->sysInvoicesGetInvoice($invoice_id, $organization_id, $include_documents, $include_child_invoice_ids, $include_corrected_invoice_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoicesApi->sysInvoicesGetInvoice: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **string**| Guid van de factuur (Invoice) |
 **organization_id** | **string**| Guid van de klant (Organization) |
 **include_documents** | **bool**| Optionele parameter (default false) waardoor het response-object voorzien kan worden van &#x60;InvoiceDocuments&#x60; | [optional]
 **include_child_invoice_ids** | **bool**| Optionele parameter (default false) waardoor het response-object van verzamelfacturen voorzien kan worden van &#x60;ChildInvoiceIds&#x60; | [optional]
 **include_corrected_invoice_ids** | **bool**| Optionele parameter (default false) waardoor het response-object voorzien kan worden van &#x60;CorrectedInvoiceIds&#x60; | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoice**](../Model/EcedoERPCRMInterfaceApiInvoice.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoicesGetInvoiceReason**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceReasonResult sysInvoicesGetInvoiceReason($invoice_id)

Vraag de reden op waarom de factuur is aangemaakt

Let op: het bepalen van de reden van een eindafrekenfactuur is niet waterdicht. Hier worden bepaalde aannames gedaan en het kan zijn dat een eindafrekening nav. een verhuizing of nav. een einde levering als reguliere eindafrekening wordt gezien.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysInvoicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)

try {
    $result = $apiInstance->sysInvoicesGetInvoiceReason($invoice_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoicesApi->sysInvoicesGetInvoiceReason: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **string**| Guid van de factuur (Invoice) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceReasonResult**](../Model/EcedoERPCRMInterfaceApiInvoiceReasonResult.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoicesGetInvoicesByCompany**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoice[] sysInvoicesGetInvoicesByCompany($invoice_number, $company_label_id)

Haal facturen van een een specifieke label op, met factuurnummers hoger dan het meegegeven factuurnummer<br></br>  Fetch invoices with invoice number greater than \"invoiceNumber\" for a company label: \"companyLabelId\"<br></br>      Maximum of 1000 records are returned. Additional calls are needed if more than 1000 records are returned

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysInvoicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$invoice_number = 789; // int | invoice number
$company_label_id = "company_label_id_example"; // string | Voor nu verplichte parameter waarmee de factuur horende bij een specifieke Label opgehaald kan worden

try {
    $result = $apiInstance->sysInvoicesGetInvoicesByCompany($invoice_number, $company_label_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoicesApi->sysInvoicesGetInvoicesByCompany: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_number** | **int**| invoice number |
 **company_label_id** | [**string**](../Model/.md)| Voor nu verplichte parameter waarmee de factuur horende bij een specifieke Label opgehaald kan worden | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoice[]**](../Model/EcedoERPCRMInterfaceApiInvoice.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoicesGetInvoicesWithPrettySmaUsages**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiSmaInvoiceDetails sysInvoicesGetInvoicesWithPrettySmaUsages($invoice_id, $organization_id)

Haal verbruiksregels van een factuur op

Deze API wordt niet langer actief ondersteund. De API is vervangen door `GET /sysapi/v1.0/organizations/{organizationId}/invoices/{invoiceId}/invoiceusages`  Opvragen verbruiksregels van een SMA maand factuur. De factuur periode mag niet langer dan een maand zijn

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysInvoicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)

try {
    $result = $apiInstance->sysInvoicesGetInvoicesWithPrettySmaUsages($invoice_id, $organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoicesApi->sysInvoicesGetInvoicesWithPrettySmaUsages: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **string**| Guid van de factuur (Invoice) |
 **organization_id** | **string**| Guid van de klant (Organization) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiSmaInvoiceDetails**](../Model/EcedoERPCRMInterfaceApiSmaInvoiceDetails.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoicesGetInvoicesWithSmaUsages**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceUsageCalculationRow[] sysInvoicesGetInvoicesWithSmaUsages($invoice_id, $organization_id)

Haal verbruiksregels van een factuur op

Opvragen verbruiksregels

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysInvoicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)

try {
    $result = $apiInstance->sysInvoicesGetInvoicesWithSmaUsages($invoice_id, $organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoicesApi->sysInvoicesGetInvoicesWithSmaUsages: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **string**| Guid van de factuur (Invoice) |
 **organization_id** | **string**| Guid van de klant (Organization) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceUsageCalculationRow[]**](../Model/EcedoERPCRMInterfaceApiInvoiceUsageCalculationRow.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysInvoicesGetInvoicesWithSmaUsagesV11**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceUsageCalculationResponse[] sysInvoicesGetInvoicesWithSmaUsagesV11($invoice_id, $organization_id)

Haal verbruiksregels van een factuur op

Opvragen verbruiksregels

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysInvoicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$invoice_id = "invoice_id_example"; // string | Guid van de factuur (Invoice)
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)

try {
    $result = $apiInstance->sysInvoicesGetInvoicesWithSmaUsagesV11($invoice_id, $organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysInvoicesApi->sysInvoicesGetInvoicesWithSmaUsagesV11: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **string**| Guid van de factuur (Invoice) |
 **organization_id** | **string**| Guid van de klant (Organization) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiInvoiceUsageCalculationResponse[]**](../Model/EcedoERPCRMInterfaceApiInvoiceUsageCalculationResponse.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

