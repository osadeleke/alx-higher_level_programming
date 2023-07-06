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
                s = "matrix must be a matrix (list of lists)"
                n = " of integers/floats"
                raise TypeError(s + n)
        new_matrix.append(temp)
    return new_matrix
