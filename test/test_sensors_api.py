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
from metacore_obs_api.api.sensors_api import SensorsApi  # noqa: E501
from metacore_obs_api.rest import ApiException


class TestSensorsApi(unittest.TestCase):
    """SensorsApi unit test stubs"""

    def setUp(self):
        self.api = metacore_obs_api.api.sensors_api.SensorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_getsensors(self):
        """Test case for getsensors

        Retrieves one or more sensors  # noqa: E501
        """
        pass

    def test_getsensors_item(self):
        """Test case for getsensors_item

        Retrieves a sensors document  # noqa: E501
        """
        pass

    def test_patchsensors_item(self):
        """Test case for patchsensors_item

        Updates a sensors document  # noqa: E501
        """
        pass

    def test_postsensors(self):
        """Test case for postsensors

        Stores one or more sensors.  # noqa: E501
        """
        pass

    def test_putsensors_item(self):
        """Test case for putsensors_item

        Replaces a sensors document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
