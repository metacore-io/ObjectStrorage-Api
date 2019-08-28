# metacore_obs_api.ShownWidgetSettingsApi

All URIs are relative to *https://api.teke.li/api/v1/obs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getshown_widget_settings**](ShownWidgetSettingsApi.md#getshown_widget_settings) | **GET** /shown_widget_settings | Retrieves one or more shown_widget_settings
[**getshown_widget_settings_item**](ShownWidgetSettingsApi.md#getshown_widget_settings_item) | **GET** /shown_widget_settings/{shown-widget-settingsId} | Retrieves a shown-widget-settings document
[**patchshown_widget_settings_item**](ShownWidgetSettingsApi.md#patchshown_widget_settings_item) | **PATCH** /shown_widget_settings/{shown-widget-settingsId} | Updates a shown-widget-settings document
[**postshown_widget_settings**](ShownWidgetSettingsApi.md#postshown_widget_settings) | **POST** /shown_widget_settings | Stores one or more shown_widget_settings.
[**putshown_widget_settings_item**](ShownWidgetSettingsApi.md#putshown_widget_settings_item) | **PUT** /shown_widget_settings/{shown-widget-settingsId} | Replaces a shown-widget-settings document


# **getshown_widget_settings**
> InlineResponse20013 getshown_widget_settings(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more shown_widget_settings

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
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
api_instance = metacore_obs_api.ShownWidgetSettingsApi(metacore_obs_api.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

try:
    # Retrieves one or more shown_widget_settings
    api_response = api_instance.getshown_widget_settings(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShownWidgetSettingsApi->getshown_widget_settings: %s\n" % e)
```

* Api Key Authentication (ApiKeyQueryAuth):
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
api_instance = metacore_obs_api.ShownWidgetSettingsApi(metacore_obs_api.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

try:
    # Retrieves one or more shown_widget_settings
    api_response = api_instance.getshown_widget_settings(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShownWidgetSettingsApi->getshown_widget_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of shown_widget_settings |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getshown_widget_settings_item**
> ShownWidgetSettings getshown_widget_settings_item(shown_widget_settings_id)

Retrieves a shown-widget-settings document

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
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
api_instance = metacore_obs_api.ShownWidgetSettingsApi(metacore_obs_api.ApiClient(configuration))
shown_widget_settings_id = 'shown_widget_settings_id_example' # str | 

try:
    # Retrieves a shown-widget-settings document
    api_response = api_instance.getshown_widget_settings_item(shown_widget_settings_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShownWidgetSettingsApi->getshown_widget_settings_item: %s\n" % e)
```

* Api Key Authentication (ApiKeyQueryAuth):
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
api_instance = metacore_obs_api.ShownWidgetSettingsApi(metacore_obs_api.ApiClient(configuration))
shown_widget_settings_id = 'shown_widget_settings_id_example' # str | 

try:
    # Retrieves a shown-widget-settings document
    api_response = api_instance.getshown_widget_settings_item(shown_widget_settings_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShownWidgetSettingsApi->getshown_widget_settings_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shown_widget_settings_id** | **str**|  | 

### Return type

[**ShownWidgetSettings**](ShownWidgetSettings.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shown-widget-settings document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchshown_widget_settings_item**
> patchshown_widget_settings_item(shown_widget_settings_id, if_match, shown_widget_settings)

Updates a shown-widget-settings document

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
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
api_instance = metacore_obs_api.ShownWidgetSettingsApi(metacore_obs_api.ApiClient(configuration))
shown_widget_settings_id = 'shown_widget_settings_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
shown_widget_settings = metacore_obs_api.ShownWidgetSettings() # ShownWidgetSettings | A shown-widget-settings or list of shown-widget-settings documents

try:
    # Updates a shown-widget-settings document
    api_instance.patchshown_widget_settings_item(shown_widget_settings_id, if_match, shown_widget_settings)
except ApiException as e:
    print("Exception when calling ShownWidgetSettingsApi->patchshown_widget_settings_item: %s\n" % e)
```

* Api Key Authentication (ApiKeyQueryAuth):
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
api_instance = metacore_obs_api.ShownWidgetSettingsApi(metacore_obs_api.ApiClient(configuration))
shown_widget_settings_id = 'shown_widget_settings_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
shown_widget_settings = metacore_obs_api.ShownWidgetSettings() # ShownWidgetSettings | A shown-widget-settings or list of shown-widget-settings documents

try:
    # Updates a shown-widget-settings document
    api_instance.patchshown_widget_settings_item(shown_widget_settings_id, if_match, shown_widget_settings)
except ApiException as e:
    print("Exception when calling ShownWidgetSettingsApi->patchshown_widget_settings_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shown_widget_settings_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 
 **shown_widget_settings** | [**ShownWidgetSettings**](ShownWidgetSettings.md)| A shown-widget-settings or list of shown-widget-settings documents | 

### Return type

void (empty response body)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shown-widget-settings document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postshown_widget_settings**
> postshown_widget_settings(shown_widget_settings)

Stores one or more shown_widget_settings.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
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
api_instance = metacore_obs_api.ShownWidgetSettingsApi(metacore_obs_api.ApiClient(configuration))
shown_widget_settings = metacore_obs_api.ShownWidgetSettings() # ShownWidgetSettings | A shown-widget-settings or list of shown-widget-settings documents

try:
    # Stores one or more shown_widget_settings.
    api_instance.postshown_widget_settings(shown_widget_settings)
except ApiException as e:
    print("Exception when calling ShownWidgetSettingsApi->postshown_widget_settings: %s\n" % e)
```

* Api Key Authentication (ApiKeyQueryAuth):
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
api_instance = metacore_obs_api.ShownWidgetSettingsApi(metacore_obs_api.ApiClient(configuration))
shown_widget_settings = metacore_obs_api.ShownWidgetSettings() # ShownWidgetSettings | A shown-widget-settings or list of shown-widget-settings documents

try:
    # Stores one or more shown_widget_settings.
    api_instance.postshown_widget_settings(shown_widget_settings)
except ApiException as e:
    print("Exception when calling ShownWidgetSettingsApi->postshown_widget_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shown_widget_settings** | [**ShownWidgetSettings**](ShownWidgetSettings.md)| A shown-widget-settings or list of shown-widget-settings documents | 

### Return type

void (empty response body)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | operation has been successful |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putshown_widget_settings_item**
> putshown_widget_settings_item(shown_widget_settings_id, if_match, shown_widget_settings)

Replaces a shown-widget-settings document

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
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
api_instance = metacore_obs_api.ShownWidgetSettingsApi(metacore_obs_api.ApiClient(configuration))
shown_widget_settings_id = 'shown_widget_settings_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
shown_widget_settings = metacore_obs_api.ShownWidgetSettings() # ShownWidgetSettings | A shown-widget-settings or list of shown-widget-settings documents

try:
    # Replaces a shown-widget-settings document
    api_instance.putshown_widget_settings_item(shown_widget_settings_id, if_match, shown_widget_settings)
except ApiException as e:
    print("Exception when calling ShownWidgetSettingsApi->putshown_widget_settings_item: %s\n" % e)
```

* Api Key Authentication (ApiKeyQueryAuth):
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
api_instance = metacore_obs_api.ShownWidgetSettingsApi(metacore_obs_api.ApiClient(configuration))
shown_widget_settings_id = 'shown_widget_settings_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
shown_widget_settings = metacore_obs_api.ShownWidgetSettings() # ShownWidgetSettings | A shown-widget-settings or list of shown-widget-settings documents

try:
    # Replaces a shown-widget-settings document
    api_instance.putshown_widget_settings_item(shown_widget_settings_id, if_match, shown_widget_settings)
except ApiException as e:
    print("Exception when calling ShownWidgetSettingsApi->putshown_widget_settings_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shown_widget_settings_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 
 **shown_widget_settings** | [**ShownWidgetSettings**](ShownWidgetSettings.md)| A shown-widget-settings or list of shown-widget-settings documents | 

### Return type

void (empty response body)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shown-widget-settings document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

