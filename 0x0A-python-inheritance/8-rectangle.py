#!/usr/bin/python3
"""
Geometry and Rectangle classes
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class, BaseGeometry subclass."""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ validates value """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def __init__(self, width, height):
        """creating an instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
