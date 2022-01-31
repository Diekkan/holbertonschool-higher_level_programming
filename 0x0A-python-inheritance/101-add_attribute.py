#!/usr/bin/python3
"""
add attribute
"""

def add_attribute(cls, name, value):
    """ can we add an attribute?"""
    if not hasattr(cls, "__dict__"):
        raise TypeError("can't add new attribute")

    cls.name = value
