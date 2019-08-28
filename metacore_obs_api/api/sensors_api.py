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


class SensorsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def getsensors(self, **kwargs):  # noqa: E501
        """Retrieves one or more sensors  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getsensors(async_req=True)
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
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.getsensors_with_http_info(**kwargs)  # noqa: E501

    def getsensors_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves one or more sensors  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getsensors_with_http_info(async_req=True)
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
        :return: tuple(InlineResponse20012, status_code(int), headers(HTTPHeaderDict))
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
                    " to method getsensors" % key
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
            '/sensors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getsensors_item(self, sensors_id, **kwargs):  # noqa: E501
        """Retrieves a sensors document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getsensors_item(sensors_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str sensors_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Sensors
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.getsensors_item_with_http_info(sensors_id, **kwargs)  # noqa: E501

    def getsensors_item_with_http_info(self, sensors_id, **kwargs):  # noqa: E501
        """Retrieves a sensors document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getsensors_item_with_http_info(sensors_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str sensors_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Sensors, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['sensors_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getsensors_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'sensors_id' is set
        if ('sensors_id' not in local_var_params or
                local_var_params['sensors_id'] is None):
            raise ApiValueError("Missing the required parameter `sensors_id` when calling `getsensors_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sensors_id' in local_var_params:
            path_params['sensorsId'] = local_var_params['sensors_id']  # noqa: E501

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
            '/sensors/{sensorsId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Sensors',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patchsensors_item(self, sensors_id, if_match, sensors, **kwargs):  # noqa: E501
        """Updates a sensors document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patchsensors_item(sensors_id, if_match, sensors, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str sensors_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :param Sensors sensors: A sensors or list of sensors documents (required)
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
        return self.patchsensors_item_with_http_info(sensors_id, if_match, sensors, **kwargs)  # noqa: E501

    def patchsensors_item_with_http_info(self, sensors_id, if_match, sensors, **kwargs):  # noqa: E501
        """Updates a sensors document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patchsensors_item_with_http_info(sensors_id, if_match, sensors, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str sensors_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :param Sensors sensors: A sensors or list of sensors documents (required)
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

        all_params = ['sensors_id', 'if_match', 'sensors']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patchsensors_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'sensors_id' is set
        if ('sensors_id' not in local_var_params or
                local_var_params['sensors_id'] is None):
            raise ApiValueError("Missing the required parameter `sensors_id` when calling `patchsensors_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in local_var_params or
                local_var_params['if_match'] is None):
            raise ApiValueError("Missing the required parameter `if_match` when calling `patchsensors_item`")  # noqa: E501
        # verify the required parameter 'sensors' is set
        if ('sensors' not in local_var_params or
                local_var_params['sensors'] is None):
            raise ApiValueError("Missing the required parameter `sensors` when calling `patchsensors_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sensors_id' in local_var_params:
            path_params['sensorsId'] = local_var_params['sensors_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in local_var_params:
            header_params['If-Match'] = local_var_params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sensors' in local_var_params:
            body_params = local_var_params['sensors']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth', 'ApiKeyQueryAuth']  # noqa: E501

        return self.api_client.call_api(
            '/sensors/{sensorsId}', 'PATCH',
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

    def postsensors(self, sensors, **kwargs):  # noqa: E501
        """Stores one or more sensors.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postsensors(sensors, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Sensors sensors: A sensors or list of sensors documents (required)
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
        return self.postsensors_with_http_info(sensors, **kwargs)  # noqa: E501

    def postsensors_with_http_info(self, sensors, **kwargs):  # noqa: E501
        """Stores one or more sensors.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postsensors_with_http_info(sensors, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Sensors sensors: A sensors or list of sensors documents (required)
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

        all_params = ['sensors']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method postsensors" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'sensors' is set
        if ('sensors' not in local_var_params or
                local_var_params['sensors'] is None):
            raise ApiValueError("Missing the required parameter `sensors` when calling `postsensors`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sensors' in local_var_params:
            body_params = local_var_params['sensors']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth', 'ApiKeyQueryAuth']  # noqa: E501

        return self.api_client.call_api(
            '/sensors', 'POST',
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

    def putsensors_item(self, sensors_id, if_match, sensors, **kwargs):  # noqa: E501
        """Replaces a sensors document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putsensors_item(sensors_id, if_match, sensors, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str sensors_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :param Sensors sensors: A sensors or list of sensors documents (required)
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
        return self.putsensors_item_with_http_info(sensors_id, if_match, sensors, **kwargs)  # noqa: E501

    def putsensors_item_with_http_info(self, sensors_id, if_match, sensors, **kwargs):  # noqa: E501
        """Replaces a sensors document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putsensors_item_with_http_info(sensors_id, if_match, sensors, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str sensors_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :param Sensors sensors: A sensors or list of sensors documents (required)
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

        all_params = ['sensors_id', 'if_match', 'sensors']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method putsensors_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'sensors_id' is set
        if ('sensors_id' not in local_var_params or
                local_var_params['sensors_id'] is None):
            raise ApiValueError("Missing the required parameter `sensors_id` when calling `putsensors_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in local_var_params or
                local_var_params['if_match'] is None):
            raise ApiValueError("Missing the required parameter `if_match` when calling `putsensors_item`")  # noqa: E501
        # verify the required parameter 'sensors' is set
        if ('sensors' not in local_var_params or
                local_var_params['sensors'] is None):
            raise ApiValueError("Missing the required parameter `sensors` when calling `putsensors_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sensors_id' in local_var_params:
            path_params['sensorsId'] = local_var_params['sensors_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in local_var_params:
            header_params['If-Match'] = local_var_params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sensors' in local_var_params:
            body_params = local_var_params['sensors']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth', 'ApiKeyQueryAuth']  # noqa: E501

        return self.api_client.call_api(
            '/sensors/{sensorsId}', 'PUT',
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
