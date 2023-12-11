# Swagger\Client\SysBillingItemsApi

All URIs are relative to *https://innova-test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysBillingItemsActivate**](SysBillingItemsApi.md#sysBillingItemsActivate) | **POST** /sysapi/v1.0/organizations/{organizationId}/billingitems/{billingItemId}/activate | Markeer factuuritem als geactiveerd
[**sysBillingItemsCancel**](SysBillingItemsApi.md#sysBillingItemsCancel) | **POST** /sysapi/v1.0/organizations/{organizationId}/billingitems/{billingItemId}/cancel | Markeer factuuritem als gedeactiveerd
[**sysBillingItemsDelete**](SysBillingItemsApi.md#sysBillingItemsDelete) | **DELETE** /sysapi/v1.0/organizations/{organizationId}/billingitems/{billingItemId} | Markeer factuuritem als verwijderd
[**sysBillingItemsGetBillingItemGroups**](SysBillingItemsApi.md#sysBillingItemsGetBillingItemGroups) | **GET** /sysapi/v1.0/billingItemGroups | Haal factuuritemgroepen op
[**sysBillingItemsGetByBillingItemId**](SysBillingItemsApi.md#sysBillingItemsGetByBillingItemId) | **GET** /sysapi/v1.0/organizations/{organizationId}/billingitems/{billingItemId} | 
[**sysBillingItemsGetByOrganizationId**](SysBillingItemsApi.md#sysBillingItemsGetByOrganizationId) | **GET** /sysapi/v1.0/organizations/{organizationId}/billingitems | Haal factuuritems van een specifieke klant op
[**sysBillingItemsPost**](SysBillingItemsApi.md#sysBillingItemsPost) | **POST** /sysapi/v1.0/organizations/{organizationId}/billingitems | Nieuw factuuritem aanmaken
[**sysBillingItemsPut**](SysBillingItemsApi.md#sysBillingItemsPut) | **PUT** /sysapi/v1.0/organizations/{organizationId}/billingitems/{billingItemId} | Wijzig een specifiek factuuritem


# **sysBillingItemsActivate**
> object sysBillingItemsActivate($billing_item_id, $organization_id, $comment)

Markeer factuuritem als geactiveerd

Met behulp van deze API kan een geannuleerd (status `Geannuleerd`) factuuritem (`BillingItem)` opnieuw worden geactiveerd, waardoor deze de status `Aangemaakt` krijgt.<br />  Als het geannuleerd een andere status heeft geeft de API een foutmelding terug.<br />

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

$apiInstance = new Swagger\Client\Api\SysBillingItemsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$billing_item_id = "billing_item_id_example"; // string | Guid van het factuuritem (BillingItem)
$organization_id = "organization_id_example"; // string | 
$comment = "comment_example"; // string | Optionele reden waarom het factuuritem opnieuw geactiveerd is

try {
    $result = $apiInstance->sysBillingItemsActivate($billing_item_id, $organization_id, $comment);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysBillingItemsApi->sysBillingItemsActivate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_item_id** | **string**| Guid van het factuuritem (BillingItem) |
 **organization_id** | **string**|  |
 **comment** | **string**| Optionele reden waarom het factuuritem opnieuw geactiveerd is | [optional]

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysBillingItemsCancel**
> object sysBillingItemsCancel($billing_item_id, $comment, $organization_id)

Markeer factuuritem als gedeactiveerd

Met behulp van deze API kan een factuuritem (`BillingItem`) worden geannuleerd.<br />  Als het factuuritem nog niet gebruikt is (status `Aangemaakt`) dan wordt het factuuritem geannuleerd (status `Geannuleerd`).<br />  Als het factuuritem een andere status heeft geeft de API een foutmelding terug.<br />

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

$apiInstance = new Swagger\Client\Api\SysBillingItemsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$billing_item_id = "billing_item_id_example"; // string | Guid van het factuuritem (BillingItem)
$comment = "comment_example"; // string | Verplichte reden waarom het factuuritem geannuleerd is
$organization_id = "organization_id_example"; // string | 

try {
    $result = $apiInstance->sysBillingItemsCancel($billing_item_id, $comment, $organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysBillingItemsApi->sysBillingItemsCancel: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_item_id** | **string**| Guid van het factuuritem (BillingItem) |
 **comment** | **string**| Verplichte reden waarom het factuuritem geannuleerd is |
 **organization_id** | **string**|  |

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysBillingItemsDelete**
> object sysBillingItemsDelete($billing_item_id, $organization_id, $comment)

Markeer factuuritem als verwijderd

Met behulp van deze API kan een factuuritem (`BillingItem`) worden verwijderd. Wat er precies gebeurt is afhangelijk van de status van het factuuritem.<br />  Als het factuuritem nog niet is gebruikt dan wordt het BillingItem volledig verwijderd<br />  Als het factuuritem al gefactureerd is dan wordt deze gemarkeerd als verwijderd (het item krijgt de status `Verwijderd`). Op deze manier blijft het factuuritem bestaan zodat de financiele administratie blijft kloppen. Als de parameter `comment` gevuld is wordt deze opmerking opgeslagen bij het factuuritem zodat later opgezocht kan worden wat de reden voor de verwijdering wa.<br />  Als het factuuritem een andere dan de twee bovenstaande statussen heeft geeft de API een foutmelding terug.<br />

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

$apiInstance = new Swagger\Client\Api\SysBillingItemsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$billing_item_id = "billing_item_id_example"; // string | Guid van het factuuritem (BillingItem)
$organization_id = "organization_id_example"; // string | 
$comment = "comment_example"; // string | Optionele reden waarom het factuuritem is verwijderd

try {
    $result = $apiInstance->sysBillingItemsDelete($billing_item_id, $organization_id, $comment);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysBillingItemsApi->sysBillingItemsDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_item_id** | **string**| Guid van het factuuritem (BillingItem) |
 **organization_id** | **string**|  |
 **comment** | **string**| Optionele reden waarom het factuuritem is verwijderd | [optional]

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysBillingItemsGetBillingItemGroups**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiBillingItemGroup[] sysBillingItemsGetBillingItemGroups($start_date, $end_date, $valid_on)

Haal factuuritemgroepen op

Factuuritemgroepen (`BillingItemGroups`) zijn voorgedefinieerde kortingen die aan een klant gekoppeld kunnen worden. Deze koppeling resulteert in een factuuritem (`BillingItem`). Met behulp van deze API kunnen alle factuuritemgroepen opgevraagd worden.    #### Request  Als validOn ingevuld is, mogen start- en einddatum niet ingevuld zijn.<br />  Als startdatum ingevuld is, mag validOn niet ingevuld zijn, maar einddatum wel.<br />  Als eindatum ingevuld is, moet startdatum ingevuld zijn, maar mag validOn niet ingevuld zijn.<br />

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

$apiInstance = new Swagger\Client\Api\SysBillingItemsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$start_date = new \DateTime("2013-10-20"); // \DateTime | Hierdoor worden alleen factuuritemgroepen teruggegeven die geldig (actief) zijn vanaf de opgegeven datum
$end_date = new \DateTime("2013-10-20"); // \DateTime | Hierdoor worden alleen factuuritemgroepen teruggegeven die geldig (actief) zijn tot de opgegeven datum
$valid_on = new \DateTime("2013-10-20"); // \DateTime | Hierdoor worden alleen factuuritemgroepen teruggegeven die geldig (actief) zijn op de opgegeven datum

try {
    $result = $apiInstance->sysBillingItemsGetBillingItemGroups($start_date, $end_date, $valid_on);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysBillingItemsApi->sysBillingItemsGetBillingItemGroups: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **\DateTime**| Hierdoor worden alleen factuuritemgroepen teruggegeven die geldig (actief) zijn vanaf de opgegeven datum | [optional]
 **end_date** | **\DateTime**| Hierdoor worden alleen factuuritemgroepen teruggegeven die geldig (actief) zijn tot de opgegeven datum | [optional]
 **valid_on** | **\DateTime**| Hierdoor worden alleen factuuritemgroepen teruggegeven die geldig (actief) zijn op de opgegeven datum | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiBillingItemGroup[]**](../Model/EcedoERPCRMInterfaceApiBillingItemGroup.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysBillingItemsGetByBillingItemId**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiBillingItem sysBillingItemsGetByBillingItemId($organization_id, $billing_item_id)



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

$apiInstance = new Swagger\Client\Api\SysBillingItemsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$billing_item_id = "billing_item_id_example"; // string | 

try {
    $result = $apiInstance->sysBillingItemsGetByBillingItemId($organization_id, $billing_item_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysBillingItemsApi->sysBillingItemsGetByBillingItemId: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **billing_item_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiBillingItem**](../Model/EcedoERPCRMInterfaceApiBillingItem.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysBillingItemsGetByOrganizationId**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiBillingItem[] sysBillingItemsGetByOrganizationId($organization_id, $external_reference, $status, $sub_type)

Haal factuuritems van een specifieke klant op

Met behulp van deze API kunnen de factuuritems (`BillingItems`) van een klant opgehaald worden.<br />  Door gebruik te maken van de optionele parameters kan het resultaat gefilterd worden.<br />

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

$apiInstance = new Swagger\Client\Api\SysBillingItemsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$external_reference = "external_reference_example"; // string | Een factuuritem kan aangemaakt worden met een externalReference. Als deze parameter gevuld is worden alleen factuuritems teruggegeven met een identieke externalReference
$status = "status_example"; // string | Hierdoor worden alleen factuuritems teruggegevens met deze specifieke status
$sub_type = "sub_type_example"; // string | Hierdoor worden alleen factuuritems teruggegevens met dit specifieke subtype

try {
    $result = $apiInstance->sysBillingItemsGetByOrganizationId($organization_id, $external_reference, $status, $sub_type);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysBillingItemsApi->sysBillingItemsGetByOrganizationId: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **external_reference** | **string**| Een factuuritem kan aangemaakt worden met een externalReference. Als deze parameter gevuld is worden alleen factuuritems teruggegeven met een identieke externalReference | [optional]
 **status** | **string**| Hierdoor worden alleen factuuritems teruggegevens met deze specifieke status | [optional]
 **sub_type** | **string**| Hierdoor worden alleen factuuritems teruggegevens met dit specifieke subtype | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiBillingItem[]**](../Model/EcedoERPCRMInterfaceApiBillingItem.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysBillingItemsPost**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiBillingItemPostResult sysBillingItemsPost($organization_id, $billing_item)

Nieuw factuuritem aanmaken

Met behulp van deze API kan een factuuritem (`BillingItem`) aangemaakt worden.

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

$apiInstance = new Swagger\Client\Api\SysBillingItemsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$billing_item = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiBillingItemPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiBillingItemPostData | De data van het factuuritem, zie het object-model voor meer informatie

try {
    $result = $apiInstance->sysBillingItemsPost($organization_id, $billing_item);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysBillingItemsApi->sysBillingItemsPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **billing_item** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiBillingItemPostData**](../Model/EcedoERPCRMInterfaceApiBillingItemPostData.md)| De data van het factuuritem, zie het object-model voor meer informatie |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiBillingItemPostResult**](../Model/EcedoERPCRMInterfaceApiBillingItemPostResult.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysBillingItemsPut**
> object sysBillingItemsPut($billing_item_id, $billing_item, $organization_id)

Wijzig een specifiek factuuritem

Met behulp van deze API kan een factuuritem (`BillingItem`) gewijzigd worden.

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

$apiInstance = new Swagger\Client\Api\SysBillingItemsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$billing_item_id = "billing_item_id_example"; // string | Guid van het factuuritem (BillingItem)
$billing_item = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiBillingItemPutData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiBillingItemPutData | De data van het factuuritem, zie het object-model voor meer informatie
$organization_id = "organization_id_example"; // string | 

try {
    $result = $apiInstance->sysBillingItemsPut($billing_item_id, $billing_item, $organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysBillingItemsApi->sysBillingItemsPut: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_item_id** | **string**| Guid van het factuuritem (BillingItem) |
 **billing_item** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiBillingItemPutData**](../Model/EcedoERPCRMInterfaceApiBillingItemPutData.md)| De data van het factuuritem, zie het object-model voor meer informatie |
 **organization_id** | **string**|  |

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

