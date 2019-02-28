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


class ClusterEmailSettings(object):
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
        'batch_mode': 'str',
        'mail_relay': 'str',
        'mail_sender': 'str',
        'mail_subject': 'str',
        'smtp_auth_passwd_set': 'bool',
        'smtp_auth_security': 'str',
        'smtp_auth_username': 'str',
        'smtp_port': 'int',
        'use_smtp_auth': 'bool',
        'user_template': 'str'
    }

    attribute_map = {
        'batch_mode': 'batch_mode',
        'mail_relay': 'mail_relay',
        'mail_sender': 'mail_sender',
        'mail_subject': 'mail_subject',
        'smtp_auth_passwd_set': 'smtp_auth_passwd_set',
        'smtp_auth_security': 'smtp_auth_security',
        'smtp_auth_username': 'smtp_auth_username',
        'smtp_port': 'smtp_port',
        'use_smtp_auth': 'use_smtp_auth',
        'user_template': 'user_template'
    }

    def __init__(self, batch_mode=None, mail_relay=None, mail_sender=None, mail_subject=None, smtp_auth_passwd_set=None, smtp_auth_security=None, smtp_auth_username=None, smtp_port=None, use_smtp_auth=None, user_template=None):  # noqa: E501
        """ClusterEmailSettings - a model defined in Swagger"""  # noqa: E501

        self._batch_mode = None
        self._mail_relay = None
        self._mail_sender = None
        self._mail_subject = None
        self._smtp_auth_passwd_set = None
        self._smtp_auth_security = None
        self._smtp_auth_username = None
        self._smtp_port = None
        self._use_smtp_auth = None
        self._user_template = None
        self.discriminator = None

        self.batch_mode = batch_mode
        self.mail_relay = mail_relay
        self.mail_sender = mail_sender
        self.mail_subject = mail_subject
        self.smtp_auth_passwd_set = smtp_auth_passwd_set
        self.smtp_auth_security = smtp_auth_security
        self.smtp_auth_username = smtp_auth_username
        self.smtp_port = smtp_port
        self.use_smtp_auth = use_smtp_auth
        if user_template is not None:
            self.user_template = user_template

    @property
    def batch_mode(self):
        """Gets the batch_mode of this ClusterEmailSettings.  # noqa: E501

        This setting determines how notifications will be batched together to be sent by email.  'none' means each notification will be sent separately.  'severity' means notifications of the same severity will be sent together.  'category' means notifications of the same category will be sent together.  'all' means all notifications will be batched together and sent in a single email.  # noqa: E501

        :return: The batch_mode of this ClusterEmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._batch_mode

    @batch_mode.setter
    def batch_mode(self, batch_mode):
        """Sets the batch_mode of this ClusterEmailSettings.

        This setting determines how notifications will be batched together to be sent by email.  'none' means each notification will be sent separately.  'severity' means notifications of the same severity will be sent together.  'category' means notifications of the same category will be sent together.  'all' means all notifications will be batched together and sent in a single email.  # noqa: E501

        :param batch_mode: The batch_mode of this ClusterEmailSettings.  # noqa: E501
        :type: str
        """
        if batch_mode is None:
            raise ValueError("Invalid value for `batch_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["all", "severity", "category", "none"]  # noqa: E501
        if batch_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `batch_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(batch_mode, allowed_values)
            )

        self._batch_mode = batch_mode

    @property
    def mail_relay(self):
        """Gets the mail_relay of this ClusterEmailSettings.  # noqa: E501

        The address of the SMTP server to be used for relaying the notification messages.  An SMTP server is required in order to send notifications.  If this string is empty, no emails will be sent.  # noqa: E501

        :return: The mail_relay of this ClusterEmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._mail_relay

    @mail_relay.setter
    def mail_relay(self, mail_relay):
        """Sets the mail_relay of this ClusterEmailSettings.

        The address of the SMTP server to be used for relaying the notification messages.  An SMTP server is required in order to send notifications.  If this string is empty, no emails will be sent.  # noqa: E501

        :param mail_relay: The mail_relay of this ClusterEmailSettings.  # noqa: E501
        :type: str
        """
        if mail_relay is None:
            raise ValueError("Invalid value for `mail_relay`, must not be `None`")  # noqa: E501

        self._mail_relay = mail_relay

    @property
    def mail_sender(self):
        """Gets the mail_sender of this ClusterEmailSettings.  # noqa: E501

        The full email address that will appear as the sender of notification messages.  # noqa: E501

        :return: The mail_sender of this ClusterEmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._mail_sender

    @mail_sender.setter
    def mail_sender(self, mail_sender):
        """Sets the mail_sender of this ClusterEmailSettings.

        The full email address that will appear as the sender of notification messages.  # noqa: E501

        :param mail_sender: The mail_sender of this ClusterEmailSettings.  # noqa: E501
        :type: str
        """
        if mail_sender is None:
            raise ValueError("Invalid value for `mail_sender`, must not be `None`")  # noqa: E501

        self._mail_sender = mail_sender

    @property
    def mail_subject(self):
        """Gets the mail_subject of this ClusterEmailSettings.  # noqa: E501

        The subject line for notification messages from this cluster.  # noqa: E501

        :return: The mail_subject of this ClusterEmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._mail_subject

    @mail_subject.setter
    def mail_subject(self, mail_subject):
        """Sets the mail_subject of this ClusterEmailSettings.

        The subject line for notification messages from this cluster.  # noqa: E501

        :param mail_subject: The mail_subject of this ClusterEmailSettings.  # noqa: E501
        :type: str
        """
        if mail_subject is None:
            raise ValueError("Invalid value for `mail_subject`, must not be `None`")  # noqa: E501

        self._mail_subject = mail_subject

    @property
    def smtp_auth_passwd_set(self):
        """Gets the smtp_auth_passwd_set of this ClusterEmailSettings.  # noqa: E501

        Indicates if an SMTP authentication password is set.  # noqa: E501

        :return: The smtp_auth_passwd_set of this ClusterEmailSettings.  # noqa: E501
        :rtype: bool
        """
        return self._smtp_auth_passwd_set

    @smtp_auth_passwd_set.setter
    def smtp_auth_passwd_set(self, smtp_auth_passwd_set):
        """Sets the smtp_auth_passwd_set of this ClusterEmailSettings.

        Indicates if an SMTP authentication password is set.  # noqa: E501

        :param smtp_auth_passwd_set: The smtp_auth_passwd_set of this ClusterEmailSettings.  # noqa: E501
        :type: bool
        """
        if smtp_auth_passwd_set is None:
            raise ValueError("Invalid value for `smtp_auth_passwd_set`, must not be `None`")  # noqa: E501

        self._smtp_auth_passwd_set = smtp_auth_passwd_set

    @property
    def smtp_auth_security(self):
        """Gets the smtp_auth_security of this ClusterEmailSettings.  # noqa: E501

        The type of secure communication protocol to use if SMTP is being used.  If 'none', plain text will be used, if 'starttls', the encrypted STARTTLS protocol will be used.  # noqa: E501

        :return: The smtp_auth_security of this ClusterEmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._smtp_auth_security

    @smtp_auth_security.setter
    def smtp_auth_security(self, smtp_auth_security):
        """Sets the smtp_auth_security of this ClusterEmailSettings.

        The type of secure communication protocol to use if SMTP is being used.  If 'none', plain text will be used, if 'starttls', the encrypted STARTTLS protocol will be used.  # noqa: E501

        :param smtp_auth_security: The smtp_auth_security of this ClusterEmailSettings.  # noqa: E501
        :type: str
        """
        if smtp_auth_security is None:
            raise ValueError("Invalid value for `smtp_auth_security`, must not be `None`")  # noqa: E501
        allowed_values = ["none", "starttls"]  # noqa: E501
        if smtp_auth_security not in allowed_values:
            raise ValueError(
                "Invalid value for `smtp_auth_security` ({0}), must be one of {1}"  # noqa: E501
                .format(smtp_auth_security, allowed_values)
            )

        self._smtp_auth_security = smtp_auth_security

    @property
    def smtp_auth_username(self):
        """Gets the smtp_auth_username of this ClusterEmailSettings.  # noqa: E501

        Username to authenticate with if SMTP authentication is being used.  # noqa: E501

        :return: The smtp_auth_username of this ClusterEmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._smtp_auth_username

    @smtp_auth_username.setter
    def smtp_auth_username(self, smtp_auth_username):
        """Sets the smtp_auth_username of this ClusterEmailSettings.

        Username to authenticate with if SMTP authentication is being used.  # noqa: E501

        :param smtp_auth_username: The smtp_auth_username of this ClusterEmailSettings.  # noqa: E501
        :type: str
        """
        if smtp_auth_username is None:
            raise ValueError("Invalid value for `smtp_auth_username`, must not be `None`")  # noqa: E501

        self._smtp_auth_username = smtp_auth_username

    @property
    def smtp_port(self):
        """Gets the smtp_port of this ClusterEmailSettings.  # noqa: E501

        The port on the SMTP server to be used for relaying the notification messages.    # noqa: E501

        :return: The smtp_port of this ClusterEmailSettings.  # noqa: E501
        :rtype: int
        """
        return self._smtp_port

    @smtp_port.setter
    def smtp_port(self, smtp_port):
        """Sets the smtp_port of this ClusterEmailSettings.

        The port on the SMTP server to be used for relaying the notification messages.    # noqa: E501

        :param smtp_port: The smtp_port of this ClusterEmailSettings.  # noqa: E501
        :type: int
        """
        if smtp_port is None:
            raise ValueError("Invalid value for `smtp_port`, must not be `None`")  # noqa: E501

        self._smtp_port = smtp_port

    @property
    def use_smtp_auth(self):
        """Gets the use_smtp_auth of this ClusterEmailSettings.  # noqa: E501

        If true, this cluster will send SMTP authentication credentials to the SMTP relay server in order to send its notification emails.  If false, the cluster will attempt to send its notification emails without authentication.  # noqa: E501

        :return: The use_smtp_auth of this ClusterEmailSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_smtp_auth

    @use_smtp_auth.setter
    def use_smtp_auth(self, use_smtp_auth):
        """Sets the use_smtp_auth of this ClusterEmailSettings.

        If true, this cluster will send SMTP authentication credentials to the SMTP relay server in order to send its notification emails.  If false, the cluster will attempt to send its notification emails without authentication.  # noqa: E501

        :param use_smtp_auth: The use_smtp_auth of this ClusterEmailSettings.  # noqa: E501
        :type: bool
        """
        if use_smtp_auth is None:
            raise ValueError("Invalid value for `use_smtp_auth`, must not be `None`")  # noqa: E501

        self._use_smtp_auth = use_smtp_auth

    @property
    def user_template(self):
        """Gets the user_template of this ClusterEmailSettings.  # noqa: E501

        Location of a custom template file that can be used to specify the layout of the notification emails.  # noqa: E501

        :return: The user_template of this ClusterEmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._user_template

    @user_template.setter
    def user_template(self, user_template):
        """Sets the user_template of this ClusterEmailSettings.

        Location of a custom template file that can be used to specify the layout of the notification emails.  # noqa: E501

        :param user_template: The user_template of this ClusterEmailSettings.  # noqa: E501
        :type: str
        """

        self._user_template = user_template

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
        if not isinstance(other, ClusterEmailSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
