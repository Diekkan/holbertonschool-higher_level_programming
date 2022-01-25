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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        # Rectangle instance initialization.
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            rectangle += ((str(self.print_symbol) * self.width) + "\n")
        return rectangle

    def __repr__(self):
        # Returns representation of instance object Rectangle.
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        # When instance deleted, do the following:
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        # Compares rectangles.
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
