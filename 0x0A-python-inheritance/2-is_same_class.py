#!/usr/bin/python3
""" is object same """


def is_same_class(obj, a_class):
    """ fucntion that tests if object is exactly an
    instance of a specified class """

    if type(obj) == a_class:
        return True
    else:
        return False
