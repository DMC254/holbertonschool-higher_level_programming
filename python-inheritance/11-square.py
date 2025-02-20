#!/usr/bin/python3
"""
===================================
module with class BaseGeometry
===================================
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle that inherits BaseGeometry"""
    def __init__(self, size):
        """Method for initialized the attrubutes"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """rectangle area"""
        return self.__size * self.__size
