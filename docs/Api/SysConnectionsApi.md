# Swagger\Client\SysConnectionsApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysConnectionsCancel**](SysConnectionsApi.md#sysConnectionsCancel) | **PUT** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/status/cancel | De status van de aansluiting op &#39;Aanmelding afgebroken&#39; zetten
[**sysConnectionsChangeAllocationMethod**](SysConnectionsApi.md#sysConnectionsChangeAllocationMethod) | **POST** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/changeallocationmethod | Wijzig allocatiemethode
[**sysConnectionsConnectionProperties**](SysConnectionsApi.md#sysConnectionsConnectionProperties) | **POST** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/connectionproperties | Wijzig aansluitinggegevens
[**sysConnectionsGetByConnectionId**](SysConnectionsApi.md#sysConnectionsGetByConnectionId) | **GET** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId} | Haal specifieke aansluiting op
[**sysConnectionsGetByOrganizationId**](SysConnectionsApi.md#sysConnectionsGetByOrganizationId) | **GET** /sysapi/v1.0/organizations/{organizationId}/connections | Haal aansluitingen van een specifieke klant op
[**sysConnectionsHasContractInPeriod**](SysConnectionsApi.md#sysConnectionsHasContractInPeriod) | **GET** /sysapi/v1.0/connections/{ean}/hascontractinperiod | Controleer of EAN in gevraagde periode reeds een contract heeft
[**sysConnectionsPost**](SysConnectionsApi.md#sysConnectionsPost) | **POST** /sysapi/v1.0/organizations/{organizationId}/connections | Nieuwe aansluiting(en) aanmaken
[**sysConnectionsPut**](SysConnectionsApi.md#sysConnectionsPut) | **PUT** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId} | Wijzig een specifiek aansluiting
[**sysConnectionsReset**](SysConnectionsApi.md#sysConnectionsReset) | **PUT** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/status/reset | De status van de aansluiting terugzetten naar de vorige status
[**sysConnectionsUpdateMeteringPoint**](SysConnectionsApi.md#sysConnectionsUpdateMeteringPoint) | **POST** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/meteringpoint | Aansluiting bijwerken met EDSN gegevens


# **sysConnectionsCancel**
> sysConnectionsCancel($organization_id, $connection_id)

De status van de aansluiting op 'Aanmelding afgebroken' zetten

Deze API mag alleen aangeroepen worden wanneer de huidige status van de aansluiting \"Aangemaakt\" (`Created`) of \"Te verhuizen\" (`Move`) is.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysConnectionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$connection_id = "connection_id_example"; // string | Guid van de aansluiting (Connection)

try {
    $apiInstance->sysConnectionsCancel($organization_id, $connection_id);
} catch (Exception $e) {
    echo 'Exception when calling SysConnectionsApi->sysConnectionsCancel: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **connection_id** | **string**| Guid van de aansluiting (Connection) |

### Return type

void (empty response body)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysConnectionsChangeAllocationMethod**
> sysConnectionsChangeAllocationMethod($organization_id, $connection_id, $change_allocation_method_post_data)

Wijzig allocatiemethode

Deze API wijzigt de allocatiemethode van een aansluiting, door de bijbehorende flow te starten. Deze flow verstuurt de wijziging naar EDSN en past het aansluitinggegeven aan.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysConnectionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$connection_id = "connection_id_example"; // string | Guid van de aansluiting (Connection)
$change_allocation_method_post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiChangeAllocationMethodPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiChangeAllocationMethodPostData | De data van de allocatiemethodewijziging, zie het object-model voor meer informatie

try {
    $apiInstance->sysConnectionsChangeAllocationMethod($organization_id, $connection_id, $change_allocation_method_post_data);
} catch (Exception $e) {
    echo 'Exception when calling SysConnectionsApi->sysConnectionsChangeAllocationMethod: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **connection_id** | **string**| Guid van de aansluiting (Connection) |
 **change_allocation_method_post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiChangeAllocationMethodPostData**](../Model/EcedoERPCRMInterfaceApiChangeAllocationMethodPostData.md)| De data van de allocatiemethodewijziging, zie het object-model voor meer informatie |

### Return type

void (empty response body)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysConnectionsConnectionProperties**
> sysConnectionsConnectionProperties($organization_id, $connection_id, $connection_property)

Wijzig aansluitinggegevens

De volgende aansluitinggegevens (`ConnectionProperties`) kunnen gewijzigd worden via de API en de volgende waarden hebben:  * LocationType: BlockHeating, ChargingStationRegular, ChargingStationFast, Horticulture;  * BillAsSingle: boolean (true, false);  * RequestP4IntervalReadings: boolean (true, false);  * RequestP4DayReadings: boolean (true, false);  * RequestP4ReadingsForBillingAllowed: boolean (true, false);  * AllocationMethod: enumeratie (SMA, PRF, TMT; er wordt geen flow gestart);  * MEP: GeenComplexGeenVerblijf, GeenComplexWelVerblijf, WelComplexGeenVerblijf, WelComplexWelVerblijf, Nvt  * PhysicalStatus: UnderConstruction, InOperation, Demolished, OutOfOperation  * HasZipAreaEnergyTaxCredit: boolean (true, false)  * TreatAsConsumer: boolean (true, false);

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysConnectionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$connection_id = "connection_id_example"; // string | Guid van de aansluiting (Connection)
$connection_property = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionPropertyPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionPropertyPostData | De data van de aansluitinggegevens, zie het object-model voor meer informatie

try {
    $apiInstance->sysConnectionsConnectionProperties($organization_id, $connection_id, $connection_property);
} catch (Exception $e) {
    echo 'Exception when calling SysConnectionsApi->sysConnectionsConnectionProperties: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **connection_id** | **string**| Guid van de aansluiting (Connection) |
 **connection_property** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionPropertyPostData**](../Model/EcedoERPCRMInterfaceApiConnectionPropertyPostData.md)| De data van de aansluitinggegevens, zie het object-model voor meer informatie |

### Return type

void (empty response body)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysConnectionsGetByConnectionId**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnection sysConnectionsGetByConnectionId($organization_id, $connection_id)

Haal specifieke aansluiting op

<p>Opvragen specifieke aansluiting van een klant.</p>  <p>Enkel het laatste actieve contract voor een aansluiting wordt geretourneerd. Afgeronde contracten worden niet geretourneerd</p>  <p> Het <code>Ecedo.ERP.CRM.Interface.Api.ConnectionProperty</code>-object bevat in het geval van een gas aansluiting bij de property met type <code>ConnectionPropertyType</code>=<b>'GridArea'</b> een extra veld (<code>GosRegion</code>) voor de non-localized-versie van de regio-waarde.</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysConnectionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$connection_id = "connection_id_example"; // string | Guid van de aansluiting (Connection)

try {
    $result = $apiInstance->sysConnectionsGetByConnectionId($organization_id, $connection_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysConnectionsApi->sysConnectionsGetByConnectionId: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **connection_id** | **string**| Guid van de aansluiting (Connection) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiConnection**](../Model/EcedoERPCRMInterfaceApiConnection.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysConnectionsGetByOrganizationId**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnection[] sysConnectionsGetByOrganizationId($organization_id, $cluster_reference)

Haal aansluitingen van een specifieke klant op

<p>Opvragen alle aansluitingen van een klant.</p>  <p> Het <code>Ecedo.ERP.CRM.Interface.Api.ConnectionProperty</code>-object bevat in het geval van een gas aansluiting bij de property met type <code>ConnectionPropertyType</code>=<b>'GridArea'</b> een extra veld (<code>GosRegion</code>) voor de non-localized-versie van de regio-waarde.</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysConnectionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$cluster_reference = "cluster_reference_example"; // string | Optionele parameter waarmee alleen aansluitingen met deze clusterreferentie opgevraagd kunnen worden

try {
    $result = $apiInstance->sysConnectionsGetByOrganizationId($organization_id, $cluster_reference);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysConnectionsApi->sysConnectionsGetByOrganizationId: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **cluster_reference** | **string**| Optionele parameter waarmee alleen aansluitingen met deze clusterreferentie opgevraagd kunnen worden | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiConnection[]**](../Model/EcedoERPCRMInterfaceApiConnection.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysConnectionsHasContractInPeriod**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiHasContractInPeriodResponse sysConnectionsHasContractInPeriod($ean, $start_date, $end_date)

Controleer of EAN in gevraagde periode reeds een contract heeft

Controleer of er een contract is voor aansluiting met EAN in de gevraagde periode.              Contracten met status 'Cancelled' (Geannuleerd) worden niet meegenomen.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysConnectionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ean = "ean_example"; // string | EAN van de aansluiting
$start_date = new \DateTime("2013-10-20"); // \DateTime | StartDatum van de te controleren periode
$end_date = new \DateTime("2013-10-20"); // \DateTime | EindDatum van de te controleren periode

try {
    $result = $apiInstance->sysConnectionsHasContractInPeriod($ean, $start_date, $end_date);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysConnectionsApi->sysConnectionsHasContractInPeriod: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **string**| EAN van de aansluiting |
 **start_date** | **\DateTime**| StartDatum van de te controleren periode |
 **end_date** | **\DateTime**| EindDatum van de te controleren periode |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiHasContractInPeriodResponse**](../Model/EcedoERPCRMInterfaceApiHasContractInPeriodResponse.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysConnectionsPost**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionContractGroupPostResult[] sysConnectionsPost($organization_id, $connection_group)

Nieuwe aansluiting(en) aanmaken

De contract-objecten zijn optioneel. Als contract is meegestuurd zal er ook een aanmeldingsflow worden gestart.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysConnectionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$connection_group = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionsConnectionGroupPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionsConnectionGroupPostData | De data van de aansluiting(en), zie het object-model voor meer informatie

try {
    $result = $apiInstance->sysConnectionsPost($organization_id, $connection_group);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysConnectionsApi->sysConnectionsPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **connection_group** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionsConnectionGroupPostData**](../Model/EcedoERPCRMInterfaceApiConnectionsConnectionGroupPostData.md)| De data van de aansluiting(en), zie het object-model voor meer informatie |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionContractGroupPostResult[]**](../Model/EcedoERPCRMInterfaceApiConnectionContractGroupPostResult.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysConnectionsPut**
> sysConnectionsPut($organization_id, $connection_id, $connection_data)

Wijzig een specifiek aansluiting

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysConnectionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$connection_id = "connection_id_example"; // string | Guid van de aansluiting (Connection)
$connection_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionPutData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionPutData | De data van de aansluiting(en), zie het object-model voor meer informatie

try {
    $apiInstance->sysConnectionsPut($organization_id, $connection_id, $connection_data);
} catch (Exception $e) {
    echo 'Exception when calling SysConnectionsApi->sysConnectionsPut: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **connection_id** | **string**| Guid van de aansluiting (Connection) |
 **connection_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiConnectionPutData**](../Model/EcedoERPCRMInterfaceApiConnectionPutData.md)| De data van de aansluiting(en), zie het object-model voor meer informatie |

### Return type

void (empty response body)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysConnectionsReset**
> sysConnectionsReset($organization_id, $connection_id)

De status van de aansluiting terugzetten naar de vorige status

Deze API kan de status van een aansluiting terugzetten naar \"Aangemaakt\" (`Created`) of \"Te verhuizen\" (`Move`)<br /><br />  Er zijn een aantal beperkingen / beveiligingen toegevoegd voor het gebruik van deze API om verkeerde statustransities te voorkomen<br />  - Deze API kan alleen gebruikt worden wanneer de huidige status \"Aanmelding afgebroken\" (`ApplicationCancelled`) is<br />  - Deze API kijkt in de status-historie om te bepalen of de status gereset moet worden naar \"Aangemaakt\" (`Created`) of \"Te verhuizen\" (`Move`)<br />  - Als de vorige status \"In flow\" (`InFlow`) was wordt deze status genegeerd en wordt gekeken naar de status voor de \"In flow\"-status<br />  - Als de vorige status niet \"Aangemaakt\" (`Created`) of \"Te verhuizen\" is wordt een foutmelding teruggegeven

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysConnectionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$connection_id = "connection_id_example"; // string | Guid van de aansluiting (Connection)

try {
    $apiInstance->sysConnectionsReset($organization_id, $connection_id);
} catch (Exception $e) {
    echo 'Exception when calling SysConnectionsApi->sysConnectionsReset: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **connection_id** | **string**| Guid van de aansluiting (Connection) |

### Return type

void (empty response body)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysConnectionsUpdateMeteringPoint**
> sysConnectionsUpdateMeteringPoint($organization_id, $connection_id, $post_data)

Aansluiting bijwerken met EDSN gegevens

Deze API vraagt de meest recente gegevens van de aansluiting (`MeteringPoint`) op bij EDSN en werkt waar nodig de aansluiting bij

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysConnectionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$connection_id = "connection_id_example"; // string | Guid van de aansluiting (Connection)
$post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiUpdateMeteringPointPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiUpdateMeteringPointPostData | De data van het EDSN verzoek, zie het object-model voor meer informatie

try {
    $apiInstance->sysConnectionsUpdateMeteringPoint($organization_id, $connection_id, $post_data);
} catch (Exception $e) {
    echo 'Exception when calling SysConnectionsApi->sysConnectionsUpdateMeteringPoint: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **connection_id** | **string**| Guid van de aansluiting (Connection) |
 **post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiUpdateMeteringPointPostData**](../Model/EcedoERPCRMInterfaceApiUpdateMeteringPointPostData.md)| De data van het EDSN verzoek, zie het object-model voor meer informatie |

### Return type

void (empty response body)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

