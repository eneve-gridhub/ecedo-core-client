# Swagger\Client\SysPropositionsApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysPropositionsEnd**](SysPropositionsApi.md#sysPropositionsEnd) | **PUT** /sysapi/v1.0/propositions/{propositionId}/end | Set de einddatum zodat de propositie beeindigd wordt.
[**sysPropositionsFilter**](SysPropositionsApi.md#sysPropositionsFilter) | **GET** /sysapi/v1.0/propositions/filter | Opvragen van proposities op basis van productid
[**sysPropositionsGet**](SysPropositionsApi.md#sysPropositionsGet) | **GET** /sysapi/v1.0/meansofproductions/{meansOfProductionId}/propositions | Opvragen Meelift proposities van een productiemiddel.
[**sysPropositionsGetPropositionPrices**](SysPropositionsApi.md#sysPropositionsGetPropositionPrices) | **GET** /sysapi/v1.0/propositionprices | Opvragen alle prijzen behorend bij een propositie
[**sysPropositionsPost**](SysPropositionsApi.md#sysPropositionsPost) | **POST** /sysapi/v1.0/propositions | Aanmaken van een propositie
[**sysPropositionsPrices**](SysPropositionsApi.md#sysPropositionsPrices) | **POST** /sysapi/v1.0/propositions/{propositionId}/prices | Aanmaken van de prijzen behorend bij een propositie


# **sysPropositionsEnd**
> object sysPropositionsEnd($proposition_id, $end_date)

Set de einddatum zodat de propositie beeindigd wordt.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysPropositionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$proposition_id = "proposition_id_example"; // string | Propositie referentie
$end_date = new \DateTime("2013-10-20"); // \DateTime | Eind datum wanneer de propositie moet eindigen. 2016-01-30

try {
    $result = $apiInstance->sysPropositionsEnd($proposition_id, $end_date);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPropositionsApi->sysPropositionsEnd: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposition_id** | **string**| Propositie referentie |
 **end_date** | **\DateTime**| Eind datum wanneer de propositie moet eindigen. 2016-01-30 |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysPropositionsFilter**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiProposition[] sysPropositionsFilter($product_id, $valid_on, $reference_filter, $company_label_id)

Opvragen van proposities op basis van productid

Ondersteunde producten:  * ElektriciteitMeelift: 10E8EF99-2EA1-4F20-B256-A2D300E260E5  * GasMeelift: 3E6CB93A-6650-4B13-B863-C8DC871C7260  * ElektriciteitKleinverbruik: 962d8c69-7403-494e-b772-a0ac011a9d00  * GasKleinverbruik: 60bc826c-aa9a-4279-b6ac-a0ac011ab7d0  * ElektriciteitGrootverbruik: 5CA64903-8345-4DBF-8E88-A1BD013E690A  * GasGrootverbruik: 55B3FB1C-DD2D-4AED-A536-FBEBF9B08381  * ExterneOpwekWind: B156E122-CA1A-4FA7-AAC9-A3FE0114A7BB  * ExterneOpwekZon: 78B56301-D77C-4BAA-AED4-A4A400DC6DBC  * ElektriciteitTankKaart: 6B1B6762-5F28-4EC1-841D-A5E500C89D6B    Let op! Bij het opvragen van ElektriciteitMeelift of GasMeelift worden altijd de proposities van de producten ElektriciteitMeelift en GasMeelift teruggegeven    Let op! De prijzen die worden teruggeven hebben allemaal het BTW percentage van vandaag. Er wordt geen rekening gehouden met de prijsperiode.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysPropositionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$product_id = "product_id_example"; // string | 
$valid_on = new \DateTime("2013-10-20"); // \DateTime | Optioneel, als gevuld dan moet de propositie geldig zijn op deze datum (yyyy-mm-dd)
$reference_filter = "reference_filter_example"; // string | Optioneel, filter de proposities op (een deel van) de gegeven naam
$company_label_id = "company_label_id_example"; // string | Verplicht veld wanneer er in een omgeving meerdere labels geconfigureerd zijn. Mag weggelaten worden of null zijn in omgevingen waar maar één label geconfigureerd is

try {
    $result = $apiInstance->sysPropositionsFilter($product_id, $valid_on, $reference_filter, $company_label_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPropositionsApi->sysPropositionsFilter: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **string**|  |
 **valid_on** | **\DateTime**| Optioneel, als gevuld dan moet de propositie geldig zijn op deze datum (yyyy-mm-dd) | [optional]
 **reference_filter** | **string**| Optioneel, filter de proposities op (een deel van) de gegeven naam | [optional]
 **company_label_id** | [**string**](../Model/.md)| Verplicht veld wanneer er in een omgeving meerdere labels geconfigureerd zijn. Mag weggelaten worden of null zijn in omgevingen waar maar één label geconfigureerd is | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiProposition[]**](../Model/EcedoERPCRMInterfaceApiProposition.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysPropositionsGet**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiProposition[] sysPropositionsGet($means_of_production_id)

Opvragen Meelift proposities van een productiemiddel.

GET https://server/sysapi/v1.0/meansofproductions/239a159b-fa2c-4e55-9384-a2d4014f9e06/Propositions

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysPropositionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$means_of_production_id = "means_of_production_id_example"; // string | 

try {
    $result = $apiInstance->sysPropositionsGet($means_of_production_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPropositionsApi->sysPropositionsGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **means_of_production_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiProposition[]**](../Model/EcedoERPCRMInterfaceApiProposition.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysPropositionsGetPropositionPrices**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiPropositionPrice[] sysPropositionsGetPropositionPrices($reference, $start_date, $end_date, $include_provisional)

Opvragen alle prijzen behorend bij een propositie

Deze API wordt niet langer ondersteund en kan incorrecte resultaten teruggeven als er een periode langer dan 1 dag wordt gebruikt.   Ook worden er geen labelprijzen teruggegeven.<br />  Gebruik GET https://server/sysapi/v1.0/prices/energielevering/propositions/{propositionId} of GET https://server/sysapi/v1.0/prices/energielevering/propositions/byReference/{propositionReference} als alternatief.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysPropositionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$reference = "reference_example"; // string | Client Propositie Reference
$start_date = new \DateTime("2013-10-20"); // \DateTime | Start prijs periode bijv. 2016-01-30
$end_date = new \DateTime("2013-10-20"); // \DateTime | Eind prijs periode bijv 2016-03-01
$include_provisional = true; // bool | Inclusief voorlopige prijzen bijv true

try {
    $result = $apiInstance->sysPropositionsGetPropositionPrices($reference, $start_date, $end_date, $include_provisional);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPropositionsApi->sysPropositionsGetPropositionPrices: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference** | **string**| Client Propositie Reference |
 **start_date** | **\DateTime**| Start prijs periode bijv. 2016-01-30 |
 **end_date** | **\DateTime**| Eind prijs periode bijv 2016-03-01 |
 **include_provisional** | **bool**| Inclusief voorlopige prijzen bijv true | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiPropositionPrice[]**](../Model/EcedoERPCRMInterfaceApiPropositionPrice.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysPropositionsPost**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiPropositionPostResult sysPropositionsPost($data)

Aanmaken van een propositie

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysPropositionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiPropositionPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiPropositionPostData | 

try {
    $result = $apiInstance->sysPropositionsPost($data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPropositionsApi->sysPropositionsPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiPropositionPostData**](../Model/EcedoERPCRMInterfaceApiPropositionPostData.md)|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiPropositionPostResult**](../Model/EcedoERPCRMInterfaceApiPropositionPostResult.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysPropositionsPrices**
> object sysPropositionsPrices($proposition_id, $post_data)

Aanmaken van de prijzen behorend bij een propositie

Prijzen zijn in EUR  Prijzen standaard excl. BTW tenzij anders aangegeven  Voor elektricteit is de unit kWh; voor Gas prijzen is de unit m3  <br />  __Technische details:__  * Alle startdata en einddata van de ingestuurde prijscomponenten moeten gelijk zijn.  * Er mag per API-call maar één soort status ingestuurd worden. Alle prijscomponenten zijn dus of Finalized of Provisional.  * Als er al prijscomponenten voor een bepaalde status aanwezig zijn en er worden prijscomponenten voor deze status ingestuurd. Dan moeten alle prijscomponenten die op de propositie aanwezig zijn met deze status ook ingestuurd worden. Er mogen niet meer of minder prijscomponenten ingestuurd worden.  * Er mag maar 1 tijdsperiode per call ingestuurd worden (alle startdata en einddata zijn dus gelijk).

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysPropositionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$proposition_id = "proposition_id_example"; // string | 
$post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiPricesPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiPricesPostData | 

try {
    $result = $apiInstance->sysPropositionsPrices($proposition_id, $post_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPropositionsApi->sysPropositionsPrices: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposition_id** | **string**|  |
 **post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiPricesPostData**](../Model/EcedoERPCRMInterfaceApiPricesPostData.md)|  |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

