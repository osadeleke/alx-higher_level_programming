#!/usr/bin/python3
"""
Module reads a text file (UTF-8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Function reads a text file (UTF-8) and prints it to stdout
    """
    with open(filename) as f:
        cont = f.read()
        print(cont, end='')
