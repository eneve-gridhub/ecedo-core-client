# Swagger\Client\SysEmailsApi

All URIs are relative to *https://test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysEmailsGet**](SysEmailsApi.md#sysEmailsGet) | **GET** /sysapi/v1.0/organizations/{organizationId}/emails | Retourneert een lijst van e-mails die bij een organisatie horen aan de hand van de meegegeven parameters
[**sysEmailsSendEmail**](SysEmailsApi.md#sysEmailsSendEmail) | **POST** /sysapi/v1.0/organizations/{organizationId}/emails/{emailId}/send | Een e-mail versturen


# **sysEmailsGet**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiEmailResponse[] sysEmailsGet($organization_id, $only_sent, $sent_after)

Retourneert een lijst van e-mails die bij een organisatie horen aan de hand van de meegegeven parameters

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysEmailsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | De guid van de organisatie van wie de e-mails geretourneerd moeten worden
$only_sent = true; // bool | Haal alleen de e-mails op die als status verstuurd hebben
$sent_after = new \DateTime("2013-10-20"); // \DateTime | Haal alleen de e-mails op die na deze datum verstuurd zijn of de e-mails die nog niet verstuurd zijn

try {
    $result = $apiInstance->sysEmailsGet($organization_id, $only_sent, $sent_after);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysEmailsApi->sysEmailsGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| De guid van de organisatie van wie de e-mails geretourneerd moeten worden |
 **only_sent** | **bool**| Haal alleen de e-mails op die als status verstuurd hebben | [optional]
 **sent_after** | **\DateTime**| Haal alleen de e-mails op die na deze datum verstuurd zijn of de e-mails die nog niet verstuurd zijn | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiEmailResponse[]**](../Model/EcedoERPCRMInterfaceApiEmailResponse.md)

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysEmailsSendEmail**
> object sysEmailsSendEmail($organization_id, $email_id)

Een e-mail versturen

Via deze call kan een e-mail voor de eerste keer verstuurd worden, maar is het ook mogelijk om een eerder verzonden e-mail opnieuw te versturen

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\SysEmailsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Id van de organisatie
$email_id = "email_id_example"; // string | Id van de e-mail die (opnieuw) verstuurd moet worden

try {
    $result = $apiInstance->sysEmailsSendEmail($organization_id, $email_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysEmailsApi->sysEmailsSendEmail: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Id van de organisatie |
 **email_id** | **string**| Id van de e-mail die (opnieuw) verstuurd moet worden |

### Return type

**object**

### Authorization

[basic](../../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

