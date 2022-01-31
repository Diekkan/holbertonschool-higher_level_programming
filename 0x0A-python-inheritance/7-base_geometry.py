#!/usr/bin/python3
"""
base geometry class
"""


class BaseGeometry:
    """ Geometry dash"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates integer """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
