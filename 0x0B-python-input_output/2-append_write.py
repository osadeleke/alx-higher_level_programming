#!/usr/bin/python3
"""
Appends string to end of file.
Returns the numbers of chars added.
"""


def append_write(filename="", text=""):
    """
    Appends string to end of file.
    Return: numbers of chars added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
