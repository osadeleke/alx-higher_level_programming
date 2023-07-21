#!/usr/bin/python3
"""
Module for Shapes
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for Size
        """
        return self.width

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
                self.width = arg
            if i == 2:
                self.x = arg
            if i == 3:
                self.y = arg
        if kwargs:
            if "size" in kwargs:
                self.width = kwargs["size"]
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Return: a dictionary returning value
        """
        new_dict = {}
        new_dict["id"] = self.id
        new_dict["size"] = self.width
        new_dict["x"] = self.x
        new_dict["y"] = self.y
        return new_dict

    def __str__(self):
        """
        String representation for Object
        """
        paone = "[Square] ({}) {}/".format(self.id, self.x)
        patwo = "{} - {}".format(self.y, self.width)
        return paone + patwo
