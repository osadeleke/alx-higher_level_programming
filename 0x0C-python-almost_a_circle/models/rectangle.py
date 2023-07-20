#!/usr/bin/python3
"""
Module for Shapes
"""


class Base:
    """
    Base for other classes in the project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """
    Inherits from: Base
    Used for a Rectangle Object
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def return_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def return_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def return_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def return_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y
