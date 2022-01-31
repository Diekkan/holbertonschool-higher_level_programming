#!/usr/bin/python3
"""
Base, Rectangle and Square
"""


class BaseGeometry:
    """ Geometry dash. """
    def area(self):
        """ defines area not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an integer value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle class, BaseGeometryDASH subclass. """
    def __init__(self, width, height):
        """ instanciation """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string repr"""
        string = "[Rectangle] "
        return (string + str(self.__width) + '/' + str(self.__height))


class Square(Rectangle):
    """Square class """
    def __init__(self, size):
        """ instanciation """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area of an square """
        return self.__size ** 2

