#!/usr/bin/python3


"""Define class Square"""


class Square:
    """represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initilize square
        Args: size (int):size of new square
        Args: position (int, int): position of new square"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """gets positions of square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """get area of square"""
        area = self.__size * self.__size
        return (area)

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return

    [print("") for i in range(0, self.__position[1])]
    for i in range(0, self.__size):
        [print("#", end="") for j in range(self.__size)]
        [print("#", end="") for k in range(self.__size)]
        print("")
