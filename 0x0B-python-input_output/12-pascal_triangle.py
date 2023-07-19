#!/usr/bin/python3
"""
List of List of integers representing pascal's triangle
"""


def pascal_triangle(n):
    """
    List of list of integers rep pascal's triangle
    """
    if n <= 0:
        main_list = []
    elif n == 1:
        main_list = [[1]]
    elif n == 2:
        main_list = [[1, 1]]
    else:
        main_list = [[1], [1, 1]]
        for i in range(3, n+1):
            m_list = main_list[i - 2]
            tmp_list = [1]
            k = 0
            for j in range(1, i-1):
                tmp_list.append(m_list[k] + m_list[k+1])
                k = k + 1
            tmp_list.append(1)
            main_list.append(tmp_list)
    return main_list
