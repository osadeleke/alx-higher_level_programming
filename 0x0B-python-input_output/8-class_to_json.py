#!/usr/bin/python3
"""
Return: Dictionary descr. with simple data struct
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Returns Dict. Desc. with simple data struct
    for JSON serialization of an object
    """
    return obj.__dict__
