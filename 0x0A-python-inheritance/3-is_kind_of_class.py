#!/usr/bin/python3
"""
is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """ Returns true if is instance
    or if is an instance of a class that inherited
    from.
    """
    return isinstance(obj, a_class)
