#!/usr/bin/python3
"""
A module that defines a rectangle
"""


class Rectangle:
    """
    This is a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for Height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        method to calculate area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        calculate perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        img = ""
        for i in range(self.__height):
            for j in range(self.__width):
                img = img + str(self.print_symbol)
            if i != (self.__height - 1):
                img = img + "\n"
        return img

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
