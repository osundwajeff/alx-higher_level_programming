#!/usr/bin/python3


"""Define class Square."""


class Square:
    """represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initilize square.
        Args:
            size (int):size of new square.
            position (int, int): position of new square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Gets the current size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """gets positions of square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if type(i) != int or i < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """get area of square."""
        area = self.__size * self.__size
        return (area)

    def my_print(self):
        """ prints in stdout the square with the character #."""
        if self.__size == 0:
            print("")

        nl = self.__position[1]
        ws = self.__position[0]

        for nline in range(nl):
            print()

        for row in range(size):
            print((' ' * ws) + ('#' * size))
