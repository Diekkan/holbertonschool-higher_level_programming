#!/usr/bin/python3
"""
Class square 
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle """
    @property
    def size(self):
        """ Size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """ Size setter """
        self.width = size
        self.height = size

    def __init__(self, size, x=0, y=0, id=None):
        """ Instancing a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string repr of square """
        sq = "[Square] "
        sq += "(" + str(self.id) + ") "
        sq += str(self.x) + "/" + str(self.y)
        return (sq + " " + str(self.width))
   
    def update(self, *args, **kwargs):
        """ updates attributes """
        dictatt = {0:"id", 1:"size", 2:"x", 3:"y"}
        if args:
            if len(args) < 5:
                for i in range(len(args)):
                    setattr(self, dictatt[i], args[i])
        else:
            for key in kwargs:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ returns a dictionary with all attributes """
        return self.__dict__


