#!/usr/bin/python3
"""
Defines a student
"""


class Student:
    """
    Defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dict_new = self.__dict__
        if attrs is None:
            return dict_new
        else:
            return {key: dict_new[key] for key in attrs if key in dict_new}
