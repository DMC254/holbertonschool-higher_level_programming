#!/usr/bin/python3
"""
================================
module with method is_same_class
================================
"""


def is_same_class(obj, a_class):
    """Method that returns True if the object is
    exactly an instance of a class"""

    return type(obj) is a_class
