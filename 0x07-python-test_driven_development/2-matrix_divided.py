#!/usr/bin/python3
"""

Module divides an element by a number indicated

"""


def matrix_divided(matrix, div):
    if isinstance(div, int) == 0 and isinstance(div, float) == 0:
        raise TypeError("div must be a number")
    new_matrix = []
    for row in matrix:
        temp = []
        for element in row:
            if isinstance(element, int) or isinstance(element, float):
                temp.append(round((element / div), 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_matrix.append(temp)
    return new_matrix
