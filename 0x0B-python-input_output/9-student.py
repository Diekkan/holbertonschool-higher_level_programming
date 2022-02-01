#!/usr/bin/python3
"""
class Student
"""


class Student:
    """ A student class"""
    def __init__(self, first_name, last_name, age):
        """ instance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns class to a json"""
        return obj.__dict__
