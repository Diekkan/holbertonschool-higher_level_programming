#!/usr/bin/python3


def add_attribute(cls, name, value):
    if not hasattr(cls, "__dict__"):
        raise TypeError("can't add new attribute")

    cls.name = value
