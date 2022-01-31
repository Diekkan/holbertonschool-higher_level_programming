#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """ Returns true if is instance
    or if is an instance of a class that inherited
    from.
    """
    if isinstance(obj, a_class)== True:
        return True
    else:
        return False
