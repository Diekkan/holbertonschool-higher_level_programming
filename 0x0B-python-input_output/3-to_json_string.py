#!/usr/bin/python3
"""
json string repr
"""


import json


def to_json_string(my_obj):
    """ returns the JSON repr of an object """
    rp = json.dumps(my_obj)
    return rp
