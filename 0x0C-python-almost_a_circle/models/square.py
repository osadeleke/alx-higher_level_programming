#!/usr/bin/python3
"""
Module for Shapes
"""
from .rectange import Rectangle


class Square(Rectangle):
    """
    Class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor
        """
        self.__size = size
        width = self.__size
        height = self.__size
        super().__init__(width, height, x, y, id)
        self.width = self.__size
        self.height = self.__size
        self.x = x
        self.y = y

    @property
    def size(self):
        """
        Getter for Size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Setter for size
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        To update shape
        """
        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            if i == 1:
                self.__size = arg
                self.width = self.__size
            if i == 2:
                self.x = arg
            if i == 3:
                self.y = arg
        if kwargs:
            if "size" in kwargs:
                self.__size = kwargs["size"]
                self.width = self.__size
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        """
        String representation for Object
        """
        paone = "[Square] ({}) {}/".format(self.id, self.x)
        patwo = "{} - {}".format(self.y, self.width)
        return paone + patwo
