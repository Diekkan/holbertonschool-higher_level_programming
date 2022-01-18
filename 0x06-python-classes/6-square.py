#!/usr/bin/python3
"""0. My first square
Attributes:
"""


class Square:
    """Class name: Square
    Attributes:
        area: area of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """init method
        Args:
            size: size of square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2
    """gets size"""
    @property
    def size(self):
        return self.__size
    """gets position"""
    @property
    def position(self):
        return self.__position
    """sets size"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """sets position"""
    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()
