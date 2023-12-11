# Swagger\Client\SysDocumentsApi

All URIs are relative to *https://innova-test.ecedo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sysDocumentsDownload**](SysDocumentsApi.md#sysDocumentsDownload) | **GET** /sysapi/v1.0/organizations/{organizationId}/documents/{documentId}/download | Download document
[**sysDocumentsGenerateDocument**](SysDocumentsApi.md#sysDocumentsGenerateDocument) | **POST** /sysapi/v1.0/organizations/{organizationId}/documents/generatedocument | Genereer document
[**sysDocumentsGetDocument**](SysDocumentsApi.md#sysDocumentsGetDocument) | **GET** /sysapi/v1.0/organizations/{organizationId}/documents/{documentId} | Retrieves a document based on the organization and documentid
[**sysDocumentsGetDocuments**](SysDocumentsApi.md#sysDocumentsGetDocuments) | **GET** /sysapi/v1.0/organizations/{organizationId}/documents | Get documents. Eventueel gefilterd op documenttype. Bij het documenttype &#39;UserDocument&#39; kan ook op userdocumenttype gefilterd worden.
[**sysDocumentsStoreNexusBallNotification**](SysDocumentsApi.md#sysDocumentsStoreNexusBallNotification) | **POST** /sysapi/v1.0/documents/nexus/allocation | Uploaden van BALLNotificationEnvelopes (Nexus)
[**sysDocumentsStorePVNEDTimeSeriesDocument**](SysDocumentsApi.md#sysDocumentsStorePVNEDTimeSeriesDocument) | **POST** /sysapi/v1.0/documents/pvned/timeseriesdocument | Upload and process PVNED&#39;s Time Series Document
[**sysDocumentsUploadUserDocument**](SysDocumentsApi.md#sysDocumentsUploadUserDocument) | **POST** /sysapi/v1.0/documents/UploadUserDocument/{organizationId}/{userDocumentType} | Upload document


# **sysDocumentsDownload**
> object sysDocumentsDownload($organization_id, $document_id)

Download document

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

$apiInstance = new Swagger\Client\Api\SysDocumentsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$document_id = "document_id_example"; // string | 

try {
    $result = $apiInstance->sysDocumentsDownload($organization_id, $document_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysDocumentsApi->sysDocumentsDownload: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **document_id** | **string**|  |

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysDocumentsGenerateDocument**
> string sysDocumentsGenerateDocument($organization_id, $generate_document_post_data)

Genereer document

Met behulp van deze API kunnen specifieke documenten gegenereerd worden<br />  De API retourneert het DocumentId van het nieuw aangemaakte document. Dit Id wordt niet in een object teruggegeven, maar als losse string.<br /><br />  Ondersteunde DocumentTypes: ExtensionLetterEnergy, WelcomeLetterEnergy<br /><br />  __ExtensionLetterEnergy__<br />  De verlengbrief (`ExtensionLetterEnergy`) wordt gegenereerd aan de hand van de nieuwste contracten bij de aansluitingen in het meegegeven cluster.<br />  Deze API kan dus worden aangeroepen voor aansluitingen waarvan de verlengde contract nog niet actief zijn.<br />  Als er meerdere toekomstige contracten zijn dan zullen de contracten gebruikt worden die het laatste ingaan.<br /><br />  __WelcomeLetterEnergy__<br />  De welkomstbrief (`WelcomeLetterEnergy`) wordt (indien zo geconfigureerd) automatisch aangemaakt door de aanmeldflow. Met behulp van deze API kan het document indien gewenst opnieuw gegenereerd worden.<br />  De welkomstbrief moet gegenereerd worden als een klant (op)nieuw in levering gaat. Er zouden op dat moment geen opeenvolgende contracten (verlengingen) bij de aansluitingen in aanwezig zijn.<br />

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

$apiInstance = new Swagger\Client\Api\SysDocumentsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | Guid van de klant (Organization)
$generate_document_post_data = new \Swagger\Client\Model\EcedoERPCRMInterfaceApiGenerateDocumentPostData(); // \Swagger\Client\Model\EcedoERPCRMInterfaceApiGenerateDocumentPostData | POST-data waarmee het gedrag van de API aangestuurd wordt. Zie het object-model voor meer informatie.

try {
    $result = $apiInstance->sysDocumentsGenerateDocument($organization_id, $generate_document_post_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysDocumentsApi->sysDocumentsGenerateDocument: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**| Guid van de klant (Organization) |
 **generate_document_post_data** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiGenerateDocumentPostData**](../Model/EcedoERPCRMInterfaceApiGenerateDocumentPostData.md)| POST-data waarmee het gedrag van de API aangestuurd wordt. Zie het object-model voor meer informatie. |

### Return type

**string**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysDocumentsGetDocument**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiDocument sysDocumentsGetDocument($organization_id, $document_id)

Retrieves a document based on the organization and documentid

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

$apiInstance = new Swagger\Client\Api\SysDocumentsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$document_id = "document_id_example"; // string | 

try {
    $result = $apiInstance->sysDocumentsGetDocument($organization_id, $document_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysDocumentsApi->sysDocumentsGetDocument: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **document_id** | **string**|  |

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiDocument**](../Model/EcedoERPCRMInterfaceApiDocument.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysDocumentsGetDocuments**
> \Swagger\Client\Model\EcedoERPCRMInterfaceApiDocument[] sysDocumentsGetDocuments($organization_id, $document_type, $user_document_type)

Get documents. Eventueel gefilterd op documenttype. Bij het documenttype 'UserDocument' kan ook op userdocumenttype gefilterd worden.

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

$apiInstance = new Swagger\Client\Api\SysDocumentsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$document_type = "document_type_example"; // string | 
$user_document_type = "user_document_type_example"; // string | 

try {
    $result = $apiInstance->sysDocumentsGetDocuments($organization_id, $document_type, $user_document_type);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysDocumentsApi->sysDocumentsGetDocuments: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **document_type** | **string**|  | [optional]
 **user_document_type** | **string**|  | [optional]

### Return type

[**\Swagger\Client\Model\EcedoERPCRMInterfaceApiDocument[]**](../Model/EcedoERPCRMInterfaceApiDocument.md)

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysDocumentsStoreNexusBallNotification**
> string sysDocumentsStoreNexusBallNotification()

Uploaden van BALLNotificationEnvelopes (Nexus)

Via deze API kunnen BALLNotificationEnvelope XML bestanden geüploaden worden.<br />  Deze bestanden worden via EDSN Nexus verstuurd naar marktpartijen. Als een leverancier deze BALL-berichten in haar applicatielandschap heeft en naar Ecedo wil versturen kan dat via deze API.<br /><br />  De request moet verstuurd worden als multipart/form-data met een File.  <br />  De response bevat het aangemaakte DocumentId (guid)

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

$apiInstance = new Swagger\Client\Api\SysDocumentsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->sysDocumentsStoreNexusBallNotification();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysDocumentsApi->sysDocumentsStoreNexusBallNotification: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters
This endpoint does not need any parameter.

### Return type

**string**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysDocumentsStorePVNEDTimeSeriesDocument**
> string sysDocumentsStorePVNEDTimeSeriesDocument()

Upload and process PVNED's Time Series Document

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

$apiInstance = new Swagger\Client\Api\SysDocumentsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->sysDocumentsStorePVNEDTimeSeriesDocument();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysDocumentsApi->sysDocumentsStorePVNEDTimeSeriesDocument: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters
This endpoint does not need any parameter.

### Return type

**string**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sysDocumentsUploadUserDocument**
> object sysDocumentsUploadUserDocument($organization_id, $user_document_type, $comment)

Upload document

Post methode om een document toe te voegen aan een organisatie

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

$apiInstance = new Swagger\Client\Api\SysDocumentsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = "organization_id_example"; // string | 
$user_document_type = "user_document_type_example"; // string | 
$comment = "comment_example"; // string | 

try {
    $result = $apiInstance->sysDocumentsUploadUserDocument($organization_id, $user_document_type, $comment);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SysDocumentsApi->sysDocumentsUploadUserDocument: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **string**|  |
 **user_document_type** | **string**|  |
 **comment** | **string**|  | [optional]

### Return type

**object**

### Authorization

[Authorization](../../README.md#Authorization), [Ocp-Apim-Subscription-Key](../../README.md#Ocp-Apim-Subscription-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

