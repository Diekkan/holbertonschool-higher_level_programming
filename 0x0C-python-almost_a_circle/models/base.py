#!/usr/bin/python3
"""
Base class att and modules
"""


import json
import os


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instance method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as op:
            json = []
            if list_objs is None:
                return op.write(cls.to_json_string(None))
            for items in list_objs:
                json.append(items.to_dictionary())

            return op.write(cls.to_json_string(json))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation of obj"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates a new instance with attributes prev set"""
        if cls.__name__ == 'Square':
            dummy = cls(2)
        if cls.__name__ == 'Rectangle':
            dummy = cls(2, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ list of instances """
        if os.path.isfile(cls.__name__ + '.json') is False:
            return []
        with open(cls.__name__ + '.json', encoding='utf-8') as op:
            list_instances = []
            json_instances = cls.from_json_string(op.read())

            for items in json_instances:
                list_instances.append(cls.create(**items))

            return list_instances
