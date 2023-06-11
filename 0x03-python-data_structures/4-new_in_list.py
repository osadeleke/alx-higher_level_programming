#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        n_list = my_list
        return n_list
    else:
        n_list = []
        for i in range(len(my_list)):
            if i == idx:
                n_list = n_list + [element]
            else:
                n_list = n_list + [my_list[i]]
        return n_list

