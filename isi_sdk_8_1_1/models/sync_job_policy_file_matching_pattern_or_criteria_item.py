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

from isi_sdk_8_1_1.models.sync_job_policy_file_matching_pattern_or_criteria_item_and_criteria_item import SyncJobPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem  # noqa: F401,E501


class SyncJobPolicyFileMatchingPatternOrCriteriaItem(object):
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
        'and_criteria': 'list[SyncJobPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem]'
    }

    attribute_map = {
        'and_criteria': 'and_criteria'
    }

    def __init__(self, and_criteria=None):  # noqa: E501
        """SyncJobPolicyFileMatchingPatternOrCriteriaItem - a model defined in Swagger"""  # noqa: E501

        self._and_criteria = None
        self.discriminator = None

        if and_criteria is not None:
            self.and_criteria = and_criteria

    @property
    def and_criteria(self):
        """Gets the and_criteria of this SyncJobPolicyFileMatchingPatternOrCriteriaItem.  # noqa: E501

        An array containing individual file criterion objects each describing one criterion.  These are logically AND'ed together to form a set of criteria.  # noqa: E501

        :return: The and_criteria of this SyncJobPolicyFileMatchingPatternOrCriteriaItem.  # noqa: E501
        :rtype: list[SyncJobPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem]
        """
        return self._and_criteria

    @and_criteria.setter
    def and_criteria(self, and_criteria):
        """Sets the and_criteria of this SyncJobPolicyFileMatchingPatternOrCriteriaItem.

        An array containing individual file criterion objects each describing one criterion.  These are logically AND'ed together to form a set of criteria.  # noqa: E501

        :param and_criteria: The and_criteria of this SyncJobPolicyFileMatchingPatternOrCriteriaItem.  # noqa: E501
        :type: list[SyncJobPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem]
        """

        self._and_criteria = and_criteria

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
        if not isinstance(other, SyncJobPolicyFileMatchingPatternOrCriteriaItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
