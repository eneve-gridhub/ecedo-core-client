# Swagger\Client\SysDashboardApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysDashboardGetDashboardOrganizationsByIdOrReference**](SysDashboardApi.md#sysDashboardGetDashboardOrganizationsByIdOrReference) | **GET** /sysapi/v1.0/dashboard/organizations/{organizationIdOrReference} | Ophalen van dashboardgegevens


# **sysDashboardGetDashboardOrganizationsByIdOrReference**
> \Swagger\Client\Model\EcedoERPUIWebControllersSysApiSysDashboardControllerDashboardDto sysDashboardGetDashboardOrganizationsByIdOrReference($organization_id_or_reference, $include_connections, $include_meter_readings, $include_advance_payments, $include_billing_items, $include_connection_contracts, $include_contract_prices, $only_usable_meter_readings)

Ophalen van dashboardgegevens

Deze API wordt niet langer actief ondersteund.<br />  Gebruik als alternatief specifieke APIs

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysDashboardApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id_or_reference = "organization_id_or_reference_example"; // string | 
$include_connections = true; // bool | 
$include_meter_readings = true; // bool | 
$include_advance_payments = true; // bool | 
$include_billing_items = true; // bool | 
$include_connection_contracts = true; // bool | 
$include_contract_prices = true; // bool | 
$only_usable_meter_readings = true; // bool | 

try {
    $result = $apiInstance->sysDashboardGetDashboardOrganizationsByIdOrReference($organization_id_or_reference, $include_connections, $include_meter_readings, $include_advance_payments, $include_billing_items, $include_connection_contracts, $include_contract_prices, $only_usable_meter_readings);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysDashboardApi->sysDashboardGetDashboardOrganizationsByIdOrReference: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id_or_reference** | **string**|  |
 **include_connections** | **bool**|  | [optional]
 **include_meter_readings** | **bool**|  | [optional]
 **include_advance_payments** | **bool**|  | [optional]
 **include_billing_items** | **bool**|  | [optional]
 **include_connection_contracts** | **bool**|  | [optional]
 **include_contract_prices** | **bool**|  | [optional]
 **only_usable_meter_readings** | **bool**|  | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPUIWebControllersSysApiSysDashboardControllerDashboardDto**](../Model/EcedoERPUIWebControllersSysApiSysDashboardControllerDashboardDto.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

