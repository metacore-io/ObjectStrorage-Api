# metacore_obs_api.DeviceTypesApi

All URIs are relative to *https://api.teke.li/api/v1/obs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getdevice_types**](DeviceTypesApi.md#getdevice_types) | **GET** /device_types | Retrieves one or more device_types
[**getdevice_types_item**](DeviceTypesApi.md#getdevice_types_item) | **GET** /device_types/{device-typesId} | Retrieves a device-types document
[**patchdevice_types_item**](DeviceTypesApi.md#patchdevice_types_item) | **PATCH** /device_types/{device-typesId} | Updates a device-types document
[**postdevice_types**](DeviceTypesApi.md#postdevice_types) | **POST** /device_types | Stores one or more device_types.
[**putdevice_types_item**](DeviceTypesApi.md#putdevice_types_item) | **PUT** /device_types/{device-typesId} | Replaces a device-types document


# **getdevice_types**
> InlineResponse2002 getdevice_types(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more device_types

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
api_instance = metacore_obs_api.DeviceTypesApi(metacore_obs_api.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

try:
    # Retrieves one or more device_types
    api_response = api_instance.getdevice_types(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->getdevice_types: %s\n" % e)
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
api_instance = metacore_obs_api.DeviceTypesApi(metacore_obs_api.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

try:
    # Retrieves one or more device_types
    api_response = api_instance.getdevice_types(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->getdevice_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of device_types |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getdevice_types_item**
> DeviceTypes getdevice_types_item(device_types_id)

Retrieves a device-types document

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
api_instance = metacore_obs_api.DeviceTypesApi(metacore_obs_api.ApiClient(configuration))
device_types_id = 'device_types_id_example' # str | 

try:
    # Retrieves a device-types document
    api_response = api_instance.getdevice_types_item(device_types_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->getdevice_types_item: %s\n" % e)
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
api_instance = metacore_obs_api.DeviceTypesApi(metacore_obs_api.ApiClient(configuration))
device_types_id = 'device_types_id_example' # str | 

try:
    # Retrieves a device-types document
    api_response = api_instance.getdevice_types_item(device_types_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->getdevice_types_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_types_id** | **str**|  | 

### Return type

[**DeviceTypes**](DeviceTypes.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | device-types document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchdevice_types_item**
> patchdevice_types_item(device_types_id, if_match, device_types)

Updates a device-types document

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
api_instance = metacore_obs_api.DeviceTypesApi(metacore_obs_api.ApiClient(configuration))
device_types_id = 'device_types_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
device_types = metacore_obs_api.DeviceTypes() # DeviceTypes | A device-types or list of device-types documents

try:
    # Updates a device-types document
    api_instance.patchdevice_types_item(device_types_id, if_match, device_types)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->patchdevice_types_item: %s\n" % e)
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
api_instance = metacore_obs_api.DeviceTypesApi(metacore_obs_api.ApiClient(configuration))
device_types_id = 'device_types_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
device_types = metacore_obs_api.DeviceTypes() # DeviceTypes | A device-types or list of device-types documents

try:
    # Updates a device-types document
    api_instance.patchdevice_types_item(device_types_id, if_match, device_types)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->patchdevice_types_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_types_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 
 **device_types** | [**DeviceTypes**](DeviceTypes.md)| A device-types or list of device-types documents | 

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
**200** | device-types document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postdevice_types**
> postdevice_types(device_types)

Stores one or more device_types.

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
api_instance = metacore_obs_api.DeviceTypesApi(metacore_obs_api.ApiClient(configuration))
device_types = metacore_obs_api.DeviceTypes() # DeviceTypes | A device-types or list of device-types documents

try:
    # Stores one or more device_types.
    api_instance.postdevice_types(device_types)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->postdevice_types: %s\n" % e)
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
api_instance = metacore_obs_api.DeviceTypesApi(metacore_obs_api.ApiClient(configuration))
device_types = metacore_obs_api.DeviceTypes() # DeviceTypes | A device-types or list of device-types documents

try:
    # Stores one or more device_types.
    api_instance.postdevice_types(device_types)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->postdevice_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_types** | [**DeviceTypes**](DeviceTypes.md)| A device-types or list of device-types documents | 

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

# **putdevice_types_item**
> putdevice_types_item(device_types_id, if_match, device_types)

Replaces a device-types document

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
api_instance = metacore_obs_api.DeviceTypesApi(metacore_obs_api.ApiClient(configuration))
device_types_id = 'device_types_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
device_types = metacore_obs_api.DeviceTypes() # DeviceTypes | A device-types or list of device-types documents

try:
    # Replaces a device-types document
    api_instance.putdevice_types_item(device_types_id, if_match, device_types)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->putdevice_types_item: %s\n" % e)
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
api_instance = metacore_obs_api.DeviceTypesApi(metacore_obs_api.ApiClient(configuration))
device_types_id = 'device_types_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
device_types = metacore_obs_api.DeviceTypes() # DeviceTypes | A device-types or list of device-types documents

try:
    # Replaces a device-types document
    api_instance.putdevice_types_item(device_types_id, if_match, device_types)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->putdevice_types_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_types_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 
 **device_types** | [**DeviceTypes**](DeviceTypes.md)| A device-types or list of device-types documents | 

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
**200** | device-types document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

