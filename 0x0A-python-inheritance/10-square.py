#!/usr/bin/python3
"""
Module 10-square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """emptyclass"""

    def area(self):

        return self.__size * self.__size

    def integer_validator(self, name, value):
        """ validates value """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def __init__(self, size):
        """ ponele """

        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return ("[Rectangle] {:d}/{:d}".format(self.__size, self.__size))
