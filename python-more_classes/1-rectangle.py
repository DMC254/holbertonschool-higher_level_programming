#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an interger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def heigth(self):
        return self.__heigth
    
    @heigth.setter
    def heigth(self, value):
        if not isinstance(value, int):
            raise TypeError("heigth must be an interger")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.heigth = value
