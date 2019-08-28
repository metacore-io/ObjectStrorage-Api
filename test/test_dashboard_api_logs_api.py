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
from metacore_obs_api.api.dashboard_api_logs_api import DashboardApiLogsApi  # noqa: E501
from metacore_obs_api.rest import ApiException


class TestDashboardApiLogsApi(unittest.TestCase):
    """DashboardApiLogsApi unit test stubs"""

    def setUp(self):
        self.api = metacore_obs_api.api.dashboard_api_logs_api.DashboardApiLogsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_getdashboard_api_logs(self):
        """Test case for getdashboard_api_logs

        Retrieves one or more dashboard_api_logs  # noqa: E501
        """
        pass

    def test_getdashboard_api_logs_item(self):
        """Test case for getdashboard_api_logs_item

        Retrieves a dashboard-api-logs document  # noqa: E501
        """
        pass

    def test_patchdashboard_api_logs_item(self):
        """Test case for patchdashboard_api_logs_item

        Updates a dashboard-api-logs document  # noqa: E501
        """
        pass

    def test_postdashboard_api_logs(self):
        """Test case for postdashboard_api_logs

        Stores one or more dashboard_api_logs.  # noqa: E501
        """
        pass

    def test_putdashboard_api_logs_item(self):
        """Test case for putdashboard_api_logs_item

        Replaces a dashboard-api-logs document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
