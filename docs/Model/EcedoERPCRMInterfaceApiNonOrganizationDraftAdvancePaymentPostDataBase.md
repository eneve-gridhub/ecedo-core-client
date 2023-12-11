# EcedoERPCRMInterfaceApiNonOrganizationDraftAdvancePaymentPostDataBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_type** | **string** | Optioneel veld (default &#x60;Consumer&#x60;) | [optional] 
**agreement_date** | [**\DateTime**](\DateTime.md) | De tekendatum van het contract. Deze tekendatum wordt gebruikt om te valideren of de propositie(s) geldig waren op het moment van tekenen. Dit is een verplicht veld wanneer de &#x60;AgreementDates&#x60; bij de aansluitingen niet gebruikt worden. | [optional] 
**month** | [**\DateTime**](\DateTime.md) | Optionele maand waarvoor het voorschot berekend moet worden. Bij proposities met wisselende prijzen of bijvoorbeeld rond de jaarwisseling met wisselende energiebelasting-prijzen heeft deze datum invloed op het resultaat. Als deze waarde niet wordt meegegeven dan wordt automatisch de eerstvolgende maand geselecteerd. Als een datum wordt meegegeven moet deze altijd op de eerste dag van een maand vallen. Als de dag van de maand in de meegegeven datum niet de eerste dag van de maand is, dan wordt deze op de eerste dag ingesteld. 2021-10-28 wordt bijvoorbeeld 2021-10-01. | [optional] 
**connections** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiNonOrganizationDraftAdvancePaymentPostConnectionData[]**](EcedoERPCRMInterfaceApiNonOrganizationDraftAdvancePaymentPostConnectionData.md) | De aansluitingen waarvoor het concept-voorschot berekend moet worden. Zie de uitleg in het object voor meer informatie. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


