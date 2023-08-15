# Swagger\Client\SysCustomInvoicesApi

All URIs are relative to *https://innova.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysCustomInvoicesCreateCustomInvoice**](SysCustomInvoicesApi.md#sysCustomInvoicesCreateCustomInvoice) | **POST** /sysapi/v1.0/organizations/{organizationId}/custominvoices | Aanmaken van een handmatige factuur


# **sysCustomInvoicesCreateCustomInvoice**
> string sysCustomInvoicesCreateCustomInvoice($organization_id, $post_data)

Aanmaken van een handmatige factuur

Factuurdatum en Betaaldatum worden indien leeggelaten automatisch gevuld op basis van de debiteur instellingen   Financiële omschrijving is max 140 karakters  InvoiceSubType mag 'Custom_General', 'Custom_ChargingStation' of 'Custom_ChargeCard' zijn

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

$apiInstance = new Swagger\Client\Api\SysCustomInvoicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiCustomInvoicePostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiCustomInvoicePostData | 

try {
    $result = $apiInstance->sysCustomInvoicesCreateCustomInvoice($organization_id, $post_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysCustomInvoicesApi->sysCustomInvoicesCreateCustomInvoice: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiCustomInvoicePostData**](../Model/EcedoERPCRMInterfaceApiCustomInvoicePostData.md)|  |

### Return type

**string**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

