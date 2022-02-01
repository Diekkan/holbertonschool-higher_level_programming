#!/usr/bin/python3
"""
load from json file def
"""


import json


def load_from_json_file(filename):
    """ creates an object from a JSON file """
    with open(filename, 'r+') as f:
        x = json.load(f)
    return x
