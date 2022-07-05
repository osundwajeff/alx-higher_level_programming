#!/usr/bin/python3
""" IO functions """
from json import JSONDecoder


def from_json_string(my_str):
    """ Creates object from its JSON representation.
    Args:
        my_str (str): A JSON representation of an object.
    Returns:
        any: object corresponding to the given JSON string,
        else an exception is thrown."""
    return JSONDecoder().decode(my_str)
