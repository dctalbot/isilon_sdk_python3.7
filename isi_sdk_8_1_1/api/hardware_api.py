# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 6
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isi_sdk_8_1_1.api_client import ApiClient


class HardwareApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_hardware_tape_name(self, hardware_tape_name, hardware_tape_name2, **kwargs):  # noqa: E501
        """create_hardware_tape_name  # noqa: E501

        Tape/Changer devices rescan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_hardware_tape_name(hardware_tape_name, hardware_tape_name2, async=True)
        >>> result = thread.get()

        :param async bool
        :param Empty hardware_tape_name: (required)
        :param str hardware_tape_name2: Tape/Changer devices rescan (required)
        :param str lnn: Logical node number.
        :param int port: Scan only specified port.
        :param float timeout: Timeout for request.
        :param bool reconcile: Remove entries for devices or paths that have become inaccessible.
        :return: CreateHardwareTapeNameResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_hardware_tape_name_with_http_info(hardware_tape_name, hardware_tape_name2, **kwargs)  # noqa: E501
        else:
            (data) = self.create_hardware_tape_name_with_http_info(hardware_tape_name, hardware_tape_name2, **kwargs)  # noqa: E501
            return data

    def create_hardware_tape_name_with_http_info(self, hardware_tape_name, hardware_tape_name2, **kwargs):  # noqa: E501
        """create_hardware_tape_name  # noqa: E501

        Tape/Changer devices rescan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_hardware_tape_name_with_http_info(hardware_tape_name, hardware_tape_name2, async=True)
        >>> result = thread.get()

        :param async bool
        :param Empty hardware_tape_name: (required)
        :param str hardware_tape_name2: Tape/Changer devices rescan (required)
        :param str lnn: Logical node number.
        :param int port: Scan only specified port.
        :param float timeout: Timeout for request.
        :param bool reconcile: Remove entries for devices or paths that have become inaccessible.
        :return: CreateHardwareTapeNameResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardware_tape_name', 'hardware_tape_name2', 'lnn', 'port', 'timeout', 'reconcile']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_hardware_tape_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hardware_tape_name' is set
        if ('hardware_tape_name' not in params or
                params['hardware_tape_name'] is None):
            raise ValueError("Missing the required parameter `hardware_tape_name` when calling `create_hardware_tape_name`")  # noqa: E501
        # verify the required parameter 'hardware_tape_name2' is set
        if ('hardware_tape_name2' not in params or
                params['hardware_tape_name2'] is None):
            raise ValueError("Missing the required parameter `hardware_tape_name2` when calling `create_hardware_tape_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'hardware_tape_name2' in params:
            path_params['HardwareTapeName'] = params['hardware_tape_name2']  # noqa: E501

        query_params = []
        if 'lnn' in params:
            query_params.append(('lnn', params['lnn']))  # noqa: E501
        if 'port' in params:
            query_params.append(('port', params['port']))  # noqa: E501
        if 'timeout' in params:
            query_params.append(('timeout', params['timeout']))  # noqa: E501
        if 'reconcile' in params:
            query_params.append(('reconcile', params['reconcile']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'hardware_tape_name' in params:
            body_params = params['hardware_tape_name']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/hardware/tape/{HardwareTapeName}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateHardwareTapeNameResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_hardware_tape_name(self, hardware_tape_name, **kwargs):  # noqa: E501
        """delete_hardware_tape_name  # noqa: E501

        Tape/Changer devices remove  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_hardware_tape_name(hardware_tape_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str hardware_tape_name: Tape/Changer devices remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_hardware_tape_name_with_http_info(hardware_tape_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_hardware_tape_name_with_http_info(hardware_tape_name, **kwargs)  # noqa: E501
            return data

    def delete_hardware_tape_name_with_http_info(self, hardware_tape_name, **kwargs):  # noqa: E501
        """delete_hardware_tape_name  # noqa: E501

        Tape/Changer devices remove  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_hardware_tape_name_with_http_info(hardware_tape_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str hardware_tape_name: Tape/Changer devices remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardware_tape_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_hardware_tape_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hardware_tape_name' is set
        if ('hardware_tape_name' not in params or
                params['hardware_tape_name'] is None):
            raise ValueError("Missing the required parameter `hardware_tape_name` when calling `delete_hardware_tape_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'hardware_tape_name' in params:
            path_params['HardwareTapeName'] = params['hardware_tape_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/hardware/tape/{HardwareTapeName}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_hardware_fcport(self, hardware_fcport_id, **kwargs):  # noqa: E501
        """get_hardware_fcport  # noqa: E501

        Get one fibre-channel port  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_hardware_fcport(hardware_fcport_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int hardware_fcport_id: Get one fibre-channel port (required)
        :param str lnn: Logical node number.
        :return: HardwareFcports
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_hardware_fcport_with_http_info(hardware_fcport_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_hardware_fcport_with_http_info(hardware_fcport_id, **kwargs)  # noqa: E501
            return data

    def get_hardware_fcport_with_http_info(self, hardware_fcport_id, **kwargs):  # noqa: E501
        """get_hardware_fcport  # noqa: E501

        Get one fibre-channel port  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_hardware_fcport_with_http_info(hardware_fcport_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int hardware_fcport_id: Get one fibre-channel port (required)
        :param str lnn: Logical node number.
        :return: HardwareFcports
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardware_fcport_id', 'lnn']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hardware_fcport" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hardware_fcport_id' is set
        if ('hardware_fcport_id' not in params or
                params['hardware_fcport_id'] is None):
            raise ValueError("Missing the required parameter `hardware_fcport_id` when calling `get_hardware_fcport`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'hardware_fcport_id' in params:
            path_params['HardwareFcportId'] = params['hardware_fcport_id']  # noqa: E501

        query_params = []
        if 'lnn' in params:
            query_params.append(('lnn', params['lnn']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/hardware/fcports/{HardwareFcportId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HardwareFcports',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_hardware_fcports(self, **kwargs):  # noqa: E501
        """get_hardware_fcports  # noqa: E501

        Get list of fibre-channel ports  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_hardware_fcports(async=True)
        >>> result = thread.get()

        :param async bool
        :param str lnn: Logical node number.
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: HardwareFcports
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_hardware_fcports_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_hardware_fcports_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_hardware_fcports_with_http_info(self, **kwargs):  # noqa: E501
        """get_hardware_fcports  # noqa: E501

        Get list of fibre-channel ports  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_hardware_fcports_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str lnn: Logical node number.
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: HardwareFcports
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lnn', 'limit', 'resume']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hardware_fcports" % key
                )
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_hardware_fcports`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_hardware_fcports`, must be a value greater than or equal to `1`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `get_hardware_fcports`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `get_hardware_fcports`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'lnn' in params:
            query_params.append(('lnn', params['lnn']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/hardware/fcports', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HardwareFcports',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_hardware_tapes(self, **kwargs):  # noqa: E501
        """get_hardware_tapes  # noqa: E501

        Get list Tape and Changer devices  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_hardware_tapes(async=True)
        >>> result = thread.get()

        :param async bool
        :param str node: List only devices on the specified node.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str devname: List only the named device.
        :param int limit: Return no more than this many results at once (see resume).
        :param str activepath: List devices with only active paths.
        :param str type: Restrict to list on tape or mc device.
        :return: HardwareTapes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_hardware_tapes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_hardware_tapes_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_hardware_tapes_with_http_info(self, **kwargs):  # noqa: E501
        """get_hardware_tapes  # noqa: E501

        Get list Tape and Changer devices  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_hardware_tapes_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str node: List only devices on the specified node.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str devname: List only the named device.
        :param int limit: Return no more than this many results at once (see resume).
        :param str activepath: List devices with only active paths.
        :param str type: Restrict to list on tape or mc device.
        :return: HardwareTapes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['node', 'resume', 'devname', 'limit', 'activepath', 'type']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hardware_tapes" % key
                )
            params[key] = val
        del params['kwargs']

        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `get_hardware_tapes`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `get_hardware_tapes`, length must be greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_hardware_tapes`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_hardware_tapes`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'node' in params:
            query_params.append(('node', params['node']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501
        if 'devname' in params:
            query_params.append(('devname', params['devname']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'activepath' in params:
            query_params.append(('activepath', params['activepath']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/hardware/tapes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HardwareTapes',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_hardware_fcport(self, hardware_fcport, hardware_fcport_id, **kwargs):  # noqa: E501
        """update_hardware_fcport  # noqa: E501

        Change wwnn, wwpn, state, topology, or rate of a FC port  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_hardware_fcport(hardware_fcport, hardware_fcport_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param HardwareFcport hardware_fcport: (required)
        :param int hardware_fcport_id: Change wwnn, wwpn, state, topology, or rate of a FC port (required)
        :param str lnn: Logical node number.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_hardware_fcport_with_http_info(hardware_fcport, hardware_fcport_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_hardware_fcport_with_http_info(hardware_fcport, hardware_fcport_id, **kwargs)  # noqa: E501
            return data

    def update_hardware_fcport_with_http_info(self, hardware_fcport, hardware_fcport_id, **kwargs):  # noqa: E501
        """update_hardware_fcport  # noqa: E501

        Change wwnn, wwpn, state, topology, or rate of a FC port  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_hardware_fcport_with_http_info(hardware_fcport, hardware_fcport_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param HardwareFcport hardware_fcport: (required)
        :param int hardware_fcport_id: Change wwnn, wwpn, state, topology, or rate of a FC port (required)
        :param str lnn: Logical node number.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardware_fcport', 'hardware_fcport_id', 'lnn']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_hardware_fcport" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hardware_fcport' is set
        if ('hardware_fcport' not in params or
                params['hardware_fcport'] is None):
            raise ValueError("Missing the required parameter `hardware_fcport` when calling `update_hardware_fcport`")  # noqa: E501
        # verify the required parameter 'hardware_fcport_id' is set
        if ('hardware_fcport_id' not in params or
                params['hardware_fcport_id'] is None):
            raise ValueError("Missing the required parameter `hardware_fcport_id` when calling `update_hardware_fcport`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'hardware_fcport_id' in params:
            path_params['HardwareFcportId'] = params['hardware_fcport_id']  # noqa: E501

        query_params = []
        if 'lnn' in params:
            query_params.append(('lnn', params['lnn']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'hardware_fcport' in params:
            body_params = params['hardware_fcport']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/hardware/fcports/{HardwareFcportId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_hardware_tape_name(self, hardware_tape_name_params, hardware_tape_name, **kwargs):  # noqa: E501
        """update_hardware_tape_name  # noqa: E501

        Tape/Changer device modify  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_hardware_tape_name(hardware_tape_name_params, hardware_tape_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param HardwareTapeNameParams hardware_tape_name_params: (required)
        :param str hardware_tape_name: Tape/Changer device modify (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_hardware_tape_name_with_http_info(hardware_tape_name_params, hardware_tape_name, **kwargs)  # noqa: E501
        else:
            (data) = self.update_hardware_tape_name_with_http_info(hardware_tape_name_params, hardware_tape_name, **kwargs)  # noqa: E501
            return data

    def update_hardware_tape_name_with_http_info(self, hardware_tape_name_params, hardware_tape_name, **kwargs):  # noqa: E501
        """update_hardware_tape_name  # noqa: E501

        Tape/Changer device modify  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_hardware_tape_name_with_http_info(hardware_tape_name_params, hardware_tape_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param HardwareTapeNameParams hardware_tape_name_params: (required)
        :param str hardware_tape_name: Tape/Changer device modify (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardware_tape_name_params', 'hardware_tape_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_hardware_tape_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hardware_tape_name_params' is set
        if ('hardware_tape_name_params' not in params or
                params['hardware_tape_name_params'] is None):
            raise ValueError("Missing the required parameter `hardware_tape_name_params` when calling `update_hardware_tape_name`")  # noqa: E501
        # verify the required parameter 'hardware_tape_name' is set
        if ('hardware_tape_name' not in params or
                params['hardware_tape_name'] is None):
            raise ValueError("Missing the required parameter `hardware_tape_name` when calling `update_hardware_tape_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'hardware_tape_name' in params:
            path_params['HardwareTapeName'] = params['hardware_tape_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'hardware_tape_name_params' in params:
            body_params = params['hardware_tape_name_params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/hardware/tape/{HardwareTapeName}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
