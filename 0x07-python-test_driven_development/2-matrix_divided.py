#!/usr/bin/python3
""" a function that divides all elements of a matrix
    Returns a new matrix
"""


def matrix_divided(matrix, div):
    """ Divide all elements of a matrix by "div"
    check if list is int/float
    check if list in matrix are same size
    """
    mess0 = "matrix must be a matrix (list of lists) of integers/floats"
    mess1 = "Each row of the matrix must have the same size"
    new_matrix = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lst in matrix:
        if len(lst) != len(matrix[0]):
            raise TypeError(mess1)
        inner_list = []
        for itm in lst:
            if not isinstance(itm, (int, float)):
                raise TypeError(mess0)
            else:
                inner_list.append(round(itm / div, 2))
        new_matrix.append(inner_list)

    return new_matrix
