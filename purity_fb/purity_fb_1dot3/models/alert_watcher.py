# coding: utf-8

"""
    Purity//FB REST Client

    Client for Purity//FB REST API (1.0 - 1.3), developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.3
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AlertWatcher(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'name': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'enabled': 'enabled'
    }

    def __init__(self, name=None, enabled=None):
        """
        AlertWatcher - a model defined in Swagger
        """

        self._name = None
        self._enabled = None

        if name is not None:
          self.name = name
        if enabled is not None:
          self.enabled = enabled

    @property
    def name(self):
        """
        Gets the name of this AlertWatcher.
        name of the object (e.g., a file system or snapshot)

        :return: The name of this AlertWatcher.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AlertWatcher.
        name of the object (e.g., a file system or snapshot)

        :param name: The name of this AlertWatcher.
        :type: str
        """

        self._name = name

    @property
    def enabled(self):
        """
        Gets the enabled of this AlertWatcher.
        is email notification enabled? Default true when adding a new watcher

        :return: The enabled of this AlertWatcher.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this AlertWatcher.
        is email notification enabled? Default true when adding a new watcher

        :param enabled: The enabled of this AlertWatcher.
        :type: bool
        """

        self._enabled = enabled

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AlertWatcher):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
