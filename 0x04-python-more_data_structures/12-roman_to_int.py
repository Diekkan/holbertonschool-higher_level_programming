#!/usr/bin/python3
def roman_to_int(roman_string):

    result = 0
    x = 0

    romans = {
           "I": 1,
           "V": 5,
           "X": 10,
           "L": 50,
           "C": 100,
           "D": 500,
           "M": 1000,
           "IV": 4,
           "IX": 9,
           "XL": 40,
           "XC": 90,
           "CD": 400,
           "CM": 900,
           }

    if type(roman_string) is not str:
        return 0

    while x < len(roman_string):
        if x+1 < len(roman_string) and roman_string[x:x+2] in romans:
            result += romans[roman_string[x:x+2]]
            x += 2
        else:
            result += romans[roman_string[x]]
            x += 1

    return result