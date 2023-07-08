#!/usr/bin/python3
"""
Text Indentation Module
"""


def text_indentation(text):
    """
    Text Indentation Method.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    lenght = len(text)
    i = 0
    while (i < lenght):
        # if text[i] == '.' or text[i] == '?' or text[i] == ':':
        if text[i] in (".", "?", ":"):
            if (i + 1) != lenght:
                s = text[i + 1]
                if (s != '.' and s != '?' and s != ':'):
                    print(text[i], end='\n\n')
                    if s == ' ':
                        i += 2
                    if s != ' ':
                        i += 1
        else:
            print(text[i], end='')
            i += 1
