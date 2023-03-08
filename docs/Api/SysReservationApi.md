# Swagger\Client\SysReservationApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysReservationGetAnnualStandardUsageReservationResults**](SysReservationApi.md#sysReservationGetAnnualStandardUsageReservationResults) | **GET** /sysapi/v1.0/propositions/{propositionReference}/reservations | Ophalen van SJV voor alle aansluitingen behorend bij een propositie referentie


# **sysReservationGetAnnualStandardUsageReservationResults**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiReservationBase[] sysReservationGetAnnualStandardUsageReservationResults($proposition_reference, $only_active)

Ophalen van SJV voor alle aansluitingen behorend bij een propositie referentie

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysReservationApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$proposition_reference = "proposition_reference_example"; // string | propositiereferentie
$only_active = true; // bool | Geeft aan of ook niet actieve aansluitingen / contracten moeten worden geretourneerd; standaard worden ook inactieve aansluitingen / contracten geretourneerd

try {
    $result = $apiInstance->sysReservationGetAnnualStandardUsageReservationResults($proposition_reference, $only_active);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysReservationApi->sysReservationGetAnnualStandardUsageReservationResults: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposition_reference** | **string**| propositiereferentie |
 **only_active** | **bool**| Geeft aan of ook niet actieve aansluitingen / contracten moeten worden geretourneerd; standaard worden ook inactieve aansluitingen / contracten geretourneerd | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiReservationBase[]**](../Model/EcedoERPCRMInterfaceApiReservationBase.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

