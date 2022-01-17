#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number = 0
    for elem in range(x):
        try:
            print("{:d}".format(my_list[elem]), end = '')
            number += 1
        except (ValueError, TypeError):
            continue
    print()
    return (number)
