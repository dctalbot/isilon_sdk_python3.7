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

from isi_sdk_8_1_1.models.auth_access_access_item_file_group import AuthAccessAccessItemFileGroup  # noqa: F401,E501
from isi_sdk_8_1_1.models.auth_group_object_history_item import AuthGroupObjectHistoryItem  # noqa: F401,E501


class AuthGroupExtended(object):
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
        'dn': 'str',
        'dns_domain': 'str',
        'domain': 'str',
        'generated_gid': 'bool',
        'gid': 'AuthAccessAccessItemFileGroup',
        'id': 'str',
        'member_of': 'list[AuthAccessAccessItemFileGroup]',
        'name': 'str',
        'object_history': 'list[AuthGroupObjectHistoryItem]',
        'provider': 'str',
        'sam_account_name': 'str',
        'sid': 'AuthAccessAccessItemFileGroup',
        'type': 'str'
    }

    attribute_map = {
        'dn': 'dn',
        'dns_domain': 'dns_domain',
        'domain': 'domain',
        'generated_gid': 'generated_gid',
        'gid': 'gid',
        'id': 'id',
        'member_of': 'member_of',
        'name': 'name',
        'object_history': 'object_history',
        'provider': 'provider',
        'sam_account_name': 'sam_account_name',
        'sid': 'sid',
        'type': 'type'
    }

    def __init__(self, dn=None, dns_domain=None, domain=None, generated_gid=None, gid=None, id=None, member_of=None, name=None, object_history=None, provider=None, sam_account_name=None, sid=None, type=None):  # noqa: E501
        """AuthGroupExtended - a model defined in Swagger"""  # noqa: E501

        self._dn = None
        self._dns_domain = None
        self._domain = None
        self._generated_gid = None
        self._gid = None
        self._id = None
        self._member_of = None
        self._name = None
        self._object_history = None
        self._provider = None
        self._sam_account_name = None
        self._sid = None
        self._type = None
        self.discriminator = None

        if dn is not None:
            self.dn = dn
        if dns_domain is not None:
            self.dns_domain = dns_domain
        if domain is not None:
            self.domain = domain
        if generated_gid is not None:
            self.generated_gid = generated_gid
        if gid is not None:
            self.gid = gid
        self.id = id
        if member_of is not None:
            self.member_of = member_of
        self.name = name
        if object_history is not None:
            self.object_history = object_history
        if provider is not None:
            self.provider = provider
        if sam_account_name is not None:
            self.sam_account_name = sam_account_name
        if sid is not None:
            self.sid = sid
        self.type = type

    @property
    def dn(self):
        """Gets the dn of this AuthGroupExtended.  # noqa: E501


        :return: The dn of this AuthGroupExtended.  # noqa: E501
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """Sets the dn of this AuthGroupExtended.


        :param dn: The dn of this AuthGroupExtended.  # noqa: E501
        :type: str
        """
        if dn is not None and len(dn) > 255:
            raise ValueError("Invalid value for `dn`, length must be less than or equal to `255`")  # noqa: E501
        if dn is not None and len(dn) < 0:
            raise ValueError("Invalid value for `dn`, length must be greater than or equal to `0`")  # noqa: E501

        self._dn = dn

    @property
    def dns_domain(self):
        """Gets the dns_domain of this AuthGroupExtended.  # noqa: E501


        :return: The dns_domain of this AuthGroupExtended.  # noqa: E501
        :rtype: str
        """
        return self._dns_domain

    @dns_domain.setter
    def dns_domain(self, dns_domain):
        """Sets the dns_domain of this AuthGroupExtended.


        :param dns_domain: The dns_domain of this AuthGroupExtended.  # noqa: E501
        :type: str
        """
        if dns_domain is not None and len(dns_domain) > 255:
            raise ValueError("Invalid value for `dns_domain`, length must be less than or equal to `255`")  # noqa: E501
        if dns_domain is not None and len(dns_domain) < 0:
            raise ValueError("Invalid value for `dns_domain`, length must be greater than or equal to `0`")  # noqa: E501

        self._dns_domain = dns_domain

    @property
    def domain(self):
        """Gets the domain of this AuthGroupExtended.  # noqa: E501


        :return: The domain of this AuthGroupExtended.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AuthGroupExtended.


        :param domain: The domain of this AuthGroupExtended.  # noqa: E501
        :type: str
        """
        if domain is not None and len(domain) > 255:
            raise ValueError("Invalid value for `domain`, length must be less than or equal to `255`")  # noqa: E501
        if domain is not None and len(domain) < 0:
            raise ValueError("Invalid value for `domain`, length must be greater than or equal to `0`")  # noqa: E501

        self._domain = domain

    @property
    def generated_gid(self):
        """Gets the generated_gid of this AuthGroupExtended.  # noqa: E501

        If true, the GID was generated.  # noqa: E501

        :return: The generated_gid of this AuthGroupExtended.  # noqa: E501
        :rtype: bool
        """
        return self._generated_gid

    @generated_gid.setter
    def generated_gid(self, generated_gid):
        """Sets the generated_gid of this AuthGroupExtended.

        If true, the GID was generated.  # noqa: E501

        :param generated_gid: The generated_gid of this AuthGroupExtended.  # noqa: E501
        :type: bool
        """

        self._generated_gid = generated_gid

    @property
    def gid(self):
        """Gets the gid of this AuthGroupExtended.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The gid of this AuthGroupExtended.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this AuthGroupExtended.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param gid: The gid of this AuthGroupExtended.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._gid = gid

    @property
    def id(self):
        """Gets the id of this AuthGroupExtended.  # noqa: E501

        Specifies the user or group ID.  # noqa: E501

        :return: The id of this AuthGroupExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthGroupExtended.

        Specifies the user or group ID.  # noqa: E501

        :param id: The id of this AuthGroupExtended.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def member_of(self):
        """Gets the member_of of this AuthGroupExtended.  # noqa: E501


        :return: The member_of of this AuthGroupExtended.  # noqa: E501
        :rtype: list[AuthAccessAccessItemFileGroup]
        """
        return self._member_of

    @member_of.setter
    def member_of(self, member_of):
        """Sets the member_of of this AuthGroupExtended.


        :param member_of: The member_of of this AuthGroupExtended.  # noqa: E501
        :type: list[AuthAccessAccessItemFileGroup]
        """

        self._member_of = member_of

    @property
    def name(self):
        """Gets the name of this AuthGroupExtended.  # noqa: E501

        Specifies a user or group name.  # noqa: E501

        :return: The name of this AuthGroupExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthGroupExtended.

        Specifies a user or group name.  # noqa: E501

        :param name: The name of this AuthGroupExtended.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def object_history(self):
        """Gets the object_history of this AuthGroupExtended.  # noqa: E501


        :return: The object_history of this AuthGroupExtended.  # noqa: E501
        :rtype: list[AuthGroupObjectHistoryItem]
        """
        return self._object_history

    @object_history.setter
    def object_history(self, object_history):
        """Sets the object_history of this AuthGroupExtended.


        :param object_history: The object_history of this AuthGroupExtended.  # noqa: E501
        :type: list[AuthGroupObjectHistoryItem]
        """

        self._object_history = object_history

    @property
    def provider(self):
        """Gets the provider of this AuthGroupExtended.  # noqa: E501


        :return: The provider of this AuthGroupExtended.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this AuthGroupExtended.


        :param provider: The provider of this AuthGroupExtended.  # noqa: E501
        :type: str
        """
        if provider is not None and len(provider) > 255:
            raise ValueError("Invalid value for `provider`, length must be less than or equal to `255`")  # noqa: E501
        if provider is not None and len(provider) < 0:
            raise ValueError("Invalid value for `provider`, length must be greater than or equal to `0`")  # noqa: E501

        self._provider = provider

    @property
    def sam_account_name(self):
        """Gets the sam_account_name of this AuthGroupExtended.  # noqa: E501


        :return: The sam_account_name of this AuthGroupExtended.  # noqa: E501
        :rtype: str
        """
        return self._sam_account_name

    @sam_account_name.setter
    def sam_account_name(self, sam_account_name):
        """Sets the sam_account_name of this AuthGroupExtended.


        :param sam_account_name: The sam_account_name of this AuthGroupExtended.  # noqa: E501
        :type: str
        """
        if sam_account_name is not None and len(sam_account_name) > 255:
            raise ValueError("Invalid value for `sam_account_name`, length must be less than or equal to `255`")  # noqa: E501
        if sam_account_name is not None and len(sam_account_name) < 0:
            raise ValueError("Invalid value for `sam_account_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._sam_account_name = sam_account_name

    @property
    def sid(self):
        """Gets the sid of this AuthGroupExtended.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The sid of this AuthGroupExtended.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this AuthGroupExtended.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param sid: The sid of this AuthGroupExtended.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._sid = sid

    @property
    def type(self):
        """Gets the type of this AuthGroupExtended.  # noqa: E501

        Specifies the object type.  # noqa: E501

        :return: The type of this AuthGroupExtended.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AuthGroupExtended.

        Specifies the object type.  # noqa: E501

        :param type: The type of this AuthGroupExtended.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if type is not None and len(type) > 255:
            raise ValueError("Invalid value for `type`, length must be less than or equal to `255`")  # noqa: E501
        if type is not None and len(type) < 0:
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `0`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, AuthGroupExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
