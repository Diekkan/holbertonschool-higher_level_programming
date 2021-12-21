#!/usr/bin/python3
def uppercase(str):
    for aux in str:
        aux = ord(aux)
        if aux > 96 and aux < 123:
            aux = aux - 32
        print("{:c}".format(aux), end='')
    print()
