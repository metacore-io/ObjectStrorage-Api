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


class Users(object):
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
        'address': 'str',
        'api_key': 'str',
        'email': 'str',
        'firstname': 'str',
        'is_active': 'bool',
        'lastname': 'str',
        'mobile_phone_number': 'int',
        'organization_id': 'str',
        'photo_url': 'str',
        'region_id': 'str',
        'role_id': 'str'
    }

    attribute_map = {
        'id': '_id',
        'address': 'address',
        'api_key': 'api_key',
        'email': 'email',
        'firstname': 'firstname',
        'is_active': 'isActive',
        'lastname': 'lastname',
        'mobile_phone_number': 'mobilePhoneNumber',
        'organization_id': 'organizationId',
        'photo_url': 'photo_url',
        'region_id': 'regionId',
        'role_id': 'roleId'
    }

    def __init__(self, id=None, address=None, api_key=None, email=None, firstname=None, is_active=True, lastname=None, mobile_phone_number=None, organization_id=None, photo_url=None, region_id=None, role_id='5'):  # noqa: E501
        """Users - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._address = None
        self._api_key = None
        self._email = None
        self._firstname = None
        self._is_active = None
        self._lastname = None
        self._mobile_phone_number = None
        self._organization_id = None
        self._photo_url = None
        self._region_id = None
        self._role_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if address is not None:
            self.address = address
        if api_key is not None:
            self.api_key = api_key
        self.email = email
        self.firstname = firstname
        if is_active is not None:
            self.is_active = is_active
        self.lastname = lastname
        if mobile_phone_number is not None:
            self.mobile_phone_number = mobile_phone_number
        self.organization_id = organization_id
        self.photo_url = photo_url
        if region_id is not None:
            self.region_id = region_id
        if role_id is not None:
            self.role_id = role_id

    @property
    def id(self):
        """Gets the id of this Users.  # noqa: E501


        :return: The id of this Users.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Users.


        :param id: The id of this Users.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def address(self):
        """Gets the address of this Users.  # noqa: E501


        :return: The address of this Users.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Users.


        :param address: The address of this Users.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def api_key(self):
        """Gets the api_key of this Users.  # noqa: E501


        :return: The api_key of this Users.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this Users.


        :param api_key: The api_key of this Users.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def email(self):
        """Gets the email of this Users.  # noqa: E501


        :return: The email of this Users.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Users.


        :param email: The email of this Users.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def firstname(self):
        """Gets the firstname of this Users.  # noqa: E501


        :return: The firstname of this Users.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this Users.


        :param firstname: The firstname of this Users.  # noqa: E501
        :type: str
        """
        if firstname is None:
            raise ValueError("Invalid value for `firstname`, must not be `None`")  # noqa: E501

        self._firstname = firstname

    @property
    def is_active(self):
        """Gets the is_active of this Users.  # noqa: E501


        :return: The is_active of this Users.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this Users.


        :param is_active: The is_active of this Users.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def lastname(self):
        """Gets the lastname of this Users.  # noqa: E501


        :return: The lastname of this Users.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this Users.


        :param lastname: The lastname of this Users.  # noqa: E501
        :type: str
        """
        if lastname is None:
            raise ValueError("Invalid value for `lastname`, must not be `None`")  # noqa: E501

        self._lastname = lastname

    @property
    def mobile_phone_number(self):
        """Gets the mobile_phone_number of this Users.  # noqa: E501


        :return: The mobile_phone_number of this Users.  # noqa: E501
        :rtype: int
        """
        return self._mobile_phone_number

    @mobile_phone_number.setter
    def mobile_phone_number(self, mobile_phone_number):
        """Sets the mobile_phone_number of this Users.


        :param mobile_phone_number: The mobile_phone_number of this Users.  # noqa: E501
        :type: int
        """

        self._mobile_phone_number = mobile_phone_number

    @property
    def organization_id(self):
        """Gets the organization_id of this Users.  # noqa: E501


        :return: The organization_id of this Users.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Users.


        :param organization_id: The organization_id of this Users.  # noqa: E501
        :type: str
        """
        if organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def photo_url(self):
        """Gets the photo_url of this Users.  # noqa: E501


        :return: The photo_url of this Users.  # noqa: E501
        :rtype: str
        """
        return self._photo_url

    @photo_url.setter
    def photo_url(self, photo_url):
        """Sets the photo_url of this Users.


        :param photo_url: The photo_url of this Users.  # noqa: E501
        :type: str
        """

        self._photo_url = photo_url

    @property
    def region_id(self):
        """Gets the region_id of this Users.  # noqa: E501


        :return: The region_id of this Users.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this Users.


        :param region_id: The region_id of this Users.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def role_id(self):
        """Gets the role_id of this Users.  # noqa: E501


        :return: The role_id of this Users.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this Users.


        :param role_id: The role_id of this Users.  # noqa: E501
        :type: str
        """

        self._role_id = role_id

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
        if not isinstance(other, Users):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
