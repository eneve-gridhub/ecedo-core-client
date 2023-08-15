# Swagger\Client\SysMeteringPointsApi

All URIs are relative to *https://innova.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysMeteringPointsCERPreNotifyContract**](SysMeteringPointsApi.md#sysMeteringPointsCERPreNotifyContract) | **POST** /sysapi/v1.0/meteringpoints/{ean}/cerprenotifycontract | Contract in CER aanmelden
[**sysMeteringPointsCreateClientKey**](SysMeteringPointsApi.md#sysMeteringPointsCreateClientKey) | **POST** /sysapi/v1.0/meteringpoints/{ean}/clientkeys | Toevoegen van klantsleutels  aan het C-AR
[**sysMeteringPointsGet**](SysMeteringPointsApi.md#sysMeteringPointsGet) | **GET** /sysapi/v1.0/meteringpoints/{ean} | Opvragen van aansluitingdetails uit het C-AR
[**sysMeteringPointsGetProposalMeteringPoint**](SysMeteringPointsApi.md#sysMeteringPointsGetProposalMeteringPoint) | **GET** /sysapi/v1.0/proposalmeteringpoints/{ean} | Opvragen van aansluitingdetails uit het C-AR tijdens het offerte-traject
[**sysMeteringPointsSearch**](SysMeteringPointsApi.md#sysMeteringPointsSearch) | **GET** /sysapi/v1.0/meteringpoints/search | Zoeken van aansluitingen in het C-AR


# **sysMeteringPointsCERPreNotifyContract**
> \Swagger\Client\Model\EcedoERPCRMInterfaceServicesEDSNCERCERNoticeData sysMeteringPointsCERPreNotifyContract($ean, $process_settings)

Contract in CER aanmelden

Dit is een passthough-API naar het Contract Einde Register (CER) van EDSN<br />  Wanneer een klant een contract bij een leverancier heeft getekend, maar dit contract nog niet actief is, dan kan dit contract alvast in het Contract Einde Register (CER) aangemeld worden om tijdelijk toegang te krijgen tot alle gegevens in het C-AR.<br />  EDSN is verantwoordelijk voor de implementatiedetails van deze API en deze detail kunnen opgezocht worden in het document \"Business Service Contract Einde Register\".<br />  Op moment van schrijven blijft een vooraanmelding 1 maand geldig. Daarna komt deze te vervallen en heeft de leverancier geen toegang meer tot het C-AR als het contract nog niet is ingegaan.

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

$apiInstance = new Swagger\Client\Api\SysMeteringPointsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ean = "ean_example"; // string | EAN van de aansluiting
$process_settings = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiPreNotifyContractProcessSettings(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiPreNotifyContractProcessSettings | Process instellingen, het object moet bestaan maar mag leeg zijn. Alle velden zijn optioneel. Zie het object-model voor meer details over de verschillende variabelen

try {
    $result = $apiInstance->sysMeteringPointsCERPreNotifyContract($ean, $process_settings);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeteringPointsApi->sysMeteringPointsCERPreNotifyContract: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **string**| EAN van de aansluiting |
 **process_settings** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiPreNotifyContractProcessSettings**](../Model/EcedoERPCRMInterfaceApiPreNotifyContractProcessSettings.md)| Process instellingen, het object moet bestaan maar mag leeg zijn. Alle velden zijn optioneel. Zie het object-model voor meer details over de verschillende variabelen |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceServicesEDSNCERCERNoticeData**](../Model/EcedoERPCRMInterfaceServicesEDSNCERCERNoticeData.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysMeteringPointsCreateClientKey**
> object sysMeteringPointsCreateClientKey($ean, $post_data)

Toevoegen van klantsleutels  aan het C-AR

Met behulp van deze API kunnen de klantsleutels in het C-AR bijgewerkt worden, bijvoorbeeld wanneer het bankrekeningnummer van de klant wijzigt.

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

$apiInstance = new Swagger\Client\Api\SysMeteringPointsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ean = "ean_example"; // string | EAN code van de aansluiting
$post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiClientKeyCreateData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiClientKeyCreateData | De data van de klantsleutel(s), zie het object-model voor meer informatie

try {
    $result = $apiInstance->sysMeteringPointsCreateClientKey($ean, $post_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeteringPointsApi->sysMeteringPointsCreateClientKey: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **string**| EAN code van de aansluiting |
 **post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiClientKeyCreateData**](../Model/EcedoERPCRMInterfaceApiClientKeyCreateData.md)| De data van de klantsleutel(s), zie het object-model voor meer informatie |

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysMeteringPointsGet**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiExtendedMeteringPoint sysMeteringPointsGet($ean, $include_cer, $cer_pre_notified, $supplier_ean)

Opvragen van aansluitingdetails uit het C-AR

Dit is een passthough-API naar het Centraal Aansluitingen Register (C-AR) van EDSN<br />  Met behulp van deze API kunnen aansluitingdetails uit het C-AR opgevraagd worden<br /><br />  **Let op!** Deze API kan alleen gebruikt worden voor grootverbruikaansluitingen of kleinverbruikaansluitingen waarvoor een vooraanmelding (fase III) is verstuurd (zie API POST /sysapi/v1.0/meteringpoints/{ean}/cerprenotifycontract)<br />  **Let op!** Het Contract Einde Register (CER) is tot onbekende datum offline. Daardoor is het niet mogelijk om contract einde datums op te vragen en dus zal de `FirstAllowedSwitchDate` uit de `Response` altijd de eerstvolgende switchdatum (rekening houdend met afkoelperiode, EDSN werkdagen, etc.)<br />  **Let op!** Op testomgevingen wordt mock-data teruggegeven. Deze data komt niet precies overeen met productiedata. Zie de <a href=\"https://ecedo.atlassian.net/wiki/spaces/KNOWLEDGE/pages/2244902913/C-AR+mockdata+op+testomgevingen\" target=\"_blank\">developer documentatie</a> voor meer uitleg en een overzicht van aansluitingen per use case.<br />

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

$apiInstance = new Swagger\Client\Api\SysMeteringPointsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ean = "ean_example"; // string | De EAN code van de aansluiting
$include_cer = true; // bool | Default: true. Met behulp van deze parameter kan aangegeven worden of het contracteinddatum uit het CER opgevraagd moet worden. Aan de hand daarvan zal de `FirstAllowedSwitchDate` in de response gevuld worden
$cer_pre_notified = true; // bool | Default: false. Met behulp van deze parameter kan aangegeven worden of de aansluiting vooraangemeld is. Dit is alleen toegestaan bij kleinverbruikaansluitingen.
$supplier_ean = "supplier_ean_example"; // string | Indien er in een omgeving meerdere leverancier-EANs geconfigureerd zijn kan met behulp van deze parameter aangegeven worden welke leverancier-EAN gebruikt moet worden om de gegevens uit het C-AR op te vragen. Standaard wordt de hoofd-EAN gebruikt.

try {
    $result = $apiInstance->sysMeteringPointsGet($ean, $include_cer, $cer_pre_notified, $supplier_ean);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeteringPointsApi->sysMeteringPointsGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **string**| De EAN code van de aansluiting |
 **include_cer** | **bool**| Default: true. Met behulp van deze parameter kan aangegeven worden of het contracteinddatum uit het CER opgevraagd moet worden. Aan de hand daarvan zal de &#x60;FirstAllowedSwitchDate&#x60; in de response gevuld worden | [optional]
 **cer_pre_notified** | **bool**| Default: false. Met behulp van deze parameter kan aangegeven worden of de aansluiting vooraangemeld is. Dit is alleen toegestaan bij kleinverbruikaansluitingen. | [optional]
 **supplier_ean** | **string**| Indien er in een omgeving meerdere leverancier-EANs geconfigureerd zijn kan met behulp van deze parameter aangegeven worden welke leverancier-EAN gebruikt moet worden om de gegevens uit het C-AR op te vragen. Standaard wordt de hoofd-EAN gebruikt. | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiExtendedMeteringPoint**](../Model/EcedoERPCRMInterfaceApiExtendedMeteringPoint.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysMeteringPointsGetProposalMeteringPoint**
> sysMeteringPointsGetProposalMeteringPoint($ean, $mandate_id, $iban_key, $birth_day_key, $include_cer, $supplier_ean)

Opvragen van aansluitingdetails uit het C-AR tijdens het offerte-traject

Dit is een passthough-API naar het Centraal Aansluitingen Register (C-AR) van EDSN<br />  Met behulp van deze API kunnen aansluitingdetails uit het C-AR opgevraagd worden tijdens het offerte-traject (ook wel aanbod op maat of Fase II genoemd)<br /><br />  **Let op!** De Fase II services zijn tot onbekende datum offline gehaald. Daardoor kan deze API niet langer gebruikt worden.<br />

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

$apiInstance = new Swagger\Client\Api\SysMeteringPointsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ean = "ean_example"; // string | EAN code van de aansluiting
$mandate_id = "mandate_id_example"; // string | Key van de leverancier waarmee het klantmandaat gevonden kan worden
$iban_key = "iban_key_example"; // string | Laatste 3 cijfers van rekeningnummer klant
$birth_day_key = "birth_day_key_example"; // string | Verjaardag vad klant in notatie MMDD
$include_cer = true; // bool | Opvragen CER contract data ja/nee
$supplier_ean = "supplier_ean_example"; // string | Indien er in een omgeving meerdere leverancier-EANs geconfigureerd zijn kan met behulp van deze parameter aangegeven worden welke leverancier-EAN gebruikt moet worden om de gegevens uit het C-AR op te vragen. Standaard wordt de hoofd-EAN gebruikt.

try {
    $apiInstance->sysMeteringPointsGetProposalMeteringPoint($ean, $mandate_id, $iban_key, $birth_day_key, $include_cer, $supplier_ean);
} catch (Exception $e) {
    echo 'Exception when calling SysMeteringPointsApi->sysMeteringPointsGetProposalMeteringPoint: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **string**| EAN code van de aansluiting |
 **mandate_id** | **string**| Key van de leverancier waarmee het klantmandaat gevonden kan worden |
 **iban_key** | **string**| Laatste 3 cijfers van rekeningnummer klant | [optional]
 **birth_day_key** | **string**| Verjaardag vad klant in notatie MMDD | [optional]
 **include_cer** | **bool**| Opvragen CER contract data ja/nee | [optional]
 **supplier_ean** | **string**| Indien er in een omgeving meerdere leverancier-EANs geconfigureerd zijn kan met behulp van deze parameter aangegeven worden welke leverancier-EAN gebruikt moet worden om de gegevens uit het C-AR op te vragen. Standaard wordt de hoofd-EAN gebruikt. | [optional]

### Return type

void (empty response body)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysMeteringPointsSearch**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiMeteringPoint[] sysMeteringPointsSearch($market_segment, $ean, $address_zip_code, $address_number, $address_addition)

Zoeken van aansluitingen in het C-AR

Dit is een passthough-API naar het Centraal Aansluitingen Register (C-AR) van EDSN<br />  Met behulp van deze API kunnen aansluitingen in het C-AR gezocht worden op basis van EAN of adres<br /><br />  Let op! Ecedo kent alleen de verbruikssegmenten (UsageTypes) \"Grootverbruik\" en \"Kleinverbruik\" en dus niet \"Artikel 1 lid 2 of 3\". Als gezocht wordt op een artikel-aansluiting, dan geeft Ecedo dit terug als verbruikssegment \"Grootverbruik\" waarbij de variabele `IsART` op `true` staat.<br />  Wanneer op EAN wordt gezocht is het niet toegestaan om marktsegment, postcode, huisnummer of huisnummertoevoeging te gebruiken<br /><br />  Wanneer gezocht wordt op EAN code is het niet toegestaan om marktsegment, postcode, huisnummer of huisnummertoevoeging mee te geven<br /><br />  **Let op!** Op testomgevingen wordt mock-data teruggegeven. Deze data komt niet precies overeen met productiedata. Zie de <a href=\"https://ecedo.atlassian.net/wiki/spaces/KNOWLEDGE/pages/2244902913/C-AR+mockdata+op+testomgevingen\" target=\"_blank\">developer documentatie</a> voor meer uitleg en een overzicht van aansluitingen per use case.<br />

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

$apiInstance = new Swagger\Client\Api\SysMeteringPointsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$market_segment = "market_segment_example"; // string | Marktsegment
$ean = "ean_example"; // string | EAN code
$address_zip_code = "address_zip_code_example"; // string | Postcode
$address_number = 56; // int | Huisnummer
$address_addition = "address_addition_example"; // string | Optionele huisnummertoevoeging

try {
    $result = $apiInstance->sysMeteringPointsSearch($market_segment, $ean, $address_zip_code, $address_number, $address_addition);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMeteringPointsApi->sysMeteringPointsSearch: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_segment** | **string**| Marktsegment | [optional]
 **ean** | **string**| EAN code | [optional]
 **address_zip_code** | **string**| Postcode | [optional]
 **address_number** | **int**| Huisnummer | [optional]
 **address_addition** | **string**| Optionele huisnummertoevoeging | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeteringPoint[]**](../Model/EcedoERPCRMInterfaceApiMeteringPoint.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

