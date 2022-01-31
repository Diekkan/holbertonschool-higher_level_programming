#!/usr/bin/python3


class MyList(list):
    # A class that inherits from list.
    def print_sorted(self):
        # A method that sorts MyList elements.
        print(sorted(self))
