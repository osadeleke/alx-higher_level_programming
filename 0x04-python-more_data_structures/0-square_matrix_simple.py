#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_list = []
        for row in matrix:
            if row is not None:
                row_list = []
                for element in row:
                    row_list.append(element ** 2)
                new_list.append(row_list)
        return new_list
    else:
        return matrix
