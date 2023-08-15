# Swagger\Client\SysResellerApi

All URIs are relative to *https://innova.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysResellerGetContractPrices**](SysResellerApi.md#sysResellerGetContractPrices) | **GET** /sysapi/v1.0/reseller/organizations/{organizationId}/proposedcontracts/{contractId}/prices | Verkrijg de prijzen van alle prijscomponenten van offertes
[**sysResellerGetContracts**](SysResellerApi.md#sysResellerGetContracts) | **GET** /sysapi/v1.0/reseller/{resellerOrganizationId}/contracts | Verkrijg de contracten van een wederverkoper
[**sysResellerGetOrganizations**](SysResellerApi.md#sysResellerGetOrganizations) | **GET** /sysapi/v1.0/reseller/resellerorganizations/{resellerOrganizationId}/organizations | Verkrijg de klanten van een wederverkoper
[**sysResellerGetProposedContracts**](SysResellerApi.md#sysResellerGetProposedContracts) | **GET** /sysapi/v1.0/reseller/resellerorganizations/{resellerOrganizationId}/proposedcontracts | Verkrijg offerte contracten
[**sysResellerPostContract**](SysResellerApi.md#sysResellerPostContract) | **POST** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/proposedcontracts | Post contract
[**sysResellerPostContractPrices**](SysResellerApi.md#sysResellerPostContractPrices) | **POST** /sysapi/v1.0/reseller/contracts/{contractId}/addresellerprices | Toevoegen van reseller prijzen per contract
[**sysResellerPostContractProposalApproved**](SysResellerApi.md#sysResellerPostContractProposalApproved) | **POST** /sysapi/v1.0/reseller/contracts/{contractId}/approveproposal | Post contract proposal approved
[**sysResellerSearch**](SysResellerApi.md#sysResellerSearch) | **GET** /sysapi/v1.0/reseller/search | Verkrijg de wederverkopers


# **sysResellerGetContractPrices**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionContractPrices[] sysResellerGetContractPrices($organization_id, $contract_id)

Verkrijg de prijzen van alle prijscomponenten van offertes

Retourneert alle contract- en propositie prijzen.

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

$apiInstance = new Swagger\Client\Api\SysResellerApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$contract_id = "contract_id_example"; // string | 

try {
    $result = $apiInstance->sysResellerGetContractPrices($organization_id, $contract_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysResellerApi->sysResellerGetContractPrices: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **contract_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionContractPrices[]**](../Model/EcedoERPCRMInterfaceApiConnectionContractPrices.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysResellerGetContracts**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiResellerContract[] sysResellerGetContracts($reseller_organization_id, $valid_on, $include_properties, $include_prices)

Verkrijg de contracten van een wederverkoper

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

$apiInstance = new Swagger\Client\Api\SysResellerApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$reseller_organization_id = "reseller_organization_id_example"; // string | 
$valid_on = new \DateTime("2013-10-20"); // \DateTime | Alleen contracten opleveren die geldig zijn op deze datum (optioneel)
$include_properties = true; // bool | Afspraken wel of niet opleveren
$include_prices = true; // bool | Prijzen wel of niet opleveren

try {
    $result = $apiInstance->sysResellerGetContracts($reseller_organization_id, $valid_on, $include_properties, $include_prices);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysResellerApi->sysResellerGetContracts: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reseller_organization_id** | **string**|  |
 **valid_on** | **\DateTime**| Alleen contracten opleveren die geldig zijn op deze datum (optioneel) | [optional]
 **include_properties** | **bool**| Afspraken wel of niet opleveren | [optional]
 **include_prices** | **bool**| Prijzen wel of niet opleveren | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiResellerContract[]**](../Model/EcedoERPCRMInterfaceApiResellerContract.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysResellerGetOrganizations**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganizationSearchResult sysResellerGetOrganizations($reseller_organization_id, $only_active)

Verkrijg de klanten van een wederverkoper

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

$apiInstance = new Swagger\Client\Api\SysResellerApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$reseller_organization_id = "reseller_organization_id_example"; // string | 
$only_active = true; // bool | 

try {
    $result = $apiInstance->sysResellerGetOrganizations($reseller_organization_id, $only_active);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysResellerApi->sysResellerGetOrganizations: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reseller_organization_id** | **string**|  |
 **only_active** | **bool**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganizationSearchResult**](../Model/EcedoERPCRMInterfaceApiOrganizationSearchResult.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysResellerGetProposedContracts**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiContract[] sysResellerGetProposedContracts($reseller_organization_id)

Verkrijg offerte contracten

Get Proposed Contracts; Retourneert alle contracten met de status ‘Proposed’ voor de betreffende reseller (zonder prijzen).

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

$apiInstance = new Swagger\Client\Api\SysResellerApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$reseller_organization_id = "reseller_organization_id_example"; // string | Id van de Reseller organization

try {
    $result = $apiInstance->sysResellerGetProposedContracts($reseller_organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysResellerApi->sysResellerGetProposedContracts: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reseller_organization_id** | **string**| Id van de Reseller organization |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiContract[]**](../Model/EcedoERPCRMInterfaceApiContract.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysResellerPostContract**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiContractPostResult sysResellerPostContract($organization_id, $connection_id, $contract, $skip_wait_for_approval)

Post contract

Hier wordt de propositie gecontroleerd en op basis hiervan de status van het contract op   ‘Proposed’ of ‘WaitForApproval’ gezet. Tevens wordt de ResellerOrganization gevuld.

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

$apiInstance = new Swagger\Client\Api\SysResellerApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$connection_id = "connection_id_example"; // string | 
$contract = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiResellerContractPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiResellerContractPostData | 
$skip_wait_for_approval = true; // bool | Als 'true' dan wordt status contract nooit op 'WaitForApproval' gezet; default 'false'

try {
    $result = $apiInstance->sysResellerPostContract($organization_id, $connection_id, $contract, $skip_wait_for_approval);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysResellerApi->sysResellerPostContract: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **connection_id** | **string**|  |
 **contract** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiResellerContractPostData**](../Model/EcedoERPCRMInterfaceApiResellerContractPostData.md)|  |
 **skip_wait_for_approval** | **bool**| Als &#39;true&#39; dan wordt status contract nooit op &#39;WaitForApproval&#39; gezet; default &#39;false&#39; | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiContractPostResult**](../Model/EcedoERPCRMInterfaceApiContractPostResult.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysResellerPostContractPrices**
> object sysResellerPostContractPrices($contract_id, $price_post_data)

Toevoegen van reseller prijzen per contract

De prijzen die de reseller bovenop de contract prijzen plaatst kunnen hier aangegeven worden samen met de geldigheid van de offerte  De toegevoegde prijzen zijn tevens de basis voor de uitkering die de reseller ontvangt per energielevering verbruik  Alle mogelijke prijzen per marktsegment moeten aanwezig zijn, voor gas contracten betekent dit een prijs voor `Base` en `FixedFee`  Voor elektriciteitscontracten betekent dit `Base`, `Peak`, ÒffPeak`, `BaseODN`, `PeakODN`, `OffPeakODN` en `FixedFee`

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

$apiInstance = new Swagger\Client\Api\SysResellerApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$contract_id = "contract_id_example"; // string | 
$price_post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiResellerContractPricePostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiResellerContractPricePostData | 

try {
    $result = $apiInstance->sysResellerPostContractPrices($contract_id, $price_post_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysResellerApi->sysResellerPostContractPrices: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **string**|  |
 **price_post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiResellerContractPricePostData**](../Model/EcedoERPCRMInterfaceApiResellerContractPricePostData.md)|  |

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysResellerPostContractProposalApproved**
> object sysResellerPostContractProposalApproved($contract_id, $approval_date)

Post contract proposal approved

Controleert of de datum dat de klant het voorstel heeft goedgekeurd voor de  ProposalValidUntil datum ligt en zo ja wijzigt de status van het contract in Active.

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

$apiInstance = new Swagger\Client\Api\SysResellerApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$contract_id = "contract_id_example"; // string | 
$approval_date = new \DateTime("2013-10-20"); // \DateTime | yyyy-mm-dd

try {
    $result = $apiInstance->sysResellerPostContractProposalApproved($contract_id, $approval_date);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysResellerApi->sysResellerPostContractProposalApproved: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **string**|  |
 **approval_date** | **\DateTime**| yyyy-mm-dd |

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysResellerSearch**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiResellerOrganization[] sysResellerSearch($organization_email_address)

Verkrijg de wederverkopers

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

$apiInstance = new Swagger\Client\Api\SysResellerApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_email_address = "organization_email_address_example"; // string | Primair e-mailadres van de reseller (exacte match)

try {
    $result = $apiInstance->sysResellerSearch($organization_email_address);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysResellerApi->sysResellerSearch: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_email_address** | **string**| Primair e-mailadres van de reseller (exacte match) | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiResellerOrganization[]**](../Model/EcedoERPCRMInterfaceApiResellerOrganization.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

