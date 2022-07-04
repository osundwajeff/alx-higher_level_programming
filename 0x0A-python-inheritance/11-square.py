#!/usr/bin/python3
""" Square inherits from Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A Square """
    def __init__(self, size):
        """ initialize a new Square.
        Args:
            size (int): size of new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ area of  a square """

        return self.__size * self.__size

    def __str__(self):
        """ Return the print() and str() representation of a Square """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
