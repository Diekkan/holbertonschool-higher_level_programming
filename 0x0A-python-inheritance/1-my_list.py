#!/usr/bin/python3
"""
1-my_list.py
"""


class MyList(list):
    """ A class that inherits from list. """
    def print_sorted(self):
        """ A method that sorts MyList elements. """
        print(sorted(self))
