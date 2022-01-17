#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divlist = []
    for elem in range(list_length):
        try:
            value = my_list_1[elem] / my_list_2[elem]
            divlist.append(value)
        except ZeroDivisionError:
            print("division by 0")
            divlist.append(0)
        except TypeError:
            print("wrong type")
            divlist.append(0)
        except IndexError:
            print("out of range")
            divlist.append(0)
        finally:
            continue
    return (divlist)
