#!/usr/bin/python3
"""
my int class
"""


class MyInt(int):
    """ Operators == and != are inverted"""
    def __eq__(self, other):
        """ equal operation """
        if self is not other:
            return not NotImplemented

    def __ne__(self, other):
        """ not equal op """
        if self.__eq__ == NotImplemented:
            return False
        else:
            return True
