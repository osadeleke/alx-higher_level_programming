#!/usr/bin/python3
"""
Text Indentation Module
"""


def text_indentation(text):
    """
    Text Indentation Method
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    lenght = len(text)
    i = 0
    while (i < lenght):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            if (i + 1) != lenght and text[i + 1] == ' ':
                print(text[i], end='\n\n')
                i += 2
        print(text[i], end='')
        i += 1
