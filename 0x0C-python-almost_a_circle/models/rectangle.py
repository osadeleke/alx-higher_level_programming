#!/usr/bin/python3
"""
Module for Shapes
"""
from .base import Base


class Rectangle(Base):
    """
    Inherits from: Base
    Used for a Rectangle Object
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Public Width Getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Public Width setter
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Public Height Getter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Public Width setter
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Public x Getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """Public Width setter
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Public y Getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """Public Width setter
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Return: Area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints rectangle instance to stdout
        """
        for space_y in range(self.__y):
            print()
        for i in range(self.__height):
            for space_x in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        for i, arg in enumerate(args):
            if i == 0:
                self.id = args[0]
            elif i == 1:
                self.__width = args[1]
            elif i == 2:
                self.__height = args[2]
            elif i == 3:
                self.__x = args[3]
            elif i == 4:
                self.__y = args[4]
        if kwargs:
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]

    def to_dictionary(self):
        """
        Returns dictionary representation of a Rectangle
        """
        fin_dict = {}
        fin_dict["width"] = self.width
        fin_dict["height"] = self.height
        fin_dict["id"] = self.id
        fin_dict["x"] = self.x
        fin_dict["y"] = self.y
        return fin_dict

    def __str__(self):
        paone = "[Rectangle] ({}) {}".format(self.id, self.__x)
        patwo = "/{} - {}/{}".format(self.__y, self.__width, self.__height)
        return paone + patwo
