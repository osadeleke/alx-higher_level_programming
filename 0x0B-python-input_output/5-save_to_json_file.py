#!/usr/bin/python3
"""
Writes Object to text file using JSON rep
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes object to text files using JSON rep
    """
    with open(filename, 'w', encoding='utf-8') as f:
        cont = json.dumps(my_obj)
        f.write(cont)
