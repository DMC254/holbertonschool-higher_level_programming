#!/usr/bin/python3
"""Defines a class"""

BaseGeometry = __import__('7base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """Define a class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, heigth):
        """
        Initializes a Rectangle with a given width and height.
        
        Args:
            width (int): width of Rectangle.
            heigth (int): heigth of the Rectangle.
        
        Raises:
            TypeError: if either width or heigth is not an interger.
            ValueError: if either width or heigth is not greater than 0.
        """

        super().interger_validator("width", width)
        super().interger_validator("heigth", heigth)
        self.__width = width
        self.__heigth = heigth
