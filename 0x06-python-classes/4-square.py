#!/usr/bin/python3


"""Define class Square"""


class Square:
    """represent a square"""

    def __init__(self, size=0):
        """initilize square
        Args: size (int): size of new square"""
        self.__size = size

    @property
    def size(self):
        """Gets the current size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """get area of square"""
        return (self.__size * self.__size)
