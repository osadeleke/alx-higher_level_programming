#!/usr/bin/python3
"""Defines a class named square with private instance"""


class Square:
    """Contains a private instance attribute"""
    def __init__(self, size=0):
        """Method to initialize size"""
        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size

    def area(self):
        """Method to return area of square"""
        return (self.__size ** 2)
