def uniq_add(my_list=[]):
    add = 0
    for i in range(len(my_list)):
        if my_list.count(my_list[i]) == 1:
            add += my_list[i]
        else:
            my_list.pop(i)
            i = i - 1
    return(add)
