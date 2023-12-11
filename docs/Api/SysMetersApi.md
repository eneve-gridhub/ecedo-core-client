# Swagger\Client\SysMetersApi

All URIs are relative to *https://innova-test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysMetersGet**](SysMetersApi.md#sysMetersGet) | **GET** /sysapi/v1.0/organizations/{organizationId}/connections/{connectionId}/meters | Haal alle meters op van een aansluiting


# **sysMetersGet**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiExtendedMeter[] sysMetersGet($organization_id, $connection_id)

Haal alle meters op van een aansluiting

Opvragen alle meters voor een aansluiting<br /><br />  __Let op!__ De response-objecten van gasmeters en elektriciteitsmeters zijn niet gelijk aan elkaar. Zie de response-voorbeelden voor de inhoudelijke verschillen.<br />  __Let op!__ Deze API is alleen van toepassing op kleinverbruikaansluitingen. Voor grootverbruikaansluitingen zal Ecedo geen nuttige resultaten teruggeven.  __Let op!__ Bij gasmeters is het veld TemperatureCorrection aanwezig. Deze wordt gevuld met de huidige waarde en kan afwijken van de daadwerkelijk gebruikte waarde in berekeningen

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

$apiInstance = new Swagger\Client\Api\SysMetersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$connection_id = "connection_id_example"; // string | Guid van de aansluiting (Connection)

try {
    $result = $apiInstance->sysMetersGet($organization_id, $connection_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysMetersApi->sysMetersGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **connection_id** | **string**| Guid van de aansluiting (Connection) |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiExtendedMeter[]**](../Model/EcedoERPCRMInterfaceApiExtendedMeter.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

