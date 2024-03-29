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
from metacore_obs_api.api.measurables_api import MeasurablesApi  # noqa: E501
from metacore_obs_api.rest import ApiException


class TestMeasurablesApi(unittest.TestCase):
    """MeasurablesApi unit test stubs"""

    def setUp(self):
        self.api = metacore_obs_api.api.measurables_api.MeasurablesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_getmeasurables(self):
        """Test case for getmeasurables

        Retrieves one or more measurables  # noqa: E501
        """
        pass

    def test_getmeasurables_item(self):
        """Test case for getmeasurables_item

        Retrieves a measurables document  # noqa: E501
        """
        pass

    def test_patchmeasurables_item(self):
        """Test case for patchmeasurables_item

        Updates a measurables document  # noqa: E501
        """
        pass

    def test_postmeasurables(self):
        """Test case for postmeasurables

        Stores one or more measurables.  # noqa: E501
        """
        pass

    def test_putmeasurables_item(self):
        """Test case for putmeasurables_item

        Replaces a measurables document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
