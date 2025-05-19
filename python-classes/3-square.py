#!/usr/bin/python3
"""Define a square class."""


class Square:
    """
    A class that defines a square.
    """
    def __init__(self, size=0):
        """
        Initializes a new square.
        
        Args:
            size: the size of the square.
            
            Raises:
            TypeError: if size is not an interger.
            ValueError: if size is less thn 0
        """
        if not isinstance(self, int):
            raise TypeError("size must be an interger")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.
        
        Returns:
            the area of the square.
        """
        return self.__size ** 2
