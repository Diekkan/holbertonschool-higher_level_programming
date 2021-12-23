#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    listname = dir(hidden_4)
    for i in range(len(listname)):
        toprint = listname[i]
        if toprint[:2] != "__":
            print(toprint)
        i += 1
