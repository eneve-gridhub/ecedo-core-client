# Swagger\Client\SysOrganizationsApi

All URIs are relative to *https://innova-test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysOrganizationsDelete**](SysOrganizationsApi.md#sysOrganizationsDelete) | **DELETE** /sysapi/v1.0/organizations/{organizationId} | Verwijdert een organisatie.
[**sysOrganizationsGetByClientReference**](SysOrganizationsApi.md#sysOrganizationsGetByClientReference) | **GET** /sysapi/v1.0/organizations/byClientReference/{clientReference} | Verkrijg klantgegevens op basis van een klantreferentie
[**sysOrganizationsGetByIdOrReference**](SysOrganizationsApi.md#sysOrganizationsGetByIdOrReference) | **GET** /sysapi/v1.0/organizations/{organizationId} | Haal specifieke klant op (op basis van OrganizationId)
[**sysOrganizationsGetByReferenceNew**](SysOrganizationsApi.md#sysOrganizationsGetByReferenceNew) | **GET** /sysapi/v1.0/organizations/byReference/{reference} | Verkrijg klantgegevens op basis van een klantnummer
[**sysOrganizationsPost**](SysOrganizationsApi.md#sysOrganizationsPost) | **POST** /sysapi/v1.0/organizations | Klant aanmaken
[**sysOrganizationsPut**](SysOrganizationsApi.md#sysOrganizationsPut) | **PUT** /sysapi/v1.0/organizations/{organizationId} | Klant wijzigen
[**sysOrganizationsSearch**](SysOrganizationsApi.md#sysOrganizationsSearch) | **GET** /sysapi/v1.0/organizations/search | Klanten zoeken


# **sysOrganizationsDelete**
> sysOrganizationsDelete($organization_id)

Verwijdert een organisatie.

Deze API verwijdert een organisatie.<br /><br />  De API kan de volgende specifieke (400) codes teruggeven:<br />  **19001**: Klanten met facturen kunnen niet verwijderd worden<br />  **19002**: De klant kan niet verwijderd worden omdat er nog actieve workflows zijn<br />  **19003**: Klanten met productunits kunnen niet verwijderd worden<br />  **19004**: De klant kan niet verwijderd worden omdat er aansluitingen zijn met een switchperiode<br />  **19005**: De klant kan niet verwijderd worden omdat er nog onverwerkte e-mails aanwezig zijn<br />  **19006**: De klant kan niet verwijderd worden omdat er nog onverwerkte triggers aanwezig zijn<br />  **19007**: Klanten met productiemiddelen kunnen niet verwijderd worden<br />

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

$apiInstance = new Swagger\Client\Api\SysOrganizationsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Het id van de organisatie die verwijderd dient te worden

try {
    $apiInstance->sysOrganizationsDelete($organization_id);
} catch (Exception $e) {
    echo 'Exception when calling SysOrganizationsApi->sysOrganizationsDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Het id van de organisatie die verwijderd dient te worden |

### Return type

void (empty response body)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysOrganizationsGetByClientReference**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganization sysOrganizationsGetByClientReference($client_reference)

Verkrijg klantgegevens op basis van een klantreferentie

Opvragen klantgegevens op basis van een klantreferentie<br /><br />

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

$apiInstance = new Swagger\Client\Api\SysOrganizationsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$client_reference = "client_reference_example"; // string | Een exact overeenkomende klantreferentie

try {
    $result = $apiInstance->sysOrganizationsGetByClientReference($client_reference);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysOrganizationsApi->sysOrganizationsGetByClientReference: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_reference** | **string**| Een exact overeenkomende klantreferentie |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganization**](../Model/EcedoERPCRMInterfaceApiOrganization.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysOrganizationsGetByIdOrReference**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganization sysOrganizationsGetByIdOrReference($organization_id)

Haal specifieke klant op (op basis van OrganizationId)

Opvragen van een specifieke klant (op basis van OrganizationId)<br /><br />

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

$apiInstance = new Swagger\Client\Api\SysOrganizationsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)

try {
    $result = $apiInstance->sysOrganizationsGetByIdOrReference($organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysOrganizationsApi->sysOrganizationsGetByIdOrReference: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganization**](../Model/EcedoERPCRMInterfaceApiOrganization.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysOrganizationsGetByReferenceNew**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganization sysOrganizationsGetByReferenceNew($reference)

Verkrijg klantgegevens op basis van een klantnummer

Opvragen klantgegevens op basis van een klantnummer<br /><br />

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

$apiInstance = new Swagger\Client\Api\SysOrganizationsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$reference = "reference_example"; // string | Een exact overeenkomend klantnummer

try {
    $result = $apiInstance->sysOrganizationsGetByReferenceNew($reference);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysOrganizationsApi->sysOrganizationsGetByReferenceNew: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference** | **string**| Een exact overeenkomend klantnummer |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganization**](../Model/EcedoERPCRMInterfaceApiOrganization.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysOrganizationsPost**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganizationPostResult sysOrganizationsPost($organization)

Klant aanmaken

Het aanmaken van een klant.

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

$apiInstance = new Swagger\Client\Api\SysOrganizationsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganizationPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganizationPostData | 

try {
    $result = $apiInstance->sysOrganizationsPost($organization);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysOrganizationsApi->sysOrganizationsPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganizationPostData**](../Model/EcedoERPCRMInterfaceApiOrganizationPostData.md)|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganizationPostResult**](../Model/EcedoERPCRMInterfaceApiOrganizationPostResult.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysOrganizationsPut**
> object sysOrganizationsPut($organization_id, $organization)

Klant wijzigen

Het wijzigen van een klant.

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

$apiInstance = new Swagger\Client\Api\SysOrganizationsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$organization = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganizationPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganizationPostData | 

try {
    $result = $apiInstance->sysOrganizationsPut($organization_id, $organization);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysOrganizationsApi->sysOrganizationsPut: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **organization** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganizationPostData**](../Model/EcedoERPCRMInterfaceApiOrganizationPostData.md)|  |

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysOrganizationsSearch**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganizationSearchResult sysOrganizationsSearch($organization_reference, $organization_address_number, $organization_address_addition, $organization_address_zip_code, $organization_email_address, $organization_phone_number, $organization_group_id, $organization_type, $organization_sub_type, $kvk_number, $parent_organization_id, $is_parent_organization, $include_connections, $reseller_id, $connection_ean, $organization_name, $company_label_id)

Klanten zoeken

API waarmee gezocht kan worden in het klantenbestand    #### Request  Als meerdere zoekparameters worden meegegeven dan bevat het resultaat alleen de klanten (`Organizations`) waarbij al deze parameters van toepassing zijn.<br />  Een klant in Ecedo geregistreerd staat onder KvK nummer 123456 en huisnummer 12, zal niet gevonden worden wanneer gezocht wordt op KvK nummer 123456 en huisnummer 33.<br /><br />  De parameter `includeConnections` heeft een grote impact op de manier waarop gezocht wordt en de inhoud van de response. Wanneer deze parameters op `true` staat wordt bij het zoeken op adresgegevens niet alleen naar de klanten, maar ook in de adresgegevens van aansluitingen.  Daarnaast zullen de organization-response-objecten voorzien zijn van aansluitingen met een grote set van details per aansluiting.<br />  Doordat een diepere boom doorzocht moet worden en de resultset groter is, heeft het gebruik van deze query parameter negatieve impact op de performance van deze API<br />    #### Response  Het aantal klant-objecten dat in de response teruggegeven kan worden is gelimiteerd. Wanneer `includeConnection` de waarde `false` heeft kunnen er maximaal 100 klantobjecten geretourneerd worden. In het geval van `true` wordt de limiet teruggebracht naar 25.  Als het maximaal aantal gevonden klant-objecten wordt overschreven zal de API een `400 bad request` met de body \"Too many results\" teruggeven.<br />  Als er geen resultaten zijn wordt een lege array teruggegeven

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

$apiInstance = new Swagger\Client\Api\SysOrganizationsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_reference = "organization_reference_example"; // string | Klantnummer (like-search)
$organization_address_number = 56; // int | Huisnummer van klantadres en/of aansluitingadres (exacte match)
$organization_address_addition = "organization_address_addition_example"; // string | Huisnummertoevoeging van klantadres en/of aansluitingadres (exacte match)
$organization_address_zip_code = "organization_address_zip_code_example"; // string | Postcode van klantadres en/of aansluitingadres (like-search). Nederlandse postcodes mogen of zonder spatie ingestuurd worden. Beide opties zijn geldig.
$organization_email_address = "organization_email_address_example"; // string | Primair e-mailadres van de klant (like-search)
$organization_phone_number = "organization_phone_number_example"; // string | Het zoeken op telefoonnummer wordt gedaan door te kijken of het vaste of mobiele nummer eindigt met de ingevoerde cijfers. Daardoor is het mogelijk om alleen op de laatse 9 getallen te zoeken en daarmee niet afhankelijk te zijn van eventuele landcode-notaties. De input moet alleen getallen bevatten, dus geen spaties of andere karakters
$organization_group_id = "organization_group_id_example"; // string | Klanten kunnen ingedeeld worden in klantgroepen. Met behulp van deze optionele parameter kan gezocht worden naar klanten in een specifieke klantgroep
$organization_type = "organization_type_example"; // string | Optionele parameter waarmee gefilterd kan worden op zakelijke of particuliere klanten
$organization_sub_type = "organization_sub_type_example"; // string | Een van de volgende waarden: Reseller (wederverkoper), Producer (Producent), Msp (Mobility Service Provider), Cpo (Charge Point Operator)
$kvk_number = "kvk_number_example"; // string | KvK-nummer (like-search)
$parent_organization_id = "parent_organization_id_example"; // string | Het organizationId van een moeder-organisatie (exacte match)
$is_parent_organization = true; // bool | Optionele boolean waarmee aangegeven kan worden dat specifiek wel of niet op moederorganisaties gezocht moet worden. Default: geen waarde, waardoor zowel moeders als dochters worden gevonden
$include_connections = true; // bool | Boolean (default false) waarmee aangegeven kan worden dat ook in adressen van aansluitingen gezocht moet worden
$reseller_id = "reseller_id_example"; // string | Optioneel organizationId van een wederverkoper (zie de `SysReseller` categorie voor meer informatie). Als `resellerId` wordt meegegeven worden alleen klanten in het resultaat opgenomen met een actief of toekomstig contract voor deze wederverkoper.
$connection_ean = "connection_ean_example"; // string | Optionele parameter waarmee gezocht kan worden naar EANs. Dit is een like-search die alleen wordt uitgevoerd wanneer de parameter includeConnections de waarde true heeft
$organization_name = "organization_name_example"; // string | Optionele parameter waarmee gezocht kan worden naar een specifieke klantnaam. Dit is een like-search
$company_label_id = "company_label_id_example"; // string | De labelId van de klant

try {
    $result = $apiInstance->sysOrganizationsSearch($organization_reference, $organization_address_number, $organization_address_addition, $organization_address_zip_code, $organization_email_address, $organization_phone_number, $organization_group_id, $organization_type, $organization_sub_type, $kvk_number, $parent_organization_id, $is_parent_organization, $include_connections, $reseller_id, $connection_ean, $organization_name, $company_label_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysOrganizationsApi->sysOrganizationsSearch: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_reference** | **string**| Klantnummer (like-search) | [optional]
 **organization_address_number** | **int**| Huisnummer van klantadres en/of aansluitingadres (exacte match) | [optional]
 **organization_address_addition** | **string**| Huisnummertoevoeging van klantadres en/of aansluitingadres (exacte match) | [optional]
 **organization_address_zip_code** | **string**| Postcode van klantadres en/of aansluitingadres (like-search). Nederlandse postcodes mogen of zonder spatie ingestuurd worden. Beide opties zijn geldig. | [optional]
 **organization_email_address** | **string**| Primair e-mailadres van de klant (like-search) | [optional]
 **organization_phone_number** | **string**| Het zoeken op telefoonnummer wordt gedaan door te kijken of het vaste of mobiele nummer eindigt met de ingevoerde cijfers. Daardoor is het mogelijk om alleen op de laatse 9 getallen te zoeken en daarmee niet afhankelijk te zijn van eventuele landcode-notaties. De input moet alleen getallen bevatten, dus geen spaties of andere karakters | [optional]
 **organization_group_id** | [**string**](../Model/.md)| Klanten kunnen ingedeeld worden in klantgroepen. Met behulp van deze optionele parameter kan gezocht worden naar klanten in een specifieke klantgroep | [optional]
 **organization_type** | **string**| Optionele parameter waarmee gefilterd kan worden op zakelijke of particuliere klanten | [optional]
 **organization_sub_type** | **string**| Een van de volgende waarden: Reseller (wederverkoper), Producer (Producent), Msp (Mobility Service Provider), Cpo (Charge Point Operator) | [optional]
 **kvk_number** | **string**| KvK-nummer (like-search) | [optional]
 **parent_organization_id** | [**string**](../Model/.md)| Het organizationId van een moeder-organisatie (exacte match) | [optional]
 **is_parent_organization** | **bool**| Optionele boolean waarmee aangegeven kan worden dat specifiek wel of niet op moederorganisaties gezocht moet worden. Default: geen waarde, waardoor zowel moeders als dochters worden gevonden | [optional]
 **include_connections** | **bool**| Boolean (default false) waarmee aangegeven kan worden dat ook in adressen van aansluitingen gezocht moet worden | [optional]
 **reseller_id** | [**string**](../Model/.md)| Optioneel organizationId van een wederverkoper (zie de &#x60;SysReseller&#x60; categorie voor meer informatie). Als &#x60;resellerId&#x60; wordt meegegeven worden alleen klanten in het resultaat opgenomen met een actief of toekomstig contract voor deze wederverkoper. | [optional]
 **connection_ean** | **string**| Optionele parameter waarmee gezocht kan worden naar EANs. Dit is een like-search die alleen wordt uitgevoerd wanneer de parameter includeConnections de waarde true heeft | [optional]
 **organization_name** | **string**| Optionele parameter waarmee gezocht kan worden naar een specifieke klantnaam. Dit is een like-search | [optional]
 **company_label_id** | [**string**](../Model/.md)| De labelId van de klant | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganizationSearchResult**](../Model/EcedoERPCRMInterfaceApiOrganizationSearchResult.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

