# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models import *  # NOQA
from swagger_server import util


class Tag(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    attribute_map = {
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, id=None, name=None):  # noqa: E501
        """Tag - a model defined in OpenAPI

        :param id: The id of this Tag.  # noqa: E501
        :type id: int
        :param name: The name of this Tag.  # noqa: E501
        :type name: str
        """

        
        self._id = id
        self._name = name



        self.openapi_types = {
            'id': int,
            'name': str
        }

    @classmethod
    def from_dict(cls, dikt) -> 'Tag':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Tag of this Tag.  # noqa: E501
        :rtype: Tag
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Tag.


        :return: The id of this Tag.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Tag.


        :param id: The id of this Tag.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Tag.


        :return: The name of this Tag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tag.


        :param name: The name of this Tag.
        :type name: str
        """

        self._name = name
