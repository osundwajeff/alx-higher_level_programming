#!/usr/bin/python3


"""Define class Square"""


class Square:
    """represent a square"""
    def __init__(self, size=0):
        """initilize square
        Args: size (int):size of new square"""
        self.__size = size

    @property
    def size(self):
        """Gets the current size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size"""
        if not isintance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """get area of square"""
        area = self.__size * self.__size
        return (area)
