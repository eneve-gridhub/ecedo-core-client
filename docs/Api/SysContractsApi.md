# Swagger\Client\SysContractsApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysContractsCreateOnbalansFlexContract**](SysContractsApi.md#sysContractsCreateOnbalansFlexContract) | **POST** /sysapi/v1.0/organizations/{organizationId}/onbalansflexcontracts | Toevoegen van een onbalansflex contract
[**sysContractsDeleteContract**](SysContractsApi.md#sysContractsDeleteContract) | **DELETE** /sysapi/v1.0/organizations/{organizationId}/contracts/{contractId} | Verwijderen van een contract
[**sysContractsDeleteContractProperties**](SysContractsApi.md#sysContractsDeleteContractProperties) | **DELETE** /sysapi/v1.0/organizations/{organizationId}/contracts/{contractId}/contractproperties/{contractPropertyType} | Verwijder een contract property
[**sysContractsEditOnbalansFlexContract**](SysContractsApi.md#sysContractsEditOnbalansFlexContract) | **PUT** /sysapi/v1.0/organizations/{organizationId}/onbalansflexcontracts/{contractId} | Wijzigen van een onbalansflex contract
[**sysContractsGetChargeContractById**](SysContractsApi.md#sysContractsGetChargeContractById) | **GET** /sysapi/v1.0/organizations/{organizationId}/chargecardcontracts/{contractId} | Ophalen van een laadpascontract op basis van contractId
[**sysContractsGetConnectionContracts**](SysContractsApi.md#sysContractsGetConnectionContracts) | **GET** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/connectioncontracts | Aansluitingcontracten ophalen van een aansluiting
[**sysContractsGetContracts**](SysContractsApi.md#sysContractsGetContracts) | **GET** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/contracts | Energieleveringcontracten ophalen van een aansluiting
[**sysContractsGetEnergieInkoopContract**](SysContractsApi.md#sysContractsGetEnergieInkoopContract) | **GET** /sysapi/v1.0/organizations/{organizationId}/energieinkoopcontracts/{contractId} | Ophalen van een energieinkoopcontract op basis van contractId
[**sysContractsGetEnergieleveringConnectionContractForContract**](SysContractsApi.md#sysContractsGetEnergieleveringConnectionContractForContract) | **GET** /sysapi/v1.0/organizations/{organizationId}/energieleveringconnectioncontracts/{contractId} | Ophalen van energieleveringconnectioncontract op basis van contractId
[**sysContractsGetEnergieleveringConnectionContracts**](SysContractsApi.md#sysContractsGetEnergieleveringConnectionContracts) | **GET** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/energieleveringconnectioncontracts | Energieleveringaansluitingcontracten ophalen van een aansluiting
[**sysContractsGetMeeliftConnectionContractForContract**](SysContractsApi.md#sysContractsGetMeeliftConnectionContractForContract) | **GET** /sysapi/v1.0/organizations/{organizationId}/meeliftconnectioncontracts/{contractId} | Ophalen van meeliftconnectioncontract op basis van contractId
[**sysContractsGetMeeliftConnectionContracts**](SysContractsApi.md#sysContractsGetMeeliftConnectionContracts) | **GET** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/meeliftconnectioncontracts | Meeliftaansluitingcontracten ophalen van een aansluiting
[**sysContractsGetMeeliftContracts**](SysContractsApi.md#sysContractsGetMeeliftContracts) | **GET** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/meeliftcontracts | Meeliftcontracten ophalen van een aansluiting
[**sysContractsGetOnbalansFlexContract**](SysContractsApi.md#sysContractsGetOnbalansFlexContract) | **GET** /sysapi/v1.0/organizations/{organizationId}/onbalansflexcontracts/{contractId} | Ophalen van een onbalansflex contract
[**sysContractsInvoiceContracts**](SysContractsApi.md#sysContractsInvoiceContracts) | **GET** /sysapi/v1.0/organizations/{organizationId}/invoices/{invoiceId}/contracts | Verkrijg de energielevering contracten die in een factuur zijn gefactureerd.  Een niet energielevering factuur zal een lege lijst retourneren.  Eventuele Meeliftcontracten worden niet geretourneerd
[**sysContractsPostContractProperties**](SysContractsApi.md#sysContractsPostContractProperties) | **POST** /sysapi/v1.0/organizations/{organizationId}/contracts/{contractId}/contractproperties | Pas een contract property aan
[**sysContractsPostContracts**](SysContractsApi.md#sysContractsPostContracts) | **POST** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/contracts | Energieleveringcontract aanmaken
[**sysContractsPostSwitchProducer**](SysContractsApi.md#sysContractsPostSwitchProducer) | **POST** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/switchproducer | Veranderen van producent op een aansluiting
[**sysContractsPutContracts**](SysContractsApi.md#sysContractsPutContracts) | **PUT** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/contracts/{contractId} | Energieleveringcontract wijzigen


# **sysContractsCreateOnbalansFlexContract**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiOnbalansFlexContractPostResult sysContractsCreateOnbalansFlexContract($organization_id, $data)

Toevoegen van een onbalansflex contract

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant
$data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiOnbalansFlexContractPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiOnbalansFlexContractPostData | data gebruikt om het contract aan te kunnen maken

try {
    $result = $apiInstance->sysContractsCreateOnbalansFlexContract($organization_id, $data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsCreateOnbalansFlexContract: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant |
 **data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiOnbalansFlexContractPostData**](../Model/EcedoERPCRMInterfaceApiOnbalansFlexContractPostData.md)| data gebruikt om het contract aan te kunnen maken |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiOnbalansFlexContractPostResult**](../Model/EcedoERPCRMInterfaceApiOnbalansFlexContractPostResult.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsDeleteContract**
> object sysContractsDeleteContract($organization_id, $contract_id)

Verwijderen van een contract

Verwijderen van contract {contractId}

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$contract_id = "contract_id_example"; // string | 

try {
    $result = $apiInstance->sysContractsDeleteContract($organization_id, $contract_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsDeleteContract: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **contract_id** | **string**|  |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsDeleteContractProperties**
> object sysContractsDeleteContractProperties($organization_id, $contract_id, $contract_property_type)

Verwijder een contract property

De volgende properties kunnen verwijderd worden: HasTerminationFee, SettlementInvoiceFrequency, HasAdvancePaymentCalculation, MaxODNLimitTariff, ElectricityGreeningOption, GasGreeningOption, AdvancePaymentScheme, NoticePeriod, HasRollingDeposit, HasTariffChangeMeterReadings

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$contract_id = "contract_id_example"; // string | 
$contract_property_type = "contract_property_type_example"; // string | 

try {
    $result = $apiInstance->sysContractsDeleteContractProperties($organization_id, $contract_id, $contract_property_type);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsDeleteContractProperties: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **contract_id** | **string**|  |
 **contract_property_type** | **string**|  |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsEditOnbalansFlexContract**
> object sysContractsEditOnbalansFlexContract($organization_id, $contract_id, $data)

Wijzigen van een onbalansflex contract

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant
$contract_id = "contract_id_example"; // string | Guid van het te wijzigen contract
$data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiOnbalansFlexContractPutData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiOnbalansFlexContractPutData | data wat gewijzigd moet worden

try {
    $result = $apiInstance->sysContractsEditOnbalansFlexContract($organization_id, $contract_id, $data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsEditOnbalansFlexContract: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant |
 **contract_id** | **string**| Guid van het te wijzigen contract |
 **data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiOnbalansFlexContractPutData**](../Model/EcedoERPCRMInterfaceApiOnbalansFlexContractPutData.md)| data wat gewijzigd moet worden |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsGetChargeContractById**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiEvChargeCardContract sysContractsGetChargeContractById($organization_id, $contract_id)

Ophalen van een laadpascontract op basis van contractId

Met deze api call kan een laadpascontract worden opgehaald op basis van het contractId

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$contract_id = "contract_id_example"; // string | 

try {
    $result = $apiInstance->sysContractsGetChargeContractById($organization_id, $contract_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsGetChargeContractById: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **contract_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiEvChargeCardContract**](../Model/EcedoERPCRMInterfaceApiEvChargeCardContract.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsGetConnectionContracts**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionContract[] sysContractsGetConnectionContracts($connection_id, $organization_id)

Aansluitingcontracten ophalen van een aansluiting

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$connection_id = "connection_id_example"; // string | 
$organization_id = "organization_id_example"; // string | 

try {
    $result = $apiInstance->sysContractsGetConnectionContracts($connection_id, $organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsGetConnectionContracts: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **string**|  |
 **organization_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionContract[]**](../Model/EcedoERPCRMInterfaceApiConnectionContract.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsGetContracts**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiContract[] sysContractsGetContracts($connection_id, $organization_id)

Energieleveringcontracten ophalen van een aansluiting

Alleen contracten met status 'Actief' en 'Afgerond' worden opgeleverd

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$connection_id = "connection_id_example"; // string | 
$organization_id = "organization_id_example"; // string | 

try {
    $result = $apiInstance->sysContractsGetContracts($connection_id, $organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsGetContracts: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **string**|  |
 **organization_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiContract[]**](../Model/EcedoERPCRMInterfaceApiContract.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsGetEnergieInkoopContract**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiEnergieInkoopContract sysContractsGetEnergieInkoopContract($organization_id, $contract_id)

Ophalen van een energieinkoopcontract op basis van contractId

Met deze api call kan een energieinkoopcontract worden opgehaald op basis van het contractid

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$contract_id = "contract_id_example"; // string | 

try {
    $result = $apiInstance->sysContractsGetEnergieInkoopContract($organization_id, $contract_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsGetEnergieInkoopContract: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **contract_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiEnergieInkoopContract**](../Model/EcedoERPCRMInterfaceApiEnergieInkoopContract.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsGetEnergieleveringConnectionContractForContract**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiEnergieleveringConnectionContract sysContractsGetEnergieleveringConnectionContractForContract($organization_id, $contract_id)

Ophalen van energieleveringconnectioncontract op basis van contractId

Met deze api call kan een energieleveringconnectioncontract worden opgehaald op basis van het contractid

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$contract_id = "contract_id_example"; // string | 

try {
    $result = $apiInstance->sysContractsGetEnergieleveringConnectionContractForContract($organization_id, $contract_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsGetEnergieleveringConnectionContractForContract: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **contract_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiEnergieleveringConnectionContract**](../Model/EcedoERPCRMInterfaceApiEnergieleveringConnectionContract.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsGetEnergieleveringConnectionContracts**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiEnergieleveringConnectionContract[] sysContractsGetEnergieleveringConnectionContracts($connection_id, $organization_id)

Energieleveringaansluitingcontracten ophalen van een aansluiting

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$connection_id = "connection_id_example"; // string | 
$organization_id = "organization_id_example"; // string | 

try {
    $result = $apiInstance->sysContractsGetEnergieleveringConnectionContracts($connection_id, $organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsGetEnergieleveringConnectionContracts: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **string**|  |
 **organization_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiEnergieleveringConnectionContract[]**](../Model/EcedoERPCRMInterfaceApiEnergieleveringConnectionContract.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsGetMeeliftConnectionContractForContract**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiMeeliftConnectionContract sysContractsGetMeeliftConnectionContractForContract($organization_id, $contract_id)

Ophalen van meeliftconnectioncontract op basis van contractId

Met deze api call kan een meeliftconnectioncontract worden opgehaald op basis van het contractId.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$contract_id = "contract_id_example"; // string | 

try {
    $result = $apiInstance->sysContractsGetMeeliftConnectionContractForContract($organization_id, $contract_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsGetMeeliftConnectionContractForContract: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **contract_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeeliftConnectionContract**](../Model/EcedoERPCRMInterfaceApiMeeliftConnectionContract.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsGetMeeliftConnectionContracts**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiMeeliftConnectionContract[] sysContractsGetMeeliftConnectionContracts($connection_id, $organization_id)

Meeliftaansluitingcontracten ophalen van een aansluiting

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$connection_id = "connection_id_example"; // string | 
$organization_id = "organization_id_example"; // string | 

try {
    $result = $apiInstance->sysContractsGetMeeliftConnectionContracts($connection_id, $organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsGetMeeliftConnectionContracts: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **string**|  |
 **organization_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeeliftConnectionContract[]**](../Model/EcedoERPCRMInterfaceApiMeeliftConnectionContract.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsGetMeeliftContracts**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiMeeliftContract[] sysContractsGetMeeliftContracts($connection_id, $organization_id)

Meeliftcontracten ophalen van een aansluiting

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$connection_id = "connection_id_example"; // string | 
$organization_id = "organization_id_example"; // string | 

try {
    $result = $apiInstance->sysContractsGetMeeliftContracts($connection_id, $organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsGetMeeliftContracts: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **string**|  |
 **organization_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiMeeliftContract[]**](../Model/EcedoERPCRMInterfaceApiMeeliftContract.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsGetOnbalansFlexContract**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiOnbalansFlexContract sysContractsGetOnbalansFlexContract($organization_id, $contract_id)

Ophalen van een onbalansflex contract

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant
$contract_id = "contract_id_example"; // string | Guid van het contract

try {
    $result = $apiInstance->sysContractsGetOnbalansFlexContract($organization_id, $contract_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsGetOnbalansFlexContract: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant |
 **contract_id** | **string**| Guid van het contract |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiOnbalansFlexContract**](../Model/EcedoERPCRMInterfaceApiOnbalansFlexContract.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsInvoiceContracts**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiBaseContract[] sysContractsInvoiceContracts($invoice_id, $organization_id)

Verkrijg de energielevering contracten die in een factuur zijn gefactureerd.  Een niet energielevering factuur zal een lege lijst retourneren.  Eventuele Meeliftcontracten worden niet geretourneerd

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$invoice_id = "invoice_id_example"; // string | 
$organization_id = "organization_id_example"; // string | 

try {
    $result = $apiInstance->sysContractsInvoiceContracts($invoice_id, $organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsInvoiceContracts: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **string**|  |
 **organization_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiBaseContract[]**](../Model/EcedoERPCRMInterfaceApiBaseContract.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsPostContractProperties**
> object sysContractsPostContractProperties($organization_id, $contract_id, $contract_property)

Pas een contract property aan

De volgende properties kunnen gewijzigd worden via de API en de volgende values hebben:  Channel: string  SalesReference: string  HasTerminationFee: boolean (true, false)  SettlementInvoiceFrequency: Monthly, Yearly  HasAdvancePaymentCalculation: boolean (true, false)  Reseller: Guid  CreditLimit: decimal  Campaign: string  HasAdvancePaymentInvoiceDocumentPrintFee: boolean (true, false)  HasCollectionFees: boolean (true, false)  CreditInsuranceIdentifier: string  ElectricityPowerType: Groen, LokaalGroen, Grijs  MaxODNLimitTariff: int  ElectricityGreeningOption: Guid  GasGreeningOption: Guid  HasRollingDeposit: boolean (true, false)  HasTariffChangeMeterReadings: boolean (true, false)  NoticePeriod: int  AdvancePaymentScheme: Fixed, SettleUsageFirstMonthProfiled

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$contract_id = "contract_id_example"; // string | 
$contract_property = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiContractPropertyPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiContractPropertyPostData | 

try {
    $result = $apiInstance->sysContractsPostContractProperties($organization_id, $contract_id, $contract_property);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsPostContractProperties: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **contract_id** | **string**|  |
 **contract_property** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiContractPropertyPostData**](../Model/EcedoERPCRMInterfaceApiContractPropertyPostData.md)|  |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsPostContracts**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiContractPostResult sysContractsPostContracts($organization_id, $connection_id, $contract)

Energieleveringcontract aanmaken

Bij 'Automatische verlenging' is de startdatum verplicht als het voorgaande contract geen einddatum heeft; als het voorgaande contract wel een einddatum heeft dan mag de startdatum niet worden ingestuurd

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$connection_id = "connection_id_example"; // string | 
$contract = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiEnergieleveringContractPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiEnergieleveringContractPostData | 

try {
    $result = $apiInstance->sysContractsPostContracts($organization_id, $connection_id, $contract);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsPostContracts: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **connection_id** | **string**|  |
 **contract** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiEnergieleveringContractPostData**](../Model/EcedoERPCRMInterfaceApiEnergieleveringContractPostData.md)|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiContractPostResult**](../Model/EcedoERPCRMInterfaceApiContractPostResult.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsPostSwitchProducer**
> object sysContractsPostSwitchProducer($organization_id, $connection_id, $producer_switch_data)

Veranderen van producent op een aansluiting

<p>Indien een contract nog niet is ingegaan wordt het meeliftcontract gewijzigd.              Indien een contract al wel is ingegaan wordt het contract gesplitst en krijgt het nieuwe contact een ander meeliftcontract</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Organisatie
$connection_id = "connection_id_example"; // string | Aansluiting
$producer_switch_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiProducerSwitchPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiProducerSwitchPostData | Andere producent

try {
    $result = $apiInstance->sysContractsPostSwitchProducer($organization_id, $connection_id, $producer_switch_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsPostSwitchProducer: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Organisatie |
 **connection_id** | **string**| Aansluiting |
 **producer_switch_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiProducerSwitchPostData**](../Model/EcedoERPCRMInterfaceApiProducerSwitchPostData.md)| Andere producent |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysContractsPutContracts**
> object sysContractsPutContracts($contract_id, $contract, $organization_id, $connection_id)

Energieleveringcontract wijzigen

EndReasons: ['Cancelled', 'InvalidTermination', 'ValidTermination', 'CustomerRenewal', 'ContractTypeChange', 'AutomaticRenewal', 'ProducerSwitch']    CancellationReasons: ['WithinCoolingDownPeriod', 'NonPayment', 'Misrepresentation', 'InvalidSwitchIn', 'ContractTakeover', 'Move', 'Cancellation', 'Dissatisfied']

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysContractsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$contract_id = "contract_id_example"; // string | 
$contract = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiEnergieleveringContractPutData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiEnergieleveringContractPutData | 
$organization_id = "organization_id_example"; // string | 
$connection_id = "connection_id_example"; // string | 

try {
    $result = $apiInstance->sysContractsPutContracts($contract_id, $contract, $organization_id, $connection_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysContractsApi->sysContractsPutContracts: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **string**|  |
 **contract** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiEnergieleveringContractPutData**](../Model/EcedoERPCRMInterfaceApiEnergieleveringContractPutData.md)|  |
 **organization_id** | **string**|  |
 **connection_id** | **string**|  |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

