#!/usr/bin/python3
def common_elements(set_1, set_2):
    s1 = list(set_1)
    s2 = list(set_2)
    repeated = s1 + s2
    for i in range(len(repeated)):
        if repeated.count(repeated[i]) > 1:
            commonset = set(repeated[i])
    return(commonset)
