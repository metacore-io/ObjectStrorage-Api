# metacore_obs_api.GraphSettingsApi

All URIs are relative to *https://api.teke.li/api/v1/obs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getgraph_settings**](GraphSettingsApi.md#getgraph_settings) | **GET** /graph_settings | Retrieves one or more graph_settings
[**getgraph_settings_item**](GraphSettingsApi.md#getgraph_settings_item) | **GET** /graph_settings/{graph-settingsId} | Retrieves a graph-settings document
[**patchgraph_settings_item**](GraphSettingsApi.md#patchgraph_settings_item) | **PATCH** /graph_settings/{graph-settingsId} | Updates a graph-settings document
[**postgraph_settings**](GraphSettingsApi.md#postgraph_settings) | **POST** /graph_settings | Stores one or more graph_settings.
[**putgraph_settings_item**](GraphSettingsApi.md#putgraph_settings_item) | **PUT** /graph_settings/{graph-settingsId} | Replaces a graph-settings document


# **getgraph_settings**
> InlineResponse2004 getgraph_settings(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more graph_settings

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
api_instance = metacore_obs_api.GraphSettingsApi(metacore_obs_api.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

try:
    # Retrieves one or more graph_settings
    api_response = api_instance.getgraph_settings(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphSettingsApi->getgraph_settings: %s\n" % e)
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
api_instance = metacore_obs_api.GraphSettingsApi(metacore_obs_api.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

try:
    # Retrieves one or more graph_settings
    api_response = api_instance.getgraph_settings(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphSettingsApi->getgraph_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of graph_settings |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getgraph_settings_item**
> GraphSettings getgraph_settings_item(graph_settings_id)

Retrieves a graph-settings document

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
api_instance = metacore_obs_api.GraphSettingsApi(metacore_obs_api.ApiClient(configuration))
graph_settings_id = 'graph_settings_id_example' # str | 

try:
    # Retrieves a graph-settings document
    api_response = api_instance.getgraph_settings_item(graph_settings_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphSettingsApi->getgraph_settings_item: %s\n" % e)
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
api_instance = metacore_obs_api.GraphSettingsApi(metacore_obs_api.ApiClient(configuration))
graph_settings_id = 'graph_settings_id_example' # str | 

try:
    # Retrieves a graph-settings document
    api_response = api_instance.getgraph_settings_item(graph_settings_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphSettingsApi->getgraph_settings_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_settings_id** | **str**|  | 

### Return type

[**GraphSettings**](GraphSettings.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | graph-settings document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchgraph_settings_item**
> patchgraph_settings_item(graph_settings_id, if_match, graph_settings)

Updates a graph-settings document

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
api_instance = metacore_obs_api.GraphSettingsApi(metacore_obs_api.ApiClient(configuration))
graph_settings_id = 'graph_settings_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
graph_settings = metacore_obs_api.GraphSettings() # GraphSettings | A graph-settings or list of graph-settings documents

try:
    # Updates a graph-settings document
    api_instance.patchgraph_settings_item(graph_settings_id, if_match, graph_settings)
except ApiException as e:
    print("Exception when calling GraphSettingsApi->patchgraph_settings_item: %s\n" % e)
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
api_instance = metacore_obs_api.GraphSettingsApi(metacore_obs_api.ApiClient(configuration))
graph_settings_id = 'graph_settings_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
graph_settings = metacore_obs_api.GraphSettings() # GraphSettings | A graph-settings or list of graph-settings documents

try:
    # Updates a graph-settings document
    api_instance.patchgraph_settings_item(graph_settings_id, if_match, graph_settings)
except ApiException as e:
    print("Exception when calling GraphSettingsApi->patchgraph_settings_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_settings_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 
 **graph_settings** | [**GraphSettings**](GraphSettings.md)| A graph-settings or list of graph-settings documents | 

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
**200** | graph-settings document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postgraph_settings**
> postgraph_settings(graph_settings)

Stores one or more graph_settings.

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
api_instance = metacore_obs_api.GraphSettingsApi(metacore_obs_api.ApiClient(configuration))
graph_settings = metacore_obs_api.GraphSettings() # GraphSettings | A graph-settings or list of graph-settings documents

try:
    # Stores one or more graph_settings.
    api_instance.postgraph_settings(graph_settings)
except ApiException as e:
    print("Exception when calling GraphSettingsApi->postgraph_settings: %s\n" % e)
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
api_instance = metacore_obs_api.GraphSettingsApi(metacore_obs_api.ApiClient(configuration))
graph_settings = metacore_obs_api.GraphSettings() # GraphSettings | A graph-settings or list of graph-settings documents

try:
    # Stores one or more graph_settings.
    api_instance.postgraph_settings(graph_settings)
except ApiException as e:
    print("Exception when calling GraphSettingsApi->postgraph_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_settings** | [**GraphSettings**](GraphSettings.md)| A graph-settings or list of graph-settings documents | 

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

# **putgraph_settings_item**
> putgraph_settings_item(graph_settings_id, if_match, graph_settings)

Replaces a graph-settings document

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
api_instance = metacore_obs_api.GraphSettingsApi(metacore_obs_api.ApiClient(configuration))
graph_settings_id = 'graph_settings_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
graph_settings = metacore_obs_api.GraphSettings() # GraphSettings | A graph-settings or list of graph-settings documents

try:
    # Replaces a graph-settings document
    api_instance.putgraph_settings_item(graph_settings_id, if_match, graph_settings)
except ApiException as e:
    print("Exception when calling GraphSettingsApi->putgraph_settings_item: %s\n" % e)
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
api_instance = metacore_obs_api.GraphSettingsApi(metacore_obs_api.ApiClient(configuration))
graph_settings_id = 'graph_settings_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
graph_settings = metacore_obs_api.GraphSettings() # GraphSettings | A graph-settings or list of graph-settings documents

try:
    # Replaces a graph-settings document
    api_instance.putgraph_settings_item(graph_settings_id, if_match, graph_settings)
except ApiException as e:
    print("Exception when calling GraphSettingsApi->putgraph_settings_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_settings_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 
 **graph_settings** | [**GraphSettings**](GraphSettings.md)| A graph-settings or list of graph-settings documents | 

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
**200** | graph-settings document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

