# Swagger\Client\SysTerminationFeesApi

All URIs are relative to *https://innova.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysTerminationFeesCalculateTerminationFeeForContract**](SysTerminationFeesApi.md#sysTerminationFeesCalculateTerminationFeeForContract) | **GET** /sysapi/v1.0/terminationfees/calculateForContract/{contractId} | Berekent een indicatieve opzegvergoeding voor een contract
[**sysTerminationFeesCalculateTerminationFeesForConnection**](SysTerminationFeesApi.md#sysTerminationFeesCalculateTerminationFeesForConnection) | **GET** /sysapi/v1.0/terminationfees/calculateForConnection/{connectionId} | Berekent een indicatieve opzegvergoeding voor een aansluiting
[**sysTerminationFeesGetCalculationTypeForContract**](SysTerminationFeesApi.md#sysTerminationFeesGetCalculationTypeForContract) | **GET** /sysapi/v1.0/terminationfees/calculationTypeByContract/{contractId} | Geeft het type opzegvergoeding terug voor een energielevering- of meeliftcontract
[**sysTerminationFeesGetCalculationTypesForConnection**](SysTerminationFeesApi.md#sysTerminationFeesGetCalculationTypesForConnection) | **GET** /sysapi/v1.0/terminationfees/calculationTypesByConnection/{connectionId} | Geeft het type opzegvergoeding terug voor een aansluiting
[**sysTerminationFeesGetReferenceProposition**](SysTerminationFeesApi.md#sysTerminationFeesGetReferenceProposition) | **GET** /sysapi/v1.0/terminationfees/referencePropositionsByContract/{contractId} | Haalt de referentiepropositie voor een energieleveringcontract op en een eventuele referentiepropositie voor een bijbehorende meeliftpropositie.
[**sysTerminationFeesGetTerminationFeesByConnection**](SysTerminationFeesApi.md#sysTerminationFeesGetTerminationFeesByConnection) | **GET** /sysapi/v1.0/terminationfees/byConnection/{connectionId} | Haalt de opzegvergoedingen op die bij een aansluiting horen
[**sysTerminationFeesGetTerminationFeesByInvoice**](SysTerminationFeesApi.md#sysTerminationFeesGetTerminationFeesByInvoice) | **GET** /sysapi/v1.0/terminationfees/byInvoice/{invoiceId} | Haalt de gefactureerde opzegvergoedingen op voor een specifieke factuur


# **sysTerminationFeesCalculateTerminationFeeForContract**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiCalculatedTerminationFee sysTerminationFeesCalculateTerminationFeeForContract($contract_id, $termination_date)

Berekent een indicatieve opzegvergoeding voor een contract

Met behulp van deze API kan een indicatieve opzegvergoeding berekend worden voor een specifiek contract en een specifieke opzegdatum.<br /><br />  De opzegvergoeding die met deze API wordt berekend is vluchtig en indicatief. Hier kan de klant geen rechten aan ontlenen, maar is bedoeld om een indicatie te geven van de hoogte van de opzegvergoeding wanneer de klant daadwerkelijk zijn of haar contract op zou zeggen.<br />

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

$apiInstance = new Swagger\Client\Api\SysTerminationFeesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$contract_id = "contract_id_example"; // string | Het contract waarvoor de opzegvergoeding voor berekend moet worden
$termination_date = new \DateTime("2013-10-20"); // \DateTime | De datum waarop het opgezegd wordt. Als dit leeg gelaten is dan wordt de huidige datum gepakt

try {
    $result = $apiInstance->sysTerminationFeesCalculateTerminationFeeForContract($contract_id, $termination_date);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysTerminationFeesApi->sysTerminationFeesCalculateTerminationFeeForContract: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **string**| Het contract waarvoor de opzegvergoeding voor berekend moet worden |
 **termination_date** | **\DateTime**| De datum waarop het opgezegd wordt. Als dit leeg gelaten is dan wordt de huidige datum gepakt | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiCalculatedTerminationFee**](../Model/EcedoERPCRMInterfaceApiCalculatedTerminationFee.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysTerminationFeesCalculateTerminationFeesForConnection**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiTerminationFeeConnectionCalculations sysTerminationFeesCalculateTerminationFeesForConnection($connection_id, $termination_date)

Berekent een indicatieve opzegvergoeding voor een aansluiting

Met behulp van deze API kan een indicatieve opzegvergoeding berekend worden voor een specifieke aansluiting en een specifieke opzegdatum.<br /><br />  De opzegvergoeding die met deze API wordt berekend is vluchtig en indicatief. Hier kan de klant geen rechten aan ontlenen, maar is bedoeld om een indicatie te geven van de hoogte van de opzegvergoeding wanneer de klant daadwerkelijk zijn of haar contract op zou zeggen.<br />

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

$apiInstance = new Swagger\Client\Api\SysTerminationFeesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$connection_id = "connection_id_example"; // string | De aansluiting waar de opzegvergoedingen voor berekend moeten worden
$termination_date = new \DateTime("2013-10-20"); // \DateTime | De datum waarop het contract opgezegd wordt. Als dit leeg gelaten is dan wordt de huidige datum gepakt

try {
    $result = $apiInstance->sysTerminationFeesCalculateTerminationFeesForConnection($connection_id, $termination_date);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysTerminationFeesApi->sysTerminationFeesCalculateTerminationFeesForConnection: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **string**| De aansluiting waar de opzegvergoedingen voor berekend moeten worden |
 **termination_date** | **\DateTime**| De datum waarop het contract opgezegd wordt. Als dit leeg gelaten is dan wordt de huidige datum gepakt | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiTerminationFeeConnectionCalculations**](../Model/EcedoERPCRMInterfaceApiTerminationFeeConnectionCalculations.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysTerminationFeesGetCalculationTypeForContract**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiTerminationFeeCalculationTypeResponse sysTerminationFeesGetCalculationTypeForContract($contract_id)

Geeft het type opzegvergoeding terug voor een energielevering- of meeliftcontract

Er zijn verschillende manieren waarop een opzegvergoeding berekend kan worden. Bijvoorbeeld Rover2023 voor kleinverbruikaansluitingen met een tekendatum op of na 1-6-2023 of Rover2013 van oudere contracten. Daarnaast kan een opzegvergoeding ook gebaseerd worden op zakelijke afspraken of kan er geen opzegvergoeding van toepassing zijn.<br /><br />  Met behulp van deze API kan per contract opgevraagd worden welk type opzegvergoeding van toepassing is.<br />  Zie het model van de response voor de mogelijke waarden.<br />

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

$apiInstance = new Swagger\Client\Api\SysTerminationFeesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$contract_id = "contract_id_example"; // string | Het contract waar het type TerminationFee berekening voor moet worden opgehaald

try {
    $result = $apiInstance->sysTerminationFeesGetCalculationTypeForContract($contract_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysTerminationFeesApi->sysTerminationFeesGetCalculationTypeForContract: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **string**| Het contract waar het type TerminationFee berekening voor moet worden opgehaald |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiTerminationFeeCalculationTypeResponse**](../Model/EcedoERPCRMInterfaceApiTerminationFeeCalculationTypeResponse.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysTerminationFeesGetCalculationTypesForConnection**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionTerminationFeeTypes sysTerminationFeesGetCalculationTypesForConnection($connection_id, $termination_date)

Geeft het type opzegvergoeding terug voor een aansluiting

Er zijn verschillende manieren waarop een opzegvergoeding berekend kan worden. Bijvoorbeeld Rover2023 voor kleinverbruikaansluitingen met een tekendatum op of na 1-6-2023 of Rover2013 van oudere contracten. Daarnaast kan een opzegvergoeding ook gebaseerd worden op zakelijke afspraken of kan er geen opzegvergoeding van toepassing zijn.<br /><br />  Met behulp van deze API kan per aansluiting opgevraagd worden welk types opzegvergoedingen van toepassing zijn op de contracten van deze aansluiting en afhankelijk van de meegegeven opzegdatum (`terminationDate`).<br />  Zie het model van de response voor de mogelijke waarden.<br />

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

$apiInstance = new Swagger\Client\Api\SysTerminationFeesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$connection_id = "connection_id_example"; // string | De aansluiting waar de type TerminationFee berekeningen voor moet worden opgehaald
$termination_date = new \DateTime("2013-10-20"); // \DateTime | De datum waarop het contract opgezegd wordt. Als dit leeg gelaten is dan wordt de huidige datum gepakt

try {
    $result = $apiInstance->sysTerminationFeesGetCalculationTypesForConnection($connection_id, $termination_date);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysTerminationFeesApi->sysTerminationFeesGetCalculationTypesForConnection: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **string**| De aansluiting waar de type TerminationFee berekeningen voor moet worden opgehaald |
 **termination_date** | **\DateTime**| De datum waarop het contract opgezegd wordt. Als dit leeg gelaten is dan wordt de huidige datum gepakt | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionTerminationFeeTypes**](../Model/EcedoERPCRMInterfaceApiConnectionTerminationFeeTypes.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysTerminationFeesGetReferenceProposition**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiTerminationFeeReferencePropositions sysTerminationFeesGetReferenceProposition($contract_id)

Haalt de referentiepropositie voor een energieleveringcontract op en een eventuele referentiepropositie voor een bijbehorende meeliftpropositie.

Deze API-call haalt een referentiepropositie voor een energieleveringcontract op, en indien aanwezig een referentiepropositie voor de bijbehorende meeliftpropositie. Deze call werkt alleen voor kleinverbruik aansluitingen en voor energieleveringscontracten.  Deze call haalt de propositie(s) op die op dit moment actief zijn en het best matchen bij de energielevering- en meeliftpropositie van het contract. Het product moet overeenkomen met de propositie van het contract. De propositiegroep en duration hebben respectievelijk hoogste prioriteit mochten er meerdere matches gevonden worden.  Mochten de propositiegroep en duration niet tot een unieke matchende propositie leiden dan wordt de propositie met de hoogste prijs gepakt.

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

$apiInstance = new Swagger\Client\Api\SysTerminationFeesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$contract_id = "contract_id_example"; // string | Het contract waar de referentiepropositie(s) voor moet worden opgehaald

try {
    $result = $apiInstance->sysTerminationFeesGetReferenceProposition($contract_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysTerminationFeesApi->sysTerminationFeesGetReferenceProposition: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **string**| Het contract waar de referentiepropositie(s) voor moet worden opgehaald |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiTerminationFeeReferencePropositions**](../Model/EcedoERPCRMInterfaceApiTerminationFeeReferencePropositions.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysTerminationFeesGetTerminationFeesByConnection**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiContractTerminationFeeBase[] sysTerminationFeesGetTerminationFeesByConnection($connection_id, $calculation_reason)

Haalt de opzegvergoedingen op die bij een aansluiting horen

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

$apiInstance = new Swagger\Client\Api\SysTerminationFeesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$connection_id = "connection_id_example"; // string | De aansluiting waarvoor de opzegvergoedingen opgehaald moeten worden
$calculation_reason = "calculation_reason_example"; // string | De reden waarvoor de opzegvergoeding berekent is waarop gefilterd moet worden (indien gevuld)

try {
    $result = $apiInstance->sysTerminationFeesGetTerminationFeesByConnection($connection_id, $calculation_reason);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysTerminationFeesApi->sysTerminationFeesGetTerminationFeesByConnection: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **string**| De aansluiting waarvoor de opzegvergoedingen opgehaald moeten worden |
 **calculation_reason** | **string**| De reden waarvoor de opzegvergoeding berekent is waarop gefilterd moet worden (indien gevuld) | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiContractTerminationFeeBase[]**](../Model/EcedoERPCRMInterfaceApiContractTerminationFeeBase.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysTerminationFeesGetTerminationFeesByInvoice**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiContractTerminationFeeBase[] sysTerminationFeesGetTerminationFeesByInvoice($invoice_id)

Haalt de gefactureerde opzegvergoedingen op voor een specifieke factuur

Deze API geeft de opzegvergoedingen terug die in een specifieke factuur in rekening zijn gebracht bij een klant.<br /><br />  Deze API kan gebruikt worden door leveranciers die zelf e-mails of pdf's genereren en daarin willen tonen welke opzegvergoedingen in rekening zijn gebracht.<br />  Deze API kan ook gebruikt worden om in een MijnPortaal te tonen welke opzegvergoedingen in een factuur in rekening zijn gebracht en op basis van welke gegevens deze opzegvergoedingen zijn berekend<br /><br />  De factuur waarvoor de opzegvergoedingen moeten worden opgehaald moet een eindafrekening (`final settlement`) of een aankoop factuur (`purchase`) van het subtype \"Opzegvergoeding\" (`TerminationFee`) zijn.

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

$apiInstance = new Swagger\Client\Api\SysTerminationFeesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$invoice_id = "invoice_id_example"; // string | De factuur waarvoor de opzegvergoedingen opgehaald moeten worden

try {
    $result = $apiInstance->sysTerminationFeesGetTerminationFeesByInvoice($invoice_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysTerminationFeesApi->sysTerminationFeesGetTerminationFeesByInvoice: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **string**| De factuur waarvoor de opzegvergoedingen opgehaald moeten worden |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiContractTerminationFeeBase[]**](../Model/EcedoERPCRMInterfaceApiContractTerminationFeeBase.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

