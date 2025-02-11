#!/usr/bin/python3
"""Define a function that returns the JSON representation of an object."""


import json


def to_json_string(my_obj):
    """Return the JSON representation of an object.

    Args:
        my_obj (object): The object to return a JSON representation of.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dump(my_obj)
