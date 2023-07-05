#!/usr/bin/python3
"""
Queen Backtracking.
Usage: nqueens N
Where:
    nqueens is name of the file
    N is the number
"""


import sys
args = sys.argv

if len(args) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    if (int(args[1]) < 4):
        print("N must be at least 4")
        exit(1)
except ValueError:
        print("N must be a number")
        exit(1)
