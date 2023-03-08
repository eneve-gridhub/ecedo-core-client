# EcedoERPCRMInterfaceApiExtendedMeter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**measure_unit** | **string** | Aantal getallen per telwerk | [optional] 
**measure_unit_localized** | **string** | Leesbare omschrijving van MeasureUnit | [optional] 
**administrative_status_code** | **string** | Administratieve status van de meter | [optional] 
**administrative_status_code_localized** | **string** | Leesbare omschrijving van AdministrativeStatusCode | [optional] 
**communication_status_code** | **string** | Uitleesbaarheid slimme meter (Technisch niet/wel op afstand uitleesbaar)  SMU (Technisch uitleesbaar) / SMN (Technisch niet uitleesbaar) | [optional] 
**communication_status_code_localized** | **string** | Leesbare omschrijving van CommunicationStatusCode | [optional] 
**no_dials** | **int** | Aantal telwerken | [optional] 
**start_date** | [**\DateTime**](\DateTime.md) | Installatiedatum van de meter  Bij een phase III is dit onbekend en zal een fictieve datum (01-01-2000) worden teruggegeven | [optional] 
**end_date** | [**\DateTime**](\DateTime.md) |  | [optional] 
**meter_id** | **string** | Het Ecedo ID (GUID) van de Meter wanneer deze in Ecedo bekend is. Als de meter uit het C-AR wordt opgehaald, is het ID van de meter \&quot;00000000-0000-0000-0000-000000000000\&quot; | [optional] 
**meter_type** | **string** | Het metertype | [optional] 
**meter_type_localized** | **string** | De Nederlandse vertaling van het metertype | [optional] 
**meter_number** | **string** | Het meternummer | [optional] 
**no_digits** | **int** | Aantal getallen per telwerk | [optional] 
**meter_registers_direction_type** | **string** | Omschrijving van het aantal telwerken en de richting van de telwerken.  L staat voor levering, T staat voor teruglevering.  LL is een meter met twee telwerken die beide levering registreren.  LT is een meter met twee telwerken waarvan de ene levering en de andere teruglevering registreert. | [optional] 
**meter_registers_direction_type_localized** | **string** | Leesbare omschrijving van MeterRegistersDirectionType | [optional] 
**meter_dial_position_order_type** | **string** | Geeft aan welke telweken volume van het normaaltarief registreren en welke telwerken het volume van het daltarief | [optional] 
**meter_dial_position_order_type_localized** | **string** | Leesbare omschrijving van MeterDialPositionOrderType | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


