# coding: utf-8

"""
    Metacore IOT Object Storage API

    Metacore IOT Core Services  # noqa: E501

    The version of the OpenAPI document: 0.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import metacore_obs_api
from metacore_obs_api.api.role_settings_api import RoleSettingsApi  # noqa: E501
from metacore_obs_api.rest import ApiException


class TestRoleSettingsApi(unittest.TestCase):
    """RoleSettingsApi unit test stubs"""

    def setUp(self):
        self.api = metacore_obs_api.api.role_settings_api.RoleSettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_getrole_settings(self):
        """Test case for getrole_settings

        Retrieves one or more role_settings  # noqa: E501
        """
        pass

    def test_getrole_settings_item(self):
        """Test case for getrole_settings_item

        Retrieves a role-settings document  # noqa: E501
        """
        pass

    def test_patchrole_settings_item(self):
        """Test case for patchrole_settings_item

        Updates a role-settings document  # noqa: E501
        """
        pass

    def test_postrole_settings(self):
        """Test case for postrole_settings

        Stores one or more role_settings.  # noqa: E501
        """
        pass

    def test_putrole_settings_item(self):
        """Test case for putrole_settings_item

        Replaces a role-settings document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
