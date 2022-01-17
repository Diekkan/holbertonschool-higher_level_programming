#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for element in range(x + 1):
        try:
            print("{}".format(my_list[element], end=''))
            count += 1
        except IndexError:
            break
    return (count)
