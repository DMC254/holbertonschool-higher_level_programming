#!/usr/bin/python3
"""
===================================
module with method inherits_from
===================================
"""


def inherits_from(obj, a_class):
    """Method that returns True if the object is an instance of a class that inherited from the specified class"""

    return issubclass(type(obj), a_class)
