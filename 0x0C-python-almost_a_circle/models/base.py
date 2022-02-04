#!/usr/bin/python3
"""
Base class att and modules
"""


import json
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
        """ returns a json string """
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """ saves json representation to file """
        if list_objs:
            if type(cls) == Rectangle:
                openname = "Rectangle.json"
            else:
                openname = "Square.json"
            with open(openname, 'w+') as f:
                for i in range(len(list_objs)):
                    f.write(self.to_json_string(list_objs[i]))
        else:
            with open(openname, 'w+') as f:
                f.write(self.to_json_string(list()))
