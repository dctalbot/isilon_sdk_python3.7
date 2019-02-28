# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 6
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ClusterOwner(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'company': 'str',
        'location': 'str',
        'primary_email': 'str',
        'primary_name': 'str',
        'primary_phone1': 'str',
        'primary_phone2': 'str',
        'secondary_email': 'str',
        'secondary_name': 'str',
        'secondary_phone1': 'str',
        'secondary_phone2': 'str'
    }

    attribute_map = {
        'company': 'company',
        'location': 'location',
        'primary_email': 'primary_email',
        'primary_name': 'primary_name',
        'primary_phone1': 'primary_phone1',
        'primary_phone2': 'primary_phone2',
        'secondary_email': 'secondary_email',
        'secondary_name': 'secondary_name',
        'secondary_phone1': 'secondary_phone1',
        'secondary_phone2': 'secondary_phone2'
    }

    def __init__(self, company=None, location=None, primary_email=None, primary_name=None, primary_phone1=None, primary_phone2=None, secondary_email=None, secondary_name=None, secondary_phone1=None, secondary_phone2=None):  # noqa: E501
        """ClusterOwner - a model defined in Swagger"""  # noqa: E501

        self._company = None
        self._location = None
        self._primary_email = None
        self._primary_name = None
        self._primary_phone1 = None
        self._primary_phone2 = None
        self._secondary_email = None
        self._secondary_name = None
        self._secondary_phone1 = None
        self._secondary_phone2 = None
        self.discriminator = None

        if company is not None:
            self.company = company
        if location is not None:
            self.location = location
        if primary_email is not None:
            self.primary_email = primary_email
        if primary_name is not None:
            self.primary_name = primary_name
        if primary_phone1 is not None:
            self.primary_phone1 = primary_phone1
        if primary_phone2 is not None:
            self.primary_phone2 = primary_phone2
        if secondary_email is not None:
            self.secondary_email = secondary_email
        if secondary_name is not None:
            self.secondary_name = secondary_name
        if secondary_phone1 is not None:
            self.secondary_phone1 = secondary_phone1
        if secondary_phone2 is not None:
            self.secondary_phone2 = secondary_phone2

    @property
    def company(self):
        """Gets the company of this ClusterOwner.  # noqa: E501

        Cluster owner company name.  # noqa: E501

        :return: The company of this ClusterOwner.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this ClusterOwner.

        Cluster owner company name.  # noqa: E501

        :param company: The company of this ClusterOwner.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def location(self):
        """Gets the location of this ClusterOwner.  # noqa: E501

        Cluster owner location.  # noqa: E501

        :return: The location of this ClusterOwner.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ClusterOwner.

        Cluster owner location.  # noqa: E501

        :param location: The location of this ClusterOwner.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def primary_email(self):
        """Gets the primary_email of this ClusterOwner.  # noqa: E501

        Cluster owner primary email address.  # noqa: E501

        :return: The primary_email of this ClusterOwner.  # noqa: E501
        :rtype: str
        """
        return self._primary_email

    @primary_email.setter
    def primary_email(self, primary_email):
        """Sets the primary_email of this ClusterOwner.

        Cluster owner primary email address.  # noqa: E501

        :param primary_email: The primary_email of this ClusterOwner.  # noqa: E501
        :type: str
        """

        self._primary_email = primary_email

    @property
    def primary_name(self):
        """Gets the primary_name of this ClusterOwner.  # noqa: E501

        Cluster owner primary contact name.  # noqa: E501

        :return: The primary_name of this ClusterOwner.  # noqa: E501
        :rtype: str
        """
        return self._primary_name

    @primary_name.setter
    def primary_name(self, primary_name):
        """Sets the primary_name of this ClusterOwner.

        Cluster owner primary contact name.  # noqa: E501

        :param primary_name: The primary_name of this ClusterOwner.  # noqa: E501
        :type: str
        """

        self._primary_name = primary_name

    @property
    def primary_phone1(self):
        """Gets the primary_phone1 of this ClusterOwner.  # noqa: E501

        Cluster owner primary contact phone number 1.  # noqa: E501

        :return: The primary_phone1 of this ClusterOwner.  # noqa: E501
        :rtype: str
        """
        return self._primary_phone1

    @primary_phone1.setter
    def primary_phone1(self, primary_phone1):
        """Sets the primary_phone1 of this ClusterOwner.

        Cluster owner primary contact phone number 1.  # noqa: E501

        :param primary_phone1: The primary_phone1 of this ClusterOwner.  # noqa: E501
        :type: str
        """

        self._primary_phone1 = primary_phone1

    @property
    def primary_phone2(self):
        """Gets the primary_phone2 of this ClusterOwner.  # noqa: E501

        Cluster owner primary contact phone number 2.  # noqa: E501

        :return: The primary_phone2 of this ClusterOwner.  # noqa: E501
        :rtype: str
        """
        return self._primary_phone2

    @primary_phone2.setter
    def primary_phone2(self, primary_phone2):
        """Sets the primary_phone2 of this ClusterOwner.

        Cluster owner primary contact phone number 2.  # noqa: E501

        :param primary_phone2: The primary_phone2 of this ClusterOwner.  # noqa: E501
        :type: str
        """

        self._primary_phone2 = primary_phone2

    @property
    def secondary_email(self):
        """Gets the secondary_email of this ClusterOwner.  # noqa: E501

        Cluster owner secondary email address.  # noqa: E501

        :return: The secondary_email of this ClusterOwner.  # noqa: E501
        :rtype: str
        """
        return self._secondary_email

    @secondary_email.setter
    def secondary_email(self, secondary_email):
        """Sets the secondary_email of this ClusterOwner.

        Cluster owner secondary email address.  # noqa: E501

        :param secondary_email: The secondary_email of this ClusterOwner.  # noqa: E501
        :type: str
        """

        self._secondary_email = secondary_email

    @property
    def secondary_name(self):
        """Gets the secondary_name of this ClusterOwner.  # noqa: E501

        Cluster owner secondary contact name.  # noqa: E501

        :return: The secondary_name of this ClusterOwner.  # noqa: E501
        :rtype: str
        """
        return self._secondary_name

    @secondary_name.setter
    def secondary_name(self, secondary_name):
        """Sets the secondary_name of this ClusterOwner.

        Cluster owner secondary contact name.  # noqa: E501

        :param secondary_name: The secondary_name of this ClusterOwner.  # noqa: E501
        :type: str
        """

        self._secondary_name = secondary_name

    @property
    def secondary_phone1(self):
        """Gets the secondary_phone1 of this ClusterOwner.  # noqa: E501

        Cluster owner secondary contact phone number 1.  # noqa: E501

        :return: The secondary_phone1 of this ClusterOwner.  # noqa: E501
        :rtype: str
        """
        return self._secondary_phone1

    @secondary_phone1.setter
    def secondary_phone1(self, secondary_phone1):
        """Sets the secondary_phone1 of this ClusterOwner.

        Cluster owner secondary contact phone number 1.  # noqa: E501

        :param secondary_phone1: The secondary_phone1 of this ClusterOwner.  # noqa: E501
        :type: str
        """

        self._secondary_phone1 = secondary_phone1

    @property
    def secondary_phone2(self):
        """Gets the secondary_phone2 of this ClusterOwner.  # noqa: E501

        Cluster owner secondary contact phone number 2.  # noqa: E501

        :return: The secondary_phone2 of this ClusterOwner.  # noqa: E501
        :rtype: str
        """
        return self._secondary_phone2

    @secondary_phone2.setter
    def secondary_phone2(self, secondary_phone2):
        """Sets the secondary_phone2 of this ClusterOwner.

        Cluster owner secondary contact phone number 2.  # noqa: E501

        :param secondary_phone2: The secondary_phone2 of this ClusterOwner.  # noqa: E501
        :type: str
        """

        self._secondary_phone2 = secondary_phone2

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, ClusterOwner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
