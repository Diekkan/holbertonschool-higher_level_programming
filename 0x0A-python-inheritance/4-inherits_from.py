#!/usr/bin/python3
"""
inherits_from
"""


def inherits_from(obj, a_class):
    """ Returns true if is instance
    of a class that inherited, false
    otherwise.
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
