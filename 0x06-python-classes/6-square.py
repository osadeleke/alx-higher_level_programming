#!/usr/bin/python3
"""Defines a class named square with private instance"""


class Square:
    """Contains a private instance attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """Method to initialize size"""
        self.__size = size
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position"""
        self.__position = value

    def area(self):
        """Method to return area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints the square using #"""
        if self.__size > 0:
            for i in range(self.__position[1]):
                print("")
            if self.__size != 0:
                for i in range(self.__size):
                    for j in range(self.__position[0]):
                        print(" ", end='')
                    for j in range(self.__size):
                        print("#", end='')
                    print()
            else:
                print()
        else:
            print()
