#!/usr/bin/python3
""" A rectangle class...

    Attributes:
    width - width of the rectangle
    height - height of the rectangle
"""


class Rectangle:
    """ Rectangle class

        Attributes:
        width & height
        Methods:
        width & height retrievers
        and setters.
        area and perimeter operations.
    """
    def __init__(self, width=0, height=0):
        # Rectangle instance initialization.
        self.width = width
        self.height = height

    @property
    def height(self):
        # Returns height.
        return self.__height

    @property
    def width(self):
        # Returns width.
        return self.__width

    @height.setter
    def height(self, value):
        # Sets height value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        # Sets width value.
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        # Returns the area of a rectangle instance.
        return (self.__height * self.__width)

    def perimeter(self):
        # Returns the perimeter of a rectangle instance.
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        # Returns what to be printed on each instance.
        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle
        for i in range(self.height):
            rectangle += (("#" * self.width) + "\n")
        return rectangle
