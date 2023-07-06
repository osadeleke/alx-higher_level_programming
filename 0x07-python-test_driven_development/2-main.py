#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8],
    [10, 11, 13]
]
print(matrix_divided(matrix, 3))
print(matrix)
