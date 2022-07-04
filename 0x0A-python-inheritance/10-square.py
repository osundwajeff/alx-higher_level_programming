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
