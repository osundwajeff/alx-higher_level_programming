#!/usr/bin/python3
"""class BaseGeometry """


class BaseGeometry:
    """ function area """

    def area(self):
        """ not implemented """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ function that validates if value is integer.
        Args:
            name(str): name
            value(int): value
        Raise:
            TypeError and ValueError
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
