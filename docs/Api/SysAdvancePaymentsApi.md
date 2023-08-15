# Swagger\Client\SysAdvancePaymentsApi

All URIs are relative to *https://innova.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysAdvancePaymentsDelete**](SysAdvancePaymentsApi.md#sysAdvancePaymentsDelete) | **DELETE** /sysapi/v1.0/organizations/{organizationId}/advancepayments/{advancePaymentId} | Voorschot verwijderen
[**sysAdvancePaymentsGetAgreedAmountSupported**](SysAdvancePaymentsApi.md#sysAdvancePaymentsGetAgreedAmountSupported) | **GET** /sysapi/v1.0/organizations/{organizationId}/advancepayments/{clusterReference}/agreedamountsupported | Opvragen of het is toegestaan om een afgesproken voorschot bedrag in te stellen
[**sysAdvancePaymentsGetByAdvancePaymentId**](SysAdvancePaymentsApi.md#sysAdvancePaymentsGetByAdvancePaymentId) | **GET** /sysapi/v1.0/organizations/{organizationId}/advancepayments/{advancePaymentId} | Haal specifiek voorschot op
[**sysAdvancePaymentsGetByOrganizationId**](SysAdvancePaymentsApi.md#sysAdvancePaymentsGetByOrganizationId) | **GET** /sysapi/v1.0/organizations/{organizationId}/advancepayments | Haal voorschotten van een specifieke klant op
[**sysAdvancePaymentsPost**](SysAdvancePaymentsApi.md#sysAdvancePaymentsPost) | **POST** /sysapi/v1.0/organizations/{organizationId}/advancepayments | Nieuw voorschot aanmaken
[**sysAdvancePaymentsPut**](SysAdvancePaymentsApi.md#sysAdvancePaymentsPut) | **PUT** /sysapi/v1.0/organizations/{organizationId}/advancepayments/{advancePaymentId} | Voorschot wijzigen


# **sysAdvancePaymentsDelete**
> object sysAdvancePaymentsDelete($organization_id, $advance_payment_id, $reactivate_previous_advance_payment)

Voorschot verwijderen

De API geeft een lege 400 Bad Request terug wanneer organizationId en/of advancePaymentId niet bestaat.

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

$apiInstance = new Swagger\Client\Api\SysAdvancePaymentsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$advance_payment_id = "advance_payment_id_example"; // string | Guid van het voorschot (AdvancePayment)
$reactivate_previous_advance_payment = true; // bool | Geeft aan of het voorgaande voorschot opnieuw geactiveerd moet worden (alleen voorgesteld voorschot)

try {
    $result = $apiInstance->sysAdvancePaymentsDelete($organization_id, $advance_payment_id, $reactivate_previous_advance_payment);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysAdvancePaymentsApi->sysAdvancePaymentsDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **advance_payment_id** | **string**| Guid van het voorschot (AdvancePayment) |
 **reactivate_previous_advance_payment** | **bool**| Geeft aan of het voorgaande voorschot opnieuw geactiveerd moet worden (alleen voorgesteld voorschot) | [optional]

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysAdvancePaymentsGetAgreedAmountSupported**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiAgreedAmountSupportedResult sysAdvancePaymentsGetAgreedAmountSupported($organization_id, $cluster_reference, $start_date)

Opvragen of het is toegestaan om een afgesproken voorschot bedrag in te stellen

Afgesproken voorschot is niet toegestaan bij voorschotten met daadwerkelijk verbruik

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

$apiInstance = new Swagger\Client\Api\SysAdvancePaymentsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$cluster_reference = "cluster_reference_example"; // string | Cluster referentie
$start_date = new \DateTime("2013-10-20"); // \DateTime | (optioneel) Voorschotmaand; als deze niet wordt meegegeven dan wordt de eerstmogelijke startdatum van een nieuw voorschot bepaald en gebruikt

try {
    $result = $apiInstance->sysAdvancePaymentsGetAgreedAmountSupported($organization_id, $cluster_reference, $start_date);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysAdvancePaymentsApi->sysAdvancePaymentsGetAgreedAmountSupported: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **cluster_reference** | **string**| Cluster referentie |
 **start_date** | **\DateTime**| (optioneel) Voorschotmaand; als deze niet wordt meegegeven dan wordt de eerstmogelijke startdatum van een nieuw voorschot bepaald en gebruikt | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAgreedAmountSupportedResult**](../Model/EcedoERPCRMInterfaceApiAgreedAmountSupportedResult.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysAdvancePaymentsGetByAdvancePaymentId**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiAdvancePayment sysAdvancePaymentsGetByAdvancePaymentId($organization_id, $advance_payment_id, $include_connection_details, $do_combine_rows)

Haal specifiek voorschot op

De API geeft een lege 400 Bad Request terug wanneer organizationId en/of advancePaymentId niet bestaat<br />  Zie het responsemodel voor documentatie over de individuele velden

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

$apiInstance = new Swagger\Client\Api\SysAdvancePaymentsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$advance_payment_id = "advance_payment_id_example"; // string | Guid van het voorschot (AdvancePayment)
$include_connection_details = true; // bool | Default false. Vult het MarketSegment wanneer true, maar gaan ten koste van performance
$do_combine_rows = true; // bool | Default false. Zie Implementation Notes voor meer informatie

try {
    $result = $apiInstance->sysAdvancePaymentsGetByAdvancePaymentId($organization_id, $advance_payment_id, $include_connection_details, $do_combine_rows);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysAdvancePaymentsApi->sysAdvancePaymentsGetByAdvancePaymentId: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **advance_payment_id** | **string**| Guid van het voorschot (AdvancePayment) |
 **include_connection_details** | **bool**| Default false. Vult het MarketSegment wanneer true, maar gaan ten koste van performance | [optional]
 **do_combine_rows** | **bool**| Default false. Zie Implementation Notes voor meer informatie | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAdvancePayment**](../Model/EcedoERPCRMInterfaceApiAdvancePayment.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysAdvancePaymentsGetByOrganizationId**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiAdvancePayment[] sysAdvancePaymentsGetByOrganizationId($organization_id, $cluster_reference, $include_connection_details, $do_combine_rows)

Haal voorschotten van een specifieke klant op

Deze API geeft de voorschotten van een klant (Organization) terug. Toekomstige, actuele en historische.     #### Request  **doCombineRows: ** De resultset bevat alle voorschot-regels in de AdvancePaymentRows-array. Dit zijn alle losse prijscomponenten die berekend worden. <br />  Als geconfigureerd is dat bepaalde prijscomponenten niet aan klanten getoond mogen worden, maar in plaats waarvan bij andere componenten opgeteld moeten worden, dan zorgt de doCombineRows query parameter er voor dat de voorschotregels op dezelfde manier gecomineerd worden als bijvoorbeeld factuurregels.<br />  De gecombineerde regels zijn terug te vinden in CombinedAdvancePaymentRows-array in de response<br />                #### Response  De API geeft een lege lijst terug wanneer de klant onbekend is of wanneer de klant (of het cluster) geen voorschotten heeft<br />  Zie het responsemodel voor documentatie over de individuele velden

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

$apiInstance = new Swagger\Client\Api\SysAdvancePaymentsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$cluster_reference = "cluster_reference_example"; // string | Optioneel filter om alleen de voorschotten van dit cluster op te vragen
$include_connection_details = true; // bool | Default false. Vult het MarketSegment wanneer true, maar gaan ten koste van performance
$do_combine_rows = true; // bool | Default false. Zie Implementation Notes voor meer informatie

try {
    $result = $apiInstance->sysAdvancePaymentsGetByOrganizationId($organization_id, $cluster_reference, $include_connection_details, $do_combine_rows);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysAdvancePaymentsApi->sysAdvancePaymentsGetByOrganizationId: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **cluster_reference** | **string**| Optioneel filter om alleen de voorschotten van dit cluster op te vragen | [optional]
 **include_connection_details** | **bool**| Default false. Vult het MarketSegment wanneer true, maar gaan ten koste van performance | [optional]
 **do_combine_rows** | **bool**| Default false. Zie Implementation Notes voor meer informatie | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAdvancePayment[]**](../Model/EcedoERPCRMInterfaceApiAdvancePayment.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysAdvancePaymentsPost**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiAdvancePayment sysAdvancePaymentsPost($organization_id, $post_data)

Nieuw voorschot aanmaken

De API geeft een lege 400 Bad Request terug wanneer organizationId en/of advancePaymentId niet bestaat<br />  Zie het request- en responsemodel voor documentatie over de individuele velden<br />

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

$apiInstance = new Swagger\Client\Api\SysAdvancePaymentsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiAdvancePaymentPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiAdvancePaymentPostData | Informatie over het nieuwe voorschot ('Amount' veld is deprecated; gebruik in plaats hiervan 'AgreedAmount')

try {
    $result = $apiInstance->sysAdvancePaymentsPost($organization_id, $post_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysAdvancePaymentsApi->sysAdvancePaymentsPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAdvancePaymentPostData**](../Model/EcedoERPCRMInterfaceApiAdvancePaymentPostData.md)| Informatie over het nieuwe voorschot (&#39;Amount&#39; veld is deprecated; gebruik in plaats hiervan &#39;AgreedAmount&#39;) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAdvancePayment**](../Model/EcedoERPCRMInterfaceApiAdvancePayment.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysAdvancePaymentsPut**
> object sysAdvancePaymentsPut($organization_id, $advance_payment_id, $put_data)

Voorschot wijzigen

De API geeft een lege 400 Bad Request terug wanneer organizationId en/of advancePaymentId niet bestaat of wanneer het voorschot niet de status IsProposed heeft.<br /><br />  __Let op!__ Als een afgesproken bedrag (`AgreedAmount`) wordt meegestuurd, dan mag deze niet heel veel hoger zijn dan het berekende voorschot. Deze check is toegevoegd om invoerfouten en daarmee facturatiefouten te voorkomen.

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

$apiInstance = new Swagger\Client\Api\SysAdvancePaymentsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$advance_payment_id = "advance_payment_id_example"; // string | Guid van het voorschot (AdvancePayment)
$put_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiAdvancePaymentPutData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiAdvancePaymentPutData | 

try {
    $result = $apiInstance->sysAdvancePaymentsPut($organization_id, $advance_payment_id, $put_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysAdvancePaymentsApi->sysAdvancePaymentsPut: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **advance_payment_id** | **string**| Guid van het voorschot (AdvancePayment) |
 **put_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAdvancePaymentPutData**](../Model/EcedoERPCRMInterfaceApiAdvancePaymentPutData.md)|  |

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

