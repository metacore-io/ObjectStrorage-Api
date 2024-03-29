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


class GraphSettingsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def getgraph_settings(self, **kwargs):  # noqa: E501
        """Retrieves one or more graph_settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getgraph_settings(async_req=True)
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
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.getgraph_settings_with_http_info(**kwargs)  # noqa: E501

    def getgraph_settings_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves one or more graph_settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getgraph_settings_with_http_info(async_req=True)
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
        :return: tuple(InlineResponse2004, status_code(int), headers(HTTPHeaderDict))
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
                    " to method getgraph_settings" % key
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
            '/graph_settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getgraph_settings_item(self, graph_settings_id, **kwargs):  # noqa: E501
        """Retrieves a graph-settings document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getgraph_settings_item(graph_settings_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str graph_settings_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GraphSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.getgraph_settings_item_with_http_info(graph_settings_id, **kwargs)  # noqa: E501

    def getgraph_settings_item_with_http_info(self, graph_settings_id, **kwargs):  # noqa: E501
        """Retrieves a graph-settings document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getgraph_settings_item_with_http_info(graph_settings_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str graph_settings_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GraphSettings, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['graph_settings_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getgraph_settings_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'graph_settings_id' is set
        if ('graph_settings_id' not in local_var_params or
                local_var_params['graph_settings_id'] is None):
            raise ApiValueError("Missing the required parameter `graph_settings_id` when calling `getgraph_settings_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'graph_settings_id' in local_var_params:
            path_params['graph-settingsId'] = local_var_params['graph_settings_id']  # noqa: E501

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
            '/graph_settings/{graph-settingsId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GraphSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patchgraph_settings_item(self, graph_settings_id, if_match, graph_settings, **kwargs):  # noqa: E501
        """Updates a graph-settings document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patchgraph_settings_item(graph_settings_id, if_match, graph_settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str graph_settings_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :param GraphSettings graph_settings: A graph-settings or list of graph-settings documents (required)
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
        return self.patchgraph_settings_item_with_http_info(graph_settings_id, if_match, graph_settings, **kwargs)  # noqa: E501

    def patchgraph_settings_item_with_http_info(self, graph_settings_id, if_match, graph_settings, **kwargs):  # noqa: E501
        """Updates a graph-settings document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patchgraph_settings_item_with_http_info(graph_settings_id, if_match, graph_settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str graph_settings_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :param GraphSettings graph_settings: A graph-settings or list of graph-settings documents (required)
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

        all_params = ['graph_settings_id', 'if_match', 'graph_settings']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patchgraph_settings_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'graph_settings_id' is set
        if ('graph_settings_id' not in local_var_params or
                local_var_params['graph_settings_id'] is None):
            raise ApiValueError("Missing the required parameter `graph_settings_id` when calling `patchgraph_settings_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in local_var_params or
                local_var_params['if_match'] is None):
            raise ApiValueError("Missing the required parameter `if_match` when calling `patchgraph_settings_item`")  # noqa: E501
        # verify the required parameter 'graph_settings' is set
        if ('graph_settings' not in local_var_params or
                local_var_params['graph_settings'] is None):
            raise ApiValueError("Missing the required parameter `graph_settings` when calling `patchgraph_settings_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'graph_settings_id' in local_var_params:
            path_params['graph-settingsId'] = local_var_params['graph_settings_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in local_var_params:
            header_params['If-Match'] = local_var_params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'graph_settings' in local_var_params:
            body_params = local_var_params['graph_settings']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth', 'ApiKeyQueryAuth']  # noqa: E501

        return self.api_client.call_api(
            '/graph_settings/{graph-settingsId}', 'PATCH',
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

    def postgraph_settings(self, graph_settings, **kwargs):  # noqa: E501
        """Stores one or more graph_settings.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postgraph_settings(graph_settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param GraphSettings graph_settings: A graph-settings or list of graph-settings documents (required)
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
        return self.postgraph_settings_with_http_info(graph_settings, **kwargs)  # noqa: E501

    def postgraph_settings_with_http_info(self, graph_settings, **kwargs):  # noqa: E501
        """Stores one or more graph_settings.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postgraph_settings_with_http_info(graph_settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param GraphSettings graph_settings: A graph-settings or list of graph-settings documents (required)
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

        all_params = ['graph_settings']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method postgraph_settings" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'graph_settings' is set
        if ('graph_settings' not in local_var_params or
                local_var_params['graph_settings'] is None):
            raise ApiValueError("Missing the required parameter `graph_settings` when calling `postgraph_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'graph_settings' in local_var_params:
            body_params = local_var_params['graph_settings']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth', 'ApiKeyQueryAuth']  # noqa: E501

        return self.api_client.call_api(
            '/graph_settings', 'POST',
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

    def putgraph_settings_item(self, graph_settings_id, if_match, graph_settings, **kwargs):  # noqa: E501
        """Replaces a graph-settings document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putgraph_settings_item(graph_settings_id, if_match, graph_settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str graph_settings_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :param GraphSettings graph_settings: A graph-settings or list of graph-settings documents (required)
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
        return self.putgraph_settings_item_with_http_info(graph_settings_id, if_match, graph_settings, **kwargs)  # noqa: E501

    def putgraph_settings_item_with_http_info(self, graph_settings_id, if_match, graph_settings, **kwargs):  # noqa: E501
        """Replaces a graph-settings document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putgraph_settings_item_with_http_info(graph_settings_id, if_match, graph_settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str graph_settings_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :param GraphSettings graph_settings: A graph-settings or list of graph-settings documents (required)
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

        all_params = ['graph_settings_id', 'if_match', 'graph_settings']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method putgraph_settings_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'graph_settings_id' is set
        if ('graph_settings_id' not in local_var_params or
                local_var_params['graph_settings_id'] is None):
            raise ApiValueError("Missing the required parameter `graph_settings_id` when calling `putgraph_settings_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in local_var_params or
                local_var_params['if_match'] is None):
            raise ApiValueError("Missing the required parameter `if_match` when calling `putgraph_settings_item`")  # noqa: E501
        # verify the required parameter 'graph_settings' is set
        if ('graph_settings' not in local_var_params or
                local_var_params['graph_settings'] is None):
            raise ApiValueError("Missing the required parameter `graph_settings` when calling `putgraph_settings_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'graph_settings_id' in local_var_params:
            path_params['graph-settingsId'] = local_var_params['graph_settings_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in local_var_params:
            header_params['If-Match'] = local_var_params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'graph_settings' in local_var_params:
            body_params = local_var_params['graph_settings']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth', 'ApiKeyQueryAuth']  # noqa: E501

        return self.api_client.call_api(
            '/graph_settings/{graph-settingsId}', 'PUT',
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
