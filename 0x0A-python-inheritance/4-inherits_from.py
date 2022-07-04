#!/usr/bin/python3
""" inherits from """


def inherits_from(obj, a_class):
    """ function that returns True
    if object is an instance of a
    class that inherited (directly or indirectly)
    from specified class
    otherwise False
    Args:
        obj: object to check
        a_class: class to match type of obj
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
