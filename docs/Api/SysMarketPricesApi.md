# Swagger\Client\SysMarketPricesApi

All URIs are relative to *https://innova.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysMarketPricesGet**](SysMarketPricesApi.md#sysMarketPricesGet) | **GET** /sysapi/v1.0/marketprices/{startDate}/{endDate}/{marketPriceType} | Haal marktprijzen (excl. btw) op voor periode en marktprijstype
[**sysMarketPricesPostMarketPrices**](SysMarketPricesApi.md#sysMarketPricesPostMarketPrices) | **POST** /sysapi/v1.0/marketprices/{marketPriceType} | Marktprijzen toevoegen voor marktprijstype


# **sysMarketPricesGet**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiMarketPrice[] sysMarketPricesGet($start_date, $end_date, $market_price_type)

Haal marktprijzen (excl. btw) op voor periode en marktprijstype

__Let op!__ Als prijzen van het type `TtfDayAheadDay` worden opgevraagd dan worden de `startDate` en `endDate` geïnterpreteerd als gasdagen.<br />  Als `startDate` \"2022-01-01\" is en `endDate` is \"2022-01-02\", dan wordt dit geïnterpreteerd als \"2022-01-01 06:00\" (lokale tijd) en \"2022-01-02 06:00\" (lokale tijd). Hierdoor bevat de response één prijs (de prijs voor de gasdag) in plaats van de twee prijzen (de prijzen voor de kalenderdag).  Periode voor opvragen data mag maximaal 370 dagen bedragen.

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

$apiInstance = new Swagger\Client\Api\SysMarketPricesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$start_date = new \DateTime("2013-10-20"); // \DateTime | 
$end_date = new \DateTime("2013-10-20"); // \DateTime | 
$market_price_type = "market_price_type_example"; // string | 

try {
    $result = $apiInstance->sysMarketPricesGet($start_date, $end_date, $market_price_type);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMarketPricesApi->sysMarketPricesGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **\DateTime**|  |
 **end_date** | **\DateTime**|  |
 **market_price_type** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMarketPrice[]**](../Model/EcedoERPCRMInterfaceApiMarketPrice.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysMarketPricesPostMarketPrices**
> object sysMarketPricesPostMarketPrices($market_price_type, $market_prices_post_data)

Marktprijzen toevoegen voor marktprijstype

Met behulp van deze API kunnen marktprijzen vanuit een ander systeem in Ecedo worden opgeslagen.<br /><br />  Alleen prijzen van type `ApxDayAheadHour` en `TtfDayAheadDay` zijn toegestaan.<br />

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

$apiInstance = new Swagger\Client\Api\SysMarketPricesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$market_price_type = "market_price_type_example"; // string | Het marktprijstype
$market_prices_post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiMarketPricesPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiMarketPricesPostData | De marktprijzen, zie het object-model voor meer informatie

try {
    $result = $apiInstance->sysMarketPricesPostMarketPrices($market_price_type, $market_prices_post_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMarketPricesApi->sysMarketPricesPostMarketPrices: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_price_type** | **string**| Het marktprijstype |
 **market_prices_post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMarketPricesPostData**](../Model/EcedoERPCRMInterfaceApiMarketPricesPostData.md)| De marktprijzen, zie het object-model voor meer informatie |

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

