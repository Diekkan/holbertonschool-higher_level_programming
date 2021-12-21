#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    absnumber = - number
    lastdigit = absnumber % 10
    lastdigit = - lastdigit
else:
    lastdigit = number % 10

if lastdigit > 5:
    print('Last digit of {:d} is {:d} and'.format(number, lastdigit), end='')
    print(' is greater than 5')
elif lastdigit < 6 and lastdigit != 0:
    print('Last digit of {:d} is {:d} and'.format(number, lastdigit), end='')
    print(' is less than 6 and not 0')
elif lastdigit == 0:
    print('Last digit of {:d} is {:d} and'.format(number, lastdigit), end='')
    print(' is 0')
