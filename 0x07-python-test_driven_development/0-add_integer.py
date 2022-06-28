#!/usr/bin/python3
"""
add_interger:
    Checks if inputs are (int)
    Returns sum of input
"""


def add_integer(a, b=98):
    """
    Checks if (int), else return sum
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
