#!/usr/bin/python3
"""
append write def
"""


def append_write(filename="", text=""):
    """ appends text at the end of file"""
    with open(filename, 'a+') as f:
        chars = f.write(text)
    return chars
