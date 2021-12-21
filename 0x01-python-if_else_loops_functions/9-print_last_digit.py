#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        absdig = (-number) % 10
        lastdig = absdig
    else:
        lastdig = number % 10
    print("{:d}".format(lastdig), end='')
    return(lastdig)
