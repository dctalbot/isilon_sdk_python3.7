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


class SyncTargetApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_policies_policy_cancel_item(self, policies_policy_cancel_item, policy, **kwargs):  # noqa: E501
        """create_policies_policy_cancel_item  # noqa: E501

        Cancel the most recent SyncIQ job for this policy from the target side.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_policies_policy_cancel_item(policies_policy_cancel_item, policy, async=True)
        >>> result = thread.get()

        :param async bool
        :param Empty policies_policy_cancel_item: (required)
        :param str policy: (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_policies_policy_cancel_item_with_http_info(policies_policy_cancel_item, policy, **kwargs)  # noqa: E501
        else:
            (data) = self.create_policies_policy_cancel_item_with_http_info(policies_policy_cancel_item, policy, **kwargs)  # noqa: E501
            return data

    def create_policies_policy_cancel_item_with_http_info(self, policies_policy_cancel_item, policy, **kwargs):  # noqa: E501
        """create_policies_policy_cancel_item  # noqa: E501

        Cancel the most recent SyncIQ job for this policy from the target side.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_policies_policy_cancel_item_with_http_info(policies_policy_cancel_item, policy, async=True)
        >>> result = thread.get()

        :param async bool
        :param Empty policies_policy_cancel_item: (required)
        :param str policy: (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policies_policy_cancel_item', 'policy']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_policies_policy_cancel_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policies_policy_cancel_item' is set
        if ('policies_policy_cancel_item' not in params or
                params['policies_policy_cancel_item'] is None):
            raise ValueError("Missing the required parameter `policies_policy_cancel_item` when calling `create_policies_policy_cancel_item`")  # noqa: E501
        # verify the required parameter 'policy' is set
        if ('policy' not in params or
                params['policy'] is None):
            raise ValueError("Missing the required parameter `policy` when calling `create_policies_policy_cancel_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy' in params:
            path_params['Policy'] = params['policy']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'policies_policy_cancel_item' in params:
            body_params = params['policies_policy_cancel_item']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/sync/target/policies/{Policy}/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_reports_report_subreport(self, reports_report_subreport_id, rid, **kwargs):  # noqa: E501
        """get_reports_report_subreport  # noqa: E501

        View a single SyncIQ target subreport.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_reports_report_subreport(reports_report_subreport_id, rid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str reports_report_subreport_id: View a single SyncIQ target subreport. (required)
        :param str rid: (required)
        :return: ReportsReportSubreports
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_reports_report_subreport_with_http_info(reports_report_subreport_id, rid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_reports_report_subreport_with_http_info(reports_report_subreport_id, rid, **kwargs)  # noqa: E501
            return data

    def get_reports_report_subreport_with_http_info(self, reports_report_subreport_id, rid, **kwargs):  # noqa: E501
        """get_reports_report_subreport  # noqa: E501

        View a single SyncIQ target subreport.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_reports_report_subreport_with_http_info(reports_report_subreport_id, rid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str reports_report_subreport_id: View a single SyncIQ target subreport. (required)
        :param str rid: (required)
        :return: ReportsReportSubreports
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['reports_report_subreport_id', 'rid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_reports_report_subreport" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reports_report_subreport_id' is set
        if ('reports_report_subreport_id' not in params or
                params['reports_report_subreport_id'] is None):
            raise ValueError("Missing the required parameter `reports_report_subreport_id` when calling `get_reports_report_subreport`")  # noqa: E501
        # verify the required parameter 'rid' is set
        if ('rid' not in params or
                params['rid'] is None):
            raise ValueError("Missing the required parameter `rid` when calling `get_reports_report_subreport`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'reports_report_subreport_id' in params:
            path_params['ReportsReportSubreportId'] = params['reports_report_subreport_id']  # noqa: E501
        if 'rid' in params:
            path_params['Rid'] = params['rid']  # noqa: E501

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
            '/platform/4/sync/target/reports/{Rid}/subreports/{ReportsReportSubreportId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportsReportSubreports',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_reports_report_subreports(self, rid, **kwargs):  # noqa: E501
        """get_reports_report_subreports  # noqa: E501

        Get a list of SyncIQ target subreports for a report.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_reports_report_subreports(rid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str rid: (required)
        :param str sort: The field that will be used for sorting.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param int newer_than: Filter the returned reports to include only those whose jobs started more recently than the specified number of days ago.
        :param str state: Filter the returned reports to include only those whose jobs are in this state.
        :param int limit: Return no more than this many results at once (see resume).
        :param str dir: The direction of the sort.
        :return: ReportsReportSubreportsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_reports_report_subreports_with_http_info(rid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_reports_report_subreports_with_http_info(rid, **kwargs)  # noqa: E501
            return data

    def get_reports_report_subreports_with_http_info(self, rid, **kwargs):  # noqa: E501
        """get_reports_report_subreports  # noqa: E501

        Get a list of SyncIQ target subreports for a report.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_reports_report_subreports_with_http_info(rid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str rid: (required)
        :param str sort: The field that will be used for sorting.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param int newer_than: Filter the returned reports to include only those whose jobs started more recently than the specified number of days ago.
        :param str state: Filter the returned reports to include only those whose jobs are in this state.
        :param int limit: Return no more than this many results at once (see resume).
        :param str dir: The direction of the sort.
        :return: ReportsReportSubreportsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rid', 'sort', 'resume', 'newer_than', 'state', 'limit', 'dir']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_reports_report_subreports" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rid' is set
        if ('rid' not in params or
                params['rid'] is None):
            raise ValueError("Missing the required parameter `rid` when calling `get_reports_report_subreports`")  # noqa: E501

        if ('sort' in params and
                len(params['sort']) > 255):
            raise ValueError("Invalid value for parameter `sort` when calling `get_reports_report_subreports`, length must be less than or equal to `255`")  # noqa: E501
        if ('sort' in params and
                len(params['sort']) < 0):
            raise ValueError("Invalid value for parameter `sort` when calling `get_reports_report_subreports`, length must be greater than or equal to `0`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `get_reports_report_subreports`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `get_reports_report_subreports`, length must be greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_reports_report_subreports`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_reports_report_subreports`, must be a value greater than or equal to `1`")  # noqa: E501
        if ('dir' in params and
                len(params['dir']) < 0):
            raise ValueError("Invalid value for parameter `dir` when calling `get_reports_report_subreports`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'rid' in params:
            path_params['Rid'] = params['rid']  # noqa: E501

        query_params = []
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501
        if 'newer_than' in params:
            query_params.append(('newer_than', params['newer_than']))  # noqa: E501
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'dir' in params:
            query_params.append(('dir', params['dir']))  # noqa: E501

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
            '/platform/4/sync/target/reports/{Rid}/subreports', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportsReportSubreportsExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
