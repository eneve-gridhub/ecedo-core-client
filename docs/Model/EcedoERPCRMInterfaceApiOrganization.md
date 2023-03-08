# EcedoERPCRMInterfaceApiOrganization

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_invoice_address** | **string** | Optioneel e-factuuradres van de klant | [optional] 
**preferred_contact_method** | **string** | Optioneel veld waarmee de standaard communicatiemethode overschreven kan worden. Dit heeft bijvoorbeeld invloed op de methode waarmee de welkomstbrief wordt verstuurd | [optional] 
**preferred_contact_method_localized** | **string** | Nederlandse vertaling van PreferredContactMethod | [optional] 
**bad_payment_history** | **bool** | Optioneel veld waarmee aangegeven kan worden dat de klant een slechte betaalhistorie heeft. De waarde van dit veld is ter registratie en heeft geen impact op processen | [optional] 
**has_receiver** | **bool** | Optioneel veld waarmee aangegeven kan worden dat de klant een bewindvoerder heeft. De waarde van dit veld is ter registratie en heeft geen impact op processen | [optional] 
**channel** | **string** | Vrij veld waarin bijvoorbeeld vastgelegd kan worden via welk kanaal de klant is gewonnen | [optional] 
**origin_reference** | **string** | Vrij veld waarin bijvoorbeeld vastgelegd kan worden via welk bron de klant is gewonnen | [optional] 
**client_reference** | **string** | Als Ecedo klantnummers genereert is dit een vrij veld waar een externe referentie in vastgelegd kan worden.&lt;br /&gt;  Als Ecedo de klantnummers niet genereert bevat dit veld een kopie de Reference | [optional] 
**sales_reference** | **string** | Vrij veld waarin bijvoorbeeld vastgelegd kan worden via welke sale deze klant is gewonnen | [optional] 
**parent_organization_id** | **string** | Optioneel veld waarmee aangegeven kan worden dat de klant een dochterorganisatie is. Dit veld bevat het  OrganizationId van de moederorganisatie. Dit is alleen mogelijk bij zakelijke klanten | [optional] 
**is_parent** | **bool** | Optioneel veld waarmee aangegeven kan worden dat de klant een moederorganisatie is. Dit is alleen mogelijk bij zakelijke klanten | [optional] 
**address** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAddress**](EcedoERPCRMInterfaceApiAddress.md) | Postadres van de klant | [optional] 
**business_address** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAddress**](EcedoERPCRMInterfaceApiAddress.md) | Eventueel afwijkend vestigingsadres van de klant. Alleen van toepassing bij zakelijke klanten | [optional] 
**debtor** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiDebtor**](EcedoERPCRMInterfaceApiDebtor.md) | Debiteur- en betaalgegevens | [optional] 
**representative** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiRepresentativeBase**](EcedoERPCRMInterfaceApiRepresentativeBase.md) | Optioneel veld waarmee de verkoper die de klant heeft getekend geregistreerd kan worden | [optional] 
**is_producer** | **bool** | Geeft aan of de klant een producent is. Alleen van toepassing bij zakelijke klanten | [optional] 
**kv_k_number** | **string** | Optioneel veld waarin het KvK-nummer van een zakelijke klant vastgelegd kan worden | [optional] 
**vat_number** | **string** | Optioneel veld waarin het btw-nummer van een zakelijke klant vastgelegd kan worden | [optional] 
**connections** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiConnection[]**](EcedoERPCRMInterfaceApiConnection.md) | Een lijst van aansluitingen die bij de klant bekend zijn. Of deze lijst gevuld is is afhankelijk van de API en de meegegeven query-parameters | [optional] 
**registered_seat** | **string** | Optioneel veld voor zakelijke klanten waarmee aangegeven worden waar de klant statutair gevestigd is | [optional] 
**authorized_signatory** | **string** | Optioneel veld voor zakelijke klanten waarmee aangegeven worden wie tekenbevoegd is | [optional] 
**representative_id** | **string** | Optioneel veld waarmee de verkoper die de klant heeft getekend geregistreerd kan worden. Dit veld is een duplicaat van het Representative-object | [optional] 
**product_or_service_info** | **bool** | Optioneel veld waarmee aangegeven kan worden dat de klant informatie over producten of diensten wil ontvangen. De waarde van dit veld is ter registratie en heeft geen impact op processen. De leverancier is zelf verantwoordelijk voor het versturen van de informatie | [optional] 
**print_welcome_letter** | **bool** | Optioneel veld waarmee aangegeven kan worden dat de klant geen welkomstbrief wil ontvangen. Alleen de waarde \&quot;false\&quot; is mogelijk | [optional] 
**with_collection_agency** | **bool** | Optioneel veld waarmee aangegeven kan worden dat de klant bij een incassobureau is aangemeld. De waarde van dit veld is ter registratie en heeft geen impact op processen | [optional] 
**is_intercompany** | **bool** | Optioneel veld waarmee bij zakelijke klanten aangegeven kan worden dat de facturen intercompany verstuurd worden | [optional] 
**company_label_id** | **string** |  | [optional] 
**organization_type** | **string** | Geeft aan of het een zakelijke of particuliere klant is | [optional] 
**organization_type_localized** | **string** | Nederlandse vertaling van OrganizationType | [optional] 
**organization_id** | **string** | Het unieke ID van deze klant | [optional] 
**reference** | **string** | Ket klantnummer van de klant | [optional] 
**organization_group_id** | **string** | Ket klantnummer van de klant | [optional] 
**organization_group** | **string** | De naam van de klantgroep waarin de klant is geplaatst | [optional] 
**name** | **string** | Bij zakelijke klanten bevat dit veld de bedrijfsnaam. Bij consumenten is dit een samengestelde naam op basis van de persoonsgegevens van de klant | [optional] 
**phone_number** | **string** | Optioneel veld waarin het vaste telefoonnummer van de klant kan worden opgeslagen | [optional] 
**mobile_number** | **string** | Optioneel veld waarin het mobiele telefoonnummer van de klant kan worden opgeslagen | [optional] 
**fax_number** | **string** | Optioneel veld waarin het faxnummer van de klant kan worden opgeslagen | [optional] 
**email** | **string** | Optioneel veld waarin het e-mailadres van de klant kan worden opgeslagen | [optional] 
**person** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiPerson**](EcedoERPCRMInterfaceApiPerson.md) | De gegevens van de primaire contactpersoon | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


