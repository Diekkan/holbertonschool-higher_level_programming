#!/usr/bin/python3
"""
read file def
"""


def read_file(filename=""):
    """ reads a file """
    with open(filename) as f:
        print(f.read())
