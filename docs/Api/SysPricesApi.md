# Swagger\Client\SysPricesApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysPricesGetByConnection**](SysPricesApi.md#sysPricesGetByConnection) | **GET** /sysapi/v1.0/prices/energielevering/connections/{connectionId} | Ophalen van de gecombineernde prijzen geldig op de meegegeven dag voor de aansluiting.
[**sysPricesGetByContract**](SysPricesApi.md#sysPricesGetByContract) | **GET** /sysapi/v1.0/prices/energielevering/contracts/{contractId} | Ophalen van de gecombineernde prijzen geldig op de meegegeven dag voor de aansluiting horend bij het contract.
[**sysPricesGetByPropositionId**](SysPricesApi.md#sysPricesGetByPropositionId) | **GET** /sysapi/v1.0/prices/energielevering/propositions/{propositionId} | Ophalen van de gecombineernde prijzen geldig op de meegegeven dag voor de propositie.
[**sysPricesGetByPropositionReference**](SysPricesApi.md#sysPricesGetByPropositionReference) | **GET** /sysapi/v1.0/prices/energielevering/propositions/byReference/{propositionReference} | Ophalen van de gecombineernde prijzen geldig op de meegegeven dag voor de propositie op basis van de propositiereferentie.


# **sysPricesGetByConnection**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiCombinedPricesResult sysPricesGetByConnection($connection_id, $price_date, $allow_missing_cap_tar, $combine_type)

Ophalen van de gecombineernde prijzen geldig op de meegegeven dag voor de aansluiting.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysPricesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$connection_id = "connection_id_example"; // string | Het Id van de aansluiting waarvoor de prijzen opgehaald moeten worden.
$price_date = new \DateTime("2013-10-20"); // \DateTime | yyyy-MM-dd; De dag waarvoor de prijzen opgehaald moeten worden. Deze datum moet binnen de een contractperiode van de aansluiting liggen.
$allow_missing_cap_tar = true; // bool | Default ‘false’; Als true dan mag de captar code ontbreken en/of de netwerkkosten. De rest van de prijzen worden dan wel opgeleverd. Als false dan zal de call uitvallen als er geen captar code is en/of de netwerkkosten ontbreken.
$combine_type = "combine_type_example"; // string | Default ‘CombineGroup’; Geeft aan op welke manier de prijzen gegroepeerd moeten worden.

try {
    $result = $apiInstance->sysPricesGetByConnection($connection_id, $price_date, $allow_missing_cap_tar, $combine_type);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPricesApi->sysPricesGetByConnection: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **string**| Het Id van de aansluiting waarvoor de prijzen opgehaald moeten worden. |
 **price_date** | **\DateTime**| yyyy-MM-dd; De dag waarvoor de prijzen opgehaald moeten worden. Deze datum moet binnen de een contractperiode van de aansluiting liggen. |
 **allow_missing_cap_tar** | **bool**| Default ‘false’; Als true dan mag de captar code ontbreken en/of de netwerkkosten. De rest van de prijzen worden dan wel opgeleverd. Als false dan zal de call uitvallen als er geen captar code is en/of de netwerkkosten ontbreken. | [optional]
 **combine_type** | **string**| Default ‘CombineGroup’; Geeft aan op welke manier de prijzen gegroepeerd moeten worden. | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiCombinedPricesResult**](../Model/EcedoERPCRMInterfaceApiCombinedPricesResult.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysPricesGetByContract**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiCombinedPricesResult sysPricesGetByContract($contract_id, $price_date, $allow_missing_cap_tar, $combine_type)

Ophalen van de gecombineernde prijzen geldig op de meegegeven dag voor de aansluiting horend bij het contract.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysPricesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$contract_id = "contract_id_example"; // string | Het Id van het contract waarvoor de prijzen opgehaald moeten worden.
$price_date = new \DateTime("2013-10-20"); // \DateTime | yyyy-MM-dd; De dag waarvoor de prijzen opgehaald moeten worden. Deze datum moet binnen de contractperiode liggen.
$allow_missing_cap_tar = true; // bool | Default ‘false’; Als true dan mag de captar code ontbreken en/of de netwerkkosten. De rest van de prijzen worden dan wel opgeleverd. Als false dan zal de call uitvallen als er geen captar code is en/of de netwerkkosten ontbreken.
$combine_type = "combine_type_example"; // string | Default ‘CombineGroup’; Geeft aan op welke manier de prijzen gegroepeerd moeten worden.

try {
    $result = $apiInstance->sysPricesGetByContract($contract_id, $price_date, $allow_missing_cap_tar, $combine_type);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPricesApi->sysPricesGetByContract: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **string**| Het Id van het contract waarvoor de prijzen opgehaald moeten worden. |
 **price_date** | **\DateTime**| yyyy-MM-dd; De dag waarvoor de prijzen opgehaald moeten worden. Deze datum moet binnen de contractperiode liggen. |
 **allow_missing_cap_tar** | **bool**| Default ‘false’; Als true dan mag de captar code ontbreken en/of de netwerkkosten. De rest van de prijzen worden dan wel opgeleverd. Als false dan zal de call uitvallen als er geen captar code is en/of de netwerkkosten ontbreken. | [optional]
 **combine_type** | **string**| Default ‘CombineGroup’; Geeft aan op welke manier de prijzen gegroepeerd moeten worden. | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiCombinedPricesResult**](../Model/EcedoERPCRMInterfaceApiCombinedPricesResult.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysPricesGetByPropositionId**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiCombinedPricesResult sysPricesGetByPropositionId($proposition_id, $price_date, $grid_operator_ean, $location_type, $is_residential, $electricity_profile, $gas_profile, $electricity_cap_tar_code, $gas_cap_tar_code, $grid_area_ean, $gos_region, $meelift_proposition_id, $organization_type, $has_reseller, $allow_missing_cap_tar, $combine_type)

Ophalen van de gecombineernde prijzen geldig op de meegegeven dag voor de propositie.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysPricesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$proposition_id = "proposition_id_example"; // string | Het id van de propositie waarvoor de prijzen opgehaald moeten worden.
$price_date = new \DateTime("2013-10-20"); // \DateTime | yyyy-MM-dd; De dag waarvoor de prijzen opgehaald moeten worden.
$grid_operator_ean = "grid_operator_ean_example"; // string | Optioneel; De EAN van de netbeheerder. Gebruikt om de netwerkkosten te bepalen. N.v.t. bij grootverbruik en niet verplicht bij kleinverbruik als 'allowMissingCapTar == true'. In dat geval worden de netwerkkosten niet toegevoegd aan het resultaat.
$location_type = "location_type_example"; // string | Optioneel; De locatietype. Deze wordt gebruikt om te bepalen welke EB en ODE tarieven opgehaald moeten worden. Voor reguliere aansluitingen is deze parameter leeg.
$is_residential = true; // bool | Verplicht bij elektriciteit, n.v.t. bij gas; Verblijfsfunctie ja/nee.
$electricity_profile = "electricity_profile_example"; // string | [Deprecated] Optioneel bij elektriciteit, n.v.t. bij gas; Het elektriciteitsprofiel. Alleen verplicht bij leveranciers die prijzen hebben per profiel.
$gas_profile = "gas_profile_example"; // string | Optioneel bij gas, n.v.t. bij elektriciteit; Het gasprofiel. Alleen verplicht bij leveranciers die prijzen hebben per profiel of bij leveranciers die gas transportkosten hebben.
$electricity_cap_tar_code = "electricity_cap_tar_code_example"; // string | Optioneel bij elektriciteit, n.v.t. bij gas; De CapTarCode. Gebruikt om de netwerkkosten te bepalen. N.v.t. bij grootverbruik en niet verplicht bij kleinverbruik als 'allowMissingCapTar == true'. In dat geval worden de netwerkkosten niet toegevoegd aan het resultaat.
$gas_cap_tar_code = "gas_cap_tar_code_example"; // string | Optioneel bij gas, n.v.t. bij elektriciteit; De CapTarCode. Gebruikt om de netwerkkosten te bepalen. N.v.t. bij grootverbruik en niet verplicht bij kleinverbruik als 'allowMissingCapTar == true'. In dat geval worden de netwerkkosten niet toegevoegd aan het resultaat.
$grid_area_ean = "grid_area_ean_example"; // string | [Deprecated] Optioneel bij gas, n.v.t. bij elektriciteit; Netgebied/GOS EAN. Alleen verplicht bij leveranciers die regiotoeslag hebben per GOS EAN.
$gos_region = "gos_region_example"; // string | [Deprecated] Optioneel bij gas, n.v.t. bij elektriciteit; GOS regio. Alleen verplicht bij leveranciers die regiotoeslag hebben per GOS regio.
$meelift_proposition_id = "meelift_proposition_id_example"; // string | Verplicht als er meelift is, n.v.t. als er geen meelift is; Het id van de meeliftpropositie waarvoor de prijzen opgehaald moeten worden.
$organization_type = "organization_type_example"; // string | Optioneel. Het klanttype. Wordt gebruikt om te bepalen of we wel of geen BTW op teruglevering in rekening moeten brengen. Als het niet wordt meegegeven wordt Zakelijk ingevuld
$has_reseller = true; // bool | Optioneel; Hiermee kan worden aangegeven dat de prijzen incl. de reseller tarieven moeten worden teruggegeven. Ook als er geen Reseller property is vastgelegd bij de propositie.
$allow_missing_cap_tar = true; // bool | Default ‘false’; Als true dan mag de captar code ontbreken en/of de netwerkkosten. De rest van de prijzen worden dan wel opgeleverd. Als false dan zal de call uitvallen als er geen captar code is en/of de netwerkkosten ontbreken.
$combine_type = "combine_type_example"; // string | Default ‘CombineGroup’; Geeft aan op welke manier de prijzen gegroepeerd moeten worden.

try {
    $result = $apiInstance->sysPricesGetByPropositionId($proposition_id, $price_date, $grid_operator_ean, $location_type, $is_residential, $electricity_profile, $gas_profile, $electricity_cap_tar_code, $gas_cap_tar_code, $grid_area_ean, $gos_region, $meelift_proposition_id, $organization_type, $has_reseller, $allow_missing_cap_tar, $combine_type);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPricesApi->sysPricesGetByPropositionId: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposition_id** | **string**| Het id van de propositie waarvoor de prijzen opgehaald moeten worden. |
 **price_date** | **\DateTime**| yyyy-MM-dd; De dag waarvoor de prijzen opgehaald moeten worden. |
 **grid_operator_ean** | **string**| Optioneel; De EAN van de netbeheerder. Gebruikt om de netwerkkosten te bepalen. N.v.t. bij grootverbruik en niet verplicht bij kleinverbruik als &#39;allowMissingCapTar &#x3D;&#x3D; true&#39;. In dat geval worden de netwerkkosten niet toegevoegd aan het resultaat. | [optional]
 **location_type** | **string**| Optioneel; De locatietype. Deze wordt gebruikt om te bepalen welke EB en ODE tarieven opgehaald moeten worden. Voor reguliere aansluitingen is deze parameter leeg. | [optional]
 **is_residential** | **bool**| Verplicht bij elektriciteit, n.v.t. bij gas; Verblijfsfunctie ja/nee. | [optional]
 **electricity_profile** | **string**| [Deprecated] Optioneel bij elektriciteit, n.v.t. bij gas; Het elektriciteitsprofiel. Alleen verplicht bij leveranciers die prijzen hebben per profiel. | [optional]
 **gas_profile** | **string**| Optioneel bij gas, n.v.t. bij elektriciteit; Het gasprofiel. Alleen verplicht bij leveranciers die prijzen hebben per profiel of bij leveranciers die gas transportkosten hebben. | [optional]
 **electricity_cap_tar_code** | **string**| Optioneel bij elektriciteit, n.v.t. bij gas; De CapTarCode. Gebruikt om de netwerkkosten te bepalen. N.v.t. bij grootverbruik en niet verplicht bij kleinverbruik als &#39;allowMissingCapTar &#x3D;&#x3D; true&#39;. In dat geval worden de netwerkkosten niet toegevoegd aan het resultaat. | [optional]
 **gas_cap_tar_code** | **string**| Optioneel bij gas, n.v.t. bij elektriciteit; De CapTarCode. Gebruikt om de netwerkkosten te bepalen. N.v.t. bij grootverbruik en niet verplicht bij kleinverbruik als &#39;allowMissingCapTar &#x3D;&#x3D; true&#39;. In dat geval worden de netwerkkosten niet toegevoegd aan het resultaat. | [optional]
 **grid_area_ean** | **string**| [Deprecated] Optioneel bij gas, n.v.t. bij elektriciteit; Netgebied/GOS EAN. Alleen verplicht bij leveranciers die regiotoeslag hebben per GOS EAN. | [optional]
 **gos_region** | **string**| [Deprecated] Optioneel bij gas, n.v.t. bij elektriciteit; GOS regio. Alleen verplicht bij leveranciers die regiotoeslag hebben per GOS regio. | [optional]
 **meelift_proposition_id** | [**string**](../Model/.md)| Verplicht als er meelift is, n.v.t. als er geen meelift is; Het id van de meeliftpropositie waarvoor de prijzen opgehaald moeten worden. | [optional]
 **organization_type** | **string**| Optioneel. Het klanttype. Wordt gebruikt om te bepalen of we wel of geen BTW op teruglevering in rekening moeten brengen. Als het niet wordt meegegeven wordt Zakelijk ingevuld | [optional]
 **has_reseller** | **bool**| Optioneel; Hiermee kan worden aangegeven dat de prijzen incl. de reseller tarieven moeten worden teruggegeven. Ook als er geen Reseller property is vastgelegd bij de propositie. | [optional]
 **allow_missing_cap_tar** | **bool**| Default ‘false’; Als true dan mag de captar code ontbreken en/of de netwerkkosten. De rest van de prijzen worden dan wel opgeleverd. Als false dan zal de call uitvallen als er geen captar code is en/of de netwerkkosten ontbreken. | [optional]
 **combine_type** | **string**| Default ‘CombineGroup’; Geeft aan op welke manier de prijzen gegroepeerd moeten worden. | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiCombinedPricesResult**](../Model/EcedoERPCRMInterfaceApiCombinedPricesResult.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysPricesGetByPropositionReference**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiCombinedPricesResult sysPricesGetByPropositionReference($proposition_reference, $price_date, $grid_operator_ean, $location_type, $is_residential, $electricity_profile, $gas_profile, $electricity_cap_tar_code, $gas_cap_tar_code, $grid_area_ean, $gos_region, $meelift_proposition_reference, $organization_type, $has_reseller, $allow_missing_cap_tar, $combine_type)

Ophalen van de gecombineernde prijzen geldig op de meegegeven dag voor de propositie op basis van de propositiereferentie.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysPricesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$proposition_reference = "proposition_reference_example"; // string | De referentie van de propositie waarvoor de prijzen opgehaald moeten worden.
$price_date = new \DateTime("2013-10-20"); // \DateTime | yyyy-MM-dd; De dag waarvoor de prijzen opgehaald moeten worden.
$grid_operator_ean = "grid_operator_ean_example"; // string | Optioneel; De EAN van de netbeheerder. Gebruikt om de netwerkkosten te bepalen. N.v.t. bij grootverbruik en niet verplicht bij kleinverbruik als 'allowMissingCapTar == true'. In dat geval worden de netwerkkosten niet toegevoegd aan het resultaat.
$location_type = "location_type_example"; // string | Optioneel; De locatietype. Deze wordt gebruikt om te bepalen welke EB en ODE tarieven opgehaald moeten worden. Voor reguliere aansluitingen is deze parameter leeg.
$is_residential = true; // bool | Verplicht bij elektriciteit, n.v.t. bij gas; Verblijfsfunctie ja/nee.
$electricity_profile = "electricity_profile_example"; // string | [Deprecated] Optioneel bij elektriciteit, n.v.t. bij gas; Het elektriciteitsprofiel. Alleen verplicht bij leveranciers die prijzen hebben per profiel.
$gas_profile = "gas_profile_example"; // string | Optioneel bij gas, n.v.t. bij elektriciteit; Het gasprofiel. Alleen verplicht bij leveranciers die prijzen hebben per profiel of bij leveranciers die gas transportkosten hebben.
$electricity_cap_tar_code = "electricity_cap_tar_code_example"; // string | Optioneel bij elektriciteit, n.v.t. bij gas; De CapTarCode. Gebruikt om de netwerkkosten te bepalen. N.v.t. bij grootverbruik en niet verplicht bij kleinverbruik als 'allowMissingCapTar == true'. In dat geval worden de netwerkkosten niet toegevoegd aan het resultaat.
$gas_cap_tar_code = "gas_cap_tar_code_example"; // string | Optioneel bij gas, n.v.t. bij elektriciteit; De CapTarCode. Gebruikt om de netwerkkosten te bepalen. N.v.t. bij grootverbruik en niet verplicht bij kleinverbruik als 'allowMissingCapTar == true'. In dat geval worden de netwerkkosten niet toegevoegd aan het resultaat.
$grid_area_ean = "grid_area_ean_example"; // string | [Deprecated] Optioneel bij gas, n.v.t. bij elektriciteit; Netgebied/GOS EAN. Alleen verplicht bij leveranciers die regiotoeslag hebben per GOS EAN.
$gos_region = "gos_region_example"; // string | [Deprecated] Optioneel bij gas, n.v.t. bij elektriciteit; GOS regio. Alleen verplicht bij leveranciers die regiotoeslag hebben per GOS regio.
$meelift_proposition_reference = "meelift_proposition_reference_example"; // string | Verplicht als er meelift is, n.v.t. als er geen meelift is; De referentie van de meeliftpropositie waarvoor de prijzen opgehaald moeten worden.
$organization_type = "organization_type_example"; // string | Optioneel. Het klanttype. Wordt gebruikt om te bepalen of we wel of geen BTW op teruglevering in rekening moeten brengen. Als het niet wordt meegegeven wordt Zakelijk ingevuld
$has_reseller = true; // bool | Optioneel; Hiermee kan worden aangegeven dat de prijzen incl. de reseller tarieven moeten worden teruggegeven. Ook als er geen Reseller property is vastgelegd bij de propositie.
$allow_missing_cap_tar = true; // bool | Default ‘false’; Als true dan mag de captar code ontbreken en/of de netwerkkosten. De rest van de prijzen worden dan wel opgeleverd. Als false dan zal de call uitvallen als er geen captar code is en/of de netwerkkosten ontbreken.
$combine_type = "combine_type_example"; // string | Default ‘CombineGroup’; Geeft aan op welke manier de prijzen gegroepeerd moeten worden.

try {
    $result = $apiInstance->sysPricesGetByPropositionReference($proposition_reference, $price_date, $grid_operator_ean, $location_type, $is_residential, $electricity_profile, $gas_profile, $electricity_cap_tar_code, $gas_cap_tar_code, $grid_area_ean, $gos_region, $meelift_proposition_reference, $organization_type, $has_reseller, $allow_missing_cap_tar, $combine_type);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysPricesApi->sysPricesGetByPropositionReference: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposition_reference** | **string**| De referentie van de propositie waarvoor de prijzen opgehaald moeten worden. |
 **price_date** | **\DateTime**| yyyy-MM-dd; De dag waarvoor de prijzen opgehaald moeten worden. |
 **grid_operator_ean** | **string**| Optioneel; De EAN van de netbeheerder. Gebruikt om de netwerkkosten te bepalen. N.v.t. bij grootverbruik en niet verplicht bij kleinverbruik als &#39;allowMissingCapTar &#x3D;&#x3D; true&#39;. In dat geval worden de netwerkkosten niet toegevoegd aan het resultaat. | [optional]
 **location_type** | **string**| Optioneel; De locatietype. Deze wordt gebruikt om te bepalen welke EB en ODE tarieven opgehaald moeten worden. Voor reguliere aansluitingen is deze parameter leeg. | [optional]
 **is_residential** | **bool**| Verplicht bij elektriciteit, n.v.t. bij gas; Verblijfsfunctie ja/nee. | [optional]
 **electricity_profile** | **string**| [Deprecated] Optioneel bij elektriciteit, n.v.t. bij gas; Het elektriciteitsprofiel. Alleen verplicht bij leveranciers die prijzen hebben per profiel. | [optional]
 **gas_profile** | **string**| Optioneel bij gas, n.v.t. bij elektriciteit; Het gasprofiel. Alleen verplicht bij leveranciers die prijzen hebben per profiel of bij leveranciers die gas transportkosten hebben. | [optional]
 **electricity_cap_tar_code** | **string**| Optioneel bij elektriciteit, n.v.t. bij gas; De CapTarCode. Gebruikt om de netwerkkosten te bepalen. N.v.t. bij grootverbruik en niet verplicht bij kleinverbruik als &#39;allowMissingCapTar &#x3D;&#x3D; true&#39;. In dat geval worden de netwerkkosten niet toegevoegd aan het resultaat. | [optional]
 **gas_cap_tar_code** | **string**| Optioneel bij gas, n.v.t. bij elektriciteit; De CapTarCode. Gebruikt om de netwerkkosten te bepalen. N.v.t. bij grootverbruik en niet verplicht bij kleinverbruik als &#39;allowMissingCapTar &#x3D;&#x3D; true&#39;. In dat geval worden de netwerkkosten niet toegevoegd aan het resultaat. | [optional]
 **grid_area_ean** | **string**| [Deprecated] Optioneel bij gas, n.v.t. bij elektriciteit; Netgebied/GOS EAN. Alleen verplicht bij leveranciers die regiotoeslag hebben per GOS EAN. | [optional]
 **gos_region** | **string**| [Deprecated] Optioneel bij gas, n.v.t. bij elektriciteit; GOS regio. Alleen verplicht bij leveranciers die regiotoeslag hebben per GOS regio. | [optional]
 **meelift_proposition_reference** | **string**| Verplicht als er meelift is, n.v.t. als er geen meelift is; De referentie van de meeliftpropositie waarvoor de prijzen opgehaald moeten worden. | [optional]
 **organization_type** | **string**| Optioneel. Het klanttype. Wordt gebruikt om te bepalen of we wel of geen BTW op teruglevering in rekening moeten brengen. Als het niet wordt meegegeven wordt Zakelijk ingevuld | [optional]
 **has_reseller** | **bool**| Optioneel; Hiermee kan worden aangegeven dat de prijzen incl. de reseller tarieven moeten worden teruggegeven. Ook als er geen Reseller property is vastgelegd bij de propositie. | [optional]
 **allow_missing_cap_tar** | **bool**| Default ‘false’; Als true dan mag de captar code ontbreken en/of de netwerkkosten. De rest van de prijzen worden dan wel opgeleverd. Als false dan zal de call uitvallen als er geen captar code is en/of de netwerkkosten ontbreken. | [optional]
 **combine_type** | **string**| Default ‘CombineGroup’; Geeft aan op welke manier de prijzen gegroepeerd moeten worden. | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiCombinedPricesResult**](../Model/EcedoERPCRMInterfaceApiCombinedPricesResult.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

