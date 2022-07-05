#!/usr/bin/python3
""" class Rectangle that inherits from class BaseGeomtery. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Initialize a Rectangle.
        Args:
            width:(int): width of new Rectangle
            height: (int): height of new Rectangle.
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ return area of Rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Return the print() and str() representation of Rectangle """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
