#!/usr/bin/python3
"""Define a function is_same_class."""


def is_same_class(obj, a_class):
    """
    Return True if obj is instance of given class.
    Otherwise, return False.
    Args:
        obj: Object to check.
        a_class: Given class.
    Returns:
        True: if obj is an exact instance of a_class.
        False: if obj is not exacly an instance.
    """
    return type(obj) is a_class
