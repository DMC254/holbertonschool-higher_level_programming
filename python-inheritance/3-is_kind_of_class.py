#!/usr/bin/python3
"""
===================================
module with method is_kind_of_class
===================================
"""


def is_kind_of_class(obj, a_class):
    """Method that returns True if the object is an instance or inherited instance of a class"""

    return isinstance(obj, a_class)
