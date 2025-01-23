#!/usr/bin/python3
"""A module that adds two integers

This module performs the addition operation betwee two numbers,
these numbers can be intergers or floats.

"""


def add_integer(a, b=98):
    """Adds two numbers
    
    Performs the addition between two numbers.
    
    Args:
        a (:obj:`int, float`): The first two numbers.
        b (:obj:`int, float`, optional): The second number.
        
    Returns:
        int: The result of the addition.
        
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an interger')
    
    if type(b) not in (int, float):
        raise TypeError('b must be an interger')
    
    a = convert_to_int(a)
    b = convert_to_int(b)
    return a + b

def convert_to_int(num):
    """Cast the data type of num parameter

    Convert a float number to a integer number

    Args:
        num (:obj:`int, float`): The number to cast.

    Returns:
        int: The number casted to integer.

    """
    if type(num) is float:
        num = int(num)
        return num
    
    return num
