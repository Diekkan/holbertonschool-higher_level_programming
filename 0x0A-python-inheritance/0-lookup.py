#!/usr/bin/python3


def lookup(obj):
    """ A function that returns the list of available
    attributes and methods of an object.
    """
    everything = []

    everything = dir(obj)
    return everything
