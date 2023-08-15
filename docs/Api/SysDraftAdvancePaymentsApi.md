# Swagger\Client\SysDraftAdvancePaymentsApi

All URIs are relative to *https://innova.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysDraftAdvancePaymentsCalculateDraftAdvancePayment**](SysDraftAdvancePaymentsApi.md#sysDraftAdvancePaymentsCalculateDraftAdvancePayment) | **POST** /sysapi/v1.0/organizations/{organizationId}/draftadvancepayments | Aanmaken proefvoorschot
[**sysDraftAdvancePaymentsCalculateDraftAdvancePaymentForNonOrganization**](SysDraftAdvancePaymentsApi.md#sysDraftAdvancePaymentsCalculateDraftAdvancePaymentForNonOrganization) | **POST** /sysapi/v1.0/draftadvancepayments | Aanmaken proefvoorschot


# **sysDraftAdvancePaymentsCalculateDraftAdvancePayment**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiDraftAdvancePayment sysDraftAdvancePaymentsCalculateDraftAdvancePayment($organization_id, $post_data)

Aanmaken proefvoorschot

Alle aansluitingen die actief zijn op de ReferenceDate (peildatum) worden meegenomen<br />  Alleen ContractPropertyType 'Reseller' kan ingestuurd worden.  Agreementdate kan op het hoogste niveau meegegeven worden of per aansluiting. Niet op beide plekken tegelijk.

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

$apiInstance = new Swagger\Client\Api\SysDraftAdvancePaymentsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiDraftAdvancePaymentPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiDraftAdvancePaymentPostData | 

try {
    $result = $apiInstance->sysDraftAdvancePaymentsCalculateDraftAdvancePayment($organization_id, $post_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysDraftAdvancePaymentsApi->sysDraftAdvancePaymentsCalculateDraftAdvancePayment: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiDraftAdvancePaymentPostData**](../Model/EcedoERPCRMInterfaceApiDraftAdvancePaymentPostData.md)|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiDraftAdvancePayment**](../Model/EcedoERPCRMInterfaceApiDraftAdvancePayment.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysDraftAdvancePaymentsCalculateDraftAdvancePaymentForNonOrganization**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiDraftAdvancePayment sysDraftAdvancePaymentsCalculateDraftAdvancePaymentForNonOrganization($post_data)

Aanmaken proefvoorschot

Met behulp van deze API kan een proefvoorschot berekend worden voor aansluitingen die nog niet in Ecedo bekend zijn.<br /><br />  Tot januari 2020 was het mogelijk om verbruiken, CapTar-codes en profielen uit het C-AR op te vragen met behulp van klantsleutels. Dat is sindsdien echter niet meer mogelijk, waardoor deze gegevens expliciet meegegeven moeten worden in de aanroep<br /><br />  In het consumentendomein wordt de elektriciteit-CapTar-code `10211` door meer dan 95% van de aansluitingen gebruikt en de gas-CapTar-code `20211` wordt door meer dan 85% van de aansluitingen gebruikt.<br />  (disclaimer: deze gegevens zijn in juni 2021 verzameld op basis van de aansluitingen die via Ecedo systemen worden beleverd. Iedere leverancier moet zelf een keuze maken welke CapTar-codes gebruikt moeten worden.)<br />

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

$apiInstance = new Swagger\Client\Api\SysDraftAdvancePaymentsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiNonOrganizationDraftAdvancePaymentPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiNonOrganizationDraftAdvancePaymentPostData | 

try {
    $result = $apiInstance->sysDraftAdvancePaymentsCalculateDraftAdvancePaymentForNonOrganization($post_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysDraftAdvancePaymentsApi->sysDraftAdvancePaymentsCalculateDraftAdvancePaymentForNonOrganization: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiNonOrganizationDraftAdvancePaymentPostData**](../Model/EcedoERPCRMInterfaceApiNonOrganizationDraftAdvancePaymentPostData.md)|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiDraftAdvancePayment**](../Model/EcedoERPCRMInterfaceApiDraftAdvancePayment.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

