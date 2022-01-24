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
    """
    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >=0")
        self.__width = width
        self.__height = height

    # Returns height.
    @property
    def height(self):
        return self.__height
    # Returns width.
    @property
    def width(self):
        return self.__width
    # Sets height.
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    # Sets width.
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
