#!/usr/bin/python3
"""0. My first square
Attributes:
"""


class Square:
    """Class name: square"""
    def __init__(self, size=0):
        """init method
        Args:
            size: size of square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
            
