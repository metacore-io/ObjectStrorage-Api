# metacore_obs_api.TenantsApi

All URIs are relative to *https://api.teke.li/api/v1/obs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gettenants**](TenantsApi.md#gettenants) | **GET** /tenants | Retrieves one or more tenants
[**gettenants_item**](TenantsApi.md#gettenants_item) | **GET** /tenants/{tenantsId} | Retrieves a tenants document
[**patchtenants_item**](TenantsApi.md#patchtenants_item) | **PATCH** /tenants/{tenantsId} | Updates a tenants document
[**posttenants**](TenantsApi.md#posttenants) | **POST** /tenants | Stores one or more tenants.
[**puttenants_item**](TenantsApi.md#puttenants_item) | **PUT** /tenants/{tenantsId} | Replaces a tenants document


# **gettenants**
> InlineResponse20014 gettenants(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more tenants

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
api_instance = metacore_obs_api.TenantsApi(metacore_obs_api.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

try:
    # Retrieves one or more tenants
    api_response = api_instance.gettenants(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsApi->gettenants: %s\n" % e)
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
api_instance = metacore_obs_api.TenantsApi(metacore_obs_api.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

try:
    # Retrieves one or more tenants
    api_response = api_instance.gettenants(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsApi->gettenants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of tenants |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gettenants_item**
> Tenants gettenants_item(tenants_id)

Retrieves a tenants document

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
api_instance = metacore_obs_api.TenantsApi(metacore_obs_api.ApiClient(configuration))
tenants_id = 'tenants_id_example' # str | 

try:
    # Retrieves a tenants document
    api_response = api_instance.gettenants_item(tenants_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsApi->gettenants_item: %s\n" % e)
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
api_instance = metacore_obs_api.TenantsApi(metacore_obs_api.ApiClient(configuration))
tenants_id = 'tenants_id_example' # str | 

try:
    # Retrieves a tenants document
    api_response = api_instance.gettenants_item(tenants_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsApi->gettenants_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenants_id** | **str**|  | 

### Return type

[**Tenants**](Tenants.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tenants document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchtenants_item**
> patchtenants_item(tenants_id, if_match, tenants)

Updates a tenants document

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
api_instance = metacore_obs_api.TenantsApi(metacore_obs_api.ApiClient(configuration))
tenants_id = 'tenants_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
tenants = metacore_obs_api.Tenants() # Tenants | A tenants or list of tenants documents

try:
    # Updates a tenants document
    api_instance.patchtenants_item(tenants_id, if_match, tenants)
except ApiException as e:
    print("Exception when calling TenantsApi->patchtenants_item: %s\n" % e)
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
api_instance = metacore_obs_api.TenantsApi(metacore_obs_api.ApiClient(configuration))
tenants_id = 'tenants_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
tenants = metacore_obs_api.Tenants() # Tenants | A tenants or list of tenants documents

try:
    # Updates a tenants document
    api_instance.patchtenants_item(tenants_id, if_match, tenants)
except ApiException as e:
    print("Exception when calling TenantsApi->patchtenants_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenants_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 
 **tenants** | [**Tenants**](Tenants.md)| A tenants or list of tenants documents | 

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
**200** | tenants document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **posttenants**
> posttenants(tenants)

Stores one or more tenants.

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
api_instance = metacore_obs_api.TenantsApi(metacore_obs_api.ApiClient(configuration))
tenants = metacore_obs_api.Tenants() # Tenants | A tenants or list of tenants documents

try:
    # Stores one or more tenants.
    api_instance.posttenants(tenants)
except ApiException as e:
    print("Exception when calling TenantsApi->posttenants: %s\n" % e)
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
api_instance = metacore_obs_api.TenantsApi(metacore_obs_api.ApiClient(configuration))
tenants = metacore_obs_api.Tenants() # Tenants | A tenants or list of tenants documents

try:
    # Stores one or more tenants.
    api_instance.posttenants(tenants)
except ApiException as e:
    print("Exception when calling TenantsApi->posttenants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenants** | [**Tenants**](Tenants.md)| A tenants or list of tenants documents | 

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

# **puttenants_item**
> puttenants_item(tenants_id, if_match, tenants)

Replaces a tenants document

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
api_instance = metacore_obs_api.TenantsApi(metacore_obs_api.ApiClient(configuration))
tenants_id = 'tenants_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
tenants = metacore_obs_api.Tenants() # Tenants | A tenants or list of tenants documents

try:
    # Replaces a tenants document
    api_instance.puttenants_item(tenants_id, if_match, tenants)
except ApiException as e:
    print("Exception when calling TenantsApi->puttenants_item: %s\n" % e)
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
api_instance = metacore_obs_api.TenantsApi(metacore_obs_api.ApiClient(configuration))
tenants_id = 'tenants_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
tenants = metacore_obs_api.Tenants() # Tenants | A tenants or list of tenants documents

try:
    # Replaces a tenants document
    api_instance.puttenants_item(tenants_id, if_match, tenants)
except ApiException as e:
    print("Exception when calling TenantsApi->puttenants_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenants_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 
 **tenants** | [**Tenants**](Tenants.md)| A tenants or list of tenants documents | 

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
**200** | tenants document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

