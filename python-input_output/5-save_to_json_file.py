#!/usr/bin/python3
"""Define a function that writes an Object to a text file,
using a JSON representation."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using its JSON representation.

    Args:
        my_obj (object): The object to be written to the file.
        filename (str): The name of the file to.
    """

    with open(filename, 'w') as file:
        json.dumps(my_obj, file)
