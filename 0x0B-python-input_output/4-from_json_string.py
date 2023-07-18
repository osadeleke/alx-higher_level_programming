#!/usr/bin/python3
"""
Return: object (py data structure) respresented by JSON string
"""
import json


def from_json_string(my_str):
    """
    Return: object represented by JSON string
    """
    return json.loads(my_str)
