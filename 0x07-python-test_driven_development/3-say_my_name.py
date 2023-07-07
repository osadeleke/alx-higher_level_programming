#!/usr/bin/python3
"""
Say My Name
"""


def say_my_name(first_name, last_name=""):
    """
    Method for say my name
    """
    if isinstance(first_name, str) == 0:
        raise TypeError("first_name must be a string")
    elif isinstance(last_name, str) == 0:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
