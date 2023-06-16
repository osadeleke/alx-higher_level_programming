#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:
        i = 0
        new_list = []
        for element in my_list:
            if my_list[i] % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
            i = i + 1
        return new_list
