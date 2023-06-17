#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    else:
        denum = 0
        sum_j = 0
        for i in range(len(my_list)):
            j = my_list[i][0] * my_list[i][1]
            sum_j = sum_j + j
            denum = denum + my_list[i][1]
        return sum_j / denum
