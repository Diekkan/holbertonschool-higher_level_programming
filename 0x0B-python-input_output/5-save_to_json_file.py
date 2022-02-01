#!/usr/bin/python3
"""
save to json file def
"""


import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a text file, using JSON"""
    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
