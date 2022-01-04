def search_replace(my_list, search, replace):
    replacing = 0
    for i in range(my_list.count(search)):
        replacing = my_list.index(search, replacing)
        my_list[replacing] = replace
