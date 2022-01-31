#!/usr/bin/python3
"""
2-is_same_class
"""


def is_same_class(obj, a_class):
    """ Returns true if is instance, otherwise False. """
    if type(obj) == a_class:
        return True
    else:
        return False
