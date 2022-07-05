#!/usr/bin/python3
""" class to JSON """


def class_to_json(obj):
    """ Retrieves the dictionary description of an object.
    Args:
        obj (any): An object whose attributes are to be retrieved.
    Returns:
        dict: The attributes of the object, otherwise None."""
    return obj.__dict__
