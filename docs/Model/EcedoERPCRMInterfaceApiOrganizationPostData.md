# EcedoERPCRMInterfaceApiOrganizationPostData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process_settings** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiOrganizationPostDataProcessSettingsPostData**](EcedoERPCRMInterfaceApiOrganizationPostDataProcessSettingsPostData.md) |  | [optional] 
**organization_type** | **string** | Verplicht veld waarmee aangegeven wordt of dit een zakelijke of particuliere klant is | [optional] 
**client_reference** | **string** | Als Ecedo klantnummers genereert is dit een vrij veld waar een externe referentie in vastgelegd kan worden.&lt;br /&gt;  Als Ecedo de klantnummers niet genereert dan moet het gewenste klantnummer via dit veld ingestuurd worden | [optional] 
**sales_reference** | **string** | Vrij veld waarin bijvoorbeeld vastgelegd kan worden via welke sale deze klant is gewonnen | [optional] 
**channel** | **string** | Vrij veld waarin bijvoorbeeld vastgelegd kan worden via welk kanaal de klant is gewonnen | [optional] 
**origin_reference** | **string** | Vrij veld waarin bijvoorbeeld vastgelegd kan worden via welk bron de klant is gewonnen | [optional] 
**name** | **string** | Verplicht veld met de bedrijfsnaam wanneer een zakelijke klant wordt aangemaakt. Dit veld mag niet gevuld zijn bij consumenten. | [optional] 
**phone_number** | **string** | Optioneel veld waarin het vaste telefoonnummer van de klant kan worden opgeslagen | [optional] 
**mobile_number** | **string** | Optioneel veld waarin het mobiele telefoonnummer van de klant kan worden opgeslagen | [optional] 
**email_address** | **string** | Optioneel veld waarin het e-mailadres van de klant kan worden opgeslagen | [optional] 
**e_invoice_address** | **string** | Optioneel e-factuuradres van de klant. Dit adres is nodig wanneer er e-facturen voor de klant aangemaakt moeten worden. | [optional] 
**bad_payment_history** | **bool** | Optioneel veld waarmee aangegeven kan worden dat de klant een slechte betaalhistorie heeft. De waarde van dit veld is ter registratie en heeft geen impact op processen | [optional] 
**has_receiver** | **bool** | Optioneel veld waarmee aangegeven kan worden dat de klant een bewindvoerder heeft. De waarde van dit veld is ter registratie en heeft geen impact op processen | [optional] 
**with_collection_agency** | **bool** | Optioneel veld waarmee aangegeven kan worden dat de klant bij een incassobureau is aangemeld. De waarde van dit veld is ter registratie en heeft geen impact op processen | [optional] 
**news_letter** | **bool** | Optioneel veld waarmee aangegeven kan worden dat de klant een nieuwsbrief wil ontvangen. De waarde van dit veld is ter registratie en heeft geen impact op processen. De leverancier is zelf verantwoordelijk voor het versturen van de nieuwsbrief | [optional] 
**product_or_service_info** | **bool** | Optioneel veld waarmee aangegeven kan worden dat de klant informatie over producten of diensten wil ontvangen. De waarde van dit veld is ter registratie en heeft geen impact op processen. De leverancier is zelf verantwoordelijk voor het versturen van de informatie | [optional] 
**print_welcome_letter** | **bool** | Optioneel veld waarmee aangegeven kan worden dat de klant geen welkomstbrief wil ontvangen. Alleen de waarde \&quot;false\&quot; is toegestaan | [optional] 
**block_settlement_active** | **bool** | Optioneel veld waarmee aangegeven kan worden dat de klant een factuurblokkade moet krijgen | [optional] 
**block_settlement_comment** | **string** | Optioneel veld waarmee aangegeven kan worden waarom de klant een factuurblokkade heeft gekregen | [optional] 
**preferred_contact_method** | **string** | Optioneel veld waarmee de standaard communicatiemethode overschreven kan worden. Dit heeft bijvoorbeeld invloed op de methode waarmee de welkomstbrief wordt verstuurd | [optional] 
**kvk_number** | **string** | Optioneel veld waarin het KvK-nummer van een zakelijke klant vastgelegd kan worden | [optional] 
**vat_number** | **string** | Optioneel veld waarin het btw-nummer van een zakelijke klant vastgelegd kan worden | [optional] 
**is_parent** | **bool** | Optioneel veld waarmee aangegeven kan worden dat de klant een moederorganisatie is. Dit is alleen toegestaan bij zakelijke klanten | [optional] 
**parent_organization_id** | **string** | Optioneel veld waarmee aangegeven kan worden dat de klant een dochterorganisatie is. De OrganizationId van de moederorganisatie moet meegegeven worden. Dit is alleen toegestaan bij zakelijke klanten | [optional] 
**organization_group_id** | **string** | Optioneel veld waarmee de klant in een specifieke klantgroep geplaatst kan worden. Als dit veld niet wordt meegegeven wordt de klant automatisch in de klantgroep \&quot;Algemeen\&quot; geplaatst | [optional] 
**invoice_group_reference** | **string** | Dochterorganisaties moeten in een factuurgroep geplaatst worden. De referentie van de factuurgroep (die bij de moeder aangemaakt moet zijn) moet in deze variabele worden meegegeven. | [optional] 
**mailing_address** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAddressPostData**](EcedoERPCRMInterfaceApiAddressPostData.md) | Postadres van de klant | [optional] 
**business_address** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiAddressPostData**](EcedoERPCRMInterfaceApiAddressPostData.md) | Eventueel afwijkend vestigingsadres van de klant. Alleen toegestaan bij zakelijke klanten | [optional] 
**person** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiPersonPostData**](EcedoERPCRMInterfaceApiPersonPostData.md) | De gegevens van de primaire contactpersoon | [optional] 
**debtor** | [**\Swagger\Client\Model\EcedoERPCRMInterfaceApiDebtorPostData**](EcedoERPCRMInterfaceApiDebtorPostData.md) | Debiteur- en betaalgegevens | [optional] 
**registered_seat** | **string** | Optioneel veld voor zakelijke klanten waarmee aangegeven worden waar de klant statutair gevestigd is | [optional] 
**authorized_signatory** | **string** | Optioneel veld voor zakelijke klanten waarmee aangegeven worden wie tekenbevoegd is | [optional] 
**representative_id** | **string** | Optioneel veld waarmee de verkoper die de klant heeft getekend geregistreerd kan worden. De verkoper moet aangemaakt zijn via de GUI | [optional] 
**is_intercompany** | **bool** | Optioneel veld waarmee bij zakelijke klanten aangegeven kan worden dat de facturen intercompany verstuurd worden | [optional] 
**company_label_id** | **string** | Verplicht veld wanneer er meerdere labels geconfigureerd zijn. Dit veld moet het ID bevatten van het label waar de klant in ondergebracht moet worden | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


