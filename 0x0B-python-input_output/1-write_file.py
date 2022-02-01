#!/usr/bin/python3
"""
write file def
"""


def write_file(filename="", text=""):
    """ writes into a file, overwrites if exist, if not makes new file"""
    with open(filename, 'w+') as f:
        chars = f.write(text)
    return chars
