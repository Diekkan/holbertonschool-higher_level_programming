#!/usr/bin/python3

class MyInt(int):
    # Operators == and != are inverted
    def __eq__(self, other):
        if self is not other:
            return not NotImplemented

    def __ne__(self, other):
        if self.__eq__ == NotImplemented:
            return False
        else:
            return True
