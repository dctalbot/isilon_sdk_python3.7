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

from isi_sdk_8_1_1.models.smb_openfile import SmbOpenfile  # noqa: F401,E501


class SmbOpenfiles(object):
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
        'openfiles': 'list[SmbOpenfile]',
        'resume': 'str',
        'total': 'int'
    }

    attribute_map = {
        'openfiles': 'openfiles',
        'resume': 'resume',
        'total': 'total'
    }

    def __init__(self, openfiles=None, resume=None, total=None):  # noqa: E501
        """SmbOpenfiles - a model defined in Swagger"""  # noqa: E501

        self._openfiles = None
        self._resume = None
        self._total = None
        self.discriminator = None

        if openfiles is not None:
            self.openfiles = openfiles
        if resume is not None:
            self.resume = resume
        if total is not None:
            self.total = total

    @property
    def openfiles(self):
        """Gets the openfiles of this SmbOpenfiles.  # noqa: E501


        :return: The openfiles of this SmbOpenfiles.  # noqa: E501
        :rtype: list[SmbOpenfile]
        """
        return self._openfiles

    @openfiles.setter
    def openfiles(self, openfiles):
        """Sets the openfiles of this SmbOpenfiles.


        :param openfiles: The openfiles of this SmbOpenfiles.  # noqa: E501
        :type: list[SmbOpenfile]
        """

        self._openfiles = openfiles

    @property
    def resume(self):
        """Gets the resume of this SmbOpenfiles.  # noqa: E501

        Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).  # noqa: E501

        :return: The resume of this SmbOpenfiles.  # noqa: E501
        :rtype: str
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this SmbOpenfiles.

        Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).  # noqa: E501

        :param resume: The resume of this SmbOpenfiles.  # noqa: E501
        :type: str
        """
        if resume is not None and len(resume) < 0:
            raise ValueError("Invalid value for `resume`, length must be greater than or equal to `0`")  # noqa: E501

        self._resume = resume

    @property
    def total(self):
        """Gets the total of this SmbOpenfiles.  # noqa: E501

        Total number of items available.  # noqa: E501

        :return: The total of this SmbOpenfiles.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this SmbOpenfiles.

        Total number of items available.  # noqa: E501

        :param total: The total of this SmbOpenfiles.  # noqa: E501
        :type: int
        """
        if total is not None and total > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if total is not None and total < 0:  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total = total

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
        if not isinstance(other, SmbOpenfiles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
