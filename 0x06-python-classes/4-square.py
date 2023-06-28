#!/usr/bin/python3
"""Defines a class named square with private instance"""


class Square:
    """Contains a private instance attribute"""
    def __init__(self, size=0):
        """Method to initialize size"""
        self.__size = size

    @property
    def size(self):
        """Getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = value

    def area(self):
        """Method to return area of square"""
        return (self.__size ** 2)
