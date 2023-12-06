#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy_it = []
    for h in range(len(my_list)):
        if my_list[h] == search:
            copy_it.append(replace)
        else:
            copy_it.append(my_list[h])
    return copy_it
