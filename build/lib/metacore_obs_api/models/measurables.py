# coding: utf-8

"""
    Metacore IOT Object Storage API

    Metacore IOT Core Services  # noqa: E501

    The version of the OpenAPI document: 0.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Measurables(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'name': 'str',
        'unit': 'str',
        'unit_name': 'str'
    }

    attribute_map = {
        'id': '_id',
        'name': 'name',
        'unit': 'unit',
        'unit_name': 'unit_name'
    }

    def __init__(self, id=None, name=None, unit=None, unit_name=None):  # noqa: E501
        """Measurables - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._unit = None
        self._unit_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.unit = unit
        self.unit_name = unit_name

    @property
    def id(self):
        """Gets the id of this Measurables.  # noqa: E501


        :return: The id of this Measurables.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Measurables.


        :param id: The id of this Measurables.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Measurables.  # noqa: E501


        :return: The name of this Measurables.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Measurables.


        :param name: The name of this Measurables.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def unit(self):
        """Gets the unit of this Measurables.  # noqa: E501


        :return: The unit of this Measurables.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Measurables.


        :param unit: The unit of this Measurables.  # noqa: E501
        :type: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

    @property
    def unit_name(self):
        """Gets the unit_name of this Measurables.  # noqa: E501


        :return: The unit_name of this Measurables.  # noqa: E501
        :rtype: str
        """
        return self._unit_name

    @unit_name.setter
    def unit_name(self, unit_name):
        """Sets the unit_name of this Measurables.


        :param unit_name: The unit_name of this Measurables.  # noqa: E501
        :type: str
        """
        if unit_name is None:
            raise ValueError("Invalid value for `unit_name`, must not be `None`")  # noqa: E501

        self._unit_name = unit_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Measurables):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other