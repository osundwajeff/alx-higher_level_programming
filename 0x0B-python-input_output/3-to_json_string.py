#!/usr/bin/python3
""" IO function"""
from json import JSONEncoder


def to_json_string(my_obj):
    """ creates JSON represenation
    Args:
        my_obj (any): object converted to JSON
    Returns:
        str: JSON representation of object, else
        exception is thrown. """
    return JSONEncoder().encode(my_obj)
