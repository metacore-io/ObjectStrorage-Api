# metacore-obs-api
Metacore IOT Core Services


- API version: 0.2
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen


## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/yuregir/ObjectStrorage-Api.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/yuregir/ObjectStrorage-Api.git`)

Then import the package:
```python
import metacore_obs_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import metacore_obs_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import metacore_obs_api
from metacore_obs_api.rest import ApiException
from pprint import pprint

configuration = metacore_obs_api.Configuration()
# Configure API key authorization: ApiKeyHeaderAuth
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
configuration = metacore_obs_api.Configuration()
# Configure API key authorization: ApiKeyQueryAuth
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Defining host is optional and default to https://api.teke.li/api/v1/obs
configuration.host = "https://api.teke.li/api/v1/obs"
# Create an instance of the API class
api_instance = metacore_obs_api.OplogApi(metacore_obs_api.ApiClient(configuration))
oplog_id = 'oplog_id_example' # str | 

try:
    # Retrieves a Oplog document
    api_response = api_instance.get_oplog_item(oplog_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OplogApi->get_oplog_item: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.teke.li/api/v1/obs*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OplogApi* | [**get_oplog_item**](docs/OplogApi.md#get_oplog_item) | **GET** /oplog/{oplogId} | Retrieves a Oplog document
*OplogApi* | [**getoplog**](docs/OplogApi.md#getoplog) | **GET** /oplog | Retrieves one or more oplog
*DashboardApiLogsApi* | [**getdashboard_api_logs**](docs/DashboardApiLogsApi.md#getdashboard_api_logs) | **GET** /dashboard_api_logs | Retrieves one or more dashboard_api_logs
*DashboardApiLogsApi* | [**getdashboard_api_logs_item**](docs/DashboardApiLogsApi.md#getdashboard_api_logs_item) | **GET** /dashboard_api_logs/{dashboard-api-logsId} | Retrieves a dashboard-api-logs document
*DashboardApiLogsApi* | [**patchdashboard_api_logs_item**](docs/DashboardApiLogsApi.md#patchdashboard_api_logs_item) | **PATCH** /dashboard_api_logs/{dashboard-api-logsId} | Updates a dashboard-api-logs document
*DashboardApiLogsApi* | [**postdashboard_api_logs**](docs/DashboardApiLogsApi.md#postdashboard_api_logs) | **POST** /dashboard_api_logs | Stores one or more dashboard_api_logs.
*DashboardApiLogsApi* | [**putdashboard_api_logs_item**](docs/DashboardApiLogsApi.md#putdashboard_api_logs_item) | **PUT** /dashboard_api_logs/{dashboard-api-logsId} | Replaces a dashboard-api-logs document
*DeviceShadowApi* | [**getdevice_shadow**](docs/DeviceShadowApi.md#getdevice_shadow) | **GET** /device_shadow | Retrieves one or more device_shadow
*DeviceShadowApi* | [**getdevice_shadow_item**](docs/DeviceShadowApi.md#getdevice_shadow_item) | **GET** /device_shadow/{device-shadowId} | Retrieves a device-shadow document
*DeviceShadowApi* | [**patchdevice_shadow_item**](docs/DeviceShadowApi.md#patchdevice_shadow_item) | **PATCH** /device_shadow/{device-shadowId} | Updates a device-shadow document
*DeviceShadowApi* | [**postdevice_shadow**](docs/DeviceShadowApi.md#postdevice_shadow) | **POST** /device_shadow | Stores one or more device_shadow.
*DeviceShadowApi* | [**putdevice_shadow_item**](docs/DeviceShadowApi.md#putdevice_shadow_item) | **PUT** /device_shadow/{device-shadowId} | Replaces a device-shadow document
*DeviceTypesApi* | [**getdevice_types**](docs/DeviceTypesApi.md#getdevice_types) | **GET** /device_types | Retrieves one or more device_types
*DeviceTypesApi* | [**getdevice_types_item**](docs/DeviceTypesApi.md#getdevice_types_item) | **GET** /device_types/{device-typesId} | Retrieves a device-types document
*DeviceTypesApi* | [**patchdevice_types_item**](docs/DeviceTypesApi.md#patchdevice_types_item) | **PATCH** /device_types/{device-typesId} | Updates a device-types document
*DeviceTypesApi* | [**postdevice_types**](docs/DeviceTypesApi.md#postdevice_types) | **POST** /device_types | Stores one or more device_types.
*DeviceTypesApi* | [**putdevice_types_item**](docs/DeviceTypesApi.md#putdevice_types_item) | **PUT** /device_types/{device-typesId} | Replaces a device-types document
*DevicesApi* | [**getdevices**](docs/DevicesApi.md#getdevices) | **GET** /devices | Retrieves one or more devices
*DevicesApi* | [**getdevices_item**](docs/DevicesApi.md#getdevices_item) | **GET** /devices/{devicesId} | Retrieves a devices document
*DevicesApi* | [**patchdevices_item**](docs/DevicesApi.md#patchdevices_item) | **PATCH** /devices/{devicesId} | Updates a devices document
*DevicesApi* | [**postdevices**](docs/DevicesApi.md#postdevices) | **POST** /devices | Stores one or more devices.
*DevicesApi* | [**putdevices_item**](docs/DevicesApi.md#putdevices_item) | **PUT** /devices/{devicesId} | Replaces a devices document
*GraphSettingsApi* | [**getgraph_settings**](docs/GraphSettingsApi.md#getgraph_settings) | **GET** /graph_settings | Retrieves one or more graph_settings
*GraphSettingsApi* | [**getgraph_settings_item**](docs/GraphSettingsApi.md#getgraph_settings_item) | **GET** /graph_settings/{graph-settingsId} | Retrieves a graph-settings document
*GraphSettingsApi* | [**patchgraph_settings_item**](docs/GraphSettingsApi.md#patchgraph_settings_item) | **PATCH** /graph_settings/{graph-settingsId} | Updates a graph-settings document
*GraphSettingsApi* | [**postgraph_settings**](docs/GraphSettingsApi.md#postgraph_settings) | **POST** /graph_settings | Stores one or more graph_settings.
*GraphSettingsApi* | [**putgraph_settings_item**](docs/GraphSettingsApi.md#putgraph_settings_item) | **PUT** /graph_settings/{graph-settingsId} | Replaces a graph-settings document
*MeasurablesApi* | [**getmeasurables**](docs/MeasurablesApi.md#getmeasurables) | **GET** /measurables | Retrieves one or more measurables
*MeasurablesApi* | [**getmeasurables_item**](docs/MeasurablesApi.md#getmeasurables_item) | **GET** /measurables/{measurablesId} | Retrieves a measurables document
*MeasurablesApi* | [**patchmeasurables_item**](docs/MeasurablesApi.md#patchmeasurables_item) | **PATCH** /measurables/{measurablesId} | Updates a measurables document
*MeasurablesApi* | [**postmeasurables**](docs/MeasurablesApi.md#postmeasurables) | **POST** /measurables | Stores one or more measurables.
*MeasurablesApi* | [**putmeasurables_item**](docs/MeasurablesApi.md#putmeasurables_item) | **PUT** /measurables/{measurablesId} | Replaces a measurables document
*OrganizationDetailsApi* | [**getorg_details**](docs/OrganizationDetailsApi.md#getorg_details) | **GET** /org_details | Retrieves one or more org_details
*OrganizationDetailsApi* | [**getorganization_details_item**](docs/OrganizationDetailsApi.md#getorganization_details_item) | **GET** /org_details/{organization-detailsId} | Retrieves a organization-details document
*OrganizationDetailsApi* | [**patchorganization_details_item**](docs/OrganizationDetailsApi.md#patchorganization_details_item) | **PATCH** /org_details/{organization-detailsId} | Updates a organization-details document
*OrganizationDetailsApi* | [**postorg_details**](docs/OrganizationDetailsApi.md#postorg_details) | **POST** /org_details | Stores one or more org_details.
*OrganizationDetailsApi* | [**putorganization_details_item**](docs/OrganizationDetailsApi.md#putorganization_details_item) | **PUT** /org_details/{organization-detailsId} | Replaces a organization-details document
*OrganizationsApi* | [**getorganizations_item**](docs/OrganizationsApi.md#getorganizations_item) | **GET** /orgs/{organizationsId} | Retrieves a organizations document
*OrganizationsApi* | [**getorgs**](docs/OrganizationsApi.md#getorgs) | **GET** /orgs | Retrieves one or more orgs
*OrganizationsApi* | [**patchorganizations_item**](docs/OrganizationsApi.md#patchorganizations_item) | **PATCH** /orgs/{organizationsId} | Updates a organizations document
*OrganizationsApi* | [**postorgs**](docs/OrganizationsApi.md#postorgs) | **POST** /orgs | Stores one or more orgs.
*OrganizationsApi* | [**putorganizations_item**](docs/OrganizationsApi.md#putorganizations_item) | **PUT** /orgs/{organizationsId} | Replaces a organizations document
*RegionsApi* | [**getregions**](docs/RegionsApi.md#getregions) | **GET** /regions | Retrieves one or more regions
*RegionsApi* | [**getregions_item**](docs/RegionsApi.md#getregions_item) | **GET** /regions/{regionsId} | Retrieves a regions document
*RegionsApi* | [**patchregions_item**](docs/RegionsApi.md#patchregions_item) | **PATCH** /regions/{regionsId} | Updates a regions document
*RegionsApi* | [**postregions**](docs/RegionsApi.md#postregions) | **POST** /regions | Stores one or more regions.
*RegionsApi* | [**putregions_item**](docs/RegionsApi.md#putregions_item) | **PUT** /regions/{regionsId} | Replaces a regions document
*RoleSettingsApi* | [**getrole_settings**](docs/RoleSettingsApi.md#getrole_settings) | **GET** /role_settings | Retrieves one or more role_settings
*RoleSettingsApi* | [**getrole_settings_item**](docs/RoleSettingsApi.md#getrole_settings_item) | **GET** /role_settings/{role-settingsId} | Retrieves a role-settings document
*RoleSettingsApi* | [**patchrole_settings_item**](docs/RoleSettingsApi.md#patchrole_settings_item) | **PATCH** /role_settings/{role-settingsId} | Updates a role-settings document
*RoleSettingsApi* | [**postrole_settings**](docs/RoleSettingsApi.md#postrole_settings) | **POST** /role_settings | Stores one or more role_settings.
*RoleSettingsApi* | [**putrole_settings_item**](docs/RoleSettingsApi.md#putrole_settings_item) | **PUT** /role_settings/{role-settingsId} | Replaces a role-settings document
*RolesApi* | [**getroles**](docs/RolesApi.md#getroles) | **GET** /roles | Retrieves one or more roles
*RolesApi* | [**getroles_item**](docs/RolesApi.md#getroles_item) | **GET** /roles/{rolesId} | Retrieves a roles document
*RolesApi* | [**patchroles_item**](docs/RolesApi.md#patchroles_item) | **PATCH** /roles/{rolesId} | Updates a roles document
*RolesApi* | [**postroles**](docs/RolesApi.md#postroles) | **POST** /roles | Stores one or more roles.
*RolesApi* | [**putroles_item**](docs/RolesApi.md#putroles_item) | **PUT** /roles/{rolesId} | Replaces a roles document
*SensorsApi* | [**getsensors**](docs/SensorsApi.md#getsensors) | **GET** /sensors | Retrieves one or more sensors
*SensorsApi* | [**getsensors_item**](docs/SensorsApi.md#getsensors_item) | **GET** /sensors/{sensorsId} | Retrieves a sensors document
*SensorsApi* | [**patchsensors_item**](docs/SensorsApi.md#patchsensors_item) | **PATCH** /sensors/{sensorsId} | Updates a sensors document
*SensorsApi* | [**postsensors**](docs/SensorsApi.md#postsensors) | **POST** /sensors | Stores one or more sensors.
*SensorsApi* | [**putsensors_item**](docs/SensorsApi.md#putsensors_item) | **PUT** /sensors/{sensorsId} | Replaces a sensors document
*ShownWidgetSettingsApi* | [**getshown_widget_settings**](docs/ShownWidgetSettingsApi.md#getshown_widget_settings) | **GET** /shown_widget_settings | Retrieves one or more shown_widget_settings
*ShownWidgetSettingsApi* | [**getshown_widget_settings_item**](docs/ShownWidgetSettingsApi.md#getshown_widget_settings_item) | **GET** /shown_widget_settings/{shown-widget-settingsId} | Retrieves a shown-widget-settings document
*ShownWidgetSettingsApi* | [**patchshown_widget_settings_item**](docs/ShownWidgetSettingsApi.md#patchshown_widget_settings_item) | **PATCH** /shown_widget_settings/{shown-widget-settingsId} | Updates a shown-widget-settings document
*ShownWidgetSettingsApi* | [**postshown_widget_settings**](docs/ShownWidgetSettingsApi.md#postshown_widget_settings) | **POST** /shown_widget_settings | Stores one or more shown_widget_settings.
*ShownWidgetSettingsApi* | [**putshown_widget_settings_item**](docs/ShownWidgetSettingsApi.md#putshown_widget_settings_item) | **PUT** /shown_widget_settings/{shown-widget-settingsId} | Replaces a shown-widget-settings document
*TenantsApi* | [**gettenants**](docs/TenantsApi.md#gettenants) | **GET** /tenants | Retrieves one or more tenants
*TenantsApi* | [**gettenants_item**](docs/TenantsApi.md#gettenants_item) | **GET** /tenants/{tenantsId} | Retrieves a tenants document
*TenantsApi* | [**patchtenants_item**](docs/TenantsApi.md#patchtenants_item) | **PATCH** /tenants/{tenantsId} | Updates a tenants document
*TenantsApi* | [**posttenants**](docs/TenantsApi.md#posttenants) | **POST** /tenants | Stores one or more tenants.
*TenantsApi* | [**puttenants_item**](docs/TenantsApi.md#puttenants_item) | **PUT** /tenants/{tenantsId} | Replaces a tenants document
*UsersApi* | [**getusers**](docs/UsersApi.md#getusers) | **GET** /users | Retrieves one or more users
*UsersApi* | [**getusers_item**](docs/UsersApi.md#getusers_item) | **GET** /users/{usersId} | Retrieves a users document
*UsersApi* | [**patchusers_item**](docs/UsersApi.md#patchusers_item) | **PATCH** /users/{usersId} | Updates a users document
*UsersApi* | [**postusers**](docs/UsersApi.md#postusers) | **POST** /users | Stores one or more users.
*UsersApi* | [**putusers_item**](docs/UsersApi.md#putusers_item) | **PUT** /users/{usersId} | Replaces a users document


## Documentation For Models

 - [DashboardApiLogs](docs/DashboardApiLogs.md)
 - [DeviceShadow](docs/DeviceShadow.md)
 - [DeviceTypes](docs/DeviceTypes.md)
 - [Devices](docs/Devices.md)
 - [DevicesLocation](docs/DevicesLocation.md)
 - [Error](docs/Error.md)
 - [ErrorError](docs/ErrorError.md)
 - [GraphSettings](docs/GraphSettings.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [Measurables](docs/Measurables.md)
 - [Oplog](docs/Oplog.md)
 - [OrganizationDetails](docs/OrganizationDetails.md)
 - [Organizations](docs/Organizations.md)
 - [Regions](docs/Regions.md)
 - [RoleSettings](docs/RoleSettings.md)
 - [Roles](docs/Roles.md)
 - [Sensors](docs/Sensors.md)
 - [ShownWidgetSettings](docs/ShownWidgetSettings.md)
 - [Tenants](docs/Tenants.md)
 - [Users](docs/Users.md)


## Documentation For Authorization


## ApiKeyHeaderAuth

- **Type**: API key
- **API key parameter name**: X-Api-Key
- **Location**: HTTP header


## ApiKeyQueryAuth

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: URL query string


## Author

Yuregir TEKELI

