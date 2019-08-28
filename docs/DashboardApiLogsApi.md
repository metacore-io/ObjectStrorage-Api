# metacore_obs_api.DashboardApiLogsApi

All URIs are relative to *https://api.teke.li/api/v1/obs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getdashboard_api_logs**](DashboardApiLogsApi.md#getdashboard_api_logs) | **GET** /dashboard_api_logs | Retrieves one or more dashboard_api_logs
[**getdashboard_api_logs_item**](DashboardApiLogsApi.md#getdashboard_api_logs_item) | **GET** /dashboard_api_logs/{dashboard-api-logsId} | Retrieves a dashboard-api-logs document
[**patchdashboard_api_logs_item**](DashboardApiLogsApi.md#patchdashboard_api_logs_item) | **PATCH** /dashboard_api_logs/{dashboard-api-logsId} | Updates a dashboard-api-logs document
[**postdashboard_api_logs**](DashboardApiLogsApi.md#postdashboard_api_logs) | **POST** /dashboard_api_logs | Stores one or more dashboard_api_logs.
[**putdashboard_api_logs_item**](DashboardApiLogsApi.md#putdashboard_api_logs_item) | **PUT** /dashboard_api_logs/{dashboard-api-logsId} | Replaces a dashboard-api-logs document


# **getdashboard_api_logs**
> InlineResponse200 getdashboard_api_logs(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more dashboard_api_logs

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
api_instance = metacore_obs_api.DashboardApiLogsApi(metacore_obs_api.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

try:
    # Retrieves one or more dashboard_api_logs
    api_response = api_instance.getdashboard_api_logs(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApiLogsApi->getdashboard_api_logs: %s\n" % e)
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
api_instance = metacore_obs_api.DashboardApiLogsApi(metacore_obs_api.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

try:
    # Retrieves one or more dashboard_api_logs
    api_response = api_instance.getdashboard_api_logs(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApiLogsApi->getdashboard_api_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of dashboard_api_logs |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getdashboard_api_logs_item**
> DashboardApiLogs getdashboard_api_logs_item(dashboard_api_logs_id)

Retrieves a dashboard-api-logs document

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
api_instance = metacore_obs_api.DashboardApiLogsApi(metacore_obs_api.ApiClient(configuration))
dashboard_api_logs_id = 'dashboard_api_logs_id_example' # str | 

try:
    # Retrieves a dashboard-api-logs document
    api_response = api_instance.getdashboard_api_logs_item(dashboard_api_logs_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApiLogsApi->getdashboard_api_logs_item: %s\n" % e)
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
api_instance = metacore_obs_api.DashboardApiLogsApi(metacore_obs_api.ApiClient(configuration))
dashboard_api_logs_id = 'dashboard_api_logs_id_example' # str | 

try:
    # Retrieves a dashboard-api-logs document
    api_response = api_instance.getdashboard_api_logs_item(dashboard_api_logs_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApiLogsApi->getdashboard_api_logs_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_api_logs_id** | **str**|  | 

### Return type

[**DashboardApiLogs**](DashboardApiLogs.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | dashboard-api-logs document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchdashboard_api_logs_item**
> patchdashboard_api_logs_item(dashboard_api_logs_id, if_match, dashboard_api_logs)

Updates a dashboard-api-logs document

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
api_instance = metacore_obs_api.DashboardApiLogsApi(metacore_obs_api.ApiClient(configuration))
dashboard_api_logs_id = 'dashboard_api_logs_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
dashboard_api_logs = metacore_obs_api.DashboardApiLogs() # DashboardApiLogs | A dashboard-api-logs or list of dashboard-api-logs documents

try:
    # Updates a dashboard-api-logs document
    api_instance.patchdashboard_api_logs_item(dashboard_api_logs_id, if_match, dashboard_api_logs)
except ApiException as e:
    print("Exception when calling DashboardApiLogsApi->patchdashboard_api_logs_item: %s\n" % e)
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
api_instance = metacore_obs_api.DashboardApiLogsApi(metacore_obs_api.ApiClient(configuration))
dashboard_api_logs_id = 'dashboard_api_logs_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
dashboard_api_logs = metacore_obs_api.DashboardApiLogs() # DashboardApiLogs | A dashboard-api-logs or list of dashboard-api-logs documents

try:
    # Updates a dashboard-api-logs document
    api_instance.patchdashboard_api_logs_item(dashboard_api_logs_id, if_match, dashboard_api_logs)
except ApiException as e:
    print("Exception when calling DashboardApiLogsApi->patchdashboard_api_logs_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_api_logs_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 
 **dashboard_api_logs** | [**DashboardApiLogs**](DashboardApiLogs.md)| A dashboard-api-logs or list of dashboard-api-logs documents | 

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
**200** | dashboard-api-logs document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postdashboard_api_logs**
> postdashboard_api_logs(dashboard_api_logs)

Stores one or more dashboard_api_logs.

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
api_instance = metacore_obs_api.DashboardApiLogsApi(metacore_obs_api.ApiClient(configuration))
dashboard_api_logs = metacore_obs_api.DashboardApiLogs() # DashboardApiLogs | A dashboard-api-logs or list of dashboard-api-logs documents

try:
    # Stores one or more dashboard_api_logs.
    api_instance.postdashboard_api_logs(dashboard_api_logs)
except ApiException as e:
    print("Exception when calling DashboardApiLogsApi->postdashboard_api_logs: %s\n" % e)
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
api_instance = metacore_obs_api.DashboardApiLogsApi(metacore_obs_api.ApiClient(configuration))
dashboard_api_logs = metacore_obs_api.DashboardApiLogs() # DashboardApiLogs | A dashboard-api-logs or list of dashboard-api-logs documents

try:
    # Stores one or more dashboard_api_logs.
    api_instance.postdashboard_api_logs(dashboard_api_logs)
except ApiException as e:
    print("Exception when calling DashboardApiLogsApi->postdashboard_api_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_api_logs** | [**DashboardApiLogs**](DashboardApiLogs.md)| A dashboard-api-logs or list of dashboard-api-logs documents | 

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

# **putdashboard_api_logs_item**
> putdashboard_api_logs_item(dashboard_api_logs_id, if_match, dashboard_api_logs)

Replaces a dashboard-api-logs document

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
api_instance = metacore_obs_api.DashboardApiLogsApi(metacore_obs_api.ApiClient(configuration))
dashboard_api_logs_id = 'dashboard_api_logs_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
dashboard_api_logs = metacore_obs_api.DashboardApiLogs() # DashboardApiLogs | A dashboard-api-logs or list of dashboard-api-logs documents

try:
    # Replaces a dashboard-api-logs document
    api_instance.putdashboard_api_logs_item(dashboard_api_logs_id, if_match, dashboard_api_logs)
except ApiException as e:
    print("Exception when calling DashboardApiLogsApi->putdashboard_api_logs_item: %s\n" % e)
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
api_instance = metacore_obs_api.DashboardApiLogsApi(metacore_obs_api.ApiClient(configuration))
dashboard_api_logs_id = 'dashboard_api_logs_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
dashboard_api_logs = metacore_obs_api.DashboardApiLogs() # DashboardApiLogs | A dashboard-api-logs or list of dashboard-api-logs documents

try:
    # Replaces a dashboard-api-logs document
    api_instance.putdashboard_api_logs_item(dashboard_api_logs_id, if_match, dashboard_api_logs)
except ApiException as e:
    print("Exception when calling DashboardApiLogsApi->putdashboard_api_logs_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_api_logs_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 
 **dashboard_api_logs** | [**DashboardApiLogs**](DashboardApiLogs.md)| A dashboard-api-logs or list of dashboard-api-logs documents | 

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
**200** | dashboard-api-logs document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

