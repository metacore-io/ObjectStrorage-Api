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


class ShownWidgetSettings(object):
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
        'organization_id': 'str',
        'role_id': 'str',
        'widget_list': 'list[str]'
    }

    attribute_map = {
        'id': '_id',
        'name': 'name',
        'organization_id': 'organizationId',
        'role_id': 'roleId',
        'widget_list': 'widgetList'
    }

    def __init__(self, id=None, name=None, organization_id=None, role_id=None, widget_list=None):  # noqa: E501
        """ShownWidgetSettings - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._organization_id = None
        self._role_id = None
        self._widget_list = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.organization_id = organization_id
        self.role_id = role_id
        if widget_list is not None:
            self.widget_list = widget_list

    @property
    def id(self):
        """Gets the id of this ShownWidgetSettings.  # noqa: E501


        :return: The id of this ShownWidgetSettings.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShownWidgetSettings.


        :param id: The id of this ShownWidgetSettings.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ShownWidgetSettings.  # noqa: E501


        :return: The name of this ShownWidgetSettings.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShownWidgetSettings.


        :param name: The name of this ShownWidgetSettings.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def organization_id(self):
        """Gets the organization_id of this ShownWidgetSettings.  # noqa: E501


        :return: The organization_id of this ShownWidgetSettings.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ShownWidgetSettings.


        :param organization_id: The organization_id of this ShownWidgetSettings.  # noqa: E501
        :type: str
        """
        if organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def role_id(self):
        """Gets the role_id of this ShownWidgetSettings.  # noqa: E501


        :return: The role_id of this ShownWidgetSettings.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this ShownWidgetSettings.


        :param role_id: The role_id of this ShownWidgetSettings.  # noqa: E501
        :type: str
        """
        if role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

    @property
    def widget_list(self):
        """Gets the widget_list of this ShownWidgetSettings.  # noqa: E501


        :return: The widget_list of this ShownWidgetSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._widget_list

    @widget_list.setter
    def widget_list(self, widget_list):
        """Sets the widget_list of this ShownWidgetSettings.


        :param widget_list: The widget_list of this ShownWidgetSettings.  # noqa: E501
        :type: list[str]
        """

        self._widget_list = widget_list

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
        if not isinstance(other, ShownWidgetSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
