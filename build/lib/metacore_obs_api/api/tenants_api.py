# coding: utf-8

"""
    Metacore IOT Object Storage API

    Metacore IOT Core Services  # noqa: E501

    The version of the OpenAPI document: 0.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from metacore_obs_api.api_client import ApiClient
from metacore_obs_api.exceptions import (
    ApiTypeError,
    ApiValueError
)


class TenantsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def gettenants(self, **kwargs):  # noqa: E501
        """Retrieves one or more tenants  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gettenants(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.gettenants_with_http_info(**kwargs)  # noqa: E501

    def gettenants_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves one or more tenants  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gettenants_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse20014, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['where', 'sort', 'page', 'max_results']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method gettenants" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'where' in local_var_params:
            query_params.append(('where', local_var_params['where']))  # noqa: E501
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'max_results' in local_var_params:
            query_params.append(('max_results', local_var_params['max_results']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth', 'ApiKeyQueryAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tenants', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20014',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def gettenants_item(self, tenants_id, **kwargs):  # noqa: E501
        """Retrieves a tenants document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gettenants_item(tenants_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tenants_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Tenants
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.gettenants_item_with_http_info(tenants_id, **kwargs)  # noqa: E501

    def gettenants_item_with_http_info(self, tenants_id, **kwargs):  # noqa: E501
        """Retrieves a tenants document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gettenants_item_with_http_info(tenants_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tenants_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Tenants, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['tenants_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method gettenants_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tenants_id' is set
        if ('tenants_id' not in local_var_params or
                local_var_params['tenants_id'] is None):
            raise ApiValueError("Missing the required parameter `tenants_id` when calling `gettenants_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenants_id' in local_var_params:
            path_params['tenantsId'] = local_var_params['tenants_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth', 'ApiKeyQueryAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tenants/{tenantsId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tenants',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patchtenants_item(self, tenants_id, if_match, tenants, **kwargs):  # noqa: E501
        """Updates a tenants document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patchtenants_item(tenants_id, if_match, tenants, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tenants_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :param Tenants tenants: A tenants or list of tenants documents (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.patchtenants_item_with_http_info(tenants_id, if_match, tenants, **kwargs)  # noqa: E501

    def patchtenants_item_with_http_info(self, tenants_id, if_match, tenants, **kwargs):  # noqa: E501
        """Updates a tenants document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patchtenants_item_with_http_info(tenants_id, if_match, tenants, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tenants_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :param Tenants tenants: A tenants or list of tenants documents (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['tenants_id', 'if_match', 'tenants']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patchtenants_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tenants_id' is set
        if ('tenants_id' not in local_var_params or
                local_var_params['tenants_id'] is None):
            raise ApiValueError("Missing the required parameter `tenants_id` when calling `patchtenants_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in local_var_params or
                local_var_params['if_match'] is None):
            raise ApiValueError("Missing the required parameter `if_match` when calling `patchtenants_item`")  # noqa: E501
        # verify the required parameter 'tenants' is set
        if ('tenants' not in local_var_params or
                local_var_params['tenants'] is None):
            raise ApiValueError("Missing the required parameter `tenants` when calling `patchtenants_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenants_id' in local_var_params:
            path_params['tenantsId'] = local_var_params['tenants_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in local_var_params:
            header_params['If-Match'] = local_var_params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tenants' in local_var_params:
            body_params = local_var_params['tenants']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth', 'ApiKeyQueryAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tenants/{tenantsId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def posttenants(self, tenants, **kwargs):  # noqa: E501
        """Stores one or more tenants.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.posttenants(tenants, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Tenants tenants: A tenants or list of tenants documents (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.posttenants_with_http_info(tenants, **kwargs)  # noqa: E501

    def posttenants_with_http_info(self, tenants, **kwargs):  # noqa: E501
        """Stores one or more tenants.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.posttenants_with_http_info(tenants, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Tenants tenants: A tenants or list of tenants documents (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['tenants']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method posttenants" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tenants' is set
        if ('tenants' not in local_var_params or
                local_var_params['tenants'] is None):
            raise ApiValueError("Missing the required parameter `tenants` when calling `posttenants`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tenants' in local_var_params:
            body_params = local_var_params['tenants']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth', 'ApiKeyQueryAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tenants', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def puttenants_item(self, tenants_id, if_match, tenants, **kwargs):  # noqa: E501
        """Replaces a tenants document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.puttenants_item(tenants_id, if_match, tenants, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tenants_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :param Tenants tenants: A tenants or list of tenants documents (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.puttenants_item_with_http_info(tenants_id, if_match, tenants, **kwargs)  # noqa: E501

    def puttenants_item_with_http_info(self, tenants_id, if_match, tenants, **kwargs):  # noqa: E501
        """Replaces a tenants document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.puttenants_item_with_http_info(tenants_id, if_match, tenants, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tenants_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :param Tenants tenants: A tenants or list of tenants documents (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['tenants_id', 'if_match', 'tenants']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method puttenants_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tenants_id' is set
        if ('tenants_id' not in local_var_params or
                local_var_params['tenants_id'] is None):
            raise ApiValueError("Missing the required parameter `tenants_id` when calling `puttenants_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in local_var_params or
                local_var_params['if_match'] is None):
            raise ApiValueError("Missing the required parameter `if_match` when calling `puttenants_item`")  # noqa: E501
        # verify the required parameter 'tenants' is set
        if ('tenants' not in local_var_params or
                local_var_params['tenants'] is None):
            raise ApiValueError("Missing the required parameter `tenants` when calling `puttenants_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenants_id' in local_var_params:
            path_params['tenantsId'] = local_var_params['tenants_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in local_var_params:
            header_params['If-Match'] = local_var_params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tenants' in local_var_params:
            body_params = local_var_params['tenants']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth', 'ApiKeyQueryAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tenants/{tenantsId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
