#!/usr/bin/python3
""" class Rectangle that inherits from class BaseGeomtery. """
BaseGeometry = __import__('7-base_geomtery').BaseGeometry


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
