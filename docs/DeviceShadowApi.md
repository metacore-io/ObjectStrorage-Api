# metacore_obs_api.DeviceShadowApi

All URIs are relative to *https://api.teke.li/api/v1/obs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getdevice_shadow**](DeviceShadowApi.md#getdevice_shadow) | **GET** /device_shadow | Retrieves one or more device_shadow
[**getdevice_shadow_item**](DeviceShadowApi.md#getdevice_shadow_item) | **GET** /device_shadow/{device-shadowId} | Retrieves a device-shadow document
[**patchdevice_shadow_item**](DeviceShadowApi.md#patchdevice_shadow_item) | **PATCH** /device_shadow/{device-shadowId} | Updates a device-shadow document
[**postdevice_shadow**](DeviceShadowApi.md#postdevice_shadow) | **POST** /device_shadow | Stores one or more device_shadow.
[**putdevice_shadow_item**](DeviceShadowApi.md#putdevice_shadow_item) | **PUT** /device_shadow/{device-shadowId} | Replaces a device-shadow document


# **getdevice_shadow**
> InlineResponse2001 getdevice_shadow(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more device_shadow

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
api_instance = metacore_obs_api.DeviceShadowApi(metacore_obs_api.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

try:
    # Retrieves one or more device_shadow
    api_response = api_instance.getdevice_shadow(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceShadowApi->getdevice_shadow: %s\n" % e)
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
api_instance = metacore_obs_api.DeviceShadowApi(metacore_obs_api.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

try:
    # Retrieves one or more device_shadow
    api_response = api_instance.getdevice_shadow(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceShadowApi->getdevice_shadow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of device_shadow |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getdevice_shadow_item**
> DeviceShadow getdevice_shadow_item(device_shadow_id)

Retrieves a device-shadow document

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
api_instance = metacore_obs_api.DeviceShadowApi(metacore_obs_api.ApiClient(configuration))
device_shadow_id = 'device_shadow_id_example' # str | 

try:
    # Retrieves a device-shadow document
    api_response = api_instance.getdevice_shadow_item(device_shadow_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceShadowApi->getdevice_shadow_item: %s\n" % e)
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
api_instance = metacore_obs_api.DeviceShadowApi(metacore_obs_api.ApiClient(configuration))
device_shadow_id = 'device_shadow_id_example' # str | 

try:
    # Retrieves a device-shadow document
    api_response = api_instance.getdevice_shadow_item(device_shadow_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceShadowApi->getdevice_shadow_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_shadow_id** | **str**|  | 

### Return type

[**DeviceShadow**](DeviceShadow.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | device-shadow document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchdevice_shadow_item**
> patchdevice_shadow_item(device_shadow_id, if_match, device_shadow)

Updates a device-shadow document

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
api_instance = metacore_obs_api.DeviceShadowApi(metacore_obs_api.ApiClient(configuration))
device_shadow_id = 'device_shadow_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
device_shadow = metacore_obs_api.DeviceShadow() # DeviceShadow | A device-shadow or list of device-shadow documents

try:
    # Updates a device-shadow document
    api_instance.patchdevice_shadow_item(device_shadow_id, if_match, device_shadow)
except ApiException as e:
    print("Exception when calling DeviceShadowApi->patchdevice_shadow_item: %s\n" % e)
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
api_instance = metacore_obs_api.DeviceShadowApi(metacore_obs_api.ApiClient(configuration))
device_shadow_id = 'device_shadow_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
device_shadow = metacore_obs_api.DeviceShadow() # DeviceShadow | A device-shadow or list of device-shadow documents

try:
    # Updates a device-shadow document
    api_instance.patchdevice_shadow_item(device_shadow_id, if_match, device_shadow)
except ApiException as e:
    print("Exception when calling DeviceShadowApi->patchdevice_shadow_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_shadow_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 
 **device_shadow** | [**DeviceShadow**](DeviceShadow.md)| A device-shadow or list of device-shadow documents | 

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
**200** | device-shadow document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postdevice_shadow**
> postdevice_shadow(device_shadow)

Stores one or more device_shadow.

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
api_instance = metacore_obs_api.DeviceShadowApi(metacore_obs_api.ApiClient(configuration))
device_shadow = metacore_obs_api.DeviceShadow() # DeviceShadow | A device-shadow or list of device-shadow documents

try:
    # Stores one or more device_shadow.
    api_instance.postdevice_shadow(device_shadow)
except ApiException as e:
    print("Exception when calling DeviceShadowApi->postdevice_shadow: %s\n" % e)
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
api_instance = metacore_obs_api.DeviceShadowApi(metacore_obs_api.ApiClient(configuration))
device_shadow = metacore_obs_api.DeviceShadow() # DeviceShadow | A device-shadow or list of device-shadow documents

try:
    # Stores one or more device_shadow.
    api_instance.postdevice_shadow(device_shadow)
except ApiException as e:
    print("Exception when calling DeviceShadowApi->postdevice_shadow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_shadow** | [**DeviceShadow**](DeviceShadow.md)| A device-shadow or list of device-shadow documents | 

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

# **putdevice_shadow_item**
> putdevice_shadow_item(device_shadow_id, if_match, device_shadow)

Replaces a device-shadow document

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
api_instance = metacore_obs_api.DeviceShadowApi(metacore_obs_api.ApiClient(configuration))
device_shadow_id = 'device_shadow_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
device_shadow = metacore_obs_api.DeviceShadow() # DeviceShadow | A device-shadow or list of device-shadow documents

try:
    # Replaces a device-shadow document
    api_instance.putdevice_shadow_item(device_shadow_id, if_match, device_shadow)
except ApiException as e:
    print("Exception when calling DeviceShadowApi->putdevice_shadow_item: %s\n" % e)
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
api_instance = metacore_obs_api.DeviceShadowApi(metacore_obs_api.ApiClient(configuration))
device_shadow_id = 'device_shadow_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
device_shadow = metacore_obs_api.DeviceShadow() # DeviceShadow | A device-shadow or list of device-shadow documents

try:
    # Replaces a device-shadow document
    api_instance.putdevice_shadow_item(device_shadow_id, if_match, device_shadow)
except ApiException as e:
    print("Exception when calling DeviceShadowApi->putdevice_shadow_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_shadow_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 
 **device_shadow** | [**DeviceShadow**](DeviceShadow.md)| A device-shadow or list of device-shadow documents | 

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
**200** | device-shadow document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

