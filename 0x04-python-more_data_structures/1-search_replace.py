#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        new_list = []
        for element in my_list:
            new_list.append(element)
        i = -1
        while True:
            try:
                i = my_list.index(search, i + 1)
                new_list[i] = replace
            except ValueError:
                return new_list
