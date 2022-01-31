#!/usr/bin/python3
"""
geometry class and rectangle
"""

class BaseGeometry:
    """Geometry dash."""
    def area(self):
        """ area not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class, BaseGeometry subclass. """
    def __init__(self, width, height):
        """ instanciation"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area defined """
        return self.__width * self.__height

    def __str__(self):
        """str representation defined """
        string = "[Rectangle] "
        return (string + str(self.__width) + '/' + str(self.__height))
