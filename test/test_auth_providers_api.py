# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 6
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_1_1
from isi_sdk_8_1_1.api.auth_providers_api import AuthProvidersApi  # noqa: E501
from isi_sdk_8_1_1.rest import ApiException


class TestAuthProvidersApi(unittest.TestCase):
    """AuthProvidersApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_1_1.api.auth_providers_api.AuthProvidersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_ads_provider_controllers(self):
        """Test case for get_ads_provider_controllers

        """
        pass

    def test_get_ads_provider_domain(self):
        """Test case for get_ads_provider_domain

        """
        pass

    def test_get_ads_provider_domains(self):
        """Test case for get_ads_provider_domains

        """
        pass

    def test_get_ads_provider_search(self):
        """Test case for get_ads_provider_search

        """
        pass


if __name__ == '__main__':
    unittest.main()
