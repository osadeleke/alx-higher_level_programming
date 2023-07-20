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

    def width(self):
        """Public Width Getter
        """
        return self.__width

    def width(self, width):
        """Public Width setter
        """
        self.__width = width

    def height(self):
        """Public Height Getter
        """
        return self.__height

    def height(self, height):
        """Public Width setter
        """
        self.__height = height

    def x(self):
        """Public x Getter
        """
        return self.__x

    def x(self, x):
        """Public Width setter
        """
        self.__x = x

    def y(self):
        """Public y Getter
        """
        return self.__y

    def y(self, y):
        """Public Width setter
        """
        self.__y = y
