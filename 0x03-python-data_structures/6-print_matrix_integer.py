#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        j = 0
        for row in matrix:
            i = 0
            for element in row:
                print("{:d} ".format(matrix[j][i]), end="")
                i = i + 1
            print()
            j = j + 1
