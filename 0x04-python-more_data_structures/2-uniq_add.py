#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not None:
        i = 0
        for j, element in enumerate(my_list):
            try:
                my_list.index(element, j + 1)
            except ValueError:
                i = i + int(element)
        return i
