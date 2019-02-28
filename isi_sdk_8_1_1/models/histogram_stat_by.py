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

from isi_sdk_8_1_1.models.histogram_stat_by_breakout import HistogramStatByBreakout  # noqa: F401,E501


class HistogramStatBy(object):
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
        'begin_time': 'int',
        'breakouts': 'list[HistogramStatByBreakout]',
        'result_length': 'int'
    }

    attribute_map = {
        'begin_time': 'begin_time',
        'breakouts': 'breakouts',
        'result_length': 'result_length'
    }

    def __init__(self, begin_time=None, breakouts=None, result_length=None):  # noqa: E501
        """HistogramStatBy - a model defined in Swagger"""  # noqa: E501

        self._begin_time = None
        self._breakouts = None
        self._result_length = None
        self.discriminator = None

        self.begin_time = begin_time
        self.breakouts = breakouts
        self.result_length = result_length

    @property
    def begin_time(self):
        """Gets the begin_time of this HistogramStatBy.  # noqa: E501

        Unix Epoch time of start of results collection job.  # noqa: E501

        :return: The begin_time of this HistogramStatBy.  # noqa: E501
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this HistogramStatBy.

        Unix Epoch time of start of results collection job.  # noqa: E501

        :param begin_time: The begin_time of this HistogramStatBy.  # noqa: E501
        :type: int
        """
        if begin_time is None:
            raise ValueError("Invalid value for `begin_time`, must not be `None`")  # noqa: E501

        self._begin_time = begin_time

    @property
    def breakouts(self):
        """Gets the breakouts of this HistogramStatBy.  # noqa: E501

        Histogram breakout data according to breakout parameter.  # noqa: E501

        :return: The breakouts of this HistogramStatBy.  # noqa: E501
        :rtype: list[HistogramStatByBreakout]
        """
        return self._breakouts

    @breakouts.setter
    def breakouts(self, breakouts):
        """Sets the breakouts of this HistogramStatBy.

        Histogram breakout data according to breakout parameter.  # noqa: E501

        :param breakouts: The breakouts of this HistogramStatBy.  # noqa: E501
        :type: list[HistogramStatByBreakout]
        """
        if breakouts is None:
            raise ValueError("Invalid value for `breakouts`, must not be `None`")  # noqa: E501

        self._breakouts = breakouts

    @property
    def result_length(self):
        """Gets the result_length of this HistogramStatBy.  # noqa: E501

        Total length of the result list.  # noqa: E501

        :return: The result_length of this HistogramStatBy.  # noqa: E501
        :rtype: int
        """
        return self._result_length

    @result_length.setter
    def result_length(self, result_length):
        """Sets the result_length of this HistogramStatBy.

        Total length of the result list.  # noqa: E501

        :param result_length: The result_length of this HistogramStatBy.  # noqa: E501
        :type: int
        """
        if result_length is None:
            raise ValueError("Invalid value for `result_length`, must not be `None`")  # noqa: E501

        self._result_length = result_length

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
        if not isinstance(other, HistogramStatBy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
