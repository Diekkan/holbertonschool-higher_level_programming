#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if letter == search else letter for letter in my_list]
