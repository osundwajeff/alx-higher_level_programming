#!/usr/bin/python3
""" is kind of class """


def is_kind_of_class(obj, a_class):
    """ functions that returns True if
    object is an instance of, or if
    object is an istance of a class 
    that inherited from,specified class,
    otherwise False"""

    if obj isinstance(a_class):
        return True
    else:
        return False
