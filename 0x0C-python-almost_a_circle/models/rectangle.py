#!/usr/bin/python3
"""
Rectangle Base class
"""


from models.base import Base


class Rectangle(Base):
    """A rectangle class that inherits from Base"""
    @property
    def height(self):
        """ gets height """
        return self.__height

    @property
    def width(self):
        """ gets width """
        return self.__width

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        """ Sets width """
        if isinstance(width, int):
            if width > 0:
                self.__width = width
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, height):
        """ Sets height """
        if isinstance(height, int):
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @x.setter
    def x(self, x):
        """ Sets y """
        if isinstance(x, int):
            if x >= 0:
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @y.setter
    def y(self, y):
        """ Sets y """
        if isinstance(y, int):
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instance method """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """ Area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """ Prints the rectangle """
        stry = "\n" * self.__y
        strx = " " * self.__x + "#" * self.__width
        print(stry, end='')
        for i in range(self.__height):
            print(strx)

    def __str__(self):
        """ str representation of rect """
        idd = "(" + str(self.id) + ") "
        xy = str(self.__x) + '/' + str(self.__y)
        wh = str(self.__width) + '/' + str(self.__height)
        return ("[Rectangle] " + idd + xy + " - " + wh)

    def update(self, *args, **kwargs):
        """ updates attributes """
        dictatt = {0: "id", 1: "width", 2: "height", 3: "x", 4: "y"}
        if args:
            if len(args) < 6:
                for i in range(len(args)):
                    setattr(self, dictatt[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ returns a dictionary with all attributes """
        dictionary = {'id': self.id, 'width': self.width}
        dictionary2 = {'height': self.height, 'x': self.x, 'y': self.y}
        dictionary.update(dictionary2)
        return dictionary
