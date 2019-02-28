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


class SnapshotSnapshotsSummarySummary(object):
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
        'active_count': 'int',
        'active_size': 'int',
        'aliases_count': 'int',
        'count': 'int',
        'deleting_count': 'int',
        'deleting_size': 'int',
        'shadow_bytes': 'int',
        'size': 'int'
    }

    attribute_map = {
        'active_count': 'active_count',
        'active_size': 'active_size',
        'aliases_count': 'aliases_count',
        'count': 'count',
        'deleting_count': 'deleting_count',
        'deleting_size': 'deleting_size',
        'shadow_bytes': 'shadow_bytes',
        'size': 'size'
    }

    def __init__(self, active_count=None, active_size=None, aliases_count=None, count=None, deleting_count=None, deleting_size=None, shadow_bytes=None, size=None):  # noqa: E501
        """SnapshotSnapshotsSummarySummary - a model defined in Swagger"""  # noqa: E501

        self._active_count = None
        self._active_size = None
        self._aliases_count = None
        self._count = None
        self._deleting_count = None
        self._deleting_size = None
        self._shadow_bytes = None
        self._size = None
        self.discriminator = None

        self.active_count = active_count
        self.active_size = active_size
        self.aliases_count = aliases_count
        self.count = count
        self.deleting_count = deleting_count
        self.deleting_size = deleting_size
        self.shadow_bytes = shadow_bytes
        self.size = size

    @property
    def active_count(self):
        """Gets the active_count of this SnapshotSnapshotsSummarySummary.  # noqa: E501

        Total number of active snapshots.  # noqa: E501

        :return: The active_count of this SnapshotSnapshotsSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._active_count

    @active_count.setter
    def active_count(self, active_count):
        """Sets the active_count of this SnapshotSnapshotsSummarySummary.

        Total number of active snapshots.  # noqa: E501

        :param active_count: The active_count of this SnapshotSnapshotsSummarySummary.  # noqa: E501
        :type: int
        """
        if active_count is None:
            raise ValueError("Invalid value for `active_count`, must not be `None`")  # noqa: E501

        self._active_count = active_count

    @property
    def active_size(self):
        """Gets the active_size of this SnapshotSnapshotsSummarySummary.  # noqa: E501

        Sum of sizes of active snapshots.  # noqa: E501

        :return: The active_size of this SnapshotSnapshotsSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._active_size

    @active_size.setter
    def active_size(self, active_size):
        """Sets the active_size of this SnapshotSnapshotsSummarySummary.

        Sum of sizes of active snapshots.  # noqa: E501

        :param active_size: The active_size of this SnapshotSnapshotsSummarySummary.  # noqa: E501
        :type: int
        """
        if active_size is None:
            raise ValueError("Invalid value for `active_size`, must not be `None`")  # noqa: E501

        self._active_size = active_size

    @property
    def aliases_count(self):
        """Gets the aliases_count of this SnapshotSnapshotsSummarySummary.  # noqa: E501

        Total number of snapshot aliases.  # noqa: E501

        :return: The aliases_count of this SnapshotSnapshotsSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._aliases_count

    @aliases_count.setter
    def aliases_count(self, aliases_count):
        """Sets the aliases_count of this SnapshotSnapshotsSummarySummary.

        Total number of snapshot aliases.  # noqa: E501

        :param aliases_count: The aliases_count of this SnapshotSnapshotsSummarySummary.  # noqa: E501
        :type: int
        """
        if aliases_count is None:
            raise ValueError("Invalid value for `aliases_count`, must not be `None`")  # noqa: E501

        self._aliases_count = aliases_count

    @property
    def count(self):
        """Gets the count of this SnapshotSnapshotsSummarySummary.  # noqa: E501

        Total number of snapshots.  # noqa: E501

        :return: The count of this SnapshotSnapshotsSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this SnapshotSnapshotsSummarySummary.

        Total number of snapshots.  # noqa: E501

        :param count: The count of this SnapshotSnapshotsSummarySummary.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def deleting_count(self):
        """Gets the deleting_count of this SnapshotSnapshotsSummarySummary.  # noqa: E501

        Total number of delete-pending snapshots.  # noqa: E501

        :return: The deleting_count of this SnapshotSnapshotsSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._deleting_count

    @deleting_count.setter
    def deleting_count(self, deleting_count):
        """Sets the deleting_count of this SnapshotSnapshotsSummarySummary.

        Total number of delete-pending snapshots.  # noqa: E501

        :param deleting_count: The deleting_count of this SnapshotSnapshotsSummarySummary.  # noqa: E501
        :type: int
        """
        if deleting_count is None:
            raise ValueError("Invalid value for `deleting_count`, must not be `None`")  # noqa: E501

        self._deleting_count = deleting_count

    @property
    def deleting_size(self):
        """Gets the deleting_size of this SnapshotSnapshotsSummarySummary.  # noqa: E501

        Sum of sizes of delete-pending snapshots.  # noqa: E501

        :return: The deleting_size of this SnapshotSnapshotsSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._deleting_size

    @deleting_size.setter
    def deleting_size(self, deleting_size):
        """Sets the deleting_size of this SnapshotSnapshotsSummarySummary.

        Sum of sizes of delete-pending snapshots.  # noqa: E501

        :param deleting_size: The deleting_size of this SnapshotSnapshotsSummarySummary.  # noqa: E501
        :type: int
        """
        if deleting_size is None:
            raise ValueError("Invalid value for `deleting_size`, must not be `None`")  # noqa: E501

        self._deleting_size = deleting_size

    @property
    def shadow_bytes(self):
        """Gets the shadow_bytes of this SnapshotSnapshotsSummarySummary.  # noqa: E501

        Sum of shadow bytes of all snapshots.  # noqa: E501

        :return: The shadow_bytes of this SnapshotSnapshotsSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._shadow_bytes

    @shadow_bytes.setter
    def shadow_bytes(self, shadow_bytes):
        """Sets the shadow_bytes of this SnapshotSnapshotsSummarySummary.

        Sum of shadow bytes of all snapshots.  # noqa: E501

        :param shadow_bytes: The shadow_bytes of this SnapshotSnapshotsSummarySummary.  # noqa: E501
        :type: int
        """
        if shadow_bytes is None:
            raise ValueError("Invalid value for `shadow_bytes`, must not be `None`")  # noqa: E501

        self._shadow_bytes = shadow_bytes

    @property
    def size(self):
        """Gets the size of this SnapshotSnapshotsSummarySummary.  # noqa: E501

        Sum of sizes in bytes of all snapshots.  # noqa: E501

        :return: The size of this SnapshotSnapshotsSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SnapshotSnapshotsSummarySummary.

        Sum of sizes in bytes of all snapshots.  # noqa: E501

        :param size: The size of this SnapshotSnapshotsSummarySummary.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

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
        if not isinstance(other, SnapshotSnapshotsSummarySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
