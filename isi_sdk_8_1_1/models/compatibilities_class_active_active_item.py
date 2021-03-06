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


class CompatibilitiesClassActiveActiveItem(object):
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
        'class_1': 'str',
        'class_2': 'str',
        'id': 'int'
    }

    attribute_map = {
        'class_1': 'class_1',
        'class_2': 'class_2',
        'id': 'id'
    }

    def __init__(self, class_1=None, class_2=None, id=None):  # noqa: E501
        """CompatibilitiesClassActiveActiveItem - a model defined in Swagger"""  # noqa: E501

        self._class_1 = None
        self._class_2 = None
        self._id = None
        self.discriminator = None

        self.class_1 = class_1
        self.class_2 = class_2
        self.id = id

    @property
    def class_1(self):
        """Gets the class_1 of this CompatibilitiesClassActiveActiveItem.  # noqa: E501

        The first class in an active compatibility  # noqa: E501

        :return: The class_1 of this CompatibilitiesClassActiveActiveItem.  # noqa: E501
        :rtype: str
        """
        return self._class_1

    @class_1.setter
    def class_1(self, class_1):
        """Sets the class_1 of this CompatibilitiesClassActiveActiveItem.

        The first class in an active compatibility  # noqa: E501

        :param class_1: The class_1 of this CompatibilitiesClassActiveActiveItem.  # noqa: E501
        :type: str
        """
        if class_1 is None:
            raise ValueError("Invalid value for `class_1`, must not be `None`")  # noqa: E501

        self._class_1 = class_1

    @property
    def class_2(self):
        """Gets the class_2 of this CompatibilitiesClassActiveActiveItem.  # noqa: E501

        The second class in an active compatibility  # noqa: E501

        :return: The class_2 of this CompatibilitiesClassActiveActiveItem.  # noqa: E501
        :rtype: str
        """
        return self._class_2

    @class_2.setter
    def class_2(self, class_2):
        """Sets the class_2 of this CompatibilitiesClassActiveActiveItem.

        The second class in an active compatibility  # noqa: E501

        :param class_2: The class_2 of this CompatibilitiesClassActiveActiveItem.  # noqa: E501
        :type: str
        """
        if class_2 is None:
            raise ValueError("Invalid value for `class_2`, must not be `None`")  # noqa: E501

        self._class_2 = class_2

    @property
    def id(self):
        """Gets the id of this CompatibilitiesClassActiveActiveItem.  # noqa: E501

        The id of this active compatibility  # noqa: E501

        :return: The id of this CompatibilitiesClassActiveActiveItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompatibilitiesClassActiveActiveItem.

        The id of this active compatibility  # noqa: E501

        :param id: The id of this CompatibilitiesClassActiveActiveItem.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, CompatibilitiesClassActiveActiveItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
