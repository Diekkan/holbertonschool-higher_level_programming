#!/usr/bin/python3
"""
from string to obj def
"""


import json


def from_json_string(my_str):
    """ returns the object deserialized """
    x = json.loads(my_str)
    return x
